# -*- coding: utf-8 -*-

from detect.amazon import amzn_product
import json

def product_info():
    data_amzn = {
        #xpath would change frequently
        "url_product": "",
        "url_img": "",
        "message_title": "",
        "product_title_xpath": "",
        "product_price_xpath": "",
        "current_price": "",
        "target_price": "" # target price to purchase the item
    }
    with open('in/amzn.json') as json_file:
        data = json.load(json_file)
    for product in data.values():
        data_amzn["url_product"] = product["url_product"]
        data_amzn["url_img"] = product["url_img"]
        data_amzn["message_title"] = product["message_title"]
        data_amzn["product_title_xpath"] = product["product_title_xpath"]
        data_amzn["product_price_xpath"] = product["product_price_xpath"]
        data_amzn["current_price"] = product["current_price"]
        data_amzn["target_price"] = product["target_price"]
        amzn_product.detect(data_amzn)

def main():
    product_info()

if __name__ == "__main__":
    main()

