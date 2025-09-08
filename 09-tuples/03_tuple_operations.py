#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
元组操作和方法 - Tuple Operations and Methods

本文件演示了Python中元组的各种操作和方法：
1. 元组连接和重复
2. 元组比较
3. 元组内置方法（count, index）
4. 元组与其他数据类型的转换
5. 元组的数学运算
6. 元组的实用函数

作者: Python学习教程
日期: 2024
"""

def main():
    print("=" * 50)
    print("元组操作和方法演示")
    print("=" * 50)
    
    # 创建示例元组
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    tuple3 = (1, 2, 3, 2, 1, 4, 2)
    fruits = ("apple", "banana", "cherry")
    numbers = (10, 20, 30, 40, 50)
    
    print(f"tuple1 = {tuple1}")
    print(f"tuple2 = {tuple2}")
    print(f"tuple3 = {tuple3}")
    print(f"fruits = {fruits}")
    print(f"numbers = {numbers}")
    
    # 1. 元组连接（+操作符）
    print("\n1. 元组连接:")
    combined = tuple1 + tuple2
    print(f"tuple1 + tuple2 = {combined}")
    
    # 多个元组连接
    multi_combined = tuple1 + tuple2 + fruits
    print(f"tuple1 + tuple2 + fruits = {multi_combined}")
    
    # 连接不同类型的元组
    mixed_combined = numbers + fruits
    print(f"numbers + fruits = {mixed_combined}")
    
    # 2. 元组重复（*操作符）
    print("\n2. 元组重复:")
    repeated = tuple1 * 3
    print(f"tuple1 * 3 = {repeated}")
    
    # 重复字符串元组
    repeated_fruits = fruits * 2
    print(f"fruits * 2 = {repeated_fruits}")
    
    # 创建初始化元组
    zeros = (0,) * 5
    print(f"(0,) * 5 = {zeros}")
    
    # 3. 元组比较
    print("\n3. 元组比较:")
    tuple_a = (1, 2, 3)
    tuple_b = (1, 2, 3)
    tuple_c = (1, 2, 4)
    tuple_d = (1, 2)
    
    print(f"tuple_a = {tuple_a}")
    print(f"tuple_b = {tuple_b}")
    print(f"tuple_c = {tuple_c}")
    print(f"tuple_d = {tuple_d}")
    
    # 相等比较
    print(f"tuple_a == tuple_b: {tuple_a == tuple_b}")
    print(f"tuple_a == tuple_c: {tuple_a == tuple_c}")
    
    # 大小比较（字典序）
    print(f"tuple_a < tuple_c: {tuple_a < tuple_c}")
    print(f"tuple_a > tuple_d: {tuple_a > tuple_d}")
    print(f"tuple_d < tuple_a: {tuple_d < tuple_a}")
    
    # 字符串元组比较
    fruits1 = ("apple", "banana")
    fruits2 = ("apple", "cherry")
    print(f"fruits1 < fruits2: {fruits1 < fruits2}")
    
    # 4. 元组内置方法
    print("\n4. 元组内置方法:")
    
    # count()方法 - 计算元素出现次数
    print(f"tuple3 = {tuple3}")
    print(f"tuple3.count(2) = {tuple3.count(2)}")
    print(f"tuple3.count(1) = {tuple3.count(1)}")
    print(f"tuple3.count(5) = {tuple3.count(5)}")
    
    # index()方法 - 查找元素第一次出现的索引
    print(f"tuple3.index(2) = {tuple3.index(2)}")
    print(f"tuple3.index(4) = {tuple3.index(4)}")
    
    # 处理index()方法的异常
    try:
        index = tuple3.index(10)
        print(f"tuple3.index(10) = {index}")
    except ValueError as e:
        print(f"ValueError: {e}")
    
    # 5. 元组长度和成员检查
    print("\n5. 元组长度和成员检查:")
    print(f"len(tuple3) = {len(tuple3)}")
    print(f"len(fruits) = {len(fruits)}")
    
    # 成员检查
    print(f"2 in tuple3: {2 in tuple3}")
    print(f"'apple' in fruits: {'apple' in fruits}")
    print(f"'grape' not in fruits: {'grape' not in fruits}")

def demonstrate_tuple_functions():
    """演示元组相关的内置函数"""
    print("\n=" * 30)
    print("元组内置函数演示")
    print("=" * 30)
    
    numbers = (5, 2, 8, 1, 9, 3)
    mixed_numbers = (1.5, 2, 3.7, 4, 5.2)
    
    print(f"numbers = {numbers}")
    print(f"mixed_numbers = {mixed_numbers}")
    
    # 数学函数
    print("\n数学函数:")
    print(f"sum(numbers) = {sum(numbers)}")
    print(f"max(numbers) = {max(numbers)}")
    print(f"min(numbers) = {min(numbers)}")
    print(f"sum(mixed_numbers) = {sum(mixed_numbers)}")
    
    # 排序相关
    print("\n排序相关:")
    print(f"sorted(numbers) = {sorted(numbers)}")
    print(f"sorted(numbers, reverse=True) = {sorted(numbers, reverse=True)}")
    
    # 字符串元组排序
    fruits = ("banana", "apple", "cherry", "date")
    print(f"fruits = {fruits}")
    print(f"sorted(fruits) = {sorted(fruits)}")
    print(f"sorted(fruits, key=len) = {sorted(fruits, key=len)}")
    
    # 其他有用函数
    print("\n其他函数:")
    print(f"any(numbers) = {any(numbers)}")
    print(f"all(numbers) = {all(numbers)}")
    
    # 包含0的情况
    with_zero = (1, 2, 0, 4)
    print(f"with_zero = {with_zero}")
    print(f"any(with_zero) = {any(with_zero)}")
    print(f"all(with_zero) = {all(with_zero)}")

def demonstrate_tuple_conversions():
    """演示元组与其他数据类型的转换"""
    print("\n=" * 30)
    print("元组转换演示")
    print("=" * 30)
    
    # 1. 元组与列表转换
    print("1. 元组与列表转换:")
    original_tuple = (1, 2, 3, 4, 5)
    converted_list = list(original_tuple)
    back_to_tuple = tuple(converted_list)
    
    print(f"原始元组: {original_tuple}")
    print(f"转换为列表: {converted_list}")
    print(f"转换回元组: {back_to_tuple}")
    
    # 2. 元组与集合转换
    print("\n2. 元组与集合转换:")
    tuple_with_duplicates = (1, 2, 2, 3, 3, 3, 4)
    converted_set = set(tuple_with_duplicates)
    unique_tuple = tuple(converted_set)
    
    print(f"有重复的元组: {tuple_with_duplicates}")
    print(f"转换为集合: {converted_set}")
    print(f"去重后的元组: {unique_tuple}")
    
    # 3. 元组与字符串转换
    print("\n3. 元组与字符串转换:")
    char_tuple = ('h', 'e', 'l', 'l', 'o')
    joined_string = ''.join(char_tuple)
    
    print(f"字符元组: {char_tuple}")
    print(f"连接为字符串: {joined_string}")
    
    # 字符串分割为元组
    text = "apple,banana,cherry"
    split_tuple = tuple(text.split(','))
    print(f"原始字符串: {text}")
    print(f"分割为元组: {split_tuple}")
    
    # 4. 元组与字典转换
    print("\n4. 元组与字典转换:")
    pairs = (("name", "Alice"), ("age", 25), ("city", "Beijing"))
    converted_dict = dict(pairs)
    
    print(f"键值对元组: {pairs}")
    print(f"转换为字典: {converted_dict}")
    
    # 字典转换为元组
    dict_items = tuple(converted_dict.items())
    dict_keys = tuple(converted_dict.keys())
    dict_values = tuple(converted_dict.values())
    
    print(f"字典项目: {dict_items}")
    print(f"字典键: {dict_keys}")
    print(f"字典值: {dict_values}")

def demonstrate_advanced_operations():
    """演示高级元组操作"""
    print("\n=" * 30)
    print("高级元组操作")
    print("=" * 30)
    
    # 1. 元组推导式（实际上是生成器表达式转元组）
    print("1. 元组推导式:")
    numbers = (1, 2, 3, 4, 5)
    squared = tuple(x**2 for x in numbers)
    print(f"原始数字: {numbers}")
    print(f"平方数: {squared}")
    
    # 条件筛选
    even_squares = tuple(x**2 for x in numbers if x % 2 == 0)
    print(f"偶数的平方: {even_squares}")
    
    # 2. 嵌套元组操作
    print("\n2. 嵌套元组操作:")
    matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    print(f"矩阵: {matrix}")
    
    # 转置矩阵
    transposed = tuple(zip(*matrix))
    print(f"转置矩阵: {transposed}")
    
    # 展平嵌套元组
    flattened = tuple(item for row in matrix for item in row)
    print(f"展平元组: {flattened}")
    
    # 3. 元组与zip函数
    print("\n3. 元组与zip函数:")
    names = ("Alice", "Bob", "Charlie")
    ages = (25, 30, 35)
    cities = ("Beijing", "Shanghai", "Guangzhou")
    
    combined = tuple(zip(names, ages, cities))
    print(f"姓名: {names}")
    print(f"年龄: {ages}")
    print(f"城市: {cities}")
    print(f"组合结果: {combined}")
    
    # 解压缩
    unzipped_names, unzipped_ages, unzipped_cities = zip(*combined)
    print(f"解压缩姓名: {unzipped_names}")
    print(f"解压缩年龄: {unzipped_ages}")
    print(f"解压缩城市: {unzipped_cities}")
    
    # 4. 元组作为字典键
    print("\n4. 元组作为字典键:")
    coordinates = {
        (0, 0): "原点",
        (1, 0): "x轴上的点",
        (0, 1): "y轴上的点",
        (1, 1): "对角线上的点"
    }
    
    print("坐标字典:")
    for coord, description in coordinates.items():
        print(f"  {coord}: {description}")
    
    # 查找特定坐标
    point = (1, 0)
    if point in coordinates:
        print(f"坐标 {point} 的描述: {coordinates[point]}")

if __name__ == "__main__":
    main()
    demonstrate_tuple_functions()
    demonstrate_tuple_conversions()
    demonstrate_advanced_operations()
    
    print("\n" + "=" * 50)
    print("元组操作和方法学习完成！")
    print("下一步：学习元组解包和多重赋值")
    print("=" * 50)