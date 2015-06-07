# A wrapper for the PYthon feedparser package which extends to allow for
# * Downloading the full HTML of the linked article
# * Extracting metadata meaningful for a corpus
# * Returning an Article that we can insert into our Database

import feedparser
import HTTPHelper
import Aritcle


class FeedDownloader:

    def __init__(feed_url):
        self.feed_url = feed_url

    def parse(self):
        pass

    def download_html(self):
        pass




