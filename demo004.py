from selenium import webdriver
import time
winlist = []

# 调用驱动
driver = webdriver.Chrome(executable_path ="chromedriver")

# 进入浏览器
driver.get("http://127.0.0.1:8080/morning/")
driver.find_element_by_link_text('登录').click()  #通过元素的id来定位
    #driver.find_element_by_name('wd').send_keys(para)  #通过元素的name来定位
    #driver.find_element_by_class_name('s_ipt').send_keys(para)  #通过class_name来定位
    # driver.find_element_by_css_selector('input#kw.s_ipt').send_keys(para) #通过css_selector来定位
    # driver.find_element_by_tag_name('').send_keys(para)
    # driver.find_element_by_xpath('//*[@id="kw"]').send_keys(para)  # 通过xpath定位，可控性不好
    # driver.find_element_by_partial_link_text('新闻').send_keys(para)
    # driver.find_element_by_link_text('新闻').send_keys(para)

# 登录
driver.find_element_by_name('user.loginName').send_keys('13957869385')               #输入账号
driver.find_element_by_name('user.loginPassword').send_keys('a123456')                 #输入密码
driver.find_element_by_id('btn_login').click()                                     #点击登录
time.sleep(2)
# 进入个人中心
driver.find_element_by_class_name('mian-nav-right-user').click()
time.sleep(3)
driver.find_element_by_link_text('个人中心').click()
time.sleep(2)

# 更改句柄
winlist = driver.window_handles #获取所有句柄
driver.switch_to.window(winlist[1])

# 设置密码
driver.find_element_by_link_text('密码设置').click()
driver.find_element_by_name('nowPassword').send_keys('a123456')
driver.find_element_by_name('newPassword').send_keys('b123456')
driver.find_element_by_name('confirmPwd').send_keys('b123456')
driver.find_element_by_xpath('//*[@id="p_tCont"]/div[3]/div/button[1]').click()
driver.find_element_by_xpath('/html/body/div[2]/div[2]/button[2]').click()
time.sleep(2)

# 退出登录
driver.find_element_by_class_name('mian-nav-right-user').click()
time.sleep(5)
driver.find_element_by_link_text('退出登录').click()
time.sleep(3)

# 重新登陆
driver.find_element_by_link_text('登录').click()
time.sleep(3)
driver.find_element_by_name('user.loginName').send_keys('13957869385')
time.sleep(1)
driver.find_element_by_name('user.loginPassword').send_keys('b123456')
driver.find_element_by_id('btn_login').click()
time.sleep(5)

# 结束
driver.close()

