from selenium_helper import SeleniumHelper

if __name__ == '__main__':
    helper = SeleniumHelper()
    helper.navigate_and_search('청량리역', '남부터미널')
    helper.close_driver()