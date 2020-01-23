from login.LoginPage import LoginPage
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner

class LoginAtlassian(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'./chromedriver')
        self.driver.maximize_window()
        self.driver.get("https://id.atlassian.com/login")
        self.login_page = LoginPage(self.driver)

    def test_web_title(self):
        assert self.login_page.is_title_matches(), "title is not match"

    def test_login(self):
        self.login_page.set_username("test@test.com")
        self.login_page.set_password("password")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output=''))