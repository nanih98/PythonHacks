import urllib3

http = urllib3.PoolManager()
body = http.request('GET',"http://www.nostarch.com")

print(body.data)