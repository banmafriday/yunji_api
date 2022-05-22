# -*- coding: utf-8 -*-
from common.logger import Log
import unittest
from pages.home_page import Login
import time

ti = time.strftime("%Y_%m_%d_%H_%M_%S")


class Login_API(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tiqu = Login()
        cls.log = Log()

    def test_01(self):
        '''---登录---'''
        # self.log.info("-----------测试开始----------")
        # self.tiqu.login()
        self.tiqu.get_tu()
        # self.tiqu.get_code()
        # self.tiqu.change_password()
        # self.tiqu.change_contact()


if __name__ == "__main__":
    unittest.main()
