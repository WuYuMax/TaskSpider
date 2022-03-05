from Sample.GraduateMessageSpider.Tasks.SearchingTask import SearchingTask
from Task.BigTask import BigTask




taskList = list()
if __name__ == '__main__':
    for i in range(1,15):
        current_message = init_message = \
    {
        "ssdm":'',
        "dwmc":'',
        "mldm":'zyxw',
        "mlmc":'',
        "yjxkdm":1251,
        "zymc":"",
        "xxfs":"",
        "pageno":1
    }
        page = i
        current_message['pageno'] = page
        task = SearchingTask(current_message)
        taskList.append(task)
    task = BigTask(taskList)

    res = task.run()
    print(res)
