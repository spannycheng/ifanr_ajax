# -*- coding: utf-8 -*-
import scrapy
import json
from ifanr_ajax.items import IfanrAjaxItem


class IfanrSpider(scrapy.Spider):
    name = 'ifanr'
    allowed_domains = ['ifanr.com']
    start_urls = ['https://sso.ifanr.com/api/v5/wp/web-feed/?limit=20&offset=0']
    num_a = 1
    num_b = 1

    def parse(self, response):
        rs = json.loads(response.text)
        print("="*60,self.num_a,"="*60)
        print(response.url)
        for obj_list in rs["objects"]:
            item = IfanrAjaxItem()
            # print(obj_list)
            item["author"] = obj_list.get('created_by').get("name")
            item["pub_time"] = obj_list.get('created_at_format')
            item["title"] = obj_list.get('post_title')
            post_url = obj_list.get('post_url')
            item["post_url"] = obj_list.get('post_url')
            item["cover_image"] = obj_list.get('post_cover_image')
            # print("+"*20,self.num_b,"+"*20)
            # print("作者：", item["name"])
            # print("时间：", item["pub_time"])
            # print("标题：", item["title"])
            # print("网址：", item["post_url"])
            # print("图片：", item["cover_image"])
            # print("\n")
            yield scrapy.Request(url=post_url,callback=self.parse_detail,meta={"item":item})
            self.num_b += 1
            # print(name)
        self.num_a += 1
        base_next_url = "https://sso.ifanr.com/api/v5/wp/web-feed/?limit=20&offset={offset}"
        for index in range(20,100,20):
            next_url = base_next_url.replace("{offset}",str(index))
            yield scrapy.Request(url=next_url,callback=self.parse)


    def parse_detail(self,response):
        item = response.meta["item"]
        item["category"] = response.xpath("//p[@class='c-article-header-meta__category']/text()").get()
        item["content"] = "".join(response.xpath("//article[contains(@class,article)]//p//text()").getall()).strip()
        print("-"*40,"第",self.num_b,"篇文章","-"*40)
        print("作者：", item["author"])
        print("时间：", item["pub_time"])
        print("标题：", item["title"])
        print("网址：", item["post_url"])
        print("图片：", item["cover_image"])
        print("分类：",item["category"])
        print("内容：",item["content"])
        print("\n")
        yield item