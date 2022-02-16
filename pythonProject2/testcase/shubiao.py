# from selenium import webdriver #导入动作链
# from selenium.webdriver import  ActionChains
# import time
#
# driver=webdriver.Chrome() #定位游览器
# time.sleep(3)
# driver.get('https://www.baidu.com/') #定位百度
# time.sleep(3)
# driver.maximize_window()
# time.sleep(3)
# a = ActionChains(driver) #创建动作池对象
# time.sleep(3)
# b = driver.find_element_by_id('lg') #定位百度logo
# time.sleep(3)
# a.context_click(b).perform() #添加右键并执行
# time.sleep(3)
# driver.quit()


# from selenium import webdriver #导入动作链
# from selenium.webdriver import  ActionChains
# import time
#
# driver=webdriver.Chrome() #定位游览器
# driver.get('https://www.baidu.com/') #定位百度
# a = ActionChains(driver) #创建动作对象
# b=driver.find_element_by_xpath('//*[@id="s-top-left"]/a[4]') # 定位到贴吧元素
# a.double_click(b).perform() # 执行双击操作
# time.sleep(5)
# driver.quit()

# from selenium import webdriver #导入动作链
# from selenium.webdriver import  ActionChains
# import time
#
# driver=webdriver.Chrome() #定位游览器
# driver.get('https://www.baidu.com/') #定位百度
# driver.maximize_window()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="s-usersetting-top"]').click()
# driver.find_element_by_link_text('搜索设置').click()
# time.sleep(3)
# driver.find_element_by_css_selector('#se-setting-7 > a.prefpanelgo.setting-btn.c-btn.c-btn-primary').click()
# time.sleep(3)
# driver.switch_to.alert.dismiss()
# time.sleep(3)
# driver.close()

# from selenium  import webdriver
# from selenium.webdriver import ActionChains
# import time
#
# driver = webdriver.Chrome()
# driver.get('https://www.jd.com/')
# driver.maximize_window()
# b=driver.find_elements_by_class_name('cate_menu_item')
# time.sleep(3)
# a = ActionChains(driver)
# for el in b:
#     a.move_to_element(el).perform()
#     time.sleep(3)
# driver.close()



from selenium import webdriver
import time

class Mylib():

    def __init__(self):
        #初始化浏览器对象
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def delay(self):
        #延迟等待
        self.driver.implicitly_wait(5)
    # def a(self):
    #     self.driver.maximize_window()

    def open_url(self, url):
        #访问网站
        self.driver.get(url)
        self.delay()
        print('访问:%s成功'%url)

    def locate_element(self, locate_type, value):

        return self.driver.find_element(locate_type,value)
        #return self.driver.locate_element(locate_type,value)

    def __del__(self):
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    web = Mylib()
    web.open_url('https://www.baidu.com')
    # web.driver.maximize_window()
    el = web.locate_element('id','kw')
    el.send_keys('尼玛炸了')
    el_sub = web.locate_element('id','su')
    el_sub.click()
