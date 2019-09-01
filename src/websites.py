import requests
import random
from bs4 import BeautifulSoup

bbc = 'https://www.bbc.com/news/'
ny_times = 'https://www.nytimes.com/'
the_star = 'https://www.thestar.com.my/'
malaysia_kini = 'https://www.malaysiakini.com/'
abc = 'https://www.abc.net.au/news/'
nine_news = 'https://www.9news.com.au/'
towards_data_science = 'https://towardsdatascience.com/'
nature = 'https://www.nature.com/'
google_ai = 'https://ai.googleblog.com/'
the_verge = 'https://www.theverge.com/tech'
tech_crunch = 'https://techcrunch.com/'
business_insider = 'https://www.businessinsider.com.au/'


class Websites:
    def __init__(self):
        return

    def bbc(self):
        web_data = BeautifulSoup(requests.get(bbc).text, 'html.parser').find_all(class_='nw-c-top-stories-primary__story gel-layout gs-u-pb gs-u-pb0@m')
        link = '{}'.format(bbc[:-6]) + web_data[0].find('a')['href']
        text = '#bbcnews ' + web_data[0].find('h3').text
        return text[:100] + ' ' + link

    def ny_times(self):
        web_data = BeautifulSoup(requests.get(ny_times).text, 'html.parser').find_all(class_='css-16ugw5f e1aa0s8g0')
        link = '{}'. format(ny_times[:-1]) + web_data[0].find('a')['href']
        text = '#nytimes ' + web_data[0].find('h2').text
        return text[:100] + ' ' + link

    def the_star(self):
        web_data = BeautifulSoup(requests.get(the_star).text, 'html.parser').find_all(class_='focus-story')
        link = web_data[0].find('a')['href']
        text = '@staronline ' + web_data[0].find('h2').text.strip()
        return text[:100] + ' ' + link

    def malaysia_kini(self):
        web_data = BeautifulSoup(requests.get(malaysia_kini).text, 'html.parser').find_all(class_='uk-container')
        link = '{}'. format(malaysia_kini[:-1]) + web_data[0].find('a')['href']
        text = '#malaysiakini ' + web_data[0].find('h3').text
        return text[:100] + ' ' + link

    def abc(self):
        web_data = BeautifulSoup(requests.get(abc).text, 'html.parser').find_all(class_='section module-body')
        link = '{}'.format(abc[:-6]) + web_data[0].find('a')['href']
        text = '#abcnews ' + web_data[0].find('h3').text.strip()
        return text[:100] + ' ' + link

    def nine_news(self):
        web_data = BeautifulSoup(requests.get(nine_news).text, 'html.parser').find_all('article')
        link = web_data[0].find('a')['href']
        text = '#ninenews ' + web_data[0].find('h1').text
        return text[:100] + ' ' + link

    def towards_data_science(self):
        web_data = BeautifulSoup(requests.get(towards_data_science).text, 'html.parser').find_all(class_='streamItem streamItem--section js-streamItem')
        feeling_lucky = random.choice(web_data)
        link = feeling_lucky.find('a')['href']
        text = '#towardsdatascience ' + feeling_lucky.find('h3').text
        return text[:100] + ' ' + link

    def nature(self):
        web_data = BeautifulSoup(requests.get(nature).text, 'html.parser').find_all('article')
        #feeling_lucky = random.choice(web_data)
        link = web_data[0].find('a')['href']
        text = '#nature ' + web_data[0].find('h3').text.strip()
        return text[:100] + ' ' + link

    def google_ai(self):
        web_data = BeautifulSoup(requests.get(google_ai).text, 'html.parser').find_all(class_='post')
        feeling_lucky = random.choice(web_data)
        link = feeling_lucky.find('a')['href']
        text = '#googleAI ' + feeling_lucky.find('h2').text.strip()
        return text[:100] + ' ' + link

    def the_verge(self):
        web_data = BeautifulSoup(requests.get(the_verge).text, 'html.parser').find_all(class_='l-hero ')
        feeling_lucky = random.choice(web_data)
        link = feeling_lucky.find('a')['href']
        text = '#theverge ' + feeling_lucky.find('h3').text.strip()
        return text[:100] + ' ' + link

    def tech_crunch(self):
        web_data = BeautifulSoup(requests.get(tech_crunch).text, 'html.parser').find_all(class_='content')
        feeling_lucky = random.choice(web_data)
        link = feeling_lucky.find('a')['href']
        text = '#techcrunch ' + feeling_lucky.find('h2', {'class': 'post-block__title'}).text.strip()
        return text[:100] + ' ' + link

    def business_insider(self):
        web_data = BeautifulSoup(requests.get(business_insider).text, 'html.parser').find_all('div', {'id': 'top-stories'})
        feeling_lucky = random.choice(web_data)
        link = feeling_lucky.find('a')['href']
        text = '#BI ' + feeling_lucky.find('h1').text.strip()
        return text[:100] + ' ' + link










