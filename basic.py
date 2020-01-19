from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(r'./chromedriver')
driver.maximize_window()
driver.get("https://www.howtoautomate.in.th")

# verify web page title
assert "Best Practices and Tips For Automated Testing in Thailand" in driver.title

first_thumb = driver.find_element_by_css_selector(".td-small-thumb:first-child")
first_thumb.click()

# wait object
wait = WebDriverWait(driver, 10)
wait.until(
    expected_conditions.title_is("Electron JS ฉบับเดียวจบยันเขียนเทส | HowToAutomate.in.th")
)

# close driver 
driver.close()