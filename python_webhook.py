import requests
import json

webhook_url ='https://webhook.site/55fb8ec1-a614-4d40-bfb9-30e287728770'

data = { 'name': 'Tom\'s new webhook',
        'Current status': 'hungry',
        'Current favorite animal': 'golden eagle'}

r = requests.post(
    webhook_url,
    data=json.dumps(data),
    headers={'Content-Type': 'application/json'},
    verify=False
)