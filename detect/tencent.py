## 获取职位详情页URL
import requests
from lxml import etree

# 设置请求头
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

# 设置域名
BASE_DOMAIN = 'https://hr.tencent.com/'

# 定义获取详情页URL函数
def get_detail_page(url):
    response = requests.get(url, headers=HEADERS)
    html = etree.HTML(response.content.decode('utf-8'))
    urls = html.xpath('//table[@class="tablelist"]//tr[@class="even" or @class="odd"]//a/@href')
    detail_page = list(map(lambda url: BASE_DOMAIN + url, urls))
    return detail_page