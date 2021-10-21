import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# https://www.jianshu.com/p/1531e12f8852

# 创建谷歌浏览器
browser = webdriver.Chrome()

# 通过浏览器访问链接
browser.get('http://eip.hand-china.com/web/guest/personal')

# 找到对应的ID页面元素
# 用户名
browser.find_element_by_id("username").clear()
browser.find_element_by_id("username").send_keys("***")
# 密码
browser.find_element_by_id("password").clear()
browser.find_element_by_id("password").send_keys("***")
# 登录按钮
browser.find_element_by_name("submit").send_keys(Keys.ENTER)

# 等待3s 避免没有获取到日志信息系导致报错
time.sleep(3)

browser.get("http://app.hand-china.com/hrms/main.screen")
# 获取请求的日志信息
request_log = browser.get_log('performance')
print("++++++++++++++++"+request_log)


for i in range(len(request_log)):
    message = json.loads(request_log[i]['message'])
    message = message['message']['params']
    # .get() 方式获取是了避免字段不存在时报错
    request = message.get('request')
    if(request is None):
        continue
    url = request.get('url')
    print("----------------------------------"+url)
