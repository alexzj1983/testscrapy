import scrapy


from testscrapy.items import GgzyItem

class GgzySpider(scrapy.Spider):
    name = "ggzy"
    allowde_domains = ["deal.ggzy.gov.cn"]
    start_urls = [
        "http://deal.ggzy.gov.cn/ds/deal/dealList.jsp"
    ]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'FINDTXT': '智慧园区'},
            callback=self.parse_p0
        )

    def parse_p0(self,response):
        sel = scrapy.Selector(response)
        sites = sel.xpath('//h4/a')
        items = []
        for site in sites:
            item = GgzyItem()
            item['title'] = site.xpath('text()').extract()
            item['link'] = site.xpath('@href').extract()
            items.append(item)
        return items
