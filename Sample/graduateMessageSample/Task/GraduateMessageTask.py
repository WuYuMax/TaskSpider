from Task.Task import Task
from Task.TaskMessage import TaskMessage
from Sample.graduateMessageSample.Task.BaseMessageTask import BaseMessageTask
from Sample.graduateMessageSample.Task.WBTask import WBTask
from Sample.graduateMessageSample.Task.MessageGetTask import MessageGetTask
from Sample.graduateMessageSample.Task.GoToMessagePageTask import GoToMessagePageTask
from Sample.graduateMessageSample.Task.PageSearchTask import PageSearchTask
from Task.BigTask import BigTask

class GraduateMessageTask(Task):

    def __init__(self,filepath,ss,ml,zy):
        self.filepath = filepath
        self.ss = ss
        self.ml = ml
        self.zy = zy
    def __messageInit(self,message:TaskMessage):
        message = BaseMessageTask().run(message)
        message.setData('ssname', self.ss)
        message.setData('mlname', self.ml)
        message.setData('zyname', self.zy)
        message.setData('pageno', 0)
        message.setData('morePage', True)
        return message

    def run(self, message: TaskMessage) -> TaskMessage:

        print('=' * 10 + 'Task Start ' + '=' * 10)
        pageno = 0
        # 信息初始化
        print('='*10+' 信息初始化中 '+'='*10)
        message = self.__messageInit(message)
        wbtask = WBTask(self.filepath)

        while message.getData('morePage'):
            # 翻页
            pageno += 1
            message.setData('pageno', pageno)
            # 开始查询
            print('=' * 10 + ' Page No.{} start '.format(str(pageno)) + '=' * 10)

            # 查找当前页面
            message = PageSearchTask().run(message)
            # 翻找每个页面中的每个学院
            BigTask(GoToMessagePageTask(), 'urls', 'dataurls').run(message)
            # 从每个学院信息中提取信息
            BigTask(MessageGetTask(), 'dataurls', 'res').run(message)
            # 写回信息
            wbtask.run(message)

            # 一页结束
            print('=' * 10 + ' Page No.{} over '.format(str(pageno)) + '=' * 10)


            # 回收内存
            message.removeData('urls')
            message.removeData('dataurls')
            message.removeData('res')

        print('=' * 10 + 'Task End ' + '=' * 10)

        return message