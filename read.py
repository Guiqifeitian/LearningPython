"""
try:
	f=open('hello.txt','r')
	print(f.read())
finally:
	if f:
		f.close()
"""
#r是读取文本utf8文件
with open('hello.txt','r') as f:
	for line in f.readlines():
		print(line.strip())
#	print(f.read())
#read()是一次性读取所有内容，read(size)是每次读取size字节内容，readline()是每次读取一行内容，readlines一次读取所有内容按行返回list
