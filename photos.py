from re import search
from bs4 import BeautifulSoup
import requests
import html5lib
import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import time

cars = ["Ferrari", "Bugatti", "Toyota"]
for car in cars:    
    url = "https://www.pngwing.com/en/search?q=car"
    driver = webdriver.Chrome(executable_path="chromedriver_win32\chromedriver.exe")
    driver.get(url)
    search_all = driver.find_element(By.ID, "search_input")
    search_all.send_keys(car)
    time.sleep(3)
    click = driver.find_element(By.ID, "search_sub").click()
    time.sleep(5)
    url = driver.current_url
    r = requests.get(url)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, "html.parser")
    title = soup.title
    print(title)
    images = soup.find_all("img")
    for image in images:
        print(image)
        f = open("car.csv", "a")
        f.write(f"{str(image)}\n")
        f.close
                    
