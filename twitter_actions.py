import tweepy
import textwrap
import fire
from src.generate_unconditional_samples import GenerateUnconditionalSamples
from src.interactive_conditional_samples import InteractiveConditionalSample
from src.text_summary import TextSummary
from src.cloud_image import CloudImage
from gensim.summarization import summarize
from datetime import datetime


class TwitterActions:
    def __init__(self, api, username):
        self.api = api
        self.username = username
        return

    def tweet_quote(self, text):
        try:
            self.api.update_status(text, tweet_method='extended')
        except tweepy.error.TweepError as e:
            print('Details of error: ', e)

    def tweet_random(self):
        gpt_model = GenerateUnconditionalSamples()
        generate_text = fire.Fire(gpt_model.sample_model)
        text_chunks = textwrap.wrap(generate_text, 280 - 5)
        try:
            self.api.update_status(
                '[{}] The following text is brought to you by #OpenAI GPT2. Reader discretion is advised.'.format(
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')), tweet_mode='extended')
            tweet = self.api.user_timeline(screen_name=self.username, count=1)[0]
            for i in range(len(text_chunks)):
                self.api.update_status('{}/{}\n'.format(i + 1, len(text_chunks)) + text_chunks[i], tweet.id,
                                       tweet_mode='extended')
        except tweepy.error.TweepError as e:
            print(e)

    def tweet_news(self, text, link):
        try:
            self.api.update_status(text + ' ' + link, tweet_method='extended')
        except tweepy.error.TweepError as e:
            print(text, e)

    def tweet_summary(self, url):
        whole_passage = TextSummary()
        text = whole_passage.page(url)
        image = CloudImage()
        text_summary = summarize(text, word_count=250)
        if len(text_summary) <= 280:
            try:
                self.api.update_with_media(image.word_cloud(text), '1/1\n', url + '\n', text_summary, tweet_mode='extended')
            except tweepy.error.TweepError as e:
                print(url, e)
        else:
            text_chunks = textwrap.wrap(text_summary, 275)
            try:
                self.api.update_with_media(image.word_cloud(text), url)
                tweet = self.api.user_timeline(screen_name=self.username, count=1)[0]
                for i in range(len(text_chunks)):
                    self.api.update_status('{}/{}\n'.format(i + 1, len(text_chunks)) + text_chunks[i], tweet.id,
                                           tweet_mode='extended')
            except tweepy.error.TweepError as e:
                print(e)

    def like_tweets(self):
        friends = [user.screen_name for user in tweepy.Cursor(self.api.friends, screen_name=self.username).items()]
        for friend in friends:
            try:
                for tweet in tweepy.Cursor(self.api.user_timeline, screen_name='@' + friend, exclude_replies=True,
                                           include_rts=False).items(1):
                    self.api.create_favorite(tweet.id)
            except tweepy.error.TweepError as e:
                print(friend, e)

    def reply_tweets(self):
        for tweet in tweepy.Cursor(self.api.mentions_timeline).items(1):
            gpt_model = InteractiveConditionalSample(tweet.text[16:])
            generate_reply = fire.Fire(gpt_model.interact_model())
            if len(generate_reply) <= 280:
                try:
                    self.api.update_status('@' + tweet.user.screen_name + generate_reply, tweet.id, tweet_mode='extended')
                except tweepy.error.TweepError as e:
                    print(e)
            else:
                text_chunks = textwrap.wrap(generate_reply, 280)
                try:
                    self.api.update_status('@' + tweet.user.screen_name + text_chunks[0], tweet.id, tweet_mode='extended')
                    for i in range(len(text_chunks)+1):
                        self.api.update_status(text_chunks[i+1], tweet.id,
                                               tweet_mode='extended')
                except tweepy.error.TweepError as e:
                    print(e)

    def view_trend(self, hashtag):
        image = CloudImage()
        text = [tweet.text.replace(hashtag, '') for tweet in tweepy.Cursor(self.api.search, q='#'+hashtag, include_rts=False,  rpp=100).items(10)]

        try:
            self.api.update_with_media(image.word_cloud(' '.join(text)), '#'+hashtag)
        except tweepy.error.TweepError as e:
            print(e)

