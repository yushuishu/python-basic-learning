import math


def test(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        temp = p * (p - a) * (p - b) * (p - c)
        s = math.sqrt(temp)
        print("可以构成三角形", "面积为: ", s)
    else:
        print("三边不能构成三角形！！")


while True:
    if __name__ == '__main__':
        x = float(input("请输入第一条边："))
        y = float(input("请输入第二条边："))
        z = float(input("请输入第三条边:"))
        print(test(x, y, z))
