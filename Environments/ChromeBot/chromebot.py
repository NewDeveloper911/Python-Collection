from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
'''
Keys can be used to get and emulate key presses
'''

PATH = "/Users/mac/Downloads/chromedriver 07-46-24-288"
driver = webdriver.Chrome(PATH)

driver.get("http://127.0.0.1:5000/login")
print(driver.title)

search = driver.find_element_by_name('nm')
search.clear()
search.send_keys("ChromeBot")
search.send_keys(Keys.RETURN) #type an enter key to submit our name

#print(driver.page_source) - This prints my entire source code for the base.html page
email = driver.find_element_by_name('email')
email.send_keys("thetruebot@gmail.com")
email.send_keys(Keys.RETURN)

dropdown = driver.find_element_by_link_text("Dropdown")
dropdown.click()
try:
    database = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "View database")))
    database.click()
except:
    print("Took too long for the bot to locate database")
    driver.quit()
'''
This code basically tells my bot to take a maximum of 10 seconds when searching
for the link to my database. If it takes too long, it will print an error
message using print() and quit
'''
names = driver.find_elements_by_class_name("data1")
emails = driver.find_elements_by_class_name("data2")
print("\nHere's a list of all users in my database")
for i in names:
    print(names[names.index(i)].text)
    print(emails[names.index(i)].text + "\n")
'''
Here, I've fetched the details of each user on my database and printed them.
'''
time.sleep(10)
driver.back() #goes back a page
#driver.forward() can be used to go forward a page and reloads an
#already loaded page again
try:
    dropdown = driver.find_element_by_link_text("Dropdown")
    dropdown.click()
    logout = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
    logout.click()
except:
    print("Took too long to log out")
    driver.quit()
driver.quit()
