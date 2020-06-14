#这是一个抽奖的方法，根据用户输入的开奖数量，利用random随机函数进行for循环最后得出随机数字
import random

b=int(input())

for i in range(b):
    a=random.randint(0,100)
    print(a)