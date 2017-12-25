from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

# consumer key, consumer secret, access token, access secret.
ckey = "u9H08Q4j2YMRdlrjjjF6FxcRo"
csecret = "qfjjCJLENe2kwEKPns1eA94ydExK5f00YDo2hg02HPcVzERAAn"
atoken = "877653009446064128-dPFZqIFi1AFk51SrAr8Fm0j3Y3fNffi"
asecret = "vqxs07z5Bv6suNfR5zrz4zSQceXKI9kju9Lwh0noYjql4"

class listener(StreamListener):

	def on_data(self, data):
		try:
			all_data = json.loads(data)

			tweet = all_data["text"]
			sentiment_value, confidence = s.sentiment(tweet)
			print(tweet, sentiment_value, confidence)

			if confidence*100 >= 80:
				output = open("twitter-out.txt", "a")
				output.write(sentiment_value)
				output.write('\n')
				output.close()

			return True
		except:
			return True

	def on_error(self, status):
		print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])