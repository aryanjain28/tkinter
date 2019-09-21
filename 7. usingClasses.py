from tkinter import *

class LoginPage:
    def __init__(self, mainWindow):
        self.topframe = Frame(mainWindow)
        self.topframe.pack(side=TOP)

        self.labelFName = Label(self.topframe, text="Enter first name : ")
        self.labelFName.grid(row=0, sticky=W)

        self.entryFname = Entry(self.topframe)
        self.entryFname.grid(row=0,column=1, sticky=E)

        self.labelLName = Label(self.topframe, text="Enter last name : ")
        self.labelLName.grid(row=1, sticky=W)

        self.entryLname = Entry(self.topframe)
        self.entryLname.grid(row=1, column=1, sticky=E)

        self.labelPassword = Label(self.topframe, text="Enter password : ")
        self.labelPassword.grid(row=2, sticky=W)

        self.entryPassword = Entry(self.topframe, show="*")
        self.entryPassword.grid(row=2, column=1, sticky=E)

        self.submitButton = Button(self.topframe, text="Submit", command=self.printMessage)
        self.submitButton.grid(row=3, columnspan=2)

    def printMessage(self):
        print("Registered!")

mainWindow = Tk()

o = LoginPage(mainWindow)

mainWindow.mainloop()
