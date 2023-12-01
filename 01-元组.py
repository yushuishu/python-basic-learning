"""
元组内容不可修改，但是元组中嵌套的的 list的内容可以修改
"""

# 定义简单的元组
t1 = (1, "python", "java", True)
t2 = ()
t3 = tuple()
print(f"t1类型：{type(t1)}， 内容是：{t1}")
print(f"t2类型：{type(t2)}， 内容是：{t2}")
print(f"t3类型：{type(t3)}， 内容是：{t3}")
# 定义单个元素 （单个元素的元组，后面必须逗号结尾 ,）
t4 = ("python", )
print(f"t4类型：{type(t4)}， 内容是：{t4}")
# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5类型：{type(t5)}，内容是：{t5}")
# 下标索引取元素
print(f"取t5：{t5[1][2]}")
# index查找
t6 = ("hello world", "python", "java", True)
index = t6.index("java")
print(f"t6 index查找内容：{index}")
# count 统计
t7 = ("golang", "python", "java", "java", "java")
num7 = t7.count('java')
print(f"count 统计: {num7}")
# 长度
print(f"t7元组长度：{len(t7)}")
