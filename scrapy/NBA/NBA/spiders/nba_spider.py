import scrapy


class QuotesSpider(scrapy.Spider):
    name = "nba"

    def start_requests(self):
        urls = [
            'https://twitter.com/search?q=nba&src=typed_query',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'nba.html' 
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)