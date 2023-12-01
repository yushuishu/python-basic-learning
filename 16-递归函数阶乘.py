def test(num):
    if num > 1:
        return num * test(num - 1)
    else:
        return 1


if __name__ == '__main__':
    n = int(input("请输入一个正整数："))
    if n >= 0:
        print("运算结果：{0}!={1}".format(n, test(n)))
    else:
        print("无效输入！")
