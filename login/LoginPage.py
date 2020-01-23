from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from login.BasePage import BasePage

class LoginPage(BasePage):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def is_title_matches(self):
        return "Log in with Atlassian account" in self.driver.title

    def set_username(self, username):
        self.fill_form_by_id("username", username)
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID, 'login-submit')))
        self.click_by_id("login-submit")
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID, 'password')))

    def set_password(self, password):
        self.fill_form_by_id("password", password)
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID, 'login-submit')))
        self.click_by_id("login-submit")