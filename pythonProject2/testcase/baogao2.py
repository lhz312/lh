import requests
import unittest
import json
import HTMLTestRunnerCN
class interfacetest01(unittest.TestCase):
    def test01(self):
        url='https://tianqiapi.com/api'
        data='version=v6&appid=73691227&appsecret=123456'
        response = requests.request('GET',url,params=data)
        print(response.json())
Testcase_dir = 'C:\Users\1\PycharmProjects\pythonProject2'
dis = unittest.defaultTestLoader.discover(Testcase_dir,'duanyan.py')
fp = open(filename,'wb')
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title='接口测试报告'，description='用例执行情况：')
runner.run(dis)
fp.close()