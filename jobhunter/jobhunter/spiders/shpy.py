import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
from ..items import JobhunterItem

class ShpySpider(scrapy.Spider):
    name = 'shpy'
    allowed_domains = ['www.liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?city=020&dq=020&pubTime=&currentPage={}&pageSize=40&key=python&suggestTag=&workYearCode=&compId=&compName=&compTag=&industry=&salary=&jobKind=&compScale=&compKind=&compStage=&eduLevel=&otherCity=&skId=pz5fwxdkrmx80pud5fnzmowryc2nwmta&ckId=rr37nkv26nktbwh5ye0t4wkso3h1aeva&sfrom=search_job_pc&fkId=eam6y5ycytm0pc1k5qke5k1anlbdewpb&scene=condition&suggestId='.format(i) for i in range(10)]
    detail_urls = []

    def __init__(self):
        self.chrome = webdriver.Edge()

    def parse(self, response, **kwargs):
        bs = BeautifulSoup(response.text, 'lxml')
        a_lst = bs.find_all('a', class_='jsx-2693574896')
        for a in a_lst:
            detail_url = a.get('href')
            self.detail_urls.append(detail_url)
        for detail_url in self.detail_urls:
            yield scrapy.Request(detail_url, callback=self.parse_detail)


    def parse_detail(self, response):
        bs = BeautifulSoup(response.text, 'lxml')
        title = ' '.join(bs.find('div', class_='name-box').text.split())
        info = bs.find('section', class_='job-intro-container').dl.dd.text

        item = JobhunterItem()
        item['title'] = title
        item['info'] = info

        yield item

    def close(self,spider):
        self.chrome.close()