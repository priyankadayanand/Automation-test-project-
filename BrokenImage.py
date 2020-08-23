from selenium import webdriver
import requests


driver = webdriver.Chrome(executable_path="E:\selenium drivers\drivers\chromedriver.exe")
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/broken_images')

images = driver.find_elements_by_tag_name('img')

class Node:
 def __init__(self, data=None, next=None):
  self.data = data
  self.next = next

class LinkedList:
 def __init__(self):
  self.head = None

for image in images:
   LL = LinkedList()
   LL.head = Node(image.get_attribute('src'))
   print(LL.head.data)
   resp = requests.get(LL.head.data)
   if resp.status_code != 200:
       print("Image is broken")
   else:
    print("Pass")

driver.close()




