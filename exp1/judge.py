age = input('input your age: ')
age = int(age)                      #进行显示转换
if age >= 18:
    print('your age is', age)
    print('adult')
elif age>=16:
    print('your age is', age)
    print('teenager')
else:
    print('your age is', age)
    print('child')