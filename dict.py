#dict集合，类似于java中的map,注意dict是用花括号，tuple使用小括号，list使用中括号,set是小括号包中括号
d={'Gary':21,'Lina':23,'Linux':22}
print(d['Gary'])
d['Thomas']=23
print('Thomas' in d)
d.pop('Lina')
print('Lina' in d)