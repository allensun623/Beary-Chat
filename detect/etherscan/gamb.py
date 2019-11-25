

import requests
from lxml import html
import pysnooper

"""get the updated news from gate.io"""

@pysnooper.snoop()
def gate_news():
    url = 'https://etherscan.io/token/0xa0008f510fe9ee696e7e320c9e5cbf61e27791ee#balances'
    page = requests.Session().get(url)
    tree = html.fromstring(page.text)
    result = tree.xpath('//table[@class="table table-md-text-normal table-hover"]//tbody//tr//td//span/text()') #get <div class="entry"> <h3>

    #lines
    count = 0
    for i in result:
        print(i, end ='\n')
        count += 1


def main():
    gate_news()

if __name__ == "__main__":
    main()

