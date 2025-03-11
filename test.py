from main import *
from SQL import *
from SQL import session
import unittest

#D, 3 different tests run and they all pass
class TestMethod(unittest.TestCase):

    #Testing if there is only 1 table being created
    def test_view_tables(self):
        self.assertEqual(view_tables(), 1)
    #Uses test entry to test if the database is running
    def test_update_database(self):
        test_entry = FiveYearWeather(10.10, 10.10, 10,10,2025,10.10,10.10,10.10,10.10,10.10,10.10,10.10,10.10,10.10)
        update_database(test_entry)
        result = session.query(WeatherData).order_by(WeatherData.id.desc()).first()
        self.assertIsNotNone(result)
        self.assertAlmostEqual(float(result.avg_temp), test_entry.avg_temp)
    #Checks to make sure there are 5 years
    def test_api(self):
        weather_data_list = [weather_data]
        daily_weathers = []
        for year in range(2021, 2026):
            api_run(year, daily_weathers, weather_data_list)
        self.assertEqual(len(daily_weathers), 5)

#Prevents the file running with the rest of the code
if __name__ == "__main__":
    unittest.main()

