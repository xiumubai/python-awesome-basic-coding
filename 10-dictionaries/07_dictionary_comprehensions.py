#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字典推导式 - 字典推导式详解

学习目标：
1. 掌握字典推导式的基本语法
2. 学会使用条件过滤创建字典
3. 了解字典推导式的高级用法
4. 掌握字典推导式的性能优势

作者：Python学习教程
日期：2024年
"""

print("=" * 50)
print("字典推导式 - 字典推导式详解")
print("=" * 50)

# 1. 基本字典推导式语法
print("\n1. 基本字典推导式语法")
print("-" * 30)

# 基本语法：{key_expression: value_expression for item in iterable}

# 从列表创建字典
numbers = [1, 2, 3, 4, 5]
squares = {x: x**2 for x in numbers}
print(f"数字及其平方: {squares}")

# 从字符串创建字典
word = "python"
char_positions = {char: index for index, char in enumerate(word)}
print(f"字符位置字典: {char_positions}")

# 从范围创建字典
cubes = {x: x**3 for x in range(1, 6)}
print(f"立方数字典: {cubes}")

# 2. 带条件的字典推导式
print("\n2. 带条件的字典推导式")
print("-" * 30)

# 语法：{key: value for item in iterable if condition}

# 筛选偶数的平方
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"偶数平方: {even_squares}")

# 筛选长度大于3的单词
words = ["cat", "dog", "elephant", "bird", "python", "java"]
long_words = {word: len(word) for word in words if len(word) > 3}
print(f"长单词及长度: {long_words}")

# 筛选正数
numbers_mixed = [-3, -1, 0, 2, 5, -2, 8]
positive_squares = {x: x**2 for x in numbers_mixed if x > 0}
print(f"正数平方: {positive_squares}")

# 3. 从现有字典创建新字典
print("\n3. 从现有字典创建新字典")
print("-" * 30)

# 原始价格字典
prices = {
    "apple": 3.5,
    "banana": 2.0,
    "orange": 4.0,
    "grape": 8.0,
    "watermelon": 15.0
}

# 应用折扣
discounted_prices = {item: price * 0.8 for item, price in prices.items()}
print(f"打折后价格: {discounted_prices}")

# 筛选昂贵商品
expensive_items = {item: price for item, price in prices.items() if price > 5.0}
print(f"昂贵商品: {expensive_items}")

# 价格分类
price_categories = {
    item: "便宜" if price < 5 else "昂贵" 
    for item, price in prices.items()
}
print(f"价格分类: {price_categories}")

# 4. 复杂的键值表达式
print("\n4. 复杂的键值表达式")
print("-" * 30)

# 学生成绩数据
students = [
    ("张三", 85),
    ("李四", 92),
    ("王五", 78),
    ("赵六", 96),
    ("钱七", 88)
]

# 创建成绩等级字典
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

student_grades = {name: get_grade(score) for name, score in students}
print(f"学生成绩等级: {student_grades}")

# 格式化键名
formatted_students = {f"学生_{name}": f"{score}分({get_grade(score)})" 
                     for name, score in students}
print(f"格式化学生信息: {formatted_students}")

# 5. 嵌套字典推导式
print("\n5. 嵌套字典推导式")
print("-" * 30)

# 创建乘法表
multiplication_table = {
    i: {j: i * j for j in range(1, 6)} 
    for i in range(1, 6)
}
print("乘法表:")
for i, row in multiplication_table.items():
    print(f"  {i}: {row}")

# 学生各科成绩
subjects = ["数学", "英语", "物理"]
student_names = ["小明", "小红", "小刚"]

# 生成随机成绩（模拟）
import random
random.seed(42)  # 固定随机种子，确保结果可重现

student_scores = {
    student: {subject: random.randint(60, 100) for subject in subjects}
    for student in student_names
}

print("\n学生各科成绩:")
for student, scores in student_scores.items():
    print(f"  {student}: {scores}")

# 6. 使用zip()创建字典
print("\n6. 使用zip()创建字典")
print("-" * 30)

# 两个列表组合成字典
cities = ["北京", "上海", "广州", "深圳"]
populations = [2154, 2424, 1530, 1344]  # 单位：万人

city_population = {city: pop for city, pop in zip(cities, populations)}
print(f"城市人口: {city_population}")

# 多个列表组合
product_names = ["笔记本", "鼠标", "键盘"]
product_prices = [5999, 99, 299]
product_stocks = [50, 200, 150]

products = {
    name: {"price": price, "stock": stock}
    for name, price, stock in zip(product_names, product_prices, product_stocks)
}
print(f"产品信息: {products}")

# 7. 字符串处理的字典推导式
print("\n7. 字符串处理的字典推导式")
print("-" * 30)

# 统计字符频率
text = "hello world python programming"
char_frequency = {char: text.count(char) for char in set(text) if char != ' '}
print(f"字符频率: {sorted(char_frequency.items())}")

# 单词长度统计
sentence = "Python is a powerful programming language"
words_list = sentence.lower().split()
word_lengths = {word: len(word) for word in words_list}
print(f"单词长度: {word_lengths}")

# 首字母大写转换
names = ["alice", "bob", "charlie", "diana"]
capitalized_names = {name: name.capitalize() for name in names}
print(f"首字母大写: {capitalized_names}")

# 8. 数据转换和清理
print("\n8. 数据转换和清理")
print("-" * 30)

# 原始数据（包含一些需要清理的数据）
raw_data = {
    "  Apple  ": "3.50",
    "BANANA": "2.00",
    "  orange": "4.00",
    "Grape  ": "8.00"
}

# 清理和转换数据
cleaned_data = {
    key.strip().lower(): float(value)
    for key, value in raw_data.items()
    if value.replace('.', '').isdigit()
}
print(f"清理后的数据: {cleaned_data}")

# 数据验证和过滤
user_inputs = {
    "age": "25",
    "height": "175.5",
    "weight": "invalid",
    "score": "95"
}

# 只保留有效的数字数据
valid_numbers = {
    key: float(value) if '.' in value else int(value)
    for key, value in user_inputs.items()
    if value.replace('.', '').isdigit()
}
print(f"有效数字数据: {valid_numbers}")

# 9. 性能比较：字典推导式 vs 传统方法
print("\n9. 性能比较：字典推导式 vs 传统方法")
print("-" * 30)

import time

# 测试数据
test_range = range(10000)

# 方法1：传统for循环
start_time = time.time()
traditional_dict = {}
for x in test_range:
    traditional_dict[x] = x ** 2
traditional_time = time.time() - start_time

# 方法2：字典推导式
start_time = time.time()
comprehension_dict = {x: x ** 2 for x in test_range}
comprehension_time = time.time() - start_time

print(f"传统方法耗时: {traditional_time:.6f}秒")
print(f"推导式耗时: {comprehension_time:.6f}秒")
print(f"推导式速度提升: {traditional_time/comprehension_time:.2f}倍")

# 验证结果相同
print(f"结果是否相同: {traditional_dict == comprehension_dict}")

# 10. 实际应用案例
print("\n10. 实际应用案例")
print("-" * 30)

# 案例1：配置文件处理
config_strings = {
    "database.host": "localhost",
    "database.port": "5432",
    "cache.enabled": "true",
    "cache.ttl": "300",
    "debug.level": "info"
}

# 转换配置值的类型
def convert_config_value(value):
    if value.lower() == "true":
        return True
    elif value.lower() == "false":
        return False
    elif value.isdigit():
        return int(value)
    else:
        return value

config = {key: convert_config_value(value) for key, value in config_strings.items()}
print(f"转换后的配置: {config}")

# 案例2：数据分组
sales_data = [
    ("2024-01", "北京", 1000),
    ("2024-01", "上海", 1200),
    ("2024-02", "北京", 1100),
    ("2024-02", "上海", 1300),
    ("2024-01", "广州", 800),
    ("2024-02", "广州", 900)
]

# 按月份分组销售数据
monthly_sales = {}
for month, city, amount in sales_data:
    if month not in monthly_sales:
        monthly_sales[month] = {}
    monthly_sales[month][city] = amount

print(f"\n按月份分组的销售数据: {monthly_sales}")

# 使用字典推导式计算月度总销售额
monthly_totals = {
    month: sum(cities.values())
    for month, cities in monthly_sales.items()
}
print(f"月度总销售额: {monthly_totals}")

# 案例3：数据透视
# 计算每个城市的总销售额
city_totals = {}
for month, city, amount in sales_data:
    city_totals[city] = city_totals.get(city, 0) + amount

print(f"城市总销售额: {city_totals}")

# 使用字典推导式找出销售额最高的城市
top_city = {city: total for city, total in city_totals.items() 
           if total == max(city_totals.values())}
print(f"销售额最高的城市: {top_city}")

# 11. 高级技巧和注意事项
print("\n11. 高级技巧和注意事项")
print("-" * 30)

# 技巧1：使用enumerate获取索引
items = ["apple", "banana", "cherry"]
indexed_items = {index: item for index, item in enumerate(items)}
print(f"带索引的字典: {indexed_items}")

# 技巧2：反转字典
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {value: key for key, value in original.items()}
print(f"原字典: {original}")
print(f"反转字典: {reversed_dict}")

# 技巧3：合并多个字典
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}

# Python 3.9+ 可以使用 | 操作符
# merged = dict1 | dict2 | dict3

# 兼容性更好的方法
merged = {k: v for d in [dict1, dict2, dict3] for k, v in d.items()}
print(f"合并字典: {merged}")

# 注意事项：避免重复键
data_with_duplicates = [("a", 1), ("b", 2), ("a", 3)]  # 'a'重复
result = {k: v for k, v in data_with_duplicates}
print(f"重复键处理（后者覆盖前者）: {result}")

# 处理重复键：收集所有值
from collections import defaultdict
collected = defaultdict(list)
for k, v in data_with_duplicates:
    collected[k].append(v)
collected_dict = {k: v for k, v in collected.items()}
print(f"收集重复键的所有值: {dict(collected_dict)}")

print("\n" + "=" * 50)
print("字典推导式总结：")
print("1. 基本语法 - {key: value for item in iterable}")
print("2. 条件过滤 - {key: value for item in iterable if condition}")
print("3. 性能优势 - 比传统循环更快更简洁")
print("4. 可读性 - 代码更加简洁和Pythonic")
print("5. 灵活性 - 支持复杂的键值表达式")
print("6. 注意重复键 - 后面的值会覆盖前面的值")
print("=" * 50)

if __name__ == "__main__":
    print("\n程序执行完成！")
    print("请尝试修改代码，练习各种字典推导式的用法。")