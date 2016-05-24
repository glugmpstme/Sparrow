#!/usr/bin/env python3

import time
# for pretty printing the received response
import pprint
# never add access tokens directly to code, specially in public code
import tokenfile
# see README.md for instructions on importing the SDK
from slackclient import SlackClient

# specify a local 'tokenfile.py' with the token string from Slack
token = tokenfile.thetoken
# initialise the SlackClient with token
sc = SlackClient(token)
pp = pprint.PrettyPrinter(indent=2)

# test API call
# TODO: Remove in production
pp.pprint(sc.api_call('api.test'))


# class MessageObject:
# 	"""docstring for MessageObject"""
# 	def __init__(self, message):
# 		self.channel = message['channel']
# 		self.ts = message['ts']
# 		self.content = message

messagesDict = {} 
threshold = 1

# TODO: replace with actual publish method
def publish(message):
	message['sp-published'] = True
	pp.pprint(sc.api_call(
		'chat.postMessage',
		channel='#social-ops',
		text='Will publish: ' + str(message),
		username='pysparrow-testing',
		icon_emoji=':robot_face:'
		))

# TODO: replace with actual unpublish method
def unpublish(message):
	pp.pprint(sc.api_call(
		'chat.postMessage',
		channel='#social-ops',
		text='Will unpublish: ' + str(message),
		username='pysparrow-testing',
		icon_emoji=':robot_face:'
		))

def storeMessage(message):
	tKey = str(message['channel'] + message['ts'])
	try:
		messagesDict[tKey]
	except KeyError:
		#thumbs up count
		message['sp-tupCount'] = 0
		message['sp-published'] = False
		messagesDict[tKey] = message
	cyPretty(messagesDict)

# delta is either +1 or -1 for add and remove respectively
def updateCount(reaction, delta):
	if reaction['reaction'] == '+1':
		tKey = str(reaction['item']['channel'] + reaction['item']['ts'])
		try:
			# TODO: potential underflow
			messagesDict[tKey]['sp-tupCount'] += delta
			if messagesDict[tKey]['sp-tupCount'] >= threshold:
				publish(messagesDict[tKey])
			elif messagesDict[tKey]['sp-tupCount'] < threshold:
				unpublish(messagesDict[tKey])
		except KeyError:
			print ('[ERR] Message not found in db!')

def cyPretty(response):	
	pp.pprint(response)

if sc.rtm_connect():
	while True:
		# rtm_read() returns an array of dicts
		responseArray = sc.rtm_read()
		for response in responseArray:
			if response['type'] == 'message':
				storeMessage(response)
			elif response['type'] == 'reaction_added':
				updateCount(response, 1)
			elif response['type'] == 'reaction_removed':
				updateCount(response, -1)
			else:
				cyPretty(response)
				#print (response['type']);
		time.sleep(1)
else:
	pp.pprint(sc.rtm_connect())