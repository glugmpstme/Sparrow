#!/usr/bin/env python

import pprint
from slackclient import SlackClient

token = 'xoxp-16751206212-16756631639-44418396547-e43ecfadc2'

sc = SlackClient(token)
pp = pprint.PrettyPrinter(indent=2)

print(sc.api_call('api.test'))

pp.pprint(sc.api_call(
	'chat.postMessage',
	channel='#social-ops',
	text='https://www.youtube.com/watch?v=PJGpsL_XYQI',
	username='pysparrow-testing',
	icon_emoji=':robot_face:'
	))