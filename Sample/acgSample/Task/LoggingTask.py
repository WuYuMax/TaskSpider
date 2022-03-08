from Task.NetworkTask import NetworkTask, VisitConfig
from Task.TaskMessage import TaskMessage


class LoggingTask(NetworkTask):
    def __init__(self):
        super().__init__()
        self.visUrl = "https://bbs.yuanacg.com/member.php"
        self.wayUrl = "NONE://none"

    def init(self, message: TaskMessage) -> VisitConfig:
        visitData = {}
        visitData['mod'] = 'logging'
        builder = VisitConfig.Builder()
        visitconfig =builder.setWebUrl(self.visUrl)\
            .postWay()\
            .addWayUrl(self.wayUrl)\
            .setDelayTime(1)\
            .setVisitData()\
            .setVisitHeader()\
            .build()
        return visitconfig


    def execute(self, visitResult) -> TaskMessage:
        pass