import unittest
from selenium import webdriver                        
from selenium.webdriver.support.ui import WebDriverWait # 这里是导入动态查找需要的第三方包
class TestCaseDemo1(unittest.TestCase):
    def test_selenium1(self):
        driver = webdriver.Chrome(executable_path="H:\Python\PyPro\chromedriver.exe")
        driver.maximize_window()
        driver.get("http://132.232.44.158:8080/")

        search_element1=('xpath','//*[@id="J_wrap_pro_add"]/li[1]/div[1]/a/img')
        find(driver,30,search_element1).click()
 
        search_element2 = ('xpath','//*[@id="J_mer_saleTag"]')
        find(driver,30,search_element2).click()

        search_element3 = ('xpath','//*[@id="J_header_cart"]/div[1]/a[1]')
        find(driver,30,search_element3).click()

        title = driver.title
        a = '删除'
        self.assertIn(title,a)

def find(driver, timeout, locator):
    element = WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))  # 实现元素的动态定位
    return element  

if __name__ == "__main__":
    unittest.main()