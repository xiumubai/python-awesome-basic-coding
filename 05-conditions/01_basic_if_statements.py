#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
基础if语句

本文件演示Python中最基本的if语句用法，包括：
1. 基本if语句语法
2. 条件表达式的写法
3. 代码块的缩进规则
4. 常见的条件判断场景

学习目标：
- 掌握if语句的基本语法
- 理解条件表达式的概念
- 学会使用缩进来组织代码块
- 能够编写简单的条件判断程序
"""

# 1. 最基本的if语句
print("=== 1. 基本if语句 ===")
age = 18
if age >= 18:
    print("你已经成年了！")
    print("可以独立做决定了。")

print("程序继续执行...")
print()

# 2. 不同类型的条件表达式
print("=== 2. 不同类型的条件表达式 ===")

# 数字比较
score = 85
if score >= 90:
    print("优秀！")

# 字符串比较
name = "Alice"
if name == "Alice":
    print(f"欢迎你，{name}！")

# 布尔值判断
is_student = True
if is_student:
    print("学生身份确认")

# 列表非空判断
my_list = [1, 2, 3]
if my_list:  # 非空列表为True
    print("列表不为空")

print()

# 3. 使用变量作为条件
print("=== 3. 使用变量作为条件 ===")
temperature = 25
hot_threshold = 30

if temperature > hot_threshold:
    print("今天很热！")

# 使用函数返回值作为条件
def is_even(number):
    """判断数字是否为偶数"""
    return number % 2 == 0

num = 8
if is_even(num):
    print(f"{num} 是偶数")

print()

# 4. 复杂条件表达式
print("=== 4. 复杂条件表达式 ===")
username = "admin"
password = "123456"

# 使用 and 连接多个条件
if username == "admin" and password == "123456":
    print("登录成功！")

# 使用 or 连接条件
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("今天是周末！")

# 使用 not 取反
is_raining = False
if not is_raining:
    print("今天没有下雨，可以出门！")

print()

# 5. 实际应用示例
print("=== 5. 实际应用示例 ===")

# 示例1：成绩等级判断
student_score = 88
if student_score >= 90:
    print("成绩等级：A")

# 示例2：用户权限检查
user_role = "admin"
if user_role == "admin":
    print("拥有管理员权限")
    print("可以访问所有功能")

# 示例3：商品库存检查
stock_quantity = 5
min_stock = 10
if stock_quantity < min_stock:
    print("库存不足，需要补货！")
    print(f"当前库存：{stock_quantity}，最低库存：{min_stock}")

print()

# 6. 常见错误和注意事项
print("=== 6. 常见错误和注意事项 ===")

# 正确的缩进
x = 5
if x > 0:
    print("x是正数")  # 正确：使用4个空格缩进
    print("这行也在if代码块内")  # 正确：保持相同缩进

# 条件表达式的括号（可选但推荐用于复杂表达式）
a, b, c = 1, 2, 3
if (a < b) and (b < c):
    print("a < b < c")

# 避免使用赋值运算符（=）而不是比较运算符（==）
value = 10
if value == 10:  # 正确：使用 == 进行比较
    print("value等于10")

print()
print("=== 程序结束 ===")

# 练习题
print("\n=== 练习题 ===")
print("1. 编写一个程序，判断一个数字是否为正数")
print("2. 编写一个程序，检查用户输入的密码长度是否至少8位")
print("3. 编写一个程序，判断今天是否是工作日（周一到周五）")
print("4. 编写一个程序，检查学生的出勤率是否达到80%以上")