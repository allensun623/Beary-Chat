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
    startup_project = tree.xpath('//a[@class="su-item-title"]/h3/text()')[0] #get startup project
    startup_tpye = tree.xpath("//div[@class='ti-status status-txt']/text()")[0]
    time_tpye = tree.xpath("//div[@class='item-state']/text()")[0]
    timer = tree.xpath('//div[@class="item-state"]/span[@class="timer-box"]/text()')[0]    
    amount_type = tree.xpath('//ul[@class="su-dtl"]/li/text()')[0]
    amount = tree.xpath("//ul[@class='su-dtl']/li/b[@class='item-total']/strong/text()")[0] + \
            tree.xpath("//ul[@class='su-dtl']/li/b[@class='item-total']/text()")[0]
    url_img = tree.xpath('//a[@class="img-con"]/img[@class="item-img"]/@src')[0] # get related hyper link

    #news and urls save as dictionary
    news_dictionary = {
        "url_project": url,
        "startup_project": startup_tpye+ ": " + startup_project,
        "amount": amount_type + ": $" + amount.replace(' ', ''), #no space
        "timer": time_tpye.replace('\r', '') \
                        .replace('\n', '') \
                        .replace(' ', '') + \
                        " " + \
                        timer,
        "url_img": url_img 
        }
    
    return news_dictionary

def detect():
    # receive the latest news
    try:
        news_info = __startup()
    except:
        news_info = {
            "startup_project": "NONE",
            "url_project": "NONE",
            "amount": "NONE",
            "url_img": "https://www.gate.io/images/startup/pendding.png"
        }
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

