'''
用于存储一串请求中的全局信息
'''
class TaskMessage():
    def __init__(self):
        self.__datas = {}
    def getData(self,key:str):
        return self.__datas.get(key)
    def setData(self,key:str,value:object):
        self.__datas[key] = value
    def extend(self,datas:dict):
        for key in datas.keys():
            self.__datas[key] = datas[key]
    def getDic(self):
        return self.__datas
    def setDic(self,dic):
        self.__datas = dic
    def removeData(self,key):
        self.__datas.pop(key)
