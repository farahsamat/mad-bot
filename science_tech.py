import requests
from bs4 import BeautifulSoup

towards_data_science = 'https://towardsdatascience.com/'
nature = 'https://www.nature.com/'


class ScienceTech:
    def __init__(self):
        return

    def towards_data_science(self):
        web_data = BeautifulSoup(requests.get(towards_data_science).text, 'html.parser').find_all(class_='streamItem streamItem--section js-streamItem')
        link = web_data[0].find('a')['href']
        text = web_data[0].find('h3').text
        return link, text

    def nature(self):
        web_data = BeautifulSoup(requests.get(nature).text, 'html.parser').find_all('article')
        link = web_data[0].find('a')['href']
        text = web_data[0].find('h3').text
        return link, text

