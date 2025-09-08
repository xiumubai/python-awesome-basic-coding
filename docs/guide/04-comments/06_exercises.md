# 注释练习题

## 学习目标

通过本节练习，你将能够：
- 熟练掌握各种注释的编写技巧
- 学会为不同类型的代码添加合适的注释
- 理解注释的最佳实践和常见误区
- 培养良好的代码注释习惯
- 提高代码的可读性和维护性

## 主要内容

本节包含7个综合练习：
1. **基础注释练习** - 为变量和计算过程添加注释
2. **函数文档字符串练习** - 编写完整的函数文档
3. **类文档字符串练习** - 为类和方法添加文档
4. **注释改进练习** - 识别和改进不良注释
5. **复杂算法注释练习** - 为算法添加详细说明
6. **实际项目注释练习** - 学生管理系统注释实践
7. **注释风格统一练习** - 保持注释风格一致性

## 完整代码

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
注释练习题

本文件包含了关于Python注释的各种练习题，帮助学习者
巩固注释的使用方法和最佳实践。

练习内容包括：
- 单行注释练习
- 多行注释练习
- 文档字符串练习
- 注释改进练习
- 实际项目注释练习

作者: Python学习教程
日期: 2024
"""

import math
import random
from typing import List, Dict, Tuple, Optional

print("=== Python注释练习题 ===")

# ============================================================
# 练习1: 基础注释练习
# ============================================================

print("\n--- 练习1: 基础注释练习 ---")

# 任务: 为下面的代码添加适当的注释
# 提示: 解释代码的目的，而不是重复代码内容

# 练习1.1: 为变量添加注释
student_count = 30
max_score = 100
pass_threshold = 60

# 练习1.2: 为计算过程添加注释
scores = [85, 92, 78, 96, 88, 73, 91, 84, 79, 95]
total_score = sum(scores)
average_score = total_score / len(scores)
pass_count = len([score for score in scores if score >= pass_threshold])
pass_rate = (pass_count / len(scores)) * 100

print(f"平均分: {average_score:.2f}")
print(f"及格率: {pass_rate:.1f}%")

# ============================================================
# 练习2: 函数文档字符串练习
# ============================================================

print("\n--- 练习2: 函数文档字符串练习 ---")

# 任务: 为下面的函数添加完整的文档字符串
# 包括: 功能描述、参数说明、返回值说明、异常说明、使用示例

def calculate_bmi(weight, height):
    # TODO: 添加文档字符串
    if height <= 0:
        raise ValueError("身高必须大于0")
    if weight <= 0:
        raise ValueError("体重必须大于0")
    
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    # TODO: 添加文档字符串
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 24:
        return "正常"
    elif bmi < 28:
        return "偏胖"
    else:
        return "肥胖"

def fibonacci(n):
    # TODO: 添加文档字符串
    # 提示: 这是计算斐波那契数列的函数
    if n < 0:
        raise ValueError("n必须是非负整数")
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 测试函数
try:
    bmi = calculate_bmi(70, 1.75)
    category = get_bmi_category(bmi)
    print(f"BMI: {bmi:.2f}, 分类: {category}")
    
    fib_10 = fibonacci(10)
    print(f"第10个斐波那契数: {fib_10}")
except ValueError as e:
    print(f"错误: {e}")

# ============================================================
# 练习3: 类文档字符串练习
# ============================================================

print("\n--- 练习3: 类文档字符串练习 ---")

# 任务: 为下面的类和方法添加完整的文档字符串

class Calculator:
    # TODO: 添加类文档字符串
    
    def __init__(self):
        # TODO: 添加构造函数文档字符串
        self.history = []
    
    def add(self, a, b):
        # TODO: 添加方法文档字符串
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def multiply(self, a, b):
        # TODO: 添加方法文档字符串
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def power(self, base, exponent):
        # TODO: 添加方法文档字符串
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    def get_history(self):
        # TODO: 添加方法文档字符串
        return self.history.copy()
    
    def clear_history(self):
        # TODO: 添加方法文档字符串
        self.history.clear()

# 测试计算器类
calc = Calculator()
result1 = calc.add(10, 5)
result2 = calc.multiply(3, 4)
result3 = calc.power(2, 8)
print(f"计算结果: {result1}, {result2}, {result3}")
print(f"计算历史: {calc.get_history()}")

# ============================================================
# 练习4: 注释改进练习
# ============================================================

print("\n--- 练习4: 注释改进练习 ---")

# 任务: 改进下面代码的注释
# 找出不好的注释并改进它们

# 不好的注释示例 - 需要改进
def process_data(data):
    # 检查数据
    if not data:
        return None
    
    # 创建结果列表
    result = []
    
    # 遍历数据
    for item in data:
        # 检查项目
        if isinstance(item, (int, float)):
            # 添加到结果
            result.append(item * 2)
    
    # 返回结果
    return result

# 改进后的版本 - 请在这里重写上面的函数
def process_data_improved(data):
    # TODO: 重写上面的函数，添加更好的注释
    pass

# ============================================================
# 练习5: 复杂算法注释练习
# ============================================================

print("\n--- 练习5: 复杂算法注释练习 ---")

# 任务: 为下面的算法添加详细注释
# 解释算法的思路、步骤和关键点

def binary_search(arr, target):
    # TODO: 添加算法说明注释
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def merge_sort(arr):
    # TODO: 添加算法说明注释
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    # TODO: 添加合并逻辑注释
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 测试算法
test_array = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
index = binary_search(test_array, target)
print(f"在数组 {test_array} 中查找 {target}: 索引 {index}")

unsorted_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = merge_sort(unsorted_array)
print(f"排序前: {unsorted_array}")
print(f"排序后: {sorted_array}")

# ============================================================
# 练习6: 实际项目注释练习
# ============================================================

print("\n--- 练习6: 实际项目注释练习 ---")

# 任务: 为下面的项目代码添加完整的注释
# 这是一个简单的学生管理系统

class Student:
    # TODO: 添加类文档字符串
    
    def __init__(self, student_id, name, age, major):
        # TODO: 添加构造函数注释
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major
        self.courses = {}
    
    def add_course(self, course_name, score=None):
        # TODO: 添加方法注释
        self.courses[course_name] = score
    
    def update_score(self, course_name, score):
        # TODO: 添加方法注释
        if course_name in self.courses:
            self.courses[course_name] = score
            return True
        return False
    
    def get_gpa(self):
        # TODO: 添加GPA计算注释
        scores = [score for score in self.courses.values() if score is not None]
        if not scores:
            return 0.0
        return sum(scores) / len(scores)
    
    def get_info(self):
        # TODO: 添加方法注释
        return {
            'id': self.student_id,
            'name': self.name,
            'age': self.age,
            'major': self.major,
            'gpa': self.get_gpa(),
            'courses': self.courses
        }

class StudentManager:
    # TODO: 添加类文档字符串
    
    def __init__(self):
        # TODO: 添加构造函数注释
        self.students = {}
    
    def add_student(self, student):
        # TODO: 添加方法注释
        if student.student_id in self.students:
            return False
        self.students[student.student_id] = student
        return True
    
    def find_student(self, student_id):
        # TODO: 添加方法注释
        return self.students.get(student_id)
    
    def get_top_students(self, n=5):
        # TODO: 添加方法注释
        students_with_gpa = [(s.get_gpa(), s) for s in self.students.values()]
        students_with_gpa.sort(reverse=True)
        return [student for _, student in students_with_gpa[:n]]
    
    def get_statistics(self):
        # TODO: 添加统计方法注释
        if not self.students:
            return {}
        
        gpas = [s.get_gpa() for s in self.students.values()]
        return {
            'total_students': len(self.students),
            'average_gpa': sum(gpas) / len(gpas),
            'highest_gpa': max(gpas),
            'lowest_gpa': min(gpas)
        }

# 测试学生管理系统
manager = StudentManager()

# 创建学生
student1 = Student("2021001", "张三", 20, "计算机科学")
student1.add_course("数学", 85)
student1.add_course("编程", 92)
student1.add_course("英语", 78)

student2 = Student("2021002", "李四", 19, "软件工程")
student2.add_course("数学", 90)
student2.add_course("编程", 88)
student2.add_course("英语", 85)

# 添加到管理系统
manager.add_student(student1)
manager.add_student(student2)

# 显示统计信息
stats = manager.get_statistics()
print(f"学生统计: {stats}")

top_students = manager.get_top_students(2)
print("优秀学生:")
for student in top_students:
    info = student.get_info()
    print(f"  {info['name']} (GPA: {info['gpa']:.2f})")

# ============================================================
# 练习7: 注释风格统一练习
# ============================================================

print("\n--- 练习7: 注释风格统一练习 ---")

# 任务: 统一下面代码的注释风格
# 选择一种注释风格并保持一致

def data_processor():
    """数据处理函数"""
    
    # 配置参数
    config = {
        'batch_size': 100,    # 批处理大小
        'timeout': 30,        # 超时时间(秒)
        'retry_count': 3      # 重试次数
    }
    
    # Step 1: 初始化数据
    data = []
    
    # Step 2: 加载数据
    for i in range(config['batch_size']):
        data.append(random.randint(1, 100))
    
    # Step 3: 处理数据
    processed_data = []
    for item in data:
        if item > 50:  # 只处理大于50的数据
            processed_data.append(item * 2)
    
    # Step 4: 返回结果
    return processed_data

# TODO: 改进上面函数的注释风格，使其更加统一和专业

# ============================================================
# 练习答案提示区域
# ============================================================

print("\n=== 练习提示 ===")
print("1. 练习1: 注释应该解释变量的用途和计算的业务含义")
print("2. 练习2: 文档字符串应该包含完整的参数、返回值和异常说明")
print("3. 练习3: 类文档字符串应该描述类的职责和使用方法")
print("4. 练习4: 避免重复代码内容的注释，专注于解释'为什么'")
print("5. 练习5: 算法注释应该解释思路、时间复杂度和关键步骤")
print("6. 练习6: 项目代码注释应该考虑维护性和团队协作")
print("7. 练习7: 保持注释风格的一致性很重要")

print("\n=== 自我检查清单 ===")
print("□ 注释是否解释了代码的目的而不是重复代码？")
print("□ 文档字符串是否包含了所有必要信息？")
print("□ 注释是否与代码保持同步？")
print("□ 是否避免了过度注释？")
print("□ 注释风格是否在整个项目中保持一致？")
print("□ 复杂算法是否有足够的解释？")
print("□ 是否使用了适当的TODO、FIXME等标记？")

# 运行这个文件来完成注释练习
# 在终端中执行: python 06_exercises.py
# 建议: 先尝试完成练习，再查看其他示例文件的参考答案
```

## 练习说明

### 练习1: 基础注释练习
**任务**：为变量和计算过程添加适当的注释

**要点**：
- 解释变量的业务含义
- 说明计算的目的
- 避免重复代码内容

**示例改进**：
```python
# 改进前
student_count = 30

# 改进后
student_count = 30  # 班级学生总数，用于计算各种比率
```

### 练习2: 函数文档字符串练习
**任务**：为函数添加完整的文档字符串

**要求**：
- 功能描述
- 参数说明（类型和含义）
- 返回值说明
- 异常说明
- 使用示例

**参考格式**：
```python
def calculate_bmi(weight: float, height: float) -> float:
    """
    计算身体质量指数(BMI)。
    
    参数:
        weight (float): 体重，单位为千克
        height (float): 身高，单位为米
    
    返回:
        float: BMI值
    
    异常:
        ValueError: 当身高或体重小于等于0时抛出
    
    示例:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
