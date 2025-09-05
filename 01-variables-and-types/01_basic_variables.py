#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第一课：基本变量定义和赋值

学习目标：
1. 理解什么是变量
2. 学会如何定义变量
3. 掌握变量赋值的基本语法
4. 了解变量在内存中的存储概念

作者：Python基础教程
日期：2024年
"""

print("=" * 50)
print("第一课：基本变量定义和赋值")
print("=" * 50)

# 1. 什么是变量？
print("\n1. 什么是变量？")
print("-" * 20)
print("变量就像一个容器，用来存储数据")
print("变量有名字，可以通过名字来访问存储的数据")

# 2. 基本变量定义和赋值
print("\n2. 基本变量定义和赋值")
print("-" * 20)

# 定义一个存储姓名的变量
name = "张三"
print(f"姓名变量：name = {name}")
print(f"变量name的值是：{name}")

# 定义一个存储年龄的变量
age = 25
print(f"年龄变量：age = {age}")
print(f"变量age的值是：{age}")

# 定义一个存储身高的变量
height = 175.5
print(f"身高变量：height = {height}")
print(f"变量height的值是：{height}")

# 定义一个存储是否是学生的变量
is_student = True
print(f"学生状态变量：is_student = {is_student}")
print(f"变量is_student的值是：{is_student}")

# 3. 变量赋值的语法规则
print("\n3. 变量赋值的语法规则")
print("-" * 20)
print("语法：变量名 = 值")
print("等号左边是变量名，等号右边是要存储的值")
print("注意：这里的等号不是数学中的等于，而是赋值操作")

# 4. 变量可以重新赋值
print("\n4. 变量可以重新赋值")
print("-" * 20)
print(f"原来的年龄：{age}")
age = 26  # 重新赋值
print(f"更新后的年龄：{age}")
print("变量的值可以随时改变")

# 5. 一次定义多个变量
print("\n5. 一次定义多个变量")
print("-" * 20)

# 方法1：分别赋值相同的值
x = y = z = 0
print(f"x = {x}, y = {y}, z = {z}")

# 方法2：同时赋值不同的值
a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")

# 方法3：交换变量的值
print(f"交换前：a = {a}, b = {b}")
a, b = b, a
print(f"交换后：a = {a}, b = {b}")

# 6. 变量的内存概念
print("\n6. 变量的内存概念")
print("-" * 20)
print("每个变量都有一个内存地址")
print(f"变量name的内存地址：{id(name)}")
print(f"变量age的内存地址：{id(age)}")
print("id()函数可以查看变量在内存中的地址")

# 7. 实践练习
print("\n7. 实践练习")
print("-" * 20)
print("请尝试定义以下变量：")
print("1. 定义一个变量存储你的姓名")
print("2. 定义一个变量存储你的年龄")
print("3. 定义一个变量存储你的爱好")
print("4. 打印这些变量的值")

# 练习示例
my_name = "李四"
my_age = 20
my_hobby = "编程"

print("\n练习答案示例：")
print(f"我的姓名：{my_name}")
print(f"我的年龄：{my_age}")
print(f"我的爱好：{my_hobby}")

# 8. 思考题
print("\n8. 思考题")
print("-" * 20)
print("1. 变量名可以是中文吗？")
print("2. 变量名可以以数字开头吗？")
print("3. 变量名可以包含空格吗？")
print("4. 什么是好的变量命名习惯？")

# 思考题答案
print("\n思考题答案：")
print("1. 可以，但不推荐")
print("2. 不可以，会报错")
print("3. 不可以，会报错")
print("4. 使用有意义的英文单词，遵循命名规范")

# 9. 常见错误示例
print("\n9. 常见错误示例")
print("-" * 20)
print("以下是一些常见的错误，请注意避免：")

# 错误1：变量名以数字开头（注释掉，因为会报错）
# 1name = "错误"  # SyntaxError
print("错误1：1name = '错误'  # 变量名不能以数字开头")

# 错误2：变量名包含空格（注释掉，因为会报错）
# my name = "错误"  # SyntaxError
print("错误2：my name = '错误'  # 变量名不能包含空格")

# 错误3：使用Python关键字作为变量名（注释掉，因为会报错）
# if = 5  # SyntaxError
print("错误3：if = 5  # 不能使用Python关键字作为变量名")

print("\n=" * 50)
print("第一课学习完成！")
print("下一课将学习Python的数据类型")
print("=" * 50)

# 运行这个文件的方法：
# 在终端中输入：python 01_basic_variables.py
# 或者在IDE中直接运行