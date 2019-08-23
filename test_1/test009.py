from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def find_element(driver,waittime,locator):
    element = WebDriverWait(driver, waittime).until(lambda s: s.find_element(*locator))  # 实现元素的动态定位
    return element
def is_elemnet_exit(driver,locator):
    try:
        WebDriverWait(driver, 10).until(lambda s: s.find_element(*locator))
        print('ture')
    except:
        print('false')
driver = webdriver.Chrome(executable_path='H:\Python\PyPro\chromedriver.exe')
driver.get('http://132.232.44.158:8080/login')

driver.maximize_window()

element1 = ('id','username')
find_element(driver,10,element1).send_keys('13957869385')

element2 = ('id','password')
find_element(driver,10,element2).send_keys('123456')

element3 = ('id','btnLogin')
find_element(driver,10,element3).click()

element4 = ('xpath','//*[@id="J_wrap_pro_add"]/li[1]/div[1]/a/img')
find_element(driver,10,element4).click()

element5 = ('id','J_mer_saleTag')
find_element(driver,10,element5).click()

element6 = ('xpath','//*[@id="J_header_cart"]/div[1]/a[1]')
find_element(driver,10,element6).click()

element7 = ('class name','cart_del_confirm_box')
is_elemnet_exit(driver,element7)


    

