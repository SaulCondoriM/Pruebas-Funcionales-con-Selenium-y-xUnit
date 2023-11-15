import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import unittest

class WebDriverDemo(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(10)

        self.driver.get("http://www.calculator.net/")

        self.driver.maximize_window()

    def test_positives(self):
    
        math_calculator = self.driver.find_element(By.XPATH, ".//*[@id='homelistwrap']/div[3]/div[2]/a")
        math_calculator.click()

        percent_calculator = self.driver.find_element(By.XPATH, ".//*[@id='content']/table[2]/tbody/tr/td/div[3]/a")
        percent_calculator.click()

        first_number = self.driver.find_element(By.ID, "cpar1")
        first_number.send_keys("10")

        second_number = self.driver.find_element(By.ID, "cpar2")
        second_number.send_keys("50")

        calculate_button = self.driver.find_element(By.XPATH, ".//*[@id='content']/form[1]/table/tbody/tr[2]/td/input[2]")
        calculate_button.click()

        result = self.driver.find_element(By.XPATH, ".//*[@id = 'content']/p[2]/font/b").text

        print("El resultado es " + result)

        self.assertEqual(result, "5")

    def test_negatives(self):


        math_calculator = self.driver.find_element(By.XPATH, ".//*[@id='homelistwrap']/div[3]/div[2]/a")
        math_calculator.click()

        percent_calculator = self.driver.find_element(By.XPATH, ".//*[@id='content']/table[2]/tbody/tr/td/div[3]/a")
        percent_calculator.click()

        first_number = self.driver.find_element(By.ID, "cpar1")
        first_number.send_keys("8")

        second_number = self.driver.find_element(By.ID, "cpar2")
        second_number.send_keys("-70")

        calculate_button = self.driver.find_element(By.XPATH, ".//*[@id='content']/form[1]/table/tbody/tr[2]/td/input[2]")
        calculate_button.click()

        result = self.driver.find_element(By.XPATH, ".//*[@id = 'content']/p[2]/font/b").text

        print("El resultado es " + result)

        self.assertEqual(result, "-5.6")

    def test_decimals_positives(self):
    
        math_calculator = self.driver.find_element(By.XPATH, ".//*[@id='homelistwrap']/div[3]/div[2]/a")
        math_calculator.click()

        percent_calculator = self.driver.find_element(By.XPATH, ".//*[@id='content']/table[2]/tbody/tr/td/div[3]/a")
        percent_calculator.click()

        first_number = self.driver.find_element(By.ID, "cpar1")
        first_number.send_keys("7.5")

        second_number = self.driver.find_element(By.ID, "cpar2")
        second_number.send_keys("30")

        calculate_button = self.driver.find_element(By.XPATH, ".//*[@id='content']/form[1]/table/tbody/tr[2]/td/input[2]")
        calculate_button.click()

        result = self.driver.find_element(By.XPATH, ".//*[@id = 'content']/p[2]/font/b").text

        print("El resultado es " + result)

        self.assertEqual(result, "2.25")

    def test_decimals_negatives(self):
    
        math_calculator = self.driver.find_element(By.XPATH, ".//*[@id='homelistwrap']/div[3]/div[2]/a")
        math_calculator.click()

        percent_calculator = self.driver.find_element(By.XPATH, ".//*[@id='content']/table[2]/tbody/tr/td/div[3]/a")
        percent_calculator.click()

        first_number = self.driver.find_element(By.ID, "cpar1")
        first_number.send_keys("-9.3")

        second_number = self.driver.find_element(By.ID, "cpar2")
        second_number.send_keys("55")

        calculate_button = self.driver.find_element(By.XPATH, ".//*[@id='content']/form[1]/table/tbody/tr[2]/td/input[2]")
        calculate_button.click()

        result = self.driver.find_element(By.XPATH, ".//*[@id = 'content']/p[2]/font/b").text

        print("El resultado es " + result)

        self.assertEqual(result, "-3.8")



    def tearDown(self):
        
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
