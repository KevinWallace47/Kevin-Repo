#Weather Data API response program

##Description:
This program generates an API response providing weather data for a given location and date for a 5 year time period. The final response is put into a class and an average for all the weather
information between the 5 years is inputted into a database called WeatherData
Example: The current input is for Albuquerque NM on January 4th, this code will provide the user with weather data for Albuquerque NM every January 4th between 2021 and 2025, an average
is given for the 5 years, and is then uploaded to the WeatherData Database.

##Installation
To install dependencies:
pip install -r requirements.txt

##Usage:
To find the weather data between 2021 and 2025 for a given date and location

##Commands
run SQL.py (creates the database) file first, then run main.py

##Inputs
The coordinates were provided from the API, however if you wanted to change location/date, you can do so by changing the coordinates as well as the date.

#Outputs
Latitude, Longitude, Month, Day of month, Year, Five year average temp, Five year min temp, Five year max temp, Five year average wind speed, five year min wind speed,
Five year min wind speed, Five year max wind speed, Five year sum precipitation, Five year min precipitation, Five year max precipitation
