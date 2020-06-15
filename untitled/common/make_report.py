# coding=utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner

#指定测试用例为当前文件夹下的test_Case目录,并匹配测试脚本
discover = unittest.defaultTestLoader.discover(start_dir="C:\\Users\\Administrator\\PycharmProjects\\untitled\\testcase",top_level_dir=None)
reportPath="C:\\Users\\Administrator\\PycharmProjects\\untitled\\testReport\\"+"TestReport.html"#定义报告存储路径
fp=open(reportPath,"w")#定义写入文件路径和方法
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"testreport",verbosity=2,
                                     description="testcase")#将报告写入到定义的文件中
runner.run(discover)#执行测试用例




