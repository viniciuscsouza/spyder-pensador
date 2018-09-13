# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class PensadorPipeline(object):

    def process_item(self, item, spider):
        self.cursor.execute("INSERT INTO frases (frase) VALUES (:frase)", item)
        self.conn.commit()
        return item

    def create_table(self):
        self.cursor.execute("""
	        CREATE TABLE IF NOT EXISTS frases(
			    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			    frase TEXT UNIQUE NOT NULL);
            """)

    def open_spider(self, spider):
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()

        self.create_table()

    def close_spider(self, spider):
        self.conn.close()