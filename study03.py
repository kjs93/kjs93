import pyupbit
import pprint
import time
import datetime

a=pyupbit.get_ohlcv("KRW-BTC","day")
print(a)