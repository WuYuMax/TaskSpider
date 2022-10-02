from Helper.DownLoad.DownLoadFileTask import DownLoadFileTask,TaskMessage


if __name__ == '__main__':
    message = TaskMessage()
    downLoad={}
    downLoad['DownLoadUrl'] = 'https://b2.szjal.cn/20190322/WUcZPxSt/index.m3u8'
    downLoad['OrderDirPath'] ='.'
    message.setData('DownLoad',downLoad)


    downloadFileTask = DownLoadFileTask()
    downloadFileTask.run(message)