
# 用于解析网页的URL对象
class WebUrl:
    host = str()
    params = dict()
    # str转化为WebUrl
    @staticmethod
    def parse(url:str):
        produce = WebUrl()
        HostAndParams = url.split("?")
        produce.host = HostAndParams[0]
        # print(HostAndParams)
        if len(HostAndParams)>1 and len(HostAndParams[1]) >1 :
            # HostAndParams[0] += '?'
            ParamsOfStr = HostAndParams[1]
            Params = ParamsOfStr.split('&')
            for content in Params:
                KeyAndValue = content.split('=')
                produce.params[KeyAndValue[0]] = KeyAndValue[1]
        return produce
    # 利用构造器
    class WebUrlBuilder:
        def __init__(self):
            self.produce = WebUrl()
        def addHost(self,host:str):
            self.produce.host = host
            return self
        def addParam(self,key:str,value:str):
            self.produce.params[key] = value
            return self
        def removeParam(self,key:str):
            self.produce.params.pop(key)
            return self
        def build(self):
            return self.produce

    def __str__(self):
        currentUrl = self.host
        if len(self.params.keys()) :
            currentUrl += '?'
        for i,currentkey in enumerate(self.params.keys()):
            currentUrl += currentkey
            currentUrl += '='
            currentUrl += str(self.params[currentkey])

            isLastOne = i != len(self.params) - 1
            if isLastOne:
                currentUrl += '&'
        return currentUrl



# 解析URL用于动态界定解析手段与位置
class WayUrl:
    currentItemNum:int = 0
    separator:str = "/"
    ways = list()
    model = str()

    # 建立空白方法URL
    def __init__(self):
        self.model = ""
        self.ways = []

    # 利用字符串构造"解析URL"
    @staticmethod
    def parse(url:str):
        produce = WayUrl()
        ModelAndWays = url.split("://")
        produce.model = ModelAndWays[0]

        WaysOfStr = ModelAndWays[1]
        produce.ways = WaysOfStr.split(WayUrl.separator)
        # print(produce.ways)

        return produce

    # 直接构造解析URL
    @staticmethod
    def create(model:str,ways:list):

        produce = WayUrl()
        produce.model = model
        produce.ways = ways
        return produce

    # WayUrl的构造器
    class WayUrlBuilder:
        def __init__(self):
            print('create New WayUrl')
            self.produce = WayUrl()
            print(self.produce.ways)

        def addModel(self, model: str):
            self.produce.model = model
            return self

        def addWays(self, ways: str):
            self.produce.ways.append(ways)
            return self

        def build(self):
            return self.produce

    # 获取解析方法
    def getModel(self):
        return self.model
    #获取整体方法
    def getWay(self):
        resWay = ""

        self.SeekTo(0)

        currentWays = self.NextWay()
        while currentWays is not None:
            resWay += currentWays
            currentWays = self.NextWay()
            if currentWays is not None:
                resWay += self.separator

        self.SeekTo(0)
        return resWay

    # 返回当前子标签的信息
    def NextWay(self):
        isOverFlow:bool = self.currentItemNum >= len(self.ways)
        if not isOverFlow:
            res = self.ways[self.currentItemNum]
            self.currentItemNum +=1
            return res
        else:
            return None

    # 调整当前位置
    def SeekTo(self,item:int):
        self.currentItemNum = item

    # 返回解析URL
    def __str__(self):
        currentUrl = self.getModel() + "://"

        # 遍历URL的各级标签
        currentWays = self.NextWay()
        while currentWays is not None:
            currentUrl += currentWays
            currentWays = self.NextWay()
            if currentWays is not None:
                currentUrl += self.separator

        return currentUrl
