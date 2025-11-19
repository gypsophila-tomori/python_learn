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
#Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key
print("===========I am a line==========\n")

s = {1, 2, 3, 4}
print(s)
s = {1, 1, 2, 2, 2, 3, 3}
print(s)
s.add(4)
print(s)

print("===========I am a line==========\n")

s1 = {1, 2, 3, 4}
s2 = {1, 3, 5, 6}
print(s1 & s2)