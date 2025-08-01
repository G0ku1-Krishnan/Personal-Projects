#utils/driver_factory.py

from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_arguement("__start-maximized")
    driver = webdriver.Chrome(option=option)
    driver.implicitly_Wait(10)
    return driver
