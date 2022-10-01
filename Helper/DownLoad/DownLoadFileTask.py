from Task.NetworkTask import NetworkTask, VisitConfig
from Task.TaskMessage import TaskMessage
import codecs
import os
'''
DownLoadTask:
@input: DownLoadUrl:str,OrderDirPath:str,FileName:str 如果FileName不存在则截取最后名
'''


class DownLoadFileTask(NetworkTask):

    def init(self, message: TaskMessage) -> VisitConfig:
        downloadUrl:str = message.getData('DownLoadUrl')
        self.orderDirPath = message.getData('OrderDirPath')
        fileName = message.getData('FileName')
        if fileName is None:
            fileName = downloadUrl.split('/')[-1]
        self.FileName = fileName


        return VisitConfig.Builder()\
            .setWebUrl(downloadUrl)\
            .getWay()\
            .build()

    def execute(self, visitResult, message: TaskMessage) -> TaskMessage:
        content = self.response.content
        orderpath = os.path.join(self.orderDirPath,self.FileName)
        with codecs.open(orderpath,mode='wb') as f:
            f.write(content)
        return message