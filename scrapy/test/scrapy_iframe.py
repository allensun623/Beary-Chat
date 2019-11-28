# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import sys
from pyvirtualdisplay import Display
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
driver = webdriver.Chrome(executable_path = DRIVER_BIN)
#chrome_options = Options()
#chrome_options.add_argument('--headless')
#driver = webdriver.Chrome('/usr/local/Sunanang/chromedriver/chromedriver',
#                         chrome_options=chrome_options)


def getDriverHttp(url):
    driver.get(url)
    iframe = driver.find_elements_by_tag_name('iframe')[1]
    driver.switch_to.frame(iframe)                          # 最重要的一步
    soup = BeautifulSoup(driver.page_source, "html.parser")
    return soup


def getVideoUrl(url):
    soup = getHttp(url)
    miPlayer = soup.find('div',id='J_miPlayer')
    url = miPlayer.find('video').get('src')
    driver.quit()
    return url


if __name__ == '__main__':
    path = getVideoUrl(u'http://aaxxy.com/vod-play-id-10788-src-1-num-2.html')
# path = getVideoUrl(url==sys.argv[1])
    print(path)