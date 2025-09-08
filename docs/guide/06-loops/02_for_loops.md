# for循环基础

for循环是Python中最常用的循环结构之一，它可以遍历任何可迭代对象（如列表、字符串、元组、字典等）。for循环的语法简洁明了，是处理序列数据的首选方法。

## 基本语法

for循环的基本语法结构：

```python
for 变量 in 可迭代对象:
    # 循环体代码
    pass
```

## 学习要点

### 1. 基础for循环

最简单的for循环遍历：

```python
# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"我喜欢吃{fruit}")

# 遍历字符串
for char in "Python":
    print(char)

# 遍历元组
colors = ("红色", "绿色", "蓝色")
for color in colors:
    print(color)
```

### 2. 使用enumerate()获取索引

当需要同时获取元素和索引时：

```python
fruits = ["苹果", "香蕉", "橙子"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"第{index}个水果是{fruit}")
```

### 3. 遍历字典

字典有三种遍历方式：

```python
student_scores = {"张三": 85, "李四": 92, "王五": 78}

# 遍历键
for name in student_scores:
    print(f"学生：{name}")

# 遍历值
for score in student_scores.values():
    print(f"分数：{score}")

# 遍历键值对
for name, score in student_scores.items():
    print(f"{name}的分数是{score}")
```

### 4. 嵌套for循环

处理二维数据结构：

```python
# 打印乘法表
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}")
    print()  # 换行

# 遍历二维列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # 换行
```

### 5. for-else语句

for循环可以配合else使用：

```python
# 查找元素
numbers = [1, 3, 5, 7, 9]
target = 6

for num in numbers:
    if num == target:
        print(f"找到了{target}")
        break
else:
    print(f"没有找到{target}")
```

## 完整代码示例

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python循环 - for循环基础

本文件详细介绍for循环的各种用法和应用场景。
for循环是Python中最常用的循环结构，用于遍历可迭代对象。

主要内容：
1. for循环基本语法
2. 遍历不同类型的数据结构
3. enumerate()函数的使用
4. 字典遍历的三种方式
5. 嵌套for循环
6. for-else语句
7. 实际应用示例

