# try:
#     p = open('c:\\eula.10283.txt')
# except Exception:
#     print('cuode')
# else:
#     print('duide')

# from selenium import webdriver
# import time
# from selenium.common.exceptions import NoSuchFrameException
#
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element_by_id('kw').send_keys("saiban")
# driver.find_element_by_id('su').click()
# time.sleep(3)
# b=True
# try:
#     driver.find_element_by_id('kw').send_keys('saiban')
#     b=True
# except NoSuchFrameException:
#     b=False
# except Exception:
#     b=False
# print(b)
# driver.close()

# import requests
# import json
# url = 'http://localhost:8080/EasyBuy/Login'
# da = 'loginName=admin&password=123456&action=login'
# reo = requests.post(url=url,params=da)
# # print(reo.text)
# print(json.dumps(reo.json(),indent=0,ensure_ascii=False))
# print(json.dumps(req.json(),indent=4, ensure_ascii=False))

import requests
import json
import jsonpath

#生成token接口
url = "http://localhost:8000/login"
# python 字典 --》 json
data = {
    "username": "admin",
    "password": "admin"
}
res = requests.post(url=url, json=data)
#使用json包,打印json格式换行并且前面空四个空格，通过ascii防止乱码
print(json.dumps(res.json(), indent=4, ensure_ascii=False))
# 返回值是个列表 所以要加索引
# print(jsonpath.jsonpath(res.json(), "$..token")[0])

print("*************************************************************")

#登录jwt接口
urllogin = "http://localhost:8000/auth/hello"
#使用jsonpath来提取
token = "Bearer " + jsonpath.jsonpath(res.json(), "$..token")[0]
headers = {
    "Authorization":token
}
res1 = requests.get(url=urllogin,headers=headers)
print(json.dumps(res1.json(), indent=4, ensure_ascii=False))

print('************************************************************')

#上传文件接口
url = "http://httpbin.org/post"
# 准备一个文件
file = open("c:/1.txt", "rb")
# 参数
files = {
    "file": file
}
res2 = requests.post(url=url, files=files)
#print(res.json())
print(json.dumps(res2.json(), indent=4, ensure_ascii=False))

