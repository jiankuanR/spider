from urllib import request

if __name__ == '__main__':
    url = "https://sou.zhaopin.com/?pageSize=60&jl=551&kw=java&kt=3"
    rsp = request.urlopen(url)

    #把内容给读取出来
    html = rsp.read()

    html = html.decode()
    print(html)