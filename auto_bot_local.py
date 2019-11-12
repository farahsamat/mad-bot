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
INTERVAL = 60 * 60 * 0.4
MINI_INTERVAL = 60 * 60 * 0.04
MICRO_INTERVAL = 60 * 60 * 0.004
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
        get_quote = Quotes()
        link = [get_quote.brainy(),
                get_quote.good_reads(),
                get_quote.good_housekeeping(),
                get_quote.keep_inspiring()]
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
                 scrape.nature(),
                 scrape.google_ai(),
                 scrape.tech_crunch(),
                 scrape.sc_news(),
                 scrape.the_verge()]
        random.shuffle(sc_tech)

        blogs = [scrape.song_of_style(),
                scrape.bag_snob()]
        random.shuffle(blogs)

        for q, n, a, b in zip(link, news, sc_tech, blogs):
            mad_bot.tweet_quote(q)
            pause = random.choice(sleep_time)
            print(int(pause), "seconds")
            time.sleep(pause)

            text, url = n
            mad_bot.tweet_news(text, url)
            pause = random.choice(sleep_time)
            print(int(pause), "seconds")
            time.sleep(pause)

            text, url = a
            mad_bot.tweet_sc_tech(text, url)
            pause = random.choice(sleep_time)
            print(int(pause), "seconds")
            time.sleep(pause)

            text, url = b
            mad_bot.tweet_lifestyle(text, url)
            pause = random.choice(sleep_time)
            print(int(pause), "seconds")
            time.sleep(pause)

        mad_bot.like_tweets()
        pause = random.choice(sleep_time)
        print(pause, "seconds")
        time.sleep(pause)
