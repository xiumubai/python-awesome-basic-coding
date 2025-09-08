#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
循环控制 - break语句

break语句用于立即退出循环，不再执行循环体中剩余的代码，
也不会执行循环的else子句（如果有的话）。

学习目标：
1. 理解break语句的作用和使用场景
2. 掌握在for循环和while循环中使用break
3. 了解break在嵌套循环中的行为
4. 学会使用break实现特定的控制逻辑
"""

# 1. 基本的break使用
print("=== 1. 基本的break使用 ===")

# 在for循环中使用break
print("在for循环中使用break:")
for i in range(10):
    if i == 5:
        print(f"遇到{i}，退出循环")
        break
    print(f"当前数字: {i}")
print("循环结束\n")

# 在while循环中使用break
print("在while循环中使用break:")
count = 0
while True:  # 无限循环
    print(f"计数: {count}")
    count += 1
    if count >= 3:
        print("达到条件，退出循环")
        break
print("while循环结束\n")

# 2. 实际应用场景
print("=== 2. 实际应用场景 ===")

# 查找特定元素
print("查找特定元素:")
numbers = [1, 3, 7, 9, 12, 15, 18]
target = 12
found = False

for i, num in enumerate(numbers):
    if num == target:
        print(f"找到目标数字 {target}，位置: {i}")
        found = True
        break
    print(f"检查数字: {num}")

if not found:
    print(f"未找到目标数字 {target}")
print()

# 用户输入验证
print("用户输入验证示例:")
valid_commands = ['start', 'stop', 'pause', 'quit']

# 模拟用户输入
user_inputs = ['hello', 'world', 'start', 'continue']

for user_input in user_inputs:
    print(f"用户输入: {user_input}")
    if user_input in valid_commands:
        print(f"有效命令: {user_input}")
        break
    else:
        print("无效命令，请重新输入")
print()

# 3. 嵌套循环中的break
print("=== 3. 嵌套循环中的break ===")

# break只影响最内层循环
print("break只影响最内层循环:")
for i in range(3):
    print(f"外层循环: {i}")
    for j in range(5):
        if j == 2:
            print(f"  内层循环在j={j}时break")
            break
        print(f"  内层循环: {j}")
    print(f"外层循环{i}继续执行")
print()

# 使用标志变量控制外层循环
print("使用标志变量控制外层循环:")
found_target = False
for i in range(3):
    if found_target:
        break
    print(f"外层循环: {i}")
    for j in range(5):
        if i == 1 and j == 2:
            print(f"  在位置({i}, {j})找到目标")
            found_target = True
            break
        print(f"  内层循环: ({i}, {j})")
print()

# 4. break与else子句
print("=== 4. break与else子句 ===")

# 正常结束的循环会执行else
print("正常结束的循环:")
for i in range(3):
    print(f"循环: {i}")
else:
    print("循环正常结束，执行else子句")
print()

# 被break中断的循环不会执行else
print("被break中断的循环:")
for i in range(5):
    if i == 2:
        print(f"在i={i}时break")
        break
    print(f"循环: {i}")
else:
    print("这行不会被执行")
print("循环被break中断\n")

# 5. 实用的break模式
print("=== 5. 实用的break模式 ===")

# 模式1: 找到第一个满足条件的元素
print("找到第一个偶数:")
numbers = [1, 3, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"第一个偶数: {num}")
        break
print()

# 模式2: 限制循环次数
print("限制尝试次数:")
max_attempts = 3
attempt = 0

while attempt < max_attempts:
    attempt += 1
    print(f"尝试第 {attempt} 次")
    
    # 模拟某种条件检查
    if attempt == 2:  # 假设第2次成功
        print("操作成功！")
        break
else:
    print("达到最大尝试次数，操作失败")
print()

# 模式3: 处理数据直到遇到特殊标记
print("处理数据直到遇到结束标记:")
data = ['apple', 'banana', 'END', 'cherry', 'date']
processed = []

for item in data:
    if item == 'END':
        print("遇到结束标记，停止处理")
        break
    processed.append(item.upper())
    print(f"处理: {item} -> {item.upper()}")

print(f"已处理的数据: {processed}")
print()

# 6. break的最佳实践
print("=== 6. break的最佳实践 ===")

# 使用有意义的条件
print("使用有意义的条件:")
passwords = ['123', 'password', 'admin123', 'secret']
correct_password = 'admin123'

for password in passwords:
    print(f"尝试密码: {password}")
    if password == correct_password:
        print("密码正确，登录成功！")
        break
    print("密码错误")
else:
    print("所有密码都不正确")

print("\n=== break语句学习总结 ===")
print("1. break用于立即退出当前循环")
print("2. 只影响最内层的循环")
print("3. 被break中断的循环不会执行else子句")
print("4. 常用于查找、验证、错误处理等场景")
print("5. 配合标志变量可以控制外层循环")