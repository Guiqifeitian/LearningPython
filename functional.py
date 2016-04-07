#变量可以是函数
"""
f=abs
print(f(-9))
"""
#传入函数
def add(x,y,f):
	return f(x)+f(y)
	
print(add(-5,5,abs))
