from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogniton System")

        # ===========variable================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        # first image
        img = Image.open(r"D:\Recognition System\college_images\photos.jpg")
        img = img.resize((800,200))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        # second image
        img1= Image.open(r"D:\Recognition System\college_images\photos.jpg")
        img1= img1.resize((800,200))
        self.photoimg1= ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)
        img3 = Image.open(r"D:\Recognition System\college_images\photos.jpg")
        img3 = img3.resize((1530,710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img,text="Attendance Management System",font=("times new roman",30,"bold"),bg="black",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1500,height=600)

        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Datails",font=("times new roman",20,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)


        img_left = Image.open(r"D:\Recognition System\college_images\student.png")
        img_left = img_left.resize((720,130))
        self.photoimage_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image= self.photoimage_left)
        f_lbl.place(x=5,y=0,width=720,height=130)


        left_inside_frame = Frame(Left_frame,bd=2,bg="white")
        left_inside_frame.place(x=0,y=135,width=710,height=370)


        # labels entry
        # Attendance_ID
        attendanceID_label = Label(left_inside_frame,text="AttendanceID",font=("times new roman",10,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",10,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        # Roll
        roll_label = Label(left_inside_frame,text="Roll",font=("times new roman",10,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        roll_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",10,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        # Name
        name_label = Label(left_inside_frame,text="Name",font=("times new roman",10,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",10,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        # Department
        dep_label = Label(left_inside_frame,text="Department",font=("times new roman",10,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dep_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",10,"bold"))
        dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        # Time
        time_label = Label(left_inside_frame,text="Time",font=("times new roman",10,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",10,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        # Date
        date_label = Label(left_inside_frame,text="Date",font=("times new roman",10,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",10,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        # Attendance
        attendance_label = Label(left_inside_frame,text="Attendance Status",font=("times new roman",10,"bold"),bg="white")
        attendance_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.attendance_combo = ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font=("times new roman",10,"bold"),state="readonly")
        self.attendance_combo["values"]=("Status","Present","Absent")
        self.attendance_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        self.attendance_combo.current(0)


        # buttons frame
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        # save button
        import_csv_btn =Button(btn_frame,text="Import csv",command=self.importCsv,width=14,font=("times new roman",15,"bold"),bg="blue",fg="white")
        import_csv_btn.grid(row=0,column=0)

        # update button 
        export_csv_btn =Button(btn_frame,text="Export csv",command=self.exportCsv,width=14,font=("times new roman",15,"bold"),bg="blue",fg="white")
        export_csv_btn.grid(row=0,column=1)
        
        # delete button
        update_btn =Button(btn_frame,text="Update",width=14,font=("times new roman",15,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        # reset button
        reset_btn =Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",15,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        


        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Datails",font=("times new roman",20,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        table_frame = Frame(Right_frame,bd=2,bg="white")
        table_frame.place(x=5,y=5,width=710,height=400)

        # ***************** scroll bar *****************
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),
                                                  xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="AttendanceID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # ===================fetch data =================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    # import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
        with open(file_name) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    
    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(file_name,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported","Your data exported to "+os.path.basename(file_name)+"successfully")
        except Exception as e:
            messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)
    
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root=Tk()
    objects=Attendance(root)
    root.mainloop()