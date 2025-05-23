from tkinter import *
from functions import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from datetime import *


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
            'Gust Speed' : 32,
            'UV' : 33
        }
        self.graphVariables = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.pastSearches = []

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

        # This line creates and packs the button to select the history API
        self.historyButton = Button(self.frame1, text='History API', command=self.history)
        self.historyButton.pack()

        # This line creates and packs the button to access past searches
        self.pastSearchesButton = Button(self.frame1, text='Past Searches', command=self.pastSearchesPage)
        self.pastSearchesButton.pack()


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
        self.submitButton = Button(self.frame2, text='Submit', command=lambda: [self.functionsRunner('current'), self.pastSearches.append(['current', self.location_var.get(), self.apiKey_var.get(), self.displayCurrent]), self.displayCurrent()])
        self.submitButton.pack()

        # Back button if you want to return to the homescreen
        self.backButtonSearch = Button(self.frame2, text='Back', command=self.APISelection)
        self.backButtonSearch.pack()


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
        self.submitButton = Button(self.frame3, text='Submit', command=lambda: [self.functionsRunner('forecast'), self.pastSearches.append(['forecast', self.location_var.get(), self.apiKey_var.get(), self.displayForecast]), self.displayForecast()])
        self.submitButton.pack()
                
        # Back button if you want to return to the homescreen
        self.backButtonSearch = Button(self.frame3, text='Back', command=self.APISelection)
        self.backButtonSearch.pack()

    
    def history(self):

        # This for loop deletes the  previous page for the new page to go on top of
        for i in self.master.winfo_children():
            i.destroy()

        # This section creates the page and all the components on it
        # This line creates and packs the frame
        self.frame4 = Frame(self.master, width=1000, height=500)
        self.frame4.pack()

         # This line creates and packs the text box for the user to enter the location
        self.locationEntry = Entry(self.frame4, textvariable=self.location_var)
        self.locationEntry.pack()

        # This line creates and packs the text box for the user to enter their API key
        self.APIKeyEntry = Entry(self.frame4, textvariable=self.apiKey_var)
        self.APIKeyEntry.pack()

        # This line creates the submit button for the code 
        self.submitButton = Button(self.frame4, text='Submit', command=lambda: [self.functionsRunner('history'), self.pastSearches.append(['history', self.location_var.get(), self.apiKey_var.get(), self.displayHistory]), self.displayHistory()])
        self.submitButton.pack()

        # Back button if you want to return to the homescreen
        self.backButtonSearch = Button(self.frame4, text='Back', command=self.APISelection)
        self.backButtonSearch.pack()


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

        # Back button if you want to return to the homescreen
        self.backButtonSearch = Button(self.frame5, text='Back', command=self.APISelection)
        self.backButtonSearch.grid()

        # This section creates the table and fills it with the locationData list
        for i in range(len(locationData)):
            for j in range(len(locationData[i])):
                self.currentTable = Text(self.frame5, height=1, width=50)
                self.currentTable.grid(row=j, column=i+1)
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

        # Back button if you want to return to the homescreen
        self.backButtonSearch = Button(self.frame6, text='Back', command=self.APISelection)
        self.backButtonSearch.grid()
        
        # This section creates the table and fills it with the locationData list
        for i in range(len(locationData[0][0])):
            self.forecastTable = Text(self.frame6, height=1, width=50)
            self.forecastTable.grid(row=i, column=1)
            self.forecastTable.insert(END, locationData[0][0][i])
        for i in range(3):
            for j in range(len(locationData[0][1][i])):
                self.forecastTable = Text(self.frame6, height=1, width=50)
                self.forecastTable.grid(row=j, column=i+2)
                self.forecastTable.insert(END, locationData[0][1][i][j])
        
        # This section makes and plots the graph for the other data
        self.grapher(locationData, self.frame6, [2], True)
        
        loopChecker = 0
        # All the checkboxes for the graph
        for i in self.assessedVariables.keys():

            # Sets each entry in graphVariables to a tkinter boolean and False
            self.graphVariables[loopChecker] = BooleanVar()
            self.graphVariables[loopChecker].set(False)

            # Generates the content of each checkbox and places it
            self.forecastCheckbox = f'forecastCheckbox{loopChecker}'
            self.forecastCheckbox = Checkbutton(self.frame6, text=i, variable=self.graphVariables[loopChecker], onvalue=True, offvalue=False)
            self.forecastCheckbox.grid(column=2, row= 20+loopChecker)

            # Uses loopchecker to make it easier to use the graphvariables and the assessed variables in the same loop
            loopChecker += 1
        
        # creates the button to refresh the graph
        self.refreshGraphButton = Button(self.frame6, text='Refresh Graph', command=lambda : [self.grapher(locationData, self.frame6, self.functionsRunner('graph checker'), False)])
        self.refreshGraphButton.grid()


    def displayHistory(self):
        
        
        locationData = listifyHistory(self.locationData_var)

        # This for loop deletes the previous page for the new page to go on top of
        for i in self.master.winfo_children():
            i.destroy()

        # This section creates and packs the frame
        self.frame7 = Frame(self.master, width=1000, height=500)
        self.frame7.pack()

        # Back button if you want to return to the homescreen
        self.backButtonSearch = Button(self.frame7, text='Back', command=self.APISelection)
        self.backButtonSearch.grid()

        # This section creates the table and fills it with the data
        for i in range(len(locationData[0])):
            for j in range(len(locationData[0][i])):
                self.currentTable = Text(self.frame7, height=1, width=50)
                self.currentTable.grid(row=j, column=i+1)
                self.currentTable.insert(END, locationData[0][i][j])

        self.grapher(locationData, self.frame7, [2], True)

        loopChecker = 0
        # This section makes the table and checkboxes
        for i in self.assessedVariables.keys():

            self.graphVariables[loopChecker] = BooleanVar()
            self.graphVariables[loopChecker].set(False)


            self.historyCheckbox = f'historyCheckbox{loopChecker}'
            self.historyCheckbox = Checkbutton(self.frame7, text=i, variable=self.graphVariables[loopChecker], onvalue=True, offvalue=False)
            self.historyCheckbox.grid(column=2, row= 20+loopChecker)

            loopChecker += 1

        # creates the button to refresh the graph
        self.refreshGraphButton = Button(self.frame7, text='Refresh Graph', command=lambda : [self.grapher(locationData, self.frame7, self.functionsRunner('graph checker'), False)])
        self.refreshGraphButton.grid()



    def pastSearchesPage(self):

        # This for loop deletes the previous page for the new page to go on top of
        for i in self.master.winfo_children():
            i.destroy()


        # This section creates and packs the frame
        self.frame8 = Frame(self.master, width=1000, height=500)
        self.frame8.pack()

        # Back button if you want to return to the homescreen
        self.backButtonSearch = Button(self.frame8, text='Back', command=self.APISelection)
        self.backButtonSearch.grid()

        # This loop creates the table for past searches and their buttons
        for i in range(len(self.pastSearches)):
            for j in range(len(self.pastSearches[i])-1):
                self.pastSearchesTable = Text(self.frame8, height=1, width=30)
                self.pastSearchesTable.grid(column=j+1, row=i+1)
                self.pastSearchesTable.insert(END, self.pastSearches[i][j])
            self.pastSearchesTableButton = Button(self.frame8, text='Continue Search?', command=lambda i=i: [self.functionsRunner('assign inputs', [self.pastSearches[i][1], self.pastSearches[i][2]]), self.functionsRunner(self.pastSearches[i][0]), self.pastSearches[i][3]()])
            self.pastSearchesTableButton.grid(column=4, row=i+1) 
        



        

    # A function to generate the graph in relevent frames
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
            self.graph.get_tk_widget().grid(column=1,rowspan=12)
        if createGraph == False:
            old_graph = self.graph.figure
            old_graph.canvas = None
            self.graph.figure = fig
            fig.canvas = self.graph
            self.graph.draw()
        

    # This function is a collection of the various functions that the code will run from the functions.py file
    def functionsRunner(self, choice, vars = []):
        apiKey = self.apiKey_var.get()
        location = self.location_var.get()
        currentDate = datetime.now() - timedelta(1)
        currentDate.strftime('%Y-%m-%d')
        if choice == 'current':
            self.locationData_var = CurrentAPISearch(apiKey, location)
        elif choice == 'forecast':
            self.locationData_var = ForecastAPISearch(apiKey, location)
        elif choice == 'history':
            self.locationData_var = HistoryAPISearch(apiKey, location, currentDate)
        elif choice == 'graph checker':
            temporaryChecker = []
            loopList = list(self.assessedVariables.values())
            for i in range(len(self.graphVariables)):
                test = self.graphVariables[i].get()
                if test == True:
                    temporaryChecker.append(loopList[i])
            return temporaryChecker
        elif choice == 'assign inputs':
            self.location_var = StringVar(value=vars[0])
            self.apiKey_var = StringVar(value=vars[1])

def runGUI():
    root = Tk()
    Weather_App(root)
    root.mainloop()