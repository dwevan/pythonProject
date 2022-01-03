from time import time
import tweepy
import twitter_credentials as twcr
import datetime

# Authorize Twitter credentials
auth = tweepy.OAuthHandler(twcr.consumer_key, twcr.consumer_secret)
auth.set_access_token(twcr.access_token, twcr.access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#steps taken from (https://fairyonice.github.io/extract-someones-tweet-using-tweepy.html, and https://towardsdatascience.com/how-to-build-a-dataset-from-twitter-using-python-tweepy-861bdbc16fa5

userID = "@UKCP_Updates"

tweets = api.user_timeline(screen_name=userID, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )

all_tweets = []
all_tweets.extend(tweets)
oldest_id = tweets[-1].id
while True:
    tweets = api.user_timeline(screen_name=userID, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           max_id = oldest_id - 1,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
    if len(tweets) == 0:
        break
    oldest_id = tweets[-1].id
    all_tweets.extend(tweets)
    print('N of tweets downloaded till now {}'.format(len(all_tweets)))

#code to label file with datestamp of when data taken
current_date_and_time = str(datetime.date.today())    
filename =  userID + '_tweets_at_' + current_date_and_time

from pandas import DataFrame
outtweets = [[tweet.id_str, 
              tweet.created_at, 
              tweet.full_text.encode("utf-8").decode("utf-8")] 
             for idx,tweet in enumerate(all_tweets)]
df = DataFrame(outtweets,columns=["id","created_at", "text"])
df.to_csv(filename + '.csv' ,index=False)

print (filename)