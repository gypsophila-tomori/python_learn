import math
def my_abs(x):
    if not isinstance(x, (int ,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def nop():          #空函数
    pass        

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y -step * math.sin(angle)
    return nx, ny

def power(x, n = 2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s

def enroll(name, gender, age = 6, city = 'Xi An'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
