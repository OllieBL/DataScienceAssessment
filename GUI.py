from tkinter import *
from functions import *

class Weather_App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("200x200")
        self.firstPage()
        self.location_var = StringVar()
        self.apiKey_var = StringVar()

    def firstPage(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=200, height=200)
        self.frame1.pack()
        self.button1 = Button(self.frame1, text='Go to page 2', command=self.present)
        self.button1.pack()

    def present(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=200, height=200)
        self.frame2.pack()
        self.locationEntry = Entry(self.frame2, textvariable=self.location_var)
        self.locationEntry.pack()
        self.APIKeyEntry = Entry(self.frame2, textvariable=self.apiKey_var)
        self.APIKeyEntry.pack()
        self.submitButton = Button(self.frame2, text='Submit', command=self.end)
        self.submitButton.pack()
    
    def end(self):
        apiKey = self.apiKey_var.get()
        location = self.location_var.get()
        print(Search_API(apiKey, location, 'current'))


root = Tk()
Weather_App(root)
root.mainloop()