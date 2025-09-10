#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
列表推导式 (List Comprehensions)

学习目标：
1. 理解列表推导式的基本语法
2. 掌握列表推导式的各种用法
3. 了解列表推导式的优势和适用场景
4. 学会使用条件表达式和嵌套循环

作者：Python学习教程
日期：2024年
"""

def basic_list_comprehensions():
    """基本列表推导式语法"""
    print("=== 基本列表推导式 ===")
    
    # 基本语法：[expression for item in iterable]
    # 创建1到10的平方数列表
    squares = [x**2 for x in range(1, 11)]
    print(f"1-10的平方数: {squares}")
    
    # 传统方法对比
    squares_traditional = []
    for x in range(1, 11):
        squares_traditional.append(x**2)
    print(f"传统方法结果: {squares_traditional}")
    
    # 字符串处理
    words = ['hello', 'world', 'python', 'programming']
    uppercase_words = [word.upper() for word in words]
    print(f"大写单词: {uppercase_words}")
    
    # 数学运算
    numbers = [1, 2, 3, 4, 5]
    doubled = [n * 2 for n in numbers]
    print(f"数字翻倍: {doubled}")
    
    print()

def conditional_list_comprehensions():
    """带条件的列表推导式"""
    print("=== 带条件的列表推导式 ===")
    
    # 语法：[expression for item in iterable if condition]
    # 筛选偶数
    numbers = range(1, 21)
    even_numbers = [x for x in numbers if x % 2 == 0]
    print(f"1-20中的偶数: {even_numbers}")
    
    # 筛选并转换
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    long_words = [word.upper() for word in words if len(word) > 5]
    print(f"长度大于5的单词(大写): {long_words}")
    
    # 多个条件
    numbers = range(1, 101)
    special_numbers = [x for x in numbers if x % 3 == 0 and x % 5 == 0]
    print(f"1-100中能被3和5整除的数: {special_numbers}")
    
    # 条件表达式（三元运算符）
    numbers = [-5, -2, 0, 3, 8, -1, 4]
    abs_or_zero = [x if x >= 0 else 0 for x in numbers]
    print(f"负数变0，正数保持: {abs_or_zero}")
    
    print()

def nested_list_comprehensions():
    """嵌套列表推导式"""
    print("=== 嵌套列表推导式 ===")
    
    # 二维列表展平
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [item for row in matrix for item in row]
    print(f"矩阵展平: {flattened}")
    
    # 创建乘法表
    multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
    print("5x5乘法表:")
    for row in multiplication_table:
        print(row)
    
    # 笛卡尔积
    colors = ['red', 'blue']
    sizes = ['S', 'M', 'L']
    combinations = [(color, size) for color in colors for size in sizes]
    print(f"颜色和尺寸组合: {combinations}")
    
    # 带条件的嵌套
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    even_from_matrix = [item for row in matrix for item in row if item % 2 == 0]
    print(f"矩阵中的偶数: {even_from_matrix}")
    
    print()

def string_list_comprehensions():
    """字符串相关的列表推导式"""
    print("=== 字符串处理 ===")
    
    # 字符处理
    text = "Hello World"
    chars = [char for char in text if char.isalpha()]
    print(f"提取字母: {''.join(chars)}")
    
    # 单词处理
    sentence = "Python is a powerful programming language"
    words = sentence.split()
    word_lengths = [len(word) for word in words]
    print(f"单词长度: {word_lengths}")
    
    # 首字母大写
    names = ['alice', 'bob', 'charlie', 'diana']
    capitalized = [name.capitalize() for name in names]
    print(f"首字母大写: {capitalized}")
    
    # 提取数字
    mixed_string = "abc123def456ghi789"
    digits = [char for char in mixed_string if char.isdigit()]
    print(f"提取数字: {''.join(digits)}")
    
    print()

def advanced_list_comprehensions():
    """高级列表推导式用法"""
    print("=== 高级用法 ===")
    
    # 使用函数
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = [x for x in range(2, 50) if is_prime(x)]
    print(f"2-50之间的质数: {primes}")
    
    # 使用enumerate
    fruits = ['apple', 'banana', 'cherry']
    indexed_fruits = [f"{i}: {fruit}" for i, fruit in enumerate(fruits)]
    print(f"带索引的水果: {indexed_fruits}")
    
    # 使用zip
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    name_age_pairs = [f"{name} is {age} years old" for name, age in zip(names, ages)]
    print(f"姓名年龄对: {name_age_pairs}")
    
    # 字典的键值对
    student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 96}
    high_achievers = [name for name, grade in student_grades.items() if grade >= 90]
    print(f"高分学生: {high_achievers}")
    
    print()

def performance_comparison():
    """性能对比示例"""
    print("=== 性能对比 ===")
    
    import time
    
    # 大数据量测试
    n = 100000
    
    # 列表推导式
    start_time = time.time()
    squares_comp = [x**2 for x in range(n)]
    comp_time = time.time() - start_time
    
    # 传统循环
    start_time = time.time()
    squares_loop = []
    for x in range(n):
        squares_loop.append(x**2)
    loop_time = time.time() - start_time
    
    # map函数
    start_time = time.time()
    squares_map = list(map(lambda x: x**2, range(n)))
    map_time = time.time() - start_time
    
    print(f"计算{n}个数的平方:")
    print(f"列表推导式: {comp_time:.4f}秒")
    print(f"传统循环: {loop_time:.4f}秒")
    print(f"map函数: {map_time:.4f}秒")
    
    # 验证结果一致性
    print(f"结果一致性: {squares_comp == squares_loop == squares_map}")
    
    print()

def practical_examples():
    """实际应用示例"""
    print("=== 实际应用示例 ===")
    
    # 数据清洗
    raw_data = ['  Alice  ', 'BOB', '  charlie', 'DIANA  ', '  eve  ']
    cleaned_data = [name.strip().title() for name in raw_data]
    print(f"清洗后的数据: {cleaned_data}")
    
    # 文件扩展名提取
    filenames = ['document.pdf', 'image.jpg', 'script.py', 'data.csv', 'readme.txt']
    extensions = [filename.split('.')[-1] for filename in filenames]
    print(f"文件扩展名: {extensions}")
    
    # 温度转换
    celsius_temps = [0, 10, 20, 30, 40]
    fahrenheit_temps = [c * 9/5 + 32 for c in celsius_temps]
    print(f"摄氏度转华氏度: {list(zip(celsius_temps, fahrenheit_temps))}")
    
    # 购物车总价计算
    items = [('apple', 2.5, 3), ('banana', 1.2, 5), ('orange', 3.0, 2)]
    total_prices = [price * quantity for name, price, quantity in items]
    print(f"商品总价: {total_prices}")
    print(f"购物车总计: {sum(total_prices):.2f}")
    
    print()

def common_mistakes():
    """常见错误和注意事项"""
    print("=== 常见错误和注意事项 ===")
    
    # 错误1：过度复杂的表达式
    print("❌ 避免过度复杂的表达式")
    numbers = [1, 2, 3, 4, 5]
    # 不推荐：太复杂
    # complex_result = [x**2 + 2*x + 1 if x % 2 == 0 else x**3 - x for x in numbers if x > 2]
    
    # 推荐：分步骤或使用函数
    def process_number(x):
        if x % 2 == 0:
            return x**2 + 2*x + 1
        else:
            return x**3 - x
    
    filtered_numbers = [x for x in numbers if x > 2]
    processed_numbers = [process_number(x) for x in filtered_numbers]
    print(f"分步处理结果: {processed_numbers}")
    
    # 错误2：修改原列表
    print("\n❌ 避免在推导式中修改原列表")
    original_list = [1, 2, 3, 4, 5]
    # 正确做法：创建新列表
    modified_list = [x * 2 for x in original_list]
    print(f"原列表: {original_list}")
    print(f"新列表: {modified_list}")
    
    # 注意3：内存使用
    print("\n⚠️ 大数据量时考虑使用生成器")
    print("列表推导式会立即创建完整列表，占用内存")
    print("生成器表达式按需生成，节省内存")
    
    print()

def main():
    """主函数"""
    print("Python 列表推导式学习教程")
    print("=" * 50)
    
    basic_list_comprehensions()
    conditional_list_comprehensions()
    nested_list_comprehensions()
    string_list_comprehensions()
    advanced_list_comprehensions()
    performance_comparison()
    practical_examples()
    common_mistakes()
    
    print("学习要点总结:")
    print("1. 列表推导式语法简洁，可读性强")
    print("2. 性能通常优于传统循环")
    print("3. 适合简单到中等复杂度的数据处理")
    print("4. 过度复杂时应考虑使用函数或传统循环")
    print("5. 大数据量时考虑使用生成器表达式")

if __name__ == "__main__":
    main()