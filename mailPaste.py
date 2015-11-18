# -*- coding: utf-8 -*-

import pyhk, pyperclip
import sys, time
import win32com.client
import codecs
from Tkinter import * 
from ttk import *


fenetre = Tk()

def f0():
	#print ("Mail 0")
	shell = win32com.client.Dispatch("WScript.Shell")
	pyperclip.copy(open("mail0.txt").read())
	shell.SendKeys("^v")
	#del_last(shell)
	
def f1():
	#print ("Mail 1")
	shell = win32com.client.Dispatch("WScript.Shell")
	pyperclip.copy(open("mail1.txt").read())
	shell.SendKeys("^v")
	#del_last(shell)
	
def f2():
	#print ("Mail 2")
	shell = win32com.client.Dispatch("WScript.Shell")
	pyperclip.copy(open("mail2.txt").read())
	shell.SendKeys("^v")
	#del_last(shell)
		
def f3():
	#print ("Mail 3")
	shell = win32com.client.Dispatch("WScript.Shell")
	pyperclip.copy(open("mail3.txt").read())
	shell.SendKeys("^v")
	#del_last(shell)
		
def f4():
	#print ("Mail 4")
	shell = win32com.client.Dispatch("WScript.Shell")
	pyperclip.copy(open("mail4.txt").read())
	shell.SendKeys("^v")
	#del_last(shell)
		
def f5():
	#print ("Mail 5")
	shell = win32com.client.Dispatch("WScript.Shell")
	pyperclip.copy(open("mail5.txt").read())
	shell.SendKeys("^v")
	#del_last(shell)
		
def f6():
	#print ("Mail 6")
	shell = win32com.client.Dispatch("WScript.Shell")
	pyperclip.copy(open("mail6.txt").read())
	shell.SendKeys("^v")
	#del_last(shell)	
	
def f7():
	#print ("Mail 7")
	shell = win32com.client.Dispatch("WScript.Shell")
	pyperclip.copy(open("mail7.txt").read())
	shell.SendKeys("^v")	
	#del_last(shell)
	
def f8():
	#print ("Mail 8")
	shell = win32com.client.Dispatch("WScript.Shell")
	pyperclip.copy(open("mail8.txt").read())
	shell.SendKeys("^v")
	#del_last(shell)	
	
def f9():
	#print ("Mail 9")
	shell = win32com.client.Dispatch("WScript.Shell")
	pyperclip.copy(open("mail9.txt").read())
	shell.SendKeys("^v")
	#del_last(shell)

def quit():
	fenetre.destroy()
	root.quit()
	
def instructions():
	s= open("Instructions.txt").read().decode('utf-8')
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
key = 'Ctrl'
hot.addHotkey([key,'0'],f0)
hot.addHotkey([key,'1'],f1)
hot.addHotkey([key,'2'],f2)
hot.addHotkey([key,'3'],f3)
hot.addHotkey([key,'4'],f4)
hot.addHotkey([key,'5'],f5)
hot.addHotkey([key,'6'],f6)
hot.addHotkey([key,'7'],f7)
hot.addHotkey([key,'8'],f8)
hot.addHotkey([key,'9'],f9)


#graphical part
fenetre.title("MailPaste")
fenetre.iconbitmap('Python.2.7.10\clipboard.ico')
cc = Label(fenetre, text="Copyright (C) 2015 LM.Garret", justify = LEFT)
cc.pack(padx=20, pady=20)
quitButton=Button(fenetre, text="Quitter", command=quit)
quitButton.pack(padx=10, pady=10, side=RIGHT)
quitButton.focus()
insButton = Button(fenetre, text="Instructions", command=instructions)
insButton.pack(padx=10, pady=10, side=RIGHT)
fenetre.resizable(width=FALSE, height=FALSE)


#start looking for hotkey.	
hot.start()
fenetre.mainloop()
