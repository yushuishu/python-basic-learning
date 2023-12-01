"""
是否支持下标索引
    支持（序列类型）: 列表、元组、字符串、
    不支持（非序列类型）：集合、字典

是否支持重复元素
    支持（序列类型）：列表、元组、字符串
    不支持（非序列类型）：集合、字典

是否可以修改
    支持：列表、集合、字典
    不支持：元组、字符串
"""
my_list = [1, 2, 3, 4, 5, 9, 8, 7, 6]
my_tuple = (1, 2, 3, 4, 5, 9, 8, 7, 6)
my_string = "123459876"
my_set = {1, 2, 3, 4, 5, 9, 8, 7, 6}
my_dict = {"name": "张三", "age": 18, "enable": True}

for index, item in my_list:
    print(f"{index}  {item}")

# len 数量
print(f"my_list 元素个数有：{len(my_list)}")
print(f"my_tuple 元素个数有：{len(my_tuple)}")
print(f"my_string 元素个数有：{len(my_string)}")
print(f"my_set 元素个数有：{len(my_set)}")
print(f"my_dict 元素个数有：{len(my_dict)}")
print()

# max 最大
print(f"my_list 最大元素：{max(my_list)}")
print(f"my_tuple 最大元素：{max(my_tuple)}")
print(f"my_string 最大元素：{max(my_string)}")
print(f"my_set 最大元素：{max(my_set)}")
print(f"my_dict 最大元素：{max(my_dict)}")
print()

# min 最小
print(f"my_list 最小元素：{min(my_list)}")
print(f"my_tuple 最小元素：{min(my_tuple)}")
print(f"my_string 最小元素：{min(my_string)}")
print(f"my_set 最小元素：{min(my_set)}")
print(f"my_dict 最小元素：{min(my_dict)}")
print()

# 类型转换：容器转列表
print(f"列表 转 列表：{list(my_list)}")
print(f"元组 转 列表：{list(my_tuple)}")
print(f"字符串 转 列表：{list(my_string)}")
print(f"集合 转 列表：{list(my_set)}")
print(f"字典 转 列表：{list(my_dict)}")
print()

# 类型转换：容器转元组
print(f"列表 转 元组：{tuple(my_list)}")
print(f"元组 转 元组：{tuple(my_tuple)}")
print(f"字符串 转 元组：{tuple(my_string)}")
print(f"集合 转 元组：{tuple(my_set)}")
print(f"字典 转 元组：{tuple(my_dict)}")
print()

# 类型转换：容器转字符串
print(f"列表 转 字符串：{str(my_list)}")
print(f"元组 转字符串：{str(my_tuple)}")
print(f"字符串 转 字符串：{str(my_string)}")
print(f"集合 转 字符串：{str(my_set)}")
print(f"字典 转 字符串：{str(my_dict)}")
print()

# 类型转换：容器转集合
print(f"列表 转 集合：{set(my_list)}")
print(f"元组 转 集合：{set(my_tuple)}")
print(f"字符串 转 集合：{set(my_string)}")
print(f"集合 转 集合：{set(my_set)}")
print(f"字典 转 集合：{set(my_dict)}")
print()

# 排序(升序) : 排序结果都会变列表对象
print(f"列表排序：{sorted(my_list)}")
print(f"元组排序：{sorted(my_tuple)}")
print(f"字符串排序：{sorted(my_string)}")
print(f"集合排序：{sorted(my_set)}")
print(f"字典排序：{sorted(my_dict)}")
print()

# 排序(降序)
print(f"列表排序（降序）：{sorted(my_list, reverse=True)}")
print(f"元组排序（降序）：{sorted(my_tuple, reverse=True)}")
print(f"字符串排序（降序）：{sorted(my_string, reverse=True)}")
print(f"集合排序（降序）：{sorted(my_set, reverse=True)}")
print(f"字典排序（降序）：{sorted(my_dict, reverse=True)}")
print()

