# __Data Science Project Development__

## __Requirements__

### __Functional Requirements__

* The user should be able to search for locations by coordinates, and name
* The user should be able to determine all weather information relevant to their search
* The system should be able to print a graph of recent weather conditions 
* The user should be able to check recent weather conditions in a location
* The user should be able to check the forecast for a location
* The user should be able to compare the weather conditions in two different places

### __Non-functional Requirements__

* The user should be able to save locations to be accessed easier
* The system should output the users request in less than 0.5 seconds
* The user should be able to get from the home screen to the point where they can get their request in less than 3 button clicks
* The user should be able to determine most functions in the application without specific help

## __Specifications__

### __Functional Specifications__

__User Requirements:__
* The user needs to be able to check the weather information about a chosen location
* The user needs to be able to find a location through coordinates, and name
* The user needs to be able to print a graph of recent weather conditions
* The user needs to be able to print a graph for the forecast for the near future
* The user needs to be able to access the forecast for the location they have chosen
* The user needs to be able to compare two different locations weather conditions at the same time

__Inputs and Outputs:__
* The system needs to output weather graphs and text which describes the weather conditions in the area, as well as the date
* The system needs to input the location, the method of request (e.g. current weather, history, forecast), and the date 

__Core Features:__
* The system needs to be able to input any information from the user to make a search
* The system needs to be able to take all of the users information and make the correct request to WeatherAPI
* The system needs to be able to search the returned request from the API and return the data that the user wanted to know about

__User Interaction:__
* The user will interact with the system using buttons for overarching options (e.g. method, type of stat being searched)
* The user will interact with the system using buttons for specific options (e.g. location)
* The system will specifically provide the name of what each button does, and will provide a help page on each button to explain it further

__Error Handling:__
* The system needs to be able to change and adjust the capitilisation of words to send requests
* The system needs to be able to interpret an error message from the API and return a correct error message to the user

#### __Use Case__
__Actor:__ User (person who wants to know the weather)

__Preconditions:__ Connection to internet, API for weather data available

__Main Flow:__ 
1. __Search/Find Location:__ User enters the name of the location (e.g. Paris, Sydney), then the system retrieves the information relevent to the location
1. __Display Information:__ System displays the information of the location searched (e.g. temperature)
1. __Visualise Information:__ System generates a graph using the information retrieved
1. __Save Location:__ User prompts system to save a location to be found easier later
1. __Compare Locations:__ User prompts system to find information of two locations and allow the user to compare them

__Postconditions:__ Location information is found, stored, compared, or visualised successfully

### __Non-Functional Specification__

__Performance:__
* The system needs to be able to respond to the user 0.5 seconds after a request has been made
* The system needs to be able to respond to the user as quickly as possible after inputs in the setup to search

__Useability and Accessibility:__
* The GUI that the user will interact with will be very simple
* The user will have exclusive choices that the system will show as different 'modes' for searching (e.g. method)
* The user will have non-exclusive choices that the system will show as checkboxes for the user to click individually
* The user will have a unique choice which is the location being searched

__Reliability:__
* The system needs to have 95.5% uptime
* The data outputted needs to have 100% reliability if the API is working

## __Design__

### __Gantt Chart__

![alt text](<Online Gantt 20250311.png>)

### __Structure Chart__

![alt text](<Structure Chart.png>)

### __Algorithms__

#### __Pseudocode__
```
BEGIN main()
    choice = 0
    WHILE choice is not 6
        INPUT choice
        IF choice is 1 THEN
            FindLocationDetails
            IF FindLocationDetails is Valid THEN
                RETURN Location_Details
            ELSE
                RETURN 'ERROR'
        IF choice is 2 THEN
            DisplayInformation
        IF choice is 3 THEN
            VisualiseInformation
        IF choice is 4 THEN
            SaveLocation
        IF choice is 5 THEN
            CompareLocations
        ENDIF
    ENDWHILE
END main()

BEGIN FindLocationDetails()
    SearchLocation
    IF API_KEY Valid THEN
        RETURN Valid
    ELSE
        RETURN Not Valid
    ENDIF
END FindLocationDetails

BEGIN VisualiseInformation(Location_Details)
    MakeGraph
    FOR number = 0 TO amount in Location_Details STEP 1
        Add Location_Details[1] to Graph
    NEXT number
```

#### __Flowcharts__

![alt text](<Flowchart main.png>)
![alt text](<Flowchart FindLocationDetails.png>)
![alt text](<Flowchart VisualiseInformation.png>)

### __Data Dictionary__

