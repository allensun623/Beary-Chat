# -*- coding: utf-8 -*-

import pysnooper
import lxml.html
import requests

@pysnooper.snoop()
def amazon_price(url, user_agent):
    kv = {'user-agent': user_agent}
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    tree = lxml.html.fromstring(r.text.encode("utf-8"))
    price = tree.cssselect("span#priceblock_dealprice")
    
    print(price)

if __name__=="__main__":
    url = "https://www.amazon.com/dp/B01NAZGQEA/ref=twister_B00WS2T4ZA?_encoding=UTF8&th=1"
    user_agent = 'Mozilla/5.0'
    amazon_price(url, user_agent)
    exit(200)