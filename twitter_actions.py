import tweepy
import textwrap
from text_summary import TextSummary
from gensim.summarization import summarize


class TwitterActions:
    def __init__(self, api, username):
        self.api = api
        self.username = username
        return

    def tweet(self, text):
        try:
            self.api.update_status(text, tweet_method='extended')
        except tweepy.error.TweepError as e:
            print('Details of error: ', e)

    def tweet_news(self, news_item):
        try:
            self.api.update_status(news_item, tweet_method='extended')
        except tweepy.error.TweepError as e:
            print(news_item, e)

    def tweet_thread(self, url):
        summarize_article = TextSummary()
        text_summary = summarize(summarize_article.page(url), word_count=150)
        if len(text_summary) <= 280:
            try:
                self.api.update_status('1/1\n', url + '\n', text_summary, tweet_mode='extended')
            except tweepy.error.TweepError as e:
                print(url, e)
        else:
            text_chunks = textwrap.wrap(text_summary, 276)
            try:
                self.api.update_status(url)
                tweet = self.api.user_timeline(screen_name=self.username, count=1)[0]
                for i in range(len(text_chunks)):
                    self.api.update_status('{}/{}\n'.format(i + 1, len(text_chunks)) + text_chunks[i], tweet.id, tweet_mode='extended')
            except tweepy.error.TweepError as e:
                print(e)

    def like_tweets(self):
        friends = [user.screen_name for user in tweepy.Cursor(self.api.friends, screen_name=self.username).items()]
        for friend in friends:
            try:
                for tweet in tweepy.Cursor(self.api.user_timeline, screen_name='@'+friend, exclude_replies=True, include_rts=False).items(1):
                    self.api.create_favorite(tweet.id)
            except tweepy.error.TweepError as e:
                print(friend, e)

