from dateutil import parser
import datetime

import feedparser

from article import Article


class FeedDownloader:
    "Use FeedParser to extract only relevant meta-data from a feed and transform it into list of Articles"

    def __init__(self, feed_url, publication):
        self.feed_url = feed_url
        self.publication = publication

    def parse(self):
        # We create one Article for every item in the feed
        articles = []
        try:
            feed = feedparser.parse(self.feed_url)
            # TODO: Normalize language - different feeds may use different conventions to specify this
            langauge = feed.feed['language']
            feed_publication_date = feed.feed['updated']
            feed_title = feed.feed['title']
            for entry in feed['entries']:
                url = entry['link']
                headline = entry['title']
                article_date = entry['published']
                date_retrieved = datetime.datetime.now()
                articles.append(Article(url, date_retrieved, article_date=article_date, publication=self.publication, 
                                headline=headline, language=langauge))
        except Exception as e:
            print "error"
            print e
        return articles
