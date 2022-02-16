from testcase import HTMLTestRunnerCN
import unittest
Testcase_dir='C:\\Users\\1\PycharmProjects\\pythonProject2\\testcase'
dis=unittest.defaultTestLoader.discover(Testcase_dir,'yongli.py')
filename='C:\\Users\\1\PycharmProjects\\pythonProject2\\testcase\\rels.html'
fp=open(filename,'wb')
runnre=HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title='测试模式',description='描述')
runnre.run(dis)
