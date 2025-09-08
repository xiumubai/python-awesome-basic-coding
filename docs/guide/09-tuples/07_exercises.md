# 元组综合练习

本节提供了一系列元组相关的练习题，从基础操作到高级应用，帮助你巩固和深化对元组的理解。每个练习都包含题目描述、示例和参考答案。

## 学习目标

- 巩固元组的基本操作
- 练习元组解包和多重赋值
- 掌握元组在实际问题中的应用
- 提高解决复杂问题的能力
- 学会元组与其他数据类型的综合使用

## 1. 基础操作练习

### 练习1.1：元组创建和访问

**题目**：创建一个包含学生信息的元组，包括姓名、年龄、专业和成绩，然后访问和打印各个信息。

```python
# 练习1.1：学生信息管理
def exercise_1_1():
    """创建和访问学生信息元组"""
    print("=== 练习1.1：学生信息管理 ===")
    
    # 创建学生信息元组
    student = ("Alice Johnson", 20, "Computer Science", 88.5)
    
    # 访问元组元素
    name = student[0]
    age = student[1]
    major = student[2]
    score = student[3]
    
    print(f"学生姓名: {name}")
    print(f"年龄: {age}")
    print(f"专业: {major}")
    print(f"成绩: {score}")
    
    # 使用负索引
    print(f"最后一项（成绩）: {student[-1]}")
    
    # 切片操作
    basic_info = student[:2]  # 姓名和年龄
    academic_info = student[2:]  # 专业和成绩
    
    print(f"基本信息: {basic_info}")
    print(f"学术信息: {academic_info}")
    
    return student

# 运行练习
exercise_1_1()
```

### 练习1.2：元组操作

**题目**：给定两个坐标点的元组，计算它们之间的距离，并创建一个包含两点和距离的新元组。

```python
# 练习1.2：坐标点距离计算
def exercise_1_2():
    """计算两点间距离"""
    print("\n=== 练习1.2：坐标点距离计算 ===")
    
    # 定义两个坐标点
    point1 = (3, 4)
    point2 = (6, 8)
    
    print(f"点1: {point1}")
    print(f"点2: {point2}")
    
    # 解包坐标
    x1, y1 = point1
    x2, y2 = point2
    
    # 计算距离
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    # 创建包含结果的元组
    result = (point1, point2, distance)
    
    print(f"距离: {distance:.2f}")
    print(f"完整结果: {result}")
    
    # 元组连接
    combined_points = point1 + point2
    print(f"连接后的坐标: {combined_points}")
    
    return result

# 运行练习
exercise_1_2()
```

## 2. 元组操作练习

### 练习2.1：数据统计

**题目**：给定一个包含多个数字的元组，计算总和、平均值、最大值、最小值，并统计特定数字的出现次数。

```python
# 练习2.1：数据统计分析
def exercise_2_1():
    """元组数据统计"""
    print("\n=== 练习2.1：数据统计分析 ===")
    
    # 测试数据
    numbers = (85, 92, 78, 85, 96, 88, 85, 91, 87, 85)
    print(f"原始数据: {numbers}")
    
    # 基本统计
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    maximum = max(numbers)
    minimum = min(numbers)
    
    print(f"总和: {total}")
    print(f"数量: {count}")
    print(f"平均值: {average:.2f}")
    print(f"最大值: {maximum}")
    print(f"最小值: {minimum}")
    
    # 统计特定值的出现次数
    target_value = 85
    occurrences = numbers.count(target_value)
    print(f"数字{target_value}出现次数: {occurrences}")
    
    # 查找特定值的位置
    first_occurrence = numbers.index(target_value)
    print(f"数字{target_value}第一次出现的位置: {first_occurrence}")
    
    # 创建统计结果元组
    statistics = (total, count, average, maximum, minimum, occurrences)
    print(f"统计结果元组: {statistics}")
    
    return statistics

# 运行练习
exercise_2_1()
```

### 练习2.2：元组排序和过滤

**题目**：给定一个包含学生信息的元组列表，按成绩排序，并过滤出及格的学生。

