# -*- coding: utf-8 -*-
import scrapy

from moviecrawler.items import Headline 

class KsCinemaSpider(scrapy.Spider):
    name = 'kscinema'
    allowed_domains = ['www.ks-cinema.com']
    start_urls = ['http://www.ks-cinema.com/movie/']


    def parse(self, response):
        """
        作品案内から個々の作品ページのリンクを抽出してたどる
        """
        for url in response.css(".arch-moviebox a::attr(href)").extract():
            yield scrapy.Request(response.urljoin(url), self.parse_topics)

    def parse_topics(self, response):
        item=Headline()
        item["title"] = response.css("h1::text").extract()
        item["body"] = response.css("#txt-area p::text").extract()
        yield item        

        
