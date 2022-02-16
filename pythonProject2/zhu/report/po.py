from selenium.webdriver.common.by import By
from zhu.commint.baidu import BasePage
import time

class BaiduPage(BasePage):
    # 元素定位，
    baidu_text_loc = (By.ID, 'kw')
    baidu_submit_loc = (By.ID, 'su')
    # 获得元素对象，
    def get_text_obj(self):
        ele = self.find_ele(*BaiduPage.baidu_text_loc)
        return ele
        time.sleep(3)
    def get_submit_obj(self):
        ele = self.find_ele(*BaiduPage.baidu_submit_loc)
        return ele
        time.sleep(3)
    # 页面操作
    def search(self, search_string):
        self.get_text_obj().send_keys(search_string)
        self.get_submit_obj().click()
        time.sleep(3)