from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://localhost:8080/EasyBuy")
        self.driver.maximize_window()

    def test1(self):
        self.driver.find_element_by_xpath('//html/body/div[5]/div/ul/li[2]/a').click()
        time.sleep(3)

    def test2(self):
        self.driver.find_element_by_xpath('//html/body/div[4]/div[2]/form/input[1]').send_keys('香水', Keys.ENTER)
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()


    if __name__ == '__main__':
        unittest.main()

# testunit = unittest.TestSuite()
# testunit.addTest(Test("test2"))
# unittest.TextTestRunner().run(testunit)