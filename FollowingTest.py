from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time




print("opening...")
driver = webdriver.Chrome()
driver.get("https://twitter.com/")
driver.maximize_window()
time.sleep(2)


@allure.severity(allure.severity_level.NORMAL)
def test_login():
    signinicon = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
    signinicon.click()

    time.sleep(2)
    username = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]')

    username.click()
    time.sleep(2)
    username2 = driver.find_element(By.NAME, 'text')
    username2.send_keys("teambrown2003")
        # username.submit()
        # time.sleep(1)
    nextbutton = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
    nextbutton.click()
    time.sleep(1)
    passwordbutton = driver.find_element(By.NAME, 'password')

    time.sleep(2)
    passwordbutton.send_keys("cocomelon12")
    loginbutton = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
    loginbutton.click()
    print("Login Successful")
    time.sleep(5)

def test_Explore():
    Explorebutton = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div')
    Explorebutton.click()
    time.sleep(2)
    Trendingbutton=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a')
    Trendingbutton.click()
    time.sleep(2)
    Aashiyanabutton=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[3]/div/div/div/div/div[2]')
    Aashiyanabutton.click()
    time.sleep(2)
    Homebutton=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[1]')
    Homebutton.click(1)
    time.sleep(1)