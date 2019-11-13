import requests
from lxml import html
import pysnooper

"""get the updated news from gate.io"""

@pysnooper.snoop()
def news():
    url = 'https://www.amazon.com/BOVKE-Calculator-Instruments-Shockproof-Protective/dp/B01HIPOCYE/ref=pd_bxgy_229_img_2/145-1698164-3586833?_encoding=UTF8&pd_rd_i=B01HIPOCYE&pd_rd_r=f8be2a89-5265-4694-bbf5-855487ca2b05&pd_rd_w=8hH6r&pd_rd_wg=skIz6&pf_rd_p=09627863-9889-4290-b90a-5e9f86682449&pf_rd_r=Q4TTQH96DJ35M9H8T9T3&psc=1&refRID=Q4TTQH96DJ35M9H8T9T3'
    page = requests.Session().get(url)
    tree = html.fromstring(page.text)
    product_title = tree.xpath('//h1[@class="a-size-large a-spacing-none"]//span[@class="a-size-large"]/text()') 
    product_price = tree.xpath('//span[@class="a-size-medium a-color-price priceBlockBuyingPriceString"]/text()') 
    product_price_ori = tree.xpath('//span[@class="priceBlockStrikePriceString a-text-strike"]/text()') 
    product_deliver = tree.xpath('//div[@id="delivery-message"]/text()') 
    print("product_title", product_title)
    print("product_price", product_price)
    print("product_deliver", product_deliver)
    #title and price save as dictionary
    #news_dictionary = {product_title[0]: product_price[0]}
    #print(news_dictionary)
    #return news_dictionary


def main():
    news()

if __name__ == "__main__":
    main()

