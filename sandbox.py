from feeder import FeedDownloader
from webhelper import WebHelper
from cleaner import Cleaner

fd = FeedDownloader("http://mybroadband.co.za/news/feed", "My Broadband")
wh = WebHelper()
cleaner = Cleaner()

articles = fd.parse()

for a in articles:
    html = wh.get_html(a.url)
    text = cleaner.clean(html)
    a.html = html
    a.plaintext = text
    print a
    print("-------------")
