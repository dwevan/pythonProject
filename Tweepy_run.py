import tweepy
import twitter_credentials as twcr

auth = tweepy.OAuthHandler(twcr.consumer_key, twcr.consumer_secret)
auth.set_access_token(twcr.access_token, twcr.access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    