from Task.NetworkTask import NetworkTask, VisitConfig
from Task.TaskMessage import TaskMessage
from requests import Session
import json

class testNetWorkTest(NetworkTask):
    def __init__(self):
        print('='*10,'__init__','='*10)
        self.baseUrl = 'https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/unlogin_dynamics?hot_offset=0'
        self.UserURL = 'JSON://data/cards/desc/user_profile/info/uname'
        self.ContentUrl = 'JSON://data/cards/card'

    def init(self, message: TaskMessage) -> VisitConfig:
        print('=' * 10, 'init', '=' * 10)
        session = Session()
        return VisitConfig.\
            Builder().\
            addWayUrl('content',self.ContentUrl).\
            addWayUrl('user',self.UserURL).\
            setWebUrl(self.baseUrl). \
            getWay().\
            setSession(session).\
            setEncoding('utf-8').\
            build()

    def execute(self, visitResult:dict) -> TaskMessage:
        print('=' * 10, 'execute', '=' * 10)
        content = visitResult.get('content')
        usernames = visitResult.get('user')

        # print(usernames)
        temp = []
        for i in range(len(usernames)):
            username = usernames[i]
            _ = content[i]
            current =json.loads(_)
            # print(current)
            t = current.get('item').get('description')
            temp.append({'name':username,'content':t})
        print(temp)

def NetworkTest():
    message = TaskMessage()
    task = testNetWorkTest()
    message = task.run(message)


print('sss')
NetworkTest()
print('end')