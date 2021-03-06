﻿# -*- coding: utf-8 -*-

import pyhk, pyperclip
import sys, time
import win32com.client, pythoncom
import win32clipboard
import codecs
from Tkinter import * 
from ttk import *
from subprocess import call

class funWrap:
	def __init__(self, num):
		self.number = num
		
	def paste(self):
		i = self.number
		pythoncom.CoInitialize ()
		shell = win32com.client.Dispatch("WScript.Shell")
		pyperclip.copy(open("Data\\"+str(i)+".txt").read())
		shell.SendKeys("^v")
		
	def copy(self):
		pythoncom.CoInitialize ()
		shell = win32com.client.Dispatch("WScript.Shell")
		shell.SendKeys("^c")
		win32clipboard.OpenClipboard()
		clipData = win32clipboard.GetClipboardData()
		win32clipboard.CloseClipboard()
		f = open("Data\\"+str(self.number)+".txt", 'w')
		f.write(clipData)
		f.close()

class hotKWrap:
	def __init__(self):
		self.hk = pyhk.pyhk()
		self.initHK()
		
	def restartHK(self, e = None):
		self.end()
		call(["start", "MultiClip.exe", str(fenetre.winfo_x()), str(fenetre.winfo_y())], shell=True)
		quitFun()
		
	def initHK(self):
		key1 = 'Lcontrol'
		key2 = 'Rcontrol'
		for i in range(10):
			t = funWrap(i)
			self.hk.addHotkey([key1, str(i)], t.paste, isThread = True)
			self.hk.addHotkey([key2, str(i)], t.copy)
			
			
	def start(self):
		self.hk.start()
		print("HotKWrap started")

	def end(self):
		self.hk.end()
		print("HotKWrap stopped")
		
class WindowWrap:
	def __init__(self, parent):
		self.w = Toplevel(parent)
		
	def destroy(self, e = None):
		self.w.destroy()
		
		
def quitFun(e = None):
	hotWrap.end()
	fenetre.destroy()
	quit()
	
def instructions(e = None):
	s= open("Data\Instructions.txt").read().decode('utf-8')
	ins = WindowWrap(fenetre)
	ins.w.title("MultiClip - Instructions")
	label = Label(ins.w, text=s, justify = LEFT)
	label.pack(padx=10, pady=5)
	closeButton=Button(ins.w, text="Ok", command=ins.destroy)
	closeButton.bind("<Return>", ins.destroy)
	closeButton.bind("<KP_Enter>", ins.destroy) 
	closeButton.pack(padx=10, pady=10, side=RIGHT)
	closeButton.focus()
	ins.w.resizable(width=FALSE, height=FALSE)
	ins.w.iconbitmap('Data\clipboard.ico')
	ins.w.focus()
	ins.w.mainloop()

#create pyhk class instance
hotWrap = hotKWrap()

#graphical part
fenetre = Tk()
pos = '+'+sys.argv[1]+'+'+sys.argv[2]
fenetre.geometry(pos)
cc = Label(fenetre, text="Copyright (C) 2015 LM.Garret", justify = LEFT)
cc.pack(padx=20, pady=20)
quitButton=Button(fenetre, text="Quitter", command=quitFun)
quitButton.bind("<Return>", quitFun)
quitButton.bind("<KP_Enter>", quitFun) 
quitButton.pack(padx=7, pady=10, side=RIGHT)
quitButton.focus()
insButton = Button(fenetre, text="Instructions", command=instructions)
insButton.bind("<Return>", instructions)
insButton.bind("<KP_Enter>", instructions) 
insButton.pack(padx=7, pady=10, side=RIGHT)
refreshButton = Button(fenetre, width = 3, text="↺", command=hotWrap.restartHK)
refreshButton.bind("<Return>", hotWrap.restartHK)
refreshButton.bind("<KP_Enter>", hotWrap.restartHK) 
refreshButton.pack(padx=7, pady=10, side=RIGHT)

fenetre.resizable(width=FALSE, height=FALSE)
fenetre.title("MultiClip")
fenetre.iconbitmap('Data\clipboard.ico')
fenetre.mainloop()

fenetre.protocol('WM_DELETE_WINDOW', quitFun)

#start looking for hotkey.	
hotWrap.start()
