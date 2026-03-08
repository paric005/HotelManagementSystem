from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # ========================= VARIABLES =========================

        self.var_ref = StringVar()
        self.var_ref.set(str(random.randint(1000, 9999)))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()

        # ========================= TITLE =========================

        lbl_title = Label(
            self.root,
            text="HOTEL MANAGEMENT SYSTEM",
            font=("times new roman", 40, "bold"),
            bg="black",
            fg="gold",
            bd=4,
            relief=RIDGE
        )
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ========================= LEFT FRAME =========================

        labelframeleft = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Customer Details",
            font=("times new roman", 12, "bold"),
            padx=2
        )
        labelframeleft.place(x=5, y=50, width=425, height=495)

        # ========================= FORM =========================

        labels = [
            ("Customer Ref", self.var_ref),
            ("Customer Name", self.var_cust_name),
            ("Mother Name", self.var_mother),
            ("Gender", self.var_gender),
            ("PostCode", self.var_post),
            ("Mobile", self.var_mobile),
            ("Email", self.var_email),
            ("Nationality", self.var_nationality),
            ("Id Proof", self.var_id_proof),
            ("Id Number", self.var_id_number),
            ("Address", self.var_address)
        ]

        for i, (text, var) in enumerate(labels):
            Label(
                labelframeleft,
                text=text,
                font=("arial", 12, "bold"),
                padx=2,
                pady=6
            ).grid(row=i, column=0, sticky=W)

            ttk.Entry(
                labelframeleft,
                font=("arial", 13, "bold"),
                textvariable=var,
                width=29
            ).grid(row=i, column=1)

        # ========================= BUTTONS =========================

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        Button(btn_frame, text="Add", command=self.add_data,
               font=("arial", 11, "bold"), bg="black", fg="gold", width=8).grid(row=0, column=0)

        Button(btn_frame, text="Update", command=self.update,
               font=("arial", 11, "bold"), bg="black", fg="gold", width=8).grid(row=0, column=1)

        Button(btn_frame, text="Delete", command=self.mDelete,
               font=("arial", 11, "bold"), bg="black", fg="gold", width=8).grid(row=0, column=2)

        Button(btn_frame, text="Reset", command=self.reset,
               font=("arial", 11, "bold"), bg="black", fg="gold", width=8).grid(row=0, column=3)

        # ========================= TABLE FRAME =========================

        Table_Frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="View Details And Search System",
            font=("arial", 12, "bold")
        )
        Table_Frame.place(x=435, y=50, width=860, height=490)

        self.serch_var = StringVar()
        self.txt_serch = StringVar()

        ttk.Combobox(
            Table_Frame,
            textvariable=self.serch_var,
            values=("Mobile", "Ref"),
            state="readonly",
            width=24
        ).grid(row=0, column=1)

        ttk.Entry(
            Table_Frame,
            textvariable=self.txt_serch,
            width=24,
            font=("arial", 13, "bold")
        ).grid(row=0, column=2)
        
        

        btnSearch = Button(Table_Frame, text="Search",command = self.search, font=("arial",11,"bold"), bg="black", fg="gold", width=10);
        btnSearch.grid(row=0, column=3, padx=1)
        btnShowAll = Button(Table_Frame, text="Show All", font=("arial",11,"bold"),command = self.fetch_data, bg="black", fg="gold", width=10);
        btnShowAll.grid(row=0, column=4, padx=1)


        # ========================= TABLE =========================

        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(
            details_table,
            columns=(
                "ref", "name", "mother", "gender", "post", "mobile",
                "email", "nationality", "idproof", "idnumber", "address"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        headings = [
            "Ref", "Name", "Mother", "Gender", "Post", "Mobile",
            "Email", "Nationality", "IdProof", "IdNumber", "Address"
        ]

        for col, head in zip(self.Cust_Details_Table["columns"], headings):
            self.Cust_Details_Table.heading(col, text=head)
            self.Cust_Details_Table.column(col, width=100)

        self.Cust_Details_Table["show"] = "headings"
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)

        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)

        # Load Data
        self.fetch_data()

    # ========================= DB CONNECTION =========================

    def connect_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="paric@005",
            database="management"
        )

    # ========================= ADD =========================

    def add_data(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Mobile is required")
            return

        try:
            conn = self.connect_db()
            cur = conn.cursor()

            cur.execute(
                "INSERT INTO customer VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get()
                )
            )

            conn.commit()
            conn.close()

            self.fetch_data()
            messagebox.showinfo("Success", "Customer Added")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ========================= FETCH =========================

    def fetch_data(self):
        try:
            conn = self.connect_db()
            cur = conn.cursor()

            cur.execute("SELECT * FROM customer")
            rows = cur.fetchall()

            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())

            for row in rows:
                self.Cust_Details_Table.insert("", END, values=row)

            conn.close()

        except Exception as e:
            messagebox.showerror("DB Error", str(e))

    # ========================= SELECT =========================

    def get_cursor(self, event=""):
        row = self.Cust_Details_Table.item(
            self.Cust_Details_Table.focus()
        )["values"]

        if not row:
            return

        (
            self.var_ref,
            self.var_cust_name,
            self.var_mother,
            self.var_gender,
            self.var_post,
            self.var_mobile,
            self.var_email,
            self.var_nationality,
            self.var_id_proof,
            self.var_id_number,
            self.var_address
        )

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])

    # ========================= UPDATE =========================

    def update(self):
        try:
            conn = self.connect_db()
            cur = conn.cursor()

            cur.execute("""
                UPDATE customer SET
                Name=%s, Mother=%s, Gender=%s, PostCode=%s,
                Mobile=%s, Email=%s, Nationality=%s,
                Idproof=%s, idnumber=%s, Address=%s
                WHERE Ref=%s
            """, (
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get(),
                self.var_ref.get()
            ))

            conn.commit()
            conn.close()

            self.fetch_data()
            messagebox.showinfo("Success", "Updated Successfully")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ========================= DELETE =========================

    def mDelete(self):
        if not messagebox.askyesno("Confirm", "Delete this record?"):
            return

        try:
            conn = self.connect_db()
            cur = conn.cursor()

            cur.execute("DELETE FROM customer WHERE Ref=%s",
                        (self.var_ref.get(),))

            conn.commit()
            conn.close()

            self.fetch_data()
            messagebox.showinfo("Success", "Deleted")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ========================= RESET =========================

    def reset(self):
        self.var_ref.set(str(random.randint(1000, 9999)))
        self.var_cust_name.set("")
        self.var_mother.set("")
        self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("")
        self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_address.set("")
    
    def search(self):
        if self.serch_var.get() == "" or self.txt_serch.get() == "":
            messagebox.showerror("Error", "Please select search option and enter value")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="paric@005",
                database="management"
            )

            my_cursor = conn.cursor()

            # Map UI values to DB column names
            column_map = {
                "Mobile": "mobile",
                "Ref": "ref"
            }

            col = column_map.get(self.serch_var.get())

            query = f"SELECT * FROM customer WHERE {col} LIKE %s"
            value = ("%" + self.txt_serch.get() + "%",)

            my_cursor.execute(query, value)

            rows = my_cursor.fetchall()

            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())

            for row in rows:
                self.Cust_Details_Table.insert("", END, values=row)

            conn.close()

        except Exception as e:
            messagebox.showerror("Error", str(e))


# ========================= RUN =========================

if __name__ == "__main__":
    root = Tk()
    app = Cust_Win(root)
    root.mainloop()


