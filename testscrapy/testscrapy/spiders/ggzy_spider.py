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
            callback=self.parse_fd
        )

    def parse_fd(self,response):
        for href in response.css('.publicont h4 a::attr(href)'):
            url = href.extract()
            yield scrapy.Request(url,callback=self.parse_url)

    def parse_url(self,response):
        yield {
            'title':response.css('h4.h4_o').extract()[0]
        }
