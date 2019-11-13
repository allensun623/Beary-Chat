# -*- coding: utf-8 -*-

import requests
from lxml import html, etree
import pysnooper

"""get the updated news from gate.io"""

@pysnooper.snoop()
def news():
    #user agent
    url_detail = "https://www.amazon.com/dp/B01NAZGQEA/ref=twister_B00WS2T4ZA?_encoding=UTF8&th=1"
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    HEADERS = {'User-Agent':user_agent}
 
    count = 0
    #Because of antiscrapy, run until get the information
    while True:
        count += 1
        #html_page = requests.Session().get(url_detail,headers = HEADERS)
        #tree = html.fromstring(html_page.text)
        response = requests.get(url_detail, headers=HEADERS)
        html_etree = etree.HTML(response.content.decode('utf-8'))
   
        product_price = html_etree.xpath('//span[@class="a-size-medium a-color-price priceBlockBuyingPriceString"]/text()') 
        product_title = html_etree.xpath('//h1[@class="a-size-large a-spacing-none"]/span[@id="productTitle"]/text()') 

        if product_price:
            break

    print("product_title: ", product_title[0].strip())
    print("product_price: ", product_price[0])
    print("Attemps: %d" %count)
        


def main():
    news()

if __name__ == "__main__":
    main()

