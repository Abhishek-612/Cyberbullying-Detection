from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API, Cursor
import twitter_credentials


class TwitterClient:
    # twitter_user= None will take you to the your Twitter timeline
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends).items(num_friends):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, num_tweets):
        home_timeline = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline.append(tweet)
        return home_timeline


class TwitterAuthenticator:

    def authenticate_twitter(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth


class TwitterStreamer:
    # Streaming and processing live tweets
    def __init__(self):
        self.twitter_auth = TwitterAuthenticator()

    def stream_tweets(self, tweet_file, hash_tag_list):
        # Authentication and API connection
        listener = TwitterListener(tweet_file)
        auth = self.twitter_auth.authenticate_twitter()
        stream = Stream(auth, listener)

        stream.filter(track=hash_tag_list,languages=['en'])


class TwitterListener(StreamListener):
    # Listener class to print tweets
    def __init__(self, tweet_file):
        self.tweet_file = tweet_file

    def on_data(self, data):
        try:
            print(data)
            with open(self.tweet_file, 'a') as f:
                f.write(data)
        except BaseException as e:
            print('Error: {}'.format(e))
        return True

    def on_error(self, status):
        if status == 420:
            # If rate limit exceeds, cancel tweet extraction.
            return False
        print(status)
