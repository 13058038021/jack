#coding:utf-8

#读一个文件
fp=open("C:\\Users\\jack\\Desktop\\常用的mysl命令.txt","r")
r=fp.read()
print(r)
fp.close()

#往一个文件里面写内容(会覆盖原有内容),如果没有这个文件会创建一个文件
fp=open("C:\\Users\\jack\\Desktop\\111.txt","w")
w=fp.write("哈哈")
fp.close()
#往一个文件里面追加内容
fp=open("C:\\Users\\jack\\Desktop\\111.txt","a")
a=fp.write("\nforever")
fp.close()
#二进制方法操作
fp=open("C:\\Users\\jack\\Desktop\\111.txt","rb")
rb=fp.read()
print(rb)
fp.close()