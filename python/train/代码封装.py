#coding:utf-8
from selenium import webdriver
#初始化方法
class Fengzhuang():
    def __init__(self):
        self.dirver=self.dirver
    def setUp(self):
        self.dirver=webdriver.Chrome()

#静态方法,静态方法不能有self，静态方法不需要实例化
class Jingtaifangfa():
    @staticmethod
    def add():
        return 1+2
    @staticmethod
    def acc():
        return 4-1

#私有方法,方法前加两个下划线,私有属性，属性前面加两个下划线
class Siyoufangfa():

    def __getName(self,a=0,b=0):
        self.__name=22
        return a+b
    def getAge(self):
        age=18
        return age



if __name__=="__main__":
    print(Jingtaifangfa.add())#静态方法不需要实例化
    a=Siyoufangfa()
    a.getAge()
