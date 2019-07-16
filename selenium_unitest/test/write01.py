from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait

import time

driver=webdriver.Chrome()
driver.get("http://127.0.0.1:8000/index/")
time.sleep(2)
driver.maximize_window()
print(Ec.title_contains("index"))
# regester_element=driver.find_element_by_id("registerde")
# Ec.invisibility_of_element_located(regester_element)
locator=(By.ID,"registerde")
WebDriverWait(driver,1).until(Ec.visibility_of_element_located(locator))
driver.find_element_by_id("registerde").click()
driver.save_screenshot("selenium01.png")
code_img=driver.find_element_by_class_name("check-img")
left=code_img.location["x"]
top=code_img.location["y"]
width=code_img.size["width"]
height=code_img.size["height"]
right=left+width
bottom=top+height
im=Image.open("selenium01.png")
img=im.crop((left,top,right,bottom))
img.save("selenium01.png")
driver.close()