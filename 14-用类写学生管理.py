# 学生类
class Student:
    def __init__(self, id, name, age):
        self.stuId = id
        self.name = name
        self.age = age

    def studentoop(self):
        pass

    # 全局变量
    new_id = ""
    new_name = ""
    new_age = ""


# 管理系统类
class Sys:
    def __init__(self):
        pass

    # 展示系统菜单
    def show_menu(self):
        print("=" * 56)
        print("-------------学生管理系统------------")
        print("1:添加用户信息")
        print("2:查询用户信息")
        print("3:修改用户信息")
        print("4:删除用户信息")
        print("5:显示用户信息")
        print("6:退出系统")
        print("=" * 56)

    # 输入学生菜单
    def getinfo(self):
        global new_id
        global new_name
        global new_age
        new_id = input("请输入学号:")
        new_name = input("请输入名字:")
        new_age = input("请输入年龄:")

    # 添加学生信息
    def add_stus(self):
        # 调用getinfo方法
        self.getinfo()
        # 以ID为Key,将新输入的信息赋值给Student类
        Student[new_id] = Student(new_id, new_name, new_age)
        # 打印添加的学生信息
        print("ID:%s" % Student[new_id].stuId, "Name:%s" % Student[new_id].name, "Age:%s" % Student[new_id].age)

    # 查询
    def find_stus(self):
        find_nameId = input("请输入要查的学号")
        if find_nameId in Student.keys():
            print("学号:%s\t名字:%s\t年龄:%s" % (Student[new_id].stuId, Student[new_id].name, Student[new_id].age))
        else:
            print("查无此人")

    # 修改
    def alter_stus(self):
        alterId = input("请输入你要修改学生的学号:")
        self.getinfo()
        # 当字典中Key相同时，覆盖掉以前的key值
        if alterId in Student.keys():
            Student[new_id] = Student(new_id, new_name, new_age)
            del Student[alterId]
        else:
            print("查无此人")

    # 删除学生信息
    def del_stus(self):
        cut_nameID = input("请输入要删除的学号:")
        if cut_nameID in Student.keys():
            del Student[cut_nameID]
        else:
            print("查无此人")

    # 显示学生信息
    def show_stus(self):
        for new_stuId in Student:
            # print("%s\t%s\t%s" % ("ID:%s"%new_stuId,"Name:%s"%new_name,"Age:%s"%new_age))
            print("ID:%s" % Student[new_stuId].stuId, "Name:%s" % Student[new_stuId].name, "Age:%s" % Student[new_stuId].age)

    # 退出系统
    def exit_stus(self):
        print("欢迎下次使用")
        exit()


# 创建系统对象
sys = Sys()
# 定义一个容器来存储学生信息
students = {}
while True:
    sys.show_menu()
    choice = int(input("请选择功能:"))
    if choice == 1:
        sys.add_stus()
    elif choice == 2:
        sys.find_stus()
    elif choice == 3:
        sys.alter_stus()
    elif choice == 4:
        sys.del_stus()
    elif choice == 5:
        sys.show_stus()
    elif choice == 6:
        sys.exit_stus()
    else:
        print("您输入有误，请重新输入")
