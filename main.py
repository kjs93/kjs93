from naverfindmap import SeleniumConfig

if __name__ == '__main__':
    helper = SeleniumConfig()
    helper.navigate_and_search('청량리역', '남부터미널')
    helper.close_driver()