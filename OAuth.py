import tweepy

consumer_token = "xj0moU1dge55Ag4TOTFeVUKpL"
consumer_secret = "7YCTOtHj6qwUmo1q01k9SHAS7rk61qxthgbkGORKEweA6ignYm"
access_token = "294518321-ECYBXhsmbZIiL4kliZ9sUdaEfdKlgEYfeKLJZrwU"
access_token_secret = "D5OG0OCVDGprwmpsZJQOqNI1GtMXQ4PQpbxwbqm2l60KZ"

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Get the User object for twitter...
user = api.get_user('matthughes97')
print(user.screen_name)
followers = api.followers()
for follower in followers:
    print(follower.screen_name, follower.followers_count)
