import requests
from lxml import html
import pysnooper

"""get the updated news from gate.io"""

@pysnooper.snoop()
def news():
    #定义常量
    url_detail = "https://www.amazon.com/dp/B01NAZGQEA/ref=twister_B00WS2T4ZA?_encoding=UTF8&th=1"
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    headers = {'User-Agent':user_agent}
    html_page = requests.Session().get(url_detail,headers = headers)


    url = 'https://www.amazon.com/dp/B01NAZGQEA/ref=twister_B00WS2T4ZA?_encoding=UTF8&th=1'
    page = requests.Session().get(url)
    tree = html.fromstring(html_page.text)
    tree1 = html.fromstring(page.text)
    product_title = tree.xpath('//h1[@class="a-size-large a-spacing-none"]//span/text()') 
    product_price = tree.xpath('//span[@class="a-size-medium a-color-price priceBlockBuyingPriceString"]/text()') 
    product_price_ori = tree.xpath('//span[@class="priceBlockStrikePriceString a-text-strike"]/text()') 
    product_deliver = tree.xpath('//div[@id="delivery-message"]/text()') 
    print("product_title", product_title)
    print("product_price", product_price)
    print("product_price_ori", product_price_ori)
    print("product_deliver", product_deliver)
    #title and price save as dictionary
    #news_dictionary = {product_title[0]: product_price[0]}
    #print(news_dictionary)
    #return news_dictionary


def main():
    news()

if __name__ == "__main__":
    main()

