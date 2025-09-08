#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
元组元素访问 - Accessing Tuple Elements

本文件演示了Python中访问元组元素的各种方法：
1. 正向索引访问
2. 负向索引访问
3. 切片操作
4. 检查元素是否存在
5. 遍历元组
6. 嵌套元组访问

作者: Python学习教程
日期: 2024
"""

def main():
    print("=" * 50)
    print("元组元素访问演示")
    print("=" * 50)
    
    # 创建示例元组
    fruits = ("apple", "banana", "cherry", "date", "elderberry")
    numbers = (10, 20, 30, 40, 50, 60, 70)
    mixed = (1, "hello", 3.14, True, [1, 2, 3])
    
    print(f"fruits = {fruits}")
    print(f"numbers = {numbers}")
    print(f"mixed = {mixed}")
    
    # 1. 正向索引访问
    print("\n1. 正向索引访问:")
    print(f"fruits[0] = {fruits[0]}")
    print(f"fruits[1] = {fruits[1]}")
    print(f"fruits[2] = {fruits[2]}")
    print(f"numbers[0] = {numbers[0]}")
    print(f"numbers[3] = {numbers[3]}")
    
    # 2. 负向索引访问
    print("\n2. 负向索引访问:")
    print(f"fruits[-1] = {fruits[-1]}")
    print(f"fruits[-2] = {fruits[-2]}")
    print(f"numbers[-1] = {numbers[-1]}")
    print(f"numbers[-3] = {numbers[-3]}")
    
    # 索引对照表
    print("\n索引对照表:")
    print("正向索引:", end=" ")
    for i in range(len(fruits)):
        print(f"{i:>8}", end="")
    print()
    print("元素值  :", end=" ")
    for fruit in fruits:
        print(f"{fruit:>8}", end="")
    print()
    print("负向索引:", end=" ")
    for i in range(-len(fruits), 0):
        print(f"{i:>8}", end="")
    print()
    
    # 3. 切片操作
    print("\n3. 切片操作:")
    print(f"fruits[1:4] = {fruits[1:4]}")
    print(f"fruits[:3] = {fruits[:3]}")
    print(f"fruits[2:] = {fruits[2:]}")
    print(f"fruits[:] = {fruits[:]}")
    print(f"fruits[::2] = {fruits[::2]}")
    print(f"fruits[::-1] = {fruits[::-1]}")
    
    # 数字元组的切片
    print(f"\nnumbers[2:5] = {numbers[2:5]}")
    print(f"numbers[-3:] = {numbers[-3:]}")
    print(f"numbers[1::2] = {numbers[1::2]}")
    
    # 4. 检查元素是否存在
    print("\n4. 检查元素是否存在:")
    print(f"'apple' in fruits: {'apple' in fruits}")
    print(f"'grape' in fruits: {'grape' in fruits}")
    print(f"30 in numbers: {30 in numbers}")
    print(f"100 in numbers: {100 in numbers}")
    
    # 使用not in
    print(f"'grape' not in fruits: {'grape' not in fruits}")
    print(f"100 not in numbers: {100 not in numbers}")
    
    # 5. 遍历元组
    print("\n5. 遍历元组:")
    
    # 直接遍历元素
    print("直接遍历fruits:")
    for fruit in fruits:
        print(f"  {fruit}")
    
    # 遍历索引和元素
    print("\n遍历索引和元素:")
    for i, fruit in enumerate(fruits):
        print(f"  索引 {i}: {fruit}")
    
    # 遍历数字元组
    print("\n遍历numbers:")
    for i, num in enumerate(numbers):
        print(f"  位置 {i}: {num}")
    
    # 6. 嵌套元组访问
    print("\n6. 嵌套元组访问:")
    nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    print(f"nested_tuple = {nested_tuple}")
    
    # 访问外层元素
    print(f"nested_tuple[0] = {nested_tuple[0]}")
    print(f"nested_tuple[1] = {nested_tuple[1]}")
    
    # 访问内层元素
    print(f"nested_tuple[0][0] = {nested_tuple[0][0]}")
    print(f"nested_tuple[1][2] = {nested_tuple[1][2]}")
    print(f"nested_tuple[2][-1] = {nested_tuple[2][-1]}")
    
    # 复杂嵌套结构
    complex_nested = (("a", "b"), (1, 2, 3), (["x", "y"], "z"))
    print(f"\ncomplex_nested = {complex_nested}")
    print(f"complex_nested[0][1] = {complex_nested[0][1]}")
    print(f"complex_nested[2][0][1] = {complex_nested[2][0][1]}")

def demonstrate_index_errors():
    """演示索引错误处理"""
    print("\n=" * 30)
    print("索引错误处理演示")
    print("=" * 30)
    
    sample_tuple = ("a", "b", "c")
    print(f"sample_tuple = {sample_tuple}")
    print(f"元组长度: {len(sample_tuple)}")
    
    # 正确的索引范围
    print("\n正确的索引范围:")
    print(f"有效正向索引: 0 到 {len(sample_tuple) - 1}")
    print(f"有效负向索引: -{len(sample_tuple)} 到 -1")
    
    # 演示索引错误
    print("\n索引错误示例:")
    try:
        print(sample_tuple[5])  # 超出范围
    except IndexError as e:
        print(f"IndexError: {e}")
    
    try:
        print(sample_tuple[-5])  # 超出范围
    except IndexError as e:
        print(f"IndexError: {e}")
    
    # 安全的索引访问
    print("\n安全的索引访问:")
    index = 5
    if 0 <= index < len(sample_tuple):
        print(f"sample_tuple[{index}] = {sample_tuple[index]}")
    else:
        print(f"索引 {index} 超出范围")

def demonstrate_practical_examples():
    """实际应用示例"""
    print("\n=" * 30)
    print("实际应用示例")
    print("=" * 30)
    
    # 1. 坐标点操作
    print("1. 坐标点操作:")
    point = (3, 4)
    x, y = point[0], point[1]
    print(f"点坐标: {point}")
    print(f"x坐标: {x}, y坐标: {y}")
    print(f"距离原点的距离: {(x**2 + y**2)**0.5:.2f}")
    
    # 2. RGB颜色处理
    print("\n2. RGB颜色处理:")
    colors = (
        (255, 0, 0),    # 红色
        (0, 255, 0),    # 绿色
        (0, 0, 255),    # 蓝色
        (255, 255, 0),  # 黄色
    )
    
    for i, color in enumerate(colors):
        r, g, b = color[0], color[1], color[2]
        print(f"颜色 {i+1}: RGB({r}, {g}, {b})")
    
    # 3. 学生成绩处理
    print("\n3. 学生成绩处理:")
    students = (
        ("张三", 85, 92, 78),
        ("李四", 90, 88, 95),
        ("王五", 78, 85, 82),
    )
    
    print("学生成绩报告:")
    for student in students:
        name = student[0]
        math = student[1]
        english = student[2]
        science = student[3]
        average = (math + english + science) / 3
        print(f"{name}: 数学{math}, 英语{english}, 科学{science}, 平均分{average:.1f}")
    
    # 4. 数据记录查找
    print("\n4. 数据记录查找:")
    records = (
        (1, "Alice", "alice@email.com"),
        (2, "Bob", "bob@email.com"),
        (3, "Charlie", "charlie@email.com"),
    )
    
    # 查找特定用户
    search_name = "Bob"
    for record in records:
        if record[1] == search_name:
            print(f"找到用户: ID={record[0]}, 姓名={record[1]}, 邮箱={record[2]}")
            break
    else:
        print(f"未找到用户: {search_name}")

if __name__ == "__main__":
    main()
    demonstrate_index_errors()
    demonstrate_practical_examples()
    
    print("\n" + "=" * 50)
    print("元组元素访问学习完成！")
    print("下一步：学习元组操作和方法")
    print("=" * 50)