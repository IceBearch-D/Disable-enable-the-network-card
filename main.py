import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import socket
from datetime import datetime
import os


def check_internet_connection():
    # 使用ping命令检测能否访问外部网站，这里以百度为例
    response = os.system(f"ping -n 1 baidu.com")
    if response == 0:
        print("Internet connection established")
        return True
    else:
        print("Internet connection unestablished, login again after 10 minutes")
        return False


# 连接校园网
options = Options()
options.add_argument('--headless')  # 启用无头模式
options.add_argument('--disable-gpu')  # 禁用GPU加速，提高性能

username_upc = "S24070010"# 学号
password_upc = "Ding033220++"

while True:
    if check_internet_connection():
        break
    driver = webdriver.Edge(options=options)
    driver.get('https://lan.upc.edu.cn/') # 有线网络，无线网是wlan
    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys(username_upc)
    password_input = driver.find_element(By.ID, 'pwd')
    driver.execute_script("arguments[0].style.display = 'block';", password_input)
    password_input.send_keys(password_upc)
    dropdown_trigger = driver.find_element(By.ID, 'selectDisname')
    dropdown_trigger.click()
    time.sleep(0.5)
    dropdown_trigger = driver.find_element(By.ID, '_service_3')
    # _service_3是中国联通，0是校园网，1是移动，4是电信
    dropdown_trigger.click()
    login_button = driver.find_element(By.ID, 'loginLink_div')
    login_button.click()
    time.sleep(2)
    print("click login")
    if check_internet_connection():
        break
    else:
        time.sleep(600)