# -*- coding: utf-8 -*-

import sweater_product

"""monitor the sweaters data"""
def product_info():
  
    #Sweater #1 : Alpaca Blend Mock Neck
    data_sweater_arket = {
        #xpath would change frequently
        "url_product": "https://www.arket.com/en/women/knitwear/product.alpaca-blend-mock-neck-grey.0778990002.html?utm_source=rewardStyle&utm_medium=affiliate&utm_campaign=1&utm_content=15&utm_term=597824&ranMID=43161&ranEAID=QFGLnEolOWg&ranSiteID=QFGLnEolOWg-XrqLWQiADtZx4hQSaKd0Rw",
        "url_img": "https://lp.arket.com/app006prod?set=key%5Bresolve.pixelRatio%5D,value%5B2%5D&set=key%5Bresolve.width%5D,value%5B800%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&set=key%5Bresolve.quality%5D,value%5B70%5D&set=ImageVersion%5B201910031725%5D,source%5B01_0778990_002_5%5D,type%5BECOMLOOK%5D&call=url%5Bfile:/product/dynamic.chain%5D",
        "message_title": "SWEATER",
        "product_title_xpath": "//div[@class='o-product-details-selection']/div[@class='product-name-price-wrapper']/h1[@class='a-heading-3']/span[@id='productTitle']/text()",
        "product_price_xpath": "//div[@class='o-product-details-selection']/div[@class='product-name-price-wrapper']/div[@id='product-price']/span[@id='productPrice']/text()",
        "product_size_xpath": "//div[@class='o-product-details-selection']/div[@id='sizesDropdown']/div[@class='m-dropdown is-filled']/button[@id='labelSize']/text()",
        "current_price": "$129"
    }
    sweater_product.detect(data_sweater_arket)
    
    #SWEATER #2.  WOOL BUTTON SLEEVE SWEATER 
    data_sweater_pixie = {
        "url_product": "https://www.pixiemarket.com/collections/sweaters-knits/products/wool-button-sleeve-sweater?variant=30775899226217&cjevent=69757b65107b11ea826f00f20a24060f",
        "url_img": "https://cdn.shopify.com/s/files/1/2037/5461/products/2019-10-10-Pixie-Market-0436.jpg?v=1571610425", 
        "message_title": "SWEATER",
        "product_title_xpath": "//div[@class='product-name']/span[@class='h1']/text()",
        "product_price_xpath": "//div[@class='price-info']/div[@class='price-box']/span[@class='regular-price']/span[@class='price']/span[@class='money']/text()",
        "product_size_xpath": "//dl[@class='product-detail product-accordian']/dd/p[2]/text()",
        "current_price": "$99.00"
    }
    sweater_product.detect(data_sweater_pixie)    
     
    #SWEATER #3 CONTRAST-KNIT SWEATER 
    data_sweater_petite = {
        "url_product": "https://www.cosstores.com/en_usd/women/womenswear/knitwear/jumpers/product.contrast-knit-sweater-blue.0781637001.html",
        "url_img": "http://http://lp.cosstores.com/app001prod?set=source[01_0781637_001_4],type[ECOMLOOK],device[hdpi],quality[80],ImageVersion[201909101505]&call=url[file:/product/main]&zoom=zoom", 
        "message_title": "SWEATER",
        "product_title_xpath": "//div[@class='o-product-information i18n']/form[@class='o-form add-to-bag']/div[@class='title']/p[@id='productTitle']/text()",
        "product_price_xpath": "//div[@class='o-product-information i18n']/form[@class='o-form add-to-bag']/div[@id='product-price']/div[@class='price parbase']/span[@id='productPrice']/text()",
        "product_size_xpath": "//div[@class='product-description']/div[@id='description']/p[11]/text()",
        "current_price": "$115"
    }
    sweater_product.detect(data_sweater_petite)

    
    #SWEATER #4 averie cashmere blend sweater - blush 
    data_sweater_petite = {
        #peice occurs when selecting size 
        "url_product": "https://petitestudionyc.com/collections/tops/products/averie-sweater-blush?rfsn=924456.2cb4d&utm_source=refersion&utm_medium=affiliate&utm_campaign=924456.2cb4d&variant=30340785045584",
        "url_img": "https://cdn.shopify.com/s/files/1/1094/6908/products/7.jpg?v=1571157084", 
        "message_title": "SWEATER",
        "product_title_xpath": "//div[@id='product-description']/h5[@class='colored-text product-title translation-pending']/text()",
        "product_price_xpath": "//div[@id='PageContainer']/div[@class='page-wrap']/div[@id='content']/div[@id='shopify-section-product-template']/div[@id='product-4178861293648']/div[@id='product-right']/div[@id='product-description']/div[1]/p[@id='product-price']/span[@class='product-price colored-text onsale']/span/span[@class='money']/text()",
        "product_size_xpath": "//div[@id='size']/button[@id='size_0781637001003']/attribute::*",
        "current_price": "$229.00"
    }
    sweater_product.detect(data_sweater_petite)
  
def main():
    product_info()

if __name__ == "__main__":
    main()

