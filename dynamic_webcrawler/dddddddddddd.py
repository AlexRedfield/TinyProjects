from selenium import webdriver

url='http://example.webscraping.com/places/default/search'
driver=webdriver.Chrome()
driver.get(url)
driver.find_element_by_id('search_term').send_keys('.')
js="document.getElementById('page_size').options[1].text='1000'"
driver.execute_script(js)

driver.find_element_by_id('search').click()

# 设置超时时间
driver.implicitly_wait(30)
links=driver.find_elements_by_xpath('//div[@id="results"]//a')
countries=[link.text for link in links]

print(countries)
driver.close()
