from ddt import ddt, data
from zhu.report.po import BaiduPage
import time
import unittest
@ddt
class BaiduTest(unittest.TestCase):

    @data('比基尼美女', '硬汉')
    def test01(self, seaString):
        BaiduPage().search(seaString)
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()