# Title: CMPE273-fall18-LAB1-Part1
# Description: Use requests to make 3 HTTP calls to Webhook
#              and print the response header 'Date'
#

import requests

urls = [
    'https://webhook.site/aca00aa8-a470-479b-a1bd-50133c3ba2a1',
    'https://webhook.site/aca00aa8-a470-479b-a1bd-50133c3ba2a1',
    'https://webhook.site/aca00aa8-a470-479b-a1bd-50133c3ba2a1'
]

for url in urls:
    response = requests.get(url)
    print(response.headers['Date'])


