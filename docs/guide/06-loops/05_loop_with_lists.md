# 循环遍历列表

列表是Python中最常用的数据结构之一，掌握如何高效地遍历和操作列表是Python编程的基础技能。本节将详细介绍各种列表遍历方法和实际应用。

## 基本遍历方法

### 1. 直接遍历元素

最简单直接的遍历方式：

```python
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(fruit)
```

### 2. 通过索引遍历

当需要索引信息时：

```python
fruits = ["苹果", "香蕉", "橙子"]
for i in range(len(fruits)):
    print(f"索引{i}: {fruits[i]}")
```

### 3. 使用enumerate()同时获取索引和值

最优雅的方式：

```python
fruits = ["苹果", "香蕉", "橙子"]
for index, fruit in enumerate(fruits):
    print(f"索引{index}: {fruit}")
```

## 学习要点

### 1. 列表推导式

创建新列表的简洁方式：

```python
# 传统方式
squares = []
for x in range(1, 6):
    squares.append(x**2)

# 列表推导式
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

### 2. 条件过滤

在遍历时进行条件判断：

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 找出偶数
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# 使用列表推导式
even_numbers = [num for num in numbers if num % 2 == 0]
```

### 3. 嵌套列表遍历

处理二维列表：

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 遍历所有元素
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # 换行
```

## 完整代码示例

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python循环 - 循环遍历列表

本文件详细介绍如何使用循环遍历和操作列表。
列表是Python中最重要的数据结构之一，
掌握列表遍历技巧对Python编程至关重要。

主要内容：
1. 基本遍历方法（直接遍历、索引遍历、enumerate）
2. 列表推导式和条件过滤
3. 嵌套列表的处理
4. 列表修改和更新
5. 查找和统计操作
6. 实际应用案例

作者：Python学习教程
日期：2024年
"""

import random

# 1. 基本遍历方法
print("=== 1. 基本遍历方法 ===")
print()

print("1.1 直接遍历元素")
fruits = ["苹果", "香蕉", "橙子", "葡萄", "草莓"]
print(f"水果列表：{fruits}")
print("直接遍历：")
for fruit in fruits:
    print(f"  我喜欢{fruit}")
print()

print("1.2 通过索引遍历")
print("通过索引访问：")
for i in range(len(fruits)):
    print(f"  索引{i}: {fruits[i]}")
print()

print("1.3 使用enumerate()")
print("使用enumerate同时获取索引和值：")
for index, fruit in enumerate(fruits):
    print(f"  第{index + 1}个水果是{fruit}")
print()

print("1.4 指定enumerate起始值")
print("从1开始编号：")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}. {fruit}")
print()

# 2. 遍历数字列表
print("=== 2. 遍历数字列表 ===")
print()

print("2.1 基本数字操作")
numbers = [1, 4, 7, 2, 9, 5, 8, 3, 6]
print(f"数字列表：{numbers}")

print("计算总和：")
total = 0
for num in numbers:
    total += num
    print(f"  当前数字：{num}，累计和：{total}")
print(f"最终总和：{total}")
print()

print("2.2 查找最大值和最小值")
max_num = numbers[0]
min_num = numbers[0]
max_index = 0
min_index = 0

for i, num in enumerate(numbers):
    if num > max_num:
        max_num = num
        max_index = i
        print(f"  发现更大的数：{num}（索引{i}）")
    if num < min_num:
        min_num = num
        min_index = i
        print(f"  发现更小的数：{num}（索引{i}）")

print(f"最大值：{max_num}（索引{max_index}）")
print(f"最小值：{min_num}（索引{min_index}）")
print()

print("2.3 统计和分类")
positive = []
negative = []
zero = []
mixed_numbers = [3, -2, 0, 7, -5, 0, 1, -1, 4]

print(f"混合数字列表：{mixed_numbers}")
for num in mixed_numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero.append(num)

print(f"正数：{positive}")
print(f"负数：{negative}")
print(f"零：{zero}")
print()

# 3. 条件处理
print("=== 3. 条件处理 ===")
print()

print("3.1 过滤元素")
scores = [85, 92, 78, 96, 88, 73, 90, 82, 95, 77]
print(f"成绩列表：{scores}")

excellent = []  # 优秀（>=90）
good = []       # 良好（80-89）
pass_scores = [] # 及格（70-79）
fail = []       # 不及格（<70）

for score in scores:
    if score >= 90:
        excellent.append(score)
        print(f"  {score} -> 优秀")
    elif score >= 80:
        good.append(score)
        print(f"  {score} -> 良好")
    elif score >= 70:
        pass_scores.append(score)
        print(f"  {score} -> 及格")
    else:
        fail.append(score)
        print(f"  {score} -> 不及格")

print(f"\n成绩统计：")
print(f"优秀：{excellent}（{len(excellent)}人）")
print(f"良好：{good}（{len(good)}人）")
print(f"及格：{pass_scores}（{len(pass_scores)}人）")
print(f"不及格：{fail}（{len(fail)}人）")
print()

print("3.2 查找特定元素")
target_scores = [90, 85, 100]
print(f"查找成绩：{target_scores}")

for target in target_scores:
    found = False
    for i, score in enumerate(scores):
        if score == target:
            print(f"  找到{target}分，位置：{i}")
            found = True
            break
    if not found:
        print(f"  没有找到{target}分")
print()

# 4. 创建新列表
print("=== 4. 创建新列表 ===")
print()

print("4.1 传统方法创建新列表")
original = [1, 2, 3, 4, 5]
print(f"原始列表：{original}")

# 创建平方列表
squares = []
for num in original:
    squares.append(num ** 2)
print(f"平方列表：{squares}")

# 创建偶数列表
even_only = []
for num in original:
    if num % 2 == 0:
        even_only.append(num)
print(f"偶数列表：{even_only}")
print()

print("4.2 列表推导式")
print("使用列表推导式创建新列表：")

# 平方列表
squares_comp = [num ** 2 for num in original]
print(f"平方列表：{squares_comp}")

# 偶数列表
even_comp = [num for num in original if num % 2 == 0]
print(f"偶数列表：{even_comp}")

# 复杂表达式
processed = [num * 2 + 1 for num in original if num > 2]
print(f"处理后列表（>2的数*2+1）：{processed}")
print()

print("4.3 字符串处理")
words = ["python", "java", "javascript", "go", "rust"]
print(f"编程语言：{words}")

# 转换为大写
upper_words = []
for word in words:
    upper_words.append(word.upper())
print(f"大写形式：{upper_words}")

# 筛选长度大于4的单词
long_words = []
for word in words:
    if len(word) > 4:
        long_words.append(word)
print(f"长单词：{long_words}")

# 使用列表推导式
long_upper = [word.upper() for word in words if len(word) > 4]
print(f"长单词大写：{long_upper}")
print()

# 5. 修改列表元素
print("=== 5. 修改列表元素 ===")
print()

print("5.1 直接修改元素")
prices = [10.5, 20.0, 15.8, 30.2, 25.5]
print(f"原始价格：{prices}")

# 所有价格打9折
print("打9折后：")
for i in range(len(prices)):
    prices[i] = prices[i] * 0.9
    print(f"  索引{i}: {prices[i]:.2f}")
print(f"修改后价格：{[round(p, 2) for p in prices]}")
print()

print("5.2 条件修改")
temperatures = [18, 25, 32, 15, 28, 35, 22]
print(f"温度列表（摄氏度）：{temperatures}")

# 将超过30度的温度标记为高温
print("温度分类：")
for i, temp in enumerate(temperatures):
    if temp > 30:
        print(f"  索引{i}: {temp}°C -> 高温")
        temperatures[i] = f"{temp}°C(高温)"
    elif temp < 20:
        print(f"  索引{i}: {temp}°C -> 低温")
        temperatures[i] = f"{temp}°C(低温)"
    else:
        print(f"  索引{i}: {temp}°C -> 适宜")
        temperatures[i] = f"{temp}°C(适宜)"

print(f"标记后：{temperatures}")
print()

# 6. 嵌套列表遍历
print("=== 6. 嵌套列表遍历 ===")
print()

print("6.1 二维列表基本遍历")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("矩阵：")
for i, row in enumerate(matrix):
    print(f"  第{i}行：{row}")
    for j, element in enumerate(row):
        print(f"    [{i}][{j}] = {element}")
print()

print("6.2 学生成绩表")
students_scores = [
    ["张三", 85, 92, 78],
    ["李四", 90, 88, 85],
    ["王五", 78, 85, 90],
    ["赵六", 92, 90, 88]
]

print("学生成绩统计：")
for student_data in students_scores:
    name = student_data[0]
    scores = student_data[1:]
    total = sum(scores)
    average = total / len(scores)
    print(f"  {name}: 各科成绩{scores}, 总分{total}, 平均分{average:.2f}")
print()

print("6.3 查找二维列表中的元素")
target = 5
print(f"在矩阵中查找元素 {target}：")
found = False
for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        if element == target:
            print(f"  找到{target}，位置：[{i}][{j}]")
            found = True
            break
    if found:
        break
if not found:
    print(f"  没有找到{target}")
print()

# 7. 同时遍历多个列表
print("=== 7. 同时遍历多个列表 ===")
print()

print("7.1 使用zip()")
names = ["张三", "李四", "王五"]
ages = [25, 30, 28]
cities = ["北京", "上海", "广州"]

print("个人信息：")
for name, age, city in zip(names, ages, cities):
    print(f"  {name}，{age}岁，来自{city}")
print()

print("7.2 使用索引同时遍历")
print("使用索引方式：")
for i in range(min(len(names), len(ages), len(cities))):
    print(f"  {names[i]}，{ages[i]}岁，来自{cities[i]}")
print()

print("7.3 处理不等长列表")
subjects = ["数学", "语文", "英语", "物理", "化学"]
scores = [85, 92, 78, 88]  # 少一个成绩

print(f"科目：{subjects}")
print(f"成绩：{scores}")
print("成绩对应：")
for i in range(len(subjects)):
    if i < len(scores):
        print(f"  {subjects[i]}: {scores[i]}分")
    else:
        print(f"  {subjects[i]}: 暂无成绩")
print()

# 8. 实际应用案例
print("=== 8. 实际应用案例 ===")
print()

print("8.1 购物车计算")
shopping_cart = [
    ["苹果", 5.5, 3],    # [商品名, 单价, 数量]
    ["香蕉", 3.2, 5],
    ["橙子", 4.8, 2],
    ["牛奶", 12.5, 1]
]

print("购物车清单：")
total_amount = 0
for item in shopping_cart:
    name, price, quantity = item
    subtotal = price * quantity
    total_amount += subtotal
    print(f"  {name}: {price}元 × {quantity} = {subtotal}元")

print(f"总计：{total_amount}元")
print()

print("8.2 数据统计分析")
sales_data = [120, 150, 180, 90, 200, 160, 140, 170, 110, 190]
print(f"销售数据：{sales_data}")

# 基本统计
total_sales = sum(sales_data)
average_sales = total_sales / len(sales_data)
max_sales = max(sales_data)
min_sales = min(sales_data)

print(f"总销售额：{total_sales}")
print(f"平均销售额：{average_sales:.2f}")
print(f"最高销售额：{max_sales}")
print(f"最低销售额：{min_sales}")

# 找出高于平均值的天数
high_performance_days = []
for i, sales in enumerate(sales_data):
    if sales > average_sales:
        high_performance_days.append(i + 1)
        print(f"  第{i + 1}天销售额{sales}高于平均值")

print(f"高于平均值的天数：{high_performance_days}")
print()

print("8.3 文本处理")
sentence = "Python is a powerful programming language"
words = sentence.split()
print(f"句子：{sentence}")
print(f"单词列表：{words}")

# 统计单词长度
word_lengths = []
for word in words:
    length = len(word)
    word_lengths.append(length)
    print(f"  '{word}': {length}个字符")

print(f"单词长度：{word_lengths}")
print(f"平均单词长度：{sum(word_lengths) / len(word_lengths):.2f}")

# 查找最长和最短的单词
longest_word = ""
shortest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
    if len(word) < len(shortest_word):
        shortest_word = word

print(f"最长单词：'{longest_word}'（{len(longest_word)}个字符）")
print(f"最短单词：'{shortest_word}'（{len(shortest_word)}个字符）")
print()

# 9. 综合练习
print("=== 9. 综合练习 ===")
print()

print("9.1 成绩管理系统")
class_scores = {
    "张三": [85, 92, 78, 88, 90],
    "李四": [90, 88, 85, 92, 87],
    "王五": [78, 85, 90, 82, 88],
    "赵六": [92, 90, 88, 85, 89]
}

print("班级成绩分析：")
all_averages = []
for name, scores in class_scores.items():
    total = sum(scores)
    average = total / len(scores)
    all_averages.append(average)
    
    # 找出最高分和最低分
    max_score = max(scores)
    min_score = min(scores)
    
    print(f"  {name}: 总分{total}, 平均分{average:.2f}, 最高分{max_score}, 最低分{min_score}")

class_average = sum(all_averages) / len(all_averages)
print(f"\n班级平均分：{class_average:.2f}")

# 找出班级前三名
student_averages = [(name, sum(scores)/len(scores)) for name, scores in class_scores.items()]
student_averages.sort(key=lambda x: x[1], reverse=True)

print("班级排名前三：")
for i, (name, avg) in enumerate(student_averages[:3]):
    print(f"  第{i+1}名：{name}（平均分{avg:.2f}）")
print()

print("9.2 数据去重和排序")
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3]
print(f"原始数据：{data}")

# 手动去重（保持顺序）
unique_data = []
for item in data:
    if item not in unique_data:
        unique_data.append(item)

print(f"去重后：{unique_data}")

# 统计频率
frequency = {}
for item in data:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("频率统计：")
for num, count in sorted(frequency.items()):
    print(f"  数字{num}: 出现{count}次")
print()

if __name__ == "__main__":
    print("=== 循环遍历列表学习总结 ===")
    print("通过本节学习，你应该掌握了：")
    print("1. 列表的三种基本遍历方法")
    print("2. 使用enumerate()同时获取索引和值")
    print("3. 列表推导式的使用技巧")
    print("4. 条件过滤和元素查找")
    print("5. 嵌套列表的处理方法")
    print("6. 同时遍历多个列表的技巧")
    print("7. 列表在实际项目中的应用")
    print("\n继续练习这些概念，你将能够熟练运用列表解决各种数据处理问题！")
```

## 注意事项

1. **遍历时修改列表**：避免在遍历过程中修改列表大小
2. **索引越界**：使用索引时注意列表边界
3. **性能考虑**：对于大列表，选择合适的遍历方法
4. **内存使用**：列表推导式vs传统循环的内存效率

## 练习建议

1. 练习不同的列表遍历方法
2. 实现各种列表操作（查找、过滤、统计）
3. 使用列表推导式简化代码
4. 处理嵌套列表和复杂数据结构
5. 结合实际场景进行列表操作练习

通过大量练习，你将能够熟练掌握列表遍历的各种技巧，这是Python数据处理的核心技能。