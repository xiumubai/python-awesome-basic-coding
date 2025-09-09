#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lambda表达式与map函数

本文件介绍Lambda表达式与map函数的结合使用，
学习如何使用map函数对序列进行批量处理。

学习目标：
1. 理解map函数的工作原理
2. 掌握Lambda表达式与map函数的结合使用
3. 学会使用map进行数据转换
4. 了解map函数的性能优势
"""

import time
from functools import reduce

# 1. map函数基础
print("=== 1. map函数基础 ===")
print("map函数语法：map(function, iterable)")
print("作用：将函数应用到可迭代对象的每个元素上")
print()

# 基本使用示例
numbers = [1, 2, 3, 4, 5]

# 使用Lambda表达式计算平方
squares = list(map(lambda x: x ** 2, numbers))
print(f"原始数字: {numbers}")
print(f"平方结果: {squares}")

# 使用Lambda表达式计算立方
cubes = list(map(lambda x: x ** 3, numbers))
print(f"立方结果: {cubes}")
print()

# 2. map与普通函数对比
print("=== 2. map与普通函数对比 ===")

# 传统方法：使用循环
def square_with_loop(numbers):
    """使用循环计算平方"""
    result = []
    for num in numbers:
        result.append(num ** 2)
    return result

# 使用map和Lambda
def square_with_map(numbers):
    """使用map和Lambda计算平方"""
    return list(map(lambda x: x ** 2, numbers))

# 使用列表推导式
def square_with_comprehension(numbers):
    """使用列表推导式计算平方"""
    return [x ** 2 for x in numbers]

test_numbers = list(range(1, 11))
print(f"测试数据: {test_numbers}")
print(f"循环方法: {square_with_loop(test_numbers)}")
print(f"map方法: {square_with_map(test_numbers)}")
print(f"推导式方法: {square_with_comprehension(test_numbers)}")
print()

# 3. 多种数据类型的map操作
print("=== 3. 多种数据类型的map操作 ===")

# 字符串操作
words = ['hello', 'world', 'python', 'lambda']
uppercase_words = list(map(lambda s: s.upper(), words))
capitalized_words = list(map(lambda s: s.capitalize(), words))
word_lengths = list(map(lambda s: len(s), words))

print(f"原始单词: {words}")
print(f"转大写: {uppercase_words}")
print(f"首字母大写: {capitalized_words}")
print(f"单词长度: {word_lengths}")
print()

# 数值转换
string_numbers = ['1', '2', '3', '4', '5']
integers = list(map(lambda x: int(x), string_numbers))
floats = list(map(lambda x: float(x), string_numbers))

print(f"字符串数字: {string_numbers}")
print(f"转换为整数: {integers}")
print(f"转换为浮点数: {floats}")
print()

# 4. 复杂的Lambda表达式与map
print("=== 4. 复杂的Lambda表达式与map ===")

# 温度转换
celsius_temps = [0, 20, 30, 37, 100]
fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, celsius_temps))

print(f"摄氏温度: {celsius_temps}")
print(f"华氏温度: {fahrenheit_temps}")

# 数据清洗
raw_data = ['  hello  ', '\tworld\n', '  python\t', 'lambda\n\n']
cleaned_data = list(map(lambda s: s.strip().upper(), raw_data))

print(f"原始数据: {raw_data}")
print(f"清洗后数据: {cleaned_data}")

# 条件转换
scores = [85, 92, 78, 96, 73, 88]
grades = list(map(lambda score: 'A' if score >= 90 else ('B' if score >= 80 else 'C'), scores))

print(f"分数: {scores}")
print(f"等级: {grades}")
print()

# 5. 多个可迭代对象的map操作
print("=== 5. 多个可迭代对象的map操作 ===")

# 两个列表的运算
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

# 对应元素相加
sums = list(map(lambda x, y: x + y, list1, list2))
print(f"列表1: {list1}")
print(f"列表2: {list2}")
print(f"对应相加: {sums}")

# 对应元素相乘
products = list(map(lambda x, y: x * y, list1, list2))
print(f"对应相乘: {products}")

# 三个列表的运算
list3 = [100, 200, 300, 400, 500]
triple_sums = list(map(lambda x, y, z: x + y + z, list1, list2, list3))
print(f"列表3: {list3}")
print(f"三列表相加: {triple_sums}")
print()

# 6. map与字典操作
print("=== 6. map与字典操作 ===")

# 学生数据处理
students = [
    {'name': '张三', 'math': 85, 'english': 78},
    {'name': '李四', 'math': 92, 'english': 88},
    {'name': '王五', 'math': 76, 'english': 82},
    {'name': '赵六', 'math': 89, 'english': 91}
]

# 计算总分
total_scores = list(map(lambda student: {
    'name': student['name'],
    'total': student['math'] + student['english']
}, students))

print("学生总分：")
for student in total_scores:
    print(f"{student['name']}: {student['total']}分")

# 提取姓名
names = list(map(lambda student: student['name'], students))
print(f"\n学生姓名: {names}")

# 计算平均分
averages = list(map(lambda student: {
    'name': student['name'],
    'average': (student['math'] + student['english']) / 2
}, students))

print("\n学生平均分：")
for student in averages:
    print(f"{student['name']}: {student['average']:.1f}分")
print()

# 7. map的性能测试
print("=== 7. map的性能测试 ===")

# 准备大量数据
large_numbers = list(range(100000))

# 测试不同方法的性能
def test_performance():
    # 方法1：使用map和Lambda
    start_time = time.time()
    result1 = list(map(lambda x: x ** 2, large_numbers))
    map_time = time.time() - start_time
    
    # 方法2：使用列表推导式
    start_time = time.time()
    result2 = [x ** 2 for x in large_numbers]
    comprehension_time = time.time() - start_time
    
    # 方法3：使用普通循环
    start_time = time.time()
    result3 = []
    for x in large_numbers:
        result3.append(x ** 2)
    loop_time = time.time() - start_time
    
    return map_time, comprehension_time, loop_time

map_time, comp_time, loop_time = test_performance()
print(f"map + Lambda 时间: {map_time:.4f} 秒")
print(f"列表推导式时间: {comp_time:.4f} 秒")
print(f"普通循环时间: {loop_time:.4f} 秒")
print()

# 8. map的惰性求值
print("=== 8. map的惰性求值 ===")

# map返回迭代器，不是列表
map_result = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(f"map对象: {map_result}")
print(f"map对象类型: {type(map_result)}")

# 需要转换为列表才能看到结果
print(f"转换为列表: {list(map_result)}")

# 迭代器只能使用一次
map_result2 = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(f"第一次转换: {list(map_result2)}")
print(f"第二次转换: {list(map_result2)}")
print("注意：迭代器只能使用一次！")
print()

# 9. 实际应用案例
print("=== 9. 实际应用案例 ===")

# 案例1：数据标准化
data = [1.5, 2.3, 3.7, 4.1, 5.9, 6.2, 7.8, 8.4, 9.1, 10.0]
mean = sum(data) / len(data)
std = (sum(map(lambda x: (x - mean) ** 2, data)) / len(data)) ** 0.5
normalized = list(map(lambda x: (x - mean) / std, data))

print(f"原始数据: {data}")
print(f"均值: {mean:.2f}, 标准差: {std:.2f}")
print(f"标准化数据: {[round(x, 2) for x in normalized]}")

# 案例2：文件路径处理
file_paths = [
    '/home/user/document.txt',
    '/home/user/image.jpg',
    '/home/user/script.py',
    '/home/user/data.csv'
]

# 提取文件名
filenames = list(map(lambda path: path.split('/')[-1], file_paths))
print(f"\n文件路径: {file_paths}")
print(f"文件名: {filenames}")

# 提取文件扩展名
extensions = list(map(lambda path: path.split('.')[-1], file_paths))
print(f"扩展名: {extensions}")

# 案例3：API数据处理
api_response = [
    {'id': 1, 'name': 'Product A', 'price': '29.99'},
    {'id': 2, 'name': 'Product B', 'price': '39.99'},
    {'id': 3, 'name': 'Product C', 'price': '19.99'}
]

# 转换价格为浮点数并添加税费
processed_products = list(map(lambda item: {
    'id': item['id'],
    'name': item['name'],
    'price': float(item['price']),
    'price_with_tax': float(item['price']) * 1.1
}, api_response))

print("\n处理后的产品数据：")
for product in processed_products:
    print(f"ID: {product['id']}, 名称: {product['name']}, "
          f"原价: ${product['price']:.2f}, 含税: ${product['price_with_tax']:.2f}")
print()

# 10. 最佳实践和注意事项
print("=== 10. 最佳实践和注意事项 ===")
print("map函数的优点：")
print("✓ 代码简洁，函数式编程风格")
print("✓ 惰性求值，内存效率高")
print("✓ 可以处理多个可迭代对象")
print("✓ 与Lambda表达式结合使用方便")
print()
print("使用注意事项：")
print("⚠ map返回迭代器，需要转换为列表查看结果")
print("⚠ 迭代器只能使用一次")
print("⚠ 复杂逻辑建议使用列表推导式")
print("⚠ 简单操作性能与列表推导式相近")
print()
print("适用场景：")
print("• 需要对序列中每个元素应用相同函数")
print("• 数据类型转换")
print("• 与其他函数式编程工具结合使用")
print("• 处理大量数据时利用惰性求值")

if __name__ == "__main__":
    print("\n=== Lambda表达式与map函数学习完成 ===")
    print("map函数是函数式编程的重要工具")
    print("与Lambda表达式结合可以简洁地处理序列数据")
    print("下一步：学习Lambda表达式与filter函数的结合使用")