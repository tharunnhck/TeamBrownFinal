from selenium import webdriver
import allure
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

import random




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
    time.sleep(3)

@allure.severity(allure.severity_level.MINOR)
def test_tweet():
    whatshappening = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/a/div[2]/div/div')
    whatshappening.click()

    time.sleep(1)
    postbar = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
    list1 = [range(10, 1000)]
    randomm = random.choice(list1)

    postbar.send_keys("Team Brown is On Twitter!!!")

    time.sleep(1)
    postbutton = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div')
    postbutton.click()
    time.sleep(2)

@allure.severity(allure.severity_level.MINOR)
def test_subscribe():
    subscribe1button = driver.find_element(By.XPATH,
                                           '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/aside/a')
    subscribe1button.click()
    time.sleep(1)
    subscribe2button = driver.find_element(By.XPATH,
                                           '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[4]')
    subscribe2button.click()
    time.sleep(2)
    pay1button = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div[2]')
    pay1button.click()
    time.sleep(2)
    pay2button = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]')
    pay2button.click()
    time.sleep(2)
    numberbutton = driver.find_element(By.XPATH,
                                       '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div')
    numberbutton.click()
    time.sleep(2)
    passwordbutton = driver.find_element(By.XPATH,
                                         '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input')
    passwordbutton.click()
    passwordbutton.send_keys('cocomelon12')
    time.sleep(1)
    pass1 = driver.find_element(By.XPATH,
                                '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
    pass1.click()


    time.sleep(1)
    pass3 = driver.find_element(By.XPATH,
                                '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
    pass3.click()
    time.sleep(1)




@allure.severity(allure.severity_level.MINOR)
def test_following():
    followingtab=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/nav/div/div[2]/div/div[2]/a')
    followingtab.click()
    time.sleep(2)

@allure.severity(allure.severity_level.MINOR)
def test_Trending():
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
    Homebutton.click()

@allure.severity(allure.severity_level.MINOR)
def test_Sports():
    Explorebutton = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div')
    Explorebutton.click()
    time.sleep(2)
    Sportsbutton = driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[4]/a')
    Sportsbutton.click()
    time.sleep(3)
    Iyarabutton = driver.find_element(By.XPATH,
                                      '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[3]/div/div')
    Iyarabutton.click()
    time.sleep(1)



@allure.severity(allure.severity_level.MINOR)
def test_profile():
    profileicon = driver.find_element(By.XPATH,
                                      '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[8]')
    profileicon.click()
    time.sleep(2)
    profilepic = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div/div[2]/div/a')
    profilepic.click()
    time.sleep(2)

    closebutton = driver.find_element(By.XPATH,
                                      '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div')
    closebutton.click()


    time.sleep(2)

@allure.severity(allure.severity_level.MINOR)
def test_backgroundimage():
    background=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/a/div/div[2]/div/img')
    background.click()
    close = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div')
    close.click()
    time.sleep(1)


@allure.severity(allure.severity_level.MINOR)
def test_notify():
    notifytab=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[3]')
    notifytab.click()
    time.sleep(1)
    notification=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/section/div/div/div[1]/div/div/article')
    notification.click()
    time.sleep(1)
    gotit=driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div')
    gotit.click()

    time.sleep(1)


@allure.severity(allure.severity_level.MINOR)
def test_logout():
    time.sleep(3)
    accountsbutton = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/header/div/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[4]/div')
    accountsbutton.click()
    logoutbutton = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]/div[1]')
    logoutbutton.click()
    logoutbutton2 = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div')
    logoutbutton2.click()
    time.sleep(1)


