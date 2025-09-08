#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python循环 - 循环遍历列表

本文件演示各种遍历列表的方法和技巧。
列表是Python中最常用的数据结构之一，掌握列表的遍历方法对编程非常重要。

学习目标：
1. 掌握遍历列表的基本方法
2. 学会使用enumerate获取索引和值
3. 了解列表推导式
4. 掌握列表的修改、过滤和变换

作者：Python学习教程
日期：2024年
"""

# 1. 基本的列表遍历
print("=== 1. 基本的列表遍历 ===")
fruits = ["苹果", "香蕉", "橙子", "葡萄", "草莓"]
print(f"水果列表：{fruits}")
print()

print("方法1：直接遍历元素")
for fruit in fruits:
    print(f"  我喜欢吃{fruit}")
print()

print("方法2：使用索引遍历")
for i in range(len(fruits)):
    print(f"  第{i+1}个水果是：{fruits[i]}")
print()

# 2. 使用enumerate获取索引和值
print("=== 2. 使用enumerate获取索引和值 ===")
print("enumerate函数可以同时获取索引和值：")
for index, fruit in enumerate(fruits):
    print(f"  索引{index}：{fruit}")
print()

print("enumerate可以指定起始索引：")
for index, fruit in enumerate(fruits, start=1):
    print(f"  第{index}个：{fruit}")
print()

# 3. 遍历数字列表
print("=== 3. 遍历数字列表 ===")
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"数字列表：{numbers}")
print()

print("计算所有数字的和：")
total = 0
for num in numbers:
    total += num
    print(f"  当前数字：{num}，累计和：{total}")
print(f"最终和：{total}")
print()

print("找出最大值和最小值：")
max_num = numbers[0]
min_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print(f"最大值：{max_num}")
print(f"最小值：{min_num}")
print()

# 4. 列表元素的条件处理
print("=== 4. 列表元素的条件处理 ===")
scores = [85, 92, 78, 96, 88, 73, 91, 87]
print(f"成绩列表：{scores}")
print()

print("统计各等级成绩：")
excellent = 0  # 90分以上
good = 0       # 80-89分
pass_grade = 0 # 60-79分
fail = 0       # 60分以下

for score in scores:
    if score >= 90:
        excellent += 1
        print(f"  {score}分 - 优秀")
    elif score >= 80:
        good += 1
        print(f"  {score}分 - 良好")
    elif score >= 60:
        pass_grade += 1
        print(f"  {score}分 - 及格")
    else:
        fail += 1
        print(f"  {score}分 - 不及格")

print(f"\n统计结果：")
print(f"  优秀：{excellent}人")
print(f"  良好：{good}人")
print(f"  及格：{pass_grade}人")
print(f"  不及格：{fail}人")
print()

# 5. 创建新列表
print("=== 5. 创建新列表 ===")
original_numbers = [1, 2, 3, 4, 5]
print(f"原始列表：{original_numbers}")
print()

print("方法1：使用循环创建平方数列表")
squares = []
for num in original_numbers:
    squares.append(num ** 2)
print(f"平方数列表：{squares}")
print()

print("方法2：使用列表推导式（更简洁）")
squares_2 = [num ** 2 for num in original_numbers]
print(f"平方数列表：{squares_2}")
print()

# 6. 列表推导式详解
print("=== 6. 列表推导式详解 ===")
print("列表推导式语法：[表达式 for 变量 in 可迭代对象 if 条件]")
print()

numbers = list(range(1, 11))
print(f"原始数字：{numbers}")
print()

print("示例1：生成偶数列表")
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"偶数：{even_numbers}")
print()

print("示例2：生成平方数（只包含奇数的平方）")
odd_squares = [num ** 2 for num in numbers if num % 2 == 1]
print(f"奇数的平方：{odd_squares}")
print()

print("示例3：字符串处理")
words = ["python", "java", "javascript", "go", "rust"]
print(f"编程语言：{words}")
long_words = [word.upper() for word in words if len(word) > 4]
print(f"长度大于4的语言（大写）：{long_words}")
print()

# 7. 修改列表元素
print("=== 7. 修改列表元素 ===")
prices = [10.5, 20.0, 15.8, 30.2, 25.6]
print(f"原始价格：{prices}")
print()

print("方法1：使用索引修改")
for i in range(len(prices)):
    prices[i] = prices[i] * 0.9  # 打9折
print(f"打折后价格：{prices}")
print()

# 重置价格用于下一个示例
prices = [10.5, 20.0, 15.8, 30.2, 25.6]
print("方法2：使用enumerate修改")
for i, price in enumerate(prices):
    if price > 20:
        prices[i] = price * 0.8  # 超过20的打8折
    else:
        prices[i] = price * 0.9  # 其他打9折
print(f"差异化折扣后：{prices}")
print()

# 8. 嵌套列表的遍历
print("=== 8. 嵌套列表的遍历 ===")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("3x3矩阵：")
for row in matrix:
    print(f"  {row}")
print()

print("遍历矩阵的每个元素：")
for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        print(f"  matrix[{i}][{j}] = {element}")
print()

print("计算矩阵所有元素的和：")
total_sum = 0
for row in matrix:
    for element in row:
        total_sum += element
print(f"矩阵元素总和：{total_sum}")
print()

# 9. 列表的查找和统计
print("=== 9. 列表的查找和统计 ===")
data = [3, 7, 2, 8, 3, 9, 1, 3, 6, 4]
print(f"数据列表：{data}")
print()

print("查找特定元素的所有位置：")
target = 3
positions = []
for i, value in enumerate(data):
    if value == target:
        positions.append(i)
print(f"数字{target}出现的位置：{positions}")
print()

print("统计每个数字出现的次数：")
counts = {}
for num in data:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

for num, count in sorted(counts.items()):
    print(f"  数字{num}出现{count}次")
print()

# 10. 列表的过滤和分组
print("=== 10. 列表的过滤和分组 ===")
students = [
    {"name": "张三", "age": 20, "score": 85},
    {"name": "李四", "age": 19, "score": 92},
    {"name": "王五", "age": 21, "score": 78},
    {"name": "赵六", "age": 20, "score": 96},
    {"name": "钱七", "age": 19, "score": 88}
]
print("学生信息：")
for student in students:
    print(f"  {student['name']}，{student['age']}岁，成绩：{student['score']}")
print()

print("筛选优秀学生（成绩>=90）：")
excellent_students = []
for student in students:
    if student['score'] >= 90:
        excellent_students.append(student)
        print(f"  {student['name']}：{student['score']}分")
print()

print("按年龄分组：")
age_groups = {}
for student in students:
    age = student['age']
    if age not in age_groups:
        age_groups[age] = []
    age_groups[age].append(student['name'])

for age, names in sorted(age_groups.items()):
    print(f"  {age}岁：{', '.join(names)}")
print()

# 11. 列表的排序遍历
print("=== 11. 列表的排序遍历 ===")
words = ["banana", "apple", "cherry", "date", "elderberry"]
print(f"原始单词列表：{words}")
print()

print("按字母顺序遍历（不改变原列表）：")
for word in sorted(words):
    print(f"  {word}")
print(f"原列表未改变：{words}")
print()

print("按长度排序遍历：")
for word in sorted(words, key=len):
    print(f"  {word} (长度：{len(word)})")
print()

print("按长度倒序遍历：")
for word in sorted(words, key=len, reverse=True):
    print(f"  {word} (长度：{len(word)})")
print()

# 12. 同时遍历多个列表
print("=== 12. 同时遍历多个列表 ===")
names = ["张三", "李四", "王五", "赵六"]
ages = [25, 30, 28, 32]
scores = [85, 92, 78, 96]

print("使用zip同时遍历多个列表：")
for name, age, score in zip(names, ages, scores):
    print(f"  {name}，{age}岁，成绩：{score}分")
print()

print("使用enumerate和zip：")
for i, (name, age, score) in enumerate(zip(names, ages, scores), 1):
    print(f"  第{i}名学生：{name}，{age}岁，成绩：{score}分")
print()

# 13. 列表的实际应用
print("=== 13. 列表的实际应用 ===")

# 应用1：购物车计算
print("应用1：购物车总价计算")
shopping_cart = [
    {"name": "苹果", "price": 5.5, "quantity": 3},
    {"name": "香蕉", "price": 3.2, "quantity": 5},
    {"name": "橙子", "price": 4.8, "quantity": 2}
]

total_cost = 0
print("购物清单：")
for item in shopping_cart:
    subtotal = item['price'] * item['quantity']
    total_cost += subtotal
    print(f"  {item['name']}：{item['price']}元 x {item['quantity']} = {subtotal}元")
print(f"总计：{total_cost}元")
print()

# 应用2：数据分析
print("应用2：销售数据分析")
monthly_sales = [12000, 15000, 13500, 18000, 16500, 14000, 17500, 19000, 16000, 15500, 18500, 20000]
months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]

print("月度销售额：")
for month, sales in zip(months, monthly_sales):
    print(f"  {month}：{sales}元")

# 计算统计信息
total_sales = sum(monthly_sales)
average_sales = total_sales / len(monthly_sales)
max_sales = max(monthly_sales)
min_sales = min(monthly_sales)

print(f"\n年度统计：")
print(f"  总销售额：{total_sales}元")
print(f"  平均月销售额：{average_sales:.2f}元")
print(f"  最高月销售额：{max_sales}元")
print(f"  最低月销售额：{min_sales}元")

# 找出最好和最差的月份
best_month = months[monthly_sales.index(max_sales)]
worst_month = months[monthly_sales.index(min_sales)]
print(f"  最佳月份：{best_month}")
print(f"  最差月份：{worst_month}")
print()

# 14. 练习题
print("=== 14. 练习题 ===")

print("练习1：找出列表中的重复元素")
numbers = [1, 2, 3, 2, 4, 5, 3, 6, 1, 7]
print(f"原列表：{numbers}")
seen = set()
duplicates = set()
for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
print(f"重复元素：{sorted(list(duplicates))}")
print()

print("练习2：列表元素去重（保持顺序）")
original = [1, 2, 3, 2, 4, 5, 3, 6, 1, 7]
print(f"原列表：{original}")
unique_list = []
for item in original:
    if item not in unique_list:
        unique_list.append(item)
print(f"去重后：{unique_list}")
print()

print("练习3：计算移动平均值")
data = [10, 12, 13, 12, 15, 16, 14, 13, 15, 17, 16, 18]
window_size = 3
print(f"原数据：{data}")
print(f"窗口大小：{window_size}")
moving_averages = []
for i in range(len(data) - window_size + 1):
    window = data[i:i + window_size]
    avg = sum(window) / len(window)
    moving_averages.append(round(avg, 2))
    print(f"  位置{i}-{i+window_size-1}：{window} -> 平均值：{avg:.2f}")
print(f"移动平均值：{moving_averages}")

if __name__ == "__main__":
    print("\n=== 列表遍历学习总结 ===")
    print("1. 直接遍历：for item in list")
    print("2. 索引遍历：for i in range(len(list))")
    print("3. enumerate：同时获取索引和值")
    print("4. 列表推导式：简洁的创建新列表")
    print("5. zip：同时遍历多个列表")
    print("6. 嵌套循环：处理二维列表")
    print("7. 条件过滤：筛选符合条件的元素")
    print("8. 统计分析：计算和、平均值、最值等")
    print("9. 排序遍历：按特定顺序处理元素")
    print("10. 实际应用：购物车、数据分析等场景")