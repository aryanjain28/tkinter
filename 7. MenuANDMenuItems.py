from tkinter import *

mainWindow = Tk()

def newProject():
    print("New project")
def save():
    print("Save project")
def saveAs():
    print("Save As..")
def Exit():
    print("Thank you!")
    mainWindow.quit()

def copy():
    print("Copied")
def cut():
    print("Cut")
def paste():
    print("Pasted")

def nothing():
    print("I did nothing!")


menuBar = Menu(mainWindow,  bg='black', fg='white', font='cursive')          #making a menu bar
mainWindow.config(menu=menuBar)                                             #adding menubar to mainwindow

#making menu items and customizing :
menuItem1 = Menu(
    menuBar,
    bg='red',
    fg='white',
    bd=4,
    activebackground='white',
    activeforeground='red',
    activeborderwidth=3,
    cursor='heart',
    font='cursive',
    tearoff=0

)

menuItem2 = Menu(
    menuBar,
    bg='lightgreen',
    fg='darkgreen',
    bd=4,
    activebackground='darkgreen',
    activeforeground='lightgreen',
    activeborderwidth=3,
    cursor='dot',
    font='cursive',
    tearoff=0
)


menuItem3 = Menu(
    menuBar,
    bg='cyan',
    fg='blue',
    bd=4,
    activebackground='blue',
    activeforeground='white',
    activeborderwidth=3,
    cursor='mouse',
    font='cursive',
    tearoff=0
)

#adding  menuitems to menubar :
menuBar.add_cascade(menu=menuItem1, label="File")
menuBar.add_cascade(menu=menuItem2, label="Edit")
menuBar.add_cascade(menu=menuItem3, label="View")

#now adding items to menuitem1 :
menuItem1.add_command(label="New Project", command=newProject)
menuItem1.add_separator()
menuItem1.add_command(label="Save", command=save)
menuItem1.add_command(label="Save As", command=saveAs)
menuItem1.add_separator()
menuItem1.add_command(label="Exit", command=Exit)

#now adding items to menuitem2 :
menuItem2.add_command(label="Copy", command=copy)
menuItem2.add_command(label="Cut", command=cut)
menuItem2.add_separator()
menuItem2.add_command(label="Paste", command=paste)

#now adding items to menuitem3 :
menuItem3.add_command(label="Do nothing", command=nothing)

mainWindow.mainloop()
