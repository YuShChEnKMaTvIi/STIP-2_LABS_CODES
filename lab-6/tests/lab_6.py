from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
time.sleep(5)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Remote(
    command_executor='http://selenium-1:4444/wd/hub',
    options=chrome_options
)


driver.get("https://google.com")
print(driver.title)
driver.quit()
