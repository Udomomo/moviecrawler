# -*- coding: utf-8 -*-
import scrapy
from . import makeBody

from moviecrawler.items import Headline 

class CinemaQualiteSpider(scrapy.Spider):
    name = 'cinemaqualite'
    allowed_domains = ['qualite.musashino-k.jp']
    start_urls = ['http://qualite.musashino-k.jp/movies/']


    def parse(self, response):
        """
        作品案内から個々の作品ページのリンクを抽出してたどる
        """
        for url in response.css(".movies.flex-item a::attr(href)").extract():
            yield scrapy.Request(response.urljoin(url), self.parse_topics)

    def parse_topics(self, response):
        item = Headline()
        title = response.css(".text.is-single-title h1 b::text").extract_first()
        body = response.css("#container>.section .text-container .text b::text").extract()

        item["title"] = makeBody.replacespace(title)
        item["body"] = makeBody.replacespace(makeBody.joinlist(body))
        yield item
