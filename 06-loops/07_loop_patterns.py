#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python循环 - 常见循环模式

本文件演示Python中常见的循环模式和编程技巧。
这些模式在实际编程中经常使用，掌握它们可以让代码更加简洁高效。

学习目标：
1. 掌握常见的循环模式和习惯用法
2. 学会使用循环控制语句（break、continue）
3. 了解循环优化技巧
4. 掌握实用的循环应用模式

作者：Python学习教程
日期：2024年
"""

# 1. 循环控制语句
print("=== 1. 循环控制语句 ===")
print("break和continue是控制循环执行的重要语句")
print()

print("break语句 - 跳出整个循环：")
for i in range(10):
    if i == 5:
        print(f"  遇到 {i}，跳出循环")
        break
    print(f"  当前数字：{i}")
print("  循环结束")
print()

print("continue语句 - 跳过当前迭代：")
for i in range(10):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(f"  奇数：{i}")
print()

print("在嵌套循环中使用break和continue：")
for i in range(3):
    print(f"外层循环 i = {i}")
    for j in range(5):
        if j == 3:
            print(f"    内层遇到 {j}，跳出内层循环")
            break
        if j == 1:
            print(f"    跳过 j = {j}")
            continue
        print(f"    内层循环 j = {j}")
    print()

# 2. 循环与else语句
print("=== 2. 循环与else语句 ===")
print("循环的else子句在循环正常结束时执行（没有被break中断）")
print()

print("示例1：查找质数")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"    {n} 不是质数，因为 {n} % {i} = 0")
            break
    else:
        print(f"    {n} 是质数")
        return True
    return False

test_numbers = [7, 12, 17, 20]
for num in test_numbers:
    is_prime(num)
print()

print("示例2：在列表中查找元素")
fruits = ["apple", "banana", "orange", "grape"]
target = "orange"

for i, fruit in enumerate(fruits):
    if fruit == target:
        print(f"  找到 {target}，位置：{i}")
        break
else:
    print(f"  没有找到 {target}")
print()

# 3. 累加器模式
print("=== 3. 累加器模式 ===")
print("累加器模式是循环中最常见的模式之一")
print()

print("基本累加：")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for num in numbers:
    total += num
print(f"  数字列表：{numbers}")
print(f"  总和：{total}")
print()

print("条件累加：")
even_sum = 0
odd_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
print(f"  偶数和：{even_sum}")
print(f"  奇数和：{odd_sum}")
print()

print("累乘模式：")
factorial = 1
n = 5
for i in range(1, n + 1):
    factorial *= i
print(f"  {n}! = {factorial}")
print()

print("字符串累加：")
words = ["Hello", "World", "Python", "Programming"]
sentence = ""
for word in words:
    sentence += word + " "
sentence = sentence.strip()  # 去掉末尾空格
print(f"  单词列表：{words}")
print(f"  组合句子：{sentence}")
print()

# 4. 计数器模式
print("=== 4. 计数器模式 ===")
print("计数器模式用于统计满足条件的元素数量")
print()

text = "Hello World! How are you today?"
print(f"文本：{text}")

# 统计不同类型的字符
vowel_count = 0
consonant_count = 0
digit_count = 0
space_count = 0
other_count = 0

vowels = "aeiouAEIOU"

for char in text:
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1
    else:
        other_count += 1

print(f"  元音字母：{vowel_count}")
print(f"  辅音字母：{consonant_count}")
print(f"  数字：{digit_count}")
print(f"  空格：{space_count}")
print(f"  其他字符：{other_count}")
print()

# 5. 查找模式
print("=== 5. 查找模式 ===")
print("查找模式用于在数据中寻找特定的元素或条件")
print()

scores = [85, 92, 78, 96, 88, 76, 94, 82, 90, 87]
print(f"成绩列表：{scores}")

# 查找最大值和最小值
max_score = scores[0]
min_score = scores[0]
max_index = 0
min_index = 0

for i, score in enumerate(scores):
    if score > max_score:
        max_score = score
        max_index = i
    if score < min_score:
        min_score = score
        min_index = i

print(f"  最高分：{max_score}（位置：{max_index}）")
print(f"  最低分：{min_score}（位置：{min_index}）")
print()

# 查找第一个满足条件的元素
print("查找第一个90分以上的成绩：")
for i, score in enumerate(scores):
    if score >= 90:
        print(f"  找到：{score}分（位置：{i}）")
        break
else:
    print("  没有找到90分以上的成绩")
print()

# 查找所有满足条件的元素
print("查找所有80分以上的成绩：")
high_scores = []
for i, score in enumerate(scores):
    if score >= 80:
        high_scores.append((score, i))

print(f"  高分成绩：{high_scores}")
print()

# 6. 过滤模式
print("=== 6. 过滤模式 ===")
print("过滤模式用于从数据中筛选出满足条件的元素")
print()

numbers = list(range(1, 21))  # 1到20的数字
print(f"原始数字：{numbers}")

# 过滤偶数
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"偶数：{even_numbers}")

# 过滤质数
primes = []
for num in numbers:
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
print(f"质数：{primes}")

# 过滤完全平方数
perfect_squares = []
for num in numbers:
    sqrt_num = int(num ** 0.5)
    if sqrt_num * sqrt_num == num:
        perfect_squares.append(num)
print(f"完全平方数：{perfect_squares}")
print()

# 7. 变换模式
print("=== 7. 变换模式 ===")
print("变换模式用于将数据从一种形式转换为另一种形式")
print()

original_list = [1, 2, 3, 4, 5]
print(f"原始列表：{original_list}")

# 平方变换
squared_list = []
for num in original_list:
    squared_list.append(num ** 2)
print(f"平方后：{squared_list}")

# 字符串变换
string_list = []
for num in original_list:
    string_list.append(f"数字{num}")
print(f"字符串化：{string_list}")

# 条件变换
conditional_list = []
for num in original_list:
    if num % 2 == 0:
        conditional_list.append(num * 10)  # 偶数乘以10
    else:
        conditional_list.append(num * 100)  # 奇数乘以100
print(f"条件变换：{conditional_list}")
print()

# 8. 分组模式
print("=== 8. 分组模式 ===")
print("分组模式用于将数据按照某种规则进行分类")
print()

students = [
    {"name": "张三", "age": 20, "grade": "A"},
    {"name": "李四", "age": 19, "grade": "B"},
    {"name": "王五", "age": 21, "grade": "A"},
    {"name": "赵六", "age": 20, "grade": "C"},
    {"name": "钱七", "age": 19, "grade": "B"}
]

print("学生信息：")
for student in students:
    print(f"  {student}")
print()

# 按年龄分组
age_groups = {}
for student in students:
    age = student["age"]
    if age not in age_groups:
        age_groups[age] = []
    age_groups[age].append(student["name"])

print("按年龄分组：")
for age, names in age_groups.items():
    print(f"  {age}岁：{names}")
print()

# 按成绩分组
grade_groups = {}
for student in students:
    grade = student["grade"]
    if grade not in grade_groups:
        grade_groups[grade] = []
    grade_groups[grade].append(student["name"])

print("按成绩分组：")
for grade, names in sorted(grade_groups.items()):
    print(f"  {grade}等：{names}")
print()

# 9. 嵌套数据处理模式
print("=== 9. 嵌套数据处理模式 ===")
print("处理复杂的嵌套数据结构")
print()

# 处理嵌套列表
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("原始矩阵：")
for row in matrix:
    print(f"  {row}")

# 展平矩阵
flattened = []
for row in matrix:
    for element in row:
        flattened.append(element)
print(f"展平后：{flattened}")

# 矩阵每个元素加1
incremented_matrix = []
for row in matrix:
    new_row = []
    for element in row:
        new_row.append(element + 1)
    incremented_matrix.append(new_row)

print("每个元素+1：")
for row in incremented_matrix:
    print(f"  {row}")
print()

# 处理嵌套字典
company = {
    "departments": {
        "IT": {
            "employees": ["Alice", "Bob", "Charlie"],
            "budget": 100000
        },
        "HR": {
            "employees": ["David", "Eve"],
            "budget": 50000
        },
        "Finance": {
            "employees": ["Frank", "Grace", "Henry", "Ivy"],
            "budget": 80000
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
    print(f"    预算：{budget}")
    
    total_employees += employee_count
    total_budget += budget

print(f"\n公司总计：")
print(f"  总员工数：{total_employees}")
print(f"  总预算：{total_budget}")
print()

# 10. 生成器模式
print("=== 10. 生成器模式 ===")
print("使用循环创建生成器和迭代器")
print()

# 斐波那契数列生成器
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
for num in fibonacci_generator(10):
    fib_numbers.append(num)
print(f"  {fib_numbers}")
print()

# 质数生成器
def prime_generator(limit):
    """生成小于limit的所有质数"""
    for num in range(2, limit):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

print("30以内的质数：")
primes_list = []
for prime in prime_generator(30):
    primes_list.append(prime)
print(f"  {primes_list}")
print()

# 11. 优化技巧
print("=== 11. 优化技巧 ===")
print("提高循环性能的常用技巧")
print()

# 技巧1：减少函数调用
print("技巧1：减少重复的函数调用")
data = list(range(1000))

# 不好的做法
import time
start = time.time()
result1 = []
for i in range(len(data)):  # 每次都调用len()
    if data[i] % 2 == 0:
        result1.append(data[i])
time1 = time.time() - start

# 好的做法
start = time.time()
result2 = []
data_len = len(data)  # 只调用一次len()
for i in range(data_len):
    if data[i] % 2 == 0:
        result2.append(data[i])
time2 = time.time() - start

print(f"  重复调用len()：{time1:.6f}秒")
print(f"  缓存len()结果：{time2:.6f}秒")
print(f"  性能提升：{(time1-time2)/time1*100:.1f}%")
print()

# 技巧2：使用enumerate而不是range(len())
print("技巧2：使用enumerate而不是range(len())")
items = ["apple", "banana", "cherry", "date"]

print("不推荐的写法：")
for i in range(len(items)):
    print(f"  {i}: {items[i]}")

print("推荐的写法：")
for i, item in enumerate(items):
    print(f"  {i}: {item}")
print()

# 技巧3：使用列表推导式
print("技巧3：使用列表推导式替代简单循环")
numbers = list(range(10))

# 传统循环
squares1 = []
for num in numbers:
    squares1.append(num ** 2)

# 列表推导式
squares2 = [num ** 2 for num in numbers]

print(f"  传统循环结果：{squares1}")
print(f"  列表推导式结果：{squares2}")
print(f"  结果相同：{squares1 == squares2}")
print()

# 12. 实际应用案例
print("=== 12. 实际应用案例 ===")

# 案例1：数据清洗
print("案例1：数据清洗")
raw_data = [
    "  Alice  ",
    "BOB",
    "charlie",
    "  ",
    "DAVID  ",
    "eve",
    None,
    "frank"
]

print(f"原始数据：{raw_data}")

# 清洗数据：去空格、统一大小写、过滤空值
cleaned_data = []
for item in raw_data:
    if item is not None:  # 过滤None值
        cleaned_item = item.strip()  # 去除首尾空格
        if cleaned_item:  # 过滤空字符串
            cleaned_data.append(cleaned_item.title())  # 转换为标题格式

print(f"清洗后数据：{cleaned_data}")
print()

# 案例2：日志分析
print("案例2：简单日志分析")
logs = [
    "2024-01-01 10:00:00 INFO User login: alice",
    "2024-01-01 10:05:00 ERROR Database connection failed",
    "2024-01-01 10:10:00 INFO User login: bob",
    "2024-01-01 10:15:00 WARNING Low disk space",
    "2024-01-01 10:20:00 ERROR File not found",
    "2024-01-01 10:25:00 INFO User logout: alice"
]

print("日志分析：")
log_stats = {"INFO": 0, "WARNING": 0, "ERROR": 0}
user_actions = []

for log in logs:
    parts = log.split()
    if len(parts) >= 3:
        level = parts[2]
        if level in log_stats:
            log_stats[level] += 1
        
        # 提取用户操作
        if "User" in log:
            user_actions.append(log)

print(f"  日志级别统计：{log_stats}")
print("  用户操作：")
for action in user_actions:
    print(f"    {action}")
print()

# 案例3：简单的文本分析
print("案例3：文本分析")
text = """
Python is a powerful programming language.
It is easy to learn and use.
Python is widely used in data science, web development, and automation.
"""

print("文本内容：")
print(text.strip())
print()

# 统计词频
words = text.lower().replace('.', '').replace(',', '').split()
word_count = {}

for word in words:
    if word:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

print("词频统计（按频率排序）：")
# 按频率排序
sorted_words = []
for word, count in word_count.items():
    sorted_words.append((count, word))

# 简单排序（冒泡排序）
for i in range(len(sorted_words)):
    for j in range(len(sorted_words) - 1 - i):
        if sorted_words[j][0] < sorted_words[j + 1][0]:
            sorted_words[j], sorted_words[j + 1] = sorted_words[j + 1], sorted_words[j]

for count, word in sorted_words[:10]:  # 显示前10个
    print(f"  {word}: {count}次")
print()

# 13. 练习题
print("=== 13. 练习题 ===")

print("练习1：实现简单的排序算法（冒泡排序）")
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"原始数组：{numbers}")

# 冒泡排序实现
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(f"排序后：{numbers}")
print()

print("练习2：找出数组中的重复元素")
test_array = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]
print(f"测试数组：{test_array}")

duplicates = []
for i in range(len(test_array)):
    for j in range(i + 1, len(test_array)):
        if test_array[i] == test_array[j] and test_array[i] not in duplicates:
            duplicates.append(test_array[i])

print(f"重复元素：{duplicates}")
print()

print("练习3：计算字符串的编辑距离（简化版）")
str1 = "kitten"
str2 = "sitting"
print(f"字符串1：{str1}")
print(f"字符串2：{str2}")

# 简化的编辑距离计算（只考虑替换操作）
differences = 0
min_len = min(len(str1), len(str2))
for i in range(min_len):
    if str1[i] != str2[i]:
        differences += 1

# 加上长度差异
differences += abs(len(str1) - len(str2))
print(f"编辑距离（简化版）：{differences}")

if __name__ == "__main__":
    print("\n=== 常见循环模式学习总结 ===")
    print("1. 控制语句：break跳出循环，continue跳过当前迭代")
    print("2. 循环else：在循环正常结束时执行")
    print("3. 累加器模式：用于求和、求积、字符串拼接")
    print("4. 计数器模式：统计满足条件的元素数量")
    print("5. 查找模式：寻找特定元素或最值")
    print("6. 过滤模式：筛选满足条件的元素")
    print("7. 变换模式：将数据转换为其他形式")
    print("8. 分组模式：按规则对数据进行分类")
    print("9. 优化技巧：减少函数调用、使用enumerate、列表推导式")
    print("10. 实际应用：数据清洗、日志分析、文本处理")
    print("11. 调试建议：使用print语句、逐步验证逻辑")
    print("12. 性能考虑：选择合适的算法和数据结构")