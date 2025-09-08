#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
列表元素访问 - 访问列表元素、索引和切片

本文件演示了Python中访问列表元素的各种方法：
1. 使用正索引访问元素
2. 使用负索引访问元素
3. 列表切片操作
4. 多维列表的访问
5. 安全访问方法

作者：Python学习教程
日期：2024年
"""

def demonstrate_basic_indexing():
    """演示基本的索引访问"""
    print("=== 基本索引访问 ===")
    
    fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']
    print(f"水果列表: {fruits}")
    print(f"列表长度: {len(fruits)}")
    
    # 正索引访问
    print("\n正索引访问:")
    for i in range(len(fruits)):
        print(f"索引 {i}: {fruits[i]}")
    
    # 访问第一个和最后一个元素
    print(f"\n第一个元素: {fruits[0]}")
    print(f"最后一个元素: {fruits[len(fruits)-1]}")

def demonstrate_negative_indexing():
    """演示负索引访问"""
    print("\n=== 负索引访问 ===")
    
    numbers = [10, 20, 30, 40, 50]
    print(f"数字列表: {numbers}")
    
    # 负索引访问
    print("\n负索引访问:")
    print(f"索引 -1 (最后一个): {numbers[-1]}")
    print(f"索引 -2 (倒数第二个): {numbers[-2]}")
    print(f"索引 -3 (倒数第三个): {numbers[-3]}")
    print(f"索引 -4 (倒数第四个): {numbers[-4]}")
    print(f"索引 -5 (倒数第五个): {numbers[-5]}")
    
    # 正负索引对比
    print("\n正负索引对比:")
    for i in range(len(numbers)):
        positive_idx = i
        negative_idx = i - len(numbers)
        print(f"正索引 {positive_idx} = 负索引 {negative_idx} = {numbers[i]}")

def demonstrate_slicing():
    """演示列表切片操作"""
    print("\n=== 列表切片操作 ===")
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print(f"字母列表: {letters}")
    
    # 基本切片
    print("\n基本切片:")
    print(f"letters[1:4]: {letters[1:4]}")
    print(f"letters[2:6]: {letters[2:6]}")
    print(f"letters[0:3]: {letters[0:3]}")
    
    # 省略起始或结束索引
    print("\n省略索引的切片:")
    print(f"letters[:3] (从开始到索引3): {letters[:3]}")
    print(f"letters[3:] (从索引3到结束): {letters[3:]}")
    print(f"letters[:] (完整复制): {letters[:]}")
    
    # 使用负索引切片
    print("\n负索引切片:")
    print(f"letters[-3:] (最后3个): {letters[-3:]}")
    print(f"letters[:-2] (除了最后2个): {letters[:-2]}")
    print(f"letters[-5:-2] (倒数第5到倒数第2): {letters[-5:-2]}")

def demonstrate_step_slicing():
    """演示带步长的切片"""
    print("\n=== 带步长的切片 ===")
    
    numbers = list(range(0, 20))
    print(f"数字列表: {numbers}")
    
    # 基本步长切片
    print("\n步长切片:")
    print(f"numbers[::2] (步长2): {numbers[::2]}")
    print(f"numbers[1::2] (从索引1开始，步长2): {numbers[1::2]}")
    print(f"numbers[::3] (步长3): {numbers[::3]}")
    
    # 反向切片
    print("\n反向切片:")
    print(f"numbers[::-1] (完全反转): {numbers[::-1]}")
    print(f"numbers[::-2] (反向，步长2): {numbers[::-2]}")
    print(f"numbers[10:5:-1] (从10到5反向): {numbers[10:5:-1]}")
    
    # 复杂切片示例
    print("\n复杂切片示例:")
    print(f"numbers[2:15:3] (从2到15，步长3): {numbers[2:15:3]}")
    print(f"numbers[15:2:-2] (从15到2反向，步长2): {numbers[15:2:-2]}")

def demonstrate_nested_list_access():
    """演示嵌套列表的访问"""
    print("\n=== 嵌套列表访问 ===")
    
    # 二维列表
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("二维列表:")
    for row in matrix:
        print(row)
    
    # 访问二维列表元素
    print("\n访问二维列表元素:")
    print(f"matrix[0]: {matrix[0]}")
    print(f"matrix[0][0]: {matrix[0][0]}")
    print(f"matrix[1][2]: {matrix[1][2]}")
    print(f"matrix[2][1]: {matrix[2][1]}")
    
    # 访问整行和整列
    print("\n访问行和列:")
    print(f"第一行: {matrix[0]}")
    print(f"第二行: {matrix[1]}")
    print(f"第一列: {[row[0] for row in matrix]}")
    print(f"第二列: {[row[1] for row in matrix]}")
    
    # 三维列表
    cube = [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ]
    
    print("\n三维列表访问:")
    print(f"cube[0]: {cube[0]}")
    print(f"cube[0][1]: {cube[0][1]}")
    print(f"cube[1][0][1]: {cube[1][0][1]}")

def demonstrate_safe_access():
    """演示安全的列表访问方法"""
    print("\n=== 安全访问方法 ===")
    
    data = [1, 2, 3, 4, 5]
    print(f"数据列表: {data}")
    
    # 检查索引是否有效
    def safe_get(lst, index, default=None):
        """安全获取列表元素"""
        try:
            return lst[index]
        except IndexError:
            return default
    
    print("\n安全访问测试:")
    print(f"safe_get(data, 2): {safe_get(data, 2)}")
    print(f"safe_get(data, 10): {safe_get(data, 10)}")
    print(f"safe_get(data, 10, 'Not Found'): {safe_get(data, 10, 'Not Found')}")
    
    # 使用条件检查
    def get_element_if_exists(lst, index):
        """如果索引存在则获取元素"""
        if 0 <= index < len(lst):
            return lst[index]
        else:
            return f"索引 {index} 超出范围 [0, {len(lst)-1}]"
    
    print("\n条件检查访问:")
    print(f"get_element_if_exists(data, 3): {get_element_if_exists(data, 3)}")
    print(f"get_element_if_exists(data, -1): {get_element_if_exists(data, -1)}")
    print(f"get_element_if_exists(data, 10): {get_element_if_exists(data, 10)}")

def demonstrate_advanced_access_patterns():
    """演示高级访问模式"""
    print("\n=== 高级访问模式 ===")
    
    students = [
        {'name': 'Alice', 'age': 20, 'grades': [85, 90, 88]},
        {'name': 'Bob', 'age': 19, 'grades': [78, 85, 92]},
        {'name': 'Charlie', 'age': 21, 'grades': [90, 87, 85]}
    ]
    
    print("学生数据:")
    for student in students:
        print(student)
    
    # 访问复杂数据结构
    print("\n访问复杂数据:")
    print(f"第一个学生的姓名: {students[0]['name']}")
    print(f"第二个学生的第一个成绩: {students[1]['grades'][0]}")
    print(f"最后一个学生的最后一个成绩: {students[-1]['grades'][-1]}")
    
    # 使用列表推导式进行批量访问
    print("\n批量访问:")
    names = [student['name'] for student in students]
    ages = [student['age'] for student in students]
    first_grades = [student['grades'][0] for student in students]
    
    print(f"所有学生姓名: {names}")
    print(f"所有学生年龄: {ages}")
    print(f"所有学生第一门成绩: {first_grades}")
    
    # 条件访问
    adult_students = [student['name'] for student in students if student['age'] >= 20]
    high_performers = [student['name'] for student in students if max(student['grades']) >= 90]
    
    print(f"\n成年学生: {adult_students}")
    print(f"高分学生: {high_performers}")

def demonstrate_common_errors():
    """演示常见的访问错误"""
    print("\n=== 常见访问错误 ===")
    
    test_list = [1, 2, 3, 4, 5]
    print(f"测试列表: {test_list}")
    
    # 演示各种错误情况
    error_cases = [
        ("访问超出范围的正索引", lambda: test_list[10]),
        ("访问超出范围的负索引", lambda: test_list[-10]),
        ("对空列表进行索引访问", lambda: [][0]),
    ]
    
    for description, operation in error_cases:
        try:
            result = operation()
            print(f"{description}: {result}")
        except IndexError as e:
            print(f"{description}: IndexError - {e}")
        except Exception as e:
            print(f"{description}: {type(e).__name__} - {e}")
    
    # 正确的处理方式
    print("\n正确的处理方式:")
    
    def safe_access_demo(lst, index):
        """安全访问演示"""
        if not lst:
            return "列表为空"
        if not isinstance(index, int):
            return "索引必须是整数"
        if index >= len(lst) or index < -len(lst):
            return f"索引 {index} 超出范围"
        return lst[index]
    
    test_cases = [10, -10, 0, -1, 2]
    for index in test_cases:
        result = safe_access_demo(test_list, index)
        print(f"safe_access_demo(test_list, {index}): {result}")

def main():
    """主函数，演示所有列表访问方法"""
    print("Python列表元素访问方法大全")
    print("=" * 50)
    
    demonstrate_basic_indexing()
    demonstrate_negative_indexing()
    demonstrate_slicing()
    demonstrate_step_slicing()
    demonstrate_nested_list_access()
    demonstrate_safe_access()
    demonstrate_advanced_access_patterns()
    demonstrate_common_errors()
    
    print("\n=== 总结 ===")
    print("列表访问的主要方法:")
    print("1. 正索引访问: list[0], list[1], ...")
    print("2. 负索引访问: list[-1], list[-2], ...")
    print("3. 切片访问: list[start:end:step]")
    print("4. 嵌套列表访问: list[i][j][k]")
    print("5. 安全访问: 使用try-except或条件检查")
    print("\n注意事项:")
    print("- 索引从0开始")
    print("- 负索引从-1开始（最后一个元素）")
    print("- 切片不包含结束索引")
    print("- 超出范围会引发IndexError")

if __name__ == "__main__":
    main()