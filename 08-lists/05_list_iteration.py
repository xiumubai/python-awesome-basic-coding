#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
列表遍历 - 列表遍历的各种方式

本文件演示了Python中遍历列表的各种方法：
1. 基本的for循环遍历
2. 使用索引遍历
3. 使用enumerate()函数
4. 使用zip()函数同时遍历多个列表
5. 反向遍历和条件遍历
6. 嵌套列表的遍历

作者：Python学习教程
日期：2024年
"""

def demonstrate_basic_iteration():
    """演示基本的遍历方法"""
    print("=== 基本遍历方法 ===")
    
    fruits = ['apple', 'banana', 'orange', 'grape']
    print(f"水果列表: {fruits}")
    
    # 1. 直接遍历元素
    print("\n直接遍历元素:")
    for fruit in fruits:
        print(f"  {fruit}")
    
    # 2. 使用while循环遍历
    print("\n使用while循环:")
    i = 0
    while i < len(fruits):
        print(f"  索引{i}: {fruits[i]}")
        i += 1
    
    # 3. 使用range()和len()遍历
    print("\n使用range()和len():")
    for i in range(len(fruits)):
        print(f"  索引{i}: {fruits[i]}")

def demonstrate_enumerate_iteration():
    """演示使用enumerate()的遍历"""
    print("\n=== 使用enumerate()遍历 ===")
    
    colors = ['red', 'green', 'blue', 'yellow']
    print(f"颜色列表: {colors}")
    
    # 基本enumerate用法
    print("\n基本enumerate用法:")
    for index, color in enumerate(colors):
        print(f"  索引{index}: {color}")
    
    # 指定起始索引
    print("\n指定起始索引为1:")
    for index, color in enumerate(colors, 1):
        print(f"  第{index}个颜色: {color}")
    
    # enumerate在实际应用中的使用
    print("\n实际应用 - 查找特定元素的所有位置:")
    numbers = [1, 3, 2, 3, 4, 3, 5]
    target = 3
    positions = []
    
    for index, number in enumerate(numbers):
        if number == target:
            positions.append(index)
    
    print(f"数字列表: {numbers}")
    print(f"数字{target}的所有位置: {positions}")

def demonstrate_zip_iteration():
    """演示使用zip()同时遍历多个列表"""
    print("\n=== 使用zip()同时遍历多个列表 ===")
    
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    cities = ['New York', 'London', 'Tokyo']
    
    print(f"姓名: {names}")
    print(f"年龄: {ages}")
    print(f"城市: {cities}")
    
    # 基本zip用法
    print("\n基本zip用法:")
    for name, age, city in zip(names, ages, cities):
        print(f"  {name}, {age}岁, 住在{city}")
    
    # 不同长度的列表
    scores1 = [85, 90, 78]
    scores2 = [88, 92]  # 较短的列表
    
    print(f"\n不同长度列表的zip:")
    print(f"成绩1: {scores1}")
    print(f"成绩2: {scores2}")
    
    for i, (s1, s2) in enumerate(zip(scores1, scores2)):
        print(f"  学生{i+1}: 成绩1={s1}, 成绩2={s2}")
    
    # 使用zip创建字典
    print("\n使用zip创建字典:")
    person_dict = dict(zip(['name', 'age', 'city'], ['David', 28, 'Paris']))
    print(f"  人员信息: {person_dict}")
    
    # zip的逆操作 - 解压
    print("\n zip的逆操作:")
    pairs = [('a', 1), ('b', 2), ('c', 3)]
    letters, numbers = zip(*pairs)
    print(f"  原始配对: {pairs}")
    print(f"  字母: {letters}")
    print(f"  数字: {numbers}")

def demonstrate_reverse_iteration():
    """演示反向遍历"""
    print("\n=== 反向遍历 ===")
    
    numbers = [1, 2, 3, 4, 5]
    print(f"数字列表: {numbers}")
    
    # 使用reversed()函数
    print("\n使用reversed()函数:")
    for num in reversed(numbers):
        print(f"  {num}")
    
    # 使用切片反转
    print("\n使用切片反转:")
    for num in numbers[::-1]:
        print(f"  {num}")
    
    # 使用负索引遍历
    print("\n使用负索引遍历:")
    for i in range(len(numbers) - 1, -1, -1):
        print(f"  索引{i}: {numbers[i]}")
    
    # 反向enumerate
    print("\n反向enumerate:")
    for index, num in enumerate(reversed(numbers)):
        original_index = len(numbers) - 1 - index
        print(f"  反向索引{index}(原索引{original_index}): {num}")

def demonstrate_conditional_iteration():
    """演示条件遍历"""
    print("\n=== 条件遍历 ===")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"数字列表: {numbers}")
    
    # 遍历偶数
    print("\n遍历偶数:")
    for num in numbers:
        if num % 2 == 0:
            print(f"  偶数: {num}")
    
    # 使用列表推导式过滤后遍历
    print("\n遍历大于5的数:")
    large_numbers = [num for num in numbers if num > 5]
    for num in large_numbers:
        print(f"  大数: {num}")
    
    # 使用filter()函数
    print("\n使用filter()遍历奇数:")
    odd_numbers = filter(lambda x: x % 2 == 1, numbers)
    for num in odd_numbers:
        print(f"  奇数: {num}")
    
    # 条件遍历的实际应用
    students = [
        {'name': 'Alice', 'grade': 85, 'subject': 'Math'},
        {'name': 'Bob', 'grade': 92, 'subject': 'Science'},
        {'name': 'Charlie', 'grade': 78, 'subject': 'Math'},
        {'name': 'Diana', 'grade': 96, 'subject': 'Science'}
    ]
    
    print("\n学生数据条件遍历:")
    print("数学成绩优秀的学生(>=85):")
    for student in students:
        if student['subject'] == 'Math' and student['grade'] >= 85:
            print(f"  {student['name']}: {student['grade']}分")

def demonstrate_nested_iteration():
    """演示嵌套列表的遍历"""
    print("\n=== 嵌套列表遍历 ===")
    
    # 二维列表
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("二维矩阵:")
    for row in matrix:
        print(f"  {row}")
    
    # 遍历所有元素
    print("\n遍历所有元素:")
    for row in matrix:
        for element in row:
            print(f"  {element}", end=' ')
    print()  # 换行
    
    # 使用索引遍历二维列表
    print("\n使用索引遍历:")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"  matrix[{i}][{j}] = {matrix[i][j]}")
    
    # 使用enumerate遍历二维列表
    print("\n使用enumerate遍历:")
    for row_idx, row in enumerate(matrix):
        for col_idx, element in enumerate(row):
            print(f"  位置({row_idx},{col_idx}): {element}")
    
    # 三维列表
    cube = [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ]
    
    print("\n三维列表遍历:")
    for i, plane in enumerate(cube):
        for j, row in enumerate(plane):
            for k, element in enumerate(row):
                print(f"  cube[{i}][{j}][{k}] = {element}")
    
    # 不规则嵌套列表
    irregular = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]
    print(f"\n不规则嵌套列表: {irregular}")
    print("遍历结果:")
    for i, sublist in enumerate(irregular):
        print(f"  子列表{i} (长度{len(sublist)}): ", end='')
        for element in sublist:
            print(f"{element} ", end='')
        print()  # 换行

def demonstrate_advanced_iteration_patterns():
    """演示高级遍历模式"""
    print("\n=== 高级遍历模式 ===")
    
    # 1. 分组遍历
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    group_size = 3
    
    print(f"原列表: {numbers}")
    print(f"按{group_size}个元素分组:")
    
    for i in range(0, len(numbers), group_size):
        group = numbers[i:i + group_size]
        print(f"  组{i//group_size + 1}: {group}")
    
    # 2. 滑动窗口遍历
    print("\n滑动窗口遍历(窗口大小3):")
    window_size = 3
    for i in range(len(numbers) - window_size + 1):
        window = numbers[i:i + window_size]
        print(f"  窗口{i+1}: {window}")
    
    # 3. 配对遍历
    print("\n相邻元素配对:")
    for i in range(len(numbers) - 1):
        pair = (numbers[i], numbers[i + 1])
        print(f"  配对{i+1}: {pair}")
    
    # 4. 使用itertools进行高级遍历
    import itertools
    
    # 排列组合
    letters = ['A', 'B', 'C']
    print(f"\n字母列表: {letters}")
    
    print("所有2元素排列:")
    for perm in itertools.permutations(letters, 2):
        print(f"  {perm}")
    
    print("所有2元素组合:")
    for comb in itertools.combinations(letters, 2):
        print(f"  {comb}")
    
    # 5. 多层嵌套的扁平化遍历
    nested_list = [[1, 2], [3, [4, 5]], [6, 7, [8, [9, 10]]]]
    
    def flatten_and_iterate(lst):
        """递归扁平化并遍历嵌套列表"""
        for item in lst:
            if isinstance(item, list):
                yield from flatten_and_iterate(item)
            else:
                yield item
    
    print(f"\n嵌套列表: {nested_list}")
    print("扁平化遍历结果:")
    for item in flatten_and_iterate(nested_list):
        print(f"  {item}")

def demonstrate_iteration_performance():
    """演示不同遍历方法的性能考虑"""
    print("\n=== 遍历性能考虑 ===")
    
    import time
    
    # 创建大列表进行性能测试
    large_list = list(range(100000))
    
    def time_iteration(func, description):
        """测量遍历时间"""
        start_time = time.time()
        result = func(large_list)
        end_time = time.time()
        print(f"{description}: {end_time - start_time:.4f}秒, 结果: {result}")
    
    # 不同遍历方法的性能比较
    def method1(lst):
        """直接遍历"""
        count = 0
        for item in lst:
            if item % 2 == 0:
                count += 1
        return count
    
    def method2(lst):
        """索引遍历"""
        count = 0
        for i in range(len(lst)):
            if lst[i] % 2 == 0:
                count += 1
        return count
    
    def method3(lst):
        """enumerate遍历"""
        count = 0
        for i, item in enumerate(lst):
            if item % 2 == 0:
                count += 1
        return count
    
    def method4(lst):
        """列表推导式"""
        return len([x for x in lst if x % 2 == 0])
    
    def method5(lst):
        """生成器表达式"""
        return sum(1 for x in lst if x % 2 == 0)
    
    print("计算偶数个数的不同方法性能比较:")
    time_iteration(method1, "直接遍历")
    time_iteration(method2, "索引遍历")
    time_iteration(method3, "enumerate遍历")
    time_iteration(method4, "列表推导式")
    time_iteration(method5, "生成器表达式")
    
    print("\n性能建议:")
    print("- 直接遍历通常最快")
    print("- 避免不必要的索引访问")
    print("- 生成器表达式内存效率高")
    print("- 列表推导式适合创建新列表")

def main():
    """主函数，演示所有遍历方法"""
    print("Python列表遍历方法大全")
    print("=" * 50)
    
    demonstrate_basic_iteration()
    demonstrate_enumerate_iteration()
    demonstrate_zip_iteration()
    demonstrate_reverse_iteration()
    demonstrate_conditional_iteration()
    demonstrate_nested_iteration()
    demonstrate_advanced_iteration_patterns()
    demonstrate_iteration_performance()
    
    print("\n=== 总结 ===")
    print("列表遍历的主要方法:")
    print("\n基本遍历:")
    print("- for item in list: 直接遍历元素")
    print("- for i in range(len(list)): 索引遍历")
    print("- while循环: 条件控制遍历")
    print("\n高级遍历:")
    print("- enumerate(list): 同时获取索引和元素")
    print("- zip(list1, list2): 同时遍历多个列表")
    print("- reversed(list): 反向遍历")
    print("- filter(func, list): 条件过滤遍历")
    print("\n嵌套遍历:")
    print("- 多层for循环: 遍历多维列表")
    print("- 递归遍历: 处理不规则嵌套")
    print("\n性能提示:")
    print("- 直接遍历通常最快")
    print("- 使用生成器节省内存")
    print("- 避免不必要的索引计算")

if __name__ == "__main__":
    main()