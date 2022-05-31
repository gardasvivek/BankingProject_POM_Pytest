import time

import pytest
from selenium import webdriver
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config.TestData import TestData


class BasePage():
    def __init__(self,driver):
        self.driver=driver
        #self.driver.get(TestData.BaseUrl)


    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_sendKeys(self,by_locator,inputText):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(inputText)
        time.sleep(3)

    def scroll_To(self,by_locator):
        target=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        action=ActionChains(self.driver)
        action.move_to_element(target)
        action.perform()

    def get_title(self):
        actual_title=self.driver.title
        return actual_title

    def goto_url(self,url):
        self.driver.get(url)

    def is_visible(self,by_locator):
        element_vivible=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element_vivible)