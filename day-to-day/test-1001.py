import json
import requests

headers = {"cache-control": "no-cache",
           "content-type": "application/json",
           "postman-token": "dec645d6-6265-fc90-19a8-f3701c4a9f94"}

data = {
 "sign":"c7230639492440566eb9aaae273be6f0e328acf1",
 "aoi_id":"17404741",
 "position_list":[
 {"lng":121.38094329833984,"delivery_id":10263910,"loc_type":4,"time":1504604274,"radius":61,"lat":31.231578826904297,"speed":0,"test":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"},
 {"lng":121.38069915771484,"delivery_id":100003393,"loc_type":4,"time":1507551727,"radius":62,"lat":31.231592178344727,"speed":0},
 {"lng":121.38626861572266,"delivery_id":100024425,"loc_type":4,"time":1507866095,"radius":5,"lat":31.230518341064453,"speed":-1},
 {"lng":121.38068389892578,"delivery_id":100048785,"loc_type":4,"time":1506852462,"radius":53,"lat":31.231590270996094,"speed":0},
 {"lng":121.38626861572266,"delivery_id":100050697,"loc_type":4,"time":1506913520,"radius":5,"lat":31.230518341064453,"speed":-1},
 {"lng":121.38626861572266,"delivery_id":100068969,"loc_type":4,"time":1507634242,"radius":5,"lat":31.230518341064453,"speed":-1},
 {"lng":121.38626861572266,"delivery_id":10263371,"loc_type":4,"time":1507978294,"radius":5,"lat":31.230518341064453,"speed":-1},
 {"lng":121.38068389892578,"delivery_id":10263380,"loc_type":4,"time":1506668053,"radius":60,"lat":31.231590270996094,"speed":0},
 {"lng":121.38063049316406,"delivery_id":10263767,"loc_type":4,"time":1506742306,"radius":65,"lat":31.232013702392578,"speed":-1}
 ],
 "app_id":100001,
 "push_time":1508037406
}

url = "http://182.61.30.232:8186/eleapi/rider/batchuploadpositions"

res = requests.post(url, data=json.dumps(data), headers=headers)
print(res.text)