from Helper.DownLoad.DownLoadFileTask import DownLoadFileTask,TaskMessage


if __name__ == '__main__':
    message = TaskMessage()
    message.setData('DownLoadUrl','https://b2.szjal.cn/20190322/WUcZPxSt/index.m3u8')
    message.setData('OrderDirPath','.')
    message.setData('FileName','index.m3u8')

    downloadFileTask = DownLoadFileTask()
    downloadFileTask.run(message)