#!/usr/bin/env python3

import pprint
import tokenfile
from slackclient import SlackClient

token = tokenfile.thetoken
print(token)

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