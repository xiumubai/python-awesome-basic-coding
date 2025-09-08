#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python循环 - range函数详解

本文件详细介绍range函数的用法和在循环中的应用。
range函数是Python中生成数字序列的重要工具，常与for循环配合使用。

学习目标：
1. 理解range函数的基本语法
2. 掌握range的三种参数形式
3. 学会在循环中使用range
4. 了解range的高级用法和技巧

作者：Python学习教程
日期：2024年
"""

# 1. range函数基础
print("=== 1. range函数基础 ===")
print("range函数用于生成数字序列，常用于for循环")
print("range函数有三种形式：")
print("1. range(stop) - 从0开始到stop-1")
print("2. range(start, stop) - 从start开始到stop-1")
print("3. range(start, stop, step) - 从start开始到stop-1，步长为step")
print()

# 2. range(stop) - 单参数形式
print("=== 2. range(stop) - 单参数形式 ===")
print("range(5) 生成 0, 1, 2, 3, 4")
print("使用list()可以查看range的内容：")
print(f"list(range(5)) = {list(range(5))}")
print()

print("在for循环中使用：")
for i in range(5):
    print(f"  i = {i}")
print()

# 3. range(start, stop) - 双参数形式
print("=== 3. range(start, stop) - 双参数形式 ===")
print("range(2, 8) 生成 2, 3, 4, 5, 6, 7")
print(f"list(range(2, 8)) = {list(range(2, 8))}")
print()

print("在for循环中使用：")
for i in range(2, 8):
    print(f"  i = {i}")
print()

# 4. range(start, stop, step) - 三参数形式
print("=== 4. range(start, stop, step) - 三参数形式 ===")
print("range(0, 10, 2) 生成 0, 2, 4, 6, 8 (步长为2)")
print(f"list(range(0, 10, 2)) = {list(range(0, 10, 2))}")
print()

print("在for循环中使用：")
for i in range(0, 10, 2):
    print(f"  i = {i}")
print()

# 5. 负数步长 - 倒序
print("=== 5. 负数步长 - 倒序 ===")
print("range(10, 0, -1) 生成 10, 9, 8, 7, 6, 5, 4, 3, 2, 1")
print(f"list(range(10, 0, -1)) = {list(range(10, 0, -1))}")
print()

print("倒序循环：")
for i in range(5, 0, -1):
    print(f"  倒计时：{i}")
print("  发射！")
print()

# 6. 负数步长的更多示例
print("=== 6. 负数步长的更多示例 ===")
print("range(20, 0, -3) 生成 20, 17, 14, 11, 8, 5, 2")
print(f"list(range(20, 0, -3)) = {list(range(20, 0, -3))}")
print()

print("range(-5, -15, -2) 生成 -5, -7, -9, -11, -13")
print(f"list(range(-5, -15, -2)) = {list(range(-5, -15, -2))}")
print()

# 7. range与列表索引
print("=== 7. range与列表索引 ===")
fruits = ["苹果", "香蕉", "橙子", "葡萄", "草莓"]
print(f"水果列表：{fruits}")
print("使用range遍历索引：")

for i in range(len(fruits)):
    print(f"  索引 {i}: {fruits[i]}")
print()

# 8. range的实际应用
print("=== 8. range的实际应用 ===")

# 应用1：生成乘法表
print("应用1：生成5x5乘法表")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}x{j}={i*j:2d}", end="  ")
    print()  # 换行
print()

# 应用2：计算平方数
print("应用2：计算1到10的平方数")
squares = []
for i in range(1, 11):
    square = i ** 2
    squares.append(square)
    print(f"  {i}² = {square}")
print(f"平方数列表：{squares}")
print()

# 应用3：生成偶数和奇数
print("应用3：生成1到20的偶数和奇数")
even_numbers = []
odd_numbers = []

for i in range(1, 21):
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print(f"偶数：{even_numbers}")
print(f"奇数：{odd_numbers}")
print()

# 更简洁的方法
print("更简洁的方法：")
even_numbers_2 = list(range(2, 21, 2))
odd_numbers_2 = list(range(1, 21, 2))
print(f"偶数：{even_numbers_2}")
print(f"奇数：{odd_numbers_2}")
print()

# 9. range与字符串操作
print("=== 9. range与字符串操作 ===")
text = "Python编程"
print(f"字符串：{text}")
print("正向遍历每个字符：")
for i in range(len(text)):
    print(f"  索引 {i}: '{text[i]}'")
print()

print("反向遍历每个字符：")
for i in range(len(text) - 1, -1, -1):
    print(f"  索引 {i}: '{text[i]}'")
print()

# 10. range的高级技巧
print("=== 10. range的高级技巧 ===")

# 技巧1：跳过某些元素
print("技巧1：只处理列表中的偶数索引元素")
data = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(f"原列表：{data}")
print("偶数索引的元素：")
for i in range(0, len(data), 2):
    print(f"  索引 {i}: {data[i]}")
print()

# 技巧2：分组处理
print("技巧2：每3个元素为一组处理")
numbers = list(range(1, 16))  # 1到15
print(f"数字列表：{numbers}")
print("分组处理（每组3个）：")
for i in range(0, len(numbers), 3):
    group = numbers[i:i+3]
    print(f"  第{i//3 + 1}组：{group}")
print()

# 11. range与数学计算
print("=== 11. range与数学计算 ===")

# 计算等差数列的和
print("计算等差数列的和：")
print("数列：2, 5, 8, 11, 14, 17, 20 (首项=2, 公差=3)")
first_term = 2
common_diff = 3
n_terms = 7

total_sum = 0
print("各项：")
for i in range(n_terms):
    term = first_term + i * common_diff
    total_sum += term
    print(f"  第{i+1}项：{term}")
print(f"数列和：{total_sum}")
print()

# 使用range直接生成等差数列
print("使用range直接生成等差数列：")
arithmetic_sequence = list(range(first_term, first_term + n_terms * common_diff, common_diff))
print(f"等差数列：{arithmetic_sequence}")
print(f"数列和：{sum(arithmetic_sequence)}")
print()

# 12. range的性能特点
print("=== 12. range的性能特点 ===")
print("range是一个惰性对象，不会立即生成所有数字")
print("这意味着range(1000000)不会占用大量内存")
print()

# 演示range的内存效率
print("演示range的内存效率：")
large_range = range(1000000)
print(f"range(1000000)对象：{large_range}")
print("range对象本身很小，只在需要时生成数字")
print()

# 如果需要列表，可以转换
print("如果需要实际的列表：")
small_list = list(range(10))
print(f"list(range(10)) = {small_list}")
print("注意：对于大范围，转换为列表会占用大量内存")
print()

# 13. range与其他函数的结合
print("=== 13. range与其他函数的结合 ===")

# 与enumerate结合
print("与enumerate结合使用：")
colors = ["红色", "绿色", "蓝色", "黄色"]
print("方法1：使用range和len")
for i in range(len(colors)):
    print(f"  {i}: {colors[i]}")

print("方法2：使用enumerate（推荐）")
for i, color in enumerate(colors):
    print(f"  {i}: {color}")
print()

# 与zip结合
print("与zip结合使用：")
names = ["张三", "李四", "王五"]
ages = [25, 30, 28]
print("使用range遍历多个列表：")
for i in range(len(names)):
    print(f"  {names[i]}，年龄：{ages[i]}")

print("使用zip（推荐）：")
for name, age in zip(names, ages):
    print(f"  {name}，年龄：{age}")
print()

# 14. 练习题
print("=== 14. 练习题 ===")

print("练习1：打印99乘法表")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}x{i}={i*j:2d}", end=" ")
    print()
print()

print("练习2：生成斐波那契数列前15项")
fib_sequence = [0, 1]
for i in range(2, 15):
    next_fib = fib_sequence[i-1] + fib_sequence[i-2]
    fib_sequence.append(next_fib)
print(f"斐波那契数列前15项：{fib_sequence}")
print()

print("练习3：找出100以内的所有质数")
primes = []
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print(f"100以内的质数有{len(primes)}个：")
print(primes[:20], "...")  # 只显示前20个
print()

print("练习4：创建一个简单的进度条")
import time
print("模拟下载进度：")
for i in range(0, 101, 10):
    bar = "█" * (i // 10) + "░" * (10 - i // 10)
    print(f"\r[{bar}] {i}%", end="")
    time.sleep(0.1)  # 模拟延迟
print("\n下载完成！")

if __name__ == "__main__":
    print("\n=== range函数学习总结 ===")
    print("1. range(stop): 从0到stop-1")
    print("2. range(start, stop): 从start到stop-1")
    print("3. range(start, stop, step): 指定步长")
    print("4. 步长可以为负数，实现倒序")
    print("5. range是惰性对象，内存效率高")
    print("6. 常与for循环配合使用")
    print("7. 适用于需要索引的场景")
    print("8. 可以生成等差数列")
    print("9. 在某些情况下，enumerate和zip更简洁")