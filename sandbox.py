from feeder import FeedDownloader
from webhelper import WebHelper
from cleaner import Cleaner

from threading import Thread

import time

t1 = time.time()

fd = FeedDownloader("http://mybroadband.co.za/news/feed", "My Broadband")
wh = WebHelper()
cleaner = Cleaner()

articles = fd.parse()

print time.time() - t1, "setup complete"
t1 = time.time()

wh.get_html_threaded(articles)
print time.time() - t1, "threaded download complete"

t1 = time.time()
for a in articles:
    a.html = wh.attempt_get_html(a.url)
print time.time() - t1, "non threaded download complete"

t1 = time.time()
for a in articles:
    if a.html:
        a.plaintext = cleaner.clean(a.html)
        print(a.plaintext[:300])
        print('')
print time.time() - t1, "cleaning complete"

