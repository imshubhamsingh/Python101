import twitter
from pprint import pprint

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

pprint(api.VerifyCredentials())

friends = api.GetFriends()
followers = api.GetFollowers()

post_update = api.PostUpdate(status='')


new_message = api.PostDirectMessage(screen_name='imshubhamsingh_',text='Hi There')

api.GetHomeTimeline()