from urllib import request,parse
import json

base_url = 'http://fanyi.baidu.com/sug'

kw = input("请输入关键词：")
data = {
    "kw" : kw
}

data = parse.urlencode(data)

headers = {
    "Content-Length" : len(data)
}

rsp = request.urlopen()