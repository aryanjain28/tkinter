from tkinter import *

mainWindow = Tk()
topFrame = Frame(mainWindow)
bottomFrame = Frame(mainWindow)

labelFName = Label(topFrame, text="Full Name : ")
entryFName = Entry(
    topFrame,
    bg='lightgreen',
    fg='darkgreen',
    bd=3,
    width=23,
    font='cursive',
    justify=CENTER,
    cursor='mouse',
    relief = 'raised',
    selectforeground = 'white',
    selectbackground = 'blue',
    selectborderwidth= 4,
    show = "",
    state = NORMAL
)

labelPassword = Label(bottomFrame, text="Password : ")
entryPassword = Entry(
    bottomFrame,
    bg='lightgreen',
    fg='darkgreen',
    bd=3,
    width=23,
    font='cursive',
    justify=CENTER,
    cursor='mouse',
    relief = 'raised',
    selectforeground = 'white',
    selectbackground = 'blue',
    selectborderwidth= 4,
    show = "*"
)

topFrame.pack(side=TOP)
labelFName.pack(side=LEFT)
entryFName.pack()

bottomFrame.pack(side=BOTTOM)
labelPassword.pack(side=LEFT)
entryPassword.pack()

mainWindow.mainloop()
