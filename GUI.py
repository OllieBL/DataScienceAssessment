from tkinter import *
from functions import *


class Weather_App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x500")
        self.APISelection()

        # These variables are string variables that allow the location and api key to be used in other parts of the code
        self.location_var = StringVar()
        self.apiKey_var = StringVar()
        self.locationData = ''


    # This function is the first selection page for the user, it allows the user to pick what API they want to search; current, history, or forecast
    def APISelection(self):

        # This for loop clears the window for the new page
        for i in self.master.winfo_children():
            i.destroy()

        # This section is all the components
        # This line creates and packs the frame
        self.frame1 = Frame(self.master, width=1000, height=500)
        self.frame1.pack()
        # This line creates and packs the button to select the current API 
        self.currentButton = Button(self.frame1, text='Current API', command=self.current)
        self.currentButton.pack()
        # This line creates and packs the button to select the forecast API
        self.forecastButton = Button(self.frame1, text='Forecast API', command=self.current)
        self.forecastButton.pack()


    # This function is the page that allows the user to select the location that they wnat to search for when they choose the 'current' API
    def current(self):

        # This for loop deletes the previous page for the new page to go on top of
        for i in self.master.winfo_children():
            i.destroy()


        # This section creates page and all the components on it
        # This line creates and packs the frame
        self.frame2 = Frame(self.master, width=1000, height=500)
        self.frame2.pack()
        # This line creates and packs the text box for the user to enter the location
        self.locationEntry = Entry(self.frame2, textvariable=self.location_var)
        self.locationEntry.pack()
        # This line creates and packs the text box for the user to enter their API key
        self.APIKeyEntry = Entry(self.frame2, textvariable=self.apiKey_var)
        self.APIKeyEntry.pack()
        # This line is the button that the user clicks on to confirm their location choice and API key
        self.submitButton = Button(self.frame2, text='Submit', command=lambda: [self.functionsRunner(), self.displayCurrent()])
        self.submitButton.pack()

    def displayCurrent(self):
        
        locationData = makeDataReadable(self.locationData)

        # This for loop deletes the previous page for the new page to go on top of
        for i in self.master.winfo_children():
            i.destroy()

        # This section creates page and all the components on it
        # This line creates and packs the frame
        self.frame4 = Frame(self.master, width=1000, height=500)
        self.frame4.pack()

        #
        for i in range(len(locationData)):
            for j in range(len(locationData[i])):
                self.currentTable = Entry(self.frame4, width=50)
                self.currentTable.grid(row=j, column=i)
                self.currentTable.insert(END, locationData[i][j])


        

    # This function is a collection of the various functions that the code will run from the functions.py file
    def functionsRunner(self):
        apiKey = self.apiKey_var.get()
        location = self.location_var.get()
        self.locationData = CurrentAPISearch(apiKey, location)
        print(self.locationData)

def runGUI():
    root = Tk()
    Weather_App(root)
    root.mainloop()


runGUI()