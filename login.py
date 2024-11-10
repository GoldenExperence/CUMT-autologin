import time
import os
import subprocess
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

# 校园网名称设置
STUDENT_SSID = "CUMT_Stu"
TEACHER_SSID = "CUMT_Tec"
# 服务器地址
URL = "http://10.2.5.251/"
# 脚本运行时间
LIMIT = 150
# 加载用户名和密码
with open("config.txt", "r", encoding="utf-8") as f:
    USERNAME = f.readline().split('=')[1].strip()
    PASSWORD = f.readline().split('=')[1].strip()
    ISP = f.readline().split('=')[1].strip()


def get_wifi_name():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if "SSID" in line:
                return line.split(":")[1].strip()
        return None
    except Exception as e:
        formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{formatted_time}: 检查Wi-Fi连接状态时出错: {e}")
        return None


def send_login_request(wifi_name):
    service = Service(executable_path=r"chrome\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    def find_element(value):
        input_elements = driver.find_elements(By.NAME, value=value)
        for input_element in input_elements:
            if input_element.get_attribute('type') != 'hidden':
                return input_element

    try:
        driver.get(URL)
        time.sleep(2)
        student_id_input = find_element('DDDDD')
        student_id_input.send_keys(USERNAME)
        # 填充密码
        password_input = find_element('upass')
        password_input.send_keys(PASSWORD)
        if wifi_name == STUDENT_SSID:
            # 选择运营商
            select_element = Select(find_element('ISP_select'))
            select_element.select_by_visible_text(ISP)
        # 点击登录按钮
        login_button = find_element("0MKKey")
        driver.execute_script("arguments[0].click();", login_button)

        time.sleep(2)

    except Exception as e:
        formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{formatted_time}: ChromeDriver错误")
        print(e)

    finally:
        driver.quit()


def main(limit):
    while limit:
        limit -= 1
        wifi_name = get_wifi_name()
        if wifi_name is None:
            time.sleep(1)
            continue
        if STUDENT_SSID == wifi_name or TEACHER_SSID == wifi_name:
            send_login_request(wifi_name)
            break
        else:
            break


if __name__ == "__main__":
    main(LIMIT)
