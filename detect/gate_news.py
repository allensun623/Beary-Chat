import requests
from lxml import html
import bearychat_send as bs
import pysnooper

"""get the updated news from gate.io"""

def news():
    url = 'https://www.gate.io/articlelist/ann'
    page = requests.Session().get(url)
    tree = html.fromstring(page.text)
    result = tree.xpath('//div[@class="entry"]//h3/text()') #get <div class="entry"> <h3>
    urls = tree.xpath('//div[@class="entry"]/a/@href') # get related hyper link

    #news and urls save as dictionary
    count = 0
    news_dictionary = {"news": "urls"}
    for i, j in zip(result, urls):
        d = {i: "https://www.gate.io"+j}
        news_dictionary.update(d)
        count += 1
        if count > 4: # print the lates five news
            break
    
    return news_dictionary

def detect():
    # receive the latest news
    news_inform = news()
    bs.send(True, 
            "GATE NEWS", 
            "GATE NEWS", 
            "cc", #channel
            [{
                "title": list(news_inform.keys())[1],
                "url": list(news_inform.keys())[1],
                "text": list(news_inform.values())[1],
                "images": [
                    {"url": "https://cosmos-images2.imgix.net/file/spina/photo/20565/191010_nature.jpg?ixlib=rails-2.1.4&auto=format&ch=Width%2CDPR&fit=max&w=1600"}
                ]
            }]
    )

def main():
    detect()

if __name__ == "__main__":
    main()

