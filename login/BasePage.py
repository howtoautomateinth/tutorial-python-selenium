from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def fill_form_by_id(self, element_id, value):
        elem = self.driver.find_element_by_id(element_id)
        elem.send_keys(value)

    def navigate(self):
        self.driver.get(self.url)

    def click_by_id(self, element_id):
        elem = self.driver.find_element_by_id(element_id)
        elem.click()