import tweepy
import re
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def wordcloudbot():
    # Consumer keys and access tokens, used for OAuth
    CONSUMER_KEY = 'enter your key'
    CONSUMER_SECRET = 'enter your secret'
    ACCESS_KEY = 'enter your key'
    ACCESS_SECRET = 'enter your secret'

    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)

    #Fetch the tweets
    tweets = api.search_tweets(q='#FPLCommunity', count =100, result_type="recent")
    tweet_text_list = []
    for i in tweets:
        tweet_text_list.append(i.text)
    df_tweet = pd.DataFrame(tweet_text_list)

    #Clean up the tweet texts
    stopwords = set(STOPWORDS)
    stopwords.update(["https","RT"])

    bigstring = df_tweet.apply(lambda x: ' '.join(x)).str.cat(sep=' ')
    bigstring = re.sub('[^A-Za-z0-9]+',' ',bigstring)

    plt.figure(figsize=(10,10))
    wordcloud = WordCloud(stopwords=stopwords,background_color='white',width=1200, height=1000,min_word_length=4,collocations=True,collocation_threshold=10).generate(bigstring)

    plt.axis('off')
    plt.imshow(wordcloud)

if __name__ == "__main__":
    wordcloudbot()
