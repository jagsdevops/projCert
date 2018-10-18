from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options();
options.add_argument("--headless");
options.binary='/usr/bin/chromium-browser'
driver_path='/home/edureka/bin/chromedriver'
browser = webdriver.Chrome(chrome_options=options,executable_path=driver_path);
browser.get("http://production-slave.example.com:8080/");
time.sleep(2)
link = browser.find_element_by_link_text('About Us')
link.click();
time.sleep(1)
text = 'This is about page.'
assert browser.page_source.find(text)
browser.quit()
