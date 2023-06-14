import requests
import json

# Webhook URL from webhook.site .
webhook_url ='https://webhook.site/55fb8ec1-a614-4d40-bfb9-30e287728770'

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