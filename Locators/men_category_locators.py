from selenium.webdriver.common.by import By
from conftest import DriverSetUp

driver = DriverSetUp.driver


# Per Page Locators - can be placed under one class
# Locators can also be placed under function


def men_dropdown():
    men_dropdown_button = driver.find_element(By.XPATH, "//*[@id='ui-id-5']/span[2]")
    return men_dropdown_button


def men_item():
    men_item_clothes = driver.find_element(By.XPATH, "//*[@id='maincontent']/div[4]/div[1]/div[2]/div["
                                                     "3]/div/div/ol/li[1]/div/a/span/span/img")
    return men_item_clothes


def add_to_cart():
    add_to_cart_submit = driver.find_element(By.XPATH, "//*[@id='product-addtocart-button']")
    return add_to_cart_submit


def add_to_cart_color_error():
    add_to_cart_color = driver.find_element(By.XPATH, "//*[@id='super_attribute[143]-error']")
    return add_to_cart_submit


def add_to_cart_size_error():
    add_to_cart_size = driver.find_element(By.XPATH, "//*[@id='super_attribute[93]-error']")
    return add_to_cart_submit