```python
# 练习2.2：学生成绩排序和过滤
def exercise_2_2():
    """学生成绩处理"""
    print("\n=== 练习2.2：学生成绩排序和过滤 ===")
    
    # 学生数据（姓名，年龄，成绩）
    students = [
        ("Alice", 20, 85),
        ("Bob", 19, 58),
        ("Charlie", 21, 92),
        ("Diana", 20, 76),
        ("Eve", 19, 45),
        ("Frank", 22, 88)
    ]
    
    print("原始学生数据:")
    for student in students:
        name, age, score = student
        print(f"  {name}: {age}岁, {score}分")
    
    # 按成绩排序（降序）
    sorted_students = sorted(students, key=lambda x: x[2], reverse=True)
    print("\n按成绩排序（降序）:")
    for rank, student in enumerate(sorted_students, 1):
        name, age, score = student
        print(f"  第{rank}名: {name} - {score}分")
    
    # 过滤及格学生（成绩>=60）
    passing_students = tuple(student for student in students if student[2] >= 60)
    print(f"\n及格学生数量: {len(passing_students)}")
    print("及格学生名单:")
    for student in passing_students:
        name, age, score = student
        print(f"  {name}: {score}分")
    
    # 计算及格率
    passing_rate = len(passing_students) / len(students) * 100
    print(f"及格率: {passing_rate:.1f}%")
    
    return sorted_students, passing_students

# 运行练习
exercise_2_2()
```

## 3. 元组解包练习

### 练习3.1：多重赋值和变量交换

**题目**：使用元组解包实现多个变量的赋值和交换操作。

```python
# 练习3.1：多重赋值和变量交换
def exercise_3_1():
    """多重赋值和变量交换"""
    print("\n=== 练习3.1：多重赋值和变量交换 ===")
    
    # 多重赋值
    name, age, city = "Alice", 25, "New York"
    print(f"多重赋值结果: {name}, {age}, {city}")
    
    # 变量交换
    a, b = 10, 20
    print(f"交换前: a={a}, b={b}")
    a, b = b, a
    print(f"交换后: a={a}, b={b}")
    
    # 多变量循环交换
    x, y, z = 1, 2, 3
    print(f"循环交换前: x={x}, y={y}, z={z}")
    x, y, z = z, x, y
    print(f"循环交换后: x={x}, y={y}, z={z}")
    
    # 函数返回多值的解包
    def get_user_info():
        return "Bob", 30, "Engineer", "Boston"
    
    name, age, job, city = get_user_info()
    print(f"函数返回值解包: {name}, {age}, {job}, {city}")
    
    # 星号表达式解包
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    first, second, *middle, second_last, last = numbers
    print(f"星号解包: 前两个={first}, {second}, 中间={middle}, 后两个={second_last}, {last}")
    
    return (name, age, job, city)

# 运行练习
exercise_3_1()
```

### 练习3.2：嵌套元组解包

**题目**：处理复杂的嵌套元组结构，提取所需信息。

```python
# 练习3.2：嵌套元组解包
def exercise_3_2():
    """嵌套元组解包"""
    print("\n=== 练习3.2：嵌套元组解包 ===")
    
    # 复杂的嵌套结构：公司信息
    company_info = (
        ("TechCorp", ("San Francisco", "CA", "USA")),
        (
            (("Alice", "CEO"), ("Bob", "CTO"), ("Charlie", "CFO")),
            (("Diana", "Engineer"), ("Eve", "Designer"))
        ),
        (2023, (1000000, 1200000, 1500000, 1800000))
    )
    
    # 解包公司基本信息
    (company_name, (city, state, country)), executives_and_employees, (year, quarterly_revenue) = company_info
    
    print(f"公司名称: {company_name}")
    print(f"地址: {city}, {state}, {country}")
    print(f"年份: {year}")
    
    # 解包高管信息
    executives, employees = executives_and_employees
    print("\n高管团队:")
    for name, position in executives:
        print(f"  {name}: {position}")
    
    print("\n员工:")
    for name, position in employees:
        print(f"  {name}: {position}")
    
    # 解包季度收入
    q1, q2, q3, q4 = quarterly_revenue
    print(f"\n季度收入:")
    print(f"  Q1: ${q1:,}")
    print(f"  Q2: ${q2:,}")
    print(f"  Q3: ${q3:,}")
    print(f"  Q4: ${q4:,}")
    print(f"  年总收入: ${sum(quarterly_revenue):,}")
    
    return company_name, executives, employees, quarterly_revenue

# 运行练习
exercise_3_2()
```

