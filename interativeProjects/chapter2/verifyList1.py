import timeit
import random

l = [3,45,2,1,4,5,23,4,56]
# creates index for list picks random


for i in range(10000, 1000001, 20000):
	index = random.randint(0, len(l) - 1)
	t = timeit.Timer("l[index]", "from __main__ import l, index")
	lst_time = t.timeit(number=1000)

	print("%d,%10.3f" % (i, lst_time))
