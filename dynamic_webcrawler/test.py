import lxml.html

url='http://example.webscraping.com/places/default/dynamic'
url='http://example.webscraping.com/places/default/view/Afghanistan-1'

def render(source_html):
    import time
    import sys
    from PyQt5.QtCore import QEventLoop
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtWebEngineWidgets import QWebEngineView

    class Render(QWebEngineView):
        def __init__(self, html):
            self.app = QApplication(sys.argv)
            QWebEngineView.__init__(self)
            self.loadFinished.connect(self._loadFinished)
            self.setHtml(html)
            self.app.exec_()

        def _loadFinished(self):
            # This is an async call, you need to wait for this
            # to be called before closing the app
            self.page().toHtml(self.callable)


        def callable(self, data):
            self.html = data
            # Data has been stored, it's safe to quit the app
            self.app.quit()

    return Render(source_html).html

import requests
sample_html = requests.get(url).text
#print(render(sample_html))
#html=render(sample_html)
tree=lxml.html.fromstring(sample_html)
pop=tree.xpath('//*[@id="places_population__row"]/td[2]')[0].text
c=tree.xpath('//*[@id="places_country__row"]/td[2]')[0].text

#result=tree.cssselect('#result')[0].text_content()
print(c)