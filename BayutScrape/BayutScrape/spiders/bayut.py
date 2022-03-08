# -*- coding: utf-8 -*-
import scrapy


class BayutSpider(scrapy.Spider):
    name = 'bayut'
    page_no = 2
    allowed_domains = ['www.bayut.com']
    start_urls = ['http://books.toscrape.com/']
    base_url = 'http://books.toscrape.com/'

    def parse(self, response):
        items = BayutScrapeItem()

        property_id = response.css('._2663f958+ ._327a3afc').css('::text').extract()
        purpose = response.css('li:nth-child(2) ._812aa185').css('::text').extract()
        type_p = response.css('li:nth-child(1) ._812aa185').css('::text').extract()
        added_on = response.css('li:nth-child(6) ._812aa185').css('::text').extract()
        furnishing = response.css('li:nth-child(4) ._812aa185').css('::text').extract()
        price = response.css('.c4fc20ba').css('::text').extract()
        location = response.css('._1f0f1758').css('::text').extract()
        bed_bath_size = response.css('.fc2d1086 , .fc2d1086 span').css('::text').extract()
        permit_number = response.css('.ff863316~ .ff863316+ .ff863316').css('::text').extract()
        agent_name = response.css('._55e4cba0').css('::text').extract()
        image_url = response.css('._6681ac2b::attr(src)')
        breadcrumbs = response.css('.fontCompensation').css('::text').extract()
        amenities = response.css('.fontCompensation+ ._96aa05ec').css('::text').extract()
        description = response.css('._2a806e1e').css('::text').extract()

        items['property_id'] = property_id
        items['purpose'] = purpose
        items['type_p'] = type_p
        items['added_on'] = added_on
        items['furnishing'] = furnishing
        items['price'] = price
        items['location'] = location
        items['bed_bath_size'] = bed_bath_size
        items['permit_number'] = permit_number
        items['agent_name'] = agent_name
        items['image_url'] = image_url
        items['breadcrumbs'] = breadcrumbs
        items['amenities '] = amenities
        items['description '] = description

        yield items




