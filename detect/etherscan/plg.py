# -*- coding: utf-8 -*-

import requests
from lxml import html, etree
import pysnooper
import random
from fake_useragent import UserAgent
import sys
sys.path.append("../..")
import bearychat_send as bs

"""get the information from amazon"""

@pysnooper.snoop()
def __token(url_token, token_title_xpath, token_head_address_xpath):
    #user agent
    url_detail = url_token
    user_agent = UserAgent().random
    HEADERS = {'User-Agent':user_agent,
                'Referer': "www.google.com"}
    cookies = 'v=3; \
                iuuid=1A6E888B4A4B29B16FBA1299108DBE9CDCB327A9713C232B36E4DB4FF222CF03; \
                webp=true; \
                ci=1%2C%E5%8C%97%E4%BA%AC; \
                __guid=26581345.3954606544145667000.1530879049181.8303; \
                _lxsdk_cuid=1646f808301c8-0a4e19f5421593-5d4e211f-100200-1646f808302c8; \
                _lxsdk=1A6E888B4A4B29B16FBA1299108DBE9CDCB327A9713C232B36E4DB4FF222CF03; \
                monitor_count=1; _lxsdk_s=16472ee89ec-de2-f91-ed0%7C%7C5; \
                __mta=189118996.1530879050545.1530936763555.1530937843742.18'
    cookie = {}
    for line in cookies.split(';'):
        name, value = cookies.strip().split('=', 1)
        cookie[name] = value
    count = 0
    #Because of anti-scrapy, running until get the information or up to 50x
    while True:
        count += 1
        response = requests.get(url_detail, cookies=cookie, headers=HEADERS)
        html_etree = etree.HTML(response.content.decode('utf-8'))
        # get the result of title
        token_title = html_etree.xpath(token_title_xpath) 
        token_title2 = html_etree.xpath('//table[@class="table table-md-text-normal table-hover"]//tbody//tr//td//span/text()') 
        token_title3 = html_etree.xpath('//table[@class="table table-md-text-normal table-hover"]//tr[1]/td[1]/span/text()') 
        token_title4 = html_etree.xpath('//table[@class="table table-md-text-normal table-hover"]/tbody/tr[0]/td[0]/span/text()') 
        token_title5 = html_etree.xpath('//table[@class="table table-md-text-normal table-hover"]//tr[2]/td[2]/text()') 
        token_head_address = html_etree.xpath(token_head_address_xpath) 
        print("token_title2", token_title2)
        print("token_title3", token_title3)
        print("token_title4", token_title4)
        print("token_title5", token_title5)
        if token_title or token_title2 or token_title3 or token_title4 or token_title5:
            print("token======")
            break
        if token_head_address:
            print("token_head_address: ", token_head_address)
            break

        # break when get info or fails
        if token_title or count > 30:
            break
    #store data to dictionary and then return
    news_dictionary = {"token": "Failed to get token infomation",
                        "percentage":"percentage ???"}


    return news_dictionary

def detect(data):
    # return token price and name from amazon    
    url_token = data.get("url_token") 
    url_img = data.get("url_img") 
    message_title = data.get("message_title")
    token_title_xpath = data.get("token_title_xpath")
    token_head_address_xpath = data.get("token_head_address_xpath")
    #detect price and title of token
    token_inform = __token(url_token, token_title_xpath, token_head_address_xpath)
    #send to beary chat
    bs.send(True, 
            message_title, 
            message_title, 
            "etherscan", #channel
            [{
                "title": token_inform.get("token"),
                "url": url_token,
                "text": token_inform.get("percentage"),
                "images": [
                    {"url": url_img}
                ]
            }]
    )
    
def main():
    pass
    #detect()

if __name__ == "__main__":
    main()

