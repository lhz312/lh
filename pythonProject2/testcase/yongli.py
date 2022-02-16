import time
import unittest
from selenium import webdriver
from testcase.common import Login


class lonQQ(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://mail.qq.com/')
        self.driver.maximize_window()
        time.sleep(3)
    def test_log(self):
        self.driver.switch_to.frame("login_frame")
        time.sleep(3)
        # self.driver.find_element_by_id('switcher_plogin').click()
        # time.sleep(3)
        # self.driver.find_element_by_id('u').send_keys('1048506163')
        # time.sleep(3)
        # self.driver.find_element_by_id('p').send_keys('lhz312613')
        Login(self.driver).login('452990633','452990633cxm')
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="login_button"]').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()