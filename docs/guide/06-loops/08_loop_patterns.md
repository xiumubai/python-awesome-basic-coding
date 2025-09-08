# 常见循环模式

在Python编程中，有许多常见的循环模式和技巧。掌握这些模式可以让你的代码更加高效、优雅和易读。本节将介绍各种实用的循环模式和最佳实践。

## 循环控制语句

### 1. break语句

用于提前退出循环：

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### 2. continue语句

跳过当前迭代，继续下一次循环：

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 只打印奇数
```

### 3. else子句

循环正常结束时执行：

```python
for i in range(5):
    print(i)
else:
    print("循环正常结束")
```

## 学习要点

### 1. 累加器模式

用于累计计算：

```python
total = 0
for i in range(1, 101):
    total += i
print(f"1到100的和：{total}")
```

### 2. 计数器模式

统计满足条件的元素：

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print(f"偶数个数：{even_count}")
```

### 3. 查找模式

在数据中查找特定元素：

```python
numbers = [3, 7, 2, 9, 1, 5]
target = 9
found = False
for num in numbers:
    if num == target:
        found = True
        break
print(f"找到目标：{found}")
```

## 完整代码示例

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python循环 - 常见循环模式

本文件详细介绍Python中常见的循环模式和编程技巧。
掌握这些模式可以让你的代码更加高效、优雅和易读，
是成为优秀Python程序员的重要技能。

主要内容：
1. 循环控制语句（break、continue、else）
2. 累加器和计数器模式
3. 查找和过滤模式
4. 变换和映射模式
5. 分组和聚合模式
6. 嵌套数据处理模式
7. 生成器和迭代器模式
8. 循环优化技巧
9. 实际应用案例

