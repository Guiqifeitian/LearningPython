#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数
#reduce把结果继续和序列的下一个元素做累积计算
#效果如下reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x,y):
	return x+y

from functools import reduce	
print(reduce(add,[1,2,3,4,5,6,7,8,9,0]))

#把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x,y):
	return x*10+y
	
print(reduce(fn,[1,2,3,4,5]))