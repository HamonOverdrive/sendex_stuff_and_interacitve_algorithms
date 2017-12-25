from timeit import Timer
import random

# possible hint is https://stackoverflow.com/questions/44144828/given-a-list-of-numbers-in-random-order-write-an-algorithm-that-works-in-onlog

my_list = [5,33,2,59,7,8,9,77,4,66,0,56]
k = 3

x = sorted(my_list)

print(x)
print(x[k-1])
