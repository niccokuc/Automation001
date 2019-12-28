from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://google.com')
print(driver.title)
driver.find_element_by_name("q").send_keys("HELLO WORLD")
driver.find_element_by_name("btnK").submit()

