def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


while True:
    if __name__ == '__main__':
        # 根据 eval的特性,可以让输入的字符 转变为数字
        print("====================================================")
        m = input('请输入：')
        n = eval(input('请输入：'))
        print(type(m))
        print(type(n))
        print("=====================================================")
        a = eval(input("请输入第一个数字："))
        b = eval(input("请输入第二个数字："))
        print("加:", add(a, b), "减:", subtract(a, b), "乘:", multiply(a, b), "除:", divide(a, b))
