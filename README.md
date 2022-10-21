# TaskSipder
---
    本项目是一个轻量爬虫任务框架，本框架的目的是用更低的代码成本书写爬虫代码，它更加符合OOP(面向对象)的思路，让我们的代码在大型任务之中更加的简洁。
    在本项目中我们首先封装了项目中常用的访问，解析功能保证了我们只需要对于每个任务完成基本的配置就可完成一个比较基础的爬虫任务。并且我保留了每个Task节点的独立性，让Task本身只保留处理数据的功能，让整个爬虫任务作为一个DAO层来处理，将任务间逻辑判断部分交由用户自己处理，可以更加便捷的使用。
    下面我们将对于基本对外接口进行介绍：
### 安装说明
你可以使用pip直接安装之后使用其中的Task包与Core包

**指令**
 ```
 pip install TaskSpider	
 ```
### API介绍
#### Task包
1. Task
	本部分将作为任务处理的基本容器我们可以在非网络任务中继承这个基本类。这个基本类只提供了run(message:TaskMessage)->TaskMessage一个接口用于处理数据。
	ps: 虽然可以在execute中可以修改Message但我们还是建议将修改后的message返回以保持各个Task运行的一致性。
2. NetWorkTask
	1. NetWorkTask
		本模块为处理网络任务的基本容器在本模块中我们封装了一个爬虫的基本内容，我们完成了四个方法，其中需要用户覆盖的方法有二：
		1. init(TaskMessage)->VisitConfig
			从传进来的数据块中提取出访问需要的Config并返回。
		2. execute(Response,message)->TaskMessage
			从解析完成的数据中提取需要写回的内容并且返回写完的数据块,message为你需要求改的message。
			ps: Reponse返回的是一个解析URL列表返回的结果列表。
			pps: 虽然可以在execute中可以修改Message但我们还是建议将修改后的message返回以保持各个Task运行的一致性。
		
	2. VisitConfig
		内含访问需要的内容。
		
		|        变量名        |    含义     |            备注             |
		| :------------------: | :---------: | :-------------------------: |
		|        webUrl        |   访问URL   |  输入host或者加上参数均可   |
		|    wayUrls:list()    | 解析URL列表 | 格式： 解析方式://解析参数  |
		| visitWay:VisitorWays |  访问方式   | 一个含有Post和Get的枚举类型 |
		|      visitData       |  访问数据   |      访问时携带的参数       |
		|     visitHeader      |  访问头部   |            可空             |
		|      delaytime       |  延迟时间   |     在访问后延迟的时间      |
		|       Session        |  访问会话   |                             |
		
		ps：wayUrl注释
		
		wayUrl目前支持四种解析方式
		
		| 方式名称(大小写不敏感) | 解析参数              | 例子                                      |
		| :--------------------: | --------------------- | ----------------------------------------- |
		|         REGEX          | 正则表达式            | regex://a/b0                              |
		|         XPATH          | xpath解析式           | Xpath:////*[@class=\'zsml-res-items\']/tr |
		|          DOM           | dom中的selector解析式 | dom://#_next > div._21bLU4._3kbg6I        |
		|          JSON          | 选择json的项目(可选)             | JSON://data/cards/desc/user_profile/info/uname                                   |
		|     NONE(指不解析)     | 无需参数              | None://                                   |
		
		pps:也可以使用Core.URLS.WayUrlBuider构建
		
	3. VisitConfigBuider
	  内部含有创建访问VisitConfig的方法，提供链式调用。
	
	  **创建NetWorkTask范例**
	
	  ```
	  class SSTask(NetworkTask):
	      def __init__(self):
	          super().__init__()
	          
	          #赋值基础常量 访问URL与解析URL
	          self.visitUrl = "https://yz.chsi.com.cn/zsml/pages/getSs.jsp"
	          self.wayUrl = "JSON://none"
	  
	      def init(self, message: TaskMessage) -> VisitConfig:
	          builder = VisitConfig.Builder()
	          visitconfig =builder.setWebUrl(self.visUrl)\
	              .postWay()\
	              .addWayUrl(self.wayUrl)\
	              .setDelayTime(0)\
	              .setVisitData(dict())\
	              .setVisitHeader(dict())\
	              .build()
	          self.message = message
	          return visitconfig
	  
	  
	      def execute(self, visitResult) -> TaskMessage:
	  
	          res = {}
	  
	          for k_v in visitResult[0]:
	              res[k_v['mc']] = k_v['dm']
	          self.message.setData(key='ss',value=res)
	          return self.message
	  ```
	
3. BigTask
	本模块提供帮助我们对于可以并行执行的同Task完成并行效果。
	
	```python
	def __init__(self,task:Task,paramsName:str,orderName:str,numOfThread:int=8):
	```
	
	task: 需要并行的任务；
	
	paramsName:message中哪个属性是需要拆分到每个并行任务中的；其中我们推荐将子任务需要的message信息组成一个字典列表来完成并行。
	
	orderName:Task完成后我们将Task返回的message中的数据统一写回的最终的message中orderName属性中，默认会生成一个字典列表。
	
	numOfThread:任务中线程池中的线程个数。
	
4. TaskMessage

   本模块用于为每一个Task提供参数并且为其写入参数以便捷Service层的书写。

   def getData(key:str,value:object)

   def setData(key)

   def removeData(key:str)

   本模块主要用于承载数据以后将更新其他的Api

5. TaskManger

   目标为让多个任务完成并行，使我们可以完成多任务之间的并行策略。

   暂未完成
