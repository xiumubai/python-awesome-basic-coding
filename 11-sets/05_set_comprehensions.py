#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
集合推导式详解

本文件详细演示了Python集合推导式的使用：
1. 基础集合推导式语法
2. 带条件的集合推导式
3. 嵌套集合推导式
4. 集合推导式与其他推导式的对比
5. 集合推导式的性能优势
6. 实际应用场景
7. 高级技巧和最佳实践

作者：Python学习教程
日期：2024年
"""

import time
import string
import random
from collections import Counter

def main():
    print("=" * 50)
    print("集合推导式详解")
    print("=" * 50)
    
    # 1. 基础集合推导式语法
    print("\n1. 基础集合推导式语法")
    print("-" * 30)
    
    # 基本语法：{expression for item in iterable}
    numbers = [1, 2, 3, 4, 5, 1, 2, 3]  # 包含重复元素的列表
    print(f"原始列表: {numbers}")
    
    # 使用集合推导式创建平方数集合
    squares = {x**2 for x in numbers}
    print(f"平方数集合: {squares}")
    
    # 对比传统方法
    traditional_squares = set()
    for x in numbers:
        traditional_squares.add(x**2)
    print(f"传统方法结果: {traditional_squares}")
    print(f"结果相同: {squares == traditional_squares}")
    
    # 字符串处理
    text = "Hello World"
    print(f"\n原始字符串: '{text}'")
    
    # 获取所有字符（去重）
    chars = {char for char in text}
    print(f"所有字符: {chars}")
    
    # 获取所有字母（去重，转小写）
    letters = {char.lower() for char in text if char.isalpha()}
    print(f"所有字母: {letters}")
    
    # 2. 带条件的集合推导式
    print("\n2. 带条件的集合推导式")
    print("-" * 30)
    
    # 语法：{expression for item in iterable if condition}
    numbers = range(1, 21)
    print(f"数字范围: {list(numbers)}")
    
    # 偶数集合
    evens = {x for x in numbers if x % 2 == 0}
    print(f"偶数集合: {evens}")
    
    # 能被3整除的数的平方
    divisible_by_3_squares = {x**2 for x in numbers if x % 3 == 0}
    print(f"能被3整除的数的平方: {divisible_by_3_squares}")
    
    # 多个条件
    special_numbers = {x for x in numbers if x % 2 == 0 and x > 10}
    print(f"大于10的偶数: {special_numbers}")
    
    # 字符串条件过滤
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
    print(f"\n单词列表: {words}")
    
    # 长度大于4的单词的首字母
    long_word_initials = {word[0].upper() for word in words if len(word) > 4}
    print(f"长单词首字母: {long_word_initials}")
    
    # 包含特定字母的单词
    words_with_a = {word for word in words if 'a' in word}
    print(f"包含字母'a'的单词: {words_with_a}")
    
    # 3. 嵌套集合推导式
    print("\n3. 嵌套集合推导式")
    print("-" * 30)
    
    # 二维数据处理
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"矩阵: {matrix}")
    
    # 提取所有元素到集合
    all_elements = {element for row in matrix for element in row}
    print(f"所有元素: {all_elements}")
    
    # 提取偶数元素
    even_elements = {element for row in matrix for element in row if element % 2 == 0}
    print(f"偶数元素: {even_elements}")
    
    # 字典嵌套处理
    students = {
        "class1": ["Alice", "Bob", "Charlie"],
        "class2": ["David", "Eve", "Frank"],
        "class3": ["Grace", "Henry", "Alice"]  # Alice在多个班级
    }
    print(f"\n学生分布: {students}")
    
    # 获取所有学生姓名（去重）
    all_students = {student for class_students in students.values() for student in class_students}
    print(f"所有学生: {all_students}")
    
    # 获取姓名长度大于4的学生
    long_name_students = {student for class_students in students.values() 
                         for student in class_students if len(student) > 4}
    print(f"长姓名学生: {long_name_students}")
    
    # 4. 集合推导式与其他推导式的对比
    print("\n4. 推导式对比")
    print("-" * 30)
    
    data = [1, 2, 3, 2, 4, 3, 5, 1, 4]
    print(f"原始数据: {data}")
    
    # 列表推导式（保留重复）
    list_comp = [x**2 for x in data]
    print(f"列表推导式: {list_comp}")
    
    # 集合推导式（自动去重）
    set_comp = {x**2 for x in data}
    print(f"集合推导式: {set_comp}")
    
    # 字典推导式
    dict_comp = {x: x**2 for x in data}
    print(f"字典推导式: {dict_comp}")
    
    # 生成器表达式转集合
    gen_to_set = set(x**2 for x in data)
    print(f"生成器转集合: {gen_to_set}")
    print(f"集合推导式与生成器转集合结果相同: {set_comp == gen_to_set}")
    
    print("\n=" * 50)
    print("集合推导式基础演示完成！")
    print("=" * 50)

def demonstrate_advanced_comprehensions():
    """
    演示高级集合推导式
    """
    print("\n高级集合推导式演示")
    print("-" * 30)
    
    # 1. 复杂表达式
    print("1. 复杂表达式:")
    
    # 数学函数组合
    import math
    numbers = range(1, 11)
    
    # 复杂数学运算
    complex_math = {round(math.sqrt(x) * math.log(x), 2) for x in numbers if x > 1}
    print(f"复杂数学运算结果: {complex_math}")
    
    # 字符串处理组合
    sentences = ["Hello world", "Python is great", "Set comprehensions rock"]
    
    # 提取所有单词的长度（去重）
    word_lengths = {len(word) for sentence in sentences for word in sentence.split()}
    print(f"单词长度集合: {word_lengths}")
    
    # 提取首字母组合
    initials = {''.join(word[0].upper() for word in sentence.split()) 
               for sentence in sentences}
    print(f"首字母组合: {initials}")
    
    # 2. 条件表达式（三元运算符）
    print("\n2. 条件表达式:")
    
    numbers = range(-5, 6)
    
    # 使用条件表达式
    processed = {x if x >= 0 else -x for x in numbers}
    print(f"绝对值集合: {processed}")
    
    # 复杂条件表达式
    categorized = {f"{x}:{'positive' if x > 0 else 'negative' if x < 0 else 'zero'}" 
                  for x in numbers}
    print(f"分类结果: {categorized}")
    
    # 3. 函数调用
    print("\n3. 函数调用:")
    
    def process_number(n):
        return n**2 if n % 2 == 0 else n**3
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    numbers = range(1, 21)
    
    # 调用自定义函数
    processed_numbers = {process_number(n) for n in numbers}
    print(f"处理后的数字: {processed_numbers}")
    
    # 素数集合
    primes = {n for n in numbers if is_prime(n)}
    print(f"素数集合: {primes}")
    
    # 4. 多层嵌套
    print("\n4. 多层嵌套:")
    
    # 三维数据结构
    data_3d = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]
    
    # 提取所有元素
    all_3d_elements = {element for layer in data_3d 
                      for row in layer 
                      for element in row}
    print(f"三维数据所有元素: {all_3d_elements}")
    
    # 复杂嵌套字典
    company_data = {
        "departments": {
            "IT": {"employees": ["Alice", "Bob"], "budget": 100000},
            "HR": {"employees": ["Charlie", "David"], "budget": 80000},
            "Finance": {"employees": ["Eve", "Frank"], "budget": 120000}
        }
    }
    
    # 提取所有员工姓名
    all_employees = {employee 
                    for dept_info in company_data["departments"].values() 
                    for employee in dept_info["employees"]}
    print(f"所有员工: {all_employees}")
    
    # 提取高预算部门的员工
    high_budget_employees = {employee 
                           for dept_info in company_data["departments"].values() 
                           for employee in dept_info["employees"]
                           if dept_info["budget"] > 90000}
    print(f"高预算部门员工: {high_budget_employees}")

def demonstrate_performance_benefits():
    """
    演示性能优势
    """
    print("\n性能优势演示")
    print("-" * 30)
    
    # 创建测试数据
    large_data = list(range(100000)) * 2  # 包含重复元素
    
    print(f"测试数据大小: {len(large_data)}")
    print(f"唯一元素数量: {len(set(large_data))}")
    
    # 方法1：传统循环
    def traditional_method(data):
        result = set()
        for x in data:
            if x % 2 == 0:
                result.add(x**2)
        return result
    
    # 方法2：集合推导式
    def comprehension_method(data):
        return {x**2 for x in data if x % 2 == 0}
    
    # 方法3：filter + map + set
    def functional_method(data):
        return set(map(lambda x: x**2, filter(lambda x: x % 2 == 0, data)))
    
    # 性能测试
    methods = [
        ("传统循环", traditional_method),
        ("集合推导式", comprehension_method),
        ("函数式方法", functional_method)
    ]
    
    results = {}
    for name, method in methods:
        start_time = time.time()
        result = method(large_data)
        end_time = time.time()
        
        results[name] = {
            'time': end_time - start_time,
            'size': len(result)
        }
        
        print(f"{name}: {results[name]['time']:.4f}秒, 结果大小: {results[name]['size']}")
    
    # 找出最快的方法
    fastest = min(results.items(), key=lambda x: x[1]['time'])
    print(f"\n最快方法: {fastest[0]} ({fastest[1]['time']:.4f}秒)")

def demonstrate_real_world_applications():
    """
    实际应用场景演示
    """
    print("\n实际应用场景")
    print("-" * 30)
    
    # 1. 数据清洗
    print("1. 数据清洗:")
    
    # 模拟脏数据
    dirty_data = [
        "  Alice  ", "bob", "CHARLIE", "alice", "  Bob  ", 
        "David", "", "   ", "eve", "DAVID", "Eve"
    ]
    
    print(f"脏数据: {dirty_data}")
    
    # 清洗数据：去空格、统一大小写、去重
    clean_names = {name.strip().title() for name in dirty_data 
                  if name.strip()}
    print(f"清洗后: {clean_names}")
    
    # 2. 文本分析
    print("\n2. 文本分析:")
    
    text = """
    Python is a powerful programming language. 
    It is easy to learn and easy to use. 
    Python is great for data science and web development.
    """
    
    print(f"原文本: {text.strip()}")
    
    # 提取所有单词（去重、小写、去标点）
    words = {word.lower().strip(string.punctuation) 
            for word in text.split() 
            if word.strip(string.punctuation)}
    print(f"唯一单词: {words}")
    
    # 提取长单词
    long_words = {word for word in words if len(word) > 4}
    print(f"长单词: {long_words}")
    
    # 提取首字母
    initials = {word[0] for word in words}
    print(f"首字母: {initials}")
    
    # 3. 数据验证
    print("\n3. 数据验证:")
    
    # 模拟用户输入数据
    user_inputs = [
        "alice@email.com", "bob@invalid", "charlie@test.com", 
        "invalid-email", "david@company.org", "eve@email.com"
    ]
    
    print(f"用户输入: {user_inputs}")
    
    # 简单邮箱验证（包含@和.）
    valid_emails = {email.lower() for email in user_inputs 
                   if '@' in email and '.' in email.split('@')[-1]}
    print(f"有效邮箱: {valid_emails}")
    
    # 提取域名
    domains = {email.split('@')[1] for email in valid_emails}
    print(f"域名: {domains}")
    
    # 4. 配置管理
    print("\n4. 配置管理:")
    
    # 模拟多环境配置
    configs = {
        "development": ["debug", "local_db", "test_mode"],
        "staging": ["debug", "remote_db", "test_mode", "ssl"],
        "production": ["remote_db", "ssl", "monitoring", "backup"]
    }
    
    print("环境配置:")
    for env, features in configs.items():
        print(f"  {env}: {features}")
    
    # 找出所有可用功能
    all_features = {feature for features in configs.values() for feature in features}
    print(f"所有功能: {all_features}")
    
    # 找出生产环境独有功能
    prod_only = {feature for feature in configs["production"] 
                if not any(feature in configs[env] for env in ["development", "staging"])}
    print(f"生产环境独有: {prod_only}")
    
    # 找出所有环境共有功能
    common_features = set(configs["development"])
    for features in configs.values():
        common_features &= set(features)
    print(f"共有功能: {common_features}")

def demonstrate_advanced_techniques():
    """
    高级技巧演示
    """
    print("\n高级技巧")
    print("-" * 30)
    
    # 1. 动态属性访问
    print("1. 动态属性访问:")
    
    class Person:
        def __init__(self, name, age, city):
            self.name = name
            self.age = age
            self.city = city
    
    people = [
        Person("Alice", 25, "New York"),
        Person("Bob", 30, "London"),
        Person("Charlie", 25, "Paris"),
        Person("David", 35, "New York")
    ]
    
    # 提取所有年龄
    ages = {person.age for person in people}
    print(f"所有年龄: {ages}")
    
    # 提取所有城市
    cities = {person.city for person in people}
    print(f"所有城市: {cities}")
    
    # 动态属性访问
    attributes = ['name', 'age', 'city']
    for attr in attributes:
        values = {getattr(person, attr) for person in people}
        print(f"所有{attr}: {values}")
    
    # 2. 条件链
    print("\n2. 条件链:")
    
    numbers = range(1, 101)
    
    # 复杂条件组合
    special_numbers = {n for n in numbers 
                      if n % 3 == 0 or n % 5 == 0  # 能被3或5整除
                      if n % 15 != 0  # 但不能被15整除
                      if n > 10}  # 且大于10
    
    print(f"特殊数字: {sorted(special_numbers)}")
    
    # 3. 集合运算组合
    print("\n3. 集合运算组合:")
    
    # 创建多个基础集合
    evens = {x for x in range(1, 21) if x % 2 == 0}
    multiples_of_3 = {x for x in range(1, 21) if x % 3 == 0}
    primes = {2, 3, 5, 7, 11, 13, 17, 19}
    
    print(f"偶数: {evens}")
    print(f"3的倍数: {multiples_of_3}")
    print(f"素数: {primes}")
    
    # 复杂集合运算
    complex_result = {x for x in (evens | multiples_of_3) - primes if x > 5}
    print(f"复杂运算结果: {complex_result}")
    
    # 4. 嵌套推导式优化
    print("\n4. 嵌套推导式优化:")
    
    # 低效的嵌套
    matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
    print(f"矩阵: {matrix}")
    
    # 低效方法：多次遍历
    def inefficient_method(matrix):
        result = set()
        for row in matrix:
            for element in row:
                if element % 2 == 0:
                    result.add(element**2)
        return result
    
    # 高效方法：单次推导
    def efficient_method(matrix):
        return {element**2 for row in matrix for element in row if element % 2 == 0}
    
    result1 = inefficient_method(matrix)
    result2 = efficient_method(matrix)
    
    print(f"低效方法结果: {result1}")
    print(f"高效方法结果: {result2}")
    print(f"结果相同: {result1 == result2}")

def best_practices_and_pitfalls():
    """
    最佳实践和常见陷阱
    """
    print("\n最佳实践和常见陷阱")
    print("-" * 30)
    
    print("最佳实践:")
    print("1. 保持推导式简洁，复杂逻辑使用函数")
    print("2. 优先使用集合推导式而不是set(列表推导式)")
    print("3. 合理使用条件过滤，避免过度嵌套")
    print("4. 注意集合的无序性和唯一性特点")
    
    print("\n常见陷阱演示:")
    
    # 陷阱1：过度复杂的推导式
    print("\n陷阱1 - 过度复杂的推导式:")
    
    # 不好的例子
    bad_example = {f"{x}:{y}" for x in range(1, 6) for y in range(1, 6) 
                  if x != y and x % 2 == 0 and y % 2 == 1 and x + y > 5}
    print(f"复杂推导式结果: {bad_example}")
    
    # 更好的方法
    def is_valid_pair(x, y):
        return x != y and x % 2 == 0 and y % 2 == 1 and x + y > 5
    
    good_example = {f"{x}:{y}" for x in range(1, 6) for y in range(1, 6) 
                   if is_valid_pair(x, y)}
    print(f"优化后结果: {good_example}")
    
    # 陷阱2：忽略集合的无序性
    print("\n陷阱2 - 忽略集合的无序性:")
    
    # 集合是无序的
    numbers = {3, 1, 4, 1, 5, 9, 2, 6}
    print(f"集合: {numbers} (顺序可能不同)")
    
    # 如果需要有序，使用sorted()
    ordered = sorted(numbers)
    print(f"有序列表: {ordered}")
    
    # 陷阱3：可变对象作为集合元素
    print("\n陷阱3 - 可变对象作为集合元素:")
    
    try:
        # 这会报错，因为列表是可变的
        invalid_set = {[1, 2], [3, 4]}
    except TypeError as e:
        print(f"错误: {e}")
    
    # 正确的方法：使用元组
    valid_set = {(1, 2), (3, 4)}
    print(f"正确的集合: {valid_set}")
    
    # 陷阱4：性能误区
    print("\n陷阱4 - 性能误区:")
    
    data = list(range(10000))
    
    # 低效：先列表推导再转集合
    start_time = time.time()
    result1 = set([x**2 for x in data if x % 2 == 0])
    time1 = time.time() - start_time
    
    # 高效：直接集合推导
    start_time = time.time()
    result2 = {x**2 for x in data if x % 2 == 0}
    time2 = time.time() - start_time
    
    print(f"列表推导+转换: {time1:.6f}秒")
    print(f"集合推导: {time2:.6f}秒")
    print(f"性能提升: {time1/time2:.2f}倍")

def practice_exercises():
    """
    练习题
    """
    print("\n练习题")
    print("-" * 20)
    
    # 练习1：文件扩展名统计
    def exercise_1():
        print("1. 文件扩展名统计:")
        
        files = [
            "document.pdf", "image.jpg", "script.py", "data.csv",
            "photo.jpg", "report.pdf", "code.py", "backup.zip",
            "music.mp3", "video.mp4", "text.txt"
        ]
        
        print(f"文件列表: {files}")
        
        # 提取所有扩展名
        extensions = {file.split('.')[-1] for file in files if '.' in file}
        print(f"所有扩展名: {extensions}")
        
        # 提取图片文件扩展名
        image_extensions = {file.split('.')[-1] for file in files 
                          if file.split('.')[-1] in ['jpg', 'png', 'gif', 'bmp']}
        print(f"图片扩展名: {image_extensions}")
    
    # 练习2：数据去重和转换
    def exercise_2():
        print("\n2. 数据去重和转换:")
        
        # 混合数据类型
        mixed_data = [1, "2", 3.0, "4", 5, "6.0", 7, "8", 9.0, "10"]
        print(f"混合数据: {mixed_data}")
        
        # 转换为数字并去重
        try:
            numbers = {float(item) for item in mixed_data}
            print(f"转换后的数字: {numbers}")
            
            # 只保留整数
            integers = {int(num) for num in numbers if num == int(num)}
            print(f"整数集合: {integers}")
        except ValueError as e:
            print(f"转换错误: {e}")
    
    # 练习3：复杂条件过滤
    def exercise_3():
        print("\n3. 复杂条件过滤:")
        
        # 学生成绩数据
        students = [
            {"name": "Alice", "math": 85, "english": 92, "science": 78},
            {"name": "Bob", "math": 92, "english": 85, "science": 90},
            {"name": "Charlie", "math": 78, "english": 88, "science": 85},
            {"name": "David", "math": 95, "english": 90, "science": 92},
            {"name": "Eve", "math": 88, "english": 95, "science": 89}
        ]
        
        print("学生成绩:")
        for student in students:
            print(f"  {student}")
        
        # 找出所有科目都超过85分的学生
        excellent_students = {student["name"] for student in students 
                            if all(score > 85 for score in [student["math"], student["english"], student["science"]])}
        print(f"优秀学生: {excellent_students}")
        
        # 找出平均分超过88的学生
        high_average_students = {student["name"] for student in students 
                               if (student["math"] + student["english"] + student["science"]) / 3 > 88}
        print(f"高平均分学生: {high_average_students}")
        
        # 找出数学成绩最高的分数
        max_math_scores = {student["math"] for student in students 
                          if student["math"] == max(s["math"] for s in students)}
        print(f"最高数学成绩: {max_math_scores}")
    
    exercise_1()
    exercise_2()
    exercise_3()

if __name__ == "__main__":
    main()
    demonstrate_advanced_comprehensions()
    demonstrate_performance_benefits()
    demonstrate_real_world_applications()
    demonstrate_advanced_techniques()
    best_practices_and_pitfalls()
    practice_exercises()