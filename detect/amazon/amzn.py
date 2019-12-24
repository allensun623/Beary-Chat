# -*- coding: utf-8 -*-

import requests
from lxml import html, etree
import bearychat_send as bs
import random
from fake_useragent import UserAgent
import json
import pysnooper
"""get the information from amazon"""

@pysnooper.snoop()
def __product(url_product, url_img_xpath, product_title_xpath, product_price_xpath, target_price):
    #user agent
    if_send = False
    url_detail = url_product
    #Because of anti-scrapy, running until get the information or up to 30x
    html_etree = html_request(url_detail)
    # url for image
    try:
        url_img = html_etree.xpath(url_img_xpath)[0]
    except:
        url_img = "http://media.rhizome.org/blog/9604/Vine-Oops-404.png"
    # get the result of price and title
    try:
        product_title = html_etree.xpath(product_title_xpath)[0]         
    except: 
        product_title = "Failed to get infomation" 
        if_send = True   
    for price in product_price_xpath:
        try:
            product_price = html_etree.xpath(price)[0] 
        except:
            pass
            
    #store data to dictionary and then return
    news_dictionary = {"product": "Failed to get infomation",
                        "price":"$$$"}
    #title
    try:
        d_product = {"product": product_title.replace('\n','')}
        news_dictionary.update(d_product)
    except:
        pass
    #price
    try:
        print(price_comparison(product_price, target_price))
        if_send = price_comparison(product_price, target_price)
        d_price = {"price": "Sale: " + product_price + " (target price: $%s)"%target_price}
        news_dictionary.update(d_price)
    except:
        pass
    print(news_dictionary)
    return (if_send, url_img, news_dictionary)

@pysnooper.snoop()   
def price_comparison(c_price, t_price):
    #remove the first charactor "$" of the string and convert to float
    current_price = float(c_price[1:])
    target_price = float(t_price)
    #if the current price <= target price, return boolean true
    return (True if current_price <= target_price else False)

def html_request(url_detail):
    #return html request with cookie, header
    cookies = 'v=3; \
                iuuid=1A6E888B4A4B29B16FBA1299108DBE9CDCB327A9713C232B36E4DB4FF222CF03; \
                webp=true; \
                ci=1%2C%E5%8C%97%E4%BA%AC; \
                __guid=26581345.3954606544145667000.1530879049181.8303; \
                _lxsdk_cuid=1646f808301c8-0a4e19f5421593-5d4e211f-100200-1646f808302c8; \
                _lxsdk=1A6E888B4A4B29B16FBA1299108DBE9CDCB327A9713C232B36E4DB4FF222CF03; \
                monitor_count=1; 
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

def detect(data):
    # return product price and name from amazon    
    url_product = data.get("url_product") 
    url_img_xpath = data.get("url_img") 
    message_title = data.get("message_title")
    product_title_xpath = data.get("product_title_xpath")
    product_price_xpath = data.get("product_price_xpath")    
    target_price = data.get("target_price")
    #detect price and title of product
    if_send, url_img, product_inform = __product(url_product, 
                                url_img_xpath,
                                product_title_xpath, 
                                product_price_xpath, 
                                target_price)
    #send to beary chat
    if if_send:
        bs.send(True, 
                message_title, 
                message_title, 
                "promotion", #channel
                [{
                    "title": product_inform.get("product"),
                    "url": url_product,
                    "text": product_inform.get("price"),
                    "images": [
                        {"url": url_img}
                    ]
                }]
        )

def product_info():
    """get xpath information"""
    with open('in/amzn.json') as json_file:
        data = json.load(json_file)
    for key, value in data.items():
        url_product = value.get("url_product")
        url_img ="//div[@id='imgTagWrapperId']/img[@id='landingImage']/@src"
        product_title_xpath = "//div[@id='title_feature_div']/div[@id='titleSection']/h1[@id='title']/span[@id='productTitle']/text()"
        product_price_xpath = ["//tr[@id='priceblock_ourprice_row']/td[@class='a-span12']/span[@id='priceblock_ourprice']/text()",
                            "//tr[@id='priceblock_saleprice_row']/td[@class='a-span12']/span[@id='priceblock_saleprice']/text()"]
        message_title = key
        target_price = value.get("target_price")
        product_xpath = {
            "url_product": url_product,
            "url_img": url_img,
            "message_title": message_title,
            "product_title_xpath": product_title_xpath,
            "product_price_xpath": product_price_xpath,
            "target_price": target_price 
        }

        detect(product_xpath)

def main():
    
    #detect()

if __name__ == "__main__":
    main()

