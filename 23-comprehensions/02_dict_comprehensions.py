#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字典推导式 (Dictionary Comprehensions)

学习目标：
1. 理解字典推导式的基本语法
2. 掌握字典推导式的各种用法
3. 学会使用条件表达式创建字典
4. 了解字典推导式在数据处理中的应用

作者：Python学习教程
日期：2024年
"""

def basic_dict_comprehensions():
    """基本字典推导式语法"""
    print("=== 基本字典推导式 ===")
    
    # 基本语法：{key_expression: value_expression for item in iterable}
    # 创建数字和其平方的字典
    squares_dict = {x: x**2 for x in range(1, 6)}
    print(f"数字平方字典: {squares_dict}")
    
    # 传统方法对比
    squares_traditional = {}
    for x in range(1, 6):
        squares_traditional[x] = x**2
    print(f"传统方法结果: {squares_traditional}")
    
    # 字符串长度字典
    words = ['apple', 'banana', 'cherry', 'date']
    word_lengths = {word: len(word) for word in words}
    print(f"单词长度字典: {word_lengths}")
    
    # 字符ASCII码字典
    chars = 'ABCDE'
    ascii_dict = {char: ord(char) for char in chars}
    print(f"字符ASCII码: {ascii_dict}")
    
    print()

def conditional_dict_comprehensions():
    """带条件的字典推导式"""
    print("=== 带条件的字典推导式 ===")
    
    # 语法：{key: value for item in iterable if condition}
    # 筛选偶数平方
    even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
    print(f"偶数平方字典: {even_squares}")
    
    # 筛选长单词
    words = ['cat', 'elephant', 'dog', 'hippopotamus', 'ant', 'butterfly']
    long_words = {word: len(word) for word in words if len(word) > 5}
    print(f"长单词字典: {long_words}")
    
    # 学生成绩筛选
    students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    grades = [85, 92, 78, 96, 88]
    high_achievers = {student: grade for student, grade in zip(students, grades) if grade >= 90}
    print(f"高分学生: {high_achievers}")
    
    # 条件表达式（三元运算符）
    numbers = range(-5, 6)
    sign_dict = {x: 'positive' if x > 0 else 'negative' if x < 0 else 'zero' for x in numbers}
    print(f"数字符号: {sign_dict}")
    
    print()

def dict_from_lists():
    """从列表创建字典"""
    print("=== 从列表创建字典 ===")
    
    # 使用zip组合两个列表
    keys = ['name', 'age', 'city', 'profession']
    values = ['Alice', 28, 'New York', 'Engineer']
    person_dict = {k: v for k, v in zip(keys, values)}
    print(f"个人信息: {person_dict}")
    
    # 使用enumerate创建索引字典
    fruits = ['apple', 'banana', 'cherry', 'date']
    fruit_index = {fruit: index for index, fruit in enumerate(fruits)}
    print(f"水果索引: {fruit_index}")
    
    # 反转字典
    original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    reversed_dict = {v: k for k, v in original_dict.items()}
    print(f"原字典: {original_dict}")
    print(f"反转字典: {reversed_dict}")
    
    # 多个列表组合
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    cities = ['New York', 'London', 'Tokyo']
    people = {name: {'age': age, 'city': city} for name, age, city in zip(names, ages, cities)}
    print(f"人员信息: {people}")
    
    print()

def string_dict_comprehensions():
    """字符串相关的字典推导式"""
    print("=== 字符串处理 ===")
    
    # 字符频率统计
    text = "hello world"
    char_count = {char: text.count(char) for char in set(text) if char != ' '}
    print(f"字符频率: {char_count}")
    
    # 单词首字母字典
    words = ['apple', 'banana', 'cherry', 'apricot', 'blueberry', 'coconut']
    first_letter_groups = {}
    for word in words:
        first_letter = word[0]
        if first_letter not in first_letter_groups:
            first_letter_groups[first_letter] = []
        first_letter_groups[first_letter].append(word)
    
    # 使用字典推导式重写
    from collections import defaultdict
    letter_groups = defaultdict(list)
    for word in words:
        letter_groups[word[0]].append(word)
    letter_dict = {k: v for k, v in letter_groups.items()}
    print(f"首字母分组: {letter_dict}")
    
    # 文件扩展名统计
    filenames = ['doc1.txt', 'image.jpg', 'script.py', 'data.csv', 'doc2.txt', 'photo.jpg']
    extension_count = {}
    for filename in filenames:
        ext = filename.split('.')[-1]
        extension_count[ext] = extension_count.get(ext, 0) + 1
    print(f"扩展名统计: {extension_count}")
    
    # 使用字典推导式统计
    extensions = [filename.split('.')[-1] for filename in filenames]
    ext_count_comp = {ext: extensions.count(ext) for ext in set(extensions)}
    print(f"推导式统计: {ext_count_comp}")
    
    print()

def nested_dict_comprehensions():
    """嵌套字典推导式"""
    print("=== 嵌套字典推导式 ===")
    
    # 创建乘法表字典
    multiplication_dict = {i: {j: i*j for j in range(1, 6)} for i in range(1, 6)}
    print("乘法表字典:")
    for i, row in multiplication_dict.items():
        print(f"{i}: {row}")
    
    # 学生成绩字典
    students = ['Alice', 'Bob', 'Charlie']
    subjects = ['Math', 'Science', 'English']
    import random
    random.seed(42)  # 固定随机种子以获得一致结果
    
    grades = {student: {subject: random.randint(70, 100) for subject in subjects} for student in students}
    print(f"\n学生成绩: {grades}")
    
    # 计算平均分
    averages = {student: sum(scores.values()) / len(scores) for student, scores in grades.items()}
    print(f"平均分: {averages}")
    
    # 矩阵转置
    matrix_dict = {f'row_{i}': {f'col_{j}': i*3 + j + 1 for j in range(3)} for i in range(3)}
    print(f"\n原矩阵: {matrix_dict}")
    
    # 转置矩阵
    transposed = {f'col_{j}': {f'row_{i}': matrix_dict[f'row_{i}'][f'col_{j}'] for i in range(3)} for j in range(3)}
    print(f"转置矩阵: {transposed}")
    
    print()

def advanced_dict_comprehensions():
    """高级字典推导式用法"""
    print("=== 高级用法 ===")
    
    # 使用函数处理
    def categorize_number(n):
        if n % 2 == 0:
            return 'even'
        else:
            return 'odd'
    
    numbers = range(1, 11)
    number_categories = {n: categorize_number(n) for n in numbers}
    print(f"数字分类: {number_categories}")
    
    # 多条件筛选
    products = [
        {'name': 'laptop', 'price': 1000, 'category': 'electronics'},
        {'name': 'book', 'price': 20, 'category': 'education'},
        {'name': 'phone', 'price': 800, 'category': 'electronics'},
        {'name': 'desk', 'price': 300, 'category': 'furniture'}
    ]
    
    expensive_electronics = {
        product['name']: product['price'] 
        for product in products 
        if product['category'] == 'electronics' and product['price'] > 500
    }
    print(f"昂贵电子产品: {expensive_electronics}")
    
    # 字典合并和过滤
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 4, 'c': 5, 'd': 6}
    
    # 合并字典，dict2的值覆盖dict1
    merged = {k: dict2.get(k, dict1.get(k)) for k in set(dict1) | set(dict2)}
    print(f"合并字典: {merged}")
    
    # 筛选共同键
    common_keys = {k: (dict1[k], dict2[k]) for k in dict1 if k in dict2}
    print(f"共同键值: {common_keys}")
    
    print()

def data_transformation():
    """数据转换应用"""
    print("=== 数据转换应用 ===")
    
    # CSV数据转换
    csv_data = [
        ['Name', 'Age', 'City'],
        ['Alice', '25', 'New York'],
        ['Bob', '30', 'London'],
        ['Charlie', '35', 'Tokyo']
    ]
    
    # 转换为字典列表
    headers = csv_data[0]
    data_dicts = [{headers[i]: row[i] for i in range(len(headers))} for row in csv_data[1:]]
    print(f"CSV转字典: {data_dicts}")
    
    # 按城市分组
    city_groups = {}
    for person in data_dicts:
        city = person['City']
        if city not in city_groups:
            city_groups[city] = []
        city_groups[city].append(person['Name'])
    print(f"城市分组: {city_groups}")
    
    # 配置文件处理
    config_lines = [
        'database_host=localhost',
        'database_port=5432',
        'debug_mode=true',
        'max_connections=100'
    ]
    
    config_dict = {line.split('=')[0]: line.split('=')[1] for line in config_lines}
    print(f"配置字典: {config_dict}")
    
    # 类型转换
    def convert_value(value):
        if value.isdigit():
            return int(value)
        elif value.lower() in ['true', 'false']:
            return value.lower() == 'true'
        else:
            return value
    
    typed_config = {k: convert_value(v) for k, v in config_dict.items()}
    print(f"类型转换后: {typed_config}")
    
    print()

def performance_comparison():
    """性能对比"""
    print("=== 性能对比 ===")
    
    import time
    
    # 大数据量测试
    n = 50000
    
    # 字典推导式
    start_time = time.time()
    squares_dict_comp = {x: x**2 for x in range(n)}
    comp_time = time.time() - start_time
    
    # 传统循环
    start_time = time.time()
    squares_dict_loop = {}
    for x in range(n):
        squares_dict_loop[x] = x**2
    loop_time = time.time() - start_time
    
    # dict()构造函数
    start_time = time.time()
    squares_dict_constructor = dict((x, x**2) for x in range(n))
    constructor_time = time.time() - start_time
    
    print(f"创建{n}个键值对的字典:")
    print(f"字典推导式: {comp_time:.4f}秒")
    print(f"传统循环: {loop_time:.4f}秒")
    print(f"dict构造函数: {constructor_time:.4f}秒")
    
    # 验证结果一致性
    print(f"结果一致性: {squares_dict_comp == squares_dict_loop == squares_dict_constructor}")
    
    print()

def common_mistakes():
    """常见错误和注意事项"""
    print("=== 常见错误和注意事项 ===")
    
    # 错误1：键重复
    print("❌ 注意键的唯一性")
    words = ['apple', 'banana', 'apricot', 'blueberry']
    # 这会导致键重复，后面的值会覆盖前面的
    first_letter_dict = {word[0]: word for word in words}
    print(f"首字母字典（有覆盖）: {first_letter_dict}")
    
    # 正确做法：使用列表存储多个值
    from collections import defaultdict
    first_letter_groups = defaultdict(list)
    for word in words:
        first_letter_groups[word[0]].append(word)
    print(f"首字母分组（正确）: {dict(first_letter_groups)}")
    
    # 错误2：在推导式中修改原字典
    print("\n❌ 避免在推导式中修改原字典")
    original_dict = {'a': 1, 'b': 2, 'c': 3}
    # 正确做法：创建新字典
    doubled_dict = {k: v * 2 for k, v in original_dict.items()}
    print(f"原字典: {original_dict}")
    print(f"新字典: {doubled_dict}")
    
    # 注意3：空值处理
    print("\n⚠️ 注意空值和异常处理")
    data = [('a', 1), ('b', None), ('c', 3), ('d', 0)]
    # 过滤空值
    filtered_dict = {k: v for k, v in data if v is not None}
    print(f"过滤空值: {filtered_dict}")
    
    # 处理除零错误
    numbers = [1, 2, 0, 4, 5]
    safe_reciprocals = {n: 1/n if n != 0 else float('inf') for n in numbers}
    print(f"安全倒数: {safe_reciprocals}")
    
    print()

def main():
    """主函数"""
    print("Python 字典推导式学习教程")
    print("=" * 50)
    
    basic_dict_comprehensions()
    conditional_dict_comprehensions()
    dict_from_lists()
    string_dict_comprehensions()
    nested_dict_comprehensions()
    advanced_dict_comprehensions()
    data_transformation()
    performance_comparison()
    common_mistakes()
    
    print("学习要点总结:")
    print("1. 字典推导式语法：{key: value for item in iterable}")
    print("2. 可以添加条件筛选和复杂表达式")
    print("3. 适合数据转换和映射操作")
    print("4. 注意键的唯一性，重复键会被覆盖")
    print("5. 性能优于传统循环，代码更简洁")
    print("6. 复杂逻辑时考虑使用函数或传统方法")

if __name__ == "__main__":
    main()