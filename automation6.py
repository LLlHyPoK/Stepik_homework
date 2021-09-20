from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Firefox()
browser.get(link)

try:
    botton = browser.find_element_by_xpath('/html/body/form/div/div/button').click()

    confirm = browser.switch_to.alert
    confirm.accept()


    time.sleep(1)
    x_number = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = x_number.text
    x = float(x)
    y = math.log(abs(12*math.sin(x)))
    y = str(y)
    input = browser.find_element_by_xpath('//*[@id="answer"]')
    input.send_keys(y)

    submit = browser.find_element_by_xpath('/html/body/form/div/div/button').click()



finally:
    time.sleep(10)
    browser.quit()
