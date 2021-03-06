# -*- coding: utf-8 -*-
import scrapy

class Chaquente (scrapy.Spider):
    name = "chaquente"
    allowed_domains = ["http://chaquente.com"]
    start_urls = (
        "http://www.http://chaquente.com/",
    )
    rules = [Rule(LinkExtractor(allow=["/tor/\d+"]), "parse_torrent")]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, "wb") as f:
            f.write(response.body)
