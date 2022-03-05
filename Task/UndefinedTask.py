from Task.DefinedTask import DenfinedTask

# 难以确定后继的任务：将以构造函数时确定其后继
class UndenfinedTask(DenfinedTask):
    __nextTasks:list = None

    def __init__(self,nextTasks:list):
        super().__init__()
        self.__nextTasks = nextTasks

    def run(self) -> list:
        self.delay()
        self.init()
        self.surf()
        self.anlyse()
        self.execute()
        nextTasks = self.__createNextTask()
        return nextTasks

    def __createNextTask(self) -> list():
        res = []
        for currentTask in self.__nextTasks:
            t = currentTask.create(self.nextMessage)
            res.append(t)
        return res

