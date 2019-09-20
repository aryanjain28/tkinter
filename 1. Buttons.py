from tkinter import *

mainWindow = Tk()

topFrame = Frame(mainWindow)
bottomFrame = Frame(mainWindow)


button1 = Button(
    topFrame,
    text="This is \nButton one",
    fg='red',
    bg='pink',
    bd=3,
    activebackground='red',
    activeforeground='pink',
    font='serif',
    height=2,
    width=8,
    justify=LEFT,
    padx=23,
    pady=23,
    relief=SUNKEN,
    underline=16,
)

button2 = Button(
    topFrame,
    text="This is \nButton two",
    fg='blue',
    bg='cyan',
    bd=3,
    activeforeground='cyan',
    activebackground='blue',
    font='cursive',
    height=2,
    width=8,
    justify=CENTER,
    padx=34,
    pady=12,
    relief=RAISED,
    underline=16,
)

button3 = Button(
    topFrame,
    text="This is \nButton three",
    fg='darkgreen',
    bg='lightgreen',
    bd=3,
    activeforeground='lightgreen',
    activebackground='darkgreen',
    font='Helvetica',
    height=2,
    width=8,
    justify=RIGHT,
    padx=3,
    pady=4,
    relief=GROOVE,
    underline=16,
)

button4 = Button(
    bottomFrame,
    text="This is \nButton four",
    fg='black',
    bg='yellow',
    bd=3,
    activeforeground='yellow',
    activebackground='black',
    font='Times',
    height=2,
    width=8,
    justify=CENTER,
    padx=0,
    pady=0,
    relief=RIDGE,
    underline=16,
)


topFrame.pack()
bottomFrame.pack(side=BOTTOM)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

mainWindow.mainloop()
