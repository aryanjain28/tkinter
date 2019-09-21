from tkinter import *

mainWindow = Tk()

canvas = Canvas(
    mainWindow,
    height=250,
    width=250,
    bg='lightgreen',
    bd=4,
    cursor='heart'

)
canvas.pack(side=TOP)

blackline = canvas.create_line(0,0,250,125,width=5)
redline = canvas.create_line(0,250,250,125, fill='red', width=5)
greenbox = canvas.create_rectangle(10,10,100,120,fill='darkgreen')
oval = canvas.create_oval(10, 70, 250, 200, fill='red')
arc = canvas.create_arc(50,50,200,200, extent=150, fill='blue')

mainWindow.mainloop()
