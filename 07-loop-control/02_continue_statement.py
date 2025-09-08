#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
循环控制 - continue语句

continue语句用于跳过当前循环迭代中剩余的代码，
直接进入下一次循环迭代。

学习目标：
1. 理解continue语句的作用和使用场景
2. 掌握在for循环和while循环中使用continue
3. 了解continue与break的区别
4. 学会使用continue实现条件过滤
"""

# 1. 基本的continue使用
print("=== 1. 基本的continue使用 ===")

# 在for循环中使用continue
print("在for循环中跳过偶数:")
for i in range(10):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(f"奇数: {i}")
print()

# 在while循环中使用continue
print("在while循环中跳过特定值:")
count = 0
while count < 8:
    count += 1
    if count == 3 or count == 6:
        print(f"跳过数字 {count}")
        continue
    print(f"处理数字: {count}")
print()

# 2. continue与break的对比
print("=== 2. continue与break的对比 ===")

# 使用continue - 跳过当前迭代
print("使用continue - 跳过5，继续循环:")
for i in range(8):
    if i == 5:
        print(f"跳过 {i}")
        continue
    print(f"处理: {i}")
print("循环完成\n")

# 使用break - 完全退出循环
print("使用break - 遇到5就退出:")
for i in range(8):
    if i == 5:
        print(f"遇到 {i}，退出循环")
        break
    print(f"处理: {i}")
print("循环结束\n")

# 3. 实际应用场景
print("=== 3. 实际应用场景 ===")

# 数据过滤和处理
print("过滤和处理数据:")
data = [1, -2, 3, 0, -5, 7, 8, -1]
positive_sum = 0

for num in data:
    if num <= 0:
        print(f"跳过非正数: {num}")
        continue
    positive_sum += num
    print(f"累加正数: {num}，当前总和: {positive_sum}")

print(f"所有正数的和: {positive_sum}\n")

# 字符串处理
print("处理字符串，跳过空格和特殊字符:")
text = "Hello, World! 123"
letters_only = ""

for char in text:
    if not char.isalpha():
        print(f"跳过非字母字符: '{char}'")
        continue
    letters_only += char
    print(f"保留字母: '{char}'")

print(f"只包含字母的结果: {letters_only}\n")

# 4. 处理列表中的无效数据
print("=== 4. 处理列表中的无效数据 ===")

# 处理包含None和无效值的列表
print("处理包含无效值的列表:")
scores = [85, None, 92, 'invalid', 78, 0, 95, -10]
valid_scores = []

for score in scores:
    # 跳过None值
    if score is None:
        print(f"跳过None值")
        continue
    
    # 跳过非数字类型
    if not isinstance(score, (int, float)):
        print(f"跳过非数字类型: {score}")
        continue
    
    # 跳过无效分数范围
    if score < 0 or score > 100:
        print(f"跳过无效分数: {score}")
        continue
    
    valid_scores.append(score)
    print(f"有效分数: {score}")

print(f"有效分数列表: {valid_scores}")
if valid_scores:
    average = sum(valid_scores) / len(valid_scores)
    print(f"平均分: {average:.2f}\n")

# 5. 嵌套循环中的continue
print("=== 5. 嵌套循环中的continue ===")

# continue只影响最内层循环
print("嵌套循环中的continue:")
for i in range(3):
    print(f"外层循环: {i}")
    for j in range(5):
        if j == 2:
            print(f"  跳过内层循环的j={j}")
            continue
        print(f"  内层循环: {j}")
    print(f"外层循环{i}完成")
print()

# 6. 复杂的条件过滤
print("=== 6. 复杂的条件过滤 ===")

# 处理用户数据
print("处理用户数据:")
users = [
    {'name': 'Alice', 'age': 25, 'active': True},
    {'name': '', 'age': 30, 'active': True},
    {'name': 'Bob', 'age': 17, 'active': True},
    {'name': 'Charlie', 'age': 35, 'active': False},
    {'name': 'David', 'age': 28, 'active': True}
]

valid_users = []

for user in users:
    # 跳过没有姓名的用户
    if not user['name']:
        print(f"跳过无姓名用户")
        continue
    
    # 跳过未成年用户
    if user['age'] < 18:
        print(f"跳过未成年用户: {user['name']}")
        continue
    
    # 跳过非活跃用户
    if not user['active']:
        print(f"跳过非活跃用户: {user['name']}")
        continue
    
    valid_users.append(user)
    print(f"有效用户: {user['name']}, 年龄: {user['age']}")

print(f"有效用户数量: {len(valid_users)}\n")

# 7. 文件处理模拟
print("=== 7. 文件处理模拟 ===")

# 处理日志文件行
print("处理日志文件:")
log_lines = [
    "2024-01-01 INFO: 系统启动",
    "2024-01-01 DEBUG: 调试信息",
    "",  # 空行
    "2024-01-01 ERROR: 发生错误",
    "# 这是注释行",
    "2024-01-01 INFO: 处理完成",
    "   ",  # 只有空格的行
    "2024-01-01 WARNING: 警告信息"
]

error_count = 0
info_count = 0

for line in log_lines:
    # 跳过空行
    if not line.strip():
        print("跳过空行")
        continue
    
    # 跳过注释行
    if line.strip().startswith('#'):
        print(f"跳过注释行: {line.strip()}")
        continue
    
    # 跳过调试信息
    if 'DEBUG' in line:
        print(f"跳过调试信息")
        continue
    
    # 统计错误和信息
    if 'ERROR' in line:
        error_count += 1
        print(f"错误日志: {line}")
    elif 'INFO' in line:
        info_count += 1
        print(f"信息日志: {line}")
    elif 'WARNING' in line:
        print(f"警告日志: {line}")

print(f"\n统计结果 - 错误: {error_count}, 信息: {info_count}\n")

# 8. continue的最佳实践
print("=== 8. continue的最佳实践 ===")

# 早期返回模式
print("使用早期返回模式提高代码可读性:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = []

for num in numbers:
    # 使用continue实现早期返回，避免深层嵌套
    if num % 2 == 0:
        continue  # 跳过偶数
    
    if num < 5:
        continue  # 跳过小于5的数
    
    # 只处理大于等于5的奇数
    result = num * 2
    results.append(result)
    print(f"处理 {num} -> {result}")

print(f"处理结果: {results}")

print("\n=== continue语句学习总结 ===")
print("1. continue用于跳过当前迭代，继续下一次循环")
print("2. 只影响最内层的循环")
print("3. 常用于数据过滤和条件处理")
print("4. 可以避免深层的if-else嵌套")
print("5. 与break配合使用可以实现复杂的循环控制")