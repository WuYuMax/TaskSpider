from enum import Enum
from Core.URLs import WebUrl
import requests

# TODO: 提供Session的传承

# 枚举类型
class VisitorWays(Enum):
    GET = 1
    POST = 2

# 负责访问网页并且根据请求方式分配方法
def visit(url,visitways:VisitorWays,data:dict,headers:dict=None,session:requests.Session=None):
    if isinstance(url,str):
        url = WebUrl.parse(url)

    defaultHeader = headers
    # 装配Header
    defaultHeader = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }

    for key in headers.keys():
        defaultHeader[key] = headers[key]

    # 内容分发
    if visitways is visitways.GET:
        return get(url,data,defaultHeader,session)
    elif visitways is visitways.POST:
        return post(url,data,defaultHeader,session)

# Post方法
def post(url:WebUrl,data:dict,headers:dict,session:requests.Session):
    res = None
    if session is not None :
        # print(url,data,headers)
        res = session.post(url.host,data,headers=headers)
    else:
        res = requests.post(str(url),data,headers=headers)

    return res

# Get方法
def get(url:WebUrl,data:dict,headers:dict,session:requests.Session):
    # currentUrlBuilder = WebUrl.WebUrlBuilder()
    # currentUrlBuilder.addHost(url.host)
    #
    # for keys in data.keys():
    #     currentUrlBuilder.addParam(keys,data[keys])
    #     # url.addparms(keys,data[keys])
    # currentUrl = currentUrlBuilder.build()
    # print(currentUrl)
    # print(url.host,url.params)
    if data :
        if session is not None:
            return session.get(url.host,params=data,headers=headers)
        return requests.get(url.host,params=data,headers=headers)
    else :
        # print('use origin params',url.host,url.params)
        if session is not None:
            return session.get(str(url),headers=headers)
        return requests.get(str(url),headers=headers)
