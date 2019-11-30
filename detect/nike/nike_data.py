# -*- coding: utf-8 -*-

#from detect.nike import nike_product
import nike_product

"""monitor the nike data"""
def product_info():
  
    #nike #1 : Nike React Element 55
    data_nike_air_vapormax = {
        #xpath would change frequently
        "url_product": "https://www.nike.com/t/react-element-55-mens-shoe-hRRzF8/BQ6166-008",
        "url_img": "https://c.static-nike.com/a/images/t_PDP_1280_v1/f_auto/cwblyah42iinky00xmyg/react-element-55-mens-shoe-hRRzF8.jpg",
        "message_title": "NIKE",
        "product_title_xpath": "//div[@class='pr12-sm css-w58mfg']/h1[@id='pdp_product_title']/text()",
        "product_price_xpath": "//div[@class='headline-baseline-base ta-sm-r css-1122yjz']/div/div[@class='css-i260wg']/text()",
        "product_size_xpath": "//fieldset[@class='mt5-sm mb3-sm body-baseline-base css-ifl20d']/div[@class='mt2-sm css-vf0kzn']/label[@class='css-1hgfp39'][8]/text()",
        "current_price": "$115.97"
    }
    nike_product.detect(data_nike_air_vapormax)
    
    
  
def main():
    product_info()

if __name__ == "__main__":
    main()

