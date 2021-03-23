import requests

url = "http://www.nostarch.com"

headers = {}
headers['User-Agent'] = "Googlebot"

requests = requests.get(url, headers=headers)


print(requests.content)
requests.close