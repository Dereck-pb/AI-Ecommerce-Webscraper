import scrapy
from scraper.items import ProductItem

class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com/products"]

    def parse(self, response):
        for product in response.css(".product-card"):
            item = ProductItem()
            item["title"] = product.css(".title::text").get()
            item["price"] = product.css(".price::text").get()
            item["rating"] = product.css(".rating::text").get()
            item["category"] = product.css(".category::text").get()
            item["url"] = response.url
            yield item
