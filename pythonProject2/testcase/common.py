# from selenium import webdriver
import time

class Login():
    def __init__(self,driver):
        self.driver=driver
        # self.driver.maximize_window()
        time.sleep(3)

    def login(self,username,psw):
        self.driver.find_element_by_id('u').send_keys(username)
        self.driver.find_element_by_id('p').send_keys(psw)
        # self.driver.find_element_by_xpath('//*[@id="login_button"]').click()
        time.sleep(3)