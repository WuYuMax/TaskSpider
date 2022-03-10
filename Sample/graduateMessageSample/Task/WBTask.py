from Task.Task import Task
from Task.TaskMessage import TaskMessage
from Core.Writer import CSVWriter

class WBTask(Task):
    def __init__(self,path:str):
        self.writer = CSVWriter(path,'a+')
        self.res_title = ['招生单位','考试方式'
            ,'院系所','专业','学习方式','研究方向','指导老师','拟招人数'
                     ,'政治','外语','业务课一','业务课二'
                     ]

    def run(self, message: TaskMessage) -> TaskMessage:
        values = message.getData('res')
        self.writer.writeTitle(self.res_title)
        for value in values:
            res = []
            for line in value.keys():
                res.append(value[line])
            self.writer.write(res)

        return message