# -*- coding: utf-8 -*-
import scrapy
# from scrapy_splash import SplashRequest
import re
import json

class JobsSpider(scrapy.Spider):
    name = 'hire'
    start_urls = ['https://www.investorgain.com/report/live-ipo-gmp/331/ipo/']
    
    def parse(self, response):
        headers = response.css("th.text-center a::text").getall()

        rows = response.css('tr')

        for row in rows:
            ipo = row.css('td[data-label="IPO"] a::text').get()
            price = row.css('td[data-label="Price"]::text').get()
            gmp = row.css('td[data-label="GMP(₹)"] b::text').get()
            est_listing = row.css('td[data-label="Est Listing"] b::text').get()
            fire_rating = row.css('td[data-label="Fire Rating"] img::attr(alt)').get()
            ipo_size = row.css('td[data-label="IPO Size"]::text').get()
            lot = row.css('td[data-label="Lot"]::text').get()
            open_date = row.css('td[data-label="Open"]::text').get()
            close_date = row.css('td[data-label="Close"]::text').get()
            boa_date = row.css('td[data-label="BoA Dt"]::text').get()
            listing_date = row.css('td[data-label="Listing"]::text').get()
            gmp_updated = row.css('td[data-label="GMP Updated"]::text').get()

            yield {
                'IPO': ipo,
                'Price': price,
                'GMP': gmp,
                'Est Listing': est_listing,
                'Fire Rating': fire_rating,
                'IPO Size': ipo_size,
                'Lot': lot,
                'Open': open_date,
                'Close': close_date,
                'BoA Dt': boa_date,
                'Listing': listing_date,
                'GMP Updated': gmp_updated
            }