作者：Python学习教程
日期：2024年
"""

import random
import time
from collections import defaultdict

# 1. 循环控制语句
print("=== 1. 循环控制语句 ===")
print()

print("1.1 break语句 - 提前退出循环")
print("查找第一个偶数：")
numbers = [1, 3, 5, 8, 9, 12, 15]
for i, num in enumerate(numbers):
    print(f"检查 {num}")
    if num % 2 == 0:
        print(f"找到第一个偶数：{num}，位置：{i}")
        break
else:
    print("没有找到偶数")
print()

print("1.2 continue语句 - 跳过当前迭代")
print("只处理正数：")
numbers = [-2, 3, -1, 5, 0, 7, -3]
for num in numbers:
    if num <= 0:
        print(f"跳过 {num}")
        continue
    print(f"处理正数：{num}，平方：{num**2}")
print()

print("1.3 for-else语句")
print("检查列表是否包含负数：")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num < 0:
        print(f"发现负数：{num}")
        break
else:
    print("列表中没有负数")
print()

print("1.4 while-else语句")
print("猜数字游戏（最多3次机会）：")
secret = 7
guesses = 0
max_guesses = 3

while guesses < max_guesses:
    # 模拟用户输入
    guess = random.randint(1, 10)
    guesses += 1
    print(f"第{guesses}次猜测：{guess}")
    
    if guess == secret:
        print(f"恭喜！猜对了，答案是 {secret}")
        break
    elif guess < secret:
        print("太小了")
    else:
        print("太大了")
else:
    print(f"游戏结束！答案是 {secret}")
print()

# 2. 累加器模式
print("=== 2. 累加器模式 ===")
print()

print("2.1 数值累加")
print("计算1到100的和：")
total = 0
for i in range(1, 101):
    total += i
print(f"结果：{total}")
print(f"验证（公式）：{100 * 101 // 2}")
print()

print("2.2 字符串累加")
print("拼接单词：")
words = ["Python", "is", "awesome", "and", "powerful"]
sentence = ""
for word in words:
    if sentence:  # 如果不是第一个单词，添加空格
        sentence += " "
    sentence += word
print(f"结果：{sentence}")
print()

print("2.3 列表累加")
print("收集偶数：")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"偶数列表：{even_numbers}")
print()

print("2.4 乘积累加")
print("计算阶乘：")
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    print(f"{i}! = {factorial}")
print(f"最终结果：{n}! = {factorial}")
print()

# 3. 计数器模式
print("=== 3. 计数器模式 ===")
print()

print("3.1 条件计数")
text = "Hello World Python Programming"
print(f"文本：{text}")

vowel_count = 0
consonant_count = 0
space_count = 0

for char in text:
    if char.lower() in 'aeiou':
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1
    elif char == ' ':
        space_count += 1

print(f"元音字母：{vowel_count}")
print(f"辅音字母：{consonant_count}")
print(f"空格：{space_count}")
print()

print("3.2 分类计数")
scores = [85, 92, 78, 96, 88, 73, 91, 82, 95, 87]
print(f"成绩列表：{scores}")

excellent = 0  # 90分以上
good = 0       # 80-89分
pass_grade = 0 # 60-79分
fail = 0       # 60分以下

for score in scores:
    if score >= 90:
        excellent += 1
    elif score >= 80:
        good += 1
    elif score >= 60:
        pass_grade += 1
    else:
        fail += 1

print(f"优秀（90+）：{excellent}人")
print(f"良好（80-89）：{good}人")
print(f"及格（60-79）：{pass_grade}人")
print(f"不及格（<60）：{fail}人")
print()

print("3.3 频率统计")
text = "programming"
print(f"字符串：{text}")

char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("字符频率：")
for char, count in sorted(char_count.items()):
    print(f"  '{char}': {count}次")
print()

# 4. 查找模式
print("=== 4. 查找模式 ===")
print()

print("4.1 线性查找")
numbers = [3, 7, 1, 9, 4, 6, 8, 2, 5]
target = 6
print(f"在 {numbers} 中查找 {target}：")

found_index = -1
for i, num in enumerate(numbers):
    if num == target:
        found_index = i
        break

if found_index != -1:
    print(f"找到 {target}，位置：{found_index}")
else:
    print(f"未找到 {target}")
print()

print("4.2 查找最大值和最小值")
numbers = [23, 45, 12, 67, 34, 89, 56, 78]
print(f"数列：{numbers}")

max_val = numbers[0]
min_val = numbers[0]
max_index = 0
min_index = 0

for i, num in enumerate(numbers):
    if num > max_val:
        max_val = num
        max_index = i
    if num < min_val:
        min_val = num
        min_index = i

print(f"最大值：{max_val}，位置：{max_index}")
print(f"最小值：{min_val}，位置：{min_index}")
print()

print("4.3 查找所有匹配项")
text = "Python is great, Python is powerful, Python is easy"
keyword = "Python"
print(f"在文本中查找所有 '{keyword}'：")

positions = []
start = 0
while True:
    pos = text.find(keyword, start)
    if pos == -1:
        break
    positions.append(pos)
    start = pos + 1

print(f"找到 {len(positions)} 个匹配，位置：{positions}")
print()

# 5. 过滤模式
print("=== 5. 过滤模式 ===")
print()

print("5.1 条件过滤")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"原始数据：{numbers}")

# 过滤偶数
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"偶数：{even_numbers}")

# 过滤大于5的数
greater_than_5 = []
for num in numbers:
    if num > 5:
        greater_than_5.append(num)
print(f"大于5：{greater_than_5}")
print()

print("5.2 字符串过滤")
words = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"单词列表：{words}")

# 过滤长度大于5的单词
long_words = []
for word in words:
    if len(word) > 5:
        long_words.append(word)
print(f"长单词（>5字符）：{long_words}")

# 过滤包含'a'的单词
words_with_a = []
for word in words:
    if 'a' in word:
        words_with_a.append(word)
print(f"包含'a'的单词：{words_with_a}")
print()

print("5.3 复合条件过滤")
students = [
    {"name": "张三", "age": 20, "score": 85},
    {"name": "李四", "age": 19, "score": 92},
    {"name": "王五", "age": 21, "score": 78},
    {"name": "赵六", "age": 20, "score": 95}
]

print("学生信息：")
for student in students:
    print(f"  {student['name']}: {student['age']}岁, {student['score']}分")

# 过滤年龄20岁且成绩90分以上的学生
excellent_students = []
for student in students:
    if student['age'] == 20 and student['score'] >= 90:
        excellent_students.append(student)

print("\n20岁且成绩90+的学生：")
for student in excellent_students:
    print(f"  {student['name']}: {student['score']}分")
print()

# 6. 变换模式
print("=== 6. 变换模式 ===")
print()

print("6.1 数据变换")
numbers = [1, 2, 3, 4, 5]
print(f"原始数据：{numbers}")

# 平方变换
squares = []
for num in numbers:
    squares.append(num ** 2)
print(f"平方：{squares}")

# 字符串变换
str_numbers = []
for num in numbers:
    str_numbers.append(f"数字{num}")
print(f"字符串形式：{str_numbers}")
print()

print("6.2 格式变换")
names = ["alice", "bob", "charlie"]
print(f"原始姓名：{names}")

# 首字母大写
capitalized_names = []
for name in names:
    capitalized_names.append(name.capitalize())
print(f"首字母大写：{capitalized_names}")

# 添加前缀
formatted_names = []
for i, name in enumerate(names):
    formatted_names.append(f"{i+1}. {name.title()}")
print(f"编号格式：{formatted_names}")
print()

print("6.3 类型变换")
str_numbers = ["1", "2", "3", "4", "5"]
print(f"字符串数字：{str_numbers}")

# 转换为整数
int_numbers = []
for str_num in str_numbers:
    int_numbers.append(int(str_num))
print(f"整数：{int_numbers}")

# 转换为浮点数并乘以2.5
float_numbers = []
for str_num in str_numbers:
    float_numbers.append(float(str_num) * 2.5)
print(f"浮点数×2.5：{float_numbers}")
print()

# 7. 分组模式
print("=== 7. 分组模式 ===")
print()

print("7.1 按条件分组")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"数字：{numbers}")

even_group = []
odd_group = []

for num in numbers:
    if num % 2 == 0:
        even_group.append(num)
    else:
        odd_group.append(num)

print(f"偶数组：{even_group}")
print(f"奇数组：{odd_group}")
print()

print("7.2 按范围分组")
scores = [45, 67, 89, 92, 78, 56, 94, 73, 88, 91]
print(f"成绩：{scores}")

grade_groups = {
    'A': [],  # 90+
    'B': [],  # 80-89
    'C': [],  # 70-79
    'D': [],  # 60-69
    'F': []   # <60
}

for score in scores:
    if score >= 90:
        grade_groups['A'].append(score)
    elif score >= 80:
        grade_groups['B'].append(score)
    elif score >= 70:
        grade_groups['C'].append(score)
    elif score >= 60:
        grade_groups['D'].append(score)
    else:
        grade_groups['F'].append(score)

for grade, scores_list in grade_groups.items():
    if scores_list:
        print(f"{grade}等级：{scores_list}")
print()

print("7.3 按属性分组")
people = [
    {"name": "张三", "city": "北京", "age": 25},
    {"name": "李四", "city": "上海", "age": 30},
    {"name": "王五", "city": "北京", "age": 28},
    {"name": "赵六", "city": "广州", "age": 32},
    {"name": "钱七", "city": "上海", "age": 27}
]

print("人员信息：")
for person in people:
    print(f"  {person['name']}: {person['city']}, {person['age']}岁")

# 按城市分组
city_groups = {}
for person in people:
    city = person['city']
    if city not in city_groups:
        city_groups[city] = []
    city_groups[city].append(person['name'])

print("\n按城市分组：")
for city, names in city_groups.items():
    print(f"  {city}: {names}")
print()

# 8. 嵌套数据处理模式
print("=== 8. 嵌套数据处理模式 ===")
print()

print("8.1 处理嵌套列表")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("矩阵：")
for row in matrix:
    print(f"  {row}")

# 展平矩阵
flattened = []
for row in matrix:
    for element in row:
        flattened.append(element)
print(f"展平后：{flattened}")

# 计算所有元素的和
total = 0
for row in matrix:
    for element in row:
        total += element
print(f"所有元素的和：{total}")
print()

print("8.2 处理嵌套字典")
company = {
    "departments": {
        "IT": {
            "employees": ["张三", "李四"],
            "budget": 100000
        },
        "HR": {
            "employees": ["王五", "赵六", "钱七"],
            "budget": 80000
        },
        "Finance": {
            "employees": ["孙八"],
            "budget": 120000
        }
    }
}

print("公司部门信息：")
total_employees = 0
total_budget = 0

for dept_name, dept_info in company["departments"].items():
    employee_count = len(dept_info["employees"])
    budget = dept_info["budget"]
    
    print(f"  {dept_name}部门：")
    print(f"    员工：{dept_info['employees']}")
    print(f"    人数：{employee_count}")
    print(f"    预算：{budget:,}元")
    
    total_employees += employee_count
    total_budget += budget

print(f"\n总员工数：{total_employees}")
print(f"总预算：{total_budget:,}元")
print()

# 9. 生成器模式
print("=== 9. 生成器模式 ===")
print()

print("9.1 简单生成器")
def number_generator(n):
    """生成0到n-1的数字"""
    for i in range(n):
        yield i

print("使用生成器：")
for num in number_generator(5):
    print(f"生成的数字：{num}")
print()

print("9.2 斐波那契生成器")
def fibonacci_generator(n):
    """生成前n个斐波那契数"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("斐波那契数列（前10个）：")
