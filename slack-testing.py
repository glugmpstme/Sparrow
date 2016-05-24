#!/usr/bin/env python

import time
import pprint
from slackclient import SlackClient

token = 'xoxp-16751206212-16756631639-44418396547-e43ecfadc2'

sc = SlackClient(token)
pp = pprint.PrettyPrinter(indent=2)

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