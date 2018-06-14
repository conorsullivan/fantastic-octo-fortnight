import requests
import eagle1

r = requests.get('http://basanese.com')

if r.status_code != 200:
	eagle1.sendMessage()
else:
	print("all is well")

