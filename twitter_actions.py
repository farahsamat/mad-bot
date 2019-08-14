import tweepy
import pickle
import re
from textblob import TextBlob
from text_summary import TextSummary
from gensim.summarization import summarize


class TwitterActions:
    def __init__(self, api):
        self.api = api
        return

    def tweet(self, text):
        try:
            self.api.update_status(text)
        except tweepy.error.TweepError as e:
            print('Details of error: ', e)

    def tweet_news(self, news_item):
        try:
            self.api.update_status(news_item)
        except tweepy.error.TweepError as e:
            print(news_item, e)

    def tweet_thread(self, url):
        summarize_article = TextSummary()
        text_summary = summarize(summarize_article.page(url), word_count=150)
        return text_summary

    