# -*- coding: utf-8 -*-
"""
@Time ：2023-04-05 10:50
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""


class Student:
    stId: None
    name: None
    age: None
    score: None

    # 构造函数
    def __init__(self, stId, name, age):
        self.stId = stId
        self.name = name
        self.age = age

    # 打印toString
    def __str__(self):
        return f"学生信息：id：{self.stId} 姓名：{self.name}  年龄：{self.age}"

    # 支持   大于、小于
    # 不支持 大于等于、小于等于
    def __lt__(self, other):
        return self.age < other.age

    # 大于等于、小于等于
    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age


stu1 = Student(1, "张三", 20)
stu2 = Student(2, "李四", 20)
# 如果没有实现  __str__ 不能打印字符串
print(stu1)
print(stu2)
# 如果没有实现  __lt__  不能使用 >  或 <
print(stu1 < stu2)
# 如果没有实现  __le__  不能使用 >=  或 <=
print(stu1 <= stu2)
# 如果没有实现  __eq__  判断的是地址
print(stu1 == stu2)
print(stu1.score)