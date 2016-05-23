import time
import pprint
from slackclient import SlackClient

token = 'xoxp-16751206212-16756631639-44418396547-e43ecfadc2'

sc = SlackClient(token)

print sc.api_call('api.test')
print type(sc.api_call('api.test'))

def cyPretty(response):
	pp = pprint.PrettyPrinter(indent=2)
	pp.pprint(response)

if sc.rtm_connect():
	while True:
		responseArray = sc.rtm_read()
		for response in responseArray:
			cyPretty(response)
		time.sleep(1)
else:
	print sc.rtm_connect()