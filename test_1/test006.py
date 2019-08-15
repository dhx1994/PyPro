from selenium import webdriver
import time

# 调用驱动
driver = webdriver.Chrome(executable_path ="H:\Python\PyPro\chromedriver.exe")

# 进入浏览器
driver.get("http://118.24.29.59:8080/")

d = driver.find_element_by_xpath('//*[@id="J_wrap_pro_add"]/li[1]/div[1]/a/img')
d.click()

d1 = driver.find_element_by_class_name('bt_add_car')
d1.click()

d2 = driver.find_element_by_class_name('header_cart_title')
d2.click()

# 判断是否加入购物车成功
try:
    driver.find_element_by_xpath('//*[@id="cart_item_1"]/td[2]/a')
except:
    print('商品加入购物车失败')

d3 = driver.find_element_by_xpath('//*[@id="J_cart_bar"]/div[1]/a')  # 立即结算
d3.click()

try:
    d4 = driver.find_element_by_css_selector('button.co_comfirm_submit.J_confirm_submit') # 尝试定位提交订单按钮
    d4.click()
except:
    driver.find_element_by_id('username').send_keys('13957869381') 
    driver.find_element_by_id('password').send_keys('123')
    driver.find_element_by_id('btnLogin').click() # 登录账号
    driver.find_element_by_xpath('//*[@id="J_header_cart"]/div[1]/a[1]').click() # 进入购物车
    time.sleep(3)
    d4 = driver.find_element_by_css_selector('a.button_bg_4.button_bg.J_omn_checkout.J_checkout')
    d4.click()      # 立即结算
    driver.find_element_by_css_selector('button.co_comfirm_submit.J_confirm_submit').click()   # 提交订单
    

