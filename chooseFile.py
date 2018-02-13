#! Python 3.4
"""
Open a file dialog window in tkinter using the filedialog method.
Tkinter has a prebuilt dialog window to access files.
This example is designed to show how you might use a file dialog askopenfilename
and use it in a program.
"""

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

import serial
import time

root = Tk(  )

#This is where we lauch the file manager bar.
def OpenFile():
    name = askopenfilename(initialdir="../",
                           filetypes =(("HPGL Plotter File", "*.hpgl"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print (name)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        s = serial.Serial("/dev/ttyS4")
        s.write(open(name,'rb').read())
        time.sleep(1)
        s.setDTR(0)
    except:
        print("No file exists")


Title = root.title( "File Opener")
label = ttk.Label(root, text ="Use the file button to choose a file",foreground="red",font=("Helvetica", 16))
label.pack()

#Menu Bar

menu = Menu(root)
root.config(menu=menu)

#file = Menu(menu)

menu.add_command(label = 'Open', command = OpenFile)
menu.add_command(label = 'Exit', command = lambda:exit())

#menu.add_cascade(label = 'File', menu = file)





root.mainloop()

'''
RESULTS:
>>>
C:/Users/Scott/Documents/Programming/json/test.txt
"I like to move it, groove it!"
'''
