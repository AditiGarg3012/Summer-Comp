import GetOldTweets3 as got
import pandas as pd
import numpy as np

def get_tweet(tweet):
    twitter_tweet = {}
    twitter_tweet["id"] = tweet.id
    twitter_tweet["date"] = tweet.date
    twitter_tweet["username"] = tweet.username
    twitter_tweet["to"] = tweet.to
    twitter_tweet["text"] = tweet.text
    twitter_tweet["retweets"] = tweet.retweets
    twitter_tweet["favorites"] = tweet.favorites
    twitter_tweet["mentions"] = tweet.mentions
    twitter_tweet["hashtags"] = tweet.hashtags
    twitter_tweet["geo"] = tweet.geo
    twitter_tweet["permalink"] = tweet.permalink
    
    return twitter_tweet


def main():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('morganstanley')\
                                           .setSince("2018-01-01")\
                                           .setUntil("2020-06-01")
    tweets = []                                       
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)
    for t in tweet:
        tweets.append(get_tweet(t))
    cols=['id','date','username','to','text','retweets','favorites','mentions','hashtags','geo','permalink']
    data_frame = pd.DataFrame(tweets, columns=cols)
    data_frame.to_csv('morganstanley.csv', index=False)



if __name__ == '__main__':
    main()

