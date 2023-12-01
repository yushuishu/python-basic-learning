def is_odd(n):
    return n % 2 == 1


# 完全平方数的筛选函数
def is_sqr(x):
    return x ** 0.5 % 1 == 0


if __name__ == '__main__':
    i = 0
    nums = [x for x in range(1, 201)]
    nums1 = filter(is_odd, nums)
    nums_list1 = list(nums1)
    print("1到200范围内的所有奇数：")
    for x in nums_list1:
        i += 1
        print("{0:<4}".format(x), end="")
        if i % 10 == 0:
            print()
    nums2 = filter(is_sqr, nums)
    nums_list2 = list(nums2)
    print("-" * 70)
    print("1到200范围内平方根是整数的数字：")
    for x in nums_list2:
        print("{0:<4}".format(x), end="")
