from tkinter import *

mainWindow = Tk()

topFrame = Frame(mainWindow)
bottomFrame = Frame(mainWindow)

label1 = Label(
    topFrame,
    text="This is \nlabel one",
    bg='red',
    fg='white',
    bd=3,
    cursor='heart',
    font='serif',
    height=3,
    width=8,
    justify=LEFT,
    padx=8,
    pady=3,
    relief='raised'
)

# flat, groove, raised, ridge, solid, or sunken

label2 = Label(
    topFrame,
    text="This is \nlabel two",
    bg='lightgreen',
    fg='darkgreen',
    bd=5,
    relief=FLAT,
    padx=0,
    pady=3,
    height=4,
    width=7,
    font='cursive',
    cursor='dotbox'
)

label3 = Label(
    topFrame,
    text="This is \nlabel three",
    bg='cyan',
    fg='blue',
    bd=4,
    relief='groove',
    height=10,
    width=10,
    padx=5,
    pady=5,
    font='Times',
    cursor='shuttle'
)

label4 = Label(
    bottomFrame,
    text="This is \nlabel four",
    bg='pink',
    fg='red',
    bd=4,
    relief='flat',
    height=15,
    width=14,
    padx=5,
    pady=5,
    font='Times',
    cursor='mouse'
)

label5 = Label(
    bottomFrame,
    text="This is \nlabel five",
    bg='purple',
    fg='white',
    bd=4,
    relief='raised',
    height=15,
    width=14,
    padx=5,
    pady=5,
    font='Times',
    cursor='spider'

)

topFrame.pack(side=TOP)
bottomFrame.pack(side=BOTTOM)

label1.pack(fill=X)
label2.pack(side=RIGHT)
label3.pack(side=BOTTOM)
label4.pack(side=LEFT,fill=X)
label5.pack(side=RIGHT)

mainWindow.mainloop()
