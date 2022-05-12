from Task.NetworkTask import NetworkTask, VisitConfig
from Task.TaskMessage import TaskMessage
from Task.Task import Task


class SSTask(NetworkTask):
    def __init__(self):
        super().__init__()
        self.visUrl = "https://yz.chsi.com.cn/zsml/pages/getSs.jsp"
        self.wayUrl = "JSON://"

    def init(self, message: TaskMessage) -> VisitConfig:
        builder = VisitConfig.Builder()
        visitconfig =builder.setWebUrl(self.visUrl)\
            .postWay()\
            .addWayUrl('ss',self.wayUrl)\
            .setDelayTime(0)\
            .setVisitData(dict())\
            .setVisitHeader(dict())\
            .build()
        self.message = message
        return visitconfig


    def execute(self, visitResult) -> TaskMessage:

        res = {}

        for k_v in visitResult['ss']:
            res[k_v['mc']] = k_v['dm']
        self.message.setData(key='ss',value=res)
        return self.message

class MLTask(NetworkTask):
    def __init__(self):
        super().__init__()
        self.visUrl = "https://yz.chsi.com.cn/zsml/pages/getMl.jsp"
        self.wayUrl = "JSON://"

    def init(self, message: TaskMessage) -> VisitConfig:
        builder = VisitConfig.Builder()
        visitconfig =builder.setWebUrl(self.visUrl)\
            .postWay()\
            .addWayUrl('ml',self.wayUrl)\
            .setDelayTime(0)\
            .setVisitData(dict())\
            .setVisitHeader(dict())\
            .build()
        self.Message = message
        return visitconfig


    def execute(self, visitResult) -> TaskMessage:

        res = {}

        for k_v in visitResult['ml']:
            res[k_v['mc']] = k_v['dm']
        self.Message.setData(key='ml',value=res)
        # print(res)
        return self.Message


class ZYTask(NetworkTask):
    def __init__(self):
        super().__init__()
        self.visUrl = "https://yz.chsi.com.cn/zsml/pages/getZy.jsp"
        self.wayUrl = "JSON://"

    def init(self, message: TaskMessage) -> VisitConfig:
        builder = VisitConfig.Builder()
        visitconfig = builder.setWebUrl(self.visUrl) \
            .postWay() \
            .addWayUrl('zy',self.wayUrl) \
            .setDelayTime(0) \
            .setVisitData(dict()) \
            .setVisitHeader(dict()) \
            .build()
        self.Message = message
        return visitconfig

    def execute(self, visitResult) -> TaskMessage:
        res = {}

        for k_v in visitResult['zy']:
            res[k_v['mc']] = k_v['dm']
        self.Message.setData(key='zy', value=res)
        return self.Message

class BaseMessageTask(Task):

    def __init__(self):
        self.sstask = SSTask()
        self.mltask = MLTask()
        self.zytask = ZYTask()
    def run(self, message: TaskMessage) -> TaskMessage:
        temp = self.sstask.run(message)
        temp = self.mltask.run(temp)
        temp = self.zytask.run(temp)


        return temp


if __name__ == '__main__':
    newMessage = BaseMessageTask().run(TaskMessage())
    # print(newMessage.getData('ml'))