fib_numbers = []
for fib in fibonacci_generator(10):
    fib_numbers.append(fib)
print(fib_numbers)
print()

print("9.3 过滤生成器")
def even_generator(numbers):
    """生成偶数"""
    for num in numbers:
        if num % 2 == 0:
            yield num

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"原始数字：{numbers}")
print("偶数：", end="")
for even in even_generator(numbers):
    print(even, end=" ")
print()
print()

# 10. 循环优化技巧
print("=== 10. 循环优化技巧 ===")
print()

print("10.1 提前退出优化")
print("在大列表中查找特定元素：")

# 创建大列表
large_list = list(range(1000000))
target = 500000

# 未优化版本
start_time = time.time()
found = False
for i, num in enumerate(large_list):
    if num == target:
        found = True
        position = i
        break  # 找到后立即退出
end_time = time.time()

print(f"找到目标 {target}，位置：{position}")
print(f"耗时：{end_time - start_time:.6f}秒")
print()

print("10.2 减少函数调用")
print("字符串处理优化：")

text = "Hello World Python Programming" * 1000

# 未优化版本
start_time = time.time()
count1 = 0
for char in text:
    if char.lower() in 'aeiou':  # 每次都调用lower()
        count1 += 1
end_time = time.time()
time1 = end_time - start_time

