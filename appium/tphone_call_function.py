import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

class Callfunction:
    def __init__(self, driver):
        self.driver = driver

    def call_btn(self):
        # XPATHS
        speak_btn = '(//android.widget.ImageView[@resource-id="com.skt.prod.dialer:id/title_icon"])[1]'
        bluetooth_btn = '(//android.widget.ImageView[@resource-id="com.skt.prod.dialer:id/title_icon"])[2]'
        bltreject = '//android.widget.Button[@resource-id="android:id/button2"]'
        keypad_btn = '(//android.widget.ImageView[@resource-id="com.skt.prod.dialer:id/title_icon"])[3]'
        record_btn = '//android.widget.ImageView[@resource-id="com.skt.prod.dialer:id/icon"]'
        next_function = '//android.widget.ImageView[@content-desc="다음기능보기"]'
        notsound_btn = '(//android.widget.ImageView[@resource-id="com.skt.prod.dialer:id/title_icon"])[1]'
        video_btn = '(//android.widget.ImageView[@resource-id="com.skt.prod.dialer:id/title_icon"])[2]'
        memo_btn = '(//android.widget.ImageView[@resource-id="com.skt.prod.dialer:id/title_icon"])[3]'
        seemore_btn = '(//android.widget.ImageView[@resource-id="com.skt.prod.dialer:id/title_icon"])[4]'
        call_end = '//android.widget.ImageView[@content-desc="통화종료"]'

        # Actions
        try:
            self.click(speak_btn)
            time.sleep(5)
            self.click(speak_btn)
            self.click(bluetooth_btn)
            time.sleep(3)
            self.click(bltreject)
            self.click(keypad_btn)
            time.sleep(1)
            self.click(keypad_btn)
            self.click(record_btn)
            self.click(next_function)
            time.sleep(1)
            self.click(notsound_btn)
            time.sleep(3)
            self.click(notsound_btn)
            self.click(video_btn)
            self.click(memo_btn)
            time.sleep(3)
            self.click_back_button()
            time.sleep(3)
            self.click(next_function)
            time.sleep(1)
            self.click(seemore_btn)
            time.sleep(3)
            self.click_back_button()
            time.sleep(3)
            self.click(call_end)
            time.sleep(3)


        except Exception as e:
            print(f"An error occurred: {e}")

    def find(self, xpath):
        return self.driver.find_element(by=AppiumBy.XPATH, value=xpath)

    def click(self, xpath):
        try:
            element = self.find(xpath)
            element.click()
        except Exception as e:
            print(f"Failed to click element with xpath: {xpath}. Error: {e}")

    # 뒤로 가기 버튼 누르기
    def click_back_button(self):
        self.driver.press_keycode(4)