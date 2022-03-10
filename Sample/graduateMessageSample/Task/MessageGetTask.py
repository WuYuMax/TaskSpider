from Task.NetworkTask import NetworkTask, VisitConfig
from Task.Task import Task
from Task.TaskMessage import TaskMessage
from requests import Session
from Sample.graduateMessageSample.Task.BaseMessageTask import BaseMessageTask
from Sample.graduateMessageSample.Task.GoToMessagePageTask import GoToMessagePageTask
from Sample.graduateMessageSample.Task.PageSearchTask import PageSearchTask
import copy

class MessageGetTask(NetworkTask):
    def __init__(self):
        self.baseUrl = 'https://yz.chsi.com.cn/'
        self.paramsUrl = 'Xpath:////*[@class=\'zsml-summary\']'
        self.fwUrl = 'Xpath:////*[@class=\'zsml-res-items\']/tr'


    def init(self, message: TaskMessage) -> VisitConfig:
        subUrl = message.getData('dataurls')['url']
        weburl = self.baseUrl +subUrl

        self.session = Session()
        if not message.getData('session'):
            self.session = message.getData('session')
        self.message = message

        return VisitConfig.Builder()\
            .addWayUrl(self.paramsUrl)\
            .addWayUrl(self.fwUrl)\
            .setWebUrl(weburl)\
            .setSession(self.session)\
            .getWay()\
            .setDelayTime(0.5)\
            .setVisitHeader(dict())\
            .build()

    def execute(self, visitResult) -> TaskMessage:
        table = visitResult[0]
        res =[]
        basetable = {}
        basetable['school_name'] = table[0].text
        basetable['way'] = table[1].text
        basetable['xy'] = table[2].text
        basetable['zy'] = table[3].text
        basetable['xz'] = table[4].text
        basetable['fx'] = table[5].text
        basetable['tearcher'] = table[6].text
        basetable['numOfPeople'] = table[7].text

        for line in visitResult[1]:
            temp = copy.deepcopy(basetable)

            values = line.findall('td')
            temp['zz'] = values[0].text.strip()
            temp['wy'] = values[1].text.strip()
            temp['z1'] = values[2].text.strip()
            temp['z2'] = values[3].text.strip()
            res.append(temp)

        self.message.setData('res',res)
        return self.message



if __name__ == '__main__':
        message = TaskMessage()
        message = BaseMessageTask().run(message)
        # print(message.getData('ss'))
        pageno = 0
        # message.setData('ssname','北京市')
        message.setData('mlname', 'zyxw')
        message.setData('zyname', '电子信息')
        message.setData('pageno', pageno)
        message.setData('morePage', True)
        # print(message.getDic())

        while message.getData('morePage'):
            pageno += 1
            message.setData('pageno', pageno)
            PageSearchTask().run(message)
            urls = message.getData('urls')
            tempurls = urls[0]
            message.setData('urls', tempurls)
            GoToMessagePageTask().run(message)

            dataurl = message.getData('dataurls')[0]
            print(message.getData('dataurls'))
            message.setData('dataurls',dataurl)
            message = MessageGetTask().run(message)
            print(message.getData('res'))


            break
            # print(message.getData('urls'),message.getData('pageno'))
            message.removeData('urls')