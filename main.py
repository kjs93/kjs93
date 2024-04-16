from selenium_helper import SeleniumConfig

if __name__ == '__main__':
    helper = SeleniumConfig()
    try:
        helper.navigate_and_search('청량리역', '남부터미널')
    finally:
        helper.close_driver()