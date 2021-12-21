import datetime
from dataclasses import dataclass
from typing import List

import requests


@dataclass
class Candle:
    open_time: int
    close_time: int
    open: float
    high: float
    low: float
    close: float
    volume: float


def get_pair_candles(
    symbol: str,
    interval: str,
    limit: int = 100,
    start_time: datetime.datetime = None,
    end_time: datetime.datetime = None,
) -> List[Candle]:
    start_time_as_timestamp = start_time and int(start_time.timestamp()) * 1000
    end_time_as_timestamp = end_time and int(end_time.timestamp()) * 1000

    query_params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit,
        "startTime": start_time_as_timestamp,
        "endTime": end_time_as_timestamp,
    }

    r = requests.get(
        "https://api.binance.com/api/v3/klines",
        params=query_params,
    )
    data = r.json()

    return [
        Candle(
            open_time=candle[0],
            close_time=candle[6],
            open=float(candle[1]),
            high=float(candle[2]),
            low=float(candle[3]),
            close=float(candle[4]),
            volume=float(candle[5]),
        )
        for candle in data
    ]


if __name__ == "__main__":
    from pprint import pprint

    pprint(get_pair_candles("ETHUSDT", interval="1h", limit=6))
    pprint(
        get_pair_candles(
            "ETHUSDT",
            interval="1h",
            limit=6,
            start_time=datetime.datetime(2021, 2, 1, 1),
        )
    )
    pprint(
        get_pair_candles(
            "ETHUSDT",
            interval="1d",
            limit=10,
            start_time=datetime.datetime(2021, 12, 1),
            end_time=datetime.datetime(2021, 12, 6),
        )
    )
    pprint(
        get_pair_candles(
            "ETHUSDT",
            interval="1d",
            limit=100,
            start_time=datetime.datetime(2021, 12, 1),
            end_time=datetime.datetime(2021, 12, 10),
        )
    )
