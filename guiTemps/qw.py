import logging
from selenium import webdriver
from page_object.searchpage import SearchPage
 
logging.basicConfig(level=logging.DEBUG)
 
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:9222")
 
driver = webdriver.Chrome(options=options)
 
# 访问网址
driver.get("http://www.baidu.com")
print(driver.title)
search = SearchPage(driver)
search.input_search("selenium")