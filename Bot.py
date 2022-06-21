import tweepy

#simple test 

#load api keys and access tokens of bot account
api_key = "1rZb5OXLAJEuAgrNWT7AjWa7n"
api_key_secret = "O0mFCLlkHzc3BAqWS9fBKs1OhcdxSidPmf91H0wmDFBA5ytgxN"
access_token = "1537218967034396672-5XiiClF9hk1gEgDEu0aPGauXgEUrPB"
access_token_secret = "0QCIIevOity2vSq4x95GoDUolqqOywfO5dw0NK9om6Wtw"

#create authenticator by passing api key and secret to OAuth authenticator
authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

#make the api
api = tweepy.API(authenticator)

#tweet
api.update_status("testing 2")