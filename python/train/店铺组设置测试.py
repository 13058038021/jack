#coding:utf-8
from common.login import LoginBelle

class fuqin(object):
    def fang(self):
        print("房子")
    def chezi(self):
        print("车子")

class erzi(fuqin):
    def nvpeng(self):
        print("女朋友")
    def fang(self):
        print("房子")
        print("庄园")

if __name__=="__main__":
    a=erzi()
    a.chezi()
    a.fang()
    a.nvpeng()


