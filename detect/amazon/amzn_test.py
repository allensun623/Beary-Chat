# -*- coding: utf-8 -*-

import requests
from lxml import html, etree
import random
from fake_useragent import UserAgent
import json
import pysnooper
"""get the information from amazon"""

@pysnooper.snoop()
def __product():
    url_detail = "https://www.amazon.com/dp/B07FK8SQDQ/ref=twister_B00WS2T4ZA?_encoding=UTF8&th=1"
    #Because of anti-scrapy, running until get the information or up to 30x
    count = 1
    title = ""
    at_count = 0
    while count < 100:
        html_etree = html_request(url_detail)
        print(html_etree)
        product_title_xpath1 = "//div[@id='title_feature_div']/div[@id='titleSection']/h1[@id='title']/span[@id='productTitle']/text()"
        product_title_xpath2 = "//h1[@id='title']/span[@id='productTitle']/text()"
        product_title_xpath3 = "//span[@id='productTitle']/text()" 
        title1 = html_etree.xpath(product_title_xpath1)
        title2 = html_etree.xpath(product_title_xpath2)
        title3 = html_etree.xpath(product_title_xpath3)
        if title1 is not None:
            at_count += 1 
        if title2 is not None:
            at_count += 1 
        if title3 is not None:
            at_count += 1 
        count += 1
    # url for image
    #url_img = html_etree.xpath("//div[@id='imgTagWrapperId']/img[@id='landingImage']/@src")
    #print(url_img)


def html_request(url_detail):
    #return html request with cookie, header
    cookies = 'v=3; \
                iuuid=1A6E888B4A4B29B16FBA1299108DBE9CDCB327A9713C232B36E4DB4FF222CF03; \
                webp=true; \
                ci=1%2C%E5%8C%97%E4%BA%AC; \
                __guid=26581345.3954606544145667000.1530879049181.8303; \
                _lxsdk_cuid=1646f808301c8-0a4e19f5421593-5d4e211f-100200-1646f808302c8; \
                _lxsdk=1A6E888B4A4B29B16FBA1299108DBE9CDCB327A9713C232B36E4DB4FF222CF03; \
                monitor_count=1; \
                _lxsdk_s=16472ee89ec-de2-f91-ed0%7C%7C5; \
                __mta=189118996.1530879050545.1530936763555.1530937843742.18'
    cookie = {}
    for line in cookies.split(';'):
        name, value = cookies.strip().split('=', 1)
        cookie[name] = value
    user_agent = UserAgent().random
    HEADERS = {'User-Agent':user_agent,
                'Referer': "www.google.com"}
    response = requests.get(url_detail, cookies=cookie, headers=HEADERS)
    html_etree = etree.HTML(response.content.decode('utf-8'))
    return html_etree

def main():
    __product()

if __name__ == "__main__":
    main()

