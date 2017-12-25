listNum = [0,5,4,2,1]
import time
from random import randrange

# 0(nSquared)
def findMin(alist):
    overallmin = alist[0]
    for i in alist:
        for j in alist:
            if i > j:
                break
            else:
                overallmin = i
    return overallmin

# linear
def findMin(alist):
    minsofar = alist[0]
    for i in alist:
        if i < minsofar:
            minsofar = i
    return minsofar
findMin(listNum)

for listSize in range(1000,10001,1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMin(alist))
    end = time.time()
    print("size: %d time: %f" % (listSize, end-start))