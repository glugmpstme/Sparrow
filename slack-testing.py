#!/usr/bin/env python3

import time
#for pretty printing the received response
import pprint
# never add access tokens directly to code, specially in public code
from token import token
#see README.md for instructions on importing the SDK
from slackclient import SlackClient

# specify a local 'tokenfile.py' with the token string from Slack
token = tokenfile.thetoken
# initialise the SlackClient with token
sc = SlackClient(token)
pp = pprint.PrettyPrinter(indent=2)

# test API call
# TODO: Remove in production
pp.pprint(sc.api_call('api.test'))


class MessageObject:
	"""docstring for MessageObject"""
	def __init__(self, message):
		self.channel = message['channel']
		self.ts = message['ts']
		self.text = message['text']

def storeMessage(message):
	pass

def cyPretty(response):	
	pp.pprint(response)

if sc.rtm_connect():
	while True:
		# rtm_read() returns an array of dicts
		responseArray = sc.rtm_read()
		for response in responseArray:
			if response['type'] == 'message' or \
			response['type'] == 'reaction_added' or \
			response['type'] == 'reaction_removed':
				cyPretty(response)
			else:
				print (response['type']);
		time.sleep(1)
else:
	pp.pprint(sc.rtm_connect())