import re
import os


filename = ("students.txt")
def main():
    ctrl = True
    while ctrl:
        menu()
        option = input("请选择：")
        option_str = re.sub("\D","",option)
        if option_str in ["0","1","2","3","4","5","6","7",]:
            option_int = int(option_str)
            if option_int == 0: # 退出
                print("您已退出学身信息管理系统")
                ctrl = False
            elif option_int == 1:   # 录入学生信息
                insert()
            elif option_int == 2:   # 查找学生信息
                search()
            elif option_int == 3:   # 删除学生信息
                delete() 
            elif option_int == 4:   # 修改学生信息
                modify()
            elif option_int == 5:   # 成绩排序
                sort()
            elif option_int == 6:   # 统计学生人数
                total()
            elif option_int == 7:   # 显示所有学生信息
                show()
# 主菜单
def menu():
    print("""
    ╔——————————————————————学生信息管理系统————————————————————————╗
    
       =======================功能菜单============================
                                                                 
       1.录入学生信息                                             
       2.查找学生信息
       3.删除学生信息
       4.修改学生信息
       5.排序
       6.统计学生总人数
       7.显示所有学生信息
       0.退出系统
       ======================功能菜单=======================     
       说明：通过数字或↑↓方向键选择菜单
    ╚——————————————————————学生信息管理系统————————————————————————╝
    """)

# 录入学生信息
def insert():
    studentList = []
    mark = True
    while mark:
        id = input("请输入ID(如 1001)：")
        if not id:
            break
        name = input("请输入姓名：")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩"))
            chinese = int(input("请输入语文成绩"))
            math = int(input("请输入数学成绩"))
            biology = int(input("请输入生物成绩"))
            physical = int(input("请输入物理成绩"))
            chemistry = int(input("请输入化学成绩"))
        except:
            print("请重新输入")
        student = {
            "id":id,
            "name":name,
            "english":english,
            "chinese":chinese,
            "math":math,
            "biology":biology,
            "physical":physical,
            "chemistry":chemistry,
        }
        studentList.append(student)
        inputMark = input("是否继续添加y/n：")
        if inputMark == "y":
            mark = True
        else:
            mark = False
    save(studentList)
    print("学生信息录入完成")

# 查找学生信息
def search():
    mark = True
    student_query = []  # 保存查询结果
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename):
            mode = input("1.按ID查询；2.按姓名查询")
            if mode == "1":
                id = input("请输入学生ID：")
            elif mode == "2":
                name = input("请输入学生姓名：")
            else:
                print("您输入有误，请重新输入")
                search()
            with open (filename,"r") as f:
                student = f.readlines()
                for list in student:
                    d = dict(eval(list))
                    if d is not "":
                        if d["id"] == id:
                            student_query.append(d)
                    if name is not "":
                        if d["name"] == name:
                            student_query.append(d)

                show_student(student_query)
                student_query.clear()
                inputMark = input("是否继续查询(y/n)：")
                if inputMark == "y":
                    mark = True
                else:
                    mark = False
        else:
            print("暂未保存数据信息")
            return

# 删除学生信息
def delete():
    mark = True
    while mark:
        studentId = input("请输入学生ID：")
        if studentId is not "":
            if os.path.exists(filename):
                with open(filename,"r",encoding="utf-6") as f:
                    student_old = f.readlines() # 读取全部内容
            else:
                student_old = []
        ifdel = False   # 标记是否删除
        if student_old:
            with open(filename,"w",encoding="utf-8") as f:
                d = {}
                for list in student_old:
                    d = dict(eval(list))
                    if d["id"] != studentId:
                        f.write(str(d)+"\n")
                    else:
                        ifdel = True
                if ifdel:
                    print(f"{studentId}信息已删除")
                else:
                    print(f"{studentId}学生信息未找到")
        else:
            print("无学生信息")
            break
        show()
        inputMark = input("是否继续删除y/n：")
        if inputMark == "y":
            mark = True
        else:
            mark = False

