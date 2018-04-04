def inc(x):
    def incx(y):
        return x + y

    return incx


# 函数柯里化
# 使用inc函数来构造各种版本的inc函数
# 1. 把函数当做变量来使用，关注描述问题而不是怎么实现，这样让让代码更易读
# 2. 因为函数返回里面的函数，所以函数关注的是表达式，关注的是描述这个问题，而不是怎么实现这个事情
inc1 = inc(2)
inc2 = inc(5)
print(inc1(2))
print(inc2(5))
