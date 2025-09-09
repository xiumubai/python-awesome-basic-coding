#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lambda表达式与普通函数的对比

本文件详细对比Lambda表达式和普通函数的区别，
帮助理解何时使用Lambda表达式，何时使用普通函数。

学习目标：
1. 理解Lambda表达式与普通函数的语法差异
2. 掌握Lambda表达式与普通函数的性能差异
3. 学会选择合适的函数定义方式
4. 了解Lambda表达式的最佳使用场景
"""

import time
import sys

# 1. 语法对比
print("=== 1. 语法对比 ===")

# 普通函数定义
def add_normal(x, y):
    """普通函数：计算两个数的和"""
    return x + y

# Lambda表达式定义
add_lambda = lambda x, y: x + y

print("普通函数定义：")
print("def add_normal(x, y):")
print("    return x + y")
print()
print("Lambda表达式定义：")
print("add_lambda = lambda x, y: x + y")
print()
print(f"普通函数调用: add_normal(3, 5) = {add_normal(3, 5)}")
print(f"Lambda函数调用: add_lambda(3, 5) = {add_lambda(3, 5)}")
print()

# 2. 功能复杂度对比
print("=== 2. 功能复杂度对比 ===")

# 复杂的普通函数
def calculate_grade(score):
    """根据分数计算等级"""
    if score >= 90:
        grade = 'A'
        message = "优秀"
    elif score >= 80:
        grade = 'B'
        message = "良好"
    elif score >= 70:
        grade = 'C'
        message = "中等"
    elif score >= 60:
        grade = 'D'
        message = "及格"
    else:
        grade = 'F'
        message = "不及格"
    
    return f"等级: {grade}, 评价: {message}"

# 简单的Lambda表达式（只能处理简单逻辑）
simple_grade = lambda score: 'A' if score >= 90 else ('B' if score >= 80 else 'C')

print("复杂逻辑 - 普通函数：")
print(f"calculate_grade(85) = {calculate_grade(85)}")
print(f"calculate_grade(55) = {calculate_grade(55)}")
print()
print("简单逻辑 - Lambda表达式：")
print(f"simple_grade(85) = {simple_grade(85)}")
print(f"simple_grade(95) = {simple_grade(95)}")
print()
print("结论：复杂逻辑应使用普通函数，简单逻辑可使用Lambda")
print()

# 3. 可读性对比
print("=== 3. 可读性对比 ===")

# 可读性好的普通函数
def is_valid_email(email):
    """检查邮箱地址是否有效"""
    if '@' not in email:
        return False
    
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    username, domain = parts
    if not username or not domain:
        return False
    
    if '.' not in domain:
        return False
    
    return True

# 可读性差的Lambda表达式（不推荐）
is_valid_email_lambda = lambda email: '@' in email and len(email.split('@')) == 2 and all(email.split('@')) and '.' in email.split('@')[1]

test_email = "user@example.com"
print(f"普通函数检查邮箱: is_valid_email('{test_email}') = {is_valid_email(test_email)}")
print(f"Lambda检查邮箱: is_valid_email_lambda('{test_email}') = {is_valid_email_lambda(test_email)}")
print()
print("结论：复杂逻辑用普通函数更易读和维护")
print()

# 4. 性能对比
print("=== 4. 性能对比 ===")

# 性能测试函数
def performance_test(func, *args, iterations=1000000):
    """测试函数性能"""
    start_time = time.time()
    for _ in range(iterations):
        func(*args)
    end_time = time.time()
    return end_time - start_time

# 测试简单运算
def multiply_normal(x, y):
    return x * y

multiply_lambda = lambda x, y: x * y

# 性能测试
normal_time = performance_test(multiply_normal, 5, 3)
lambda_time = performance_test(multiply_lambda, 5, 3)

print(f"普通函数执行时间: {normal_time:.6f} 秒")
print(f"Lambda函数执行时间: {lambda_time:.6f} 秒")
print(f"性能差异: {abs(normal_time - lambda_time):.6f} 秒")
print("结论：简单操作的性能差异微乎其微")
print()

# 5. 内存占用对比
print("=== 5. 内存占用对比 ===")

# 检查函数对象大小
print(f"普通函数对象大小: {sys.getsizeof(multiply_normal)} 字节")
print(f"Lambda函数对象大小: {sys.getsizeof(multiply_lambda)} 字节")
print("结论：内存占用基本相同")
print()

# 6. 调试和错误处理对比
print("=== 6. 调试和错误处理对比 ===")

# 普通函数 - 易于调试
def divide_normal(x, y):
    """普通除法函数，包含错误处理"""
    if y == 0:
        raise ValueError("除数不能为零")
    return x / y

# Lambda表达式 - 难以调试
divide_lambda = lambda x, y: x / y if y != 0 else None

print("普通函数错误处理：")
try:
    result = divide_normal(10, 0)
except ValueError as e:
    print(f"捕获错误: {e}")

print("\nLambda表达式错误处理：")
result = divide_lambda(10, 0)
print(f"Lambda结果: {result}")
print("结论：普通函数更适合需要错误处理的场景")
print()

# 7. 文档和注释对比
print("=== 7. 文档和注释对比 ===")

# 普通函数 - 支持完整文档
def calculate_bmi(weight, height):
    """
    计算身体质量指数(BMI)
    
    参数:
        weight (float): 体重，单位：千克
        height (float): 身高，单位：米
    
    返回:
        float: BMI值
    
    示例:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    return weight / (height ** 2)

