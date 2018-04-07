# SETUP
from tkinter import *
from tkinter import ttk
from send_sms import send
import parse


#Func def
def func1(message,rawphone):
	fixnum=parse.parse(rawphone)
	send(message,fixnum)
	

root = Tk()

content = ttk.Frame(root)
frame = ttk.Frame()
namelbl = ttk.Label(content, text="Send a Text Notification")
numlbl = ttk.Label(content, text="Phone # to send message to:")
meslbl = ttk.Label(content, text="Your message:")
rawnum = ttk.Entry(content)
mess = Text(content, height=4, width=40)

senbut = ttk.Button(content, text="Send!", command = (lambda: func1(mess.get("1.0",END),rawnum.get())))

content.grid(column=0, row=0)
frame.grid(column=1, row=0, columnspan=5, rowspan=5)
namelbl.grid(column=1, row=0, columnspan=2)
numlbl.grid(column=0, row=1, columnspan=2)
meslbl.grid(column=1, row=2)
rawnum.grid(column=2, row=1)
mess.grid(column=1, row=3)
senbut.grid(column=2, row=3)

root.mainloop()
