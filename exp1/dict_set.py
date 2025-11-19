d = {'Michael':95,'Tomori':98,'Gypsophila':96}
print(d['Michael'])
if 'Tom' in d:
    print("yes")
else:
    print('no')
s = d.get('Admin')
print(s)
d.pop('Michael')
print(d)
#dict的key必须是不可变对象
#dict的key必须是不可变对象