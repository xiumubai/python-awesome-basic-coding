#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
列表推导式 - 高效创建和处理列表的方法

本文件演示了Python中列表推导式的各种用法：
1. 基本列表推导式语法
2. 带条件的列表推导式
3. 嵌套列表推导式
4. 多重条件和复杂表达式
5. 列表推导式与传统方法的比较
6. 实际应用场景和最佳实践

作者：Python学习教程
日期：2024年
"""

def demonstrate_basic_comprehensions():
    """演示基本列表推导式"""
    print("=== 基本列表推导式 ===")
    
    # 基本语法：[expression for item in iterable]
    
    # 1. 创建数字列表
    numbers = [x for x in range(10)]
    print(f"基本数字列表: {numbers}")
    
    # 2. 数学运算
    squares = [x**2 for x in range(1, 6)]
    print(f"平方数列表: {squares}")
    
    # 3. 字符串操作
    words = ['hello', 'world', 'python', 'programming']
    upper_words = [word.upper() for word in words]
    print(f"原单词: {words}")
    print(f"大写单词: {upper_words}")
    
    # 4. 字符串长度
    word_lengths = [len(word) for word in words]
    print(f"单词长度: {word_lengths}")
    
    # 5. 类型转换
    str_numbers = ['1', '2', '3', '4', '5']
    int_numbers = [int(x) for x in str_numbers]
    print(f"字符串数字: {str_numbers}")
    print(f"整数: {int_numbers}")
    
    # 6. 从其他数据结构创建列表
    tuple_data = (1, 2, 3, 4, 5)
    list_from_tuple = [x * 2 for x in tuple_data]
    print(f"元组数据: {tuple_data}")
    print(f"从元组创建的列表: {list_from_tuple}")

def demonstrate_conditional_comprehensions():
    """演示带条件的列表推导式"""
    print("\n=== 带条件的列表推导式 ===")
    
    # 语法：[expression for item in iterable if condition]
    
    numbers = list(range(1, 21))
    print(f"原数字列表: {numbers}")
    
    # 1. 过滤偶数
    even_numbers = [x for x in numbers if x % 2 == 0]
    print(f"偶数: {even_numbers}")
    
    # 2. 过滤奇数并平方
    odd_squares = [x**2 for x in numbers if x % 2 == 1]
    print(f"奇数的平方: {odd_squares}")
    
    # 3. 字符串过滤
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    long_words = [word for word in words if len(word) > 5]
    print(f"原单词: {words}")
    print(f"长单词(>5字符): {long_words}")
    
    # 4. 多重条件
    divisible_by_3_and_5 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
    print(f"1-100中能被3和5整除的数: {divisible_by_3_and_5}")
    
    # 5. 字符串条件过滤
    names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    names_with_a = [name for name in names if 'a' in name.lower()]
    print(f"原姓名: {names}")
    print(f"包含字母'a'的姓名: {names_with_a}")
    
    # 6. 复杂条件
    students = [
        {'name': 'Alice', 'age': 20, 'grade': 85},
        {'name': 'Bob', 'age': 22, 'grade': 92},
        {'name': 'Charlie', 'age': 19, 'grade': 78},
        {'name': 'Diana', 'age': 21, 'grade': 96}
    ]
    
    excellent_students = [student['name'] for student in students 
                         if student['grade'] >= 90 and student['age'] >= 20]
    print(f"优秀学生(成绩>=90且年龄>=20): {excellent_students}")

def demonstrate_conditional_expressions():
    """演示条件表达式在列表推导式中的使用"""
    print("\n=== 条件表达式列表推导式 ===")
    
    # 语法：[expression_if_true if condition else expression_if_false for item in iterable]
    
    numbers = list(range(1, 11))
    print(f"原数字: {numbers}")
    
    # 1. 简单条件表达式
    even_odd_labels = ['偶数' if x % 2 == 0 else '奇数' for x in numbers]
    print(f"奇偶标签: {even_odd_labels}")
    
    # 2. 数值处理
    processed_numbers = [x if x % 2 == 0 else x * 2 for x in numbers]
    print(f"处理后的数字(偶数不变，奇数翻倍): {processed_numbers}")
    
    # 3. 字符串处理
    words = ['python', 'java', 'javascript', 'go', 'rust']
    formatted_words = [word.upper() if len(word) <= 4 else word.title() 
                      for word in words]
    print(f"原单词: {words}")
    print(f"格式化单词(短词大写，长词标题格式): {formatted_words}")
    
    # 4. 复杂条件表达式
    scores = [85, 92, 78, 96, 88, 73, 91]
    grades = ['A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' 
             for score in scores]
    print(f"分数: {scores}")
    print(f"等级: {grades}")
    
    # 5. 结合过滤条件
    positive_negative = [x if x > 0 else abs(x) for x in [-3, -1, 0, 2, 5, -7] if x != 0]
    print(f"非零数字的绝对值处理: {positive_negative}")

def demonstrate_nested_comprehensions():
    """演示嵌套列表推导式"""
    print("\n=== 嵌套列表推导式 ===")
    
    # 1. 创建二维列表
    matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print("乘法表矩阵:")
    for row in matrix:
        print(f"  {row}")
    
    # 2. 扁平化二维列表
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [item for sublist in nested_list for item in sublist]
    print(f"\n原嵌套列表: {nested_list}")
    print(f"扁平化结果: {flattened}")
    
    # 3. 带条件的嵌套推导式
    even_from_nested = [item for sublist in nested_list for item in sublist if item % 2 == 0]
    print(f"嵌套列表中的偶数: {even_from_nested}")
    
    # 4. 复杂嵌套结构
    words_matrix = [['hello', 'world'], ['python', 'programming'], ['list', 'comprehension']]
    upper_chars = [[char.upper() for char in word] for row in words_matrix for word in row]
    print(f"\n单词矩阵: {words_matrix}")
    print(f"大写字符列表: {upper_chars}")
    
    # 5. 三维列表推导式
    cube = [[[i+j+k for k in range(2)] for j in range(2)] for i in range(2)]
    print(f"\n三维立方体:")
    for i, plane in enumerate(cube):
        print(f"  平面{i}: {plane}")
    
    # 6. 实际应用：处理表格数据
    table_data = [
        ['Name', 'Age', 'City'],
        ['Alice', '25', 'New York'],
        ['Bob', '30', 'London'],
        ['Charlie', '35', 'Tokyo']
    ]
    
    # 提取除标题外的所有数据
    data_rows = [row for row in table_data[1:]]
    print(f"\n表格数据: {table_data}")
    print(f"数据行: {data_rows}")
    
    # 提取特定列（年龄）
    ages = [int(row[1]) for row in table_data[1:]]
    print(f"年龄列: {ages}")

def demonstrate_advanced_comprehensions():
    """演示高级列表推导式技巧"""
    print("\n=== 高级列表推导式技巧 ===")
    
    # 1. 使用enumerate
    words = ['apple', 'banana', 'cherry']
    indexed_words = [f"{i}: {word}" for i, word in enumerate(words)]
    print(f"带索引的单词: {indexed_words}")
    
    # 2. 使用zip
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    name_age_pairs = [f"{name}({age})" for name, age in zip(names, ages)]
    print(f"姓名年龄对: {name_age_pairs}")
    
    # 3. 字符串方法链
    sentences = ['  hello world  ', '  PYTHON programming  ', '  List Comprehension  ']
    cleaned = [sentence.strip().title() for sentence in sentences]
    print(f"原句子: {sentences}")
    print(f"清理后: {cleaned}")
    
    # 4. 使用函数
    def is_prime(n):
        """判断是否为质数"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = [x for x in range(2, 50) if is_prime(x)]
    print(f"\n2-50之间的质数: {primes}")
    
    # 5. 复杂数据结构处理
    products = [
        {'name': 'Laptop', 'price': 1000, 'category': 'Electronics'},
        {'name': 'Book', 'price': 20, 'category': 'Education'},
        {'name': 'Phone', 'price': 800, 'category': 'Electronics'},
        {'name': 'Desk', 'price': 300, 'category': 'Furniture'}
    ]
    
    # 提取电子产品名称
    electronics = [product['name'] for product in products 
                  if product['category'] == 'Electronics']
    print(f"电子产品: {electronics}")
    
    # 计算折扣价格
    discounted_prices = [{'name': p['name'], 'discounted_price': p['price'] * 0.9} 
                        for p in products if p['price'] > 100]
    print(f"折扣价格(原价>100): {discounted_prices}")
    
    # 6. 使用集合推导式和字典推导式
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    
    # 集合推导式（去重）
    unique_squares = {x**2 for x in numbers}
    print(f"\n原数字: {numbers}")
    print(f"唯一平方数: {unique_squares}")
    
    # 字典推导式
    word_lengths = {word: len(word) for word in ['apple', 'banana', 'cherry']}
    print(f"单词长度字典: {word_lengths}")

