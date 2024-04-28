from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Start the WebDriver and open the HTML page
service = Service(executable_path='/usr/local/bin/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://punithkosana.github.io/Automation-Testing-with-Selenium/")

# Adding a delay to see the result
time.sleep(5)

# Assert some condition to verify the result
assert "Expected Title" in driver.title

# Take a screenshot
timestamp = time.strftime("%Y%m%d-%H%M%S")
screenshot_file = f"screenshot_{timestamp}.png"
driver.save_screenshot(screenshot_file)

# Close the WebDriver
driver.close()
