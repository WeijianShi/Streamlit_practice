import scrapy


class RedditbotSpider(scrapy.Spider):
    name = "redditbot"
    allowed_domains = ["www.reddit.com"]
    start_urls = ["https://www.reddit.com/r/gameofthrones/"]

    def parse(self, response):
        pass
