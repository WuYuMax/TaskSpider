from Task.DefinedTask import DenfinedTask
from Core.NetWork import VisitorWays
from requests import Session

class SearchingTask(DenfinedTask):
    __isFinish:bool = True

    def __init__(self,message:dict,session:Session=None):
        super().__init__()
        self.visitData = message
        self.Session = session
        # self.resultData = list()
        # self.response = None
        # self.delayTimes = 1

    def init(self):
        self.webUrl = 'https://yz.chsi.com.cn/zsml/queryAction.do#'
        self.wayUrls = ['xpath:////*[@id="form3"]/a','xpath:////*[@class ="lip unable "]']
        self.visitoryWay = VisitorWays.POST
        # print(self.visitData)
        self.visitHeader['Cookie']=  'JSESSIONID=F0313E47BFC33EB7023FF5B390A70DCF; zg_did=%7B%22did%22%3A%20%22175a325eff2ba-0fbf63495c84d7-230346d-144000-175a325eff35f5%22%7D; _ga=GA1.3.1289928378.1604759974; CHSIDSTID=17c061f21bd1f9-0d2e98676d1ce-a7d193d-144000-17c061f21be389; zg_14e129856fe4458eb91a735923550aa6=%7B%22sid%22%3A%201633878634409%2C%22updated%22%3A%201633878636554%2C%22info%22%3A%201633878634416%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fwww.chsi.com.cn%2F%22%7D; zg_0d76434d9bb94abfaa16e1d5a3d82b52=%7B%22sid%22%3A%201633878637053%2C%22updated%22%3A%201633878678591%2C%22info%22%3A%201633878637059%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.chsi.com.cn%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fmy.chsi.com.cn%2Farchive%2Findex.jsp%22%2C%22cuid%22%3A%20%22e296692d1fd8b344c888b69078e4772b%22%7D; zg_adfb574f9c54457db21741353c3b0aa7=%7B%22sid%22%3A%201635780530725%2C%22updated%22%3A%201635780554255%2C%22info%22%3A%201635741861301%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fyz.chsi.com.cn%2F%22%2C%22cuid%22%3A%20%22e296692d1fd8b344c888b69078e4772b%22%7D; aliyungf_tc=05fdc54558c5f40efdadc9a997ca8c6f3e9fda7ecf1ac1eca53d8ba13c98fda9; XSRF-CCKTOKEN=81a2056f34edd9fef8dddb2a3d725cba; CHSICC_CLIENTFLAGYZ=5d9a178e980046720dfb5abc37a90f32; _gid=GA1.3.233620838.1641811536; CHSICC_CLIENTFLAGZSML=8129ee05d13c6db1979256b08d7772e9; acw_tc=2f6fc11516418285930132648eae8e24253074c510318d07d976609368c084; JSESSIONID=27F01848EDE48872025396B6386F6E09'
        if self.session is None:
            self.session = Session()



    def execute(self):
        SchoolsAndUrls = self.resultData[0]
        Pages:list = self.resultData[1]
        # print("pageno =",self.visitData['pageno'])
        for schoolandUrl in SchoolsAndUrls:
            print(schoolandUrl.get('href'),schoolandUrl.text)
        if Pages.__len__() > 0 :
            self.__isFinish = False

    def createNextTask(self) -> list():
        resultList = list()
        if self.__isFinish is not False:
            # print('next pageno')
            self.visitData['pageno'] += 1
            message= self.visitData
            nextSearchingTask = SearchingTask(message,self.session)
            resultList.append(nextSearchingTask)
        # print(resultList)
        return resultList
