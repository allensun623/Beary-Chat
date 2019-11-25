# -*- coding: utf-8 -*-

import plg

def token_info():
  
    #pleadgecamp(PLG) 
    data_plg = {
        #xpath would change frequently
        "url_token": "https://etherscan.io/token/0x85ca6710D0F1D511d130f6935eDDA88ACBD921bD#balances",
        "url_img": "https://images-na.ssl-images-amazon.com/images/I/71tPl2JkqUL._SY606_.jpg",
        "message_title": "PLG",
        "token_head_address_xpath": "//table[@class='table table-md-text-normal table-hover']/thead[@class='thead-light']/tr[1]/td[1]/text()",
        "token_title_xpath": "//table[@class='table table-md-text-normal table-hover']/tbody/tr/td/span/text()",
    }
    plg.detect(data_plg)
    #amazon oil filter 
    """
    data_oil_filter = {
        "url_token": "https://www.amazon.com/gp/token/B002EBQX72/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1",
        "url_img": "https://images-na.ssl-images-amazon.com/images/I/51Pj1mJWleL._AC_SY400_.jpg",
        "message_title": "OIL FILTER",
        "token_title_xpath": "//div[@id='title_feature_div']/div[@id='titleSection']/h1[@id='title']/span[@id='tokenTitle']/text()",
        "token_price_xpath": "//tr[@id='priceblock_ourprice_row']/td[@class='a-span12']/span[@id='priceblock_ourprice']/text()",
        "current_price": "$8.99"
    }
    amzn_token.detect(data_oil_filter)
    """

def main():
    token_info()

if __name__ == "__main__":
    main()

