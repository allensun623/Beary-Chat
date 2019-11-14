import requests
from lxml import html
import pysnooper

"""get the updated price from a product"""

@pysnooper.snoop()
def skinstore_product():
    url = 'https://www.skinstore.com/erno-laszlo-hydra-therapy-skin-vitality-mask-4-x-37ml/10941238.html?autocomplete=productsuggestion'
    page = requests.Session().get(url)
    tree = html.fromstring(page.text)
    product_name = tree.xpath('//div[@class="productName"]//h1/text()') #get <div class="entry"> <h3>
    product_price= tree.xpath('//span[@class="productPrice_priceInfo"]//p/text()') #get <div class="entry"> <h3>

    #lines
    count = 0
    for i in product_name:
        print(i, end ='\n')
        count += 1    

    count = 0
    for i in product_price:
        print(i, end ='\n')
        count += 1

def main():
    skinstore_product()

if __name__ == "__main__":
    main()

