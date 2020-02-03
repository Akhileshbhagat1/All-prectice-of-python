# -*- coding: utf-8 -*-
import scrapy

from webscrappingPrectice.plant.plant.items import PlantItem


class PlantInfoSpider(scrapy.Spider):
    name = 'plant_info'
    allowed_domains = ['greatplantpicks.org']
    start_urls = ['http://greatplantpicks.org/']

    def parse(self, response):
        for sel in response.xpath('//tbody/tr'):
            item = PlantItem()
            item['name'] = sel.xpath('td[@class="common-name"]/a/text()').extract_first()
            item['genus'] = sel.xpath('td[@class="plantname"]/a/span[@class="genus"]/text()').extract_first()
            item['genus'] = sel.xpath('td[@class="plantname"]/a/span[@class="species"]/text()').extract_first()
            # item['species'] = sel.xpath('td[@class="common-name"]/a/text()').extract_first()
            yield item



