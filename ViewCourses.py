# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:16:58 2019

J.A.R.V.I.S Says Hello

@author: Sayan
"""

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "Asdf$1234"
mydatabase="student"

con = pymysql.connect(host="localhost",user="admin",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
courseTable = "courses" #Course Table
    
def ViewCourse(): 
    
    root = Tk()
    root.title("Course")
    root.minsize(width=400,height=400)
    root.geometry("600x500")


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
    
    Canvas1.config(bg="#F8EFBA",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)
        
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
        
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    headingLabel = Label(headingFrame2, text="VIEW COURSES", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)   
    
    y = 0.25
    
    Label(labelFrame, text="%-20s%-30s%-20s%-30s"%('Course #','Course_Name','Semester','Term'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getCourses = "select course_number, course_name, semester, term from "+courseTable
    try:
        cur.execute(getCourses)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-20s%-30s%-20s%-30s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Bad Format","Can't fetch files from database")
    
    root.mainloop()