## 4. 实际应用练习

### 练习4.1：数据分析

**题目**：分析销售数据，计算每个销售员的业绩统计。

```python
# 练习4.1：销售数据分析
def exercise_4_1():
    """销售数据分析"""
    print("\n=== 练习4.1：销售数据分析 ===")
    
    # 销售数据：(销售员, 月份, 销售额)
    sales_data = [
        ("Alice", "January", 15000),
        ("Bob", "January", 12000),
        ("Alice", "February", 18000),
        ("Charlie", "January", 20000),
        ("Bob", "February", 14000),
        ("Alice", "March", 16000),
        ("Charlie", "February", 22000),
        ("Bob", "March", 13000),
        ("Charlie", "March", 25000)
    ]
    
    print("原始销售数据:")
    for record in sales_data:
        salesperson, month, amount = record
        print(f"  {salesperson} - {month}: ${amount:,}")
    
    # 按销售员统计
    salesperson_stats = {}
    
    for record in sales_data:
        salesperson, month, amount = record
        
        if salesperson not in salesperson_stats:
            salesperson_stats[salesperson] = []
        
        salesperson_stats[salesperson].append(amount)
    
    # 计算每个销售员的统计信息
    print("\n销售员业绩统计:")
    all_stats = []
    
    for salesperson, amounts in salesperson_stats.items():
        total = sum(amounts)
        average = total / len(amounts)
        best_month = max(amounts)
        worst_month = min(amounts)
        
        stats = (salesperson, total, average, best_month, worst_month, len(amounts))
        all_stats.append(stats)
        
        print(f"  {salesperson}:")
        print(f"    总销售额: ${total:,}")
        print(f"    平均月销售额: ${average:,.0f}")
        print(f"    最佳月份: ${best_month:,}")
        print(f"    最差月份: ${worst_month:,}")
        print(f"    销售月数: {len(amounts)}")
    
    # 找出最佳销售员
    best_salesperson = max(all_stats, key=lambda x: x[1])
    print(f"\n最佳销售员: {best_salesperson[0]}，总销售额: ${best_salesperson[1]:,}")
    
    return tuple(all_stats)

# 运行练习
exercise_4_1()
```

### 练习4.2：坐标系统

**题目**：实现一个简单的2D坐标系统，包括点的创建、距离计算、区域判断等功能。

