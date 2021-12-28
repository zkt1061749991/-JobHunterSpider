import scrapy

from JobHunterSpider.items import WuyouItem


class WuyouspiderSpider(scrapy.Spider):
    name = 'WuYouSpider'
    allowed_domains = ['51job.com']
    start_urls = ["https://search.51job.com/list/000000,000000,0000,00,9,99,+,2,1.html"]

    def parse(self, response):
        print(response.text)
        selectors = response.xpath("//div[@class='j_joblist']//div[@class='e']")
        print(selectors)
        item = WuyouItem()
        for selector in selectors:
            item = {}
            item['pname'] = selector.xpath("./span[@class='jname at']/text()").get()
            item['time'] = selector.xpath("./span[@class='time']/text()").get()
            item['salary'] = selector.xpath("./span[@class='sal']/text()").get()
            item['workCityAndworkingExpAndeducation'] = selector.xpath("./span[@class='d at']/text()").get()
            item['welfareLabel'] = selector.xpath("./p[@class='tags']/@title").get()
            item['cname'] = selector.xpath("./a[@class='cname at']/text()").get()
            item['propertyAndcompanySize'] = selector.xpath("./p[@class='dc at']/text()").get()
            item['industry'] = selector.xpath("./p[@class='int at']/text()").get()
            print("sssssssssssssssssss")
        # if selectors is None:
        #     # 没有数据
        #     pass
        # else:
        #     for page in range(1, 5):
        #         yield scrapy.Request(
        #             url=str(response.url).replace(',1.html', f',{page}.html'),
        #             dont_filter=True,
        #             callback=self.parse_result
        #         )

    def parse_result(self, response):
        selectors = response.xpath("//div[@class='j_joblist']//div[@class='e']")
        print(selectors)
        item = WuyouItem()
        for selector in selectors:
            item = {}
            item['pname'] = selector.xpath("./span[@class='jname at']/text()").get()
            item['time'] = selector.xpath("./span[@class='time']/text()").get()
            item['salary'] = selector.xpath("./span[@class='sal']/text()").get()
            item['workCityAndworkingExpAndeducation'] = selector.xpath("./span[@class='d at']/text()").get()
            item['welfareLabel'] = selector.xpath("./p[@class='tags']/@title").get()
            item['cname'] = selector.xpath("./a[@class='cname at']/text()").get()
            item['propertyAndcompanySize'] = selector.xpath("./p[@class='dc at']/text()").get()
            item['industry'] = selector.xpath("./p[@class='int at']/text()").get()
            print("ssssssssssssssssss")
            yield item
