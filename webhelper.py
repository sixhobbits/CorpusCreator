# A wrapper for urllib2 to download HTML from a url
import urllib2
import StringIO


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
        response = _make_request(url)
        # if html is gzipped.
        if response.info().get('Content-Encoding') == 'gzip':
            buf = StringIO(response.read())
            f = gzip.GzipFile(fileobj=buf)
            page = f.read()
        else:
            page = response.read()
        return page
