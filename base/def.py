def func(x,*arg):
    print(x)
    result = x
    print(arg)
    for i in arg:
        result += i
    return result


print(func(1,2,3,4,5,6,7,8,9))

# def foo(**kargs):
#     print(kargs)
# foo(a=1,b=2,c=3)


def foo(x,y,z,*args,**kwargs):
    print(x)
    print(y)
    print(z)
    print(args)
    print(kwargs)


foo(1, 2, 3, 4, 5, name="qiwsir")

g = lambda x,y:x+y
print(g(3,4))

# add = lambda x:x+3


def add(x):
    return x+3


numbers = [0,1,2,3,4,5,6]
print(list(map(add,numbers)))

lst = range(1,6)
r = 0
for i in lst:
    r += i
print(r)

a = [3,9,4,5]
b = [3,3,2,1]
print(sum(x*y for x,y in zip(a,b)))

c = range(-5,5)
print(list(filter(lambda x:x>0,c)))
print([x for x in c if x > 0])



