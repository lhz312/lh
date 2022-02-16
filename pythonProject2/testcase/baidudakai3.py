from ddt import ddt, data
from po.baidu_page import BaiduPage


@ddt
class BaiduTest(unittest.TestCase):

    @data('软件测试', '硬件测试')
    def test01(self, seaString):
        BaiduPage().search(seaString)
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()