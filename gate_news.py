import requests
from lxml import html
import pysnooper

"""get the updated news from gate.io"""
@pysnooper.snoop()
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


def main():
    news()

if __name__ == "__main__":
    main()

