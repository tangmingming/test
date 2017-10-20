import urllib2
import json

headers = {"cache-control": "no-cache",
           "content-type": "application/json",
           "postman-token": "dec645d6-6265-fc90-19a8-f3701c4a9f94"}

data = {}

url = "sparta.dianwoda.com"

req = urllib2.Request(url=url, data=json.dumps(data), headers=headers)

res = urllib2.urlopen(req)

print res.read()