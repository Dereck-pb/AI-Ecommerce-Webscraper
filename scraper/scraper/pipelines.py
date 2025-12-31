import psycopg2

class PostgresPipeline:
    def open_spider(self, spider):
        self.conn = psycopg2.connect(
            host="localhost",
            database="ecommerce",
            user="postgres",
            password="YOUR_PASSWORD"
        )
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        self.cur.execute("""
            INSERT INTO products (title, price, rating, category, url)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            item["title"],
            item["price"],
            item["rating"],
            item["category"],
            item["url"]
        ))
        self.conn.commit()
        return item