```python
# 练习4.2：2D坐标系统
def exercise_4_2():
    """2D坐标系统"""
    print("\n=== 练习4.2：2D坐标系统 ===")
    
    # 定义一些点
    points = [
        (0, 0),    # 原点
        (3, 4),    # 第一象限
        (-2, 3),   # 第二象限
        (-1, -2),  # 第三象限
        (4, -1)    # 第四象限
    ]
    
    print("坐标点:")
    for i, point in enumerate(points):
        x, y = point
        print(f"  点{i+1}: ({x}, {y})")
    
    # 计算每个点到原点的距离
    print("\n到原点的距离:")
    distances = []
    for point in points:
        x, y = point
        distance = (x**2 + y**2)**0.5
        distances.append((point, distance))
        print(f"  {point}: {distance:.2f}")
    
    # 找出最远和最近的点
    farthest = max(distances, key=lambda x: x[1])
    closest = min(distances, key=lambda x: x[1])
    
    print(f"\n最远点: {farthest[0]}，距离: {farthest[1]:.2f}")
    print(f"最近点: {closest[0]}，距离: {closest[1]:.2f}")
    
    # 判断点所在的象限
    def get_quadrant(point):
        x, y = point
        if x > 0 and y > 0:
            return "第一象限"
        elif x < 0 and y > 0:
            return "第二象限"
        elif x < 0 and y < 0:
            return "第三象限"
        elif x > 0 and y < 0:
            return "第四象限"
        elif x == 0 and y == 0:
            return "原点"
        elif x == 0:
            return "y轴"
        else:
            return "x轴"
    
    print("\n象限分布:")
    quadrant_stats = {}
    for point in points:
        quadrant = get_quadrant(point)
        print(f"  {point}: {quadrant}")
        
        if quadrant not in quadrant_stats:
            quadrant_stats[quadrant] = 0
        quadrant_stats[quadrant] += 1
    
    print("\n象限统计:")
    for quadrant, count in quadrant_stats.items():
        print(f"  {quadrant}: {count}个点")
    
    # 计算所有点对之间的距离
    print("\n点对距离:")
    point_pairs = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            p1, p2 = points[i], points[j]
            x1, y1 = p1
            x2, y2 = p2
            distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
            point_pairs.append((p1, p2, distance))
            print(f"  {p1} 到 {p2}: {distance:.2f}")
    
    # 找出最近和最远的点对
    closest_pair = min(point_pairs, key=lambda x: x[2])
    farthest_pair = max(point_pairs, key=lambda x: x[2])
    
    print(f"\n最近点对: {closest_pair[0]} 和 {closest_pair[1]}，距离: {closest_pair[2]:.2f}")
    print(f"最远点对: {farthest_pair[0]} 和 {farthest_pair[1]}，距离: {farthest_pair[2]:.2f}")
    
    return points, distances, point_pairs

# 运行练习
exercise_4_2()
```

## 5. 高级练习

### 练习5.1：数据转换和处理

**题目**：处理CSV格式的数据，进行清洗、转换和分析。

```python
# 练习5.1：数据转换和处理
def exercise_5_1():
    """数据转换和处理"""
    print("\n=== 练习5.1：数据转换和处理 ===")
    
    # 模拟CSV数据（每行是一个字符串）
    csv_data = [
        "Alice,25,Engineer,85000,New York",
        "Bob,30,Designer,75000,Los Angeles",
        "Charlie,28,Manager,95000,Chicago",
        "Diana,26,Developer,80000,Seattle",
        "Eve,32,Analyst,70000,Boston"
    ]
    
    print("原始CSV数据:")
    for row in csv_data:
        print(f"  {row}")
    
    # 解析CSV数据为元组
    parsed_data = []
    for row in csv_data:
        parts = row.split(',')
        name = parts[0].strip()
        age = int(parts[1].strip())
        job = parts[2].strip()
        salary = int(parts[3].strip())
        city = parts[4].strip()
        
        record = (name, age, job, salary, city)
        parsed_data.append(record)
    
    print("\n解析后的数据:")
    for record in parsed_data:
        name, age, job, salary, city = record
        print(f"  {name}: {age}岁, {job}, ${salary:,}, {city}")
    
    # 数据分析
    # 1. 按薪资排序
    sorted_by_salary = sorted(parsed_data, key=lambda x: x[3], reverse=True)
    print("\n按薪资排序（降序）:")
    for rank, record in enumerate(sorted_by_salary, 1):
        name, age, job, salary, city = record
        print(f"  {rank}. {name}: ${salary:,}")
    
    # 2. 按年龄分组
    age_groups = {
        "20-25": [],
        "26-30": [],
        "31-35": []
    }
    
    for record in parsed_data:
        name, age, job, salary, city = record
        if 20 <= age <= 25:
            age_groups["20-25"].append(record)
        elif 26 <= age <= 30:
            age_groups["26-30"].append(record)
        elif 31 <= age <= 35:
            age_groups["31-35"].append(record)
    
    print("\n年龄分组:")
    for group, members in age_groups.items():
        print(f"  {group}岁: {len(members)}人")
        for member in members:
            name, age, job, salary, city = member
            print(f"    {name} ({age}岁)")
    
    # 3. 职位统计
    job_stats = {}
    for record in parsed_data:
        name, age, job, salary, city = record
        if job not in job_stats:
            job_stats[job] = []
        job_stats[job].append(salary)
    
    print("\n职位薪资统计:")
    for job, salaries in job_stats.items():
        avg_salary = sum(salaries) / len(salaries)
        print(f"  {job}: 平均薪资 ${avg_salary:,.0f} ({len(salaries)}人)")
    
    # 4. 城市分布
    city_distribution = {}
    for record in parsed_data:
        name, age, job, salary, city = record
        if city not in city_distribution:
            city_distribution[city] = 0
        city_distribution[city] += 1
    
    print("\n城市分布:")
    for city, count in sorted(city_distribution.items(), key=lambda x: x[1], reverse=True):
        print(f"  {city}: {count}人")
    
    return tuple(parsed_data), sorted_by_salary, age_groups, job_stats

# 运行练习
exercise_5_1()
```

