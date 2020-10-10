from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
'''
Keys can be used to get and emulate key presses
'''

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://127.0.0.1:5000/login")
print(driver.title)

search = driver.find_element_by_name('nm')
search.send_keys("ChromeBot")
search.send_keys(Keys.RETURN) #type an enter key to submit our name

#print(driver.page_source) - This prints my entire source code for the base.html page
email = driver.find_element_by_name('email')
email.send_keys("thetruebot@gmail.com")
email.send_keys(Keys.RETURN)

driver.get("http://127.0.0.1:5000/view")
names = driver.find_elements_by_class_name("data1")
emails = driver.find_elements_by_class_name("data2")
print("\n Here's a list of all users in my database")
for i in names:
    print(names[names.index(i)].text)
    print(emails[names.index(i)].text + "\n")
'''
Here, I've fetched the details of each user on my database and printed them.
'''
time.sleep(5)
driver.quit()
