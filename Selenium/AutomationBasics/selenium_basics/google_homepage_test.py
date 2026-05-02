from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.microsoft import EdgeChromiumDriverManager


browser = input('What browser do you wan t to use?')

match (browser.lower()):
    case 'chrome':
        driver = webdriver.Chrome(service=Service('../resources/chromedriver.exe'))
    case 'edge':
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe '))
        #service=Service(EdgeChromiumDriverManager().install()))
    case _:
        print('Unknown browser - Not Available. \n Executing with defaulting EDGE Browser')
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe '))

driver.get("https://www.google.com")



pagetitle = driver.title


if pagetitle == 'Google':
    print("Google Homepage loaded - Pass")
else:
    print("Google Homepage Not loaded - Fail")

sleep(5)

driver.quit()