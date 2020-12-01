#!/usr/bin/python

"""import tkinter
top = tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()
"""

from tkinter import *
master = Tk() 
Label(master, text='A1').grid(row=0) 
Label(master, text='A2').grid(row=1) 
e1 = Entry(master) 
e2 = Entry(master) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
master.title("Secant Method")
master.geometry("400x300+10+10")
mainloop() 