from tkinter import *

count1 = 0
count2 = 0

mainWindow = Tk()

def getName(x):
    global count1
    global count2
    c=0

    if x=='Button 1':
        count1+=1
        c=count1
    else:
        count2+=1
        c=count2

    if c != 1:
        print("You have clicked "+x+" "+str(c)+" times.")
    else:
        print("You have clicked me " +x+" "+ str(c) + " time.")

button1 = Button(mainWindow, text="Button 1", command= lambda : getName('Button 1'))
button2 = Button(mainWindow, text="Button 2", command= lambda : getName('Button 2'))

button1.pack()
button2.pack()

mainWindow.mainloop()
