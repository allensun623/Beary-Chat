# -*- coding: utf-8 -*-

import requests
from lxml import html, etree
import pysnooper
import bearychat_send as bs

"""get the updated news from gate.io"""

@pysnooper.snoop()
def product():
    #user agent
    url_detail = "https://www.amazon.com/dp/B01NAZGQEA/ref=twister_B00WS2T4ZA?_encoding=UTF8&th=1"
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    HEADERS = {'User-Agent':user_agent}
 
    count = 0
    #Because of anti-scrapy, run until get the information
    while True:
        count += 1
        response = requests.get(url_detail, headers=HEADERS)
        html_etree = etree.HTML(response.content.decode('utf-8'))
   
        product_price = html_etree.xpath('//span[@class="a-size-medium a-color-price priceBlockBuyingPriceString"]/text()') 
        product_title = html_etree.xpath('//h1[@class="a-size-large a-spacing-none"]/span[@id="productTitle"]/text()') 
        #product_img = html_etree.xpath('//div[@id="imgTagWrapperId"]/img[@id="landingImage"]/@src') 

        if product_price:
            break

    #print("product_title: ", product_title[0].strip())
    #print("product_price: ", product_price[0])
    #print("Attemps: %d" %count)
    news_dictionary = {"product": "price"}
    if product_price[0] == "$139.98": # if price changed
        d = {product_title[0].strip(): "Price: " + product_price[0]}
    else:
        d = {product_title[0].strip(): "Price changed to: " + product_price[0]}
    news_dictionary.update(d)
    return news_dictionary

def detect():
    # return product price from amazon
    product_inform = product()
    bs.send(True, 
            "Calculator", 
            "Calculator", 
            "promotion",
            [{
                "title": list(product_inform.keys())[1],
                "url": "https://www.amazon.com/dp/B01NAZGQEA/ref=twister_B00WS2T4ZA?_encoding=UTF8&th=1",
                "text": list(product_inform.values())[1],
                "images": [
                    {"url": "https://images-na.ssl-images-amazon.com/images/I/71tPl2JkqUL._SY606_.jpg"}
                ]
            }]
    )
def main():
    detect()

if __name__ == "__main__":
    main()

