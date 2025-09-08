#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
函数返回值详解

本文件演示Python函数返回值的各种用法，包括：
1. 无返回值的函数
2. 单个返回值
3. 多个返回值
4. 不同类型的返回值
5. 条件返回
6. 早期返回

作者：Python学习教程
日期：2024年
"""

print("=" * 50)
print("Python 函数返回值详解")
print("=" * 50)

# 1. 无返回值的函数
print("\n1. 无返回值的函数")
print("-" * 30)

def print_message(message):
    """无返回值的函数，只执行操作"""
    print(f"消息：{message}")
    # 没有return语句，函数默认返回None

def save_data(data):
    """模拟保存数据，无返回值"""
    print(f"正在保存数据：{data}")
    print("数据保存完成")

# 调用无返回值的函数
print("调用无返回值的函数：")
print_message("Hello World")
result = print_message("测试消息")
print(f"函数返回值：{result}")  # None

save_data("重要文件")
print()

# 2. 单个返回值
print("\n2. 单个返回值")
print("-" * 30)

def add(a, b):
    """返回两个数的和"""
    return a + b

def get_greeting(name):
    """返回问候语字符串"""
    return f"Hello, {name}!"

def is_even(number):
    """返回布尔值，判断是否为偶数"""
    return number % 2 == 0

# 使用单个返回值
print("单个返回值示例：")
sum_result = add(5, 3)
print(f"5 + 3 = {sum_result}")

greeting = get_greeting("Alice")
print(greeting)

print(f"4是偶数吗？{is_even(4)}")
print(f"7是偶数吗？{is_even(7)}")
print()

# 3. 多个返回值
print("\n3. 多个返回值")
print("-" * 30)

def get_name_age():
    """返回姓名和年龄"""
    return "张三", 25

def calculate_circle(radius):
    """计算圆的面积和周长"""
    import math
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

def get_min_max(numbers):
    """返回列表中的最小值和最大值"""
    if not numbers:
        return None, None
    return min(numbers), max(numbers)

# 使用多个返回值
print("多个返回值示例：")
name, age = get_name_age()
print(f"姓名：{name}，年龄：{age}")

area, circumference = calculate_circle(5)
print(f"半径为5的圆：面积={area:.2f}，周长={circumference:.2f}")

numbers = [1, 5, 3, 9, 2, 7]
min_val, max_val = get_min_max(numbers)
print(f"列表{numbers}的最小值：{min_val}，最大值：{max_val}")
print()

# 4. 不同类型的返回值
print("\n4. 不同类型的返回值")
print("-" * 30)

def get_user_info(user_id):
    """返回字典类型的用户信息"""
    users = {
        1: {"name": "Alice", "email": "alice@example.com", "age": 25},
        2: {"name": "Bob", "email": "bob@example.com", "age": 30}
    }
    return users.get(user_id, {})

def get_fibonacci(n):
    """返回斐波那契数列（列表类型）"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def create_multiplier(factor):
    """返回函数类型"""
    def multiply(x):
        return x * factor
    return multiply

# 使用不同类型的返回值
print("不同类型返回值示例：")
user = get_user_info(1)
print(f"用户信息：{user}")

fib_sequence = get_fibonacci(8)
print(f"斐波那契数列（前8项）：{fib_sequence}")

double = create_multiplier(2)
triple = create_multiplier(3)
print(f"使用返回的函数：double(5) = {double(5)}, triple(4) = {triple(4)}")
print()

# 5. 条件返回
print("\n5. 条件返回")
print("-" * 30)

def divide(a, b):
    """安全除法，根据条件返回不同结果"""
    if b == 0:
        return None  # 除数为0时返回None
    return a / b

def get_grade(score):
    """根据分数返回等级"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def find_item(items, target):
    """在列表中查找项目，返回索引或-1"""
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1

# 使用条件返回
print("条件返回示例：")
print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")

scores = [95, 87, 76, 65, 45]
for score in scores:
    grade = get_grade(score)
    print(f"分数{score}对应等级：{grade}")

fruits = ["apple", "banana", "orange"]
print(f"查找'banana'：索引{find_item(fruits, 'banana')}")
print(f"查找'grape'：索引{find_item(fruits, 'grape')}")
print()

# 6. 早期返回（Early Return）
print("\n6. 早期返回（Early Return）")
print("-" * 30)

def validate_and_process(data):
    """验证数据并处理，使用早期返回"""
    # 早期返回：数据为空
    if not data:
        return "错误：数据为空"
    
    # 早期返回：数据类型错误
    if not isinstance(data, list):
        return "错误：数据必须是列表"
    
    # 早期返回：列表为空
    if len(data) == 0:
        return "错误：列表不能为空"
    
    # 正常处理
    processed = [item * 2 for item in data if isinstance(item, (int, float))]
    return f"处理完成：{processed}"

def calculate_discount(price, customer_type):
    """计算折扣，使用早期返回"""
    # 早期返回：价格无效
    if price <= 0:
        return 0
    
    # 早期返回：VIP客户
    if customer_type == "VIP":
        return price * 0.8  # 8折
    
    # 早期返回：会员客户
    if customer_type == "Member":
        return price * 0.9  # 9折
    
    # 普通客户
    return price

# 使用早期返回
print("早期返回示例：")
test_data = [
    [1, 2, 3, 4],
    [],
    "not a list",
    None,
    [1, 2, "text", 3.5]
]

for data in test_data:
    result = validate_and_process(data)
    print(f"处理 {data}：{result}")

print("\n折扣计算：")
customers = [
    (100, "VIP"),
    (100, "Member"),
    (100, "Regular"),
    (-50, "VIP")
]

for price, customer_type in customers:
    final_price = calculate_discount(price, customer_type)
    print(f"原价{price}，客户类型{customer_type}，最终价格：{final_price}")

# 7. 返回值的解包和忽略
print("\n7. 返回值的解包和忽略")
print("-" * 30)

def get_statistics(numbers):
    """返回统计信息：平均值、最小值、最大值、总和"""
    if not numbers:
        return 0, 0, 0, 0
    
    avg = sum(numbers) / len(numbers)
    min_val = min(numbers)
    max_val = max(numbers)
    total = sum(numbers)
    return avg, min_val, max_val, total

# 完全解包
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
avg, min_val, max_val, total = get_statistics(data)
print(f"完全解包：平均值={avg:.1f}, 最小值={min_val}, 最大值={max_val}, 总和={total}")

# 部分解包（忽略某些返回值）
avg, _, max_val, _ = get_statistics(data)
print(f"部分解包：平均值={avg:.1f}, 最大值={max_val}")

# 获取所有返回值作为元组
stats = get_statistics(data)
print(f"元组形式：{stats}")

print("\n=" * 50)
print("函数返回值学习完成！")
print("=" * 50)
print("\n总结：")
print("1. 函数可以没有返回值（返回None）")
print("2. 函数可以返回单个值")
print("3. 函数可以返回多个值（元组形式）")
print("4. 返回值可以是任何Python数据类型")
print("5. 可以根据条件返回不同的值")
print("6. 早期返回可以简化代码逻辑")
print("7. 多个返回值可以解包或部分忽略")