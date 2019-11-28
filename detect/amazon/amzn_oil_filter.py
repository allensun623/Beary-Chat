# -*- coding: utf-8 -*-

import requests
from lxml import html, etree
import pysnooper
import bearychat_send as bs
import random
from fake_useragent import UserAgent

"""get the updated news from gate.io"""

@pysnooper.snoop()
def __product(url):
    #user agent
    url_detail = url
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
        # xpath would change frequently
        product_title = html_etree.xpath("//div[@id='title_feature_div']/div[@id='titleSection']/h1[@id='title']/span[@id='productTitle']/text()") 
        product_price = html_etree.xpath("//tr[@id='priceblock_ourprice_row']/td[@class='a-span12']/span[@id='priceblock_ourprice']/text()") 
        # break the while
        if product_price:
            break
        # if fails    
        elif count > 50:
            break
    
    #store data to dictionary and then return
    news_dictionary = {"product": "Failed to get infomation",
                        "price":"$$$"}
    try:
        if product_price[0] == "$8.99": # if price changed
            d_price = {"price": "Price: " + product_price[0]}
        else:
            d_price = {"price": "Price changed to: " + product_price[0]}
        news_dictionary.update(d_price)
        d_product = {"product": product_title[0]}
        news_dictionary.update(d_product)
    except:
        pass

    return news_dictionary

def detect():
    # return product price and name from amazon
    url = "https://www.amazon.com/gp/product/B002EBQX72/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1"
    product_inform = __product(url)
    bs.send(True, 
            "OIL FILTER", 
            "OIL FILTER", 
            "promotion", #channel
            [{
                "title": product_inform.get("product"),
                "url": url,
                "text": product_inform.get("price"),
                "images": [
                    {"url": "https://images-na.ssl-images-amazon.com/images/I/51Pj1mJWleL._AC_SY400_.jpg"}
                ]
            }]
    )
    
def main():
    detect()

if __name__ == "__main__":
    main()

