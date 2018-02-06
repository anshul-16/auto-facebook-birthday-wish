from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import schedule
import time

def job():
    chrome_path="path of chrome driver"    #enter the chrome path here
    driver=webdriver.Chrome(chrome_path)
    driver.get('http://facebook.com')
    username = driver.find_element_by_xpath("""//*[@id="email"]""")
    password = driver.find_element_by_xpath("""//*[@id="pass"]""")
    username.send_keys("username")                      #enter your user name in place of username
    password.send_keys("password")                      #enter your password in place of password
    elem_login=driver.find_element_by_id("loginbutton")
    elem_login.click()
    time.sleep(1)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(1)
    elem_events=driver.find_element_by_link_text("Events")
    elem_events.click()
    time.sleep(1)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(1)
    elem_birthdays=driver.find_element_by_link_text("Birthdays")
    elem_birthdays.click()
    time.sleep(2)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    for i in range(10):
        wish = driver.find_element_by_name("message").send_keys("Happy Birthday!")
        time.sleep(2)
        elem_text=driver.find_element_by_name("message_text").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.refresh()
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

#schedule.every().day.at("00:16").do(job)
job()

'''while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
'''
