import tweepy
import pickle
import re
import random
from textblob import TextBlob
from websites import Websites
from quotes import Quotes
from text_summary import TextSummary
from gensim.summarization import summarize


class TwitterActions:
    def __init__(self):
        return

    def tweet(self):
        get_quote = Quotes()
        return get_quote.good_reads()

    def scrape_and_tweet(self):
        scrape = Websites()
        news_items = []
        link_text = [scrape.ny_times(),
                     scrape.nine_news(),
                     scrape.the_star(),
                     scrape.abc(),
                     scrape.bbc(),
                     scrape.towards_data_science(),
                     scrape.nature(),
                     scrape.google_ai(),
                     scrape.the_verge(),
                     scrape.business_insider(),
                     scrape.tech_crunch(),
                     scrape.malaysia_kini()
                     ]

        num = [x for x in range(len(link_text))]
        random.shuffle(num)
        for i in num:
            news_items.append(link_text[i])
        return news_items

    def summary_thread(self, url):
        summarize_article = TextSummary()
        text_summary = summarize(summarize_article.page(url), word_count=150)
        return text_summary
