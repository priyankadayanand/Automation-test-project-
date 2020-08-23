from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path="E:\selenium drivers\drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/horizontal_slider")

slider = driver.find_element_by_xpath("//div[@class='sliderContainer']//input")
move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(60, 0).release(). perform()
time.sleep(2)
move.click_and_hold(slider).move_by_offset(-60, 0).release(). perform()
time.sleep(2)