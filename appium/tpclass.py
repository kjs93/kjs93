import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

class Tphonesetup:
    def __init__(self):
        self.capabilities = dict(
            platformName='Android',
            platformVersion='14',
            automationName='uiautomator2',
            deviceName='R5CT4351QZP',
            appPackage='com.skt.prod.dialer',
            appActivity='com.skt.prod.dialer.activities.main.MainActivity',
            newCommandTimeout=60,
            autoGrantPermissions=True
        )

        self.appium_server_url = 'http://localhost:4723'
        self.driver = webdriver.Remote(self.appium_server_url, options=UiAutomator2Options().load_capabilities(self.capabilities))

        time.sleep(3)

    def quit(self):
        self.driver.quit()

    def setup_dialer(self):
        # XPaths
        confirm_btn = '//android.widget.TextView[@resource-id="com.skt.prod.dialer:id/confirm_btn"]'
        check_btn = '//android.widget.CheckBox[@resource-id="com.skt.prod.dialer:id/check_btn_agreeAll"]'
        accept_btn = '//android.widget.TextView[@resource-id="com.skt.prod.dialer:id/acceptButton"]'
        llbtnpositive = '//android.widget.LinearLayout[@resource-id="com.skt.prod.dialer:id/llBtnPositive"]'
        profile_setting = '//android.widget.TextView[@resource-id="com.skt.prod.dialer:id/profile_setting_later_btn"]'
        btn_next = '//android.widget.TextView[@resource-id="com.skt.prod.dialer:id/btn_next"]'

        # Click actions
        self.click(confirm_btn)
        time.sleep(3)
        self.click(check_btn)
        self.click(accept_btn)
        time.sleep(3)
        self.click(llbtnpositive)
        time.sleep(10)
        self.click(profile_setting)
        time.sleep(5)
        self.click(btn_next)
        time.sleep(5)

    def find(self, xpath):
        return self.driver.find_element(by=AppiumBy.XPATH, value=xpath)

    def click(self, xpath):
        try:
            element = self.find(xpath)
            element.click()
        except Exception as e:
            print(f"Failed to click element with xpath: {xpath}. Error: {e}")

    def recent_call(self):
        # XPaths
        recent_records = '//android.widget.ImageView[@resource-id="com.skt.prod.dialer:id/lottie_history"]'
        btn_positive = '//android.widget.TextView[@resource-id="com.skt.prod.dialer:id/btnPositive"]'
        call_button = '(//android.widget.ImageView[@resource-id="com.skt.prod.dialer:id/call_button"])[1]'

        # Click actions
        self.click(recent_records)
        time.sleep(1)
        self.click(btn_positive)
        time.sleep(1)
        self.click(call_button)
        time.sleep(1)