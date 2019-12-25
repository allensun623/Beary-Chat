import scrapy


class QuotesSpider(scrapy.Spider):
    name = "douban"
    start_urls = [
        'https://movie.douban.com/top250',
    ]

    def parse(self, response):
        for movie in response.xpath("//div[@class='item']/div[@class='info']/text()"):
            yield {
                'title': movie.xpath("//div[@class='hd']/a/span[@class='title']/text()").get(),
                'list': movie.xpath("//div[@class='info']/div[@class='bd']/p[1]/text()").get(),
            }

        next_page = response.xpath("//div[@class='paginator']/span[@class='next']/a/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)