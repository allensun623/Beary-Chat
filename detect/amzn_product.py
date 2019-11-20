# -*- coding: utf-8 -*-

import requests
from lxml import html, etree
import pysnooper
import bearychat_send as bs
import random
from fake_useragent import UserAgent

"""get the information from amazon"""

@pysnooper.snoop()
def __product(url_prodect, product_title_xpath, product_price_xpath, current_price):
    #user agent
    url_detail = url_prodect
    user_agent = UserAgent().random
    HEADERS = {'User-Agent':user_agent,
                'Referer': "www.google.com"}
    count = 0
    #Because of anti-scrapy, running until get the information or up to 50x
    while True:
        count += 1
        response = requests.get(url_detail, headers=HEADERS)
        html_etree = etree.HTML(response.content.decode('utf-8'))
        # get the result of price and title
        product_title = html_etree.xpath(product_title_xpath) 
        product_price = html_etree.xpath(product_price_xpath) 
        # break when get info or fails
        if product_price or count > 30:
            break
    #store data to dictionary and then return
    news_dictionary = {"product": "Failed to get infomation",
                        "price":"$$$"}
    try:
        if product_price[0] == current_price: # if price changed
            d_price = {"price": "Price: " + product_price[0]}
        else:
            d_price = {"price": "Original price: " + current_price + "\n" + "Sale: " + product_price[0]}
        news_dictionary.update(d_price)
        d_product = {"product": product_title[0]}
        news_dictionary.update(d_product)
    except:
        pass

    return news_dictionary

def detect(data):
    # return product price and name from amazon    
    url_product = data.get("url_product") 
    url_img = data.get("url_img") 
    message_title = data.get("message_title")
    product_title_xpath = data.get("product_title_xpath")
    product_price_xpath = data.get("product_price_xpath")
    current_price = data.get("current_price")
    #detect price and title of product
    product_inform = __product(url_product, product_title_xpath, product_price_xpath, current_price)
    #send to beary chat
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
    
def main():
    pass
    #detect()

if __name__ == "__main__":
    main()

