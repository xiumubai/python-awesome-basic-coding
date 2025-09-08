#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python循环 - for循环基础

本文件演示for循环的基本用法和常见应用场景。
for循环是Python中最常用的循环结构，用于遍历序列（如列表、元组、字符串）或其他可迭代对象。

学习目标：
1. 理解for循环的基本语法
2. 掌握for循环遍历不同数据类型
3. 学会使用for循环处理实际问题
4. 了解for循环的执行流程

作者：Python学习教程
日期：2024年
"""

# 1. for循环的基本语法
print("=== 1. for循环基本语法 ===")
print("for循环语法：for 变量 in 可迭代对象:")
print("    循环体")
print()

# 2. 遍历列表
print("=== 2. 遍历列表 ===")
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print(f"水果列表：{fruits}")
print("遍历水果列表：")
for fruit in fruits:
    print(f"  我喜欢吃{fruit}")
print()

# 3. 遍历字符串
print("=== 3. 遍历字符串 ===")
word = "Python"
print(f"字符串：{word}")
print("逐个字符遍历：")
for char in word:
    print(f"  字符：{char}")
print()

# 4. 遍历元组
print("=== 4. 遍历元组 ===")
colors = ("红色", "绿色", "蓝色")
print(f"颜色元组：{colors}")
print("遍历颜色：")
for color in colors:
    print(f"  {color}很漂亮")
print()

# 5. 使用enumerate()获取索引和值
print("=== 5. 使用enumerate()获取索引 ===")
subjects = ["数学", "语文", "英语", "物理"]
print(f"科目列表：{subjects}")
print("带索引的遍历：")
for index, subject in enumerate(subjects):
    print(f"  第{index + 1}门课程：{subject}")
print()

# 6. 遍历字典
print("=== 6. 遍历字典 ===")
student_scores = {
    "张三": 85,
    "李四": 92,
    "王五": 78,
    "赵六": 96
}
print(f"学生成绩：{student_scores}")

# 遍历键
print("遍历学生姓名（键）：")
for name in student_scores.keys():
    print(f"  学生：{name}")

# 遍历值
print("遍历成绩（值）：")
for score in student_scores.values():
    print(f"  成绩：{score}分")

# 遍历键值对
print("遍历姓名和成绩：")
for name, score in student_scores.items():
    print(f"  {name}的成绩是{score}分")
print()

# 7. for循环的实际应用
print("=== 7. 实际应用示例 ===")

# 计算列表中所有数字的总和
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"数字列表：{numbers}")
total = 0
for num in numbers:
    total += num
print(f"所有数字的总和：{total}")

# 找出列表中的偶数
print("\n找出偶数：")
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"偶数列表：{even_numbers}")

# 统计字符串中各字符出现次数
text = "hello world"
print(f"\n统计字符串 '{text}' 中各字符出现次数：")
char_count = {}
for char in text:
    if char != ' ':  # 忽略空格
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

for char, count in char_count.items():
    print(f"  字符 '{char}' 出现了 {count} 次")
print()

# 8. 嵌套for循环简单示例
print("=== 8. 嵌套for循环 ===")
print("打印乘法表（部分）：")
for i in range(1, 4):  # 外层循环
    for j in range(1, 4):  # 内层循环
        result = i * j
        print(f"{i} × {j} = {result}", end="  ")
    print()  # 换行
print()

# 9. for循环与else语句
print("=== 9. for循环与else语句 ===")
print("for循环可以配合else使用，当循环正常结束时执行else")

# 查找列表中是否有特定元素
search_list = [1, 2, 3, 4, 5]
target = 3
print(f"在列表 {search_list} 中查找 {target}：")

for item in search_list:
    if item == target:
        print(f"  找到了 {target}！")
        break
else:
    print(f"  没有找到 {target}")

# 查找不存在的元素
target = 10
print(f"\n在列表 {search_list} 中查找 {target}：")
for item in search_list:
    if item == target:
        print(f"  找到了 {target}！")
        break
else:
    print(f"  没有找到 {target}")
print()

# 10. 练习题
print("=== 10. 练习题 ===")
print("练习1：计算1到100的和")
sum_result = 0
for i in range(1, 101):
    sum_result += i
print(f"1到100的和是：{sum_result}")

print("\n练习2：找出1到20中的质数")
primes = []
for num in range(2, 21):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print(f"1到20中的质数：{primes}")

print("\n练习3：反转字符串")
original = "Python"
reversed_str = ""
for char in original:
    reversed_str = char + reversed_str
print(f"原字符串：{original}")
print(f"反转后：{reversed_str}")

if __name__ == "__main__":
    print("\n=== for循环学习总结 ===")
    print("1. for循环用于遍历可迭代对象")
    print("2. 可以遍历列表、元组、字符串、字典等")
    print("3. enumerate()可以同时获取索引和值")
    print("4. 字典遍历可以使用keys()、values()、items()")
    print("5. for循环可以嵌套使用")
    print("6. for循环可以配合else使用")
    print("7. for循环是处理序列数据的重要工具")