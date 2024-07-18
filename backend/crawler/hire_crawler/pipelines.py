# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class HireCrawlerPipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('data.db')  # Connect to SQLite database
        self.curr = self.conn.cursor()

        self.curr.execute('''CREATE TABLE IF NOT EXISTS ipos (
                            IPO TEXT,
                            Price REAL,
                            GMP REAL
                        )''')
        self.conn.commit()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        # Example: Insert data into a table named 'jobs'
        self.curr.execute("INSERT INTO ipos (IPO, Price, GMP) VALUES (?, ?, ?)", (item['IPO'], item['Price'], item['GMP']))
        self.conn.commit()
        return item