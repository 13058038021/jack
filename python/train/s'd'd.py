#算出 n的累计的积,比如(n=5 ,1*2*3*4*5=120)

# sum = 1
# for i in range(1,6) : #i=3
#     ji =sum*i
#     print(ji)

def sum_cycle(n):
    sum = 1
    for i in range(1,n) :
        sum =sum*i
        print(sum)
sum_cycle(5)

