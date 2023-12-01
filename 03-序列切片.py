"""
序列：
内容连续，有序，可以使用下标索引的 容器
列表，元组，字符串 都可以被称为 序列


切片：
表示从序列中，从指定位置，按照步长依次取出元素，到指定位置，得到一个新序列
格式：序列[起始下标 : 结束下标 : 步长]
包含起始下标数据，不包含结束下标数据

PS：切片得到新的序列，不影响原原序列
"""

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 步长默认1,
result1 = my_list[1: 4]
print(f"result1结果：{result1}")

my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# 默认全部
result2 = my_tuple[:]
print(f"结果2：{result2}")

string = "0123456789x"
# 步长2
result3 = string[::2]
print(f"结果3：{result3}")

# 序列翻转
result4 = string[::-1]
print(f"结果4：{result4}")

result5 = string[3:1:-1]
print(f"结果5：{result5}")

result6 = string[1:]
print(f"结果6：{result6}")
