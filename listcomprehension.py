#列表生成器
d=[x*x for x in range(1,11)]
print(d)
e=[x*x for x in range(1,11) if x%2==0]
print(e)
h=[m+n for m in 'ABC' for n in 'XYZ']
print(h)
f={'S':'dd','L':'ff','P':'rr'}
g=[k+'='+v for k,v in f.items()]
print(g)
L=['HELLO','APPLE','IBM']
print([s.lower() for s in L])