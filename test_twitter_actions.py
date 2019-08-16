import os
import tweepy
import unittest
from dotenv import load_dotenv
from twitter_actions import TwitterActions

load_dotenv()
test_tweet = 'Test tweet. #themadbot'
test_news_list = ['#news1 at his elit sententiae',
                  '#news2 te quo aliquam mediocrem',
                  '#news3 id est falli viderer.']
test_text_summary = ''

username = os.getenv("USERNAME")
consumer_key = os.getenv("KEY")
consumer_secret = os.getenv("SECRET")
access_token = os.getenv("TOKEN")
access_token_secret = os.getenv("TOKEN_SECRET")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


class TwitterActionsTest(unittest.TestCase):
    def setUp(self):
        self.TwitterActions = TwitterActions(api)

    def test_tweet_with_duplicate_status_raises_error(self):
        self.TwitterActions.tweet(test_tweet)
        with self.assertRaises(tweepy.error.TweepError):
            api.update_status(test_tweet)

    def test_tweet_news_with_duplicate_news_raises_error(self):
        for i in range(len(test_news_list)):
            self.TwitterActions.tweet_news(test_news_list[i])
        with self.assertRaises(tweepy.error.TweepError):
            for i in range(len(test_news_list)):
                api.update_status(test_news_list[i])

