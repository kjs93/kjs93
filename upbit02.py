import pyupbit
import pprint
import time
import datetime

access='Fvlj2ibYwAZxXU3Gw1xDQQYhYxfy7nTlFxmxW9uN'
secret='1J0oPxFXtoAGH8YeXU9IjVL3a9XOIanxbQmIxxFc'

upbit=pyupbit.Upbit(access, secret)

# 변동성 돌파 전략
def cal_target(ticker):
    df=pyupbit.get_ohlcv(ticker,"day")
    yesterday=df.iloc[-2]
    today=df.iloc[-1]
    yesterday_range=yesterday['high']-yesterday['low']
    target=today['open']+yesterday_range *0.5
    return target

target=cal_target("KRW-BTC")
op_mode=False
hold=False

while True:
    try:
        now = datetime.datetime.now()

        # 매도 시도
        if now.hour == 8 and now.minute == 59 and 50 <= now.second <= 59:
            if op_mode and hold:
                btc_balance = upbit.get_balance("KRW-BTC")
                if btc_balance > 0:
                    upbit.sell_market_order("KRW-BTC", btc_balance)
                    hold = False
            op_mode = False

        # 09:00:00 목표가 갱신
        if now.hour == 9 and now.minute == 0 and 20 <= now.second <= 30:
            target = cal_target("KRW-BTC")
            op_mode = True
            time.sleep(10)

        price = pyupbit.get_current_price("KRW-BTC")

        # 매초마다 조건을 확인한 후 매수시도
        if op_mode and not hold and price >= target:
            krw_balance = upbit.get_balance("KRW")
            if krw_balance >= 0:  # 예치금이 0원 이상일 때만 매수 시도
                upbit.buy_market_order("KRW-BTC", krw_balance)
                hold = True

        # 상태 출력
        print(f"현재시간: {now} 목표가: {target} 현재가: {price} 보유상태: {hold} 동작상태: {op_mode}")

    except Exception as e:
        print(f"에러 발생: {e}")
        time.sleep(1)  # 에러 발생 시 1초 대기 후 다음 반복으로 이동
