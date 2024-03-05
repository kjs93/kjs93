import pyupbit


access="Fvlj2ibYwAZxXU3Gw1xDQQYhYxfy7nTlFxmxW9uN"
secret="1J0oPxFXtoAGH8YeXU9IjVL3a9XOIanxbQmIxxFc"

# 로그인
upbit=pyupbit.Upbit(access, secret)

# 업비트 현재가 조회
def get_current_price(ticker):
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 업비트 잔고 조회
def get_balance(ticker):
    balances=upbit.get_balances()
    for b in balances:
        if b['currency']==ticker:
            return float(b['balance'])
        else:
            return 0
    return 0

# 업비트 평단가 조회
def get_buy_average(currency):
    balances=upbit.get_balances()
    for b in balances:
        if b['currency']==currency:
            if b['avg_buy_price'] is not None:
                return float(b['avg_buy_price'])
            else:
                return 0

current_price=get_current_price("KRW-DOGE")
krw=get_balance("KRW")
BTC_now=get_balance("BTC")
buy_average=get_buy_average("BTC")
print(current_price, krw, BTC_now, buy_average)
# 업비트 비트코인 매수
# buy=upbit.buy_market_order("KRW-BTC",6000*0.9995)
# print(buy)

# # 업비트 비트코인 매도
# sell=upbit.sell_market_order("KRW-BTC",BTC_now*0.9995)
# print(sell)

