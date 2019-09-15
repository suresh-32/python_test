from selenium import webdriver
import pytest
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 3.7\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    print("Test completed")
def test_login(test_setup):
    driver.get("http://newtours.demoaut.com/")
    driver.find_element_by_name("userName").send_keys("mercury")
    driver.find_element_by_name("password").send_keys("mercury")
    driver.find_element_by_name("login").click()
    driver.implicitly_wait(30)
    print(driver.title)

