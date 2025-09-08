#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
元组解包和多重赋值 - Tuple Unpacking and Multiple Assignment

本文件演示了Python中元组解包和多重赋值的各种用法：
1. 基本元组解包
2. 多重赋值
3. 交换变量值
4. 函数返回多个值
5. 星号表达式解包
6. 嵌套元组解包
7. 实际应用场景

作者: Python学习教程
日期: 2024
"""

def main():
    print("=" * 50)
    print("元组解包和多重赋值演示")
    print("=" * 50)
    
    # 1. 基本元组解包
    print("1. 基本元组解包:")
    
    # 创建一个元组
    point = (3, 4)
    print(f"原始元组: {point}")
    
    # 解包到变量
    x, y = point
    print(f"解包后: x = {x}, y = {y}")
    
    # 更多元素的解包
    person = ("Alice", 25, "Engineer")
    name, age, job = person
    print(f"\n人员信息: {person}")
    print(f"姓名: {name}, 年龄: {age}, 职业: {job}")
    
    # 2. 多重赋值
    print("\n2. 多重赋值:")
    
    # 同时赋值多个变量
    a, b, c = 1, 2, 3
    print(f"a = {a}, b = {b}, c = {c}")
    
    # 等价于元组解包
    a, b, c = (1, 2, 3)
    print(f"使用元组: a = {a}, b = {b}, c = {c}")
    
    # 3. 交换变量值
    print("\n3. 交换变量值:")
    
    x, y = 10, 20
    print(f"交换前: x = {x}, y = {y}")
    
    # Python中优雅的交换方式
    x, y = y, x
    print(f"交换后: x = {x}, y = {y}")
    
    # 多个变量的循环交换
    a, b, c = 1, 2, 3
    print(f"\n循环交换前: a = {a}, b = {b}, c = {c}")
    a, b, c = b, c, a
    print(f"循环交换后: a = {a}, b = {b}, c = {c}")
    
    # 4. 函数返回多个值
    print("\n4. 函数返回多个值:")
    
    def get_name_age():
        """返回姓名和年龄"""
        return "Bob", 30
    
    def calculate_stats(numbers):
        """计算统计信息"""
        total = sum(numbers)
        count = len(numbers)
        average = total / count if count > 0 else 0
        return total, count, average
    
    # 接收函数返回的多个值
    name, age = get_name_age()
    print(f"从函数获取: 姓名 = {name}, 年龄 = {age}")
    
    numbers = [10, 20, 30, 40, 50]
    total, count, avg = calculate_stats(numbers)
    print(f"统计结果: 总和 = {total}, 数量 = {count}, 平均值 = {avg}")

def demonstrate_star_unpacking():
    """演示星号表达式解包"""
    print("\n=" * 30)
    print("星号表达式解包演示")
    print("=" * 30)
    
    # 1. 基本星号解包
    print("1. 基本星号解包:")
    
    numbers = (1, 2, 3, 4, 5, 6)
    print(f"原始元组: {numbers}")
    
    # 取第一个和最后一个，中间的放到列表中
    first, *middle, last = numbers
    print(f"first = {first}")
    print(f"middle = {middle}")
    print(f"last = {last}")
    
    # 取前两个，剩余的放到列表中
    first, second, *rest = numbers
    print(f"\nfirst = {first}, second = {second}")
    print(f"rest = {rest}")
    
    # 取最后两个，前面的放到列表中
    *beginning, second_last, last = numbers
    print(f"\nbeginning = {beginning}")
    print(f"second_last = {second_last}, last = {last}")
    
    # 2. 字符串解包
    print("\n2. 字符串解包:")
    
    word = "hello"
    first_char, *middle_chars, last_char = word
    print(f"单词: {word}")
    print(f"首字符: {first_char}")
    print(f"中间字符: {middle_chars}")
    print(f"末字符: {last_char}")
    
    # 3. 处理不定长度的数据
    print("\n3. 处理不定长度的数据:")
    
    def process_scores(name, *scores):
        """处理学生成绩"""
        if not scores:
            return f"{name}: 没有成绩记录"
        
        total = sum(scores)
        average = total / len(scores)
        return f"{name}: 总分 {total}, 平均分 {average:.1f}"
    
    # 使用元组解包传递参数
    student1 = ("Alice", 85, 92, 78, 90)
    student2 = ("Bob", 88, 95)
    student3 = ("Charlie",)
    
    print(process_scores(*student1))
    print(process_scores(*student2))
    print(process_scores(*student3))

def demonstrate_nested_unpacking():
    """演示嵌套元组解包"""
    print("\n=" * 30)
    print("嵌套元组解包演示")
    print("=" * 30)
    
    # 1. 简单嵌套解包
    print("1. 简单嵌套解包:")
    
    nested_data = ((1, 2), (3, 4))
    print(f"嵌套元组: {nested_data}")
    
    (a, b), (c, d) = nested_data
    print(f"解包结果: a={a}, b={b}, c={c}, d={d}")
    
    # 2. 复杂嵌套解包
    print("\n2. 复杂嵌套解包:")
    
    complex_data = (("Alice", 25), ("Engineer", "Beijing"))
    print(f"复杂数据: {complex_data}")
    
    (name, age), (job, city) = complex_data
    print(f"姓名: {name}, 年龄: {age}")
    print(f"职业: {job}, 城市: {city}")
    
    # 3. 三维数据解包
    print("\n3. 三维数据解包:")
    
    matrix = (((1, 2), (3, 4)), ((5, 6), (7, 8)))
    print(f"三维矩阵: {matrix}")
    
    ((a, b), (c, d)), ((e, f), (g, h)) = matrix
    print(f"解包结果:")
    print(f"  第一组: a={a}, b={b}, c={c}, d={d}")
    print(f"  第二组: e={e}, f={f}, g={g}, h={h}")
    
    # 4. 混合数据类型解包
    print("\n4. 混合数据类型解包:")
    
    mixed_data = ("John", (25, "Male"), ["Python", "Java"])
    print(f"混合数据: {mixed_data}")
    
    name, (age, gender), skills = mixed_data
    print(f"姓名: {name}")
    print(f"年龄: {age}, 性别: {gender}")
    print(f"技能: {skills}")

def demonstrate_practical_applications():
    """演示实际应用场景"""
    print("\n=" * 30)
    print("实际应用场景")
    print("=" * 30)
    
    # 1. 处理CSV数据
    print("1. 处理CSV数据:")
    
    csv_data = [
        ("Alice", "25", "Engineer", "75000"),
        ("Bob", "30", "Designer", "65000"),
        ("Charlie", "28", "Manager", "85000")
    ]
    
    print("员工信息:")
    for name, age, position, salary in csv_data:
        print(f"  {name} ({age}岁) - {position}, 薪资: ${salary}")
    
    # 2. 坐标计算
    print("\n2. 坐标计算:")
    
    def distance_between_points(point1, point2):
        """计算两点间距离"""
        x1, y1 = point1
        x2, y2 = point2
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    point_a = (0, 0)
    point_b = (3, 4)
    
    dist = distance_between_points(point_a, point_b)
    print(f"点 {point_a} 到点 {point_b} 的距离: {dist}")
    
    # 3. 字典项目处理
    print("\n3. 字典项目处理:")
    
    student_grades = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "Diana": 96
    }
    
    print("学生成绩排名:")
    for rank, (name, grade) in enumerate(sorted(student_grades.items(), 
                                               key=lambda x: x[1], 
                                               reverse=True), 1):
        print(f"  第{rank}名: {name} - {grade}分")
    
    # 4. 函数参数解包
    print("\n4. 函数参数解包:")
    
    def create_person(name, age, city, job):
        """创建人员信息"""
        return f"{name} ({age}岁) 来自{city}，职业是{job}"
    
    person_data = ("Emma", 27, "上海", "数据分析师")
    result = create_person(*person_data)
    print(f"人员信息: {result}")
    
    # 5. 配置参数处理
    print("\n5. 配置参数处理:")
    
    def setup_database(host, port, username, password, database):
        """设置数据库连接"""
        return f"连接到 {host}:{port}/{database} (用户: {username})"
    
    # 从配置元组解包
    db_config = ("localhost", 5432, "admin", "secret", "myapp")
    connection_info = setup_database(*db_config)
    print(f"数据库配置: {connection_info}")
    
    # 6. 批量变量赋值
    print("\n6. 批量变量赋值:")
    
    # 初始化多个变量
    default_values = (0, 0, 100, 100)
    x, y, width, height = default_values
    print(f"窗口设置: 位置({x}, {y}), 大小({width}x{height})")
    
    # RGB颜色值
    colors = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255)
    }
    
    for color_name, (r, g, b) in colors.items():
        print(f"{color_name}: RGB({r}, {g}, {b})")

def demonstrate_common_mistakes():
    """演示常见错误和注意事项"""
    print("\n=" * 30)
    print("常见错误和注意事项")
    print("=" * 30)
    
    # 1. 元素数量不匹配
    print("1. 元素数量不匹配:")
    
    data = (1, 2, 3)
    
    try:
        a, b = data  # 尝试解包3个元素到2个变量
    except ValueError as e:
        print(f"错误: {e}")
    
    try:
        a, b, c, d = data  # 尝试解包3个元素到4个变量
    except ValueError as e:
        print(f"错误: {e}")
    
    # 正确的做法
    a, b, c = data
    print(f"正确解包: a={a}, b={b}, c={c}")
    
    # 2. 使用星号处理不确定数量
    print("\n2. 处理不确定数量的元素:")
    
    def safe_unpack(data):
        """安全解包函数"""
        if len(data) >= 2:
            first, second, *rest = data
            print(f"前两个: {first}, {second}")
            if rest:
                print(f"剩余: {rest}")
        else:
            print(f"数据不足: {data}")
    
    safe_unpack((1, 2, 3, 4, 5))
    safe_unpack((1, 2))
    safe_unpack((1,))
    
    # 3. 忽略不需要的值
    print("\n3. 忽略不需要的值:")
    
    person_info = ("Alice", 25, "Engineer", "alice@email.com", "123-456-7890")
    
    # 只需要姓名和职业
    name, _, job, *_ = person_info
    print(f"需要的信息: 姓名={name}, 职业={job}")
    
    # 或者使用下划线忽略
    name, age, job, _, _ = person_info
    print(f"另一种方式: 姓名={name}, 年龄={age}, 职业={job}")

if __name__ == "__main__":
    main()
    demonstrate_star_unpacking()
    demonstrate_nested_unpacking()
    demonstrate_practical_applications()
    demonstrate_common_mistakes()
    
    print("\n" + "=" * 50)
    print("元组解包和多重赋值学习完成！")
    print("下一步：学习元组与列表的比较")
    print("=" * 50)