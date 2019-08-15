from selenium.webdriver.support.ui import WebDriverWait
def find_element(driver,locator):
    """
        查找单个元素
            参数：locator=("id", "123")
            类型：w
            ID = "id"
            XPATH = "xpath"
            LINK_TEXT = "link text"
            PARTIAL_LINK_TEXT = "partial link text"
            NAME = "name"
            TAG_NAME = "tag name"
            CLASS_NAME = "class name"
            CSS_SELECTOR = "css selector"
    """
    element = WebDriverWait(driver, 10).until(lambda s: s.find_element(*locator))  # 实现元素的动态定位
    return element  
def is_element_exist(driver,locater):
    try:
        WebDriverWait(driver, 10).until(lambda s: s.find_element(*locator))  # 实现元素的动态定位
        return True
    except:
        return False