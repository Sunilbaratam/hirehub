import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from scrapy.selector import Selector
from time import sleep

class HireSpider(scrapy.Spider):
    name = 'hire'
    start_urls = {
        'https://jobs.careers.microsoft.com/global/en/search?lc=India&l=en_us&pg=1&pgSz=20&o=Relevance&flt=true&ulcs=true&cc=India&ref=cms'
    }

    def __init__(self, *args, **kwargs):
        super(HireSpider, self).__init__(*args, **kwargs)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def parse(self, response):

        self.driver.get(response.url)
        sleep(3)
        company = response.css("title::text").extract_first().split(' ')
        company = company[3]
        role = response.css('div::text').extract()
        roles = response.css("h2.MZGzlrn8gfgSs8TZHhv2::text").extract()
        print(roles)
        print(role)

    def closed(self, reason):
        self.driver.quit()