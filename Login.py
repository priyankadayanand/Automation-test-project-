from selenium import webdriver


driver = webdriver.Chrome(executable_path="E:\selenium drivers\drivers\chromedriver.exe")
driver.maximize_window()
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