```

### 练习3: 类文档字符串练习
**任务**：为类和方法添加完整的文档字符串

**要求**：
- 类的职责和用途
- 主要属性说明
- 使用示例
- 方法的详细说明

### 练习4: 注释改进练习
**任务**：识别和改进不良注释

**常见问题**：
- 重复代码内容
- 注释过于显而易见
- 缺乏业务含义解释

**改进原则**：
- 解释"为什么"而不是"做什么"
- 提供业务上下文
- 保持简洁明了

### 练习5: 复杂算法注释练习
**任务**：为算法添加详细的注释说明

**要求**：
- 算法思路和原理
- 时间和空间复杂度
- 关键步骤解释
- 边界条件处理

### 练习6: 实际项目注释练习
**任务**：为学生管理系统添加完整注释

**考虑因素**：
- 业务逻辑说明
- 数据结构设计
- 错误处理策略
- 团队协作需求

### 练习7: 注释风格统一练习
**任务**：统一代码的注释风格

**要求**：
- 选择一致的注释格式
- 保持术语统一
- 遵循团队规范

## 练习提示

### 自我检查清单
- □ 注释是否解释了代码的目的而不是重复代码？
- □ 文档字符串是否包含了所有必要信息？
- □ 注释是否与代码保持同步？
- □ 是否避免了过度注释？
- □ 注释风格是否在整个项目中保持一致？
- □ 复杂算法是否有足够的解释？
- □ 是否使用了适当的TODO、FIXME等标记？

### 学习建议
1. **循序渐进**：从简单的变量注释开始，逐步练习复杂的文档字符串
2. **对比学习**：参考其他示例文件的注释风格
3. **实践应用**：在实际项目中应用所学的注释技巧
4. **团队讨论**：与团队成员讨论注释规范和最佳实践
5. **持续改进**：定期回顾和改进自己的注释质量

## 运行示例

```bash
# 运行练习文件
python 06_exercises.py
```

**输出结果**：
```
=== Python注释练习题 ===

