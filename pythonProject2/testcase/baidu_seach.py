# # from selenium import webdriver
# # import time
# #
# #
# # driver = webdriver.Chrome()
# # driver.get('https://www.taobao.com/')
# # driver.maximize_window()
# # time.sleep(3)
# # driver.find_element_by_id('q').send_keys('牛奶')
# # driver.find_element_by_class_name('search-button').click()
# # time.sleep(5)
# # driver.close()
#
# # from selenium import webdriver
# # import time
# # driver = webdriver.Chrome()
# # driver.get('https://www.baidu.com/')
# # driver.maximize_window()
# # time.sleep(3)
# # driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/a[1]').click()
# # driver.switch_to.window(driver.window_handles[1])
# # time.sleep(3)
# # driver.find_element_by_class_name('a3').click()
# # time.sleep(3)
# # handles = driver.window_handles
# # driver.switch_to.window(handles[-1])
# # time.sleep(3)
# # driver.close()
#
#
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()
time.sleep(3)
driver.find_element_by_id('kw').send_keys('QQ邮箱') #百度输入qq邮箱
driver.find_element_by_id('su').click() # 点击搜索邮箱
time.sleep(3)
driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click() #点击打开邮箱
handles = driver.window_handles
driver.switch_to.window(handles[-1])
time.sleep(3)
driver.switch_to.frame('login_frame') # 获取登录框架
time.sleep(3)
driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click() #点击账号密码登录
driver.find_element_by_id('u').send_keys('1048596163') #点击输入账号
driver.find_element_by_id('p').send_keys('lhz312613') #点击输入密码
driver.find_element_by_xpath('//*[@id="login_button"]').click() # 点击登录
time.sleep(3)
driver.find_element_by_xpath('//*[@id="composebtn"]').click() #点击写信
time.sleep(3)
driver.switch_to.frame('mainFrame') #获取框架
driver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('452990633@qq.com') #输入写信人
time.sleep(3)
driver.find_element_by_name('UploadFile').send_keys('C:\\1.jpg') # 添加文件
#driver.switch_to.parent_frame() #返回上层的页面
time.sleep(3)
driver.find_element_by_css_selector('#toolbar > div.toolbg.toolbgline > a:nth-child(2)').click() # 点击发送
