#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
多行注释的使用

本文件演示Python中多行注释的各种使用方法。
Python没有专门的多行注释语法，但可以通过以下方式实现：
1. 使用多个单行注释（#）
2. 使用三重引号字符串（""" 或 '''）

作者: Python学习教程
日期: 2024
"""

# 方法1: 使用多个单行注释创建多行注释
# 这是多行注释的第一行
# 这是多行注释的第二行
# 这是多行注释的第三行
# 每一行都需要以#开头

print("演示多行注释的使用")

# 方法2: 使用三重双引号创建多行注释
"""
这是使用三重双引号创建的多行注释
可以跨越多行
不需要在每行前面加#号
但是要注意，这实际上是一个字符串字面量
如果不赋值给变量，Python会忽略它
"""

# 方法3: 使用三重单引号创建多行注释
'''
这是使用三重单引号创建的多行注释
效果与三重双引号相同
可以根据个人喜好选择使用哪种
'''

# ============================================================
# 多行注释的实际应用场景
# ============================================================

# 场景1: 详细的算法说明
"""
冒泡排序算法实现

算法原理：
1. 比较相邻的两个元素
2. 如果前一个元素大于后一个元素，则交换它们的位置
3. 重复这个过程，直到没有需要交换的元素
4. 每一轮都会将最大的元素"冒泡"到数组的末尾

时间复杂度: O(n²)
空间复杂度: O(1)
"""

def bubble_sort(arr):
    n = len(arr)
    # 外层循环控制排序轮数
    for i in range(n):
        # 内层循环进行相邻元素比较
        for j in range(0, n - i - 1):
            # 如果前一个元素大于后一个元素，则交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 测试冒泡排序
test_list = [64, 34, 25, 12, 22, 11, 90]
print(f"排序前: {test_list}")
sorted_list = bubble_sort(test_list.copy())
print(f"排序后: {sorted_list}")

# 场景2: 复杂功能的详细说明
'''
用户注册系统

功能描述：
- 验证用户名格式（长度3-20字符，只能包含字母、数字、下划线）
- 验证密码强度（至少8位，包含大小写字母、数字和特殊字符）
- 验证邮箱格式
- 检查用户名和邮箱是否已存在
- 密码加密存储

返回值：
- 成功：返回用户ID
- 失败：返回错误信息
'''

def register_user(username, password, email):
    # 这里只是示例，实际应用中需要更完善的验证
    if len(username) < 3 or len(username) > 20:
        return "用户名长度必须在3-20字符之间"
    
    if len(password) < 8:
        return "密码长度至少8位"
    
    if "@" not in email:
        return "邮箱格式不正确"
    
    # 模拟注册成功
    return f"用户 {username} 注册成功"

# 测试用户注册
result = register_user("testuser", "password123", "test@example.com")
print(result)

# 场景3: 临时禁用大段代码
"""
以下代码块被临时注释掉，用于调试或测试

def old_function():
    print("这是旧版本的函数")
    # 一些复杂的逻辑
    for i in range(10):
        print(f"处理第 {i} 项")
    return "处理完成"

# 调用旧函数
result = old_function()
print(result)
"""

# 场景4: 版权和许可信息
"""
Copyright (c) 2024 Python学习教程

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
"""

# 场景5: 配置说明
'''
数据库配置参数说明：

HOST: 数据库服务器地址
PORT: 数据库端口号（MySQL默认3306，PostgreSQL默认5432）
DATABASE: 数据库名称
USERNAME: 数据库用户名
PASSWORD: 数据库密码
CHARSET: 字符编码（推荐utf8mb4）
TIMEZONE: 时区设置
'''

db_config = {
    "host": "localhost",
    "port": 3306,
    "database": "test_db",
    "username": "root",
    "password": "password",
    "charset": "utf8mb4"
}

print(f"数据库配置: {db_config}")

# ============================================================
# 多行注释的注意事项
# ============================================================

"""
注意事项：

1. 三重引号字符串实际上是字符串字面量，不是真正的注释
2. 如果在函数或类的开头使用三重引号，它会被当作文档字符串（docstring）
3. 多行注释应该用于解释复杂的逻辑，而不是显而易见的代码
4. 保持注释与代码同步更新
5. 避免过度注释，让代码本身具有可读性
"""

print("\n=== 多行注释演示完成 ===")
print("多行注释适用于详细说明、算法描述、版权信息等场景")
print("选择合适的注释方式可以提高代码的可读性和维护性")

# 运行这个文件来查看多行注释的效果
# 在终端中执行: python 02_multi_line_comments.py