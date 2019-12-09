# -*- coding: utf-8 -*-

from detect.amazon import amzn_product


def product_info():
  
    #amazon calculator 
    data_calculator = {
        #xpath would change frequently
        "url_product": "https://www.amazon.com/dp/B07FK8SQDQ/ref=twister_B00WS2T4ZA?_encoding=UTF8&th=1",
        "url_img": "https://images-na.ssl-images-amazon.com/images/I/51JN-fLvUiL.jpg",
        "message_title": "CALCULATOR",
        "product_title_xpath": "//div[@id='title_feature_div']/div[@id='titleSection']/h1[@id='title']/span[@id='productTitle']/text()",
        "product_price_xpath": "//tr[@id='priceblock_ourprice_row']/td[@class='a-span12']/span[@id='priceblock_ourprice']/text()",
        "current_price": "$118.98",
        "target_price": "109.2" # target price to purchase the item
    }
    amzn_product.detect(data_calculator)
    #amazon oil filter 
    data_oil_filter = {
        "url_product": "https://www.amazon.com/gp/product/B002EBQX72/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1",
        "url_img": "https://images-na.ssl-images-amazon.com/images/I/51Pj1mJWleL._AC_SY400_.jpg",
        "message_title": "OIL FILTER",
        "product_title_xpath": "//div[@id='title_feature_div']/div[@id='titleSection']/h1[@id='title']/span[@id='productTitle']/text()",
        "product_price_xpath": "//tr[@id='priceblock_ourprice_row']/td[@class='a-span12']/span[@id='priceblock_ourprice']/text()",
        "current_price": "$8.99",
        "target_price": "5.2"

    }
    amzn_product.detect(data_oil_filter)
    #amazon coffee
    data_coffee = {
        "url_product": "https://www.amazon.com/gp/product/B00OVBGFZI/ref=ox_sc_act_title_2?smid=ACK6XR0AS3JM0&psc=1",
        "url_img": "https://images-na.ssl-images-amazon.com/images/I/71gHseSfYsL._SX522_.jpg",
        "message_title": "The Real Deal Enema Coffee",
        "product_title_xpath": "//div[@id='title_feature_div']/div[@id='titleSection']/h1[@id='title']/span[@id='productTitle']/text()",
        "product_price_xpath": "//tr[@id='priceblock_saleprice_row']/td[@class='a-span12']/span[@id='priceblock_saleprice']/text()",
        "current_price": "$29.97",
        "target_price": "27.2"

    }
    amzn_product.detect(data_coffee)    
  
def main():
    product_info()

if __name__ == "__main__":
    main()

