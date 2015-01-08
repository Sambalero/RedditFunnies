from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get('http://www.reddit.com/r/funny')
links = driver.find_elements_by_css_selector('a.title')
hrefs = []
for link in links:
  hrefs.append(link.get_attribute('href'))
for i in range(2, len(hrefs)-1):
  driver.find_element_by_css_selector('body').send_keys(Keys.COMMAND + 't')
  driver.get(hrefs[i])

