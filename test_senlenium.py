from  selenium  import webdriver
import pytest

def test_demo1():
    # 打开浏览器 
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.maximize_window()
    driver.get("http://132.232.44.158:9999/shopxo/")

    #定位并操作元素

    driver.find_element_by_id("search-input").send_keys("华为")
    driver.find_element_by_id("ai-topsearch").click()
    try:
        assert "￥1999.00" == driver.find_element_by_xpath('/html/body/div[4]/div/ul/li/div/p[2]/strong')
        print("测试用例执行成功")
    except:
        print("测试用例执行失败")

