# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JobhunterPipeline:

    file = None

    def open_spider(self, spider):
        print('打开存储空间，存储为csv')
        self.file = open(r'C:\Users\Knigh\Desktop\上海-python工作.csv', 'w', encoding='gb18030')

    def process_item(self, item, spider):
        title = item['title']
        info = item['info']
        self.file.write(title+'\n'+info)

        return item

    def close_spider(self, spider):
        print('关闭存储空间')
        self.file.close()