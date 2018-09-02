# Title: CMPE273-fall18-LAB1-Part2
# Description: Use requests to make 3 HTTP calls ASYNCHRONOUSLY to Webhook
#              and print the response header 'Date'
#

import grequests     

urls = [
    'https://webhook.site/13626683-202f-4877-9197-16169a41e065',
    'https://webhook.site/13626683-202f-4877-9197-16169a41e065',
    'https://webhook.site/13626683-202f-4877-9197-16169a41e065'
] 
    
unsent_request = (grequests.get(url) for url in urls)
    
results = grequests.map(unsent_request)  

for i in results: print(i.headers['Date'])