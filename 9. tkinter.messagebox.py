from tkinter import *
import tkinter.messagebox


def name(event):
    tkinter.messagebox.showinfo('Hello!', "Hello! My name is Aryan Jain!!")

def ques(event):
    answer = tkinter.messagebox.askquestion('Ques', 'Is coding fun?')
    if answer=='yes':
        print("Answer is a yes!!!")
    else:
        print("Answer is a no!!!")

def err(event):
    tkinter.messagebox.showerror('Error', 'Here comes an error!')

def warn(event):
    tkinter.messagebox.showwarning('Warning!', 'This is a warninig!')

def ok(event):
    tkinter.messagebox.askokcancel('Ok/Cancel', 'Answer in ok or cancel!')

def yn(event):
    answer = tkinter.messagebox.askyesno('Yes/No', "Answer in yes or no!")
    if answer==True:
        print("Answer is a yes!!!")
    else:
        print("Answer is a no!!!")


def retry(event):
    tkinter.messagebox.askretrycancel('Retry', 'Try, try but dont cry!')



mainWindow = Tk()

button1 = Button(mainWindow, text="Name", bd=4, bg='blue', fg='white', relief='raised')
button1.bind('<Button-1>',func=name)
button1.pack(side=LEFT,  fill=X)

button2 = Button(mainWindow, text="Ques", bd=4, bg='red', fg='white', relief='raised')
button2.bind('<Button-1>',func=ques)
button2.pack(side=LEFT,  fill=X)

button3 = Button(mainWindow, text="Error", bd=4, bg='darkgreen', fg='white', relief='raised')
button3.bind('<Button-1>',func=err)
button3.pack(side=LEFT,  fill=X)

button4 = Button(mainWindow, text="warn", bd=4, bg='cyan', fg='blue', relief='raised')
button4.bind('<Button-1>',func=warn)
button4.pack(side=LEFT,  fill=X)

button5 = Button(mainWindow, text="OK", bd=4, bg='black', fg='white', relief='raised')
button5.bind('<Button-1>',func=ok)
button5.pack(side=LEFT,  fill=X)

button6 = Button(mainWindow, text="YN", bd=4, bg='yellow', fg='black', relief='raised')
button6.bind('<Button-1>',func=yn)
button6.pack(side=LEFT,  fill=X)

button7 = Button(mainWindow, text="retry", bd=4, bg='pink', fg='black', relief='raised')
button7.bind('<Button-1>',func=retry)
button7.pack(side=LEFT,  fill=X)

mainWindow.mainloop()
