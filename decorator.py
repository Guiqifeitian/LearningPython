#函数对象有一个__name__属性
f=abs
print(f.__name__)

def log(func):
	def wrapper(*args,**kw):
		print('call %s()'%func.__name__)
		return func(*args,**kw)
	return wrapper

@log
def now():
	print('2016-4-7')
	
now()
#now=log(now)

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
	
@log('execute')
def then():
	print('Hello')
	
then()