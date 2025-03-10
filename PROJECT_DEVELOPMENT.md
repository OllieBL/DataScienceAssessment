# Data Science Project Development

## Requirements

### Functional Requirements

* The user should be able to search for locations by coordinates, and name
* The user should be able to determine all weather information relevant to their search
* The system should be able to print a graph of recent weather conditions 
* The user should be able to check recent weather conditions in a location
* The user should be able to check the forecast for a location
* The user should be able to compare the weather conditions in two different places

### Non-functional Requirements

* The user should be able to save locations to be accessed easier
* The system should output the users request in less than 0.5 seconds
* The user should be able to get from the home screen to the point where they can get their request in less than 3 button clicks
* The user should be able to determine most functions in the application without specific help

## Specifications

### Functional Specifications

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

### Non-Functional Specification

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

## Design

### Gantt Chart

### Structure Chart

### Algorithms

### Data Dictionary

## Development

### UI Design

### Progress Report

## Integration

## Testing and Debugging

## Installation

## Maintenance