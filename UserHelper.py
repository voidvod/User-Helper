#import tkinter as it will be used for the window applicaiton
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import simpledialog
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
###delete### OSfile = open('OSversion.txt', 'a')
Error_log = open('Error_log.txt', 'a')
#Function to find out the Operating System/package manager
###delete### print( platform.platform(), file =OSfile)

#Define button actions

#Variable which is null - check if user input already exists
Pass_value = ''
## Define function that does nothing but passes
def donothing(var=''):
    pass

## Change this to pupup

# Open up packmanager.list in order to read all of the currently supported pack managers
file_read = open('_internal/Util/packagemanager.list', "r")
# transform packmanager list in raw data packmanager_data
packmanager_data = file_read.read()
#close the open file packmanager.list
file_read.close()

#transform the raw data in a list
packmanager_list = packmanager_data.splitlines()

def Update(Pass, act_inv):
    if act_inv == "Update":
        for packmanager in packmanager_list:
            cmd = os.system("which " + packmanager)
            cmd_upd = f'echo {Pass} | sudo -S {packmanager} update'

            if cmd!=256:
                # APT, APT-GET, NALA
                if packmanager in ["apt","apt-get","nala"]:                                                     
                    os.system(cmd_upd)
                # DNF
                elif packmanager in ["dnf"]:
                    os.system(cmd_upd)
                    dnf_update  = f'echo {Pass} | sudo -S {packmanager} update'
                    os.system(dnf_update)
                # SNAP
                elif packmanager in ["snap"]:
                    snap_update = f'echo {Pass} | sudo -S {packmanager} refresh'
                    os.system(snap_update)
                # YUM
                elif packmanager in ["yum"]:
                    yum_update = f'echo Pass | sudo - S {packmanager} check-update'
                    os.system(yum_update)
                    os.system(cmd_upd)
                # ZYPPER
                elif packmanager in ["zypper"]:
                    os.system(cmd_upd)
                    zypper_upd = "echo {Pass} | sudo -S {packmanager} up"
                    os.system(zypper_upd)
                # PIP
                elif packmanager in ["pip"]:
                    pip_upd = f'{packmanager} install --upgrade pip'
                    os.system(pip_upd)
                # FLATPAK
                elif packmanager in ["flatpak"]:
                    os.system(cmd_upd)
                # APK, APK-TOOLS
                elif packmanager in ["apk-tools", "apk"]:
                    apk_upd = f'echo {Pass} |sudo -S apk update && upgrade -y'
                    os.system(apk_upd)

### need to finish this
def Upgrade(Pass, act_inv):
    if act_inv == "Upgrade":
        for packmanager in packmanager_list:
            cmd = os.system("which " + packmanager)
            cmd_upg = f'echo {Pass} | sudo -S {packmanager} upgrade -y'

            if cmd!=256:
                # APT, APT-GET, NALA
                if packmanager in ["apt","apt-get","nala"]:                                                     
                    os.system(cmd_upg)
                # DNF
                elif packmanager in ["dnf"]:
                    dnf_run = f'echo {Pass} | sudo -S {packmanager} update -y'
                    os.system(dnf_run)
                # SNAP
                elif packmanager in ["snap"]:
                    snap_upgrade = f'echo {Pass} | sudo -S {packmanager} refresh'
                    os.system(snap_upgrade)
                # YUM
                elif packmanager in ["yum"]:
                    yum_update = f'echo {Pass} | sudo - S {packmanager} check-update'
                    os.system(yum_update)
                    os.system(cmd_upg)
                # ZYPPER
                elif packmanager in ["zypper"]:
                    zypper_upd_b_upg = f'echo {Pass} | sudo -S {packmanager} && sudo -S {packmanager} update '
                    os.system(zypper_upd_b_upg)
                    zypper_upg = f'echo {Pass} | sudo -S {packmanager} up'
                    os.system(zypper_upd)
                # PIP
                elif packmanager in ["pip"]:
                    pip_upg = f'{packmanager} install --upgrade pip'
                    os.system(pip_upg)
                # FLATPAK
                elif packmanager in ["flatpak"]:
                    os.system(cmd_upg)
                # APK, APK-TOOLS
                elif packmanager in ["apk-tools", "apk"]:
                    apk_upg = f'echo {Pass} |sudo -S apk update && upgrade -y'
                    os.system(apk_upg)

def System_Clean(Pass, act_inv):
    if act_inv == "System Clean":
        for packmanager in packmanager_list:
            cmd = os.system("which " + packmanager)
            cmd_clean = f'echo {Pass} | sudo -S {packmanager} autoremove -y'

            if cmd!=256:
                # APT, APT-GET, NALA
                if packmanager in ["apt","apt-get","nala"]:
                    os.system(cmd_clean)
                # DNF
                elif packmanager in ["dnf"]:
                    os.system(cmd_clean)
                # SNAP
                elif packmanager in ["snap"]:
                    os.system("pushd ./_internal")
                    os.system("pushd ./Util")
                    snap_cmd = f'echo {Pass} | sudo -S bash Snap_clean.sh'
                    os.system("popd")
                    os.system("popd")
                # YUM
                elif packmanager in ["yum"]:
                    os.system(cmd_clean)
                # ZYPPER
                elif packmanager in ["zypper"]:
                    zypper_clean = f'echo {Pass} | sudo -S {packmanager} cc -a'
                    os.system(zypper_clean)
                # PIP
                # no pip autoremove at the moment ### check later

                # FLATPAK
                elif packmanager in ["flatpak"]:
                    flatpak_clean = f'{packmanager} uninstall --unused'
                    flatpak_repair = f'{packmanager} repair'
                    os.system(flatpak_clean)
                    os.system(flatpak_repair)
                # APK, APK-TOOLS
                ## APK seems to have a better way of uninstalling packages


###


def New_Window():
    # Grabbing Password from user in variable Pass_value
    global Pass_value
    Pass_value = simpledialog.askstring(title = "Password imput ",
                prompt = "Password: ", show='*')


def button1_action():
    action_invoked = "Update"
    if Pass_value == '': 
        New_Window(),
    Update(Pass_value, action_invoked), 
    messagebox.showinfo("Update Complete", "Update System Button was completed")
    # This is used to test that multiple commands run
    #messagebox.showinfo("Test multiple commands", "This shows both commands run"),

def button2_action():
    action_invoked = "Upgrade"
    if Pass_value == '': 
        New_Window(),                                           
    Upgrade(Pass_value, action_invoked),
    messagebox.showinfo("Upgrade Complete", "Upgrade System Button was completed")

def button3_action():
    action_invoked = "System Clean"
    if Pass_value == '': 
       New_Window(),                                           
    System_Clean(Pass_value, action_invoked),
    messagebox.showinfo("Clean System Complete", "System Clean has completed"),

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
Error_log.close()
win.mainloop()

