#just testing
from twitter import *

new_status = "Hello world!" #whatever is given by the bot comes here 

config = {}
execfile("config.py", config)

#authenticate configuration
twitter = Twitter(
	auth =  OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

#update
results =  twitter.statuses.update(status = new_status)
