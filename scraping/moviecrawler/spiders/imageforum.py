# -*- coding: utf-8 -*-
import scrapy
from . import makeBody

from moviecrawler.items import Headline 

class ImageforumSpider(scrapy.Spider):
    name = 'imageforum'
    allowed_domains = ['www.imageforum.co.jp']
    start_urls = ['http://www.imageforum.co.jp/theatre/movies/']


    def parse(self, response):
        """
        作品案内から個々の作品ページのリンクを抽出してたどる
        """
        for url in response.css(".movies a::attr(href)").extract():
            yield scrapy.Request(response.urljoin(url), self.parse_topics)

    def parse_topics(self, response):
        item=Headline()
        title = response.css(".schedule-day-title.schedule-day-title3::text").extract_first()
        body = response.css(".text.mbL strong::text").extract()

        item["title"] = makeBody.replacespace(title)
        item["body"] = makeBody.replacespace(makeBody.joinlist(body))
        yield item
