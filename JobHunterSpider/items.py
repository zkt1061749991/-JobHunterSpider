# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    # 职位名称
    pname = scrapy.Field()
    # 公司名称
    cname = scrapy.Field()
    # 工作城市
    workCity = scrapy.Field()
    # 薪资范围
    salary = scrapy.Field()
    # 学历要求
    education = scrapy.Field()
    # 公司类型
    property = scrapy.Field()
    # 公司规模
    companySize = scrapy.Field()
    # 工作经验
    workingExp = scrapy.Field()
    # 福利待遇
    welfareLabel = scrapy.Field()


class WuyouItem(scrapy.Item):
    # 职位名称
    pname = scrapy.Field()
    # 薪资待遇
    salary = scrapy.Field()
    # 工作城市和经验要求
    workCityAndworkingExpAndeducation = scrapy.Field()
    # 福利待遇
    welfareLabel = scrapy.Field()
    # 公司名称
    cname = scrapy.Field()
    # 公司属性和规模
    propertyAndcompanySize = scrapy.Field()
    # 职业类型
    industry = scrapy.Field()

