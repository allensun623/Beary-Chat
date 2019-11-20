import requests
from lxml import html
import bearychat_send as bs
import pysnooper

"""get the updated news from gate.io"""

def __news():
    url = 'https://www.gate.io/articlelist/ann'
    page = requests.Session().get(url)
    tree = html.fromstring(page.text)
    result = tree.xpath('//div[@class="entry"]//h3/text()') #get <div class="entry"> <h3>
    urls = tree.xpath('//div[@class="entry"]/a/@href') # get related hyper link

    #news and urls save as dictionary
    news_dictionary = {
        "news": result[0],
        "urls": "https://www.gate.io/" + urls[0]
        }
    
    return news_dictionary

def detect():
    # receive the latest news
    news_info = __news()
    bs.send(True, 
            "GATE NEWS", 
            "GATE NEWS", 
            "cc", #channel
            [{
                "title": news_info.get("news"),
                "url": news_info.get("urls"),
                #"text": news_info.get("urls"),
                "images": [
                    {"url": "https://cosmos-images2.imgix.net/file/spina/photo/20565/191010_nature.jpg?ixlib=rails-2.1.4&auto=format&ch=Width%2CDPR&fit=max&w=1600"}
                ]
            }]
    )

def main():
    detect()

if __name__ == "__main__":
    main()

