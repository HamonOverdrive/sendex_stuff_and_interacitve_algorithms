from timeit import Timer

def build_dict(n): # build dict = { 0:"0", 1:"1", 2:"2", ... n:"n" }
	return {i: str(i) for i in range(n)}

def getx(x,n):
	x.get(n) == str(0) # finds beginning of dict
	x.get(n) == str(n//2) # finds halfway of dict
	x.get(n) == str(n-1) # find last item of dict
	x.get(n) == str("a") # finds nothing in the dict

def setx(x,n):
	x.__setitem__('foo', 'bar')
	x.__setitem__('d', 'ff')
	x.__setitem__('ee', 'v')
	x.__setitem__('snake', 'eater')



timeDict = Timer(
	"getx(x,n)", # timing this
	"from __main__ import n, build_dict, getx; x = build_dict(n)") # setup

timeSet = Timer(
	"setx(x,n)", # timing this
	"from __main__ import n, build_dict, setx; x = build_dict(n)") # setup

print("N", "\t", "Dict", "\t", "Set") # print headers
for size in range(1000, 100000+1, 5000): # sizes to graph for n:
	n = size # copy size to __main__ module variable n
	dict_sect = timeDict.repeat(5,5)
	setd_sect = timeDict.repeat(5, 5)
	print(n, "\t", min(dict_sect), "\t", min(setd_sect))

