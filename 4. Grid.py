from tkinter import *

mainWindow = Tk()

mainWindow.title("Aryan's box")

labelFName = Label(mainWindow, text="First name : ")
entryFName = Entry(mainWindow, font='cursive')

labelLName = Label(mainWindow, text="Last name : ")
entryLName = Entry(mainWindow, font='cursive')

labelPassword = Label(mainWindow, text="Password : ")
entryPassword = Entry(mainWindow, font='cursive', show="*")

submitButton = Button(mainWindow, text='SUBMIT!', relief='raised', bd=3, fg='white', bg='red')

labelFName.grid(row=0, column=0, sticky=W, ipadx=5, ipady=5)
entryFName.grid(row=0, column=1, sticky=E, padx=3, pady=3)

labelLName.grid(row=1, column=0, sticky=W, ipadx=5, ipady=5)
entryLName.grid(row=1, column=1, sticky=E, padx=3, pady=3)

labelPassword.grid(row=2, column=0, sticky=W, ipadx=5, ipady=5)
entryPassword.grid(row=2, column=1, sticky=E, padx=3, pady=3)

submitButton.grid(row=3, column=0, columnspan=2, padx=6, pady=6)

mainWindow.mainloop()
