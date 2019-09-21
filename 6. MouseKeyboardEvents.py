from tkinter import *

mainWindow = Tk()

def left(event):
    print("Left")

def middle(event):
    print(event.type)

def doubleTap(event):
    print("Double click")

def middlerelease(event):
    print("Middle release")

def motion(event):
    print("("+str(event.x)+","+str(event.y)+")")

def enter(event):
    print("Entered")

def leave(event):
    print("Left")

def leftKey(event):
    print('Left key pressed')

def rightKey(event):
    print('Right key pressed')

def upKey(event):
    print('Up key pressed')

def downKey(event):
    print('Down key pressed')

def key(event):
    print('Key pressed', repr(event.char))

def focusIn(event):
    print('Focused')

def focusOut(event):
    print('Out of Focus')

emptyFrame = Frame(mainWindow, width=250,  height=250)

#Mouse events :
emptyFrame.bind('<Button-2>', middle)
emptyFrame.bind('<Double-Button-1>', doubleTap)
emptyFrame.bind('<ButtonRelease-2>', middlerelease)
emptyFrame.bind('<B3-Motion>', motion)
emptyFrame.bind('<Enter>', enter)
emptyFrame.bind('<Leave>', leave)

#KeyBoard events :
mainWindow.bind('<Left>', leftKey)
mainWindow.bind('<Right>', rightKey)
mainWindow.bind('<Up>', upKey)
mainWindow.bind('<Down>', downKey)
mainWindow.bind('<Key>', key)   #all the keys on keyboard
mainWindow.bind('<FocusIn>', focusIn)
mainWindow.bind('<FocusOut>', focusOut)

emptyFrame.pack()

mainWindow.mainloop()
