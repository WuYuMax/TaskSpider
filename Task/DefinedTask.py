from Core.NetWork import visit
from Core.NetWork import VisitorWays
from Core import  Anlyst
from Core.URLs import WayUrl
from Core.URLs import WebUrl
from abc import abstractmethod
import time
from Task.Task import  Task
from requests import Session


# 可以确定后继访问的任务
class DenfinedTask(Task):

    webUrl = None
    wayUrls = list()
    visitoryWay:VisitorWays
    visitData = dict()
    visitHeader = dict()
    response = None
    resultData = list()
    delayTimes:int = 1
    session:Session = None

    def __init__(self,Message):
        self.resultData = list()
        self.response = None
        self.visitData = dict()
        self.nextMessage = None

    def run(self)->list:
        self.delay()
        self.init()
        self.surf()
        self.anlyse()
        self.execute()
        nextTasks = self.createNextTask()
        return nextTasks

    @staticmethod
    def create(message):
        pass

    @abstractmethod
    def init(self):
        pass

    def surf(self):
        self.response = visit(self.webUrl,self.visitoryWay,self.visitData,self.visitHeader,self.session)
        self.response.encoding = self.response.apparent_encoding

    def anlyse(self):
        for wayUrl in self.wayUrls:
            currentData = Anlyst.anlyse(wayUrl,self.response.text)
            self.resultData.append(currentData)

    def writeBack(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    def delay(self):
        # print(self.delayTimes)
        time.sleep(self.delayTimes)

    @abstractmethod
    def createNextTask(self)->list():
        pass