def demonstrate_performance_comparison():
    """演示列表推导式与传统方法的性能比较"""
    print("\n=== 性能比较 ===")
    
    import time
    
    def time_function(func, description):
        """测量函数执行时间"""
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"{description}: {end_time - start_time:.4f}秒")
        return result
    
    # 创建大量数据进行测试
    size = 100000
    
    # 方法1：传统for循环
    def traditional_method():
        result = []
        for i in range(size):
            if i % 2 == 0:
                result.append(i**2)
        return result
    
    # 方法2：列表推导式
    def comprehension_method():
        return [i**2 for i in range(size) if i % 2 == 0]
    
    # 方法3：filter + map
    def filter_map_method():
        return list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(size))))
    
    print(f"处理{size}个数字，筛选偶数并平方:")
    result1 = time_function(traditional_method, "传统for循环")
    result2 = time_function(comprehension_method, "列表推导式")
    result3 = time_function(filter_map_method, "filter+map")
    
    # 验证结果一致性
    print(f"结果一致性: {result1 == result2 == result3}")
    print(f"结果长度: {len(result1)}")
    
    print("\n性能总结:")
    print("- 列表推导式通常比传统循环快")
    print("- 列表推导式代码更简洁易读")
    print("- 对于复杂逻辑，传统循环可能更清晰")

