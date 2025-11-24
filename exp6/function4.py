def calc(number):
    sum = 0
    for n in number:
        sum = sum + n
    return sum

def calc2(*numbers):           #可变参数
    sum2 = 0
    for a in numbers:
        sum2 = sum2 + a
    return sum2

b = calc([1, 2, 3, 4, 5])
c = calc2(1, 2, 3, 4, 5)
print(b)
print(c)
