import tweepy
import csv
import requests
import pickle
from bs4 import BeautifulSoup

fav_sites = ['https://towardsdatascience.com/',
             'https://www.nature.com/',
             'https://www.bbc.com/news',
             'https://www.abc.net.au/news/']


class TwitterActions:
    def __init__(self, api, username):
        self.api = api
        self.username = username
        return

    def get_twitter_config(self):  # Recommended to do only once a day
        config = self.api.configuration()
        with open('config.pickle', 'wb') as f:
            pickle.dump(config, f)

    def get_friend_list(self):
        friend_list = []
        for friend in tweepy.Cursor(self.api.friends, screen_name=self.username).items():
            friend_list.append(friend.screen_name)
        return friend_list

    def get_follower_list(self):
        follower_list = []
        for follower in tweepy.Cursor(self.api.followers, screen_name=self.username).items():
            follower_list.append(follower.screen_name)
        return follower_list

    def tweet(self, tweet):
        return self.api.update_status('#themadbottweets {}'.format(tweet))

    def scrape_and_tweet(self, url):
        link = ''
        respond = requests.get(url).text
        soup = BeautifulSoup(respond, 'html.parser')
        for i in range(len(fav_sites)):
            if url == fav_sites[0]:  # Towards Data Science
                web_data = soup.find_all(class_='streamItem streamItem--section js-streamItem')
                link = web_data[0].find('a')['href']
                text = web_data[0].find('div').text
            elif url == fav_sites[1]:  # Nature
                web_data = soup.find_all('article')
                link = web_data[0].find('a')['href']
                text = web_data[0].find('h3').text #TODO: remove escape charaters
            elif url == fav_sites[2]:  # BBC
                web_data = soup.find_all(class_='nw-c-top-stories-primary__story gel-layout gs-u-pb gs-u-pb0@m')
                link = 'https://bbc.com'+web_data[0].find('a')['href']
                text = web_data[0].find('p').text
            elif url == fav_sites[3]:  # ABC
                web_data = soup.find_all(class_='section module-body')
                link = 'https://abc.net.au'+web_data[0].find('a')['href']
                text = web_data[0].find('p').text
        return self.api.update_status('#themadbottweets {}... {}'.format(text[:100], link))

    def favorite(self, twitter_id):
        return self.api.create_favorite(twitter_id)

    def retweet(self, keyword):
        tweet_ids = []
        for tweet in tweepy.Cursor(self.api.search, q='{}'.format(keyword), include_entities=True).items(1):
            if (not tweet.retweeted) and ('RT @' not in tweet.text):
                tweet_ids.append(tweet.id)
        for id in tweet_ids:
            self.api.retweet(id)

    def reply(self):
        return

    def message(self):
        return



