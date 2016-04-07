#高阶函数将函数作为返回值
def cal(*args):
	def su():
		i=0
		for x in args:
			i=i+x
		print(i)
		return i
	return su
	
f=cal(1,2,3,4,5,8,78,99)
#f()