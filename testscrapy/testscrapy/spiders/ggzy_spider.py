from scrapy.spider import Spider
from scrapy.selector import Selector
from testscrapy.items import GgzyItem

class GgzySpider(Spider):
    name = "ggzy"
    allowde_domains = ["deal.ggzy.gov.cn"]
    start_urls = [
        "http://deal.ggzy.gov.cn/ds/deal/dealList.jsp"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//h4/a')
        items = []
        for site in sites:
            item = GgzyItem()
            item['title'] = site.xpath('text()').extract()
            item['link'] = site.xpath('@href').extract()
            items.append(item)
        return items