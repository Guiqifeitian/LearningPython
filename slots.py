class Student(object):
	__slots__=('name','age')#ֻ只准动态绑定name，age
	
s=Student()
s.name='Gary'	
s.age=23
#s.score=99绑定失败
print(s.name)
print(s.age)

#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class Puil(Student):
	pass
	
p=Puil()
p.score=99
print(p.score)