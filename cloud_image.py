import matplotlib.pyplot as plt
import re
import os
from wordcloud import WordCloud, STOPWORDS

stopwords = set(STOPWORDS)


class CloudImage:
    def __init__(self):
        return

    def word_cloud(self, text):
        w_cloud = WordCloud(width=800, height=800,
                           background_color='white',
                           min_font_size=10,
                           stopwords=stopwords).generate(' '.join(re.sub(r"[^a-z0-9]", " ", text.lower()).split(" ")))

        # plot and save the WordCloud image
        image_path = os.path.abspath('images') + '/word_cloud.png'
        plt.figure(figsize=(4, 4), facecolor=None)
        plt.imshow(w_cloud)
        plt.axis("off")
        plt.tight_layout(pad=0)
        plt.savefig(os.path.abspath(image_path))
        return image_path