# 优化版本
start_time = time.time()
count2 = 0
vowels = 'aeiouAEIOU'  # 预定义包含大小写
for char in text:
    if char in vowels:  # 避免重复调用lower()
        count2 += 1
end_time = time.time()
time2 = end_time - start_time

print(f"未优化版本：{count1}个元音，耗时：{time1:.6f}秒")
print(f"优化版本：{count2}个元音，耗时：{time2:.6f}秒")
print(f"性能提升：{time1/time2:.2f}倍")
print()

print("10.3 使用内置函数")
print("求和操作比较：")

numbers = list(range(100000))

# 使用循环
start_time = time.time()
total1 = 0
for num in numbers:
    total1 += num
end_time = time.time()
time1 = end_time - start_time

# 使用内置函数
start_time = time.time()
total2 = sum(numbers)
end_time = time.time()
time2 = end_time - start_time

print(f"循环求和：{total1}，耗时：{time1:.6f}秒")
print(f"内置函数：{total2}，耗时：{time2:.6f}秒")
print(f"性能提升：{time1/time2:.2f}倍")
print()

# 11. 实际应用案例
print("=== 11. 实际应用案例 ===")
print()

print("11.1 数据清洗")
raw_data = [
    "  张三  ", "", "李四", None, "  王五  ", "赵六", "", "  "
]
print(f"原始数据：{raw_data}")