### 练习5.2：复杂数据结构操作

**题目**：处理包含多层嵌套的复杂数据结构，实现数据的查询、统计和转换。

```python
# 练习5.2：复杂数据结构操作
def exercise_5_2():
    """复杂数据结构操作"""
    print("\n=== 练习5.2：复杂数据结构操作 ===")
    
    # 复杂的学校数据结构
    school_data = (
        ("计算机科学系", (
            (("Alice", "大一"), (("数学", 85), ("编程", 92), ("英语", 78))),
            (("Bob", "大二"), (("数据结构", 88), ("算法", 90), ("数据库", 85))),
            (("Charlie", "大三"), (("软件工程", 95), ("网络", 87), ("AI", 93)))
        )),
        ("数学系", (
            (("Diana", "大一"), (("微积分", 90), ("线性代数", 88), ("统计", 85))),
            (("Eve", "大二"), (("概率论", 92), ("数值分析", 89), ("离散数学", 91)))
        ))
    )
    
    print("学校数据结构分析:")
    
    # 解析和统计数据
    all_students = []
    department_stats = {}
    
    for department_info in school_data:
        dept_name, students_data = department_info
        print(f"\n{dept_name}:")
        
        department_stats[dept_name] = {
            "student_count": 0,
            "total_scores": [],
            "grade_distribution": {}
        }
        
        for student_info in students_data:
            (name, grade), courses = student_info
            print(f"  {name} ({grade}):")
            
            # 统计年级分布
            if grade not in department_stats[dept_name]["grade_distribution"]:
                department_stats[dept_name]["grade_distribution"][grade] = 0
            department_stats[dept_name]["grade_distribution"][grade] += 1
            
            # 计算学生平均分
            scores = [score for course, score in courses]
            avg_score = sum(scores) / len(scores)
            
            # 记录所有成绩
            department_stats[dept_name]["total_scores"].extend(scores)
            department_stats[dept_name]["student_count"] += 1
            
            # 创建完整的学生记录
            student_record = (dept_name, name, grade, courses, avg_score)
            all_students.append(student_record)
            
            print(f"    课程成绩: {dict(courses)}")
            print(f"    平均分: {avg_score:.1f}")
    
    # 全校统计
    print("\n=== 全校统计 ===")
    
    # 各系统计
    for dept, stats in department_stats.items():
        dept_avg = sum(stats["total_scores"]) / len(stats["total_scores"])
        print(f"\n{dept}:")
        print(f"  学生人数: {stats['student_count']}")
        print(f"  系平均分: {dept_avg:.1f}")
        print(f"  年级分布: {dict(stats['grade_distribution'])}")
    
    # 找出最优秀的学生
    best_student = max(all_students, key=lambda x: x[4])
    dept, name, grade, courses, avg_score = best_student
    print(f"\n最优秀学生: {name} ({dept}, {grade})，平均分: {avg_score:.1f}")
    
    # 按系和年级分组
    grouped_data = {}
    for student in all_students:
        dept, name, grade, courses, avg_score = student
        key = (dept, grade)
        
        if key not in grouped_data:
            grouped_data[key] = []
        grouped_data[key].append((name, avg_score))
    
    print("\n按系和年级分组:")
    for (dept, grade), students in grouped_data.items():
        avg_group_score = sum(score for name, score in students) / len(students)
        print(f"  {dept} {grade}: {len(students)}人，平均分: {avg_group_score:.1f}")
        for name, score in students:
            print(f"    {name}: {score:.1f}")
    
    # 课程成绩统计
    course_stats = {}
    for student in all_students:
        dept, name, grade, courses, avg_score = student
        for course, score in courses:
            if course not in course_stats:
                course_stats[course] = []
            course_stats[course].append(score)
    
    print("\n课程成绩统计:")
    for course, scores in course_stats.items():
        avg_score = sum(scores) / len(scores)
        max_score = max(scores)
        min_score = min(scores)
        print(f"  {course}: 平均{avg_score:.1f}, 最高{max_score}, 最低{min_score} ({len(scores)}人选修)")
    
    return all_students, department_stats, grouped_data, course_stats

# 运行练习
exercise_5_2()
```

