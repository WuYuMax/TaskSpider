from Task.NetworkTask import NetworkTask, VisitConfig
from Task.TaskMessage import TaskMessage
from requests import Session
from Sample.graduateMessageSample.Task.BaseMessageTask import  BaseMessageTask

class PageSearchTask(NetworkTask):
    def __init__(self):
        self.weburl = 'https://yz.chsi.com.cn/zsml/queryAction.do'
        self.valueurl = 'Xpath:////*[@class=\"ch-table\"]/tbody/tr/td/form/a'
        self.nextpageurl = 'Xpath:////*[contains(@class,\"unable\") and not(contains(@class,\"lip-first\"))]'
        # self.wayurl = 'NONE://'
        self.Header = {}

    def init(self, message: TaskMessage) -> VisitConfig:
        self.message = message
        builder = VisitConfig.Builder()

        if not message.getData('session') :
            self.session = Session()
        else:
            self.session = message.getData('session')

        ss  =  message.getData('ssname')
        ml  = message.getData('mlname')
        zy  = message.getData('zyname')

        # print(message.getData('ss'))
        if ss :
            ss = message.getData('ss')[ss]
        if ml and ml is not 'zyxw':
            ml = message.getData('ml')[ml]
        if zy :
            zy = message.getData('zy')[zy]
        xxfs = 1
        page = message.getData('pageno')

        visitData = {}
        visitData['ssdm'] = ss
        visitData['dwmc'] = ''
        visitData['mldm'] = ml
        visitData['mlmc'] = ''
        visitData['yjxkdm'] = zy
        visitData['xxfs'] = xxfs
        visitData['pageno'] = page
        # print(visitData)

        config = builder.setSession(self.session).\
            addWayUrl(self.valueurl).\
            addWayUrl(self.nextpageurl).\
            setWebUrl(self.weburl).\
            setVisitData(visitData).\
            setVisitHeader(self.Header).\
            setDelayTime(0).\
            getWay().\
            setDelayTime(0.5).\
            build()
        # print(config.visitData,config.visitHeader)
        return config

    def execute(self, visitResult) -> TaskMessage:
        links =[]
        # print(visitResult[1])
        for line in visitResult[0]:
            # print(line.get('href'),line.text)
            k_v = {}
            k_v['name'] = line.text
            k_v['url'] = line.get('href')
            links.append(k_v)

        if len(visitResult[1]) == 0:
            self.message.setData('morePage',True)
        else:
            self.message.setData('morePage',False)

        self.message.setData('urls',links)
        self.message.setData('session',self.session)

        return self.message


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
        message = PageSearchTask().run(message)
        print(message.getData('urls'),message.getData('pageno'))
        message.removeData('urls')

