# pysparrow 
Sparrow, but in python!

### Core Objective
Auto repost all content from channel #social-ops to fb and twitter based on *threshold* of *+1*s

### Additional Objectives

1. List posts
2. Undo posts
3. Varible threshold

### Instructions for Slack Python SDK

1. Assuming Linux and python3
2. Install and activate [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
3. `pip install slackclient`
4. Get your test OAuth token from the [test token generator](https://api.slack.com/docs/oauth-test-tokens)

### Strategy

#### Stage 1: slack-interaction

1. Listen to each message on the channel #social-ops
2. Store each message (a dict object in itself) in a dict indexed by it's channel+ts
3. Listen to all reactions added and removed
4. Associate each *+1* or *-1* with the corresponding message
5. If threshold is reached send an ack to the channel