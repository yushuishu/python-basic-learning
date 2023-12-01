"""
python中，json和dict非常类似，都是key-value的形式，而且json和dict也可以非常方便的通过dumps和loads互转，但是它们之间还是有区别的：
json：是一种数据格式，是纯字符串。可以被解析成python的dict或其他形式。
dict：是一个完整的数据结构，是对hash table这一数据结构的实现，是一套从存储到提取都封装好的方案。
      它使用内置的hash函数来规划key对应的value的存储位置，从而获得O(1)的数据读取速度。

json和dict对比：
1）json的key只能是字符串，dict的key可以是任何可hash的对象，例如：字符串、数字、元组等。
2）json的key可以是有序、重复的；dict的key不可重复；
3）json的value只能是字符串、浮点数、布尔值或者null,或者它们构成的数组或者对象；
4）json任意key存在默认值undefined,dict默认没有默认值；
5）json访问方式可以是[],也可以是.,遍历方式分in，of； dict的value仅仅可以下标访问；
6）json的字符串强制用双引号，dict的字符串可以用单引号、双引号；
7）dict可以嵌套tuple,json里只有数组
8）json：true、false、null
9）dict：True、False、None
10）json中文必须是unicode编码，如“\u6211”
11）json的类型时字符串，字典的类型是dict
"""

# 字典的key以是任何可hash的对象，例如：字符串、数字、元组等。
my_dict = {"张三": 80, 100: 50, True: False}
print(f"my_dict类型：{type(my_dict)}")
print(f"key：100，value：{my_dict[100]}")

# 嵌套
my_dict2 = {
    "张三": {
        "语文": 80,
        "数学": 100,
        "英语": 90
    },
    "李四": {
        "语文": 90,
        "数学": 99,
        "英语": 80
    }
}
print(f"my_dict2类型：{type(my_dict2)}")
print(f"my_dict2数据：{my_dict2}")

# 新增
my_dict2["王五"] = {"语文": 60, "数学": 50, "英语": 75}
print(f"my_dict2新增元素：{my_dict2}")

# 更新
my_dict2["张三"]["英语"] = 70
print(f"my_dict2更新元素：{my_dict2}")

# 删除
my_dict2.pop("王五")
print(f"my_dict2移除元素：{my_dict2}")

# 获取全部key
keys = my_dict2.keys()
print(f"获取全部key：{keys}")

# 遍历字典
print("")
for key in keys:
    print(f"字典的key：{key} ，值是：{my_dict2[key]}")
print()

# 统计字典内的元素数量
print(f"字典的元素数量：{len(my_dict2)}")

# 清空
my_dict2.clear()
print(f"my_dict2清空元素后的内容：{my_dict2}")

