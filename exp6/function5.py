def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(3))
#局部变量为组合数据类型并且未在函数内部创建，等同于全局变量
ls = ['f','F']
def func(a, b):
    ls.append(b)
    return a*b

s = func("knock ~ ", 2)
print(s)