#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
单行注释的使用

本文件演示Python中单行注释的各种使用方法和最佳实践。
单行注释使用井号(#)开头，从井号到行末的所有内容都被视为注释。

作者: Python学习教程
日期: 2024
"""

# 这是一个单行注释
# 注释用于解释代码的功能和目的

# 1. 基本的单行注释
print("Hello, World!")  # 这也是一个单行注释，位于代码行的末尾

# 2. 用于解释变量的用途
name = "张三"  # 存储用户姓名
age = 25      # 存储用户年龄
score = 95.5  # 存储考试成绩

print(f"姓名: {name}")
print(f"年龄: {age}")
print(f"成绩: {score}")

# 3. 用于解释复杂的计算过程
# 计算圆的面积
# 公式: 面积 = π × 半径²
radius = 5
pi = 3.14159
area = pi * radius ** 2  # 使用幂运算计算半径的平方
print(f"半径为 {radius} 的圆的面积是: {area}")

# 4. 用于标记代码段落
# ==================== 数据处理部分 ====================
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)  # 计算列表中所有数字的总和
average = total / len(numbers)  # 计算平均值

print(f"数字列表: {numbers}")
print(f"总和: {total}")
print(f"平均值: {average}")

# ==================== 条件判断部分 ====================
# 判断成绩等级
if score >= 90:
    grade = "优秀"  # 90分及以上为优秀
elif score >= 80:
    grade = "良好"  # 80-89分为良好
elif score >= 70:
    grade = "中等"  # 70-79分为中等
elif score >= 60:
    grade = "及格"  # 60-69分为及格
else:
    grade = "不及格"  # 60分以下为不及格

print(f"成绩等级: {grade}")

# 5. 临时禁用代码（注释掉不需要执行的代码）
# print("这行代码被注释掉了，不会执行")
# debug_mode = True
# if debug_mode:
#     print("调试信息")

# 6. 添加TODO标记
# TODO: 添加输入验证功能
# TODO: 优化计算性能
# FIXME: 修复除零错误
# NOTE: 这里需要特别注意数据类型

# 7. 版权和许可信息
# Copyright (c) 2024 Python学习教程
# Licensed under MIT License

print("\n=== 单行注释演示完成 ===")
print("单行注释是Python编程中最常用的注释方式")
print("合理使用注释可以让代码更易读、更易维护")

# 运行这个文件来查看单行注释的效果
# 在终端中执行: python 01_single_line_comments.py