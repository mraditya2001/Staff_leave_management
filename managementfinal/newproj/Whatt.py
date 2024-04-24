from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title(" FGIET FACULTY MANAGEMENT SYSTEM")

        # # Inside your Student class __init__ method after creating the treeview widgescroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL, command=self.student_table.xview)
        # scroll_x.pack(side=BOTTOM, fill=X)
        # self.student_table.configure(xscrollcommand=scroll_x.set)
        #
        # scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL, command=self.student_table.yview)
        # scroll_y.pack(side=RIGHT, fill=Y)
        # self.student_table.configure(yscrollcommand=scroll_y.set)
        #
        # # Also add the following lines after creating other relevant widgets
        # txt_address.config(yscrollcommand=scroll_y.set)

        # variables
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_duty = StringVar()
        self.var_post = StringVar()
        self.var_dis = StringVar()
        self.var_reason = StringVar()
        self.var_gender = StringVar()
        self.var_ID = StringVar()
        self.var_mail = StringVar()
        self.var_DOB = StringVar()
        self.var_phone = StringVar()
        self.var_home = StringVar()
        self.var_NoOfDays = StringVar()
        self.var_taken = StringVar()
        self.var_date = StringVar()
        self.var_curr_add = StringVar()

        img=Image.open(r"college_images/fgietlogo.jpg")
        img=img.resize((510,160),Image.ANTIALIAS)
        self.photoimg= ImageTk.PhotoImage(img)
        self.btn_1 = Button(self.root, image=self.photoimg, cursor="hand2")
        self.btn_1.place(x=540, y=0, width=540, height=160)

        # 1st
        img_1 = Image.open(r"college_images/fgietlogo.jpg")
        img_1 = img_1.resize((540, 160), Image.ANTIALIAS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        self.btn_1 = Button(self.root, image=self.photoimg_1, cursor="hand2")
        self.btn_1.place(x=0, y=0, width=540, height=160)

        # 2nd
        img_2 = Image.open(r"college_images/feroze-gandhi-institute-of-engineering-technology-rae-bareli-214415.jpg")
        img_2 = img_2.resize((540, 160), Image.ANTIALIAS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        self.btn_2 = Button(self.root, image=self.photoimg_2, cursor="hand2")
        self.btn_2.place(x=540, y=0, width=540, height=160)

        # 3st
        img_3 = Image.open(r"college_images/fgietimages (1).jfif")
        img_3 = img_3.resize((540, 160), Image.ANTIALIAS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)

        self.btn_3 = Button(self.root, image=self.photoimg_3, cursor="hand2")
        self.btn_3.place(x=1000, y=0, width=540, height=160)

        # bg img
        img_4 = Image.open(r"college_images/feroze-gandhi-institute-of-engineering-technology-rae-bareli-214415.jpg")
        img_4 = img.resize((540, 160), Image.ANTIALIAS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)

        bg_lbl= Label(self.root,image=self.photoimg_4, bd=2, relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1530,height=710)
        # self.btn_4 = Button(self.root, image=self.photoimg_4, cursor="hand2")
        # self.btn_4.place(x=1000, y=0, width=540, height=160)


        lbl_title = Label(bg_lbl, text="FACULTY MANAGEMENT SYSTEM", font=("times new roman", 37, "bold"), fg="dark blue",
                        bg="violet")
        lbl_title.place(x=0, y=0, width=1530, height=50)

        # manage frame
        Manage_frame = Frame(bg_lbl, bd=2, relief=RIDGE, bg="white")
        Manage_frame.place(x=15, y=55, width=1500, height=560)

        # left frame
        DataLeftFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="TEACHERS Information", font=("times new roman", 12, "bold"), fg="red", bg="white")
        DataLeftFrame.place(x=10, y=10, width=660, height=560)

        # img1
        img_5 = Image.open(r"college_images\3rd.jpg")
        img_5 = img_5.resize((650, 120), Image.ANTIALIAS)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)

        my_img = Label(DataLeftFrame, image=self.photoimg_5, bd=2, relief=RIDGE)
        my_img.place(x=0, y=1, width=650, height=120)

        # current course LabelFrame information
        std_lbl_info_frame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="TEACHERS Information",
                                        font=("times new roman", 12, "bold"), fg="red", bg="white")
        std_lbl_info_frame.place(x=10, y=10, width=660, height=560)

        # labels
        lbl_dep = Label(std_lbl_info_frame, text="Department", font=("arial", 12, "bold"), bg="white")
        lbl_dep.grid(row=0, column=0, padx=2, sticky=W)

        combo_dep = ttk.Combobox(std_lbl_info_frame,textvariable=self.var_dep, font=("arial", 12, "bold"), width=17, state="readonly")
        combo_dep["value"] = (
        "Select Department", "Computer Science and Engineering", "Elctronic and Communication Engineering",
        "Aeronautical Engineering", "Mechanical Engineering", "MCA")
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # duty
        course_std = Label(std_lbl_info_frame, font=("arial", 12, "bold"), text="Other Duty:", bg="white")
        course_std.grid(row=1, column=2, padx=2, pady=10, sticky=W)

        com_txtcourse_std = ttk.Combobox(std_lbl_info_frame, state="readonly",textvariable=self.var_duty, font=("arial", 12, "bold"), width=17)

        com_txtcourse_std['value'] = ("Select ", "Not Applicable", "Warden", "Sports Head", "Fest Organizer")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=1, column=3, sticky=W, padx=2, pady=10)

        # post
        currunt_year = Label(std_lbl_info_frame,font=("arial", 12, "bold"), text="Post:", bg="white")
        currunt_year.grid(row=1, column=0, sticky=W, padx=2, pady=10)

        com_txt_currunt_year = ttk.Combobox(std_lbl_info_frame, state="readonly",textvariable=self.var_post, font=("arial", 12, "bold"), width=17)

        com_txt_currunt_year['value']=("Select post","Head of Department","Professor","Associate professor", "Administration staff", "Support staff")
        com_txt_currunt_year.current(0)
        com_txt_currunt_year.grid(row=1,column=1,sticky=W,padx=2)
        #reason
        label_Semester=Label(std_lbl_info_frame,font=("arial",12,"bold"),text="Reason:",bg="white")
        label_Semester.grid(row=2,column=2,sticky=W,padx=2,pady=10)
        comSemister=ttk.Combobox(std_lbl_info_frame,state="readonly",textvariable=self.var_reason, font=("arial",12,"bold"),width=17)
        comSemister['value']=("Select type","Family Issue","Health Issue","Other Issue")
        comSemister.current(0)
        comSemister.grid(row=2,column=3,sticky=W,padx=2,pady=10)
        
        #Teacher's class Lableframe Information
        std_lbl_class_frame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="Enter Your Details",
                                        font=("times new roman", 12, "bold"), fg="red", bg="white")
        std_lbl_class_frame.place(x=15, y=170, width=650, height=250)

        lbl_id=Label(std_lbl_class_frame,font=("arial",12,"bold"),text="CollegeID",bg="white")
        lbl_id.grid(row=0,column=0,sticky=W,padx=2,pady=7)

        txt_id = ttk.Entry(std_lbl_class_frame, width=22,textvariable=self.var_ID, font=("arial", 11, "bold"))
        txt_id.grid(row=0, column=1, padx=2, pady=7)

        #Name
        lbl_Name=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Your Name:",bg="white")
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(std_lbl_class_frame,width=22,textvariable=self.var_name,font=("arial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)
        # Gender
        lbl_div= Label(std_lbl_info_frame,font=("arial",11,"bold"),text="Gender:", bg="white")
        lbl_div.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        com_txt_div=ttk.Combobox(std_lbl_info_frame,state="readonly",textvariable=self.var_gender,font=("arial",12,"bold"),width=18)
        com_txt_div['value']=("Select Gender","Male","Female")
        com_txt_div.current(0)
        com_txt_div.grid(row=0,column=3,sticky=W,padx=2,pady=7)
        #Hometown
        lbl_roll=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Home Town:",bg="white")
        lbl_roll.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_roll=ttk.Entry(std_lbl_class_frame,width=22,textvariable=self.var_home,font=("arial",11,"bold"))
        txt_roll.grid(row=1,column=3,padx=3,pady=7)

        # Disable
        lbl_dis=Label(std_lbl_info_frame,font=("arial",11,"bold"),text="Any Disability:", bg="white")
        lbl_dis.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        com_txt_dis=ttk.Combobox(std_lbl_info_frame,state="readonly",textvariable=self.var_dis, font=("arial",12,"bold"),width=18)
        com_txt_dis['value']=["Enter","Yes","No"]
        com_txt_dis.current(0)
        com_txt_dis.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        # Teacher's did_you Information
        std_lbl_did_you = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="",
                                        font=("times new roman", 12, "bold"), fg="red", bg="white")
        std_lbl_did_you.place(x=15, y=340, width=650, height=250)

        # No of days
        lbl_dob = Label(std_lbl_did_you,font=("arial", 11, "bold"), text="No. of days you want leave:", bg="white")
        lbl_dob.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        txt_dob = ttk.Entry(std_lbl_did_you, width=22,textvariable=self.var_NoOfDays, font=("arial", 11, "bold"))
        txt_dob.grid(row=2, column=1, padx=2, pady=7)

        # # Teacher's more more_spc Information
        # std_lbl_more_spc = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="Add Some More Detail",
        #                              font=("times new roman", 12, "bold"), fg="red", bg="white")
        # std_lbl_more_spc.place(x=15, y=385, width=650, height=250)


        # # explain in brief
        #
        # txt_roll = ttk.Entry(std_lbl_more_spc, width=79, font=("arial", 11, "bold"))
        # txt_roll.grid(row=1, column=3, padx=3, pady=7)

        # DID YOU
        lbl_did = Label(std_lbl_did_you, font=("arial", 11, "bold"), text="Did you already taken a leave without Informing:", bg="white")
        lbl_did.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        com_txt_did = ttk.Combobox(std_lbl_did_you, state="readonly",textvariable=self.var_taken, font=("arial", 12, "bold"), width=18)
        com_txt_did['value'] = ["Enter", "Yes", "No"]
        com_txt_did.current(0)
        com_txt_did.grid(row=3, column=1, sticky=W, padx=2, pady=7)

        lbl_dob = Label(std_lbl_did_you, font=("arial", 11, "bold"), text="enter today's date", bg="white")
        lbl_dob.grid(row=4, column=0, sticky=W, padx=2, pady=7)

        txt_dob = ttk.Entry(std_lbl_did_you, width=22, font=("arial", 11, "bold"))
        txt_dob.grid(row=4, column=1, padx=2, pady=7)

        # DOB
        lbl_dob=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="DOB:",bg="white")
        lbl_dob.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(std_lbl_class_frame,width=22,textvariable=self.var_DOB,font=("arial",11,"bold"))
        txt_dob.grid(row=2,column=1,padx=2,pady=7)

        #Email
        lbl_email = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="E-MAIL", bg="white")
        lbl_email.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        txt_email = ttk.Entry(std_lbl_class_frame, width=22,textvariable=self.var_mail, font=("arial", 11, "bold"))
        txt_email.grid(row=1, column=1, padx=2, pady=7)
        #phone
        lbl_phone = Label(std_lbl_class_frame, font=("arial", 11, "bold"), text="PHONE NO.", bg="white")
        lbl_phone.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        txt_phone = ttk.Entry(std_lbl_class_frame, width=22,textvariable=self.var_phone, font=("arial", 11, "bold"))
        txt_phone.grid(row=2, column=3, padx=2, pady=7)
        #Address
        lbl_address = Label(std_lbl_did_you, font=("arial", 11, "bold"), text="Current  Address", bg="white")
        lbl_address.grid(row=5, column=0, sticky=W, padx=2, pady=7)

        txt_address = ttk.Entry(std_lbl_did_you, width=22,textvariable=self.var_curr_add, font=("arial", 11, "bold"))
        txt_address.grid(row=5, column=1, padx=2, pady=7)

        # button frame
        btn_frame = Frame(bg_lbl, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=35, y=560, width=640, height=40)

        btn_Add = Button(btn_frame, text="Save",command=self.add_data, font=("arial", 11, "bold"), width=17, bg="violet", fg="black")
        btn_Add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, text="Update",command=self.update_data, font=("arial", 11, "bold"), width=17, bg="violet", fg="black")
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, text="Withdraw",command=self.delete_data,font=("arial", 11, "bold"), width=17, bg="violet", fg="black")
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset",command=self.reset_data, font=("arial", 11, "bold"), width=17, bg="violet", fg="black")
        btn_reset.grid(row=0, column=3, padx=2)

        # Right frame
        DataRightFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="Request Window",
                                    font=("times new roman", 12, "bold"), fg="red", bg="white")
        DataRightFrame.place(x=680, y=10, width=870, height=540)

        # img1
        img_6 = Image.open(r"college_images/fgirtbackgroundimages.png")
        img_6 = img_6.resize((650, 120), Image.ANTIALIAS)
        self.photoimg_6 = ImageTk.PhotoImage(img_6)

        my_img = Label(DataRightFrame, image=self.photoimg_6, bd=2, relief=RIDGE)
        my_img.place(x=0, y=0, width=800, height=120)
        #track frame
        Track_Frame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="Track your Request",
                                    font=("times new roman", 12, "bold"), fg="red", bg="white")
        Track_Frame.place(x=680, y=155, width=810, height=70)

        lbl_search = Label(Track_Frame, font=("arial", 11, "bold"), text="Search Request by:", bg="blue", fg="white")
        lbl_search.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        self.var_track=StringVar()
        com_txt_search = ttk.Combobox(Track_Frame, state="readonly", font=("arial", 12, "bold"), width=18)
        com_txt_search['value'] = ["Enter", "Department", "CollegeID", "Post", "Disability", "Reason", "Other Duty"]
        com_txt_search.current(0)
        com_txt_search.grid(row=2, column=1, sticky=W, padx=5, pady=7,)

        txt_search = ttk.Entry( Track_Frame,textvariable=self.var_track, width=22, font=("arial", 13, "bold"))
        txt_search.grid(row=2, column=2, padx=4, pady=10)

        btn_Search = Button(Track_Frame, text="Search",command=self.search_data, font=("arial", 11, "bold"), width=10, bg="red", fg="white")
        btn_Search.grid(row=2, column=3, padx=1)

        btn_showAll = Button(Track_Frame, text="Show All",command=self.fetch_data, font=("arial", 11, "bold"), width=10, bg="red", fg="white")
        btn_showAll.grid(row=2, column=4, padx=1)
        ##### =================Faculty table and their request==================== #####

        table_frame=Frame(DataRightFrame,bd=4, relief=RIDGE)
        table_frame.place(x=0, y=200, width=805, height=320)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame, column=("name","dep","duty","post","dis","reason",
                                                             "gender","ID","mail","DOB","phone","home","NoOfDays","taken",
                                                             "date","curr_add"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("name", text="Name")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("duty", text="Other Duty")
        self.student_table.heading("post", text="Post")
        self.student_table.heading("dis", text="Disability")
        self.student_table.heading("reason", text="Reason")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("ID", text="CollegeID")
        self.student_table.heading("mail", text="E-Mail")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("phone", text="PHONE NO.")
        self.student_table.heading("home", text="Home Town")
        self.student_table.heading("NoOfDays", text="No of Days")
        self.student_table.heading("taken", text="Already taken leave")
        self.student_table.heading("date", text="Date of Appling")
        self.student_table.heading("curr_add",text="current address")

        self.student_table["show"]="headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("duty", width=100)
        self.student_table.column("post", width=100)
        self.student_table.column("dis", width=100)
        self.student_table.column("reason", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("ID", width=100)
        self.student_table.column("mail", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("home", width=100)
        self.student_table.column("NoOfDays", width=100)
        self.student_table.column("taken", width=100)
        self.student_table.column("date", width=100)
        self.student_table.column("curr_add",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_dep.get() == "" or self.var_mail.get() == "" or self.var_ID.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Test@123",
                                               database="mydata")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO faculty (name, dep, duty, post, dis, reason, gender, ID, mail, "
                    "DOB, phone, home, NoOfDays, taken, date, curr_add) VALUES "
                    "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_name.get(),
                        self.var_dep.get(),
                        self.var_duty.get(),
                        self.var_post.get(),
                        self.var_dis.get(),
                        self.var_reason.get(),
                        self.var_gender.get(),
                        self.var_ID.get(),
                        self.var_mail.get(),
                        self.var_DOB.get(),
                        self.var_phone.get(),
                        self.var_home.get(),
                        self.var_NoOfDays.get(),
                        self.var_taken.get(),
                        self.var_date.get(),
                        self.var_curr_add.get(),
                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Your Request has been sent!", parent=self.root)
                self.fetch_data()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM faculty")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                # Inserting values into the treeview widget in the desired order
                self.student_table.insert("", END, values=(
                    i[0],  # name
                    i[7],  # department
                    i[2],  # other duty
                    i[3],  # post
                    i[4],  # disability
                    i[6],  # reason
                    i[5],  # gender
                    i[1],  # collegeID
                    i[8],  # Email
                    i[9],  # dob
                    i[10],  # phone no
                    i[11],  # home town
                    i[12],  # no of days
                    i[13],  # already taken leave
                    i[15],  # current address
                    i[14],  # date of applying
                ))
            conn.commit()
        conn.close()

    # #fetch function
    # def fetch_data(self):
    #     conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="mydata")
    #     my_cursor = conn.cursor()
    #     my_cursor.execute("SELECT * FROM faculty")
    #     data = my_cursor.fetchall()
    #     if len(data) != 0:
    #         self.student_table.delete(*self.student_table.get_children())
    #         for i in data:
    #             self.student_table.insert("", END, values=i)
    #         conn.commit()
    #     conn.close()
    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]

        self.var_name.set(data[0])
        self.var_dep.set(data[1])
        self.var_duty.set(data[2])
        self.var_post.set(data[3])
        self.var_dis.set(data[4])
        self.var_reason.set(data[5])
        self.var_gender.set(data[6])
        self.var_ID.set(data[7])
        self.var_mail.set(data[8])
        self.var_DOB.set(data[9])
        self.var_phone.set(data[10])
        self.var_home.set(data[11])
        self.var_NoOfDays.set(data[12])
        self.var_taken.set(data[13])
        self.var_date.set(data[14])
        self.var_curr_add.set(data[15])

    # # get cursor
    # def get_cursor(self,event=""):
    #     cursor_row=self.faculty_table.focus()
    #     content=self.faculty_table.item(cursor_row)
    #     data=content["values"]
    #
    #     self.var_name.set(data[0]),
    #     self.var_dep.set(data[1]),
    #     self.var_duty.set(data[2]),
    #     self.var_post.set(data[3]),
    #     self.var_dis.set(data[4]),
    #     self.var_reason.set(data[5]),
    #     self.var_gender.set(data[6]),
    #     self.var_ID.set(data[7]),
    #     self.var_mail.set(data[8]),
    #     self.var_DOB.set(data[9]),
    #     self.var_phone.set(data[10]),
    #     self.var_home.set(data[11]),
    #     self.var_NoOfDays.set(data[12]),
    #     self.var_taken.set(data[13]),
    #     self.var_date.set(data[14]),
    #     self.var_curr_add.set(data[15]),

    def update_data(self):
        if self.var_dep.get() == "" or self.var_mail.get() == "" or self.var_ID.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            try:
                update = messagebox.askyesno("Update", "Are you sure Update this student data", parent=self.root)
                if update:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Test@123",
                                                   database="mydata")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "UPDATE faculty SET dep=%s, name=%s, duty=%s, post=%s, dis=%s, reason=%s, gender=%s, mail=%s, DOB=%s, phone=%s, home=%s, NoOfDays=%s, taken=%s, date=%s, curr_var=%s WHERE ID=%s",
                        (self.var_dep.get(), self.var_name.get(), self.var_duty.get(),
                         self.var_post.get(), self.var_dis.get(), self.var_reason.get(),
                         self.var_gender.get(), self.var_mail.get(), self.var_DOB.get(),
                         self.var_phone.get(), self.var_home.get(), self.var_NoOfDays.get(),
                         self.var_taken.get(), self.var_date.get(), self.var_curr_add.get()))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student Successfully uploaded", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


    #delete

    def delete_data(self):
        if self.var_ID.get() == "":
            messagebox.showerror("Error", "All Fields Are required")
        else:
            try:
                delete = messagebox.askyesno("Withdraw?", "Are you sure want to withdraw your request")
                if delete:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Test@123",
                                                   database="mydata")
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM faculty WHERE ID=%s"
                    value = (self.var_ID.get(),)
                    my_cursor.execute(sql, value)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Withdraw!", "Your request has been withdrawn", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # Reset
    def reset_data(self):
        self.var_name.set(""),
        self.var_dep.set("Select Department"),
        self.var_duty.set("Select "),
        self.var_post.set("Select post"),
        self.var_dis.set("Enter"),
        self.var_reason.set("Select type"),
        self.var_gender.set("Select"),
        self.var_ID.set(""),
        self.var_mail.set(""),
        self.var_DOB.set(""),
        self.var_phone.set(""),
        self.var_home.set(""),
        self.var_NoOfDays.set(""),
        self.var_taken.set("Enter"),
        self.var_date.set(""),
        self.var_curr_add.set(""),

    # search data
    def search_data(self):
        if self.var_track.get() == "" or self.var_com_search.get() == "":
            messagebox.showerror("Error", "Please select option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Test@123",
                                               database="mydata")
                my_cursor = conn.cursor()
                query = "SELECT * FROM faculty WHERE " + self.var_com_search.get() + " LIKE '%" + self.var_track.get() + "%'"
                my_cursor.execute(query)
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()


