from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path="E:\selenium drivers\drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/hovers")

ExpectedUser1 = "name: user1"
ExpectedUser2 = "name: user2"
ExpectedUser3 = "name: user3"

action = ActionChains(driver)
# User 1
image1Ele = driver.find_element_by_css_selector("#content > div > div:nth-child(3) > img")
action.move_to_element(image1Ele).perform()
userEle = driver.find_element_by_css_selector("#content > div > div:nth-child(3) > div > h5")
userName = userEle.text
assert userName in ExpectedUser1
time.sleep(1)

# User 2
image2Ele = driver.find_element_by_css_selector("#content > div > div:nth-child(4) > img")
action.move_to_element(image2Ele).perform()
user2Ele = driver.find_element_by_css_selector("#content > div > div:nth-child(4) > div > h5" )
userName2 = user2Ele.text
assert userName2 in ExpectedUser2
time.sleep(1)

# User 3
image3Ele = driver.find_element_by_css_selector("#content > div > div:nth-child(5) > img")
action.move_to_element(image3Ele).perform()
user3Ele = driver.find_element_by_css_selector( "#content > div > div:nth-child(5) > div > h5" )
userName3 = user2Ele.text
assert userName3 in ExpectedUser3
time.sleep(1)