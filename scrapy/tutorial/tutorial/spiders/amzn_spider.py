import scrapy


class QuotesSpider(scrapy.Spider):
    name = "amzn"
    start_urls = [
        'https://www.amazon.com/dp/B07FK8SQDQ/ref=twister_B00WS2T4ZA?_encoding=UTF8&th=1',
    ]

    def parse(self, response):
        yield {
            'title': response.xpath("div[@id='title_feature_div']/div[@id='titleSection']/h1[@id='title']/span[@id='productTitle']/text()").get(),
            'price': response.xpath("td[@class='a-span12']/span[@id='priceblock_ourprice']/text()").get(),
        }