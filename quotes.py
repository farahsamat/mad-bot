import requests
import random
from bs4 import BeautifulSoup

good_reads_quotes = 'https://www.goodreads.com/quotes/'
gr_tags = ['philosophy',
        'science',
        'education',
        'inspirational',
        'time',
        'life',
        'wisdom']

brainy_quote = 'https://www.brainyquote.com/'
bq_tags = ['topics/leadership-quotes',
           'topics/life-quotes',
           'topics/success-quotes',
           'quote_pictures',
           'topics/funny-quotes',
           'authors/lao-tzu-quotes',
           'authors/confucius-quotes']


class Quotes:
    def __init__(self):
        return

    def good_reads(self):
        web_data = BeautifulSoup(requests.get(good_reads_quotes + 'tag/{}'.format(random.choice(gr_tags))).text,
                                 'html.parser').find_all(class_='quoteDetails')
        text = '#goodreads #quote ' + random.choice(web_data).find(class_='quoteText').text.replace('\n', '').strip()
        return text

    def brainy(self):
        web_data = BeautifulSoup(requests.get(brainy_quote + '{}'.format(random.choice(bq_tags))).text,
                                 'html.parser').find_all(class_='clearfix')
        text_items = [item.text for item in random.choice(web_data).find_all('a')]
        text = '#brainyquote ' + ' - '.join(text_items)
        return text
