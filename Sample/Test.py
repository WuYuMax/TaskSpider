from Sample.GraduateMessageSpider.Tasks.SearchingTask import SearchingTask
from Task.TaskManger import TaskManger
init_message = \
    {
        "ssdm":'',
        "dwmc":'',
        "mldm":'zyxw',
        "mlmc":'',
        "yjxkdm":1251,
        "zymc":"",
        "xxfs":"",
        "pageno":2
    }

if __name__ == '__main__':
    searchingtask = SearchingTask(init_message)
    taskmanger  = TaskManger()
    taskmanger.register(searchingtask)
    taskmanger.start()
    taskmanger.jion()



