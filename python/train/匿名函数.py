#conding :utf-8

#匿名函数,没有名字，比较方便
a=(lambda x,y,z:x+y+z)(1,2,3)
print(a)

#匿名函数遍历1-10所有数
squares1 = list(map(lambda x: x, range(1,11)))
print(squares1)
#匿名函数遍历1-10的所有数，每个数分别乘以3
squares2 = list(map(lambda x: x +3, range(1,11)))
print(squares2)


#for循环遍历
for i in range(1,10):
    print(i+5)