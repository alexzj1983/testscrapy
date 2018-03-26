import scrapy


from testscrapy.items import GgzyItem

class GgzySpider(scrapy.Spider):
    name = "ggzy"
    allowde_domains = ["deal.ggzy.gov.cn"]
    start_urls = [
        "http://deal.ggzy.gov.cn/ds/deal/dealList.jsp"
    ]

    def parse(self, response):
        for page in range(1,4):
            yield scrapy.FormRequest.from_response(
                response,
                formdata={
                    'FINDTXT': '智慧园区',
                    'TIMEBEGIN_SHOW':'2017-12-20',
                    'TIMEEND_SHOW':'2018-03-26',
                    'TIMEBEGIN':'2017-12-20',
                    'TIMEEND':'2018-03-26',
                    'DEAL_TIME':'05',
                    'DEAL_CLASSIFY':'00',
                    'DEAL_STAGE':'0000',
                    'DEAL_PROVINCE':'0',
                    'DEAL_CITY':'0',
                    'DEAL_PLATFORM':'0',
                    'DEAL_TRADE':'0',
                    'isShowAll':'0',
                    'PAGENUMBER':str(page)
                },
                callback=self.parse_fd
            )

    def parse_fd(self,response):
        for href in response.css('.publicont h4 a::attr(href)'):
            url = href.extract()
            yield scrapy.Request(url,callback=self.parse_url)

    def parse_url(self,response):
        yield {
            'title':response.css('h4.h4_o::text').extract()[0],
            'biddate':response.css()
        }
