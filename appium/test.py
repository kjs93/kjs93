from tpclass import Tphonesetup
from tphone_call_function import Callfunction

if __name__ == '__main__':
    tpclass = Tphonesetup()
    tpclass.setup_dialer() #T전화 약관동의 > 시작 > 키패드 화면 진입 TC001

    tpclass.recent_call() #첫번째 최근기록 통화 시도 TC002

    tphone_call_function = Callfunction(tpclass.driver)
    tphone_call_function.call_btn() # 통화 중 각 기능 버튼 Tap TC003