## 6. 综合项目练习

### 练习6.1：学生成绩管理系统

**题目**：设计一个完整的学生成绩管理系统，包括数据存储、查询、统计等功能。

```python
# 练习6.1：学生成绩管理系统
class StudentGradeSystem:
    """学生成绩管理系统"""
    
    def __init__(self):
        # 使用元组存储不可变的学生记录
        # 格式：(学号, 姓名, 班级, ((科目1, 成绩1), (科目2, 成绩2), ...))
        self.students = [
            ("S001", "Alice", "CS101", (("数学", 85), ("英语", 78), ("编程", 92))),
            ("S002", "Bob", "CS101", (("数学", 78), ("英语", 85), ("编程", 88))),
            ("S003", "Charlie", "CS102", (("数学", 92), ("英语", 88), ("编程", 95))),
            ("S004", "Diana", "CS101", (("数学", 88), ("英语", 92), ("编程", 85))),
            ("S005", "Eve", "CS102", (("数学", 95), ("英语", 90), ("编程", 98)))
        ]
    
    def display_all_students(self):
        """显示所有学生信息"""
        print("=== 所有学生信息 ===")
        for student in self.students:
            student_id, name, class_name, grades = student
            avg_score = sum(score for subject, score in grades) / len(grades)
            print(f"学号: {student_id}, 姓名: {name}, 班级: {class_name}, 平均分: {avg_score:.1f}")
            for subject, score in grades:
                print(f"  {subject}: {score}分")
            print()
    
    def find_student_by_id(self, student_id):
        """根据学号查找学生"""
        for student in self.students:
            sid, name, class_name, grades = student
            if sid == student_id:
                return student
        return None
    
    def get_class_statistics(self, class_name):
        """获取班级统计信息"""
        class_students = []
        for student in self.students:
            sid, name, cls, grades = student
            if cls == class_name:
                class_students.append(student)
        
        if not class_students:
            return None
        
        # 计算班级统计
        all_scores = []
        subject_scores = {}
        
        for student in class_students:
            sid, name, cls, grades = student
            student_avg = sum(score for subject, score in grades) / len(grades)
            all_scores.append(student_avg)
            
            for subject, score in grades:
                if subject not in subject_scores:
                    subject_scores[subject] = []
                subject_scores[subject].append(score)
        
        class_avg = sum(all_scores) / len(all_scores)
        
        return {
            "class_name": class_name,
            "student_count": len(class_students),
            "class_average": class_avg,
            "highest_average": max(all_scores),
            "lowest_average": min(all_scores),
            "subject_averages": {subject: sum(scores)/len(scores) 
                               for subject, scores in subject_scores.items()}
        }
    
    def get_subject_ranking(self, subject):
        """获取某科目的排名"""
        subject_scores = []
        
        for student in self.students:
            sid, name, class_name, grades = student
            for subj, score in grades:
                if subj == subject:
                    subject_scores.append((name, class_name, score))
                    break
        
        # 按成绩排序
        subject_scores.sort(key=lambda x: x[2], reverse=True)
        return subject_scores
    
    def get_top_students(self, n=3):
        """获取前n名学生"""
        student_averages = []
        
        for student in self.students:
            sid, name, class_name, grades = student
            avg_score = sum(score for subject, score in grades) / len(grades)
            student_averages.append((name, class_name, avg_score, grades))
        
        # 按平均分排序
        student_averages.sort(key=lambda x: x[2], reverse=True)
        return student_averages[:n]

def exercise_6_1():
    """运行学生成绩管理系统"""
    print("\n=== 练习6.1：学生成绩管理系统 ===")
    
    system = StudentGradeSystem()
    
    # 显示所有学生
    system.display_all_students()
    
    # 查找特定学生
    print("=== 查找学生 S003 ===")
    student = system.find_student_by_id("S003")
    if student:
        sid, name, class_name, grades = student
        print(f"找到学生: {name} ({sid}), 班级: {class_name}")
        for subject, score in grades:
            print(f"  {subject}: {score}分")
    
    # 班级统计
    print("\n=== CS101班级统计 ===")
    stats = system.get_class_statistics("CS101")
    if stats:
        print(f"班级: {stats['class_name']}")
        print(f"学生人数: {stats['student_count']}")
        print(f"班级平均分: {stats['class_average']:.1f}")
        print(f"最高平均分: {stats['highest_average']:.1f}")
        print(f"最低平均分: {stats['lowest_average']:.1f}")
        print("各科平均分:")
        for subject, avg in stats['subject_averages'].items():
            print(f"  {subject}: {avg:.1f}")
    
    # 科目排名
    print("\n=== 数学科目排名 ===")
    math_ranking = system.get_subject_ranking("数学")
    for rank, (name, class_name, score) in enumerate(math_ranking, 1):
        print(f"  第{rank}名: {name} ({class_name}) - {score}分")
    
    # 前三名学生
    print("\n=== 前三名学生 ===")
    top_students = system.get_top_students(3)
    for rank, (name, class_name, avg_score, grades) in enumerate(top_students, 1):
        print(f"  第{rank}名: {name} ({class_name}) - 平均分: {avg_score:.1f}")
        for subject, score in grades:
            print(f"    {subject}: {score}分")
    
    return system

# 运行练习
exercise_6_1()
```

