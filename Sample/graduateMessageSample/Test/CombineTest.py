from Task.TaskMessage import TaskMessage
from Sample.graduateMessageSample.Task.BaseMessageTask import BaseMessageTask
from Sample.graduateMessageSample.Task.PageSearchTask import PageSearchTask
from Task.BigTask import BigTask
from Sample.graduateMessageSample.Task.GoToMessagePageTask import GoToMessagePageTask
from Sample.graduateMessageSample.Task.MessageGetTask import  MessageGetTask
from Sample.graduateMessageSample.Task.WBTask import WBTask


ssName = None
zyNamme = '工学'
mlName = '计算机科学与技术'
DicPath = '../Dic/'
FildPath = DicPath+zyNamme+mlName


if __name__ == '__main__':
    message = TaskMessage()
    message = BaseMessageTask().run(message)
    # print(message.getData('ss'))
    pageno = 0
    # message.setData('ssname','北京市')
    message.setData('mlname', mlName)
    message.setData('zyname', mlName)
    message.setData('pageno', pageno)
    message.setData('morePage', True)
    wbtask = WBTask(FildPath)
    # print(message.getDic())

    while message.getData('morePage'):
        pageno += 1
        message.setData('pageno', pageno)
        message = PageSearchTask().run(message)
        BigTask(GoToMessagePageTask(),'urls','dataurls').run(message)
        print(message.getData('dataurls'))
        BigTask(MessageGetTask(),'dataurls','res').run(message)
        print(message.getData('res'))
        wbtask.run(message)

        message.removeData('urls')
        message.removeData('dataurls')
        message.removeData('res')
