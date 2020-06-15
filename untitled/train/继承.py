#coding:utf-8

class suanfa(object):
    def add(self):
        return 1+2
    def chufa(self):
        return 9/2
    def chengfa(self):
        return 3*5

class jianfa(suanfa):
    def jianfa (self,a,b):
        return a-b







if __name__=="__main__":
    a=jianfa()
    b=a.add()
    c=a.jianfa(6,3)
    d=a.chengfa()
    print(d)





