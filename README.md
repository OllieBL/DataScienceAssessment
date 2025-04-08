# __Weather Program__

This Python program allows you to retrieve weather information from an external API. The program uses the `requests` library to fetch real-time weather data and `matplotlib` to visualise the weather conditions in a graphical format.

## __Features__
- Can find past, present and future weather for a location of the users choosing
- Can create graphs for visualising the data received 
- Saves past requests from the user to make it easier when they want to look up information

## __Requirements__
To run this program, you need to install the following dependencies:

- `matplotlib` for data visualisation.
- `requests` to make HTTP requests to the weather API.

### __Install dependencies__
To install the required dependencies, you can run:

```bash
pip install -r requirements.txt

```

## __How to use__
### __Homepage__
The homepage is fairly easy to navigate, with the current API tab representing the api that is used to check the current weather in a location, the forecast API tab representing the API that is used for checking the forecast of the weather for a location, the history API tab represents the API that is used to check the weather of a day in the past in a location, and the past searches tab, which is used to access previous searches. 
### __Current API__
This tab checks the weather in a location currently, and it is used by inputting the location in the top text box and the API key in the bottom box. After inputting this and clicking on the submit button, the next page will show up, which contains all relevent information about the location currently. All of the statistics provided are fairly self explanatory, and at any time you can use the back button to go back to the homescreen
### __Forecast API__
This tab checks the weather in a location three days in the future, and it is used by inputting the location the top text box and the API key in the bottom box. After inputting this and clicking on the submit button, the next page will show the relevant information of the location for whole days in the top table, and the graph will by default only display temperature in celsius, however user can change the table to display any statistic shown in the checkboxes, then clicking the refresh graph button. Unfortunately, the graph does not scale the output, so be careful when using very differently scaled stats, like uv and pressure. You can press the back button at any time to go back to the homescreen.
### __Past API__
This tab checks the weather in a location one day in the past, and it is used by inputting the location the top text box and the API key in the bottom box. After inputting this and clicking on the submit button, the next page will show the relevant information of the location for the whole day in the top table, and the graph will by default only display temperature in celsius, however user can change the table to display any statistic shown in the checkboxes, then clicking the refresh graph button. Unfortunately, the graph does not scale the output, so be careful when using very differently scaled stats, like uv and pressure. You can press the back button at any time to go back to the homescreen.
### __Past Searches__
This tab allows you to access the past searches that you have made in the program, however it does not save over uses of the program. It displays the search made as first the kind of API used, current, forecast, or history, then the location, then the API key that was used, then a button that allows you to make the search again to make it easier to continue from where you where.