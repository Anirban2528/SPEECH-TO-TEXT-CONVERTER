import speech_recognition as s
from tkinter import *
from pathlib import Path
import time
import urllib.request
import os

root=Tk()
root.title('Speech to text converter')
root.geometry("300x300")
root.configure(background='#171717')

if os.path.isdir(str(Path.home()/'Recordings'))==False:
  os.mkdir(str(Path.home()/'Recordings'))

class Fun:
  def __init__(self,txt1,root):
    self.txt1=txt1
    self.root=root
    
  def des(self):
    self.lab2.destroy()
    self.clr.destroy()
    
  def fun(self):
    if self.txt1.get()=='':
      self.lab2=Label(self.root,text='Please Enter File Name',bg='#171717',fg='white')
      self.lab2.pack()
      self.clr=Button(self.root,text='Clear',font=9,command=self.des,bg='#4682B4',fg='white')
      self.clr.pack()
      return
    
    try:
      urllib.request.urlopen('https://www.google.com/')
    except:
      self.lab2=Label(self.root,text='Internet connection unavailaible!',bg='#171717',fg='white')
      self.lab2.pack()
      self.clr=Button(self.root,text='Clear',font=9,command=self.des,bg='#4682B4',fg='white')
      self.clr.pack()
      return
      
    r=s.Recognizer()
    with s.Microphone() as source:
      r.pause_treshold=0.8
      audio=r.listen(source)
      
      try:
        query=r.recognize_google(audio, language='en-in')
      except Exception as e:
        print(e)
        return
      if query.lower()=="exit": exit(0)
      output=query.replace(' comma',', ').replace(' full stop','. ').replace(' coma',', ').replace('full stop','.')

    t=self.txt1.get()+'.txt'
    try:
      with open(str(Path.home()/'Recordings'/t),'r') as rec:
        self.data=rec.read()
        self.data=self.data.replace('  ',' ')
      with open(str(Path.home()/'Recordings'/t),'w') as rec:
        rec.write(self.data+' '+output)
      self.lab2=Label(self.root,text=self.data+' '+output,font=9,bg='#171717',fg='white')
      self.lab2.pack()
      self.clr=Button(self.root,text='clear',font=9,command=self.des,bg='#4682B4',fg='white')
      self.clr.pack()
    
    except:
      with open(str(Path.home()/'Recordings'/t),'w') as rec:
        rec.write(output)
        self.lab2=Label(self.root,text=output,font=9,fg='white',bg='#171717')
      self.lab2.pack()
      self.clr=Button(self.root,text='clear',font=9,command=self.des,bg='#4682B4',fg='white')
      self.clr.pack()
        
        
lab1=Label(root,text="Enter file name:",font=9,fg='white',bg='#171717')
lab1.pack()
txt1=Entry(root,width=40)
txt1.pack()
obj=Fun(txt1,root)
btn1=Button(root,text='Record',bg='red',font=9,command=obj.fun,fg='white')
btn1.pack()
root.mainloop()