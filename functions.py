import requests

def CurrentAPISearch(APIKey, location): # calls the weather api for the current weather part of it
    # All in a try function to make sure that the code doesn't put the error in the terminal or give the user something that I don't want 
    try:
        response = requests.get(f'http://api.weatherapi.com/v1/current.json?key={APIKey}&q={location}') # standard request call to the current api. APIkey is the users api key that they entered and location is entered location
        locationData = response.json() # converts the api information into a json
        assert 'location' in locationData # gives a way of creating an actual error, rather than just the soft error that the code would normally output at this point
        return locationData # returns the api information as locationData
    except:
        return 'error' # error information back to the code in case of error so it still works

def ForecastAPISearch(APIKey, location): # calls the weather api for the forecast weather part of it
    # All in a try function to make sure that the code doesn't put the error in the terminal or give the user something that I don't want 
    try:
        response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={APIKey}&q={location}&days=3') # standard request call to the forecast api. APIkey is the users api key that they entered and location is entered location
        locationData = response.json() # converts the api information into a json
        return locationData # returns the api information as locationData
    except:
        return 'error' # error information back to the code in case of error so it still works

def HistoryAPISearch(APIKey, location, date): # calls the weather api for the history weather part of it
    # All in a try function to make sure that the code doesn't put the error in the terminal or give the user something that I don't want 
    try:
        response = requests.get(f'http://api.weatherapi.com/v1/history.json?key={APIKey}&q={location}&date={date}') # standard request call to the current api. APIkey is the users api key that they entered, location is entered location, and date is the day before the present day
        locationData = response.json() # converts the api information into a json
        return locationData # returns the api information as locationData
    except:
        return 'error' # error information back to the code in case of error so it still works


def listifyCurrent(locationData): # converts the current weather json into a list for easier use in loops
    try: # everything is in a try, to make sure that the user doesn't get any faulty data
        out = [[],[]] # the list that stores all the information after the listify function. out[0] is the names of the measured statistics, and out[1] is the values of the statistics
        for i in locationData.values(): # for loop over the values of the api information to add the relevent things to the list
            for j in i: # another for loop to get the right depth for the return
                out[0].append(j) # adds the name of the key to the list
                out[1].append(i[j]) # adds the statistic to the list

        return out # return the list complete
    except:
        return 'error' # error information back to the code in case of error so it still works

def listifyForecast(locationData): # converts the forecast weather json into a list for easier use in loops
    try: # everything is in a try, to make sure that the user doesn't get any faulty data
        out = [[[],[[],[],[]]],[]] # the list that returns the information. out[0][0] is the keys used, out[0][1] is the stats for each day overall, out[1] is the list to store all the individual hours for the list
        firstToggle = -1 # a way of keeping track of the number of loops made without using while loops or range(len()) for the dictionary
        locationDataDay = locationData['forecast']['forecastday'] # the actual information that the api gives about the weather, so it is easier to work with
        numberLoops = -1 # a way of keeping track of the number of loops made without using while loops or range(len()) for the dictionary
        for i in locationDataDay: # looping over the things in locationDataDay
            firstToggle += 1 # add to the toggle
            for j in i['day']: # looping over the overall days provided
                if firstToggle < 1: # check to see if this was the first time the loop was made, to add one copy of the keys to the list
                    out[0][0].append(j) # add the keys to the list
                out[0][1][firstToggle].append(i['day'][j]) # add the stat to the list
        
        for i in locationDataDay: # looping over locationDataDay
            for j in i['hour']: # looping over the hours provided by the api
                out[1].append([]) # add a list for each hour in the api
                numberLoops += 1 # add to numnberLoops
                for x in j: # looping for the values in the function
                    out[1][numberLoops].append(j[x]) # adding the stat to the list

        return out # return the list of the api
    except:
        return 'error' # return error to make sure that the code works fully afterwards

def listifyHistory(locationData): # conerts the history weather json into a list for easier use in loops
    try: # everything is in a try, to make sure that the user doesn't get any faulty data
        out = [[[],[]],[]] # the list that returns the information. out[0][0] is the keys for the overall day's stats, out[0][1] are the stats for the overall day, out[1][]
        locationDataDay = locationData['forecast']['forecastday'] # the actual information that the api gives about the weather, so it is easier to work with
        numberLoops = -1 # a way of keeping track of the number of loops made without using while loops or range(len()) for the dictionary
        for i in locationDataDay[0]['day']: # looping over the values and keys in the information
            out[0][0].append(i) # add the key to the list
            out[0][1].append(locationDataDay[0]['day'][i]) # add the stat to the list
        for i in locationDataDay[0]['hour']: # looping over the hours
            out[1].append([]) # add a list to put the stats in
            numberLoops += 1 # add to numberLoops 
            for j in i: # loop over the stats in each hour
                out[1][numberLoops].append(i[j]) # add the stat to the list
        
        return out # return the list
    except:
        return 'error' # output an error to make sure the code works