# Lambda表达式 - 无法添加详细文档
bmi_lambda = lambda w, h: w / (h ** 2)  # 只能添加简单注释

print("普通函数文档：")
print(calculate_bmi.__doc__)
print(f"\nLambda函数: {bmi_lambda.__doc__}")
print("结论：普通函数支持完整的文档字符串")
print()

# 8. 使用场景对比
print("=== 8. 使用场景对比 ===")

print("Lambda表达式适用场景：")
print("1. 简单的单行表达式")
print("2. 作为高阶函数的参数（如map, filter, sort）")
print("3. 临时使用的简单函数")
print("4. 函数式编程风格")
print()

print("普通函数适用场景：")
print("1. 复杂的业务逻辑")
print("2. 需要详细文档的函数")
print("3. 需要错误处理的函数")
print("4. 多次重用的函数")
print("5. 需要调试的函数")
print()

# 9. 实际应用示例
print("=== 9. 实际应用示例 ===")

# 数据处理示例
students = [
    {'name': '张三', 'age': 20, 'score': 85},
    {'name': '李四', 'age': 19, 'score': 92},
    {'name': '王五', 'age': 21, 'score': 78},
    {'name': '赵六', 'age': 20, 'score': 88}
]

# 使用Lambda表达式进行简单排序
students_by_score = sorted(students, key=lambda x: x['score'], reverse=True)
print("按分数排序（使用Lambda）：")
for student in students_by_score:
    print(f"{student['name']}: {student['score']}分")
print()

# 使用普通函数进行复杂处理
def get_student_summary(student):
    """获取学生综合信息"""
    name = student['name']
    age = student['age']
    score = student['score']
    
    if score >= 90:
        level = "优秀"
    elif score >= 80:
        level = "良好"
    else:
        level = "一般"
    
    return f"{name}（{age}岁）- {score}分 - {level}"

print("学生综合信息（使用普通函数）：")
for student in students:
    print(get_student_summary(student))
print()

# 10. 最佳实践建议
print("=== 10. 最佳实践建议 ===")
print("选择Lambda表达式的情况：")
print("✓ 函数逻辑简单（1-2行代码）")
print("✓ 只使用一次或很少使用")
print("✓ 作为高阶函数的参数")
print("✓ 不需要复杂的错误处理")
print()
print("选择普通函数的情况：")
print("✓ 函数逻辑复杂（多行代码）")
print("✓ 需要详细的文档说明")
print("✓ 需要错误处理和调试")
print("✓ 会被多次重用")
print("✓ 需要单元测试")

if __name__ == "__main__":
    print("\n=== Lambda表达式与普通函数对比学习完成 ===")
    print("理解两者的差异有助于选择合适的函数定义方式")
    print("下一步：学习Lambda表达式与map函数的结合使用")