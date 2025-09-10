#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成器表达式

本模块介绍：
1. 生成器表达式的语法
2. 生成器表达式与列表推导式的区别
3. 生成器表达式的应用场景
4. 嵌套生成器表达式
5. 生成器表达式的性能优势
"""

import sys
import time
from collections.abc import Iterator

# 1. 生成器表达式的基本语法
print("=== 1. 生成器表达式的基本语法 ===")
print("生成器表达式语法: (expression for item in iterable)")
print("类似列表推导式，但使用圆括号而不是方括号")
print()

# 基本生成器表达式
numbers = [1, 2, 3, 4, 5]
squares_gen = (x ** 2 for x in numbers)
print(f"生成器表达式: {squares_gen}")
print(f"类型: {type(squares_gen)}")
print(f"是否为迭代器: {isinstance(squares_gen, Iterator)}")
print()

print("遍历生成器表达式:")
for square in squares_gen:
    print(f"平方: {square}")
print()

# 2. 生成器表达式与列表推导式的对比
print("=== 2. 生成器表达式与列表推导式的对比 ===")

# 列表推导式
list_comp = [x ** 2 for x in range(10)]
print(f"列表推导式: {list_comp}")
print(f"类型: {type(list_comp)}")
print(f"内存占用: {sys.getsizeof(list_comp)} 字节")
print()

# 生成器表达式
gen_exp = (x ** 2 for x in range(10))
print(f"生成器表达式: {gen_exp}")
print(f"类型: {type(gen_exp)}")
print(f"内存占用: {sys.getsizeof(gen_exp)} 字节")
print()

print("生成器表达式的值（按需生成）:")
for i, value in enumerate(gen_exp):
    print(f"第{i+1}个值: {value}")
    if i >= 4:  # 只显示前5个
        break
print()

# 3. 带条件的生成器表达式
print("=== 3. 带条件的生成器表达式 ===")

# 过滤偶数并求平方
even_squares = (x ** 2 for x in range(20) if x % 2 == 0)
print("偶数的平方:")
for square in even_squares:
    print(f"偶数平方: {square}")
print()

# 字符串处理
words = ['hello', 'world', 'python', 'generator', 'expression']
long_words = (word.upper() for word in words if len(word) > 5)
print("长度大于5的单词（大写）:")
for word in long_words:
    print(f"长单词: {word}")
print()

# 4. 嵌套生成器表达式
print("=== 4. 嵌套生成器表达式 ===")

# 二维数据处理
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = (item for row in matrix for item in row)
print("矩阵扁平化:")
for item in flattened:
    print(f"元素: {item}")
print()

# 嵌套条件
filtered_flattened = (item for row in matrix for item in row if item % 2 == 0)
print("矩阵中的偶数:")
for item in filtered_flattened:
    print(f"偶数: {item}")
print()

# 5. 生成器表达式在函数中的使用
print("=== 5. 生成器表达式在函数中的使用 ===")

# 作为函数参数
numbers = range(1, 11)
print(f"数字总和: {sum(x for x in numbers)}")
print(f"最大值: {max(x ** 2 for x in numbers)}")
print(f"最小值: {min(x for x in numbers if x > 5)}")
print()

# 在函数中返回生成器表达式
def get_fibonacci_gen(n):
    """返回斐波那契数列生成器表达式"""
    def fib_sequence():
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
    
    return (x for x in fib_sequence())

print("斐波那契数列（前8项）:")
fib_gen = get_fibonacci_gen(8)
for fib in fib_gen:
    print(f"斐波那契: {fib}")
print()

# 6. 生成器表达式的链式操作
print("=== 6. 生成器表达式的链式操作 ===")

# 多步骤数据处理
data = range(1, 21)
step1 = (x for x in data if x % 2 == 0)  # 过滤偶数
step2 = (x ** 2 for x in step1)          # 求平方
step3 = (x for x in step2 if x > 50)     # 过滤大于50的数

print("链式处理结果:")
for result in step3:
    print(f"处理结果: {result}")
print()

# 一行完成链式操作
chained = (x ** 2 for x in (y for y in range(1, 21) if y % 2 == 0) if x ** 2 > 50)
print("一行链式操作:")
for result in chained:
    print(f"链式结果: {result}")
print()

# 7. 生成器表达式处理文件数据
print("=== 7. 生成器表达式处理文件数据 ===")

# 模拟文件数据
file_lines = [
    "apple,10,2.5",
    "banana,15,1.8",
    "orange,8,3.2",
    "grape,20,4.5",
    "watermelon,5,8.0"
]

# 解析CSV数据
csv_data = (line.split(',') for line in file_lines)
print("CSV数据解析:")
for row in csv_data:
    print(f"数据行: {row}")
print()

# 处理数值数据
numeric_data = ([row[0], int(row[1]), float(row[2])] for row in (line.split(',') for line in file_lines))
print("数值数据处理:")
for item, quantity, price in numeric_data:
    total = quantity * price
    print(f"{item}: {quantity}个 × {price}元 = {total}元")
print()

# 8. 生成器表达式的内存效率演示
print("=== 8. 生成器表达式的内存效率演示 ===")

# 大数据集处理
n = 1000000

print("内存使用比较:")
# 列表推导式
start_time = time.time()
list_result = [x ** 2 for x in range(n)]
list_time = time.time() - start_time
list_memory = sys.getsizeof(list_result)
print(f"列表推导式 - 时间: {list_time:.4f}秒, 内存: {list_memory:,} 字节")

# 生成器表达式
start_time = time.time()
gen_result = (x ** 2 for x in range(n))
gen_time = time.time() - start_time
gen_memory = sys.getsizeof(gen_result)
print(f"生成器表达式 - 时间: {gen_time:.6f}秒, 内存: {gen_memory:,} 字节")

print(f"内存节省: {(list_memory - gen_memory) / list_memory * 100:.2f}%")
print()

# 9. 生成器表达式的实际应用场景
print("=== 9. 生成器表达式的实际应用场景 ===")

# 日志文件分析
log_entries = [
    "2024-01-01 10:00:00 INFO User login successful",
    "2024-01-01 10:05:00 ERROR Database connection failed",
    "2024-01-01 10:10:00 INFO User logout",
    "2024-01-01 10:15:00 WARNING Low disk space",
    "2024-01-01 10:20:00 ERROR File not found"
]

# 提取错误日志
error_logs = (log for log in log_entries if 'ERROR' in log)
print("错误日志:")
for error in error_logs:
    print(f"错误: {error}")
print()

# 数据统计
scores = [85, 92, 78, 96, 88, 76, 94, 82, 90, 87]
high_scores = (score for score in scores if score >= 90)
print(f"高分数量: {len(list(high_scores))}")

# 重新创建生成器（因为已被消耗）
high_scores = (score for score in scores if score >= 90)
print(f"高分平均值: {sum(high_scores) / len([s for s in scores if s >= 90]):.2f}")
print()

# 10. 生成器表达式的高级用法
print("=== 10. 生成器表达式的高级用法 ===")

# 条件表达式
numbers = range(-5, 6)
abs_values = (x if x >= 0 else -x for x in numbers)
print("绝对值:")
for abs_val in abs_values:
    print(f"绝对值: {abs_val}")
print()

# 多重条件
data = range(1, 101)
special_numbers = (x for x in data if x % 3 == 0 if x % 5 == 0)
print("既能被3又能被5整除的数（前5个）:")
for i, num in enumerate(special_numbers):
    if i >= 5:
        break
    print(f"特殊数: {num}")
print()

# 生成器表达式与zip结合
names = ['Alice', 'Bob', 'Charlie', 'Diana']
ages = [25, 30, 35, 28]
info_gen = (f"{name} is {age} years old" for name, age in zip(names, ages))
print("人员信息:")
for info in info_gen:
    print(info)
print()

# 11. 生成器表达式的注意事项
print("=== 11. 生成器表达式的注意事项 ===")

# 一次性消耗
gen1 = (x for x in range(5))
print("第一次遍历:")
for x in gen1:
    print(f"值: {x}")

print("\n第二次遍历（已耗尽）:")
for x in gen1:
    print(f"值: {x}")
print("生成器已耗尽，无输出")
print()

# 延迟求值
print("延迟求值演示:")
data_list = [1, 2, 3]
gen2 = (x * 2 for x in data_list)
data_list.append(4)  # 修改原始数据
print("修改原始数据后的生成器输出:")
for x in gen2:
    print(f"值: {x}")
print("注意：生成器不会包含后添加的元素")
print()

print("=== 生成器表达式学习完成 ===")
print("关键要点:")
print("1. 生成器表达式使用圆括号语法")
print("2. 比列表推导式更节省内存")
print("3. 支持条件过滤和嵌套")
print("4. 适合处理大数据集")
print("5. 具有延迟求值特性")
print("6. 是一次性的迭代器")
print("7. 可以与其他函数组合使用")

if __name__ == "__main__":
    print("\n=== 运行完成 ===")
    print("本模块演示了生成器表达式的各种用法和应用场景")