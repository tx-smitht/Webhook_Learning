import requests
import json

# Webhook URL from webhook.site .
webhook_url ='http://127.0.0.1:5000/webhook'

# Create the fake data
data = { 'name': 'Tom\'s new webhook',
        'Current status': 'hungry',
        'Current favorite animal': 'golden eagle'}

# Make a post request
r = requests.post(
    webhook_url,
    data=json.dumps(data),
    headers={'Content-Type': 'application/json'},
    verify=False
)