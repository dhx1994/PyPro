import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # 这里是导入动态查找需要的第三方包
def find(driver, timeout, locator):
    element = WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))  # 实现元素的动态定位
    return element  
def test_01_demo1():
    driver = webdriver.Chrome(executable_path ="H:\\Python\\PyPro\\chromedriver.exe")
    driver.get('http://132.232.44.158:8080/register')
    driver.maximize_window()
    
    search_element1 = ('id','username')
    find(driver,20,search_element1).send_keys('13958961234')

    search_element2 = ('id','code')
    find(driver,20,search_element2).send_keys('1234')

    search_element3 = ('id','password')
    find(driver,20,search_element3).send_keys('123')

    search_element4 = ('id','rePassword')
    find(driver,20,search_element4).send_keys('123')

    search_element5 = ('id','btnReg')
    find(driver,20,search_element5).click()

    driver.quit()


if __name__ == "__main__":
    test_01_demo1()

