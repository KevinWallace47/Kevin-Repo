import SQL
import openmeteo_requests
from sphinx.cmd.quickstart import nonempty
import sqlite3
import sqlalchemy
from weatherclass import *
import requests_cache
import pandas as pd
from retry_requests import retry

#C3, main.py file using an instance of the class created in weatherclass.py
weather_data = FiveYearWeather(
		None,
		None,
		None,
		None,
		2025,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,)


#Runs API, inputs year variable and creates a list for the daily weather.
def api_run(
		year: str,
		daily_weathers: list,
		weather_data: list
):
	# Setup the Open-Meteo API client with cache and retry on error
	cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
	retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
	openmeteo = openmeteo_requests.Client(session = retry_session)

	# Make sure all required weather variables are listed here
	# The order of variables in hourly or daily is important to assign them correctly below
	url = "https://archive-api.open-meteo.com/v1/archive"
	params = {
		"latitude": 52.52,
		"longitude": 13.41,
		"start_date": f"{year}-01-04",
		"end_date": f"{year}-01-04",
		"hourly": "temperature_2m",
		"daily": ["temperature_2m_mean", "precipitation_sum", "wind_speed_10m_max"]
	}

	weather_data[0].lat = params["latitude"]
	weather_data[0].long = params["longitude"]
	weather_data[0].month = params["start_date"][5:7]
	weather_data[0].day = params["start_date"][8:10]
	weather_data[0].year = '2021 - 2025'


	responses = openmeteo.weather_api(url, params=params)

	# Process first location. Add a for-loop for multiple locations or weather models
	response = responses[0]
	print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
	print(f"Elevation {response.Elevation()} m asl")
	print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
	print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

	# Process hourly data. The order of variables needs to be the same as requested.
	hourly = response.Hourly()
	hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

	hourly_data = {"date": pd.date_range(
		start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
		end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
		freq = pd.Timedelta(seconds = hourly.Interval()),
		inclusive = "left"
	)}

	hourly_data["temperature_2m"] = hourly_temperature_2m

	hourly_dataframe = pd.DataFrame(data = hourly_data)
	#print(hourly_dataframe)

	# Process daily data. The order of variables needs to be the same as requested.
	#C2 Methods from the API that call the 3 variables requested.
	daily = response.Daily()
	daily_temperature_2m_mean = daily.Variables(0).ValuesAsNumpy()
	daily_precipitation_sum = daily.Variables(1).ValuesAsNumpy()
	daily_wind_speed_10m_max = daily.Variables(2).ValuesAsNumpy()

	daily_data = {"date": pd.date_range(
		start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
		end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
		freq = pd.Timedelta(seconds = daily.Interval()),
		inclusive = "left"
	)}

	daily_data["temperature_2m_mean"] = daily_temperature_2m_mean
	daily_data["precipitation_sum"] = daily_precipitation_sum
	daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max

	daily_dataframe = pd.DataFrame(data = daily_data)
	#print(daily_dataframe)
	#print(daily_precipitation_sum)
	alb = DailyWeather(daily_temperature_2m_mean,
					   daily_wind_speed_10m_max,
					   daily_precipitation_sum)
	#print(alb)
	daily_weathers.append(alb)

#Put class into list so changes within the function are reflected into the list.
weather_data_list = [weather_data]

#List for each day of weather.
daily_weathers = []
for year in range(2021, 2026):
	api_run(str(year), daily_weathers, weather_data_list)

#Outputting daily weather
#for daily_weather in daily_weathers:
	#print(daily_weather)
	#print( )
#print(daily_weathers[1])


#C5 populate the weather data table using the individual daily weathers and finding the average, minimum, and max values
weather_data.update_average_values(daily_weathers)
weather_data.update_min_values(daily_weathers)
weather_data.update_max_values(daily_weathers)

#Outputting five year average weather
print(weather_data)
#C6 queries the database
SQL.view_tables()
SQL.update_database(weather_data)