--- 练习1: 基础注释练习 ---
平均分: 86.10
及格率: 100.0%

--- 练习2: 函数文档字符串练习 ---
BMI: 22.86, 分类: 正常
第10个斐波那契数: 55

--- 练习3: 类文档字符串练习 ---
计算结果: 15, 12, 256
计算历史: ['10 + 5 = 15', '3 × 4 = 12', '2 ^ 8 = 256']

--- 练习4: 注释改进练习 ---

--- 练习5: 复杂算法注释练习 ---
在数组 [1, 3, 5, 7, 9, 11, 13, 15] 中查找 7: 索引 3
排序前: [64, 34, 25, 12, 22, 11, 90]
排序后: [11, 12, 22, 25, 34, 64, 90]

--- 练习6: 实际项目注释练习 ---
学生统计: {'total_students': 2, 'average_gpa': 86.33, 'highest_gpa': 87.67, 'lowest_gpa': 85.0}
优秀学生:
  李四 (GPA: 87.67)
  张三 (GPA: 85.00)

--- 练习7: 注释风格统一练习 ---

=== 练习提示 ===
1. 练习1: 注释应该解释变量的用途和计算的业务含义
2. 练习2: 文档字符串应该包含完整的参数、返回值和异常说明
3. 练习3: 类文档字符串应该描述类的职责和使用方法
4. 练习4: 避免重复代码内容的注释，专注于解释'为什么'
5. 练习5: 算法注释应该解释思路、时间复杂度和关键步骤
6. 练习6: 项目代码注释应该考虑维护性和团队协作
7. 练习7: 保持注释风格的一致性很重要

=== 自我检查清单 ===
□ 注释是否解释了代码的目的而不是重复代码？
□ 文档字符串是否包含了所有必要信息？
□ 注释是否与代码保持同步？
□ 是否避免了过度注释？
□ 注释风格是否在整个项目中保持一致？
□ 复杂算法是否有足够的解释？
□ 是否使用了适当的TODO、FIXME等标记？
```

## 学习要点

1. **注释质量**：好的注释能显著提高代码的可读性和维护性
2. **实践练习**：通过大量练习培养良好的注释习惯
3. **风格一致**：在项目中保持统一的注释风格
4. **持续改进**：随着经验积累不断提高注释质量
5. **团队协作**：与团队成员共同制定和遵守注释规范

## 导航链接

- [返回目录](./index.md)
- [上一节：注释最佳实践](./comment-best-practices.md)
- [下一模块：05-operators](../05-operators/index.md)
- [Python基础教程首页](../index.md)