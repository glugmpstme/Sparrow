from slackclient import SlackClient

token = 'xoxp-16751206212-16756631639-44418396547-e43ecfadc2'

sc = SlackClient(token)

print sc.api_call('api.test')
print type(sc.api_call('api.test'))

print sc.api_call(
	'chat.postMessage',
	channel='#social-ops',
	text='There is going to be a lot of noise here during testing. Fleel free to leave/mute for the time being',
	username='pysparrow-testing',
	icon_emoji=':robot_face:'
	)