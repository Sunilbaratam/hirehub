# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
import uuid

class HireCrawlerPipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('data.db')  # Connect to SQLite database
        self.curr = self.conn.cursor()
        # self.curr.execute('''DROP TABLE IF EXISTS ipos''')
        # self.curr.execute('''CREATE TABLE ipos (
        #                     id TEXT PRIMARY KEY,
        #                     name TEXT,
        #                     price REAL,
        #                     size REAL,
        #                     quantity REAL,
        #                     opening_date TEXT,
        #                     closing_date TEXT,
        #                     listing_date TEXT  
        #                 )''')
        self.conn.commit()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        # Example: Insert data into a table named 'jobs'
        id = str(uuid.uuid4())
        self.curr.execute("INSERT INTO ipos (id, name, price, size, quantity, opening_date, closing_date, listing_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                          (id, item['IPO'], item['Price'], item['IPO Size'], item['Lot'], item['Open'], item['Close'], item['Listing']))
        self.conn.commit()
        return item