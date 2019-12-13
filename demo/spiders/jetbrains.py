from scrapy import Spider
from scrapy_splash import SplashRequest

from demo.items import JetbrainsItem


class JetbrainsSpider(Spider):

    name = 'jetbrainsSpider'
    home_url = 'https://www.jetbrains.com/help/pycharm'
    start_urls = [home_url + '/quick-start-guide.html']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, args={"wait": 3})

    def parse(self, response):
        j_items = []
        j_item = JetbrainsItem()
        for doc in response.xpath('/html/body/div[1]/div/div/nav/div/div/ul/li'):
            print(doc)
            is_exist = doc.css('svg').extract_first(default='not-found')
            if is_exist == 'not-found':
                j_item["linkText"] = doc.xpath('.//a[@data-test="toc-item"]/text()').extract()[0]
                j_item["linkUrl"] = doc.xpath('.//a[@data-test="toc-item"]/@href').extract()[0]
                j_item["isExpandable"] = "no"
                yield j_item
            else:
                j_item["linkText"] = doc.xpath('.//a[@data-test="toc-item"]/text()').extract()[0]
                j_item["linkUrl"] = doc.xpath('.//a[@data-test="toc-item"]/@href').extract()[0]
                j_item["isExpandable"] = "yes"
                yield j_item
                yield SplashRequest(url=self.home_url + '/' + j_item["linkUrl"], callback=self.parse, args={"wait": 3})
                # yield response.follow(self.home_url + '/' + j_item["linkUrl"], self.parse)

        # print(j_items)

    def getJetBrainsItem(str):
        item = str