import json

import scrapy

from JobHunterSpider.items import ZhilianItem


class ZhilianspiderSpider(scrapy.Spider):
    name = 'ZhiLianSpider'
    allowed_domains = ['zhaopin.com']
    start_urls = ['https://fe-api.zhaopin.com/c/i/jobs/searched-jobs?pageNo=2&pageSize=50']

    def parse(self, response):
        # 对应json数据中的data
        datas = json.loads(response.text)
        try:
            totalcount = int(datas['data']['page']['total'])
            totalPagecount = int(datas['data']['page']['totalPage'])
        except Exception:
            totalcount = 0

        if totalcount == 0:
            # 没有数据
            pass
        else:
            if totalPagecount <=1 :
                pass
            else:
                for page in range(1, totalPagecount):
                    yield scrapy.Request(
                        url=str(response.url).replace('pageNo=1', f'pageNo={page}'),
                        dont_filter=True,
                        callback=self.parse_result
                    )

    # 对最终的结果进行解析
    def parse_result(self, response):
        item = ZhilianItem()
        datas = json.loads(response.text)
        try:
            data_list = datas['data']['list']
        except Exception:
            data_list = []

        if len(data_list) > 0:
            for data in data_list:
                item = {}
                # 职位名称
                item['pname'] = data['name']
                # 公司名称
                item['cname'] = data['company']
                # 工作城市
                item['workCity'] = data['workCity']
                # 薪资范围
                item['salary'] = data['salary']
                # 学历要求
                item['education'] = data['education']
                # 公司类型
                item['property'] = data['property']
                # 公司规模
                item['companySize'] = data['companySize']
                # 工作经验
                item['workingExp'] = data['workingExp']
                # 福利待遇
                # 提取json数据中的value值，先转换为列表，再转换为字符串返回
                json_data = data['welfareLabel']
                json_list = []
                for i in json_data:
                    json_list.append(i['value'])
                temp_data = [str(k) for k in json_list]
                welfare_str = ','.join(temp_data)
                item['welfareLabel'] = welfare_str
                print(item)
                yield item

