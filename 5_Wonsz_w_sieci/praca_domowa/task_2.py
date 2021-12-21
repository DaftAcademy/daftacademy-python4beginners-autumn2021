import datetime
from dataclasses import dataclass
from typing import List


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
    """
    Napisz funkcję która zwróci historię świecową dla danego symbolu i danego interwału
    z zadanego okresu czasu.

    Tips:
        1. Dokumentacja: https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data
        2. Co to jest świeca? https://www.kaiko.com/collections/ohlcv

    Przykład:
    Dane z ostatnich 6 godzin, świece godzinne
    >>> get_pair_candles("ETHUSDT", interval="1h", limit=6, start_time=datetime.datetime.now())
    [Candle(open_time=1639389600000, close_time=1639393199999, open=3998.63, high=4009.37, low=3978.17, close=3994.1, volume=7161.2313),
     Candle(open_time=1639393200000, close_time=1639396799999, open=3994.1, high=4015.0, low=3987.0, close=4011.25, volume=6508.9229),
     Candle(open_time=1639396800000, close_time=1639400399999, open=4011.26, high=4021.59, low=3985.27, close=3989.77, volume=7906.7248),
     Candle(open_time=1639400400000, close_time=1639403999999, open=3989.76, high=3997.65, low=3959.42, close=3974.16, volume=13619.0755),
     Candle(open_time=1639404000000, close_time=1639407599999, open=3974.17, high=3974.74, low=3901.15, close=3920.54, volume=33012.5845),
     Candle(open_time=1639407600000, close_time=1639411199999, open=3920.53, high=3921.09, low=3908.0, close=3908.02, volume=2350.1331)]
    Dane z ostatnich 2 miesięcy, świece tygodniowe
    >>> get_pair_candles("AVAXUSDT", interval="1w", limit=8)
    [Candle(open_time=1635120000000, close_time=1635724799999, open=64.53, high=73.01, low=57.02, close=64.5, volume=17396408.49),
     Candle(open_time=1635724800000, close_time=1636329599999, open=64.5, high=88.88, low=62.19, close=87.57, volume=22389240.571),
     Candle(open_time=1636329600000, close_time=1636934399999, open=87.56, high=99.9, low=78.31, close=95.4, volume=25371399.668),
     Candle(open_time=1636934400000, close_time=1637539199999, open=95.4, high=147.0, low=83.5, close=128.47, volume=39385128.983),
     Candle(open_time=1637539200000, close_time=1638143999999, open=128.52, high=145.0, low=100.57, close=110.42, volume=30816578.94),
     Candle(open_time=1638144000000, close_time=1638748799999, open=110.42, high=127.41, low=76.57, close=86.35, volume=25271961.91),
     Candle(open_time=1638748800000, close_time=1639353599999, open=86.34, high=96.62, low=77.0, close=88.0, volume=19830099.67),
     Candle(open_time=1639353600000, close_time=1639958399999, open=88.01, high=89.92, low=80.0, close=80.0, volume=2000231.75)]
     >>>get_pair_candles(
     >>>    "ETHUSDT",
     >>>    interval="1d",
     >>>    limit=10,
     >>>    start_time=datetime.datetime(2021, 12, 1),
     >>>    end_time=datetime.datetime(2021, 12, 6),
     >>>)
    [Candle(open_time=1638316800000, close_time=1638403199999, open=4630.25, high=4778.75, low=4523.99, close=4582.95, volume=508198.3105),
     Candle(open_time=1638403200000, close_time=1638489599999, open=4582.95, high=4634.83, low=4433.0, close=4511.21, volume=451861.9545),
     Candle(open_time=1638489600000, close_time=1638575999999, open=4511.35, high=4654.88, low=4032.5, close=4215.73, volume=677974.8659),
     Candle(open_time=1638576000000, close_time=1638662399999, open=4215.01, high=4238.59, low=3503.68, close=4117.25, volume=1111773.1451),
     Candle(open_time=1638662400000, close_time=1638748799999, open=4117.25, high=4248.19, low=4031.39, close=4196.44, volume=536325.4413)]
    """
