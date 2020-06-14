import os
import time
# print(__file__)
# d=os.path.realpath(__file__)#获取当前文件位置
# print(d)
#
# filepath=os.path.dirname(d)#获取当前文件夹名称
# print(filepath)
#
# filename=os.path.basename(d)#获取当前文件名称
# print(filename)
#
# resultpath=os.path.join(filepath,"report.html")#获取报告

path="C:\\Users\\jack\\Desktop\\qiangge"
path2="C:\\Users\\jack\\Desktop\\qiangge\\qiange"
a=os.path.exists(path)
print(a)
if not a:
    os.mkdir(path)
fp=open(path+'.txt','w')
w=fp.write("121323")

time.sleep(3)

a=os.path.exists(path)
if a == True:#判断a路径是否存在，存在则删除
    os.removedirs(path)




