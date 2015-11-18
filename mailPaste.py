# -*- coding: utf-8 -*-

import pyhk, pyperclip
import sys, time
import win32com.client, pythoncom
import codecs
from Tkinter import * 
from ttk import *

class funWrap:
	def __init__(self, num):
		self.number = num
		
	def fun(self):
		i = self.number
		pythoncom.CoInitialize ()
		shell = win32com.client.Dispatch("WScript.Shell")
		pyperclip.copy(open("mail"+str(i)+".txt").read())
		shell.SendKeys("^v")

def quit():
	hot.end()
	fenetre.destroy()
	root.quit()
	
def instructions():
	s= open("Python.2.7.10\Instructions.txt").read().decode('utf-8')
	ins = Toplevel(fenetre)
	ins.title("MailPaste - Instructions")
	label = Label(ins, text=s, justify = LEFT)
	label.pack(padx=10, pady=10)
	closeButton=Button(ins, text="Fermer", command=ins.destroy)
	closeButton.pack(padx=10, pady=10, side=RIGHT)
	closeButton.focus()
	ins.resizable(width=FALSE, height=FALSE)
	ins.iconbitmap('Python.2.7.10\clipboard.ico')
	ins.focus()
	ins.mainloop()
	

#create pyhk class instance
hot = pyhk.pyhk()
key = 'Lcontrol'
for i in range(9):
	t = funWrap(i)
	hot.addHotkey([key, str(i)], t.fun, isThread = True)


#graphical part
fenetre = Tk()
fenetre.title("MailPaste")
fenetre.iconbitmap('Python.2.7.10\clipboard.ico')
fenetre.protocol('WM_DELETE_WINDOW', quit)
cc = Label(fenetre, text="Copyright (C) 2015 LM.Garret", justify = LEFT)
cc.pack(padx=20, pady=20)
quitButton=Button(fenetre, text="Quitter", command=quit)
quitButton.pack(padx=10, pady=10, side=RIGHT)
quitButton.focus()
insButton = Button(fenetre, text="Instructions", command=instructions)
insButton.pack(padx=10, pady=10, side=RIGHT)
fenetre.resizable(width=FALSE, height=FALSE)
fenetre.mainloop()

#start looking for hotkey.	
hot.start()
