from Core.URLs import WebUrl
from Core.URLs import WayUrl
from Core.NetWork import visit
from Core.NetWork import VisitorWays

def WebUrlTest():
    url = WebUrl.WebUrlBuilder().addHost('http://www.baidu.com/s?').\
        addParam("wd","python who is yourdady").build()
    inputDic = {"wd":"python"}
    res = visit(url.host,VisitorWays.GET,inputDic,dict())
    res.encoding = res.apparent_encoding
    print(res.text)


def WayUrlTestByBuilder():
    # 构造器构造测试
    testWayUrl =WayUrl.WayUrlBuilder().\
        addModel("DOM").addWays("itemxx").\
        addWays("li").build()
    print(str(testWayUrl))
def WayUrlTestByCreate():
    testWayUrl = WayUrl.create("JSON",["xx"])
    print(str(testWayUrl))
def WayUrlTestByStr(url:str):
    testWayUrl = WayUrl.parse(url)
    print(str(testWayUrl),testWayUrl.ways)
def TwoDifferentWayURL():
    one = WayUrl.parse("DOM://li/li/li")
    two = WayUrl.parse("Xpath://")
    print(two)
    print(one)
    pass


if __name__ == '__main__':
    # WebUrlTest()
    # WebUrlPostTest()
    # WayUrlTestByCreate()
    # WayUrlTestByBuilder()
    # WayUrlTestByStr("XPATH://li/la/lb/item/value")
    # TwoDifferentWayURL()
    pass