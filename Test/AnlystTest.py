from Core.Anlyst import anlyse
from Core.URLs import WayUrl
from Core.URLs import WebUrl
from Test.NetWorkTest import WebUrlPostTest
from Core.NetWork import VisitorWays
from Core.NetWork import visit


xpaths = ['//*[@id="form3"]/a/@href']
selector = '#form3 > a'

def TestOfAnlyseByRegex():
    url  = "regex://a/b0"
    rep = getText().text
    anlyse(url,rep)

def TestOfAnlseByWayUrl():
    wayurl = WayUrl.WayUrlBuilder().addModel("xPath").build()
    anlyse(wayurl)

def getText():
    return WebUrlPostTest()

def TestOfXPath():
    url = WayUrl.WayUrlBuilder().addModel("xpath").\
           addWays(xpaths[0]).build()
    rep = getText()
    res = anlyse(url,rep.text)
    print(res)

def TestOfDOM():
    rep = getText().text
    # print(url)
    url = WayUrl.WayUrlBuilder().\
        addModel("DOM").\
        addWays(selector).\
        build()
    print(url)

    x = anlyse(url,rep)
    for item in x:
        print(item.string)
    print(x)

def TestOfJson():
    weburl = WebUrl.WebUrlBuilder().addHost("https://yz.chsi.com.cn/zsml/pages/getSs.jsp").build()
    rep = visit(weburl,VisitorWays.POST,dict(),dict())
    rep.encoding = rep.apparent_encoding

    wayurl = WayUrl.WayUrlBuilder().addModel("JSON").build()

    res = anlyse(wayurl,rep.text)
    print(res)


if __name__ == '__main__':
    TestOfAnlyseByRegex()
    TestOfXPath()
    TestOfDOM()
    TestOfJson()
    pass