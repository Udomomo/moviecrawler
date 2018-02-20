# -*- coding: utf-8 -*-
import scrapy

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
        item=Headline()
        item["title"] = response.css(".text.is-single-title h1 b::text").extract()
        item["body"] = response.css("#container>.section .text-container .text p::text").extract()
        yield item        

        
