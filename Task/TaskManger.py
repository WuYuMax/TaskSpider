from Task.Task import Task
from threading import Thread
import time

# 负责调度与控制
class TaskManger():

    __taskList = list()
    def __init__(self):
        self.__MutiThread = Thread(target=self.__execute)
    def register(self,task:Task):
        self.__taskList.append(task)
    def start(self):
        self.__MutiThread.start()
    def jion(self):
        self.__MutiThread.join()

    def __execute(self):
        while self.__taskList.__len__() != 0:
            currentTask:Task = self.__getNextOne()
            nextTasks:list = currentTask.run()
            if nextTasks is not None:
                self.__extendTasks(nextTasks)

    def __getNextOne(self):
        return self.__taskList.pop()
    def __extendTasks(self,tasks:list):
        self.__taskList.extend(tasks)
