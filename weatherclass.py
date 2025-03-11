#this is my weather class
#C1, class with all listed variables
class FiveYearWeather:
    def __init__(self, lat, long, month, day, year, avg_temp, min_temp, max_temp, avg_wind, min_wind, max_wind, sum_prec, min_prec, max_prec):
        # Float
        self.lat = lat
        # Float
        self.long = long
        # Int
        self.month = month
        # Int
        self.day = day
        # Int
        self.year = year
        # Float
        self.avg_temp = avg_temp
        # Float
        self.min_temp = min_temp
        # Float
        self.max_temp = max_temp
        # Float
        self.avg_wind = avg_wind
        # Float
        self.min_wind = min_wind
        # Float
        self.max_wind = max_wind
        # Float
        self.sum_prec = sum_prec
        # Float
        self.min_prec = min_prec
        # Float
        self.max_prec = max_prec

    #Makes it so you can print an object of this classes information
    def __str__(self):
        return f"{self.lat}\n {self.long}\n {self.month}\n {self.day}\n {self.year}\n {self.avg_temp}\n {self.min_temp}\n {self.max_temp}\n {self.avg_wind}\n {self.min_wind}\n {self.sum_prec}\n {self.min_prec}\n {self.max_prec}"

    #passes in daily weathers and calculates the average between all the days
    def update_average_values(self, daily_weathers:list):
        total_temp = 0
        total_wind = 0
        total_prec = 0
        for daily_weather in daily_weathers:
           total_temp += daily_weather.mean_temp
           total_wind += daily_weather.max_wind
           total_prec += daily_weather.prec_sum

        self.avg_temp = total_temp / 5
        self.avg_wind = total_wind / 5
        self.sum_prec = total_prec
    #Passes in daily weathers and calculates the min values between all days
    def update_min_values(self, daily_weathers:list):
        self.min_temp = daily_weathers[0].mean_temp
        self.min_wind = daily_weathers[0].max_wind
        self.min_prec = daily_weathers[0].prec_sum
        for daily_weather in daily_weathers:
            if self.min_temp >= daily_weather.mean_temp:
                self.min_temp = daily_weather.mean_temp
        for daily_weather in daily_weathers:
            if self.min_wind >= daily_weather.max_wind:
                self.min_wind = daily_weather.max_wind
        for daily_weather in daily_weathers:
            if self.min_prec >= daily_weather.mean_temp:
                self.min_prec = daily_weather.prec_sum
    #Passes in daily weathers list and calculates the max values between all days
    def update_max_values(self, daily_weathers:list):
        self.max_temp = daily_weathers[0].mean_temp
        self.max_wind = daily_weathers[0].max_wind
        self.max_prec = daily_weathers[0].prec_sum
        for daily_weather in daily_weathers:
            if self.max_temp <= daily_weather.mean_temp:
                self.max_temp = daily_weather.mean_temp
        for daily_weather in daily_weathers:
            if self.max_wind <= daily_weather.max_wind:
                self.max_wind = daily_weather.max_wind
        for daily_weather in daily_weathers:
            if self.max_prec <= daily_weather.prec_sum:
                self.max_prec = daily_weather.prec_sum

#class for information regarding individual days
class DailyWeather:
    def __init__(self, mean_temp: float, max_wind: float, prec_sum: float):
        self.mean_temp = mean_temp
        self.max_wind = max_wind
        self.prec_sum = prec_sum
    #Makes it so you can read the information from the class
    def __str__(self):
        return f"{self.mean_temp}\n {self.max_wind}\n {self.prec_sum}"

    #Creates an average temp
    def update_average(self):
        self.avg_temp = (self.min_temp + self.max_temp) / 2

