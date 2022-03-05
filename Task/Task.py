from Core.NetWork import visit
from Core.NetWork import VisitorWays
from Core import  Anlyst
from Core.URLs import WayUrl
from Core.URLs import WebUrl
from abc import abstractmethod
import time
from requests import Session

class Task:
    def run(self)->list:
      pass