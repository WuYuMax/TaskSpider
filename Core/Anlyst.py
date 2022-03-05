from Core.URLs import WayUrl
import lxml.etree as etree
from bs4 import BeautifulSoup
import json
import re

# 根据解析URL分配解析方式
def anlyse(url,textOfReponse:str):
#     若为string则转换
    if isinstance(url,str):
        url =  WayUrl.parse(url)
    # print(str(url.getWay()))
#     分析URL的解析方法
    currentModel = url.getModel().upper()
    if currentModel == "REGEX":
        return anlyseByRegex(url,textOfReponse)
    elif currentModel == "XPATH":
        return anlyseByXpath(url,textOfReponse)
    elif currentModel == "DOM":
        return anlyseByDOM(url,textOfReponse)
    elif currentModel == "JSON":
        return anlyseByJson(url,textOfReponse)
    else:
        print("URL解析方式不支持",currentModel)
    return None

# TODO:将所有的返回格式化以方便处理


# 正则表达式解析方式
def anlyseByRegex(url:WayUrl,textOfReponse):
    # print("Anlyse By REGEX")
    return re.findall(url.getWay(),textOfReponse)

# XPath解析方式
def anlyseByXpath(url:WayUrl,textOfReponse):
    # print("Anlyse By XPath")
    currentHtml = etree.HTML(textOfReponse,parser=etree.HTMLParser(encoding='utf-8'))
    rule = url.getWay()
    res_set = currentHtml.xpath(rule)
    # print(textOfReponse)
    return res_set

# DOM解析方式
# TODO: 支持多种的BS索引方式 如今只支持Selector
def anlyseByDOM(url:WayUrl,textOfReponse):
    # print("Anlyse By DOM")
    soup = BeautifulSoup(textOfReponse,'lxml')
    rule = url.getWay()
    return soup.select(rule)

# JSON解析方式
def anlyseByJson(url:WayUrl,textOfReponse):
    # print("anlyseByJson")
    return json.loads(textOfReponse)
