# -*- coding: utf-8 -*-

import requests
from lxml import html, etree
import pysnooper
import bearychat_send as bs
import random

"""get the updated news from gate.io"""

@pysnooper.snoop()
def product():
    #user agent
    url_detail = "https://www.amazon.com/dp/B01NAZGQEA/ref=twister_B00WS2T4ZA?_encoding=UTF8&th=1"  
    user_agents =['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Beamrise/17.2.0.9 Chrome/17.0.939.0 Safari/535.8',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
                'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5',
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322)',
                'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
                'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
                'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11']  
    #random user agent
    i = random.randint(0,8)
    user_agent = user_agents[i]
    HEADERS = {'User-Agent':user_agent,
                'Referer': "www.google.com"}
    count = 0
    #Because of anti-scrapy, running until get the information or up to 50x
    while True:
        count += 1
        response = requests.get(url_detail, headers=HEADERS)
        html_etree = etree.HTML(response.content.decode('utf-8'))
        # get the result of price and title
        product_price = html_etree.xpath("//td[@class='a-span12']/span[@id='priceblock_ourprice']/text()") 
        product_title = html_etree.xpath("//div[@id='titleSection']/h1[@id='title']/span[@id='productTitle']/text()") 

        if product_price:
            break

        # if fails    
        if count > 50:
            product_price = "$$$"
            product_title = "Failed to get infomation"
            break

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
            "promotion", #channel
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

