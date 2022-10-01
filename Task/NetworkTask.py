from Core.NetWork import visit
from Core.NetWork import VisitorWays
from Core import  Anlyst
from Core.URLs import WayUrl
from Core.URLs import WebUrl
from Task.TaskMessage import TaskMessage
from abc import abstractmethod
import time
from Task.Task import  Task
from requests import Session


class VisitConfig():
    def __init__(self):
        self.webUrl = None
        self.wayUrls = list()
        self.visitoryWay:VisitorWays = None
        self.visitData = dict()
        self.visitHeader = dict()
        self.delaytime = 0
        self.Session = None
        self.encode = None
    class Builder():
        def __init__(self):
           self.producer= VisitConfig()
        def setWebUrl(self,webUrl):
            self.producer.webUrl = webUrl
            return self
        # 已经修改为键值对方案
        def addWayUrl(self,wayName,wayUrl):
            self.producer.wayUrls.append((wayName,wayUrl))
            return  self
        def postWay(self):
            self.producer.visitoryWay = VisitorWays.POST
            return self
        def getWay(self):
            self.producer.visitoryWay = VisitorWays.GET
            return self
        def setVisitData(self,visitData):
            self.producer.visitData = visitData
            return self
        def setVisitHeader(self,visitHeader):
            self.producer.visitHeader = visitHeader
            return self
        def setDelayTime(self,delayTimes):
            self.producer.delaytime =delayTimes
            return self
        def setEncoding(self,encode=None):
            self.producer.encode = encode
            return self
        def setSession(self,session):
            self.producer.session = session
            return self
        def build(self):
            res = self.producer
            self.producer = VisitConfig()
            return res

# 网络任务的模板 我们只需要完成基础内容的赋予并且完成解析URL的赋予就可以完成一个询问节点
class NetworkTask(Task):

    # init构造函数被用于初始化一个访问节点的基础信息如网址，解析url
    def __init__(self):
        pass

    def run(self,message:TaskMessage)->TaskMessage:
        self.visitConfig = self.init(message)
        response = self.surf()
        res = self.anlyse(response)
        self.response = response
        self.delay()
        newMessage = self.execute(res,message)
        return newMessage

    # 我们在init阶段将message中的内容成功转化为我们需要的内容
    @abstractmethod
    def init(self,message:TaskMessage)->VisitConfig:
        pass

    def surf(self):
        visitConfig = self.visitConfig
        response = visit(visitConfig.webUrl,visitConfig.visitoryWay,visitConfig.visitData,visitConfig.visitHeader,visitConfig.Session)

        if visitConfig.encode :
            response.encoding = visitConfig.encode
        else:
            response.encoding = response.apparent_encoding
        return response
        # self.response = visit(self.webUrl,self.visitoryWay,self.visitData,self.visitHeader,self.session)
        # self.response.encoding = self.response.apparent_encoding

    # 已经改为键值对模式
    def anlyse(self,response):
        resultData = {}
        for wayName,wayUrl in self.visitConfig.wayUrls:
            currentData = Anlyst.anlyse(wayUrl,response.text)
            resultData[wayName] = currentData
        return resultData

    @abstractmethod
    def execute(self,visitResult,message:TaskMessage)->TaskMessage:
        pass

    def delay(self):
        time.sleep(self.visitConfig.delaytime)




