from selenium import webdriver
import unittest
from time import sleep
import os
class computer_room(unittest.TestCase):
    #点击新建
    def computer(self):
        self.d = webdriver.Chrome()
        self.d.maximize_window()
        self.d.implicitly_wait()
