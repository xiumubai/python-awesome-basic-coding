#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lambda表达式基础

本文件介绍Lambda表达式的基本概念、语法和简单用法。
Lambda表达式是Python中创建匿名函数的一种方式。

学习目标：
1. 理解Lambda表达式的概念
2. 掌握Lambda表达式的基本语法
3. 学会使用Lambda表达式创建简单函数
4. 了解Lambda表达式的使用场景
"""

# 1. Lambda表达式的基本语法
print("=== 1. Lambda表达式的基本语法 ===")
print("Lambda表达式语法：lambda 参数: 表达式")
print()

# 最简单的Lambda表达式
simple_lambda = lambda: "Hello, Lambda!"
print(f"无参数Lambda: {simple_lambda()}")

# 单参数Lambda表达式
square = lambda x: x ** 2
print(f"平方函数: square(5) = {square(5)}")

# 多参数Lambda表达式
add = lambda x, y: x + y
print(f"加法函数: add(3, 4) = {add(3, 4)}")

# 三个参数的Lambda表达式
volume = lambda l, w, h: l * w * h
print(f"体积计算: volume(2, 3, 4) = {volume(2, 3, 4)}")
print()

# 2. Lambda表达式与变量
print("=== 2. Lambda表达式与变量 ===")

# 将Lambda表达式赋值给变量
multiply = lambda x, y: x * y
print(f"乘法函数: multiply(6, 7) = {multiply(6, 7)}")

# Lambda表达式可以使用外部变量
factor = 10
scale = lambda x: x * factor
print(f"缩放函数: scale(5) = {scale(5)}")
print()

# 3. Lambda表达式的条件判断
print("=== 3. Lambda表达式中的条件判断 ===")

# 使用三元运算符
max_value = lambda x, y: x if x > y else y
print(f"最大值函数: max_value(8, 12) = {max_value(8, 12)}")

# 判断奇偶数
is_even = lambda x: "偶数" if x % 2 == 0 else "奇数"
print(f"奇偶判断: is_even(7) = {is_even(7)}")
print(f"奇偶判断: is_even(8) = {is_even(8)}")

# 绝对值函数
abs_value = lambda x: x if x >= 0 else -x
print(f"绝对值函数: abs_value(-5) = {abs_value(-5)}")
print()

# 4. Lambda表达式的数据类型操作
print("=== 4. Lambda表达式的数据类型操作 ===")

# 字符串操作
uppercase = lambda s: s.upper()
print(f"转大写: uppercase('hello') = {uppercase('hello')}")

# 字符串长度
string_length = lambda s: len(s)
print(f"字符串长度: string_length('Python') = {string_length('Python')}")

# 列表操作
list_sum = lambda lst: sum(lst)
print(f"列表求和: list_sum([1, 2, 3, 4, 5]) = {list_sum([1, 2, 3, 4, 5])}")

# 字典操作
get_name = lambda person: person.get('name', '未知')
person_dict = {'name': '张三', 'age': 25}
print(f"获取姓名: get_name(person_dict) = {get_name(person_dict)}")
print()

# 5. Lambda表达式的实际应用示例
print("=== 5. Lambda表达式的实际应用示例 ===")

# 温度转换
celsius_to_fahrenheit = lambda c: c * 9/5 + 32
fahrenheit_to_celsius = lambda f: (f - 32) * 5/9

print(f"摄氏度转华氏度: 25°C = {celsius_to_fahrenheit(25):.1f}°F")
print(f"华氏度转摄氏度: 77°F = {fahrenheit_to_celsius(77):.1f}°C")

# 计算圆的面积
import math
circle_area = lambda r: math.pi * r ** 2
print(f"圆的面积: 半径5的圆面积 = {circle_area(5):.2f}")

# 计算复利
compound_interest = lambda principal, rate, time: principal * (1 + rate) ** time
print(f"复利计算: 本金1000，年利率5%，3年后 = {compound_interest(1000, 0.05, 3):.2f}")
print()

# 6. Lambda表达式的限制
print("=== 6. Lambda表达式的限制 ===")
print("Lambda表达式的限制：")
print("1. 只能包含表达式，不能包含语句")
print("2. 不能包含return语句（自动返回表达式的值）")
print("3. 不能包含赋值语句")
print("4. 不能包含循环或条件语句块")
print("5. 通常用于简单的单行函数")
print()

# 7. Lambda表达式 vs 普通函数对比
print("=== 7. Lambda表达式 vs 普通函数对比 ===")

# 普通函数
def normal_square(x):
    return x ** 2

# Lambda函数
lambda_square = lambda x: x ** 2

print(f"普通函数: normal_square(4) = {normal_square(4)}")
print(f"Lambda函数: lambda_square(4) = {lambda_square(4)}")
print("两者功能相同，但Lambda更简洁")
print()

# 8. 练习题
print("=== 8. 练习题 ===")
print("请尝试以下练习：")
print("1. 创建一个Lambda函数计算两个数的差")
print("2. 创建一个Lambda函数判断一个数是否为正数")
print("3. 创建一个Lambda函数计算字符串中的单词数量")
print("4. 创建一个Lambda函数返回列表中的最大值")
print()

# 练习答案
print("练习答案：")
subtract = lambda x, y: x - y
is_positive = lambda x: x > 0
word_count = lambda s: len(s.split())
max_in_list = lambda lst: max(lst) if lst else None

print(f"1. 差值函数: subtract(10, 3) = {subtract(10, 3)}")
print(f"2. 正数判断: is_positive(-5) = {is_positive(-5)}")
print(f"3. 单词计数: word_count('Hello Python World') = {word_count('Hello Python World')}")
print(f"4. 最大值: max_in_list([3, 7, 2, 9, 1]) = {max_in_list([3, 7, 2, 9, 1])}")

if __name__ == "__main__":
    print("\n=== Lambda表达式基础学习完成 ===")
    print("Lambda表达式是Python中创建简单匿名函数的强大工具")
    print("适用于需要简单函数作为参数的场景")
    print("下一步：学习Lambda表达式与普通函数的详细对比")