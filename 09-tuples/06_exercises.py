#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
元组综合练习 - Tuple Comprehensive Exercises

本文件包含了元组相关的各种练习题，涵盖：
1. 基础练习
2. 元组操作练习
3. 元组解包练习
4. 实际应用练习
5. 高级练习
6. 综合项目练习

每个练习都包含题目描述、示例和参考答案

作者: Python学习教程
日期: 2024
"""

def exercise_1_basic_operations():
    """练习1: 基础操作"""
    print("=" * 50)
    print("练习1: 元组基础操作")
    print("=" * 50)
    
    print("题目1: 创建和访问元组")
    print("创建一个包含你最喜欢的5种水果的元组，然后：")
    print("- 打印整个元组")
    print("- 打印第一个和最后一个水果")
    print("- 打印中间三个水果")
    print("- 检查'苹果'是否在元组中")
    
    # 参考答案
    print("\n参考答案:")
    fruits = ("苹果", "香蕉", "橙子", "葡萄", "草莓")
    print(f"水果元组: {fruits}")
    print(f"第一个水果: {fruits[0]}")
    print(f"最后一个水果: {fruits[-1]}")
    print(f"中间三个水果: {fruits[1:4]}")
    print(f"'苹果'在元组中: {'苹果' in fruits}")
    
    print("\n" + "-" * 30)
    print("题目2: 元组统计")
    print("给定元组 (1, 2, 3, 2, 4, 2, 5)，计算：")
    print("- 元组长度")
    print("- 数字2出现的次数")
    print("- 数字3第一次出现的位置")
    print("- 所有元素的和")
    
    # 参考答案
    print("\n参考答案:")
    numbers = (1, 2, 3, 2, 4, 2, 5)
    print(f"原始元组: {numbers}")
    print(f"元组长度: {len(numbers)}")
    print(f"数字2出现次数: {numbers.count(2)}")
    print(f"数字3的位置: {numbers.index(3)}")
    print(f"所有元素的和: {sum(numbers)}")

def exercise_2_tuple_operations():
    """练习2: 元组操作"""
    print("\n=" * 50)
    print("练习2: 元组操作")
    print("=" * 50)
    
    print("题目1: 元组连接和重复")
    print("给定两个元组 tuple1 = (1, 2, 3) 和 tuple2 = (4, 5, 6)")
    print("- 连接两个元组")
    print("- 将第一个元组重复3次")
    print("- 创建一个新元组，包含两个元组的所有元素，但顺序相反")
    
    # 参考答案
    print("\n参考答案:")
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    
    connected = tuple1 + tuple2
    repeated = tuple1 * 3
    reversed_combined = tuple(reversed(tuple1 + tuple2))
    
    print(f"tuple1: {tuple1}")
    print(f"tuple2: {tuple2}")
    print(f"连接结果: {connected}")
    print(f"重复结果: {repeated}")
    print(f"反向连接: {reversed_combined}")
    
    print("\n" + "-" * 30)
    print("题目2: 元组比较")
    print("比较以下元组对，判断大小关系：")
    print("- (1, 2, 3) 和 (1, 2, 4)")
    print("- (1, 2) 和 (1, 2, 0)")
    print("- ('a', 'b') 和 ('a', 'c')")
    
    # 参考答案
    print("\n参考答案:")
    comparisons = [
        ((1, 2, 3), (1, 2, 4)),
        ((1, 2), (1, 2, 0)),
        (('a', 'b'), ('a', 'c'))
    ]
    
    for t1, t2 in comparisons:
        if t1 < t2:
            result = "<"
        elif t1 > t2:
            result = ">"
        else:
            result = "=="
        print(f"{t1} {result} {t2}")

def exercise_3_tuple_unpacking():
    """练习3: 元组解包"""
    print("\n=" * 50)
    print("练习3: 元组解包")
    print("=" * 50)
    
    print("题目1: 基本解包")
    print("给定学生信息元组 ('张三', 20, '计算机科学', 85.5)")
    print("使用元组解包提取姓名、年龄、专业和成绩")
    
    # 参考答案
    print("\n参考答案:")
    student_info = ('张三', 20, '计算机科学', 85.5)
    name, age, major, score = student_info
    
    print(f"学生信息: {student_info}")
    print(f"姓名: {name}")
    print(f"年龄: {age}")
    print(f"专业: {major}")
    print(f"成绩: {score}")
    
    print("\n" + "-" * 30)
    print("题目2: 星号解包")
    print("给定成绩元组 (95, 87, 92, 78, 85, 90, 88)")
    print("- 提取第一个成绩、最后一个成绩和中间所有成绩")
    print("- 提取前两个成绩和剩余成绩")
    
    # 参考答案
    print("\n参考答案:")
    scores = (95, 87, 92, 78, 85, 90, 88)
    
    first, *middle, last = scores
    print(f"成绩元组: {scores}")
    print(f"第一个成绩: {first}")
    print(f"中间成绩: {middle}")
    print(f"最后成绩: {last}")
    
    first_two, second, *rest = scores
    print(f"\n前两个成绩: {first_two}, {second}")
    print(f"剩余成绩: {rest}")
    
    print("\n" + "-" * 30)
    print("题目3: 嵌套解包")
    print("给定嵌套元组 (('北京', '上海'), ('广州', '深圳'))")
    print("解包得到四个城市名称")
    
    # 参考答案
    print("\n参考答案:")
    cities = (('北京', '上海'), ('广州', '深圳'))
    (city1, city2), (city3, city4) = cities
    
    print(f"嵌套元组: {cities}")
    print(f"城市1: {city1}")
    print(f"城市2: {city2}")
    print(f"城市3: {city3}")
    print(f"城市4: {city4}")

def exercise_4_practical_applications():
    """练习4: 实际应用"""
    print("\n=" * 50)
    print("练习4: 实际应用")
    print("=" * 50)
    
    print("题目1: 坐标计算")
    print("给定三个点的坐标: A(0,0), B(3,4), C(6,0)")
    print("- 计算AB和AC的距离")
    print("- 判断这三个点是否构成直角三角形")
    
    # 参考答案
    print("\n参考答案:")
    import math
    
    point_a = (0, 0)
    point_b = (3, 4)
    point_c = (6, 0)
    
    def distance(p1, p2):
        """计算两点间距离"""
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    ab = distance(point_a, point_b)
    ac = distance(point_a, point_c)
    bc = distance(point_b, point_c)
    
    print(f"点A: {point_a}")
    print(f"点B: {point_b}")
    print(f"点C: {point_c}")
    print(f"AB距离: {ab:.2f}")
    print(f"AC距离: {ac:.2f}")
    print(f"BC距离: {bc:.2f}")
    
    # 检查是否为直角三角形（勾股定理）
    sides = sorted([ab, ac, bc])
    is_right_triangle = abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-10
    print(f"是否为直角三角形: {is_right_triangle}")
    
    print("\n" + "-" * 30)
    print("题目2: 学生成绩管理")
    print("给定学生成绩数据：")
    print("[('Alice', 85, 92, 78), ('Bob', 90, 87, 85), ('Charlie', 78, 85, 90)]")
    print("- 计算每个学生的平均成绩")
    print("- 找出总分最高的学生")
    print("- 按平均成绩排序")
    
    # 参考答案
    print("\n参考答案:")
    students = [('Alice', 85, 92, 78), ('Bob', 90, 87, 85), ('Charlie', 78, 85, 90)]
    
    print("学生成绩分析:")
    student_stats = []
    
    for student in students:
        name, *scores = student
        total = sum(scores)
        average = total / len(scores)
        student_stats.append((name, total, average))
        print(f"{name}: 成绩{scores}, 总分{total}, 平均{average:.1f}")
    
    # 找出总分最高的学生
    best_student = max(student_stats, key=lambda x: x[1])
    print(f"\n总分最高: {best_student[0]} ({best_student[1]}分)")
    
    # 按平均成绩排序
    sorted_students = sorted(student_stats, key=lambda x: x[2], reverse=True)
    print("\n按平均成绩排序:")
    for i, (name, total, avg) in enumerate(sorted_students, 1):
        print(f"{i}. {name}: 平均{avg:.1f}分")

def exercise_5_advanced_exercises():
    """练习5: 高级练习"""
    print("\n=" * 50)
    print("练习5: 高级练习")
    print("=" * 50)
    
    print("题目1: 元组作为字典键")
    print("创建一个字典，用坐标元组作为键，存储棋盘上的棋子")
    print("- 在(0,0)放置'车'，(0,7)放置'车'")
    print("- 在(4,4)放置'王'")
    print("- 查询指定位置的棋子")
    print("- 移动棋子从一个位置到另一个位置")
    
    # 参考答案
    print("\n参考答案:")
    chessboard = {}
    
    # 放置棋子
    chessboard[(0, 0)] = '车'
    chessboard[(0, 7)] = '车'
    chessboard[(4, 4)] = '王'
    
    print("初始棋盘:")
    for pos, piece in chessboard.items():
        print(f"  位置{pos}: {piece}")
    
    # 查询位置
    query_pos = (4, 4)
    piece = chessboard.get(query_pos, '空')
    print(f"\n位置{query_pos}的棋子: {piece}")
    
    # 移动棋子
    from_pos = (4, 4)
    to_pos = (5, 5)
    
    if from_pos in chessboard:
        piece = chessboard.pop(from_pos)
        chessboard[to_pos] = piece
        print(f"\n移动棋子: {from_pos} -> {to_pos}")
    
    print("移动后棋盘:")
    for pos, piece in chessboard.items():
        print(f"  位置{pos}: {piece}")
    
    print("\n" + "-" * 30)
    print("题目2: 数据分组")
    print("给定一组点的坐标，按象限分组")
    print("点: [(1,2), (-1,3), (2,-1), (-2,-3), (0,0), (3,0)]")
    
    # 参考答案
    print("\n参考答案:")
    points = [(1, 2), (-1, 3), (2, -1), (-2, -3), (0, 0), (3, 0)]
    
    def get_quadrant(point):
        """确定点所在象限"""
        x, y = point
        if x > 0 and y > 0:
            return "第一象限"
        elif x < 0 and y > 0:
            return "第二象限"
        elif x < 0 and y < 0:
            return "第三象限"
        elif x > 0 and y < 0:
            return "第四象限"
        else:
            return "坐标轴上"
    
    # 分组
    quadrants = {}
    for point in points:
        quad = get_quadrant(point)
        if quad not in quadrants:
            quadrants[quad] = []
        quadrants[quad].append(point)
    
    print("点的分组:")
    for quad, points_in_quad in quadrants.items():
        print(f"{quad}: {points_in_quad}")

def exercise_6_comprehensive_project():
    """练习6: 综合项目"""
    print("\n=" * 50)
    print("练习6: 综合项目 - 员工管理系统")
    print("=" * 50)
    
    print("项目要求:")
    print("创建一个简单的员工管理系统，使用元组存储员工信息")
    print("员工信息格式: (ID, 姓名, 部门, 职位, 薪资)")
    print("实现以下功能:")
    print("1. 添加员工")
    print("2. 查找员工")
    print("3. 按部门分组")
    print("4. 计算部门平均薪资")
    print("5. 薪资排序")
    
    # 参考实现
    print("\n参考实现:")
    
    class EmployeeManager:
        def __init__(self):
            self.employees = []
        
        def add_employee(self, employee_tuple):
            """添加员工"""
            self.employees.append(employee_tuple)
            emp_id, name, dept, position, salary = employee_tuple
            print(f"已添加员工: {name} (ID: {emp_id})")
        
        def find_employee(self, emp_id):
            """查找员工"""
            for employee in self.employees:
                if employee[0] == emp_id:
                    return employee
            return None
        
        def group_by_department(self):
            """按部门分组"""
            departments = {}
            for employee in self.employees:
                emp_id, name, dept, position, salary = employee
                if dept not in departments:
                    departments[dept] = []
                departments[dept].append(employee)
            return departments
        
        def calculate_dept_average_salary(self):
            """计算部门平均薪资"""
            departments = self.group_by_department()
            dept_averages = {}
            
            for dept, employees in departments.items():
                total_salary = sum(emp[4] for emp in employees)
                avg_salary = total_salary / len(employees)
                dept_averages[dept] = avg_salary
            
            return dept_averages
        
        def sort_by_salary(self, reverse=True):
            """按薪资排序"""
            return sorted(self.employees, key=lambda x: x[4], reverse=reverse)
        
        def display_all_employees(self):
            """显示所有员工"""
            print("\n所有员工信息:")
            for employee in self.employees:
                emp_id, name, dept, position, salary = employee
                print(f"  ID: {emp_id}, 姓名: {name}, 部门: {dept}, 职位: {position}, 薪资: {salary}")
    
    # 使用示例
    manager = EmployeeManager()
    
    # 添加员工数据
    employees_data = [
        (1001, "张三", "技术部", "工程师", 8000),
        (1002, "李四", "销售部", "销售经理", 9000),
        (1003, "王五", "技术部", "高级工程师", 12000),
        (1004, "赵六", "人事部", "人事专员", 6000),
        (1005, "钱七", "销售部", "销售代表", 7000)
    ]
    
    for emp_data in employees_data:
        manager.add_employee(emp_data)
    
    # 显示所有员工
    manager.display_all_employees()
    
    # 查找员工
    print("\n查找员工 (ID: 1003):")
    employee = manager.find_employee(1003)
    if employee:
        emp_id, name, dept, position, salary = employee
        print(f"找到员工: {name}, 部门: {dept}, 职位: {position}, 薪资: {salary}")
    
    # 按部门分组
    print("\n按部门分组:")
    departments = manager.group_by_department()
    for dept, employees in departments.items():
        print(f"{dept}: {len(employees)}人")
        for emp in employees:
            print(f"  - {emp[1]} ({emp[3]})")
    
    # 计算部门平均薪资
    print("\n部门平均薪资:")
    dept_averages = manager.calculate_dept_average_salary()
    for dept, avg_salary in dept_averages.items():
        print(f"{dept}: {avg_salary:.0f}元")
    
    # 按薪资排序
    print("\n按薪资排序 (从高到低):")
    sorted_employees = manager.sort_by_salary()
    for i, employee in enumerate(sorted_employees, 1):
        emp_id, name, dept, position, salary = employee
        print(f"{i}. {name} ({dept}): {salary}元")

def bonus_exercises():
    """附加练习"""
    print("\n=" * 50)
    print("附加练习")
    print("=" * 50)
    
    print("练习1: 元组推导式（生成器表达式）")
    print("使用生成器表达式创建包含1-10平方数的元组")
    
    # 参考答案
    print("\n参考答案:")
    squares = tuple(x**2 for x in range(1, 11))
    print(f"平方数元组: {squares}")
    
    print("\n" + "-" * 30)
    print("练习2: 元组与函数")
    print("编写函数，接受任意数量的数字参数，返回(最小值, 最大值, 平均值)")
    
    # 参考答案
    print("\n参考答案:")
    def analyze_numbers(*numbers):
        """分析数字，返回统计信息"""
        if not numbers:
            return None
        
        min_val = min(numbers)
        max_val = max(numbers)
        avg_val = sum(numbers) / len(numbers)
        
        return (min_val, max_val, avg_val)
    
    # 测试函数
    result = analyze_numbers(10, 5, 8, 12, 3, 15, 7)
    if result:
        min_val, max_val, avg_val = result
        print(f"输入数字: 10, 5, 8, 12, 3, 15, 7")
        print(f"分析结果: 最小值={min_val}, 最大值={max_val}, 平均值={avg_val:.1f}")
    
    print("\n" + "-" * 30)
    print("练习3: 元组与文件处理")
    print("模拟CSV数据处理，将字符串数据转换为元组")
    
    # 参考答案
    print("\n参考答案:")
    csv_data = [
        "张三,25,工程师,8000",
        "李四,30,经理,12000",
        "王五,28,设计师,9000"
    ]
    
    print("原始CSV数据:")
    for line in csv_data:
        print(f"  {line}")
    
    # 转换为元组
    employee_tuples = []
    for line in csv_data:
        parts = line.split(',')
        name = parts[0]
        age = int(parts[1])
        position = parts[2]
        salary = int(parts[3])
        employee_tuples.append((name, age, position, salary))
    
    print("\n转换后的元组:")
    for emp_tuple in employee_tuples:
        print(f"  {emp_tuple}")
    
    # 数据分析
    total_salary = sum(emp[3] for emp in employee_tuples)
    avg_age = sum(emp[1] for emp in employee_tuples) / len(employee_tuples)
    
    print(f"\n数据分析:")
    print(f"总薪资: {total_salary}元")
    print(f"平均年龄: {avg_age:.1f}岁")

def practice_tips():
    """练习提示"""
    print("\n=" * 50)
    print("练习提示和总结")
    print("=" * 50)
    
    tips = [
        "元组是不可变的，一旦创建就不能修改",
        "使用元组解包可以优雅地处理多个返回值",
        "元组可以作为字典的键，列表不行",
        "元组比列表占用更少的内存",
        "单元素元组需要在元素后加逗号: (item,)",
        "使用*操作符可以进行灵活的元组解包",
        "元组适合存储不变的数据，如坐标、配置等",
        "嵌套元组可以表示复杂的数据结构",
        "元组与列表可以相互转换: tuple(list) 和 list(tuple)",
        "命名元组(namedtuple)提供了更好的可读性"
    ]
    
    print("重要提示:")
    for i, tip in enumerate(tips, 1):
        print(f"{i:2d}. {tip}")
    
    print("\n练习建议:")
    suggestions = [
        "多练习元组解包，这是Python的重要特性",
        "尝试在实际项目中使用元组存储不变数据",
        "比较元组和列表的性能差异",
        "学习使用元组作为字典键的技巧",
        "掌握嵌套元组的处理方法",
        "练习函数返回多个值的场景"
    ]
    
    for i, suggestion in enumerate(suggestions, 1):
        print(f"{i}. {suggestion}")

if __name__ == "__main__":
    exercise_1_basic_operations()
    exercise_2_tuple_operations()
    exercise_3_tuple_unpacking()
    exercise_4_practical_applications()
    exercise_5_advanced_exercises()
    exercise_6_comprehensive_project()
    bonus_exercises()
    practice_tips()
    
    print("\n" + "=" * 50)
    print("元组综合练习完成！")
    print("恭喜你完成了所有元组相关的学习和练习！")
    print("=" * 50)