import time 
from PIL import Image 
import pyttsx3
import pytesseract
from tkinter import *
from tkinter.filedialog import askopenfilename
from translate import Translator
from tkinter.ttk import *
from langdetect import detect
from tkinter import messagebox
import cv2

import numpy as np
from espeakng import ESpeakNG
from autocorrect import spell

global pic

def say():
    esng = ESpeakNG() 
    esng.voice = "german"
    with open('D:/abc.txt',mode='r') as files:
        p=files.read(500)
    esng.say("hello world")
def faq():



    win=Tk()
    
    win.title("FAQ")
    
    label1=Label(win,text="Frequently Asked Questions", font="42")
    label1.grid(row=1,column=1)
    label2=Label(win,text="Ques. What is name of this project?")
    label2.grid(row=2,column=1)
    label3=Label(win,text="Ans. The name of this project is Multilingual Translator \.")
    label3.grid(row=3,column=1)
    label4=Label(win,text="Ques. Who is the developer?")
    label4.grid(row=4,column=1)
    label5=Label(win,text="Ans. Sabhya Bhushan.")
    label5.grid(row=5,column=1)
    label6=Label(win,text="Ques. Who is the guide?")
    label6.grid(row=6,column=1)
    label7=Label(win,text="Ans. This project has been developed under the guidance of our trainer Mr. Gaurav Tomar.")
    label7.grid(row=7,column=1)
    label8=Label(win,text="Ques. What is the objective of this project?")
    label8.grid(row=8,column=1)
    label9=Label(win,text="Ans. The objective of this project is to make the task simple.\n Many people face the problem while\n reading some text written in some other language")
    label9.grid(row=9,column=1)
    label10=Label(win,text="Ques. Name the technologies used in the project.")
    label10.grid(row=10,column=1)
    label11=Label(win,text="Ans. The technologies used in this project are Python, Computer Vision, Machine Learning.")
    label11.grid(row=11,column=1)
    
    win.mainloop()

def detectsource():
    with open('D:/abc.txt',mode='r') as files:
        p=files.read(500)
    lang=detect(p)
    entry1.delete(0, END)
    entry1.insert(10,lang)

root=Tk()

def upload():
    
    pic=askopenfilename(filetypes=(("JPEG File", "*.jpg"),("PNG File","*.png")))
    messagebox.showinfo("INFO","Picture uploaded successfully!!!")
    
    pytesseract.pytesseract.tesseract_cmd='C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
    result=pytesseract.image_to_string(pic)
    with open('D:/abc.txt',mode='w+') as files:
        files.write(result)
    text1.focus()
    text1.delete(1.0,END)
    text1.insert(CURRENT,result)
    '''
def advance():
    pic=askopenfilename(filetypes=(("JPEG File", "*.jpg"),("PNG File","*.png")))
    messagebox.showinfo("INFO","Picture uploaded successfully!!!")
    
    img=cv2.imread(pic,0)
    #img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   
    kernel=np.ones((5,5),np.uint8)
    #img=cv2.dilate(img,kernel,iterations=1)
    img=cv2.erode(img,kernel,iterations=1)
    #img=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE,kernel)
    cv2.imwrite("edited.jpg",img)
    cv2.imshow("edited.jpg",img)
    result= pytesseract.image_to_string((Image.open(pic)).convert('L'))
    print(result)
'''
def translate():
    mpb=Progressbar(root, orient="horizontal", length=200, mode="determinate")
    mpb.grid(row=15,column=10)
    mpb["maximum"]=100
    mpb["value"]=99
    
    with open('D:/abc.txt',mode='r') as files:
        p=files.read(500)
        
    translator=Translator(from_lang=entry1.get(),to_lang=entry2.get())
    translation=translator.translate(p)
    
    text2.focus()
    text2.delete(1.0,END)
    text2.insert(CURRENT,translation)
    
root.title("My Translator")

label1=Label(root,text="Multilingual Translator", font="42")
label1.grid(row=1,column=12)

button1=Button(root,text="Take Picture")
button1.grid(row=4,column=12,pady=20)

button2=Button(root,text="Upload Picture",command=upload)
button2.grid(row=5,column=12,pady=20)

label2=Label(root,text="Source language")
label2.grid(row=6,column=8,pady=20)

entry1=Entry(root)
entry1.grid(row=6,column=10,pady=20)

label3=Label(root,text="Don't know the source language?")
label3.grid(row=6,column=11,pady=20)

button2=Button(root,text="Click Here",command=detectsource)
button2.grid(row=6,column=12,pady=20)

label4=Label(root,text="Translate to")
label4.grid(row=8,column=8,pady=20)

entry2=Entry(root)
entry2.grid(row=8,column=10,pady=20)

label5=Label(root, text="Source Text")
label5.grid(row=10,column=10,pady=20)

text1=Text(root,height=15,width=60)
text1.grid(row=12,column=10)

label6=Label(root, text="Translated Text")
label6.grid(row=10,column=15,pady=20)

text2=Text(root,height=15,width=55)
text2.grid(row=12,column=15)

button3=Button(root,text="Translate",command=translate)
button3.grid(row=16,column=12,pady=20)

button4=Button(root,text="FAQ",command=faq)
button4.grid(row=1,column=15,pady=20)

#button3=Button(root,text="Advance",command=advance)
#button3.grid(row=16,column=14,pady=20)

root.mainloop()

'''
pip install translate
pip install autocorrect
pip install ESpeakNG
pip install langdetect
pip install pytesseract'''



