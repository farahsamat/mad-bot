import requests
from bs4 import BeautifulSoup


class TextSummary:
    def __init__(self):
        return

    def page(self, url):
        paragraph = [p.getText() for p in BeautifulSoup(requests.get(url).text, 'html.parser').find_all('p')]
        whole_text = ' '.join(paragraph)
        return whole_text