def demonstrate_best_practices():
    """演示列表推导式的最佳实践"""
    print("\n=== 最佳实践 ===")
    
    # 1. 保持简洁
    print("✓ 好的做法 - 简洁明了:")
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    print(f"  平方数: {squares}")
    
    print("\n✗ 避免过于复杂的表达式:")
    # 复杂的推导式应该拆分
    complex_result = [x**2 + 2*x + 1 if x % 2 == 0 else x**3 - x**2 + x - 1 
                     for x in range(10) if x > 2 and x < 8]
    print(f"  复杂表达式结果: {complex_result}")
    print("  建议：将复杂逻辑提取为函数")
    
    # 2. 使用有意义的变量名
    print("\n✓ 使用有意义的变量名:")
    students = ['Alice', 'Bob', 'Charlie']
    student_lengths = [len(name) for name in students]  # 好
    # x_lengths = [len(x) for x in students]  # 不好
    print(f"  学生姓名长度: {student_lengths}")
    
    # 3. 适当使用括号提高可读性
    print("\n✓ 使用括号提高可读性:")
    result = [
        (x, x**2, x**3) 
        for x in range(1, 6) 
        if x % 2 == 1
    ]
    print(f"  奇数及其幂: {result}")
    
    # 4. 何时不使用列表推导式
    print("\n何时避免使用列表推导式:")
    print("- 逻辑过于复杂时")
    print("- 需要异常处理时")
    print("- 有副作用的操作时")
    print("- 嵌套层次过深时")
    
    # 5. 内存考虑
    print("\n内存使用考虑:")
    print("- 大数据集考虑使用生成器表达式")
    print("- 生成器: (x**2 for x in range(1000000))")
    print("- 列表推导式: [x**2 for x in range(1000000)]")
    
    # 生成器示例
    gen = (x**2 for x in range(10))
    print(f"生成器对象: {gen}")
    print(f"生成器内容: {list(gen)}")

def demonstrate_real_world_examples():
    """演示实际应用场景"""
    print("\n=== 实际应用场景 ===")
    
    # 1. 数据清洗
    raw_data = ['  Alice  ', '', '  Bob  ', None, '  Charlie  ', '   ']
    cleaned_data = [name.strip() for name in raw_data 
                   if name and name.strip()]
    print(f"原始数据: {raw_data}")
    print(f"清洗后数据: {cleaned_data}")
    
    # 2. 文件处理
    file_names = ['document.txt', 'image.jpg', 'script.py', 'data.csv', 'photo.png']
    python_files = [name for name in file_names if name.endswith('.py')]
    image_files = [name for name in file_names if name.endswith(('.jpg', '.png'))]
    
    print(f"\n所有文件: {file_names}")
    print(f"Python文件: {python_files}")
    print(f"图片文件: {image_files}")
    
    # 3. 数据转换
    csv_row = "Alice,25,Engineer,New York"
    fields = [field.strip() for field in csv_row.split(',')]
    print(f"\nCSV行: {csv_row}")
    print(f"字段列表: {fields}")
    
    # 4. 数学计算
    coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
    distances = [((x**2 + y**2)**0.5) for x, y in coordinates]
    print(f"\n坐标点: {coordinates}")
    print(f"到原点距离: {[round(d, 2) for d in distances]}")
    
    # 5. 文本处理
    text = "Hello World Python Programming"
    words = text.split()
    word_info = [{'word': word, 'length': len(word), 'upper': word.upper()} 
                for word in words]
    print(f"\n原文本: {text}")
    print("单词信息:")
    for info in word_info:
        print(f"  {info}")

def main():
    """主函数，演示所有列表推导式用法"""
    print("Python列表推导式完全指南")
    print("=" * 50)
    
    demonstrate_basic_comprehensions()
    demonstrate_conditional_comprehensions()
    demonstrate_conditional_expressions()
    demonstrate_nested_comprehensions()
    demonstrate_advanced_comprehensions()
    demonstrate_performance_comparison()
    demonstrate_best_practices()
    demonstrate_real_world_examples()
    
    print("\n=== 总结 ===")
    print("列表推导式语法总结:")
    print("\n基本语法:")
    print("[expression for item in iterable]")
    print("\n带过滤条件:")
    print("[expression for item in iterable if condition]")
    print("\n条件表达式:")
    print("[expr_if_true if condition else expr_if_false for item in iterable]")
    print("\n嵌套推导式:")
    print("[item for sublist in nested_list for item in sublist]")
    print("\n优势:")
    print("- 代码简洁，可读性强")
    print("- 执行效率高")
    print("- 符合Python风格")
    print("- 减少错误可能性")
    print("\n注意事项:")
    print("- 避免过于复杂的表达式")
    print("- 大数据集考虑使用生成器")
    print("- 复杂逻辑建议使用传统循环")

if __name__ == "__main__":
    main()