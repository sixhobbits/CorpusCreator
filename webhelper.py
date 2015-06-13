# A wrapper for urllib2 to download HTML from a url
import StringIO
from threading import Thread
import time
import urllib2


def _make_request(url):
    try:
        response = urllib2.urlopen(url)
        return response
    except urllib2.HTTPError as e:
        if e.code == 403 or e.code == 404:
            # try with different agent
            req = urllib2.Request(url, headers={'User-Agent': "Mozilla/5.0"})
            response = urllib2.urlopen(req)
            return response
        else:
            raise e


class WebHelper:
    def __init__(self):
        pass

    def get_html(self, url):
        """Download the HTML from the URL"
        Handle compression and retrying with a different user agent if necessary

        Args:
            url (str): The url from which to fetch the html
        Returns:
            page (str): The full HTML retrieved from the URL
        """

        response = _make_request(url)
        # if html is gzipped.
        if response.info().get('Content-Encoding') == 'gzip':
            buf = StringIO(response.read())
            f = gzip.GzipFile(fileobj=buf)
            page = f.read()
        else:
            page = response.read()
        return page

    def attempt_get_html(self, url):
        """Attempt to get HTML for the URL, retrying and then swallowing exceptions

        Args:
            url (str): The URL
        Returns:
            html (str or None): The downloaded HTML if possible or None if our attempts failed.
        """
        for retry in range(3):
            try:
                return self.get_html(url)
            except Exception as e:
                time.sleep(3)

    def populate_html(self, url_object):
        """Attempts to populate a URL object with and HTML property by downloading from the given URL.
        Args:
            url_object (object): An object containing a URL in a property called .url.
        Returns:
            url_object (object): The same object, but with its .html property set to the HTML of the page or None.
        url_object.html = attempt_get_html(url_object.url)
        return url_object
        """
        url_object.html = self.attempt_get_html(url_object.url)
        return url_object

    def get_html_threaded(self, url_objects):
        """(Best effort) download HTML for each URL. A new thread is created for each URL.

        Args:
            url_objects ([obj]): The URLs. Each should be an object with the URL in a property called .url.
        Returns:
            url_objects ([obj]): The input objects, now each has has a .html property populated with HTML or None.
        """
        threads = [Thread(target=self.populate_html, args=(o,)) for o in url_objects]
        [t.start() for t in threads]
        [t.join() for t in threads]
        return url_objects
