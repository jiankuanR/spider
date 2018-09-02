from urllib import request,parse
import json

base_url = 'http://fanyi.baidu.com/sug'

kw = input("请输入关键词：")
data = {
    "kw" : kw
}

data = parse.urlencode(data).encode("utf-8")

headers = {
    "Content-Length" : len(data)
}

req = request.Request(url = base_url,data = data,headers = headers)
rsp = request.urlopen(req)

json_data = rsp.read().decode("utf-8")

json_data = json.loads(json_data)

for item in json_data["data"]:
    print(item)