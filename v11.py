from urllib import request

if __name__ == '__main__':

    url = "http://www.renren.com/967875686/profile"

    headers = {
        "Cookie":"td_cookie=18446744069593017649; anonymid=jlnay6jl-t6enl4; depovince=CQ; _r01_=1; JSESSIONID=abcN9ti8IIdXZ4WNgkJww; ick_login=06a0c949-f991-4845-a575-e5240b9a4d15; t=576192d847a6342b8535781f0b2009b66; societyguester=576192d847a6342b8535781f0b2009b66; id=967875686; xnsid=5cd78247; jebecookies=7fba4685-50e6-4ce0-a801-88ed1db1580f|||||; ver=7.0; loginfrom=null; jebe_key=893e855b-2f67-4a2f-a1d9-ff2eecaf862f%7C88c3d4ba188163ac8a0ac5a6a84a72c8%7C1536040666042%7C1%7C1536040668756; wp_fold=0"
    }

    req = request.Request(url,headers = headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode("utf-8")

    with open("helloworld.html","w") as f:
        f.write(html)