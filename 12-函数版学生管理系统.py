"""
打印菜单 print_menu
添加     add_message
查询     select_message
修改     modify_message
删除     delete_message
"""


def print_menu():
    print('''
     学生信息管理系统
     1-添加学生信息
     2-查询学生信息
     3-修改学生信息
     4-删除学生信息
    ''')


# 添加函数
def add_message():
    name = input('请输入学生姓名:')
    age = input('请输入学生年龄:')
    sex = input('请输入学生性别:')
    score = input('请输入学生成绩:')
    # 保存一个人的信息
    stu_dict = {'name': name, 'age': age, 'sex': sex, 'score': score}
    all_stu.append(stu_dict)
    print(all_stu)


# 查询函数
def select_message():
    print('''1.查询单个信息 2.查询所有信息''')
    select = input('请输入你需要的选项')
    if select == '1':
        stu_id = int(input('请输入你要查询的学生编号'))
        student = all_stu[stu_id - 1]
        print('编号  姓名  年龄  性别  成绩')
        print('{}    {}    {}    {}   {}'.format(stu_id, student['name'], student['age'], student['sex'], student['score']))
    elif select == '2':
        print('编号  姓名  年龄  性别  成绩')
        for index, student in enumerate(all_stu):
            print('{}    {}    {}    {}   {}'.format(index, student['name'], student['age'], student['sex'], student['score']))


# 修改函数
def modify_message():
    stu_id = int(input('请输入要修改的学生编号:'))
    student = all_stu[stu_id - 1]
    new_name = input('请输入修改后的学生姓名:')
    new_age = input('请输入修改后的学生年龄:')
    new_sex = input('请输入修改后的学生性别:')
    new_score = input('请输入修改后的学生成绩:')
    student['name'] = new_name
    student['age'] = new_age
    student['sex'] = new_sex
    student['score'] = new_score
    print('修改完毕')


def delete_message():
    """
    删除函数
    :return:
    """
    print('''1-删除一个学生信息 2-删除所有学生信息''')
    select = input('请输入选项;')
    if select == '1':
        stu_id = int(input('请输入要删除的学生编号'))
        del all_stu[stu_id - 1]
    elif select == '2':
        all_stu.clear()
    else:
        print('请输入有效选项')


all_stu = []
while True:
    # 打印菜单
    print_menu()
    select = input('请输入选项:')
    if select == '1':
        add_message()
    elif select == '2':
        select_message()
    elif select == '3':
        modify_message()
    elif select == '4':
        delete_message()
    elif select == 'Q':
        break
    else:
        print('请输入有效选项')
