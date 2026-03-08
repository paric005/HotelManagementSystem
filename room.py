from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")
        
    
        # ======================= Title =======================

        lbl_title = Label(self.root,text="RoomBooking Details",font=("Times New Roman", 18, "bold"),bg="black",fg="gold" )
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ======================= Logo =======================

        img2 = Image.open(r"C:\Users\Parijat\Documents\HOTEL\logo.png")
        img2 = img2.resize((100, 40), Image.LANCZOS) 

        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)
        
        
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Details",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=Entry(labelframeleft,font=("arial",13,"bold"),width=29,state="readonly")
        entry_contact.grid(row=0,column=1)
        
        # ======================= Labels and entrys =======================
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        enty_contact=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        enty_contact.grid(row=0,column=1,sticky=W)

        btnFetchData=Button(labelframeleft,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)

        check_in_date=Label(labelframeleft,font=("arial",8,"bold"),text="Check_in Date:",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        lbl_Check_out=Label(labelframeleft,font=("arial",12,"bold"),text="Check_Out Date:",padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txt_Check_out.grid(row=2,column=1)

        label_RoomType=Label(labelframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)
        combo_RoomType=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=("Single","Double","Luxury")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        lblRoomAvailable=Label(labelframeleft,font=("arial",12,"bold"),text="Available Room:",padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        txtRoomAvailable=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtRoomAvailable.grid(row=4,column=1)

        lblMeal=Label(labelframeleft,font=("arial",12,"bold"),text="Meal:",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtMeal.grid(row=5,column=1)

        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="No Of Days:",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)

        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="Paid Tax:",padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=7,column=1)

        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="Sub Total:",padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=8,column=1)

        lblIdNumber=Label(labelframeleft,font=("arial",12,"bold"),text="Total Cost:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)
        
        

    

if __name__ == "__main__":
    root = Tk()
    app = Roombooking(root)
    root.mainloop()