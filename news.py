import requests
from bs4 import BeautifulSoup

bbc = 'https://www.bbc.com/news/'
ny_times = 'https://www.nytimes.com/'
the_star = 'https://www.thestar.com.my/'
malaysia_kini = 'https://www.malaysiakini.com/'
abc = 'https://www.abc.net.au/news/'
nine_news = 'https://www.9news.com.au/'


class News:
    def __init__(self):
        return

    def bbc(self):
        web_data = BeautifulSoup(requests.get(bbc).text, 'html.parser').find_all(class_='nw-c-top-stories-primary__story gel-layout gs-u-pb gs-u-pb0@m')
        link = '{}'.format(bbc[:-6]) + web_data[0].find('a')['href']
        text = web_data[0].find('h3').text
        return link, text

    def ny_times(self):
        web_data = BeautifulSoup(requests.get(ny_times).text, 'html.parser').find_all(class_='css-16ugw5f e1aa0s8g0')
        link = '{}'. format(ny_times[:-1]) + web_data[0].find('a')['href']
        text = web_data[0].find('h2').text
        return link, text
        return

    def the_star(self):
        web_data = BeautifulSoup(requests.get(the_star).text, 'html.parser').find_all(class_='focus-story')
        link = web_data[0].find('a')['href']
        text = web_data[0].find('h2').text.strip()
        return link, text

    def malaysia_kini(self):
        web_data = BeautifulSoup(requests.get(malaysia_kini).text, 'html.parser').find_all(class_='uk-container')
        link = '{}'. format(malaysia_kini[:-1]) + web_data[0].find('a')['href']
        text = web_data[0].find('h3').text
        return link, text

    def abc(self):
        web_data = BeautifulSoup(requests.get(abc).text, 'html.parser').find_all(class_='section module-body')
        link = '{}'.format(abc[:-6]) + web_data[0].find('a')['href']
        text = web_data[0].find('h3').text
        return link, text

    def nine_news(self):
        web_data = BeautifulSoup(requests.get(nine_news).text, 'html.parser').find_all('article')
        link = web_data[0].find('a')['href']
        text = web_data[0].find('h1').text
        return link, text
        return







