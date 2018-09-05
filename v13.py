from urllib import request,parse
from http import cookiejar


#创建cookieJar实例
cookie = cookiejar.CookieJar()
#cookie管理器
cookie_Handler = request.HTTPCookieProcessor(cookie)
#http管理器
http_Handler = request.HTTPHandler()
#https管理器
https_Handler = request.HTTPSHandler()

opener = request.build_opener(cookie_Handler,http_Handler,https_Handler)

def login():

    url = "http://www.renren.com/PLogin.do"
    data = {
        "email":"13039991659",
        "password":"wozhidao"
    }

    data = parse.urlencode(data)

    req = request.Request(url,data = data.encode("utf-8"))

    rsp = opener.open(req)

def getHomePage( ):
    url = "http://www.renren.com/860398849/profile"

    rsp = opener.open(url)

    html = rsp.read().decode()

    with open("haha.html", "w") as f:
        f.write(html)

if __name__ == '__main__':
    login()
    getHomePage()