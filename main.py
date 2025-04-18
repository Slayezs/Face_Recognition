from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogniton System")

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
        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button 
        img4 = Image.open(r"D:\Recognition System\college_images\student.png")
        img4 = img4.resize((220,220))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        btn1= Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        btn1.place(x=200,y=100,width=220,height=220)

        btn1_1= Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white")
        btn1_1.place(x=200,y=300,width=220,height=40)


         #Detect face button 
        img5 = Image.open(r"D:\Recognition System\college_images\face_detector.jpg")
        img5 = img5.resize((220,220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        btn1= Button(bg_img,image=self.photoimg5,command=self.face_details,cursor="hand2")
        btn1.place(x=500,y=100,width=220,height=220)

        btn1_1= Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_details,font=("times new roman",10,"bold"),bg="black",fg="white")
        btn1_1.place(x=500,y=300,width=220,height=40)

         # Attendance face button 
        img6 = Image.open(r"D:\Recognition System\college_images\attendance.webp")
        img6 = img6.resize((220,220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btn1= Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.atttendance_details)
        btn1.place(x=800,y=100,width=220,height=220)

        btn1_1= Button(bg_img,text="Attendance",cursor="hand2",command=self.atttendance_details,font=("times new roman",10,"bold"),bg="black",fg="white")
        btn1_1.place(x=800,y=300,width=220,height=40)


         #help face button 
        img7 = Image.open(r"D:\Recognition System\college_images\help_desk.png")
        img7 = img7.resize((220,220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        btn1= Button(bg_img,image=self.photoimg7,cursor="hand2")
        btn1.place(x=1100,y=100,width=220,height=220)

        btn1_1= Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white")
        btn1_1.place(x=1100,y=300,width=220,height=40)
        


        #Train data button 
        img8 = Image.open(r"D:\Recognition System\college_images\train_data.png")
        img8 = img8.resize((220,220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        btn1= Button(bg_img,image=self.photoimg8,command=self.train_details,cursor="hand2")
        btn1.place(x=200,y=380,width=220,height=220)

        btn1_1= Button(bg_img,text="Train Data",cursor="hand2",command=self.train_details,font=("times new roman",10,"bold"),bg="black",fg="white")
        btn1_1.place(x=200,y=580,width=220,height=40)


         # Photos button 
        img9 = Image.open(r"D:\Recognition System\college_images\photos.jpg")
        img9 = img9.resize((220,220))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        btn1= Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        btn1.place(x=500,y=380,width=220,height=220)

        btn1_1= Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",10,"bold"),bg="black",fg="white")
        btn1_1.place(x=500,y=580,width=220,height=40)

         # Developer button 
        img10 = Image.open(r"D:\Recognition System\college_images\developer.jpg")
        img10 = img10.resize((220,220))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        btn1= Button(bg_img,image=self.photoimg10,cursor="hand2")
        btn1.place(x=800,y=380,width=220,height=220)

        btn1_1= Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white")
        btn1_1.place(x=800,y=580,width=220,height=40)


         #Exit button 
        img11 = Image.open(r"D:\Recognition System\college_images\exit.jpg")
        img11 = img11.resize((220,220))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        btn1= Button(bg_img,image=self.photoimg11,cursor="hand2")
        btn1.place(x=1100,y=380,width=220,height=220)

        btn1_1= Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white")
        btn1_1.place(x=1100,y=580,width=220,height=40)



    def open_img(self):
        os.startfile("data")





        # ****************  Function Button ****************

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def atttendance_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()     



 


