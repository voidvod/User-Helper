#import tkinter as it will be used for the window applicaiton
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter as tk
#we import platform to be able to determine the linux version
import platform
#we import os and subprocess in order to be able to call terminal comamnds
import sys
import os
import subprocess

#empty window open until user closes

win = Tk()
win.title('UserHelper')

#Frame widget dimensions
win.resizable(0, 0)


#Creating local files for Operating system and for logging errors
OSfile = open('OSversion.txt', 'a')
Error_log = open('Error_log.txt', 'a')
#Function to find out the Operating System/package manager
print( platform.platform(), file =OSfile)

#Define button actions

#Variable which is null - check if user input already exists
Pass_value = ''
## Define function that does nothing but passes
def donothing(var=''):
    pass

## Change this to pupup
def New_Window():
    # Grabbing Password from user in variable Pass_value
    global Pass_value
    Pass_value = simpledialog.askstring(title = "Password imput ",
                prompt = "Password: ")
    messagebox.showinfo("User Input is" ,Pass_value)


def button1_action():
            messagebox.showinfo("Update Complete", "Update System Button was pressed"),
            # This is used to test that multiple commands run
            messagebox.showinfo("Test multiple commands", "This shows both commands run"),
            if Pass_value == '': 
               New_Window(),
            os.system('echo ' + Pass_value + ' | sudo -S nala update') 
def button2_action():
    messagebox.showinfo("Upgrade Complete", "Upgrade System Button was pressed"),
    if Pass_value == '': 
               New_Window(),                                           
    os.system('echo ' + Pass_value + ' | sudo -S nala upgrade -y')

def button3_action():
    messagebox.showinfo("Clean System Complete", "Clean System Button was pressed"),
    if Pass_value == '': 
               New_Window(),                                           
    os.system('echo ' + Pass_value + ' | sudo -S nala autoremove -y')

##

# Defining Buttons using other py scripts

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


