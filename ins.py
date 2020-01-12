from selenium import webdriver
from instabot import Bot
import urllib
import time
from datetime import datetime
import os

browser = webdriver.Firefox(executable_path=r"./geckodriver.exe")
BASE_URL = "https://www.instagram.com/explore/tags/"
tags = ['india','travel']
img_urls = []
cnt = 1
bot = Bot()
bot.login(username="username", password="password")
for tag in tags:
    browser.get(f"{BASE_URL}{tag}/")
    temp = browser.find_elements_by_class_name("FFVAD")
    i = 0
    for i in range(1):
        img_urls.append(temp[i].get_attribute('src'))
        urllib.request.urlretrieve(f"{img_urls[i]}", f"./photos/{cnt}.jpg")
        # print(cnt)
        cnt += 1
    img_urls.clear()
    browser.get("https://www.all-hashtag.com/hashtag-generator.php")
    time.sleep(5)
    flag = browser.find_element_by_xpath("//input[@id ='keyword']")
    flag.send_keys(tag)
    k = browser.find_element_by_xpath("//label[@for ='input-top']")
    k.click()
    k = browser.find_element_by_class_name("btn-gen")
    k.click()
    time.sleep(10)
    get_hashtag = browser.find_element_by_class_name("copy-hashtags")
    get_caption = str(get_hashtag.get_attribute("innerHTML"))
    for filename in os.listdir("./photos"):
        time.sleep(30)
        bot.upload_photo(
            f"./photos/{filename}", caption=f"Follow @socialtrendsss for more such content {get_caption}")
    for filename in os.listdir("./photos"):
        file_path = os.path.join("./photos", filename)
        os.unlink(file_path)
browser.quit()
