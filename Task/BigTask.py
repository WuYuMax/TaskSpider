from Task.Task import Task
from Task.TaskMessage import TaskMessage
import threadpool
import time
import threading
import copy

# From orderName take your messages and Run The Task ,The New Message Will Be Take to the OrderName
class BigTask(Task):
    __MAX_Threads = 8

    def __init__(self,task:Task,paramsName:str,orderName:str,numOfThread:int=8):
        super().__init__()
        self.TaskRequest = list()
        self.resultMessage = list()
        self.resultMutex = threading.Lock()
        # 建立线程池
        self.Pool = threadpool.ThreadPool(numOfThread)
        self.paramsName = paramsName
        self.orderName = orderName
        self.task = task


    def __collectAllTask(a,request,response:TaskMessage):
        a.resultMutex.acquire()

        value = response.getDic()

        a.resultMessage.append(value)
        a.resultMutex.release()

    def __dispatchMessage(self,message:TaskMessage)->list:
        messages =[]
        for param in message.getData(self.paramsName):
            current = TaskMessage()
            # current.removeData(self.paramsName)
            if type(param) is dict:
                current.setDic(param)
            else:
                current.setData(self.paramsName,param)
            # print(current.getDic())
            messages.append(current)
        return messages


    def run(self,message:TaskMessage) ->TaskMessage:
        newmessages = self.__dispatchMessage(message)

        self.TaskRequest.clear()

        for currentmessage in newmessages:
            # print('test',currentmessage.getData(self.paramsName))
            currenttask = copy.deepcopy(self.task)
            currentRequest = threadpool.WorkRequest(currenttask.run,args=[currentmessage],callback=self.__collectAllTask)
            self.TaskRequest.append(currentRequest)

        for req in self.TaskRequest:
            self.Pool.putRequest(req)

        self.Pool.wait()
        # print('all over')
        message.setData(self.orderName,self.resultMessage)
        # print(self.resultTasks)
        return message