# 修改学生信息
def modify():
    show()
    if os.path.exists(filename):
        with open(filename,"r") as f:
            student_old = f.readlines()
    else:
        return
    studentid = input("请输入要修改的学生id：")
    with open(filename,"w") as f:
        for student in student_old:
            d = dict(eval(student))
            if d["id"] == studentid:
                print("找到该学生信息，可以修改\n")
                while True:
                    try:
                        d["name"] = input("请输入姓名")
                        d["english"] = input("请输入英语成绩")
                        d["math"] = input("请输入英语成绩")
                        d["chinese"] = input("请输入英语成绩")
                        d["biology"] = input("请输入生物成绩")
                        d["physical"] = input("请输入物理成绩")
                        d["chemistry"] = input("请输入化学成绩")
                    except:
                        print("输入有误，请重新输入")
                    else:
                        break
                student = str(d)    # 将字典转为字符串
                f.write(student+"\n")
                print("修改成功")
            else:
                f.write(student)    # 将没有的信息添加到文件
    mark = input("是否继续修改学生信息(y/n)：")
    if mark == "y":
        modify()

def sort():
    show()
    if os.path.exists(filename):
        with open(filename,"r",encoding="utf-8") as f:
            student_new = []
            student_old = f.readlines()
            for list in student_old:
                d = dict(eval(list))
                student_new.append(d)
    else:
        return
    ascORdesc = input("请选择（0升序、1降序）")
    if ascORdesc == "0":
        ascORdescBool = False
    elif ascORdesc == "1":
        ascORdescBool = True
    else:
        print("您输入有误")
        sort()
    mode = input("请选择排序方式（1.英语成绩；2.语文成绩；3.数学成绩；4.生物成绩；5.物理成绩；6.化学成绩；0.总成绩成绩；）")
    if mode == "1":
        student_new.sort(key=lambda x:x["english"],reverse=ascORdescBool)
    elif mode == "2":
        student_new.sort(key=lambda x:x["chinese"],reverse=ascORdescBool)
    elif mode == "3":
        student_new.sort(key=lambda x:x["math"],reverse=ascORdescBool) 
    elif mode == "4":
        student_new.sort(key=lambda x:x["biology"],reverse=ascORdescBool) 
    elif mode == "5":
        student_new.sort(key=lambda x:x["physical"],reverse=ascORdescBool) 
    elif mode == "6":
        student_new.sort(key=lambda x:x["chemistry"],reverse=ascORdescBool)
    elif mode == "0":
        student_new.sort(key=lambda x:x["chemistry"]+x["english"]+x["chinese"]+x["math"]+x["biology"]+x["physical"]
        ,reverse=ascORdescBool) 
    else:
        print("输入有误，请重新输入")
        sort()
    show_student(student_new)
# 统计学生人数
def total():
    if os.path.exists(filename):
        with open (filename,"r",encoding="utf-8") as f:
            student_old = f.readlines()
            if student_old:
                print(f"一共有{len(student_old)}名学生")
            else:
                print("未录入学生信息")
    else:
        print("暂未保存数据信息")


# 显示所有学生信息
def show():
    student_new = []
    if os.path.exists(filename):
        with open(filename,"r",encoding="utf-8") as f:
            student_old = f.readlines()
            for list in student_old:
                student_new.append(eval(list))
                if student_new:
                    show_student(student_new)
                else:
                    print("暂未保存信息")



# 文件存储
def save(student):
    try:
        student_txt = open(filename,"a",encoding="utf-8")
    except Exception as e:
        student_txt = open(filename,"w",encoding="utf-8")
    for info in student:
        student_txt.write(str(info)+"\n") 
    student_txt.close()

# 显示存在列表中的信息
def show_student(studentList):
    if not studentList:
        print("没有数据")
        return
    format_title = "{:^6}{:^4}\t{:^4}\t{:^4}\t{:^4}\t{:^4}\t{:^4}\t{:^4}\t{:^4}"
    print(format_title.format("ID","名字","英语成绩","语文成绩","数学成绩","生物成绩","物理成绩","化学成绩","总成绩"))
    format_data = "{:^6}{:^4}\t{:^4}\t{:^4}\t{:^4}\t{:^4}\t{:^4}\t{:^4}\t{:^4}"
    for info in studentList:
        print(format_data.format(info.get("id"),
        info.get("name"),
        str(info.get("english")),str(info.get("chinese")),str(info.get("math")),
        str(info.get("biology")),str(info.get("physical")),str(info.get("chemistry")),
        str(info.get("english")+info.get("chinese")+info.get("math")+info.get("biology")
        +info.get("physical")+info.get("chemistry"))
        ))
if __name__ == '__main__':
    main()  