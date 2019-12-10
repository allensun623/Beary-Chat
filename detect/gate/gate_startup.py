import requests
from lxml import html
import bearychat_send as bs
import pysnooper

"""get the updated news from gate.io"""

@pysnooper.snoop()
def __startup():
    url = 'https://www.gate.io/startup'
    page = requests.Session().get(url)
    tree = html.fromstring(page.text)
    startup_project = tree.xpath('//a[@class="su-item-title"]/h3/text()') #get startup project
    startup_tpye = tree.xpath("//div[@class='ti-status status-txt']/text()")
    time_tpye = tree.xpath("//div[@class='item-state']/text()")
    timer = tree.xpath('//div[@class="item-state"]/span[@class="timer-box"]/text()')
    amount = tree.xpath('//div[@class="item-box zt2"]/ul[@class="su-dtl"]/li/b[@class="item-total"]/text()')
    url_img = tree.xpath('//a[@class="img-con"]/img[@class="item-img"]/@src') # get related hyper link

    #news and urls save as dictionary
    news_dictionary = {
        "url_project": url,
        "startup_project": startup_tpye[0]+ ": " + startup_project[0],
        "amount": "目标: " + amount[0].replace(' ', ''), #no space
        "timer": time_tpye[0].replace('\r', '').replace('\n', '').replace(' ', '') + " " + timer[0],
        "url_img": url_img[0] 
        }
    
    return news_dictionary

def detect():
    # receive the latest news
    news_info = __startup()
    bs.send(True, 
            "GATE STARTUP", 
            "GATE STARTUP", 
            "cc", #channel
            [{
                "title": news_info.get("startup_project"),
                "url": news_info.get("url_project"),
                "text": news_info.get("amount") + "\n" + news_info.get("timer"),
                "images": [
                    {"url": news_info.get("url_img")}
                ]
            }]
    )

def main():
    detect()

if __name__ == "__main__":
    main()

