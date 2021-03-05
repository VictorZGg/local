from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
browser = webdriver.Chrome()

#2.通过浏览器向服务器发送URL请求
browser.get("https://www.baidu.com/")

sleep(3)

#3.刷新浏览器
browser.refresh()

#4.设置浏览器的大小
browser.set_window_size(1400,800)

#5.设置链接内容
element=browser.find_element_by_link_text("新闻")
element.click()




driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
#2.定位到要悬停的元素
element= driver.find_element_by_link_text("更多")

#3.对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(element).perform()

#找到链接
elem1=driver.find_element_by_link_text("百科")
elem1.click()

#通过元素选择器找到id=sh_2,并点击设置
elem2=driver.find_element_by_id("sh_1")
elem2.click()

#保存设置
elem3=driver.find_element_by_class_name("prefpanelgo")
elem3.click()




# print(driver.title)
driver.quit()