# 清洗数据：去除空值、空字符串和多余空格
cleaned_data = []
for item in raw_data:
    if item is not None and str(item).strip():  # 检查非空
        cleaned_item = str(item).strip()  # 去除空格
        cleaned_data.append(cleaned_item)

print(f"清洗后：{cleaned_data}")
print()

print("11.2 日志分析")
log_entries = [
    "2024-01-01 10:00:00 INFO User login successful",
    "2024-01-01 10:05:00 ERROR Database connection failed",
    "2024-01-01 10:10:00 INFO User logout",
    "2024-01-01 10:15:00 WARNING Low disk space",
    "2024-01-01 10:20:00 ERROR File not found",
    "2024-01-01 10:25:00 INFO System backup completed"
]

print("日志分析：")
log_stats = {
    'INFO': 0,
    'WARNING': 0,
    'ERROR': 0
}

error_messages = []

for entry in log_entries:
    parts = entry.split()
    if len(parts) >= 3:
        level = parts[2]
        if level in log_stats:
            log_stats[level] += 1
        
        if level == 'ERROR':
            error_messages.append(entry)

print("日志级别统计：")
for level, count in log_stats.items():
    print(f"  {level}: {count}条")

print("\n错误日志：")
for error in error_messages:
    print(f"  {error}")
print()

print("11.3 文本分析")
text = """
Python是一种高级编程语言。Python简单易学，功能强大。
许多公司都在使用Python开发项目。Python在数据科学领域特别受欢迎。
学习Python可以帮助你成为更好的程序员。
"""

print("文本分析：")
print(f"原文：{text.strip()}")

# 分词（简单按空格和标点分割）
words = []
current_word = ""

for char in text:
    if char.isalnum():
        current_word += char
    else:
        if current_word:
            words.append(current_word)
            current_word = ""

if current_word:
    words.append(current_word)

# 词频统计
word_count = {}
for word in words:
    word_lower = word.lower()
    if word_lower in word_count:
        word_count[word_lower] += 1
    else:
        word_count[word_lower] = 1

# 按频率排序
sorted_words = []
for word, count in word_count.items():
    sorted_words.append((word, count))

# 简单排序（按频率降序）
for i in range(len(sorted_words)):
    for j in range(i + 1, len(sorted_words)):
        if sorted_words[i][1] < sorted_words[j][1]:
            sorted_words[i], sorted_words[j] = sorted_words[j], sorted_words[i]

print(f"\n总词数：{len(words)}")
print(f"不重复词数：{len(word_count)}")
print("\n词频统计（前10个）：")
for word, count in sorted_words[:10]:
    print(f"  '{word}': {count}次")
print()

if __name__ == "__main__":
    print("=== 常见循环模式学习总结 ===")
    print("通过本节学习，你应该掌握了：")
    print("1. 循环控制语句的正确使用")
    print("2. 累加器和计数器模式")
    print("3. 查找和过滤的实现技巧")
    print("4. 数据变换和分组方法")
    print("5. 嵌套数据的处理策略")
    print("6. 生成器的基本概念")
    print("7. 循环性能优化技巧")
    print("8. 实际问题的解决方案")
    print("\n掌握这些循环模式将大大提高你的编程效率和代码质量！")
```

## 注意事项

1. **性能考虑**：选择合适的循环模式可以显著提高性能
2. **可读性**：优雅的循环模式让代码更易理解和维护
3. **内存使用**：注意大数据集的内存消耗
4. **提前退出**：合理使用break可以避免不必要的计算

## 练习建议

1. 实践各种循环控制语句的组合使用
2. 编写不同类型的累加器和计数器
3. 实现各种查找和过滤算法
4. 练习数据变换和分组操作
5. 尝试优化现有的循环代码

通过大量练习这些循环模式，你将能够写出更加高效、优雅的Python代码。