import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import shutil
import time

url = "http://www.rebeccabathory.com/orphansoftime"

# web_r = requests.get(url)
#
# web_soup = BeautifulSoup(web_r.text, 'html.parser')
#
# for img in web_soup.findAll('img'):
#     print(img)

driver = webdriver.Chrome()

driver.get(url)

# for img in sel_soup.findAll('img'):
#     print(img)


# iteration = 0
# while iteration < 10:
html = driver.execute_script("return document.documentElement.innerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')
images = []
for i in sel_soup.findAll('div', {'class': 'lazyload-wrap'}):
    images.append(i.findAll('img')[0]['src'])
current_path = os.getcwd()
for img in images:
    try:
        file_name = os.path.basename(img)
        new_paths = os.path.join(current_path, "images", file_name)
        img_r = requests.get(img, stream=True)
        with open(new_paths, "wb") as output_file:
            shutil.copyfileobj(img_r.raw, output_file)
        del img_r
    except:
        pass
    # iteration += 1
    # time.sleep(5)
