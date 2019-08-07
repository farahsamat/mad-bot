import tweepy
import pickle
from news import News
from science_tech import ScienceTech

fav_sites = ['https://towardsdatascience.com/',
             'https://www.nature.com/',
             'https://www.bbc.com/news',
             'https://www.abc.net.au/news/',
             'https://www.malaysiakini.com/',
             'https://www.thestar.com.my/',
             'https://www.nytimes.com/',
             'https://www.9news.com.au/']


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
        get_news = News()
        get_scitech = ScienceTech()
        link, text = '', ''

        for i in range(len(fav_sites)):
            if url == fav_sites[0]:  # Towards Data Science
                link, text = get_scitech.towards_data_science()
            elif url == fav_sites[1]:  # Nature
                link, text = get_scitech.nature()
            elif url == fav_sites[2]:  # BBC
                link, text = get_news.bbc()
            elif url == fav_sites[3]:  # ABC
                link, text = get_news.abc()
            elif url == fav_sites[4]:   # Malaysiakini
                link, text = get_news.malaysia_kini()
            elif url == fav_sites[5]:   # The Star
                link, text = get_news.the_star()
            elif url == fav_sites[6]:   # NY Times
                link, text = get_news.ny_times()
            elif url == fav_sites[7]:   # Nine News
                link, text = get_news.nine_news()

        return self.api.update_status('#themadbottweets {} {}'.format(text[:100], link))

    def favorite(self, twitter_id):

        return self.api.create_favorite(twitter_id)

    def retweet(self, keyword):
        for tweet in tweepy.Cursor(self.api.search, q='{}'.format(keyword), include_entities=True, lang='en').items(20):
            if (not tweet.retweeted) and ('RT @' not in tweet.text):
                return self.api.retweet(tweet.id)

    def reply(self):
        return

    def message(self):
        return



