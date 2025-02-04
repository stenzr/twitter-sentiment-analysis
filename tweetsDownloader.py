import tweepy
import userCredentials

#twitter authentication

auth = tweepy.OAuthHandler(userCredentials.consumer_key, userCredentials.consumer_secret)
auth.set_access_token(userCredentials.access_token, userCredentials.access_token_secret)
api = tweepy.API(auth)


#streaming
from tweepy import Stream
from tweepy.streaming import StreamListener


class MyListener(StreamListener):

	def on_data(self, data):
		try:
			with open('kedarnathDatasetTwitter.json', 'a') as f:
				f.write(data)
				return True
		except BaseException as e:
			print("Error on_data: %s" % str(e))
		return True

	def on_error(self, status):
		print(status)
		return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#kedarnath'])