| Variable | Data Type | Format for Display | Size in Bytes | Size for Display | Description | Example | Validation |
|---|---|---|---|---|---|---|---|
| last_updated | string | YYYY-MM-DD HH-MM | 6 | 6 | Local time when the real time data was updated | 2025-03-16 14:45 | Valid date that is within an hour of the present |
| last_updated_epoch | int | N..N | 3 | 2 | Local time when the real time data was updated in unix time | 1742096700 | Valid unix time that is within an hour of the present |
| temp_c/temp_f | float | NN.N | 3 | 2 | Temperature in celsius/farhenheit | 37.3 / 99.1 | Valid float |
| feelslike_c/f | float | NN.N | 3 | 2 | Feels like temperature in celsius/farhenheit | 39.4 / 103.0 | Valid float |
| windchill_c/f | float | NN.N | 3 | 2 | Windchill temperature in celcius/farhenheit | 34.1 / 93.4 | Valid float |
| heatindex_c/f | float | NN.N | 3 | 2 | Heat index in celcius/farhenheit | 34.3 / 93.7 | Valid float |
| dewpoint_c/f | float | NN.N | 3 | 2 | Dew point in celcius/farhenheit | 14.7 / 58.5 | Valid float |
| wind_kph/mph | float | NN.N | 3 | 2 | Wind speed in kilometres/miles per hour | 41.8 / 25.9 | Valid float above 0 |
| wind_degree | int | NNN | 1 | 1 | Wind direction in degrees | 182 | Integer between 0 and 360 |
| wind_dir | string | XXX | 3 | 3 | Wind direction as 16 point compass | S | 1-3 characters out of N, S, E, W immediately next to each other |
| pressure_mb/in | float | NNNN.NN | 4 | 3 | Pressure in millibars/inches | 1021.0 / 30.15 | Valid float above 0 |
| precip_mm/in | float | NN.NN | 4 | 3 | Precipitation amount in millimeters/inches | 0.09 / 0.0 | Valid float above 0 |
| humidity | int | NN | 2 | 1 | Humidity as percentage | 52 | Valid int between 0 and 100 |
| cloud | int | NN | 2 | 1 | Cloud cover as percentage | 25 | Valid int between 0 and 100 |
| uv | float | NN.N | 3 | 2 | UV Index | 0.0 | Valid float above 0 |
| gust_kph/mph | float | NN.N | 3 | 2 | Wind gust in kilometres/miles per hour | 51.9 / 32.2 | Valid float above 0 |
| vis_km/miles | float | NN.N | 2 | 2 | Visibility in kilometres/miles | 10.0 / 6.0 | Valid float above 0 |
| maxtemp_c/f | float | NN.N | 2 | 2 | Maximum temperature in celsius/farhenheit for the day | 24.3 / 75.8 | Valid float | 
| mintemp_c/f | float | NN.N | 2 | 2 | Minimum temperature in celsius/farhenheit for the day | 18.2 / 64.7 | Valid float | 
| avgtemp_c/f | float | NN.N | 2 | 2 | Average temperature in celsius/farhenheit for the day | 21.5 / 70.8 | Valid float | 
| maxwind_kph/mph | float | NN.N | 2 | 2 | Maximum wind speed in kilometres/miles per hour | 31.7 / 19.7 | Valid float greater than 0 |
| totalprecip_mm/in | float | NN.N | 2 | 2 | Total precipitation in milimetres/inches | 0.04 / 0.0 | Valid float equal to or above 0 | 
| totalsnow_cm* | float | NN.N | 2 | 2 | Total snowfall in centimetres | 0.0 | Valid float equal to or above 0 |
| avgvis_km/miles | float | NN.N | 2 | 2 | Average visibility in kilometres/miles | 10.0 / 6.0 | Valid float above 0 | 
| avghumidity | int | NN | 1 | 1 | Average humidity as percentage | 71 | Valid int from 0 to 100 |
| daily_chance_of_rain | int | NN | 1 | 1 | Chance of rain as a percentage | 0 | Valid int from 0 to 100 |
| daily_chance_of_snow | int | NN | 1 | 1 | Chance of snow as a percentage | 0 | Valid int from 0 to 100 |
| sunrise | string | XX:XX XX | 4 | 4 | Sunrise time | 06:57 AM | First two characters an int from 01-12, second two characters must be an int from 00-60, last two characters must be either 'AM' or 'PM' |
| sunset | string | XX:XX XX | 4 | 4 | Sunset time | 07:08 PM | First two characters an int from 01-12, second two characters must be an int from 00-60, last two characters must be either 'AM' or 'PM' |
| moonrise | string | XX:XX XX | 4 | 4 | Moonrise time | 09:26 PM | First two characters an int from 01-12, second two characters must be an int from 00-60, last two characters must be either 'AM' or 'PM' |
| moonset | string | XX:XX XX | 4 | 4 | Moonset time | 11:15 AM | First two characters an int from 01-12, second two characters must be an int from 00-60, last two characters must be either 'AM' or 'PM' |

