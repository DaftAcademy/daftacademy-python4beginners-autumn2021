import time
import unittest

from task_0 import get_weather_for_point
from task_0_solution import get_weather_for_point as get_weather_for_point_solution


class TestWeatherForPoint(unittest.TestCase):
    TEST_COORDINATES = [
        (21.0122, 52.2297),
        (77.0369, 38.9072),
        (18.4241, 33.9249),
        (116.4074, 39.9042),
    ]

    def test_weather_for_point_capitols(self):

        for coordinates in self.TEST_COORDINATES:
            time.sleep(0.5)

            longitude, latitude = coordinates

            expected_result = get_weather_for_point_solution(
                longitude=longitude, latitude=latitude
            )
            result = get_weather_for_point(longitude=longitude, latitude=latitude)

            self.assertTrue(
                expected_result.temperature - 2
                <= result.temperature
                <= expected_result.temperature + 2
            )
            self.assertTrue(
                expected_result.feels_like - 2
                <= result.feels_like
                <= expected_result.feels_like + 2
            )
            self.assertTrue(
                expected_result.pressure - 2
                <= result.pressure
                <= expected_result.pressure + 2
            )
            self.assertTrue(
                expected_result.humidity - 2
                <= result.humidity
                <= expected_result.humidity + 2
            )
            self.assertTrue(
                expected_result.clouds - 2
                <= result.clouds
                <= expected_result.clouds + 2
            )
            self.assertEqual(result.longitude, expected_result.longitude)
            self.assertEqual(result.latitude, expected_result.latitude)
