from Task.Task import  Task
from Core.NetWork import VisitorWays
import time
from Core.Writer import CSVWriter
from Core.Writer import Writer

xpath = "//*[@id=\"app\"]/div[3]/div[1]/div[2]/ul"
# //*[@id="app"]/div[3]/div[1]/div[2]/ul/li[1]/div/p[1]/a/span
# //*[@id="app"]/div[3]/div[1]/div[2]/ul/li[1]/div/p[1]/a/span
class FindCourseTask(Task):

    def init(self):
        self.webUrl = "https://bangumi.bilibili.com/api/timeline_v2_global?"
        self.wayUrls.append("JSON://")
        self.visitoryWay = VisitorWays.GET
        self.visitHeader["cookie"]="buvid3=D6474868-6DC4-4A41-A632-CAE869232F0C143109infoc; blackside_state=1; rpdid=|(u|JlRkRukm0J'uY|R~l)J|m; fingerprint=8f479522926f719a9ccb2445d8db973d; buvid_fp=D6474868-6DC4-4A41-A632-CAE869232F0C143109infoc; buvid_fp_plain=71089BAA-82E5-49CC-9181-1F018EF17051143089infoc; CURRENT_QUALITY=112; _uuid=847357AD-A101B-241E-61108-85FD10A9D39F1009583infoc; CURRENT_FNVAL=2000; PVID=1; b_lsid=2DE3141F_17E327453B1; arrange=matrix"
        self.visitHeader["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
        self.visitHeader["sec-fetch-dest"]="windows"
        self.delayTimes = 10
    def execute(self):
        # print(self.response.text)
        mywriter:Writer = CSVWriter("../result.csv", 'wb')
        res = self.resultData[0]['result']
        # print(res)

        for value in res:
            if value['is_finish'] == 1:
                mywriter.write((value['title'],value['lastupdate_at']))
                # print(value['title'],value['lastupdate_at'])
            else :
                mywriter.write((value['title'],'还未开播'))
                # print(value['title'],"还未开播")
        pass
    def createNextTask(self):
        return self

if __name__ == '__main__':
    task:Task = FindCourseTask()
    # task.delayTimes
    tasklist = list()
    tasklist.append(task)
    TTL = 100

    while len(tasklist) != 0 and TTL !=0 :
        currenttask = tasklist.pop()
        print(currenttask)
        currenttask.init()
        currenttask.surf()
        currenttask.anlyse()
        currenttask.execute()
        currenttask.delay()
        nexttask = currenttask.createNextTask()
        if nexttask != None:
            tasklist.append(nexttask)
            TTL -= 1
        # time.sleep(600)


