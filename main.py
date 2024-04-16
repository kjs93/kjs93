from naverfindmap import SeleniumConfig

if __name__ == '__main__':
    helper = SeleniumConfig()
    helper.find_result('청량리역', '남부터미널')
    helper.close_driver()