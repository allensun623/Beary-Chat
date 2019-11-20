# -*- coding: utf-8 -*-

from detect import amzn_product

def product_info():
    #amazon oil filter 
    data_oil_filter = {
        "url_product": "https://www.amazon.com/gp/product/B002EBQX72/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1",
        "url_img": "https://images-na.ssl-images-amazon.com/images/I/51Pj1mJWleL._AC_SY400_.jpg",
        "message_title": "OIL FILTER",
        "product_title_xpath": "//div[@id='title_feature_div']/div[@id='titleSection']/h1[@id='title']/span[@id='productTitle']/text()",
        "product_price_xpath": "//tr[@id='priceblock_ourprice_row']/td[@class='a-span12']/span[@id='priceblock_ourprice']/text()",
        "current_price": "$8.99"
    }
    amzn_product.detect(data_oil_filter)
    
    #amazon calculator 
    data_calculator = {
        #xpath would change frequently
        "url_product": "https://www.amazon.com/dp/B01NAZGQEA/ref=twister_B00WS2T4ZA?_encoding=UTF8&th=1",
        "url_img": "https://images-na.ssl-images-amazon.com/images/I/71tPl2JkqUL._SY606_.jpg",
        "message_title": "CALCULATOR",
        "product_title_xpath": "//div[@id='title_feature_div']//span[@id='productTitle']/text()",
        "product_price_xpath": "//table[@class='a-lineitem']//td[@class='a-span12']/span[@id='priceblock_ourprice']/text()",
        "current_price": "$139.98"
    }
    amzn_product.detect(data_calculator)

def main():
    product_info()

if __name__ == "__main__":
    main()

