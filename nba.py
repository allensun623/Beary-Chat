import requests
from lxml import html
import pysnooper

"""get the updated news from gate.io"""

@pysnooper.snoop()
def news():
    #user agent
    url_detail = "https://www.nba.com/"
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    headers = {'User-Agent':user_agent}
    html_page = requests.Session().get(url_detail,headers = headers)
    tree = html.fromstring(html_page.text)

    product_title = tree.xpath('//div[@class="nba-nav__container nba-nav__container--center"]/ul/li/a/text()') 
    product_score = tree.xpath("//div[@class='dialog-off-canvas-main-canvas']/section[@class='off-canvas-wrap']/div[@class='inner-wrap']/div[@class='headerWrapper']/header[@class='nba-nav-header']/section[@class='nba-nav-wrapper']/nav[@id='block-mainnavigation']/nav[@class='nba-nav nba-primary-nav']/div[@class='nba-nav__container nba-nav__container--center']/ul[@class='nba-nav__container--center-menu']/li[@class='nba-nav__container--center-menu-item'][1]/a/text()") 
    
    print("product_title", product_title)
    print("product_score", product_score)
    #title and price save as dictionary
    #news_dictionary = {product_title[0]: product_price[0]}
    #print(news_dictionary)
    #return news_dictionary


def main():
    news()

if __name__ == "__main__":
    main()

