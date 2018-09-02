from urllib import request,parse

if __name__ == '__main__':

    base_url = 'http://www.baidu.com/s?'

    wd = input("关键词")

    qs = {
        "wd":wd
    }

    qs = parse.urlencode(qs)
    rsp = request.urlopen(base_url+qs)

    html = rsp.read()

    html = html.decode()

    print(html)