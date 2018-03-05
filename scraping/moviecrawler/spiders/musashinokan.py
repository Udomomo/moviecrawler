# -*- coding: utf-8 -*-
import scrapy
from . import makeBody

from moviecrawler.items import Headline 

class MusashinokanSpider(scrapy.Spider):
    name = 'musashinokan'
    allowed_domains = ['shinjuku.musashino-k.jp']
    start_urls = ['http://shinjuku.musashino-k.jp/movies/']


    def parse(self, response):
        """
        作品案内から個々の作品ページのリンクを抽出してたどる
        """
        for url in response.css(".movies.flex-item a::attr(href)").extract():
            yield scrapy.Request(response.urljoin(url), self.parse_topics)

    def parse_topics(self, response):
        item=Headline()
        title = response.css(".movies-title b::text").extract_first()
        body = response.css(".main.is-site-main .text-container .text b::text").extract()

        item["title"] = makeBody.replacespace(title)
        item["body"] = makeBody.replacespace(makeBody.joinlist(body))
        yield item
