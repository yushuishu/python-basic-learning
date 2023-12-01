# -*- coding: utf-8 -*-
"""
@Time ：2023-04-05 11:19
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from typing import Union

# 基础数据
a: int = 10
b: str = "xxx"
c: bool = False


# 类对象
class Teacher:
    pass


tea: Teacher = Teacher()

# 容器
my_list: list = [1, 2, 3]
my_tuple: tuple = (4, "python", True)
my_dict: dict = {"name": "张三"}
# 容器详细注解
my_list2: list[int] = [1, 2, 3]
my_tuple2: tuple[int, str, bool] = (4, "python", True)
my_dict2: dict[str, int] = {"age": 18}

# 使用注释，进行类型注解
# type: int
my_list3: list = [1, 2, 3]
# type: int, str, bool
my_tuple3: tuple = (4, "python", True)
# type: str, int
my_dict3: dict = {"age": 18}


# 函数
def add(x: int, y: int):
    print(x + y)


# 光标放到括号内部，Ctrl + p 提示
add(1, 2)

# 混合类型 Union：from typing import Union
my_list4: list[Union[int, str]] = [1, "xyz"]


def func(data: Union[int, str]):
    print(f"data: {data}")

