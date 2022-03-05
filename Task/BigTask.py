from Task.Task import Task
import threadpool
import time
import threading

class BigTask(Task):
    __MAX_Threads = 8

    def __init__(self,taskList:list):
        super().__init__()
        self.TaskRequest = list()
        self.resultTasks = list()
        self.resultMutex = threading.Lock()
        # 建立线程池
        if len(taskList) < self.__MAX_Threads:
            self.Pool = threadpool.ThreadPool(len(taskList))
        else:
            self.Pool = threadpool.ThreadPool(self.__MAX_Threads)

        for currentTask in taskList:
            currentRequest = threadpool.WorkRequest(currentTask.run,None,callback=self.__collectAllTask)
            self.TaskRequest.append(currentRequest)

    def __collectAllTask(a,request,response:list):
        a.resultMutex.acquire()
        a.resultTasks.extend(response)
        a.resultMutex.release()

    def run(self) ->list:
        res = []
        for req in self.TaskRequest:
            self.Pool.putRequest(req)

        self.Pool.wait()
        res.append(BigTask(self.resultTasks))
        # print(self.resultTasks)
        return res

