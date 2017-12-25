from timeit import Timer


def build_list(n): # create list of 1 to n
    # print('building list for n', n)
    return list(range(n))

def build_dict(n): # build dict = { 0:"0",1:"1", 2:"2", .... n:"n" }
    # print('building dict for n', n)
    return {i: str(i) for i in range(n)}

def delx(x,n):
    # print('removing item', 0)
    del x[0]
    # print('removing item', n//2)
    del x[n//2]
    # print('removing item', 0)
    del x[0]

def delx_dict(x,n):
    # print(x)
    # print('removing item', 0)
    del x[0]
    # print('removing item', n//2)
    del x[n//2]
    # print('removing item', n-1)
    del x[n-1]

timeList = Timer(
    "delx(x,n)", # time this
    "from __main__ import n, build_list, delx; x = build_list(n)") # setup

timeDict = Timer(
    "delx_dict(x,n)", # time this
    "from __main__ import n, build_dict, delx_dict; x = build_dict(n)") # setup

# print min of 5 runs of 5
print("N", "\t", "List", "\t", "Dict")
for size in range(1000, 100000+1, 5000): # sizes to graph for n:
    # print('size', size)
    n = size # copy size to __main__ module variable n
    # print('calling timelist repeat')
    list_secs = timeList.repeat(5,1)
    # print('calling timedict repeat')
    dict_sect = timeDict.repeat(5,1)
    print(n, "\t", min(list_secs), "\t", min(dict_sect))

# Based on the data it seems like del for the list is O(n) while dict is O(1)