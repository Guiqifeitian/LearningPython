#定义函数，n=2表示默认为2
def power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

print(power(5))
print(power(4,3))

#默认参数必须指向不变对象，不能直接指向list等可变对象，必须稍加修改
def add_append(L=None):
	if L is None:
		L=[]
	L.append('END')
	return L
	
print(add_append())
print(add_append())
print(add_append())

#可变参数，可以用list或者tuple
def  calc(numbers):
	sum=0
	for n in numbers:
		sum =sum+n*n
	return sum
	
print(calc([2,3,4,5,6,7]))
print(calc((1,2,3,4)))

# 在参数前加*，表示可变参数
def cal(*numbers):
	sum=0
	for n in numbers:
		sum =sum+n*n
	return sum
	
print(cal(3,34,5,5,5,5))
nums=[3,4,5]
print(cal(*nums))

#可变参数允许你传入0个或任意个参数，
#这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含
#参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name,age,**kw):
	print('name',name,'age',age,'other',kw)

person('Gary',13)
other={'height':170}
person('Gary',13,height='170')
person('Gary',13,height=other['height'])
person('Gary',13,**other)

#参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
	
print(f1(1, 2))
print(f1(1, 2, c=3))
print(f1(1, 2, 3, 'a', 'b'))
print(f2(1, 2, d=99, ext=None))