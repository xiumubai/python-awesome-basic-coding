#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
列表创建 - 创建列表的各种方法

本文件演示了Python中创建列表的多种方法：
1. 使用方括号创建列表
2. 使用list()函数创建列表
3. 使用range()函数创建数字列表
4. 使用列表推导式创建列表
5. 创建特殊类型的列表

作者：Python学习教程
日期：2024年
"""

def demonstrate_basic_list_creation():
    """演示基本的列表创建方法"""
    print("=== 基本列表创建方法 ===")
    
    # 1. 创建空列表
    empty_list1 = []
    empty_list2 = list()
    print(f"空列表1: {empty_list1}")
    print(f"空列表2: {empty_list2}")
    print(f"两个空列表相等: {empty_list1 == empty_list2}")
    
    # 2. 创建包含元素的列表
    numbers = [1, 2, 3, 4, 5]
    fruits = ['apple', 'banana', 'orange']
    mixed = [1, 'hello', 3.14, True]
    
    print(f"\n数字列表: {numbers}")
    print(f"水果列表: {fruits}")
    print(f"混合类型列表: {mixed}")
    
    # 3. 使用重复操作符创建列表
    zeros = [0] * 5
    pattern = ['a', 'b'] * 3
    
    print(f"\n重复创建 - 零列表: {zeros}")
    print(f"重复创建 - 模式列表: {pattern}")

def demonstrate_list_function():
    """演示使用list()函数创建列表"""
    print("\n=== 使用list()函数创建列表 ===")
    
    # 1. 从字符串创建列表
    string_to_list = list("hello")
    print(f"字符串转列表: {string_to_list}")
    
    # 2. 从元组创建列表
    tuple_data = (1, 2, 3, 4)
    tuple_to_list = list(tuple_data)
    print(f"元组转列表: {tuple_to_list}")
    
    # 3. 从集合创建列表
    set_data = {3, 1, 4, 1, 5}
    set_to_list = list(set_data)
    print(f"集合转列表: {set_to_list}")
    
    # 4. 从字典创建列表
    dict_data = {'a': 1, 'b': 2, 'c': 3}
    keys_list = list(dict_data.keys())
    values_list = list(dict_data.values())
    items_list = list(dict_data.items())
    
    print(f"字典键转列表: {keys_list}")
    print(f"字典值转列表: {values_list}")
    print(f"字典项转列表: {items_list}")

def demonstrate_range_lists():
    """演示使用range()函数创建数字列表"""
    print("\n=== 使用range()创建数字列表 ===")
    
    # 1. 基本range用法
    range_list1 = list(range(5))
    range_list2 = list(range(1, 6))
    range_list3 = list(range(0, 10, 2))
    range_list4 = list(range(10, 0, -1))
    
    print(f"range(5): {range_list1}")
    print(f"range(1, 6): {range_list2}")
    print(f"range(0, 10, 2): {range_list3}")
    print(f"range(10, 0, -1): {range_list4}")
    
    # 2. 创建特殊数字序列
    even_numbers = list(range(0, 21, 2))
    odd_numbers = list(range(1, 21, 2))
    multiples_of_5 = list(range(0, 51, 5))
    
    print(f"\n偶数列表(0-20): {even_numbers}")
    print(f"奇数列表(1-19): {odd_numbers}")
    print(f"5的倍数(0-50): {multiples_of_5}")

def demonstrate_list_comprehensions():
    """演示使用列表推导式创建列表"""
    print("\n=== 使用列表推导式创建列表 ===")
    
    # 1. 基本列表推导式
    squares = [x**2 for x in range(1, 6)]
    print(f"平方数列表: {squares}")
    
    # 2. 带条件的列表推导式
    even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
    print(f"偶数的平方: {even_squares}")
    
    # 3. 字符串处理
    words = ['hello', 'world', 'python']
    upper_words = [word.upper() for word in words]
    word_lengths = [len(word) for word in words]
    
    print(f"大写单词: {upper_words}")
    print(f"单词长度: {word_lengths}")
    
    # 4. 嵌套列表推导式
    matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
    print(f"乘法表矩阵: {matrix}")

def demonstrate_special_lists():
    """演示创建特殊类型的列表"""
    print("\n=== 创建特殊类型的列表 ===")
    
    # 1. 嵌套列表
    nested_list = [[1, 2], [3, 4], [5, 6]]
    print(f"嵌套列表: {nested_list}")
    
    # 2. 包含不同数据类型的列表
    mixed_types = [42, 'hello', [1, 2, 3], {'key': 'value'}, (1, 2)]
    print(f"混合类型列表: {mixed_types}")
    
    # 3. 使用函数创建列表
    import random
    random_numbers = [random.randint(1, 100) for _ in range(5)]
    print(f"随机数列表: {random_numbers}")
    
    # 4. 创建二维列表（矩阵）
    rows, cols = 3, 4
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    print(f"3x4零矩阵: {matrix}")
    
    # 5. 创建包含函数的列表
    def square(x):
        return x ** 2
    
    def cube(x):
        return x ** 3
    
    functions = [square, cube, lambda x: x * 2]
    print(f"\n函数列表应用到数字5:")
    for i, func in enumerate(functions):
        print(f"函数{i+1}(5) = {func(5)}")

def demonstrate_list_copying():
    """演示列表复制的不同方法"""
    print("\n=== 列表复制方法 ===")
    
    original = [1, 2, 3, 4, 5]
    
    # 1. 浅复制方法
    copy1 = original.copy()
    copy2 = original[:]
    copy3 = list(original)
    
    print(f"原始列表: {original}")
    print(f"copy()方法: {copy1}")
    print(f"切片复制: {copy2}")
    print(f"list()复制: {copy3}")
    
    # 验证是否为不同对象
    print(f"\ncopy1 is original: {copy1 is original}")
    print(f"copy1 == original: {copy1 == original}")
    
    # 2. 深复制（对于嵌套列表）
    import copy
    nested_original = [[1, 2], [3, 4]]
    shallow_copy = nested_original.copy()
    deep_copy = copy.deepcopy(nested_original)
    
    print(f"\n嵌套列表原始: {nested_original}")
    print(f"浅复制: {shallow_copy}")
    print(f"深复制: {deep_copy}")
    
    # 修改嵌套列表测试
    nested_original[0][0] = 999
    print(f"\n修改原始列表后:")
    print(f"原始列表: {nested_original}")
    print(f"浅复制: {shallow_copy}")
    print(f"深复制: {deep_copy}")

def main():
    """主函数，演示所有列表创建方法"""
    print("Python列表创建方法大全")
    print("=" * 50)
    
    demonstrate_basic_list_creation()
    demonstrate_list_function()
    demonstrate_range_lists()
    demonstrate_list_comprehensions()
    demonstrate_special_lists()
    demonstrate_list_copying()
    
    print("\n=== 总结 ===")
    print("列表创建的主要方法:")
    print("1. 使用方括号 [] 直接创建")
    print("2. 使用 list() 函数转换其他数据类型")
    print("3. 使用 range() 函数创建数字序列")
    print("4. 使用列表推导式进行复杂创建")
    print("5. 使用重复操作符 * 创建重复元素")
    print("6. 复制现有列表创建新列表")

if __name__ == "__main__":
    main()