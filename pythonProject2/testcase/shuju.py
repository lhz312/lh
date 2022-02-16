from selenium import webdriver
import time
import xlrd

dricer=webdriver.Chrome()#游览器
dricer.maximize_window() #窗口最大化
data = xlrd.open_workbook('C:\\Users\\1\\PycharmProjects\\pythonProject2\\testcase\\list.xls')
#读取xls文件
table=data.sheet_by_name('Sheet1') # 读取第一个工作表
# list=[]
for a in range(0,table.nrows): #使用for循环输出所有数据
    list=table.row_values(a)
    break
# print(list)
time.sleep(3)
dricer.get(list[0])
time.sleep(3)
dricer.find_element_by_id(list[3]).send_keys(list[4])
time.sleep(3)
dricer.find_element_by_id(list[7]).click()
time.sleep(3)
# list=[]
for a in range(0,table.nrows):
    list=table.row_values(a)
    break
# print(list)
dricer.find_element_by_xpath(list[-1]).click()
time.sleep(10)
dricer.close()



