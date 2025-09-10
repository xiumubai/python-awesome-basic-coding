#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
推导式练习题 (Comprehensions Exercises)

本模块包含各种推导式的练习题，从基础到高级，
帮助学习者巩固和提高推导式的使用技能。

练习分类：
1. 基础练习 - 简单的列表、字典、集合推导式
2. 条件练习 - 带条件的推导式
3. 嵌套练习 - 嵌套循环和复杂结构
4. 实际应用 - 解决实际问题
5. 高级挑战 - 复杂的综合应用

学习建议：
- 先尝试自己解决，再查看答案
- 理解每个解决方案的思路
- 尝试用不同方法解决同一问题
- 注意代码的可读性和性能
"""

import re
import math
import random
from datetime import datetime, timedelta
from collections import Counter, defaultdict
from typing import List, Dict, Set, Tuple, Any

def exercise_basic_list_comprehensions():
    """基础列表推导式练习"""
    print("=== 基础列表推导式练习 ===")
    
    # 练习1：创建1到10的平方列表
    print("练习1：创建1到10的平方列表")
    # 你的答案：
    answer1 = [x**2 for x in range(1, 11)]
    print(f"答案：{answer1}")
    
    # 练习2：从字符串列表中提取长度
    print("\n练习2：从字符串列表中提取长度")
    words = ['apple', 'banana', 'cherry', 'date']
    print(f"输入：{words}")
    # 你的答案：
    answer2 = [len(word) for word in words]
    print(f"答案：{answer2}")
    
    # 练习3：将字符串列表转换为大写
    print("\n练习3：将字符串列表转换为大写")
    names = ['alice', 'bob', 'charlie']
    print(f"输入：{names}")
    # 你的答案：
    answer3 = [name.upper() for name in names]
    print(f"答案：{answer3}")
    
    # 练习4：从嵌套列表中提取第一个元素
    print("\n练习4：从嵌套列表中提取第一个元素")
    nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"输入：{nested}")
    # 你的答案：
    answer4 = [row[0] for row in nested]
    print(f"答案：{answer4}")
    
    # 练习5：创建坐标对列表
    print("\n练习5：创建坐标对列表 (x, y) 其中 x, y 都在 0-2 范围内")
    # 你的答案：
    answer5 = [(x, y) for x in range(3) for y in range(3)]
    print(f"答案：{answer5}")
    
    print()

def exercise_conditional_comprehensions():
    """条件推导式练习"""
    print("=== 条件推导式练习 ===")
    
    # 练习1：筛选偶数
    print("练习1：从1到20中筛选偶数")
    # 你的答案：
    answer1 = [x for x in range(1, 21) if x % 2 == 0]
    print(f"答案：{answer1}")
    
    # 练习2：筛选长单词
    print("\n练习2：筛选长度大于5的单词")
    words = ['python', 'java', 'javascript', 'go', 'rust', 'typescript']
    print(f"输入：{words}")
    # 你的答案：
    answer2 = [word for word in words if len(word) > 5]
    print(f"答案：{answer2}")
    
    # 练习3：条件转换
    print("\n练习3：正数保持不变，负数取绝对值")
    numbers = [-3, -1, 0, 2, 5, -7, 8]
    print(f"输入：{numbers}")
    # 你的答案：
    answer3 = [x if x >= 0 else -x for x in numbers]
    print(f"答案：{answer3}")
    
    # 练习4：复合条件
    print("\n练习4：筛选能被3整除但不能被6整除的数")
    numbers = list(range(1, 31))
    print(f"输入：{numbers[:10]}...")
    # 你的答案：
    answer4 = [x for x in numbers if x % 3 == 0 and x % 6 != 0]
    print(f"答案：{answer4}")
    
    # 练习5：字符串条件处理
    print("\n练习5：提取包含字母'a'的单词，并转换为大写")
    words = ['cat', 'dog', 'elephant', 'bird', 'snake']
    print(f"输入：{words}")
    # 你的答案：
    answer5 = [word.upper() for word in words if 'a' in word]
    print(f"答案：{answer5}")
    
    print()

def exercise_dictionary_comprehensions():
    """字典推导式练习"""
    print("=== 字典推导式练习 ===")
    
    # 练习1：创建数字到平方的映射
    print("练习1：创建1到5的数字到平方的映射")
    # 你的答案：
    answer1 = {x: x**2 for x in range(1, 6)}
    print(f"答案：{answer1}")
    
    # 练习2：从两个列表创建字典
    print("\n练习2：从键列表和值列表创建字典")
    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3, 4]
    print(f"键：{keys}")
    print(f"值：{values}")
    # 你的答案：
    answer2 = {k: v for k, v in zip(keys, values)}
    print(f"答案：{answer2}")
    
    # 练习3：字符串长度字典
    print("\n练习3：创建单词到长度的映射")
    words = ['apple', 'banana', 'cherry']
    print(f"输入：{words}")
    # 你的答案：
    answer3 = {word: len(word) for word in words}
    print(f"答案：{answer3}")
    
    # 练习4：条件字典
    print("\n练习4：只包含偶数的平方字典")
    numbers = range(1, 11)
    print(f"输入：{list(numbers)}")
    # 你的答案：
    answer4 = {x: x**2 for x in numbers if x % 2 == 0}
    print(f"答案：{answer4}")
    
    # 练习5：反转字典
    print("\n练习5：反转字典的键值对")
    original = {'a': 1, 'b': 2, 'c': 3}
    print(f"输入：{original}")
    # 你的答案：
    answer5 = {v: k for k, v in original.items()}
    print(f"答案：{answer5}")
    
    print()

def exercise_set_comprehensions():
    """集合推导式练习"""
    print("=== 集合推导式练习 ===")
    
    # 练习1：创建平方数集合
    print("练习1：创建1到10的平方数集合")
    # 你的答案：
    answer1 = {x**2 for x in range(1, 11)}
    print(f"答案：{answer1}")
    
    # 练习2：去重并转换
    print("\n练习2：从列表中去重并转换为大写")
    words = ['apple', 'banana', 'apple', 'cherry', 'banana']
    print(f"输入：{words}")
    # 你的答案：
    answer2 = {word.upper() for word in words}
    print(f"答案：{answer2}")
    
    # 练习3：字符集合
    print("\n练习3：提取字符串中的所有字符（去重）")
    text = "hello world"
    print(f"输入：'{text}'")
    # 你的答案：
    answer3 = {char for char in text if char != ' '}
    print(f"答案：{answer3}")
    
    # 练习4：数学集合操作
    print("\n练习4：找出1到20中能被2或3整除的数")
    # 你的答案：
    answer4 = {x for x in range(1, 21) if x % 2 == 0 or x % 3 == 0}
    print(f"答案：{answer4}")
    
    # 练习5：嵌套集合
    print("\n练习5：从嵌套列表中提取所有唯一元素")
    nested = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    print(f"输入：{nested}")
    # 你的答案：
    answer5 = {item for sublist in nested for item in sublist}
    print(f"答案：{answer5}")
    
    print()

def exercise_nested_comprehensions():
    """嵌套推导式练习"""
    print("=== 嵌套推导式练习 ===")
    
    # 练习1：创建乘法表
    print("练习1：创建3x3乘法表")
    # 你的答案：
    answer1 = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print(f"答案：{answer1}")
    
    # 练习2：矩阵转置
    print("\n练习2：转置矩阵")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"输入：{matrix}")
    # 你的答案：
    answer2 = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print(f"答案：{answer2}")
    
    # 练习3：扁平化嵌套列表
    print("\n练习3：扁平化嵌套列表")
    nested = [[1, 2], [3, 4, 5], [6]]
    print(f"输入：{nested}")
    # 你的答案：
    answer3 = [item for sublist in nested for item in sublist]
    print(f"答案：{answer3}")
    
    # 练习4：条件嵌套
    print("\n练习4：创建坐标对，但排除对角线")
    # 你的答案：
    answer4 = [(i, j) for i in range(3) for j in range(3) if i != j]
    print(f"答案：{answer4}")
    
    # 练习5：嵌套字典
    print("\n练习5：从学生数据创建成绩字典")
    students = [('Alice', [85, 90, 78]), ('Bob', [92, 88, 84]), ('Charlie', [79, 85, 91])]
    print(f"输入：{students}")
    # 你的答案：
    answer5 = {name: {f'exam_{i+1}': score for i, score in enumerate(scores)} 
              for name, scores in students}
    print(f"答案：{answer5}")
    
    print()

def exercise_real_world_applications():
    """实际应用练习"""
    print("=== 实际应用练习 ===")
    
    # 练习1：数据清洗
    print("练习1：清洗和标准化邮箱地址")
    emails = ['  Alice@GMAIL.com  ', 'bob@yahoo.COM', '  charlie@hotmail.com']
    print(f"输入：{emails}")
    # 你的答案：
    answer1 = [email.strip().lower() for email in emails]
    print(f"答案：{answer1}")
    
    # 练习2：文本分析
    print("\n练习2：统计文本中的单词长度分布")
    text = "Python is a powerful programming language"
    print(f"输入：'{text}'")
    # 你的答案：
    words = text.split()
    answer2 = {len(word): [w for w in words if len(w) == len(word)] for word in words}
    # 去重
    answer2 = {length: list(set(word_list)) for length, word_list in answer2.items()}
    print(f"答案：{answer2}")
    
    # 练习3：数据转换
    print("\n练习3：将温度从华氏度转换为摄氏度")
    fahrenheit_temps = [32, 68, 86, 104, 122]
    print(f"输入（华氏度）：{fahrenheit_temps}")
    # 你的答案：
    answer3 = [round((f - 32) * 5/9, 1) for f in fahrenheit_temps]
    print(f"答案（摄氏度）：{answer3}")
    
    # 练习4：数据过滤和聚合
    print("\n练习4：从销售数据中提取高价值订单")
    orders = [
        {'id': 1, 'amount': 150, 'status': 'completed'},
        {'id': 2, 'amount': 75, 'status': 'pending'},
        {'id': 3, 'amount': 200, 'status': 'completed'},
        {'id': 4, 'amount': 50, 'status': 'cancelled'}
    ]
    print(f"输入：{orders}")
    # 你的答案：
    answer4 = [order['id'] for order in orders 
              if order['amount'] > 100 and order['status'] == 'completed']
    print(f"答案（高价值已完成订单ID）：{answer4}")
    
    # 练习5：日期处理
    print("\n练习5：生成未来7天的日期列表")
    today = datetime.now().date()
    print(f"今天：{today}")
    # 你的答案：
    answer5 = [(today + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(1, 8)]
    print(f"答案：{answer5}")
    
    print()

def exercise_advanced_challenges():
    """高级挑战练习"""
    print("=== 高级挑战练习 ===")
    
    # 练习1：素数筛选
    print("练习1：找出1到50之间的所有素数")
    # 你的答案：
    def is_prime(n):
        if n < 2:
            return False
        return all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    
    answer1 = [n for n in range(1, 51) if is_prime(n)]
    print(f"答案：{answer1}")
    
    # 练习2：单词频率统计
    print("\n练习2：统计文本中每个单词的出现频率")
    text = "the quick brown fox jumps over the lazy dog the fox is quick"
    print(f"输入：'{text}'")
    # 你的答案：
    words = text.split()
    answer2 = {word: words.count(word) for word in set(words)}
    print(f"答案：{answer2}")
    
    # 练习3：数据分组
    print("\n练习3：按年龄组分组学生")
    students = [
        {'name': 'Alice', 'age': 20},
        {'name': 'Bob', 'age': 22},
        {'name': 'Charlie', 'age': 20},
        {'name': 'Diana', 'age': 21},
        {'name': 'Eve', 'age': 22}
    ]
    print(f"输入：{students}")
    # 你的答案：
    age_groups = {}
    for student in students:
        age = student['age']
        if age not in age_groups:
            age_groups[age] = []
        age_groups[age].append(student['name'])
    
    # 使用推导式的版本
    unique_ages = {student['age'] for student in students}
    answer3 = {age: [student['name'] for student in students if student['age'] == age] 
              for age in unique_ages}
    print(f"答案：{answer3}")
    
    # 练习4：复杂数据转换
    print("\n练习4：将嵌套字典转换为扁平结构")
    nested_data = {
        'user1': {'name': 'Alice', 'scores': {'math': 85, 'english': 90}},
        'user2': {'name': 'Bob', 'scores': {'math': 78, 'english': 85}}
    }
    print(f"输入：{nested_data}")
    # 你的答案：
    answer4 = {f"{user_id}_{subject}": score 
              for user_id, user_data in nested_data.items() 
              for subject, score in user_data['scores'].items()}
    print(f"答案：{answer4}")
    
    # 练习5：算法实现
    print("\n练习5：使用推导式实现快速排序的分区")
    numbers = [3, 6, 8, 10, 1, 2, 1]
    pivot = 5
    print(f"输入：{numbers}, 基准值：{pivot}")
    # 你的答案：
    smaller = [x for x in numbers if x < pivot]
    equal = [x for x in numbers if x == pivot]
    larger = [x for x in numbers if x > pivot]
    answer5 = {'smaller': smaller, 'equal': equal, 'larger': larger}
    print(f"答案：{answer5}")
    
    print()

def exercise_performance_optimization():
    """性能优化练习"""
    print("=== 性能优化练习 ===")
    
    # 练习1：优化重复计算
    print("练习1：优化重复的字符串长度计算")
    words = ['python', 'java', 'javascript', 'go'] * 1000
    
    # 低效版本（重复计算）
    def inefficient_version():
        return [word.upper() for word in words if len(word) > len(word.lower())]
    
    # 高效版本
    def efficient_version():
        return [word.upper() for word in words if len(word) > 3]  # 简化条件
    
    print("提示：避免在条件中重复计算相同的值")
    
    # 练习2：选择合适的数据结构
    print("\n练习2：优化查找操作")
    valid_ids = list(range(1000, 2000))
    test_ids = [500, 1500, 2500, 1200, 800]
    
    # 低效版本（列表查找）
    def list_lookup():
        return [id for id in test_ids if id in valid_ids]
    
    # 高效版本（集合查找）
    def set_lookup():
        valid_set = set(valid_ids)
        return [id for id in test_ids if id in valid_set]
    
    print("提示：使用集合进行查找操作比列表快得多")
    
    # 练习3：生成器 vs 列表
    print("\n练习3：选择合适的数据生成方式")
    
    # 内存密集型（列表）
    def memory_intensive():
        return [x**2 for x in range(1000000)]
    
    # 内存友好型（生成器）
    def memory_friendly():
        return (x**2 for x in range(1000000))
    
    print("提示：当只需要迭代一次时，使用生成器表达式")
    
    print()

def exercise_error_handling():
    """错误处理练习"""
    print("=== 错误处理练习 ===")
    
    # 练习1：安全的类型转换
    print("练习1：安全地将字符串列表转换为整数")
    string_numbers = ['1', '2', 'abc', '4', '', '6']
    print(f"输入：{string_numbers}")
    
    # 你的答案：
    def safe_int(s):
        try:
            return int(s)
        except ValueError:
            return 0
    
    answer1 = [safe_int(s) for s in string_numbers]
    print(f"答案：{answer1}")
    
    # 练习2：处理嵌套数据的缺失值
    print("\n练习2：安全地访问嵌套字典")
    data = [
        {'name': 'Alice', 'details': {'age': 25}},
        {'name': 'Bob'},  # 缺少details
        {'name': 'Charlie', 'details': {'age': 30}}
    ]
    print(f"输入：{data}")
    
    # 你的答案：
    answer2 = [person.get('details', {}).get('age', 'Unknown') for person in data]
    print(f"答案：{answer2}")
    
    # 练习3：过滤有效数据
    print("\n练习3：过滤掉无效的邮箱地址")
    emails = ['alice@gmail.com', 'invalid-email', 'bob@yahoo.com', '', 'charlie@']
    print(f"输入：{emails}")
    
    # 你的答案：
    def is_valid_email(email):
        return '@' in email and '.' in email.split('@')[-1] and len(email) > 5
    
    answer3 = [email for email in emails if is_valid_email(email)]
    print(f"答案：{answer3}")
    
    print()

def comprehensive_challenge():
    """综合挑战"""
    print("=== 综合挑战：数据分析项目 ===")
    
    # 模拟销售数据
    sales_data = [
        {'date': '2024-01-01', 'product': 'laptop', 'category': 'electronics', 'price': 1200, 'quantity': 2},
        {'date': '2024-01-02', 'product': 'mouse', 'category': 'electronics', 'price': 25, 'quantity': 5},
        {'date': '2024-01-02', 'product': 'book', 'category': 'education', 'price': 15, 'quantity': 3},
        {'date': '2024-01-03', 'product': 'laptop', 'category': 'electronics', 'price': 1200, 'quantity': 1},
        {'date': '2024-01-03', 'product': 'pen', 'category': 'office', 'price': 2, 'quantity': 10},
        {'date': '2024-01-04', 'product': 'book', 'category': 'education', 'price': 15, 'quantity': 2},
    ]
    
    print("销售数据分析挑战：")
    print(f"数据样本：{sales_data[:2]}...")
    
    # 挑战1：计算每个产品的总收入
    print("\n挑战1：计算每个产品的总收入")
    products = {item['product'] for item in sales_data}
    product_revenue = {product: sum(item['price'] * item['quantity'] 
                                  for item in sales_data 
                                  if item['product'] == product) 
                      for product in products}
    print(f"答案：{product_revenue}")
    
    # 挑战2：找出高价值交易（总价值>100）
    print("\n挑战2：找出高价值交易（总价值>100）")
    high_value_transactions = [{
        'product': item['product'],
        'total_value': item['price'] * item['quantity']
    } for item in sales_data if item['price'] * item['quantity'] > 100]
    print(f"答案：{high_value_transactions}")
    
    # 挑战3：按类别统计销售数量
    print("\n挑战3：按类别统计销售数量")
    categories = {item['category'] for item in sales_data}
    category_quantities = {category: sum(item['quantity'] 
                                       for item in sales_data 
                                       if item['category'] == category) 
                          for category in categories}
    print(f"答案：{category_quantities}")
    
    # 挑战4：创建日期到收入的映射
    print("\n挑战4：创建日期到收入的映射")
    dates = {item['date'] for item in sales_data}
    daily_revenue = {date: sum(item['price'] * item['quantity'] 
                             for item in sales_data 
                             if item['date'] == date) 
                    for date in dates}
    print(f"答案：{daily_revenue}")
    
    # 挑战5：找出最畅销的产品（按数量）
    print("\n挑战5：找出最畅销的产品（按数量）")
    product_quantities = {product: sum(item['quantity'] 
                                     for item in sales_data 
                                     if item['product'] == product) 
                         for product in products}
    best_selling = max(product_quantities.items(), key=lambda x: x[1])
    print(f"答案：{best_selling[0]} (数量: {best_selling[1]})")
    
    print()

def main():
    """主函数"""
    print("Python 推导式练习题集")
    print("=" * 60)
    
    # 运行所有练习
    exercise_basic_list_comprehensions()
    exercise_conditional_comprehensions()
    exercise_dictionary_comprehensions()
    exercise_set_comprehensions()
    exercise_nested_comprehensions()
    exercise_real_world_applications()
    exercise_advanced_challenges()
    exercise_performance_optimization()
    exercise_error_handling()
    comprehensive_challenge()
    
    print("=" * 60)
    print("练习总结和学习建议")
    print("=" * 60)
    
    print("\n🎯 学习要点回顾：")
    print("1. 列表推导式：[expr for item in iterable if condition]")
    print("2. 字典推导式：{key: value for item in iterable if condition}")
    print("3. 集合推导式：{expr for item in iterable if condition}")
    print("4. 生成器表达式：(expr for item in iterable if condition)")
    
    print("\n💡 最佳实践：")
    print("1. 保持推导式简洁易读")
    print("2. 复杂逻辑使用传统循环")
    print("3. 注意性能和内存使用")
    print("4. 合理处理异常情况")
    print("5. 选择合适的数据结构")
    
    print("\n🚀 进阶建议：")
    print("1. 尝试用不同方法解决同一问题")
    print("2. 比较推导式与传统方法的性能")
    print("3. 在实际项目中应用所学知识")
    print("4. 关注代码的可读性和维护性")
    print("5. 持续练习和总结经验")
    
    print("\n✨ 恭喜完成所有练习！继续加油！")

if __name__ == "__main__":
    main()