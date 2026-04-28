from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

pyCode = """
import tkinter 
import pandas as pd
import tkinter as tk
import json
import jwt
#from py_jwt_validator import PyJwtValidator, PyJwtException
import clipboard
import pyperclip
from PIL import Image
from PIL import ImageTk
import time

class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Scanner QR Data')
        
        self.lbl3=Label(win, text='Result')
        self.t1=Entry(bd=3)
        
        self.t3=Text()
        self.btn1 = Button(win, text='Get_Data')
        self.btn2=Button(win, text='New_Scan')
        self.btn3=Button(win, text='Result')
        #self.btn4=Button(win, text='BULK_SCAN')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50,height = 30, width = 300)
        
        self.b1=Button(win, text='Evaluate QR', command=self.Get_Data, bg='green', fg='black')
        self.b2=Button(win, text='New Scan', bg='brown', fg='white')
        #self.b3=Button(win, text='BULK SCAN', command=self.BULK_SCAN,bg='blue', fg='white')
        self.b2.bind('<Button-1>', self.New_Scan)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        #self.b3.place(x=300, y=150)
        self.t3.place(x=200, y=200,height = 400, width = 600)
   
    def New_Scan(self, event):
        self.t1.delete(0, END)
        self.t3.delete(1.0, END)
   
        

window=tk.Tk()

mywin=MyWindow(window)
window.title('QR Netra - v4.0 Powered by TESLAA-Appario QR Scan')
window.geometry("1910x1070+10+10")
window.mainloop()

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=400,
    chunk_overlap=0,
)


result = splitter.split_text(pyCode)
print(len(result))

for i in result:
    print(f'Chunk: "{i}"\n')
    print("******************************"*10)  