作者：Python学习教程
日期：2024年
"""

# 1. for循环基本语法
print("=== 1. for循环基本语法 ===")
print()

print("1.1 遍历列表")
fruits = ["苹果", "香蕉", "橙子", "葡萄", "草莓"]
print(f"水果列表：{fruits}")
print("遍历结果：")
for fruit in fruits:
    print(f"  我喜欢吃{fruit}")
print()

print("1.2 遍历字符串")
text = "Python"
print(f"字符串：{text}")
print("字符遍历：")
for char in text:
    print(f"  字符：{char}")
print()

print("1.3 遍历元组")
colors = ("红色", "绿色", "蓝色", "黄色")
print(f"颜色元组：{colors}")
print("遍历结果：")
for color in colors:
    print(f"  颜色：{color}")
print()

# 2. 使用enumerate()获取索引和值
print("=== 2. 使用enumerate()获取索引和值 ===")
print()

print("2.1 基本用法")
fruits = ["苹果", "香蕉", "橙子"]
print(f"水果列表：{fruits}")
print("带索引的遍历：")
for index, fruit in enumerate(fruits):
    print(f"  索引{index}: {fruit}")
print()

print("2.2 指定起始索引")
print("从1开始编号：")
for index, fruit in enumerate(fruits, start=1):
    print(f"  第{index}个水果：{fruit}")
print()

print("2.3 实际应用：创建编号列表")
shopping_list = ["牛奶", "面包", "鸡蛋", "苹果"]
print("购物清单：")
for i, item in enumerate(shopping_list, 1):
    print(f"  {i}. {item}")
print()

# 3. 遍历字典
print("=== 3. 遍历字典 ===")
print()

student_scores = {
    "张三": 85,
    "李四": 92,
    "王五": 78,
    "赵六": 88,
    "钱七": 95
}

print(f"学生成绩字典：{student_scores}")
print()

print("3.1 遍历键（默认方式）")
for name in student_scores:
    print(f"  学生：{name}")
print()

print("3.2 遍历值")
for score in student_scores.values():
    print(f"  分数：{score}")
print()

print("3.3 遍历键值对")
for name, score in student_scores.items():
    print(f"  {name}的分数是{score}分")
print()

print("3.4 实际应用：成绩统计")
total_score = 0
student_count = 0
for name, score in student_scores.items():
    total_score += score
    student_count += 1
    if score >= 90:
        print(f"  优秀学生：{name}（{score}分）")

average_score = total_score / student_count
print(f"\n班级平均分：{average_score:.2f}")
print()

# 4. 实际应用示例
print("=== 4. 实际应用示例 ===")
print()

print("4.1 统计字符频率")
text = "hello world"
print(f"文本：{text}")
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("字符频率统计：")
for char, count in char_count.items():
    if char == ' ':
        print(f"  空格: {count}次")
    else:
        print(f"  '{char}': {count}次")
print()

print("4.2 查找最大值和最小值")
numbers = [23, 45, 12, 67, 34, 89, 15]
print(f"数字列表：{numbers}")

max_num = numbers[0]
min_num = numbers[0]
max_index = 0
min_index = 0

for i, num in enumerate(numbers):
    if num > max_num:
        max_num = num
        max_index = i
    if num < min_num:
        min_num = num
        min_index = i

print(f"最大值：{max_num}（索引：{max_index}）")
print(f"最小值：{min_num}（索引：{min_index}）")
print()

print("4.3 列表过滤")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"原始列表：{numbers}")

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(f"偶数：{even_numbers}")
print(f"奇数：{odd_numbers}")
print()

# 5. 嵌套for循环
print("=== 5. 嵌套for循环 ===")
print()

print("5.1 打印乘法表")
print("3x3乘法表：")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i}×{j}={result:2d}", end="  ")
    print()  # 换行
print()

print("5.2 遍历二维列表")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("矩阵：")
for row in matrix:
    for element in row:
        print(f"{element:2d}", end=" ")
    print()  # 换行
print()

print("5.3 生成坐标点")
print("3x3网格的坐标点：")
for x in range(3):
    for y in range(3):
        print(f"({x},{y})", end=" ")
    print()  # 换行
print()

# 6. for-else语句
print("=== 6. for-else语句 ===")
print()

print("6.1 查找元素（找到的情况）")
numbers = [1, 3, 5, 7, 9]
target = 5
print(f"在列表 {numbers} 中查找 {target}")

for num in numbers:
    if num == target:
        print(f"找到了{target}！")
        break
else:
    print(f"没有找到{target}")
print()

print("6.2 查找元素（未找到的情况）")
target = 6
print(f"在列表 {numbers} 中查找 {target}")

for num in numbers:
    if num == target:
        print(f"找到了{target}！")
        break
else:
    print(f"没有找到{target}")
print()

print("6.3 验证所有元素")
numbers = [2, 4, 6, 8, 10]
print(f"检查列表 {numbers} 中是否都是偶数")

for num in numbers:
    if num % 2 != 0:
        print(f"发现奇数：{num}")
        break
else:
    print("所有数字都是偶数！")
print()

# 7. 综合练习
print("=== 7. 综合练习 ===")
print()

print("7.1 单词统计")
text = "python is great python is fun python is powerful"
print(f"文本：{text}")

words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("单词统计：")
for word, count in word_count.items():
    print(f"  '{word}': {count}次")
print()

print("7.2 成绩等级划分")
scores = [85, 92, 78, 96, 88, 73, 90, 82]
print(f"成绩列表：{scores}")

grade_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

for score in scores:
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'D'
    
    grade_count[grade] += 1
    print(f"  分数 {score} -> 等级 {grade}")

print("\n等级统计：")
for grade, count in grade_count.items():
    print(f"  等级{grade}: {count}人")
print()

print("7.3 数字模式")
print("生成数字三角形：")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # 换行
print()

if __name__ == "__main__":
    print("=== for循环学习总结 ===")
    print("通过本节学习，你应该掌握了：")
    print("1. for循环的基本语法和使用方法")
    print("2. 遍历不同类型的数据结构（列表、字符串、元组、字典）")
    print("3. enumerate()函数获取索引和值")
    print("4. 字典的三种遍历方式")
    print("5. 嵌套for循环处理二维数据")
    print("6. for-else语句的特殊用法")
    print("7. for循环在实际编程中的应用")
    print("\n继续练习这些概念，你将能够熟练运用for循环解决各种问题！")
```

## 注意事项

1. **循环变量作用域**：循环变量在循环结束后仍然存在
2. **修改列表**：在遍历列表时修改列表可能导致意外结果
3. **性能考虑**：对于大数据集，考虑使用生成器或其他优化方法
4. **可读性**：使用有意义的变量名提高代码可读性

## 练习建议

1. 尝试遍历不同类型的数据结构
2. 练习使用enumerate()处理需要索引的场景
3. 实现简单的数据统计和分析功能
4. 编写嵌套循环处理二维数据
5. 使用for-else语句实现查找功能

通过大量练习，你将能够熟练掌握for循环的各种用法，为后续学习更复杂的编程概念打下坚实基础。