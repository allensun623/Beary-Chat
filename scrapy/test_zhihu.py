import re
import os
import selenium
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import pysnooper
"""通过Python爬取这些问题的内容，浏览次数，关注人数，总结一份权威（搞笑）的“沙雕”问题排行榜"""
@pysnooper.snoop()
def scrapy_zhihu():

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
    driver = webdriver.Chrome(executable_path = DRIVER_BIN)
   
    #driver.maximize_window()

    url = 'https://www.zhihu.com/question/37453271'
    js='window.open("'+url+'")'
    driver.execute_script(js)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    for i in range(100):
        js="var q=document.documentElement.scrollTop=10000000"  
        driver.execute_script(js)

    all_html = [k.get_property('innerHTML') for k in driver.find_elements_by_class_name('AnswerItem')]
    all_text = ''.join(all_html)

    #all_text = all_text.replace('\u002F','/')
    all_text = all_text.replace('questions','question')
    pat = 'question/\d+'
    questions = list(set([k for k in re.findall(pat,all_text)]))
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win32; x32; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Connection': 'keep-alive'}
    cookies ='v=3; iuuid=1A6E888B4A4B29B16FBA1299108DBE9CDCB327A9713C232B36E4DB4FF222CF03; webp=true; ci=1%2C%E5%8C%97%E4%BA%AC; __guid=26581345.3954606544145667000.1530879049181.8303; _lxsdk_cuid=1646f808301c8-0a4e19f5421593-5d4e211f-100200-1646f808302c8; _lxsdk=1A6E888B4A4B29B16FBA1299108DBE9CDCB327A9713C232B36E4DB4FF222CF03; monitor_count=1; _lxsdk_s=16472ee89ec-de2-f91-ed0%7C%7C5; __mta=189118996.1530879050545.1530936763555.1530937843742.18'
    cookie = {}
    for line in cookies.split(';'):
        name, value = cookies.strip().split('=', 1)
        cookie[name] = value

    questions_df = pd.DataFrame(columns = ['title','visit','follower','answer','is_open'])

    for i in range(len(questions)):
        try:
            url = 'https://www.zhihu.com/'+questions[i]
            html = requests.get(url,cookies=cookie, headers=header).content
            bsObj = BeautifulSoup(html.decode('utf-8'),"html.parser")
            text = str(bsObj)
            title = bsObj.find('h1',attrs={'class':'QuestionHeader-title'}).text
            visit = int(re.findall('"visitCount":\d+',text)[0].replace('"visitCount":',''))
            follower = int(re.findall('"followerCount":\d+',text)[0].replace('"followerCount":',''))
            answer = int(re.findall('"answerCount":\d+',text)[0].replace('"answerCount":',''))
            is_open = int(len(re.findall('问题已关闭',text))==0)
            questions_df = questions_df.append({'title':title,'visit':visit,
                                                'follower':follower,'answer':answer,
                                                'is_open':is_open},ignore_index=True)
            time.sleep(2)
            print(i)
        except:
            print('错误'+str(i))


def main():
    scrapy_zhihu()

if __name__ == "__main__":
    main()