#例如n=5  1*2*3*4*5=120

# x=5
#
# def func1(x):
#     if x==1:
#         return 1
#     return x * func1(x-1)
#
# print(func1(x))


def jiecheng(n=5):
    if n==1:
        return 1
    else:
        return n*jiecheng(n-1)
        print(jiecheng)
#print(jiecheng)


#
# def sum_cycle(n):
#     sum = 1
#     for i in range(1,n+1) :
#         sum =sum*i
#         print(sum)
#
# sum_cycle(10)


a=[1,3,2,6,9,4]
a.sort()
print(a)