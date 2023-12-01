def test_func(func):
    def res(x, y):
        print("参数 x={0},参数 y={1}".format(x, y))
        return func(x, y)
    return res


def add(x, y):
    return x + y


def diff(x, y):
    return x - y


# 返回 res 函数
fun = test_func(diff)
# 执行 res 函数并返回 diff 执行的结果：diff 在 res中被使用
print(fun(10, 5))
# 执行 add 返回结果
print("{0}+{1}={2}".format(2, 3, add(2, 3)))
# 执行 diff 返回结果
print("{0}-{1}={2}".format(7, 2, diff(7, 2)))
