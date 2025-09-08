#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
集合的创建方法

本文件演示了Python中创建集合的各种方法：
1. 使用花括号创建集合
2. 使用set()函数创建集合
3. 从其他数据类型创建集合
4. 创建空集合的注意事项
5. 集合的特性：无序性和唯一性

作者：Python学习教程
日期：2024年
"""

def main():
    print("=" * 50)
    print("集合的创建方法演示")
    print("=" * 50)
    
    # 1. 使用花括号创建集合
    print("\n1. 使用花括号创建集合")
    print("-" * 30)
    
    # 创建包含数字的集合
    numbers = {1, 2, 3, 4, 5}
    print(f"数字集合: {numbers}")
    print(f"集合类型: {type(numbers)}")
    
    # 创建包含字符串的集合
    fruits = {"apple", "banana", "orange", "grape"}
    print(f"水果集合: {fruits}")
    
    # 创建混合类型的集合
    mixed = {1, "hello", 3.14, True}
    print(f"混合类型集合: {mixed}")
    
    # 2. 使用set()函数创建集合
    print("\n2. 使用set()函数创建集合")
    print("-" * 30)
    
    # 从列表创建集合
    list_data = [1, 2, 3, 4, 5, 3, 2, 1]  # 包含重复元素
    set_from_list = set(list_data)
    print(f"原始列表: {list_data}")
    print(f"从列表创建的集合: {set_from_list}")
    print("注意：重复元素被自动去除")
    
    # 从字符串创建集合
    string_data = "hello world"
    set_from_string = set(string_data)
    print(f"\n原始字符串: '{string_data}'")
    print(f"从字符串创建的集合: {set_from_string}")
    print("注意：每个字符成为集合的一个元素")
    
    # 从元组创建集合
    tuple_data = (1, 2, 3, 2, 1, 4)
    set_from_tuple = set(tuple_data)
    print(f"\n原始元组: {tuple_data}")
    print(f"从元组创建的集合: {set_from_tuple}")
    
    # 3. 创建空集合
    print("\n3. 创建空集合")
    print("-" * 30)
    
    # 正确的方式：使用set()
    empty_set = set()
    print(f"空集合: {empty_set}")
    print(f"空集合类型: {type(empty_set)}")
    print(f"空集合长度: {len(empty_set)}")
    
    # 错误的方式：使用{}
    empty_dict = {}
    print(f"\n使用{{}}创建的是: {type(empty_dict)}")
    print("注意：{}创建的是字典，不是集合！")
    
    # 4. 集合的特性演示
    print("\n4. 集合的特性演示")
    print("-" * 30)
    
    # 唯一性：自动去重
    duplicate_data = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    unique_set = set(duplicate_data)
    print(f"包含重复元素的列表: {duplicate_data}")
    print(f"转换为集合后: {unique_set}")
    print(f"原始长度: {len(duplicate_data)}, 集合长度: {len(unique_set)}")
    
    # 无序性：集合中的元素没有固定顺序
    print("\n无序性演示：")
    for i in range(3):
        temp_set = {5, 1, 3, 2, 4}
        print(f"第{i+1}次创建同样的集合: {temp_set}")
    print("注意：集合的显示顺序可能不同，这是正常的")
    
    # 5. 使用集合进行去重操作
    print("\n5. 使用集合进行去重操作")
    print("-" * 30)
    
    # 去除列表中的重复元素
    original_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
    print(f"原始列表: {original_list}")
    
    # 方法1：转换为集合再转回列表
    unique_list1 = list(set(original_list))
    print(f"去重后的列表: {unique_list1}")
    
    # 方法2：保持原有顺序的去重
    unique_list2 = []
    seen = set()
    for item in original_list:
        if item not in seen:
            unique_list2.append(item)
            seen.add(item)
    print(f"保持顺序的去重列表: {unique_list2}")
    
    # 6. 集合的实际应用示例
    print("\n6. 集合的实际应用示例")
    print("-" * 30)
    
    # 统计文本中的唯一单词
    text = "python is great python is powerful python is easy"
    words = text.split()
    unique_words = set(words)
    print(f"原始文本: {text}")
    print(f"所有单词: {words}")
    print(f"唯一单词: {unique_words}")
    print(f"总单词数: {len(words)}, 唯一单词数: {len(unique_words)}")
    
    # 检查两个列表的共同元素
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1 & set2  # 交集
    print(f"\n列表1: {list1}")
    print(f"列表2: {list2}")
    print(f"共同元素: {common_elements}")
    
    print("\n=" * 50)
    print("集合创建方法演示完成！")
    print("=" * 50)

def demonstrate_set_creation_methods():
    """
    演示不同的集合创建方法
    """
    print("\n补充：更多集合创建方法")
    print("-" * 30)
    
    # 使用集合推导式（后续章节会详细介绍）
    squares = {x**2 for x in range(1, 6)}
    print(f"使用集合推导式创建平方数集合: {squares}")
    
    # 从字典的键创建集合
    person = {"name": "Alice", "age": 25, "city": "Beijing"}
    keys_set = set(person.keys())
    print(f"从字典键创建集合: {keys_set}")
    
    # 从字典的值创建集合
    values_set = set(person.values())
    print(f"从字典值创建集合: {values_set}")

def practice_exercises():
    """
    练习题
    """
    print("\n练习题：")
    print("-" * 20)
    
    # 练习1：创建一个包含1到10的偶数的集合
    even_numbers = {x for x in range(1, 11) if x % 2 == 0}
    print(f"1. 1到10的偶数集合: {even_numbers}")
    
    # 练习2：从两个列表创建集合并找出不同元素
    colors1 = ["red", "blue", "green", "yellow"]
    colors2 = ["blue", "green", "purple", "orange"]
    set_colors1 = set(colors1)
    set_colors2 = set(colors2)
    different_colors = set_colors1 ^ set_colors2  # 对称差集
    print(f"2. 两个颜色列表的不同元素: {different_colors}")
    
    # 练习3：统计字符串中的唯一字符数量
    text = "programming"
    unique_chars = set(text)
    print(f"3. 字符串'{text}'中的唯一字符: {unique_chars}")
    print(f"   唯一字符数量: {len(unique_chars)}")

if __name__ == "__main__":
    main()
    demonstrate_set_creation_methods()
    practice_exercises()