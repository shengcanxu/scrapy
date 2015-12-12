import scrapy
from projects.woshipm.woshipm.items import WoshipmItem

class WoshipmSpider(scrapy.Spider):
    name = "woshipm"
    allowed_domains = ["woshipm.com"]
    start_urls = [
        "http://www.woshipm.com/",
    ]

    def parse(self, response):
        for href in response.xpath('//*[@id="home-list"]//dl/dd//h3/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parseContents)

    def parseContents(self, response):
        for sel in response.xpath('//ul/li'):
            item = WoshipmItem()
            item['title'] = sel.xpath('//h3[@class="list-h3"]/a/text()').extract()
            item['updateTime'] = sel.xpath('//div[@class="down-box"]/li[@class="time"]/text()').extract()
            item['reads'] = sel.xpath('//div[@class="down-box"]/li[@class="read"]/text()').extract()
            yield item