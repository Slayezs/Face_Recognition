from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogniton System")

        #  ==========variable =================================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester= StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()


# first image
        img = Image.open(r"D:\Recognition System\college_images\photos.jpg")
        img = img.resize((500,130))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

# second image
        img1= Image.open(r"D:\Recognition System\college_images\photos.jpg")
        img1= img1.resize((500,130))
        self.photoimg1= ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

# third image
        img2 = Image.open(r"D:\Recognition System\college_images\photos.jpg")
        img2 = img2.resize((500,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

# background image
        img3 = Image.open(r"D:\Recognition System\college_images\photos.jpg")
        img3 = img3.resize((1530,710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

# title 
        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="black",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1500,height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Datails",font=("times new roman",20,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open(r"D:\Recognition System\college_images\student.png")
        img_left = img_left.resize((720,130))
        self.photoimage_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image= self.photoimage_left)
        f_lbl.place(x=5,y=0,width=720,height=130)


        # current courses information
        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",20,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=150)

        # department
        dep_label = Label(current_course_frame,text="Dep",font=("times new roman",10,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer Science","Mechanical","Civil","Electronics")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)


        # course
        course_label = Label(current_course_frame,text="Course",font=("times new roman",10,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","TE","SE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        # year
        year_label = Label(current_course_frame,text="Year",font=("times new roman",10,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        # semester
        semester_label = Label(current_course_frame,text="Semester",font=("times new roman",10,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        # Class Student  information
        class_student_info_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",20,"bold"))
        class_student_info_frame.place(x=5,y=250,width=720,height=300)

        # Student ID
        studentID_label = Label(class_student_info_frame,text="Student_id",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry = ttk.Entry(class_student_info_frame,textvariable=self.var_std_id,width=20,font=("times new roman",10,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Student name
        student_name_label = Label(class_student_info_frame,text="Name",font=("times new roman",10,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry = ttk.Entry(class_student_info_frame,textvariable=self.var_std_name,width=20,font=("times new roman",10,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Class division
        class_division_label = Label(class_student_info_frame,text="Division",font=("times new roman",10,"bold"),bg="white")
        class_division_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #class_division_entry = ttk.Entry(class_student_info_frame,textvariable=self.var_div,width=20,font=("times new roman",10,"bold"))
        #class_division_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo = ttk.Combobox(class_student_info_frame,textvariable=self.var_div,width=20,font=("times new roman",10,"bold"))
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        # Roll No
        roll_no_label = Label(class_student_info_frame,text="Roll",font=("times new roman",10,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry = ttk.Entry(class_student_info_frame,textvariable=self.var_roll,width=20,font=("times new roman",10,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender 
        gender_label = Label(class_student_info_frame,text="Gender",font=("times new roman",10,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo = ttk.Combobox(class_student_info_frame,textvariable=self.var_gender,width=20,font=("times new roman",10,"bold"))
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        # Date of Birth 
        dob_label = Label(class_student_info_frame,text="Dob",font=("times new roman",10,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry = ttk.Entry(class_student_info_frame,textvariable=self.var_dob,width=20,font=("times new roman",10,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        # Email
        email_label = Label(class_student_info_frame,text="Email",font=("times new roman",10,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry = ttk.Entry(class_student_info_frame,textvariable=self.var_email,width=20,font=("times new roman",10,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Phone No
        phone_label = Label(class_student_info_frame,text="Phone",font=("times new roman",10,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry = ttk.Entry(class_student_info_frame,textvariable=self.var_phone,width=20,font=("times new roman",10,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address
        address_label = Label(class_student_info_frame,text="Address",font=("times new roman",10,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry = ttk.Entry(class_student_info_frame,textvariable=self.var_address,width=20,font=("times new roman",10,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teacher Name
        teacher_name_label = Label(class_student_info_frame,text="Teacher",font=("times new roman",10,"bold"),bg="white")
        teacher_name_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_name_entry = ttk.Entry(class_student_info_frame,textvariable=self.var_teacher,width=20,font=("times new roman",10,"bold"))
        teacher_name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        # radio buttons
        self.var_radio1 =StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_info_frame,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=6,column=0) #6,0

        radiobtn2 = ttk.Radiobutton(class_student_info_frame,text="NO Photo Sample",variable=self.var_radio1,value="No")
        radiobtn2.grid(row=6,column=1)  #6,1

        # buttons frame
        btn_frame = Frame(class_student_info_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=715,height=35)

        # save button
        save_btn =Button(btn_frame,text="Save",command=self.add_data,width=14,font=("times new roman",15,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        # update button 
        update_btn =Button(btn_frame,text="Update",command=self.update_data,width=14,font=("times new roman",15,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        # delete button
        delete_btn =Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("times new roman",15,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        # reset button
        reset_btn =Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",15,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        # buttons1 frame
        btn1_frame = Frame(class_student_info_frame,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=0,y=210,width=715,height=30)

        # Take photo button
        take_photo_btn =Button(btn1_frame,text="Take Photo sample",command=self.generate_dataset,width=40,font=("times new roman",10,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        # Update photo button
        update_photo_btn =Button(btn1_frame,text="Update Photo Sample",width=40,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)





        # Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Datails",font=("times new roman",20,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        img_right = Image.open(r"D:\Recognition System\college_images\student.png")
        img_right = img_left.resize((720,130))
        self.photoimage_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame,image= self.photoimage_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        # ***************** Search System ***************** 
        search_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",20,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label = Label(search_frame,text="Search by",font=("times new roman",10,"bold"))
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo = ttk.Combobox(search_frame,font=("times new roman",10,"bold"),state="readonly",width=20)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        serach_entry = ttk.Entry(search_frame,width=15,font=("times new roman",10,"bold"))
        serach_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn =Button(search_frame,text="Search",width=12,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        show_all_btn =Button(search_frame,text="Show All",width=12,font=("times new roman",10,"bold"),bg="blue",fg="white")
        show_all_btn.grid(row=0,column=4,padx=10,pady=5,sticky=W)


         # ***************** Table Frame ***************** 
        table_frame =Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("dep","course","year","semester","id","name","div","roll","gender","dob","email","phone_no","address","teacher","photo"),
                                          xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Dep")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("id",text="Student_id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Dob")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone_no",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSample")
        self.student_table["show"]="headings"


        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone_no",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    # ========function decration ========
    def add_data(self):
      if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "" :
          messagebox.showerror("Error","All Fields are required",parent = self.root)
      else :
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Password?12root",database = "face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()   
                    ))
            
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Students details has been added successfully",parent=self.root)
            
            except Exception as es:
                    messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
            
    # ===================fetch Data =================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Password?12root",database = "face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

# ============ get cursor =================

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus() 
        content = self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

# update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "" :
            messagebox.showerror("Error","All Fields are required",parent = self.root)
        else :
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details?",parent = self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Password?12root",database = "face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(       
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_std_name.get(),
                                        self.var_div.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get(),
                                        self.var_std_id.get()  
                                    
                                     ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root )
                conn.commit()
                self.fetch_data()
                conn.close()
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root) 

# delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Password?12root",database = "face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

        # reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
      #  self.student_table.delete(*self.student_table.get_children())
                    

     ########### Generate Data Set ###############
    def generate_dataset(self): 
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "" :
            messagebox.showerror("Error","All Fields are required",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Password?12root",database = "face_recognizer")
                my_cursor=conn.cursor() 
                my_cursor.execute("select * from student")
                my_result = my_cursor.fetchall()
                id =0
                for x in my_result:
                    id+=1  
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(       
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_std_name.get(),
                                        self.var_div.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get(),
                                        self.var_std_id.get() == id+1
                                    
                                     ))  
                conn.commit() 
                self.fetch_data()
                self.reset_data()
                conn.close()


                ##################### Taking pictures for face detection from opencv #######################
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor = 1.3
                    # minimum neighbour = 5
                    for(x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                
                cap = cv2.VideoCapture(0)
                img_id =0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    # to stop the loop
                    if cv2.waitKey(1) == 13 or int (img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
            


if __name__ == "__main__":
    root=Tk()
    objects=Student(root)
    root.mainloop()
