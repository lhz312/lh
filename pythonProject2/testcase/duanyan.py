import requests
import unittest
class EasyBuylogin(unittest.TestCase):
    def test01(self):
        url= 'http://localhost:8080/EasyBuy/Login'
        data='loginName=admin&password=123456&action=login'
        headers={
            'Content-Type': 'application/x-www-from-urlencoded'
        }
        response = requests.request('post', url, headers=headers, params=data)
        print(response.text)
        #获取状态码
        result = response.json()['status']
        print(result)
        self.assertEqual(1, result)


if __name__ == '__main__':
    unittest.main()





