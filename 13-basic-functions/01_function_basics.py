#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
函数基础语法

本文件演示Python函数的基础语法，包括：
1. 函数的定义和调用
2. 函数的基本结构
3. 函数命名规范
4. 简单的函数示例

作者：Python学习教程
日期：2024年
"""

print("=" * 50)
print("Python 函数基础语法")
print("=" * 50)

# 1. 最简单的函数定义
print("\n1. 最简单的函数定义")
print("-" * 30)

def greet():
    """最简单的函数，没有参数，没有返回值"""
    print("Hello, World!")

# 调用函数
print("调用greet()函数：")
greet()

# 2. 带参数的函数
print("\n2. 带参数的函数")
print("-" * 30)

def greet_person(name):
    """带一个参数的函数"""
    print(f"Hello, {name}!")

# 调用带参数的函数
print("调用greet_person('Alice')：")
greet_person('Alice')
print("调用greet_person('Bob')：")
greet_person('Bob')

# 3. 带多个参数的函数
print("\n3. 带多个参数的函数")
print("-" * 30)

def introduce(name, age):
    """带两个参数的函数"""
    print(f"我叫{name}，今年{age}岁")

# 调用带多个参数的函数
print("调用introduce('张三', 25)：")
introduce('张三', 25)
print("调用introduce('李四', 30)：")
introduce('李四', 30)

# 4. 带返回值的函数
print("\n4. 带返回值的函数")
print("-" * 30)

def add_numbers(a, b):
    """计算两个数的和并返回结果"""
    result = a + b
    return result

# 调用带返回值的函数
print("调用add_numbers(3, 5)：")
sum_result = add_numbers(3, 5)
print(f"结果：{sum_result}")

print("调用add_numbers(10, 20)：")
print(f"结果：{add_numbers(10, 20)}")

# 5. 函数的完整结构示例
print("\n5. 函数的完整结构示例")
print("-" * 30)

def calculate_area(length, width):
    """
    计算矩形面积
    
    参数:
        length (float): 矩形的长
        width (float): 矩形的宽
    
    返回:
        float: 矩形的面积
    """
    # 函数体：执行计算
    area = length * width
    
    # 返回结果
    return area

# 使用函数
print("计算矩形面积：")
length = 5.0
width = 3.0
area = calculate_area(length, width)
print(f"长{length}，宽{width}的矩形面积是：{area}")

# 6. 函数命名规范示例
print("\n6. 函数命名规范示例")
print("-" * 30)

# 好的函数命名（使用小写字母和下划线）
def get_user_name():
    """获取用户名"""
    return "用户123"

def calculate_total_price(price, quantity):
    """计算总价"""
    return price * quantity

def is_valid_email(email):
    """检查邮箱是否有效"""
    return "@" in email

# 使用这些函数
print(f"用户名：{get_user_name()}")
print(f"总价：{calculate_total_price(10.5, 3)}")
print(f"邮箱有效性：{is_valid_email('test@example.com')}")

# 7. 函数可以调用其他函数
print("\n7. 函数可以调用其他函数")
print("-" * 30)

def get_full_name(first_name, last_name):
    """获取全名"""
    return f"{first_name} {last_name}"

def create_greeting(first_name, last_name):
    """创建问候语，调用其他函数"""
    full_name = get_full_name(first_name, last_name)
    return f"欢迎，{full_name}！"

# 使用函数
greeting = create_greeting("张", "三")
print(greeting)

# 8. 函数的执行流程演示
print("\n8. 函数的执行流程演示")
print("-" * 30)

def demo_function(x):
    """演示函数执行流程"""
    print(f"  函数开始执行，参数x = {x}")
    result = x * 2
    print(f"  计算结果：{x} * 2 = {result}")
    print("  函数即将返回")
    return result

print("主程序：调用demo_function(5)")
result = demo_function(5)
print(f"主程序：函数返回值为 {result}")

# 9. 实用函数示例
print("\n9. 实用函数示例")
print("-" * 30)

def celsius_to_fahrenheit(celsius):
    """摄氏度转华氏度"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """华氏度转摄氏度"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# 温度转换示例
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f = 77
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c:.1f}°C")

print("\n=" * 50)
print("函数基础语法学习完成！")
print("=" * 50)
print("\n总结：")
print("1. 函数使用def关键字定义")
print("2. 函数名应该使用小写字母和下划线")
print("3. 函数可以有参数，也可以没有参数")
print("4. 函数可以有返回值，也可以没有返回值")
print("5. 函数可以调用其他函数")
print("6. 函数让代码更加模块化和可重用")