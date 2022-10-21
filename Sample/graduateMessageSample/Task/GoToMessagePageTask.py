from Task.NetworkTask import NetworkTask, VisitConfig
from Task.TaskMessage import TaskMessage
from Task.Task import Task
from Sample.graduateMessageSample.Task.BaseMessageTask import BaseMessageTask
from Sample.graduateMessageSample.Task.PageSearchTask import PageSearchTask
from Task.BigTask import BigTask
from requests import Session
from Core.URLs import WebUrl




class GoToSingleMessagePageTask(NetworkTask):
    def __init__(self):
        self.baseUrl = 'https://yz.chsi.com.cn'
        self.wayurl ='Xpath:////*[@class=\"ch-table more-content\"]/tbody/tr/td[8]/a'
        self.hasnext = 'Xpath:////*[contains(@class,\"unable\") and not(contains(@class,\"lip-first\"))]'
        # self.wayurl = 'NONE://'



    def init(self, message: TaskMessage) -> VisitConfig:
        params = message.getDic()
        suburl = params['url']
        weburl = self.baseUrl + suburl
        weburl:WebUrl = WebUrl.parse(weburl)
        weburl.params['pageno'] = message.getData('pageno')


        if not message.getData('session') :
            self.session = Session()
        else:
            self.session = message.getData('session')

        return VisitConfig.Builder()\
            .addWayUrl('value',self.wayurl)\
            .addWayUrl('hasnext',self.hasnext)\
            .setWebUrl(weburl)\
            .setDelayTime(0.5)\
            .setVisitData(None)\
            .getWay()\
            .setSession(self.session)\
            .build()

    def execute(self, visitResult,message:TaskMessage) -> TaskMessage:
        # print(visitResult)
        res = []
        for value in visitResult.get('value'):
            t = {}
            t['url'] = value.get('href')
            res.append(t)

        message.setData('dataurls',res)

        if len(visitResult.get('hasnext')) == 0:
            message.setData('hasnextpage',True)
        else:
            message.setData('len',len(visitResult.get('hasnext')))
            message.setData('hasnextpage',False)


        return message

class GoToMessagePageTask(Task):

    def run(self, message: TaskMessage) -> TaskMessage:
        pageno = 1
        message.setData('hasnextpage',True)
        res = []

        while message.getData('hasnextpage'):

            message.setData('pageno',pageno)
            message = GoToSingleMessagePageTask().run(message)
            res.extend(message.getData('dataurls'))
            pageno += 1
        message.setData('dataurls',res)
        return message


if __name__ == '__main__':
    message = TaskMessage()
    message = BaseMessageTask().run(message)
    # print(message.getData('ss'))
    pageno = 0
    # message.setData('ssname','北京市')
    message.setData('mlname','zyxw')
    message.setData('zyname','电子信息')
    message.setData('pageno',pageno)
    message.setData('morePage',True)
    # print(message.getDic())

    while message.getData('morePage'):
        pageno += 1
        message.setData('pageno', pageno)
        PageSearchTask().run(message)
        urls = message.getData('urls')
        tempurls = urls[0]
        message.setData('urls',tempurls)
        GoToMessagePageTask().run(message)

        print(message.getData('dataurls'))
        break
        # print(message.getData('urls'),message.getData('pageno'))
        message.removeData('urls')