## 7. 运行所有练习

```python
def run_all_exercises():
    """运行所有练习"""
    print("开始运行所有元组练习...")
    print("=" * 60)
    
    # 运行所有练习
    exercises = [
        exercise_1_1, exercise_1_2,
        exercise_2_1, exercise_2_2,
        exercise_3_1, exercise_3_2,
        exercise_4_1, exercise_4_2,
        exercise_5_1, exercise_5_2,
        exercise_6_1
    ]
    
    results = []
    for exercise in exercises:
        try:
            result = exercise()
            results.append(result)
        except Exception as e:
            print(f"练习 {exercise.__name__} 执行出错: {e}")
            results.append(None)
    
    print("\n" + "=" * 60)
    print("所有练习执行完成！")
    
    return results

# 如果直接运行此文件，执行所有练习
if __name__ == "__main__":
    run_all_exercises()
```

## 学习要点总结

通过这些练习，你应该掌握了：

1. **基础操作**：元组的创建、访问、切片等基本操作
2. **数据处理**：使用元组进行数据统计、排序、过滤
3. **解包技巧**：多重赋值、星号表达式、嵌套解包
4. **实际应用**：在真实场景中使用元组解决问题
5. **性能优化**：理解元组的性能特点和使用场景
6. **复杂结构**：处理多层嵌套的复杂数据结构
7. **系统设计**：使用元组设计完整的数据管理系统

## 进阶练习建议

1. **自定义练习**：根据自己的需求创建更多练习
2. **性能测试**：比较元组和列表在不同场景下的性能
3. **实际项目**：在真实项目中应用元组的知识
4. **代码优化**：重构现有代码，合理使用元组
5. **算法实现**：使用元组实现各种算法和数据结构

通过大量的练习，你将能够熟练掌握元组的使用，并在实际编程中灵活运用这些知识。