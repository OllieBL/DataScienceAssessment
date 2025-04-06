from tkinter import *
from functions import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class Weather_App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x500")
        self.APISelection()

        # These variables are string variables that allow the location and api key to be used in other parts of the code
        self.location_var = StringVar()
        self.apiKey_var = StringVar()
        self.locationData_var = ''
        self.assessedVariables = {
            'Temp' : 2,
            'Wind Speed' : 7,
            'Pressure' : 10,
            'Precipitation' : 12,
            'Humidity' : 15,
            'Feels Like' : 17,
            'Wind Chill' : 19,
            'Heat Index' : 21,
            'Dewpoint' : 23,
            'Chance of Rain' : 26,
            'Gust Speed' : 34,
            'UV' : 35
        }
        self.graphVariables = [0,0,0,0,0,0,0,0,0,0,0,0]

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
        self.forecastButton = Button(self.frame1, text='Forecast API', command=self.forecast)
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
        self.submitButton = Button(self.frame2, text='Submit', command=lambda: [self.functionsRunner('current'), self.displayCurrent()])
        self.submitButton.pack()


    def forecast(self):

        # This for loop deletes the  previous page for the new page to go on top of
        for i in self.master.winfo_children():
            i.destroy()

        # This section creates the page and all the components on it
        # This line creates and packs the frame
        self.frame3 = Frame(self.master, width=1000, height=500)
        self.frame3.pack()

        # This line creates and packs the text box for the user to enter the location
        self.locationEntry = Entry(self.frame3, textvariable=self.location_var)
        self.locationEntry.pack()

        # This line creates and packs the text box for the user to enter their API key
        self.APIKeyEntry = Entry(self.frame3, textvariable=self.apiKey_var)
        self.APIKeyEntry.pack()

        # This line creates the submit button for the code 
        self.submitButton = Button(self.frame3, text='Submit', command=lambda: [self.functionsRunner('forecast'), self.displayForecast()])
        self.submitButton.pack()


    # This is the function that has the page that displays the return from the current weather api
    def displayCurrent(self):
        
        # This line makes locationData into a list to use it later in the table
        locationData = listifyCurrent(self.locationData_var)

        # This for loop deletes the previous page for the new page to go on top of
        for i in self.master.winfo_children():
            i.destroy()

        # This section creates page and all the components on it
        # This line creates and packs the frame
        self.frame5 = Frame(self.master, width=1000, height=500)
        self.frame5.pack()

        # This section creates the table and fills it with the locationData list
        for i in range(len(locationData)):
            for j in range(len(locationData[i])):
                self.currentTable = Text(self.frame5, height=1, width=50)
                self.currentTable.grid(row=j, column=i)
                self.currentTable.insert(END, locationData[i][j])

    # This is the function that has the page that displays the return from the forecast weather api
    def displayForecast(self):

        # This line makes location Data into a list to use it later in the table
        locationData = listifyForecast(self.locationData_var)

        # This for loop deletes the previous page for the new page to go on top of
        for i in self.master.winfo_children():
            i.destroy()

        
        # This section creates the page and all the components on it
        # This line creates and packs the frame
        self.frame6 = Frame(self.master, width=1000, height=500)
        self.frame6.pack()
        
        # This section creates the table and fills it with the locationData list
        for i in range(len(locationData[0][0])):
            self.forecastTable = Text(self.frame6, height=1, width=50)
            self.forecastTable.grid(row=i, column=0)
            self.forecastTable.insert(END, locationData[0][0][i])
        for i in range(3):
            for j in range(len(locationData[0][1][i])):
                self.forecastTable = Text(self.frame6, height=1, width=50)
                self.forecastTable.grid(row=j, column=i+1)
                self.forecastTable.insert(END, locationData[0][1][i][j])
        
        # This section makes and plots the graph for the other data
        self.grapher(locationData, self.frame6, [2], True)
        
        loopChecker = 0
        # All the checkboxes for the graph
        for i in self.assessedVariables.keys():
            self.graphVariables[loopChecker] = BooleanVar()
            self.graphVariables[loopChecker].set(False)
            self.forecastCheckbox = f'forecastCheckbox{loopChecker}'
            self.forecastCheckbox = Checkbutton(self.frame6, text=i, variable=self.graphVariables[loopChecker], onvalue=True, offvalue=False)
            self.forecastCheckbox.grid(column=1, row= 20+loopChecker)
            loopChecker += 1
        self.refreshGraphButton = Button(self.frame6, text='Refresh Graph', command=lambda : [self.grapher(locationData, self.frame6, self.functionsRunner('graph checker'), False)])
        self.refreshGraphButton.grid()

    
    def grapher(self, locationData, frame, wantedDisplays, createGraph):
        chartData = []
        for i in wantedDisplays:
            chartData.append([])
        for i in range(len(wantedDisplays)):
            for j in locationData[1]:
                chartData[i].append(j[wantedDisplays[i]])
        fig = Figure(figsize=(4,4))
        ax = fig.add_subplot(111)
        for i in chartData:
            ax.plot(i)
        if createGraph == True:
            self.graph = FigureCanvasTkAgg(fig, frame)
            self.graph.draw()
            self.graph.get_tk_widget().grid(rowspan=12)
        if createGraph == False:
            old_graph = self.graph.figure
            old_graph.canvas = None
            self.graph.figure = fig
            fig.canvas = self.graph
            self.graph.draw()
        

    # This function is a collection of the various functions that the code will run from the functions.py file
    def functionsRunner(self, choice):
        apiKey = self.apiKey_var.get()
        location = self.location_var.get()
        if choice == 'current':
            self.locationData_var = CurrentAPISearch(apiKey, location)
        elif choice == 'forecast':
            self.locationData_var = ForecastAPISearch(apiKey, location)
        elif choice == 'graph checker':
            temporaryChecker = []
            loopList = list(self.assessedVariables.values())
            for i in range(len(self.graphVariables)):
                test = self.graphVariables[i].get()
                if test == True:
                    temporaryChecker.append(loopList[i])
            return temporaryChecker

def runGUI():
    root = Tk()
    Weather_App(root)
    root.mainloop()


runGUI()

'''chartData = []
        for i in wantedDisplays:
            chartData.append([])
        for i in range(len(wantedDisplays)):
            for j in locationData[1]:
                chartData[i].append(j[wantedDisplays[i]])
        fig = Figure(figsize=(4,4))
        ax = fig.add_subplot(111)
        for i in chartData:
            ax.plot(i)
        if createGraph == True:
            self.graph = FigureCanvasTkAgg(fig, frame)
            self.graph.draw()
            self.graph.get_tk_widget().grid(rowspan=12)
        if createGraph == False:
            old_graph = self.graph.figure
            old_graph.canvas = None
            self.graph.figure = fig
            fig.canvas = self.graph'''