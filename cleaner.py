from reporter import Reporter


class Cleaner:

    def __init__(self):
        self.reporter = Reporter()

    def clean(self, html):
        self.reporter.read(html=html)
        return self.reporter.report_news()
