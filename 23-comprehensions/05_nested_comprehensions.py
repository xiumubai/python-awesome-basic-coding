#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
嵌套推导式 (Nested Comprehensions)

嵌套推导式是指在推导式中包含多个for循环或嵌套的推导式结构。
它们可以用来处理多维数据结构、生成复杂的数据组合，
以及实现多层次的数据转换。

学习目标：
1. 理解嵌套推导式的语法和执行顺序
2. 掌握多维数据结构的处理
3. 学会使用嵌套推导式进行数据展平
4. 了解笛卡尔积和组合生成
5. 掌握复杂条件下的嵌套推导式
6. 理解可读性与性能的平衡
"""

import time
from itertools import product

def demonstrate_basic_nested_syntax():
    """演示嵌套推导式的基本语法"""
    print("=== 嵌套推导式基本语法 ===")
    
    # 基本嵌套语法：[expression for outer in outer_iterable for inner in inner_iterable]
    # 等价于：
    # result = []
    # for outer in outer_iterable:
    #     for inner in inner_iterable:
    #         result.append(expression)
    
    # 简单的嵌套循环
    colors = ['red', 'blue']
    sizes = ['S', 'M', 'L']
    
    # 生成所有颜色和尺寸的组合
    combinations = [(color, size) for color in colors for size in sizes]
    print(f"颜色尺寸组合: {combinations}")
    
    # 等价的传统循环
    traditional = []
    for color in colors:
        for size in sizes:
            traditional.append((color, size))
    print(f"传统循环结果: {traditional}")
    print(f"结果一致: {combinations == traditional}")
    
    # 生成乘法表
    multiplication_table = [(i, j, i*j) for i in range(1, 4) for j in range(1, 4)]
    print(f"\n乘法表: {multiplication_table}")
    
    print()

def demonstrate_matrix_operations():
    """演示矩阵操作的嵌套推导式"""
    print("=== 矩阵操作 ===")
    
    # 创建矩阵
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"原矩阵: {matrix}")
    
    # 1. 矩阵展平
    flattened = [item for row in matrix for item in row]
    print(f"展平矩阵: {flattened}")
    
    # 2. 矩阵转置
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print(f"转置矩阵: {transposed}")
    
    # 3. 矩阵每个元素平方
    squared_matrix = [[item**2 for item in row] for row in matrix]
    print(f"平方矩阵: {squared_matrix}")
    
    # 4. 矩阵条件过滤
    even_elements = [item for row in matrix for item in row if item % 2 == 0]
    print(f"偶数元素: {even_elements}")
    
    # 5. 创建单位矩阵
    size = 4
    identity = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    print(f"\n{size}x{size}单位矩阵:")
    for row in identity:
        print(f"  {row}")
    
    # 6. 创建乘法表矩阵
    mult_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
    print(f"\n5x5乘法表:")
    for row in mult_table:
        print(f"  {row}")
    
    print()

def demonstrate_string_processing():
    """演示字符串处理的嵌套推导式"""
    print("=== 字符串处理 ===")
    
    # 文本数据
    sentences = [
        "Hello world",
        "Python is awesome",
        "Nested comprehensions are powerful"
    ]
    
    # 1. 提取所有单词
    words = [word for sentence in sentences for word in sentence.split()]
    print(f"所有单词: {words}")
    
    # 2. 提取所有字符（除空格）
    chars = [char for sentence in sentences for char in sentence if char != ' ']
    print(f"所有字符: {chars[:20]}...")  # 只显示前20个
    
    # 3. 统计每个句子的单词长度
    word_lengths = [[len(word) for word in sentence.split()] for sentence in sentences]
    print(f"单词长度: {word_lengths}")
    
    # 4. 提取长单词（长度>5）
    long_words = [word for sentence in sentences 
                  for word in sentence.split() if len(word) > 5]
    print(f"长单词: {long_words}")
    
    # 5. 生成首字母缩写
    acronyms = [''.join([word[0].upper() for word in sentence.split()]) 
                for sentence in sentences]
    print(f"首字母缩写: {acronyms}")
    
    # 6. 单词和其位置
    word_positions = [(word, i, j) for i, sentence in enumerate(sentences) 
                      for j, word in enumerate(sentence.split())]
    print(f"单词位置: {word_positions[:5]}...")  # 只显示前5个
    
    print()

def demonstrate_data_structure_processing():
    """演示复杂数据结构的处理"""
    print("=== 复杂数据结构处理 ===")
    
    # 学生数据
    students = [
        {'name': 'Alice', 'grades': [85, 90, 78], 'subjects': ['Math', 'Science', 'English']},
        {'name': 'Bob', 'grades': [92, 88, 95], 'subjects': ['Math', 'Science', 'History']},
        {'name': 'Charlie', 'grades': [78, 85, 82], 'subjects': ['English', 'History', 'Art']}
    ]
    
    # 1. 提取所有成绩
    all_grades = [grade for student in students for grade in student['grades']]
    print(f"所有成绩: {all_grades}")
    
    # 2. 提取所有科目（去重）
    all_subjects = list(set([subject for student in students 
                            for subject in student['subjects']]))
    print(f"所有科目: {sorted(all_subjects)}")
    
    # 3. 学生姓名和平均分
    student_averages = [(student['name'], sum(student['grades'])/len(student['grades'])) 
                       for student in students]
    print(f"学生平均分: {student_averages}")
    
    # 4. 高分成绩（>85）及对应学生
    high_grades = [(student['name'], grade) for student in students 
                   for grade in student['grades'] if grade > 85]
    print(f"高分成绩: {high_grades}")
    
    # 5. 学生-科目组合
    student_subjects = [(student['name'], subject) for student in students 
                       for subject in student['subjects']]
    print(f"学生科目组合: {student_subjects}")
    
    # 6. 创建成绩矩阵
    grade_matrix = [student['grades'] for student in students]
    print(f"\n成绩矩阵:")
    for i, row in enumerate(grade_matrix):
        print(f"  {students[i]['name']}: {row}")
    
    print()

def demonstrate_conditional_nesting():
    """演示带条件的嵌套推导式"""
    print("=== 条件嵌套推导式 ===")
    
    # 数据集
    data = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    
    # 1. 提取偶数且大于5的元素
    filtered_elements = [item for row in data for item in row 
                        if item % 2 == 0 and item > 5]
    print(f"偶数且>5: {filtered_elements}")
    
    # 2. 每行的偶数
    even_by_row = [[item for item in row if item % 2 == 0] for row in data]
    print(f"每行偶数: {even_by_row}")
    
    # 3. 非空行的第一个元素
    first_elements = [row[0] for row in data if row]  # 防止空行
    print(f"每行第一个元素: {first_elements}")
    
    # 4. 条件矩阵变换
    transformed = [[item*2 if item % 2 == 0 else item*3 for item in row] 
                  for row in data]
    print(f"条件变换: {transformed}")
    
    # 5. 复杂条件：行索引为偶数且元素为奇数
    complex_filter = [item for i, row in enumerate(data) 
                     for item in row if i % 2 == 0 and item % 2 == 1]
    print(f"复杂条件过滤: {complex_filter}")
    
    # 6. 生成坐标和值的组合
    coordinates = [(i, j, data[i][j]) for i in range(len(data)) 
                  for j in range(len(data[i])) if data[i][j] > 7]
    print(f"大于7的坐标值: {coordinates}")
    
    print()

def demonstrate_cartesian_product():
    """演示笛卡尔积的生成"""
    print("=== 笛卡尔积生成 ===")
    
    # 基本笛卡尔积
    letters = ['A', 'B']
    numbers = [1, 2, 3]
    
    # 使用嵌套推导式
    cartesian = [(letter, number) for letter in letters for number in numbers]
    print(f"字母数字组合: {cartesian}")
    
    # 使用itertools.product对比
    cartesian_itertools = list(product(letters, numbers))
    print(f"itertools结果: {cartesian_itertools}")
    print(f"结果一致: {cartesian == cartesian_itertools}")
    
    # 三个集合的笛卡尔积
    colors = ['red', 'blue']
    sizes = ['S', 'M']
    materials = ['cotton', 'silk']
    
    products = [(color, size, material) 
               for color in colors 
               for size in sizes 
               for material in materials]
    print(f"\n产品组合: {products}")
    
    # 带条件的笛卡尔积
    valid_combinations = [(color, size, material) 
                         for color in colors 
                         for size in sizes 
                         for material in materials
                         if not (color == 'red' and material == 'silk')]  # 排除红色丝绸
    print(f"有效组合: {valid_combinations}")
    
    # 生成坐标网格
    x_range = range(3)
    y_range = range(3)
    grid = [(x, y) for x in x_range for y in y_range]
    print(f"\n坐标网格: {grid}")
    
    # 生成距离矩阵
    points = [(0, 0), (1, 1), (2, 2)]
    distances = [((x1, y1), (x2, y2), ((x2-x1)**2 + (y2-y1)**2)**0.5)
                for x1, y1 in points for x2, y2 in points if (x1, y1) != (x2, y2)]
    print(f"点距离: {distances[:3]}...")  # 只显示前3个
    
    print()

def demonstrate_performance_considerations():
    """演示性能考虑"""
    print("=== 性能考虑 ===")
    
    # 测试数据
    matrix = [[i*j for j in range(100)] for i in range(100)]
    
    # 1. 嵌套推导式 vs 传统循环
    print("展平大矩阵性能对比:")
    
    # 嵌套推导式
    start_time = time.time()
    flattened_comp = [item for row in matrix for item in row]
    comp_time = time.time() - start_time
    
    # 传统循环
    start_time = time.time()
    flattened_loop = []
    for row in matrix:
        for item in row:
            flattened_loop.append(item)
    loop_time = time.time() - start_time
    
    print(f"推导式: {comp_time:.4f}秒")
    print(f"传统循环: {loop_time:.4f}秒")
    print(f"结果一致: {flattened_comp == flattened_loop}")
    
    # 2. 内存使用对比
    import sys
    
    # 列表推导式
    list_comp = [item for row in matrix for item in row]
    list_size = sys.getsizeof(list_comp)
    
    # 生成器表达式
    gen_exp = (item for row in matrix for item in row)
    gen_size = sys.getsizeof(gen_exp)
    
    print(f"\n内存使用:")
    print(f"列表推导式: {list_size:,} 字节")
    print(f"生成器表达式: {gen_size:,} 字节")
    print(f"内存节省: {(list_size - gen_size) / list_size * 100:.1f}%")
    
    # 清理内存
    del flattened_comp, flattened_loop, list_comp, gen_exp
    print()

def demonstrate_readability_vs_complexity():
    """演示可读性与复杂性的平衡"""
    print("=== 可读性与复杂性平衡 ===")
    
    # 复杂数据
    data = [
        {'users': [{'name': 'Alice', 'scores': [85, 90]}, {'name': 'Bob', 'scores': [78, 82]}]},
        {'users': [{'name': 'Charlie', 'scores': [92, 88]}, {'name': 'Diana', 'scores': [95, 91]}]}
    ]
    
    # ❌ 过于复杂的嵌套推导式（不推荐）
    print("❌ 过于复杂的嵌套推导式:")
    complex_result = [score for group in data for user in group['users'] 
                     for score in user['scores'] if score > 85]
    print(f"高分: {complex_result}")
    
    # ✅ 更清晰的分步处理（推荐）
    print("\n✅ 清晰的分步处理:")
    all_users = [user for group in data for user in group['users']]
    all_scores = [score for user in all_users for score in user['scores']]
    high_scores = [score for score in all_scores if score > 85]
    print(f"高分: {high_scores}")
    
    # ✅ 使用函数分解复杂逻辑（最推荐）
    print("\n✅ 使用函数分解:")
    def extract_high_scores(data, threshold=85):
        """提取高分成绩"""
        users = [user for group in data for user in group['users']]
        scores = [score for user in users for score in user['scores']]
        return [score for score in scores if score > threshold]
    
    result = extract_high_scores(data)
    print(f"高分: {result}")
    
    # 可读性指导原则
    print("\n可读性指导原则:")
    print("1. 嵌套层数不超过2-3层")
    print("2. 每行长度控制在80字符以内")
    print("3. 复杂逻辑使用函数分解")
    print("4. 添加适当的注释说明")
    print("5. 考虑使用传统循环提高可读性")
    
    print()

def demonstrate_common_patterns():
    """演示常见的嵌套推导式模式"""
    print("=== 常见模式 ===")
    
    # 1. 矩阵操作模式
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # 展平
    flatten = [item for row in matrix for item in row]
    print(f"展平: {flatten}")
    
    # 转置
    transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print(f"转置: {transpose}")
    
    # 2. 组合生成模式
    items = ['a', 'b', 'c']
    pairs = [(x, y) for x in items for y in items if x != y]
    print(f"\n不重复配对: {pairs}")
    
    # 3. 过滤聚合模式
    groups = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    group_sums = [sum(group) for group in groups]
    print(f"\n组求和: {group_sums}")
    
    # 4. 条件映射模式
    numbers = range(1, 11)
    categorized = [('even', x) if x % 2 == 0 else ('odd', x) for x in numbers]
    print(f"\n分类: {categorized}")
    
    # 5. 嵌套字典处理模式
    nested_dict = {
        'group1': {'a': 1, 'b': 2},
        'group2': {'c': 3, 'd': 4}
    }
    
    # 提取所有值
    all_values = [value for group in nested_dict.values() 
                 for value in group.values()]
    print(f"\n所有值: {all_values}")
    
    # 提取键值对
    all_pairs = [(key, value) for group in nested_dict.values() 
                for key, value in group.items()]
    print(f"所有键值对: {all_pairs}")
    
    print()

def main():
    """主函数"""
    print("Python 嵌套推导式详解\n")
    print("=" * 50)
    
    demonstrate_basic_nested_syntax()
    demonstrate_matrix_operations()
    demonstrate_string_processing()
    demonstrate_data_structure_processing()
    demonstrate_conditional_nesting()
    demonstrate_cartesian_product()
    demonstrate_performance_considerations()
    demonstrate_readability_vs_complexity()
    demonstrate_common_patterns()
    
    print("学习要点总结:")
    print("1. 嵌套推导式语法：[expr for outer in outer_iter for inner in inner_iter]")
    print("2. 执行顺序：外层循环在前，内层循环在后")
    print("3. 适合处理多维数据结构和矩阵操作")
    print("4. 可以生成笛卡尔积和复杂组合")
    print("5. 支持多层条件过滤")
    print("6. 注意可读性与复杂性的平衡")
    print("7. 复杂逻辑建议使用函数分解")
    print("8. 考虑性能和内存使用")

if __name__ == "__main__":
    main()