# -*- coding: utf-8 -*-
import scrapy

from moviecrawler.items import Headline

class CinemaQualiteSpider(scrapy.Spider):
    name = 'cinemaqualite'

    def start_requests(self):
        start_urls = [
            'http://qualite.musashino-k.jp/movies/',
            'http://shinjuku.musashino-k.jp/movies/',
            'http://www.imageforum.co.jp/theatre/movies/',
            'http://www.ks-cinema.com/movie/'
        ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pass
