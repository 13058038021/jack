#coding:utf-8

#遍历字符串
a="ABCDEFG"

for i in (a):
    print(i)

#排序
a=[1,3,2,6,9,4]
a.sort()
print(a)
#去重遍历打印
list=[1,2,3,4,7,7,8,3,5,6,7,6]
new_list=[]

for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)

#翻转list
def Reverse(lst):
    lst.reverse()
    return lst


lst = [11, 11, 12, 13, 14, 15]
print(Reverse(lst))

#翻转字符串
s = '1234'
print(s[::-1])

#算出 n的累计的积
def sum_cycle(n):
    sum = 1
    for i in range(1,n+1) :
        sum =sum*i
        print(sum)
sum_cycle(5)