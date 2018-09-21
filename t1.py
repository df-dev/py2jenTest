#! /usr/bin/env python3


import requests
# this is a test comment

url_get = requests.get('https://sudosilence.net')

print(url_get.url)
print(url_get.text)


