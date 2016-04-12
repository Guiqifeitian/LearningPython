#getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
	def __init__(self):
		self.x=9
		
obj=MyObject()

print(hasattr(obj,'x'))
print(hasattr(obj,'y'))
setattr(obj,'y',19)
print(hasattr(obj,'y'))
getattr(obj,'y')
print(obj.y)