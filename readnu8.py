#读取非utf8文本文件
#读取gbk文件
f=open('gbk.txt','r',encoding='gb2312')
print(f.read())
f.close()
