# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 19:59:49 2019

J.A.R.V.I.S Says Hello

@author: Sayan
"""

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql



def courseAdd():
    
    course_number = en1.get()
    course_name = en2.get()
    semester = en3.get()
    term = en4.get()
    # status = en5.get()
    # status = status.lower()
    
    insertCourse_statement = "insert into "+courseTable+"(course_number, course_name, semester, term) values("+course_number+",'"+course_name+"','"+semester+"',"+term+")"
    print(insertCourse_statement)
    try:
        cur.execute(insertCourse_statement)
        con.commit()
        messagebox.showinfo("info","Successfully add course into Database")
    except:
        messagebox.showinfo("Error","Can't add course into Database")
    
    print(course_number)
    print(course_name)
    print(semester)
    print(term)

    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    # en5.delete(0, END)

    
def addCourses(): 
    
    global en1,en2,en3,en4,en5,Canvas1,con,cur,courseTable,root
    
    root = Tk()
    root.title("Course Management")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "Asdf$1234"
    mydatabase="student"

    con = pymysql.connect(host="localhost",user="admin",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    courseTable = "courses" # Book Table

    same=True
    n=0.3

    # Adding a background image
    background_image =Image.open("college.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size
    
    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n)
    
    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#74b9ff",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)
        
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.7)
        
    # Course Number
    lb1 = Label(labelFrame,text="Course Number : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.1)
        
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.1, relwidth=0.62)
        
    # Course Name
    lb2 = Label(labelFrame,text="Course Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.25)
        
    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.25, relwidth=0.62)
        
    # Semester
    lb3 = Label(labelFrame,text="Semester : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4)
        
    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.4, relwidth=0.62)
        
    # Term
    lb4 = Label(labelFrame,text="Term : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.55)
        
    en4 = Entry(labelFrame)
    en4.place(relx=0.3,rely=0.55, relwidth=0.62)
        
    # # Book Status
    # lb5 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
    # lb5.place(relx=0.05,rely=0.75)
        
    # en5 = Entry(labelFrame)
    # en5.place(relx=0.3,rely=0.75, relwidth=0.62)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=courseAdd)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()