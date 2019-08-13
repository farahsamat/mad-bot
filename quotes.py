import requests
import random
from bs4 import BeautifulSoup

good_reads_quotes = 'https://www.goodreads.com/quotes/'
tags = ['philosophy',
        'science',
        'education',
        'inspirational',
        'time',
        'life']


class Quotes:
    def __init__(self):
        return

    def good_reads(self):
        web_data = BeautifulSoup(requests.get(good_reads_quotes + 'tag/{}'.format(random.choice(tags))).text,
                                 'html.parser').find_all(class_='quote mediumText ')
        text = '#goodreads #quote ' + random.choice(web_data).find(class_='quoteText').text.replace('\n', '').strip()
        return text
