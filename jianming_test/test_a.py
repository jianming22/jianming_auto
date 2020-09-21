# import pytest
#
# @pytest.fixture()
#
# def add_fixture():
#     print("\n先登录")
#     return "登录"
#
# @pytest.fixture()
# def dir_fixture():
#     print("\n不登录")
#     return "不登录"

# def add(a,b):
#     s = a+b
#     return s
# add(4,6)
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os
#登录
def test_image():
    driver =webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://baidu.com/")
    pic_path = '.\\image'
    isexists = os.path.exists(pic_path)
    if isexists:
        pass
    else:
        os.makedirs(pic_path)
    time.sleep(3)
    print(driver.title)
    try:
        assert '百度一下，你就知道' == driver.title
        assert "1" == "1"
        print('Assertion test pass.')
    except Exception as e:
        print('Assertion test fail.', format(e))
        driver.save_screenshot('.//image//%s.png' % int(time.time()))
    assert '百度一下，你就知道' == driver.title
    driver.quit()
