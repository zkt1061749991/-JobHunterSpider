# JobHunter云求职系统

基于微服务和大数据的求职系统 爬虫系统

使用分布式思想改进现有的传统架构平台，构建模块化的微服务系统。

- 使用 Scrapy-Redis + Spring @Scheduled 持久化求职信息
- 基于oauth2实现接口级别的权限控制
- 基于sentinel实现流量控制
- 基于Scrapy-redis的爬虫数据缓冲与判重