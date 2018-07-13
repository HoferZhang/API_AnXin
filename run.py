# -*- coding: utf-8 -*-
# @Time    : 2018.7.13 17:00
# @Author  : Hofer

import unittest
import xmlrunner

suite = unittest.TestSuite()  # 创建测试套件

# 找到某个目录下所有的以test开头的Python文件里面的测试用例
all_cases = unittest.defaultTestLoader.discover('testcase', 'test_*.py')


for case in all_cases:
    suite.addTests(case)  # 把所有的测试用例添加进来
    fp = open('res.html', 'wb')
    runner = xmlrunner.XMLTestRunner(output='report')  # 指定报告放的目录
    runner.run(suite)
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='all_tests', description='所有测试情况')
    # runner.run(suite)
