# -*- coding: utf-8 -*-

from detect.amazon import amzn_product
import json

def product_info():

    with open('in/amzn.json') as json_file:
        data = json.load(json_file)
    for product in data.values():
        amzn_product.detect(product)

def main():
    product_info()

if __name__ == "__main__":
    main()

