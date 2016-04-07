#g=(x*x for x in range(10))
#print(g)
#next基本不用，用for循环
"""
print(next(g))
print(next(g))
print(next(g))
"""

#斐波那契额数列
"""
def fib(max):
	n,a,b=0,0,1
	while n< max:
		print(b)
		a,b=b,a+b
		n=n+1
	return 'done'
	
print(fib(13))
"""
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
#在执行过程中，遇到yield就中断，下次又继续执行
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(7):
	print(n)