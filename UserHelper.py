#import tkinter as it will be used for the window applicaiton
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
#we import platform to be able to determine the linux version
import platform
#we import os and subprocess in order to be able to call terminal comamnds
import sys
import os
import subprocess
    
#empty window open until user closes

win = Tk()
win.title('UserHelper')

#Creating local files for Operating system and for logging errors
OSfile = open('OSversion.txt', 'a')
Error_log = open('Error_log.txt', 'a')
#Function to find out the Operating System/package manager
print( platform.platform(), file =OSfile)

#Define button actions

## Change this to pupup
def button1_action():
  messagebox.showinfo("Update Complete", "Update System Button was pressed")

def button2_action():
    messagebox.showinfo("Upgrade Complete", "Upgrade System Button was pressed")

def button3_action():
    messagebox.showinfo("Clean System Complete", "Clean System Button was pressed")
##

# Defining Buttons using other py scripts

#Frame widget dimensions
win.resizable(0, 0)


# Create buttons
##Create button Action

###set position of buttons and text
System_update_button = Button(win, text='System Update', command=button1_action)
System_update_button.grid(row=1, column=0, columnspan=2, padx=50, pady=50)
System_upgrade_button = Button(win, text='System Upgrade', command=button2_action)
System_upgrade_button.grid(row=2, column=0, columnspan=2, padx=50, pady=50)
System_clean_button = Button(win, text='System Clean', command=button3_action)
System_clean_button.grid(row=3, column=0, columnspan=2, padx=50, pady=50)
Exit_button = Button(win, text='Exit', command= win.destroy)
Exit_button.grid(row=4, column=0, columnspan=2, padx=50, pady=50)
#Root mainloop until exit
win.mainloop()