**Yes average snowfall is only in metric, as opposed to all other ones which are in both metric and imperial*

## __Installation__

The information for this section is in [requirements](requirements.txt) and [README](README.md)

## __Maintenance__

1. The Weather API is likely to remain consistent in its functionality over time, but if it does change I can adjust the code to change with the API by altering the formatting of a few functions. The main functions in need of altering the in the outcome of a changed API output would be the listify functions which convert the json output of the API request into a list, and if the API change their formatting at all the function may not work as intended, failing to group things properly and giving faulty data to the other functions, but it would be fairly easy to alter to work just by fixing the exact functionality of each of them. Another way they would change it is the order of the statisitics used, which affects how the application generates the graph, however it would be solved by altering the numbers used to map the statistics to their names. Through these methods I would be able to keep up the code with changes to the API.
1. To keep the program up with the changes to the libraries and applications that the program uses like requests, matplotlib, new python versions, datetime, and tkinter, the code would probably remain very similar to how it already functions, however the syntax changes that the libraries introduce would be kept up with, with changes to the code to make the function the same. However, what would be a greater challenge would be if certain features were dropped from libraries, like if matplotlib stopped supporting the FigureCanvasTkAgg function, the information displays would become basically non-functional. The best way to fix something like this would be to find a functional alternative, like, in this scenario, finding a way of displaying the image of the graph on the GUI. It is through these methods that I would make sure the code is functional over time.
1. The best way to fix a bug found after deployment would be to change the code such that the element that caused the bug would no longer be relevent, or change it so that the scenario that caused the bug would be made irrelevent. An example of this would be if by a series of unexpected inputs, like if they repeatedly clicked the submit button, and somehow caused it to make more requests than one, the user could cause the program to crash, and the way that I would solve this would be to alter the elements used such that if this sequence occured then an exception occured and the user was given a regular error, rather than a crash, and in the button example I would change the button element so that the user wouldn't be able to click the button more than once. It would be through this method that I would fix the code after deployment remove logical bugs.
1. To keep clear documentation I would add comments to the code that I have written as I am doing it, in order to make sure that it doesn't become unusable to anyone wanting to use the code, and keeping all information relevent to the libraries installed kept in the README so that anyone can manage how the code works over time

## __Evaluation__

1. The code is fairly well functioning, and fills most of the functional requirements, however the code misses out on some of the features that I wanted to implement, and the non-functional requirements are also mostly fulfilled, however one is missed out on. The function of the program is pretty good, but is lacking the ability to compare multiple location at once, which was a feature that would have been ideal to have as it allows for the application to be more unique than other similar applications, and the non-functional requirement that I missed out on was the ability to save the locations that the user has used before. It partially exists in a byproduct of how the code saves the input of the user in the boxes, allowing the user to use the same location or API key in a different request, however that is not the original intent of the requirement. It is because of this I don't believe that I properly fulfilled the requirements that I gave myself, however I do believe that the application is highly functioning and useable.
1. Ideally, the area of improvement in the project would be the requirements that I didn't fulfill, however I would also like to improve the appearance of the application, as it is currently only the default appearance of every element on the screen, and I would also like to add some better use of the graph in the application, mostly by adding some use of the axis, and making it more useable by allowing you to compare certain stats that have very different scales, like the pressure. These are the things that I would like to improve if possible
1. The project was managed fairly well, in regard to how well the time management occured, and how issues were solved when encountered. In regard to time management, I did quite well, with no sections taking much longer than they should've, and being able to complete almost everything before the due date, which is a notable improvement on past assignments. In regards to managaing issues, I also did fairly well, with only a few major issues occuring, mostly in regards to unknown syntax requirements causing logical errors, particaularly the refresh graph button that kept running the code as it was created instead of when it was clicked, which was solved through a few hours of dedicated problem solving to fix it, however it was functioning and no features were removed because of it and nothing was missed out on in development because of an issue. All round, the project management was quite successful on this project because if didn't stray too far away from where it was expected to be, and I completed all elements of the task.