from appium import webdriver

# 打开被测的app
desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '9'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'PCT-AL10'                # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'com.tbk.daka0401'       # app的名字：adb shell dumpsys activity activities | findstr mResumedActivity"：andriod 8.0
desired_caps['appActivity'] = '.activity.MainActivity'                   # app的启动页名字：adb shell dumpsys activity | findstr "mFocusedActivity"
desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘
# 解锁手机并且去打开app
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

app = driver.find_element_by_id("com.tbk.daka0401:id/titleTv")
app.send_keys('电脑')