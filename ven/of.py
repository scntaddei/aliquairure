from selenium import webdriver

chrome_driver = Service("path/to/chromedriver")
chrome_driver.start()

driver = webdriver.Chrome(service=chrome_driver)
driver.get("https://www.example.com