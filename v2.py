import urllib
import chardet

if __name__ == '__main__':
    url = 'https://blog.csdn.net/c406495762/article/details/72858983'

    rsp = urllib.request.urlopen(url)

    html = rsp.read()

    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    html = html.decode(cs.get('encodeing','utf-8'))

    print(html)