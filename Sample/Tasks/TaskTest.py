from Core.NetWork import VisitorWays
from Task.Task import Task
class WebTask(Task):
    def init(self):
        self.delayTimes = 5
        self.webUrl = "https://cn.pornhub.com/video/search"
        self.wayUrls = ['xpath:////*[@id = "videoSearchResult" ]/ *[ @ class = "pcVideoListItem js-pop videoblock videoBox"]/div/div/span/a']
        self.visitoryWay = VisitorWays.GET
        self.visitData={'search':'中文音声','page':3}
        # self.visitHeader= {'cookie':'ua=8866308252d63f9bf74b74e606896148; platform=pc; bs=c2nlqkhy63vgx0y0avl4cbfgodnt7ajd; ss=280145308362155656; fg_fcf2e67d6468e8e1072596aead761f2b=76241.100000; _ga=GA1.2.495535536.1641795883; _gid=GA1.2.109650310.1641795883; d_uidb=62872155-7d37-a059-0a17-d6098e9dd09e; d_uid=62872155-7d37-a059-0a17-d6098e9dd09e; atatusScript=hide; d_fs=1; RNKEY=1791679*2595899:1364564708:1290284587:1; _gat=1'}


    def execute(self):
        for result in self.resultData:
            for ky in result:
                print(ky.get('href'),ky.get('title'))
if __name__ == '__main__':
    task = WebTask()
    task.init()
    task.surf()
    task.anlyse()
    task.execute()