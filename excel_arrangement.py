import pyupbit
import numpy as np

# OHLCV(open, high, close, volume)로 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터
df = pyupbit.get_ohlcv("KRW-BTC",count=7)

# 변동성 돌파 기준 범위 계산, (고가-저가) * k값(0.5)
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

# ror(수익률), np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)
# 누적 곱 계산(cumprod) => 누적 수익률
df['hpr'] = df['ror'].cumprod()

#낙폭
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

# MDD 계산
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")