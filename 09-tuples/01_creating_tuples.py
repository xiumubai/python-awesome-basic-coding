#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
元组创建 - Creating Tuples

本文件演示了Python中创建元组的各种方法：
1. 使用圆括号创建元组
2. 不使用圆括号创建元组
3. 创建空元组
4. 创建单元素元组
5. 使用tuple()函数创建元组
6. 从其他数据类型转换为元组

作者: Python学习教程
日期: 2024
"""

def main():
    print("=" * 50)
    print("元组创建方法演示")
    print("=" * 50)
    
    # 1. 使用圆括号创建元组
    print("\n1. 使用圆括号创建元组:")
    tuple1 = (1, 2, 3, 4, 5)
    print(f"tuple1 = {tuple1}")
    print(f"类型: {type(tuple1)}")
    
    # 包含不同数据类型的元组
    mixed_tuple = (1, "hello", 3.14, True)
    print(f"mixed_tuple = {mixed_tuple}")
    
    # 2. 不使用圆括号创建元组（元组打包）
    print("\n2. 不使用圆括号创建元组（元组打包）:")
    tuple2 = 1, 2, 3, 4, 5
    print(f"tuple2 = {tuple2}")
    print(f"类型: {type(tuple2)}")
    
    # 3. 创建空元组
    print("\n3. 创建空元组:")
    empty_tuple1 = ()
    empty_tuple2 = tuple()
    print(f"empty_tuple1 = {empty_tuple1}")
    print(f"empty_tuple2 = {empty_tuple2}")
    print(f"长度: {len(empty_tuple1)}")
    
    # 4. 创建单元素元组（注意逗号的重要性）
    print("\n4. 创建单元素元组:")
    # 正确的单元素元组创建方法
    single_tuple = (42,)  # 注意逗号
    print(f"single_tuple = {single_tuple}")
    print(f"类型: {type(single_tuple)}")
    
    # 错误示例：没有逗号不是元组
    not_tuple = (42)  # 这只是一个整数
    print(f"not_tuple = {not_tuple}")
    print(f"类型: {type(not_tuple)}")
    
    # 不使用括号的单元素元组
    single_tuple2 = 42,
    print(f"single_tuple2 = {single_tuple2}")
    print(f"类型: {type(single_tuple2)}")
    
    # 5. 使用tuple()函数创建元组
    print("\n5. 使用tuple()函数创建元组:")
    
    # 从列表创建元组
    list_data = [1, 2, 3, 4, 5]
    tuple_from_list = tuple(list_data)
    print(f"从列表创建: {tuple_from_list}")
    
    # 从字符串创建元组
    string_data = "hello"
    tuple_from_string = tuple(string_data)
    print(f"从字符串创建: {tuple_from_string}")
    
    # 从range创建元组
    tuple_from_range = tuple(range(1, 6))
    print(f"从range创建: {tuple_from_range}")
    
    # 6. 嵌套元组
    print("\n6. 嵌套元组:")
    nested_tuple = ((1, 2), (3, 4), (5, 6))
    print(f"nested_tuple = {nested_tuple}")
    
    # 混合嵌套
    complex_tuple = (1, (2, 3), [4, 5], "hello")
    print(f"complex_tuple = {complex_tuple}")
    
    # 7. 元组的特性演示
    print("\n7. 元组的特性:")
    demo_tuple = (1, 2, 3, 2, 1)
    print(f"demo_tuple = {demo_tuple}")
    print(f"长度: {len(demo_tuple)}")
    print(f"元素2的个数: {demo_tuple.count(2)}")
    print(f"元素1第一次出现的索引: {demo_tuple.index(1)}")
    
    # 8. 元组与列表的转换
    print("\n8. 元组与列表的转换:")
    original_list = [1, 2, 3, 4, 5]
    converted_tuple = tuple(original_list)
    converted_back_list = list(converted_tuple)
    
    print(f"原始列表: {original_list}")
    print(f"转换为元组: {converted_tuple}")
    print(f"转换回列表: {converted_back_list}")
    
    # 9. 实际应用示例
    print("\n9. 实际应用示例:")
    
    # 坐标点
    point = (3, 4)
    print(f"坐标点: {point}")
    
    # RGB颜色值
    red_color = (255, 0, 0)
    green_color = (0, 255, 0)
    blue_color = (0, 0, 255)
    print(f"红色: {red_color}")
    print(f"绿色: {green_color}")
    print(f"蓝色: {blue_color}")
    
    # 学生信息
    student = ("张三", 20, "计算机科学", 3.8)
    print(f"学生信息: {student}")
    
    # 数据库记录
    database_record = (1, "John Doe", "john@email.com", "2024-01-01")
    print(f"数据库记录: {database_record}")

def demonstrate_tuple_immutability():
    """演示元组的不可变性"""
    print("\n=" * 30)
    print("元组不可变性演示")
    print("=" * 30)
    
    my_tuple = (1, 2, 3, 4, 5)
    print(f"原始元组: {my_tuple}")
    
    # 尝试修改元组会引发错误
    try:
        my_tuple[0] = 10  # 这会引发TypeError
    except TypeError as e:
        print(f"错误: {e}")
        print("元组是不可变的，不能修改其元素")
    
    # 但是可以创建新的元组
    new_tuple = (10,) + my_tuple[1:]
    print(f"创建新元组: {new_tuple}")

if __name__ == "__main__":
    main()
    demonstrate_tuple_immutability()
    
    print("\n" + "=" * 50)
    print("元组创建学习完成！")
    print("下一步：学习元组元素访问")
    print("=" * 50)