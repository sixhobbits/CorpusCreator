# A representation of one article in the corpus
from unidecode import unidecode


def encode(text):
    if text:
        return text.encode("utf-8", "ignore")


class Article:

    def __init__(self, url, retrieved_date, publication, article_date=None, headline=None, author=None, plaintext=None, html=None,
                 language=None):
        self.url = url
        self.retrieved_date = retrieved_date
        self.article_date = article_date
        self.publication = publication
        self.headline = headline
        self.author = author
        self.plaintext = plaintext
        self.html = html
        self.language = language

    def __str__(self):
        headline = self.headline.encode("utf-8", "ignore")
        plaintext = self.plaintext.encode("utf-8", "ignore")

        res = "{} by {}, ({})\n\n{}\n Available at: {}".format(headline, self.author, self.article_date, plaintext, self.url)
        return res