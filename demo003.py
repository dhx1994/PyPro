'''import itchat

itchat.auto_login(hotReload=True)

friendlists = itchat.get_friends()

newlist = []
for friend in friendlists:
    newlist.append(friend["City"])
citydict = {}
for i in newlist:
    num = newlist.count(i)
    citydict[i] = num
print(citydict)'''
from selenium import webdriver
import time
def micro1(para):
    driver = webdriver.Chrome(executable_path ="chromedriver")
    driver.get("https://www.baidu.com")
   # driver.find_element_by_id('kw').send_keys(para)  #通过元素的id来定位
    #driver.find_element_by_name('wd').send_keys(para)  #通过元素的name来定位
    #driver.find_element_by_class_name('s_ipt').send_keys(para)  #通过class_name来定位
    # driver.find_element_by_css_selector('input#kw.s_ipt').send_keys(para) #通过css_selector来定位
    # driver.find_element_by_tag_name('').send_keys(para)
    # driver.find_element_by_xpath('//*[@id="kw"]').send_keys(para)  # 通过xpath定位，可控性不好
    # driver.find_element_by_partial_link_text('新闻').send_keys(para)
    # driver.find_element_by_link_text('新闻').send_keys(para)
    driver.find_element_by_id('su').click()
    time.sleep(5)
    title = driver.title
    if '{}_百度搜索'.format(para) == title:
        print('测试成功！搜索成功！')
    else:
        print('测试失败！')
    driver.quit()  #退出
a = input("请输入搜索内容！")
micro1(a)
#<span class="bg s_ipt_wr quickdelete-wrap"><span class="soutu-btn"></span><input id="kw" name="wd" class="s_ipt" value=""
#  maxlength="255" autocomplete="off"><a href="javascript:;" id="quickdelete" title="清空" class="quickdelete" style="top: 0px; right: 0px;
#display: none;"></a></span>