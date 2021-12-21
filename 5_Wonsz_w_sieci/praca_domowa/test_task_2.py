import datetime
import time
import unittest

from task_2 import get_pair_candles
from task_2_solution import get_pair_candles as get_pair_candles_solution


class TestGetPairCandles(unittest.TestCase):
    TEST_KWARGS = [
        {
            "symbol": "ETHUSDT",
            "interval": "1h",
            "limit": 6,
            "start_time": datetime.datetime(2021, 12, 1),
        },
        {
            "symbol": "BTCUSDT",
            "interval": "15m",
            "limit": 10,
            "start_time": datetime.datetime(2021, 11, 1),
        },
        {
            "symbol": "SANDUSDT",
            "interval": "30m",
            "limit": 4,
            "start_time": datetime.datetime(2021, 10, 1),
        },
        {
            "symbol": "ETHUSDT",
            "interval": "1d",
            "limit": 7,
            "start_time": datetime.datetime(2021, 12, 1),
            "end_time": datetime.datetime(2021, 12, 10),
        },
    ]

    def test_get_pair_candles(self):

        for kwargs in self.TEST_KWARGS:
            time.sleep(0.5)

            expected_result = get_pair_candles_solution(**kwargs)
            result = get_pair_candles(**kwargs)

            self.assertListEqual(result, expected_result)
