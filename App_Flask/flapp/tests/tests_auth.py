from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class MyTestCase(unittest.TestCase):

    def test_login(self):
        with webdriver.Firefox() as driver:
            url = "http://127.0.0.1:5000/auth/login"
            driver.get(url)
            driver.find_element(By.id, "login").send_keys('toto')
            driver.find_element(By.id, "password").send_keys('mdp')
            driver.find_element(By.id, "submit").click()
            self.assertEqual(url, False) 
