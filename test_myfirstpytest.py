from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

#Task10 Part 1
def test_task10part1(driver):
    driver.get("https://www.saucedemo.com")
    #Printing Title of the Webpage
    print('\nTitle is: ', driver.title)
    #Printing Current URL
    print('Current URL is: ', driver.current_url)
    #Extracting page source and saving it into a file
    page_content = driver.page_source
    with open("Webpage_task_11.txt", "w") as file:
        file.write(page_content)
    driver.quit()

def test_positive_test(driver):
    driver.get("https://www.saucedemo.com")
    assert driver.title == "Swag Labs", "Title is not Swag Labs"
    assert driver.current_url == "https://www.saucedemo.com/", "Current URL is not Sauce Demo"

    #Login to Dashboard with valid password
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    #assert that current url of the dashboard is displayed
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Current URL is not the Dashboard"

def test_negative_test(driver):
    driver.get("https://www.saucedemo.com")

    # Login to Dashboard with invalid password
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    # assert that error message is displayed
    assert driver.current_url != "https://www.saucedemo.com/inventory.html", "User is not in the login page"
    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert error_message == "Epic sadface: Username and password do not match any user in this service", "Error message was not displayed"
