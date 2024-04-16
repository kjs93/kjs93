from naverfindmap import SeleniumConfig
import time


if __name__ == '__main__':
    test = SeleniumConfig()
    test.find_result('청량리역', '남부터미널')
    time.sleep(5)
    test.close_driver()