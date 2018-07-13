# -*- coding: utf-8 -*-
# @Time    : 2018.7.13 17:04
# @Author  : Hofer

import requests
import unittest


url = 'http://10.10.90.245:8076/bms/api/user/getUserByUidChannel'
params = {"uid": "5b08fe587f100879738b494b", "channel": "wx_anxinjiankang"}


class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('111')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('22222')

    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('4444444')

    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('33333')

    def test_1(self):
        rsp = requests.get(url=url, params=params).json()
        self.assertEqual(200, rsp['resCode'])  # 测试用例

    def test_b_run(self):
        self.assertEqual(2, 2)  # 测试用例


if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例