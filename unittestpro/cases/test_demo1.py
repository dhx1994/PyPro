import unittest
from selenium import webdriver                        
from selenium.webdriver.support.ui import WebDriverWait # 这里是导入动态查找需要的第三方包
from utils.seleniumtools import find_element
from utils.seleniumtools import is_element_exist
class TestCaseDemo1(unittest.TestCase):
   
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="H:\\Python\\PyPro\\UnittestPro\\drivers\\chromedriver.exe")
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_selenium1(self):
        self.driver.get("http://132.232.44.158:8080/")
        search_element1=('xpath','//*[@id="J_wrap_pro_add"]/li[1]/div[1]/a/img')
        find_element(self.driver,search_element1).click()
 
        search_element2 = ('xpath','//*[@id="J_mer_saleTag"]')
        find_element(self.driver,search_element2).click()

        search_element3 = ('xpath','//*[@id="J_header_cart"]/div[1]/a[1]')
        find_element(self.driver,search_element3).click()
        
        search_element4 = ('xpath','//*[@id="cart_item_2"]/td[6]/div/a')
        is_element_exist(self.driver,search_element4)
if __name__ == "__main__":
    unittest.main()