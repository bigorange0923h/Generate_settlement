from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# https://www.jianshu.com/p/1531e12f8852

# 创建谷歌浏览器
browser = webdriver.Chrome()

# 通过浏览器访问链接
browser.get('https://login.hand-china.com/sso/login?service=http%3A%2F%2Feip.hand-china.com%2Fc%2Fportal%2Flogin%3Fredirect%3D%252Fen%252Fpersonal%26refererPlid%3D50108%26p_l_id%3D20146')

# 找到对应的ID页面元素
# 用户名
browser.find_element_by_id("username").clear()
browser.find_element_by_id("username").send_keys("****")
# 密码
browser.find_element_by_id("password").clear()
browser.find_element_by_id("password").send_keys("****")
# 登录按钮
browser.find_element_by_name("submit").send_keys(Keys.ENTER)
