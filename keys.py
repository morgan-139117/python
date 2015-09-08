d = {}
d["1"] = "one"
d["2"] = "two"
d["3"] = "three"
d["4"] = "four"

del d["3"]

for key,value in d.items():
	print "%s --> %s" % (key,value)

l = [1,2,3]
print l

t = tuple(l)

print t

l1 = list(t)

print l1

lists = [[]] * 3

listdeep = [[],[1],[]]

listdeeper =[[] for i in range(3) ]


print lists

lists[0].append(2)

listdeep[2].append(2)

listdeeper[2].append(2)


print lists

print 'deep',listdeep

print 'deep',listdeeper



