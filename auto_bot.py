import tweepy
import os
import random
import time
from twitter_actions import TwitterActions
from src.quotes import Quotes
from src.websites import Websites
from dotenv import load_dotenv

load_dotenv()
os.system('cls' if os.name == 'nt' else 'clear')
INTERVAL = 60 * 60 * 1
MINI_INTERVAL = 60 * 60 * 0.1
MICRO_INTERVAL = 60 * 60 * 0.01
sleep_time = [INTERVAL, MINI_INTERVAL, MICRO_INTERVAL]

if __name__ == "__main__":
    username = os.getenv("USERNAME")
    consumer_key = os.getenv("KEY")
    consumer_secret = os.getenv("SECRET")
    access_token = os.getenv("TOKEN")
    access_token_secret = os.getenv("TOKEN_SECRET")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    mad_bot = TwitterActions(api, username)

    while True:
        url_collection = []

        get_quote = Quotes()
        link = [get_quote.brainy(),
                get_quote.good_reads()]
        random.shuffle(link)

        scrape = Websites()
        news = [scrape.ny_times(),
                scrape.nine_news(),
                scrape.the_star(),
                scrape.abc(),
                scrape.bbc(),
                scrape.malaysia_kini()]
        random.shuffle(news)

        sc_tech = [scrape.towards_data_science(),
                 scrape.google_ai(),
                 scrape.tech_crunch()]
        random.shuffle(sc_tech)


        for quote, news, tech in zip(link, news, sc_tech):
            mad_bot.tweet_quote(quote)
            pause = random.choice(sleep_time)
            print(int(pause), "seconds")
            time.sleep(pause)

            text, url = news
            url_collection.append(url)
            mad_bot.tweet_news(text, url)
            pause = random.choice(sleep_time)
            print(int(pause), "seconds")
            time.sleep(pause)

            text, url = tech
            url_collection.append(url)
            mad_bot.tweet_news(text, url)
            pause = random.choice(sleep_time)
            print(int(pause), "seconds")
            time.sleep(pause)

        mad_bot.tweet_summary(random.choice(url_collection))
        pause = random.choice(sleep_time)
        print(pause, "seconds")
        time.sleep(pause)

        mad_bot.like_tweets()
        pause = random.choice(sleep_time)
        print(pause, "seconds")
        time.sleep(pause)
