#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
嵌套列表 - 嵌套列表和多维列表的操作

本文件演示了Python中嵌套列表的各种操作：
1. 创建和初始化嵌套列表
2. 访问和修改嵌套列表元素
3. 二维列表（矩阵）操作
4. 三维和多维列表
5. 嵌套列表的遍历和处理
6. 实际应用场景和最佳实践

作者：Python学习教程
日期：2024年
"""

def demonstrate_creating_nested_lists():
    """演示创建嵌套列表的各种方法"""
    print("=== 创建嵌套列表 ===")
    
    # 1. 直接创建二维列表
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"直接创建的矩阵: {matrix1}")
    
    # 2. 使用列表推导式创建
    matrix2 = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
    print(f"推导式创建的矩阵: {matrix2}")
    
    # 3. 使用循环创建
    matrix3 = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(i + j)
        matrix3.append(row)
    print(f"循环创建的矩阵: {matrix3}")
    
    # 4. 创建空的嵌套列表
    empty_matrix = [[] for _ in range(3)]
    print(f"空矩阵: {empty_matrix}")
    
    # 5. 错误的创建方式（浅拷贝问题）
    print("\n⚠️ 常见错误 - 浅拷贝问题:")
    wrong_matrix = [[0] * 3] * 3  # 错误方式
    print(f"错误创建的矩阵: {wrong_matrix}")
    wrong_matrix[0][0] = 1
    print(f"修改后的错误矩阵: {wrong_matrix}")
    print("所有行都被修改了！")
    
    # 6. 正确的创建方式
    correct_matrix = [[0] * 3 for _ in range(3)]  # 正确方式
    print(f"\n✓ 正确创建的矩阵: {correct_matrix}")
    correct_matrix[0][0] = 1
    print(f"修改后的正确矩阵: {correct_matrix}")
    print("只有指定行被修改")
    
    # 7. 不规则嵌套列表
    irregular_list = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]
    print(f"\n不规则嵌套列表: {irregular_list}")
    
    # 8. 混合数据类型的嵌套列表
    mixed_list = [['Alice', 25], ['Bob', 30], ['Charlie', 35]]
    print(f"混合数据类型: {mixed_list}")

def demonstrate_accessing_nested_elements():
    """演示访问嵌套列表元素"""
    print("\n=== 访问嵌套列表元素 ===")
    
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    
    print(f"矩阵: {matrix}")
    
    # 1. 基本访问
    print(f"\n第一行: {matrix[0]}")
    print(f"第一行第一列: {matrix[0][0]}")
    print(f"第二行第三列: {matrix[1][2]}")
    print(f"最后一行最后一列: {matrix[-1][-1]}")
    
    # 2. 切片访问
    print(f"\n前两行: {matrix[:2]}")
    print(f"每行的前两列: {[row[:2] for row in matrix]}")
    print(f"第二列: {[row[1] for row in matrix]}")
    
    # 3. 安全访问（避免索引错误）
    def safe_get(matrix, row, col, default=None):
        """安全获取矩阵元素"""
        try:
            return matrix[row][col]
        except (IndexError, TypeError):
            return default
    
    print(f"\n安全访问存在的元素: {safe_get(matrix, 1, 2)}")
    print(f"安全访问不存在的元素: {safe_get(matrix, 10, 10, 'N/A')}")
    
    # 4. 不规则列表的访问
    irregular = [[1, 2], [3, 4, 5], [6]]
    print(f"\n不规则列表: {irregular}")
    
    for i, row in enumerate(irregular):
        for j, element in enumerate(row):
            print(f"  [{i}][{j}] = {element}")
    
    # 5. 深层嵌套访问
    deep_nested = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    print(f"\n深层嵌套: {deep_nested}")
    print(f"访问 [0][1][0]: {deep_nested[0][1][0]}")
    print(f"访问 [1][0][1]: {deep_nested[1][0][1]}")

def demonstrate_modifying_nested_lists():
    """演示修改嵌套列表"""
    print("\n=== 修改嵌套列表 ===")
    
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print(f"原始矩阵: {matrix}")
    
    # 1. 修改单个元素
    matrix[1][1] = 99
    print(f"修改中心元素后: {matrix}")
    
    # 2. 修改整行
    matrix[0] = [10, 20, 30]
    print(f"修改第一行后: {matrix}")
    
    # 3. 修改整列
    for i in range(len(matrix)):
        matrix[i][2] = i * 10
    print(f"修改第三列后: {matrix}")
    
    # 4. 添加行
    matrix.append([40, 50, 60])
    print(f"添加行后: {matrix}")
    
    # 5. 添加列
    for row in matrix:
        row.append(0)
    print(f"添加列后: {matrix}")
    
    # 6. 删除行
    del matrix[0]
    print(f"删除第一行后: {matrix}")
    
    # 7. 删除列
    for row in matrix:
        del row[1]
    print(f"删除第二列后: {matrix}")
    
    # 8. 插入行
    matrix.insert(1, [100, 200, 300])
    print(f"插入行后: {matrix}")
    
    # 9. 批量修改
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= 2
    print(f"所有元素翻倍后: {matrix}")

def demonstrate_matrix_operations():
    """演示矩阵操作"""
    print("\n=== 矩阵操作 ===")
    
    # 创建两个矩阵
    matrix_a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    matrix_b = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    
    print(f"矩阵A: {matrix_a}")
    print(f"矩阵B: {matrix_b}")
    
    # 1. 矩阵加法
    def matrix_add(m1, m2):
        """矩阵加法"""
        result = []
        for i in range(len(m1)):
            row = []
            for j in range(len(m1[i])):
                row.append(m1[i][j] + m2[i][j])
            result.append(row)
        return result
    
    sum_matrix = matrix_add(matrix_a, matrix_b)
    print(f"\n矩阵加法结果: {sum_matrix}")
    
    # 2. 矩阵转置
    def matrix_transpose(matrix):
        """矩阵转置"""
        return [[matrix[j][i] for j in range(len(matrix))] 
                for i in range(len(matrix[0]))]
    
    transposed = matrix_transpose(matrix_a)
    print(f"\n矩阵A转置: {transposed}")
    
    # 3. 矩阵乘法（简单版本）
    def matrix_multiply(m1, m2):
        """矩阵乘法"""
        result = []
        for i in range(len(m1)):
            row = []
            for j in range(len(m2[0])):
                sum_val = 0
                for k in range(len(m2)):
                    sum_val += m1[i][k] * m2[k][j]
                row.append(sum_val)
            result.append(row)
        return result
    
    # 创建适合乘法的矩阵
    matrix_c = [[1, 2], [3, 4], [5, 6]]  # 3x2
    matrix_d = [[7, 8, 9], [10, 11, 12]]  # 2x3
    
    print(f"\n矩阵C (3x2): {matrix_c}")
    print(f"矩阵D (2x3): {matrix_d}")
    
    product = matrix_multiply(matrix_c, matrix_d)
    print(f"矩阵乘法 C×D: {product}")
    
    # 4. 查找矩阵中的最大值和最小值
    def matrix_min_max(matrix):
        """查找矩阵的最大值和最小值"""
        flat = [element for row in matrix for element in row]
        return min(flat), max(flat)
    
    min_val, max_val = matrix_min_max(matrix_a)
    print(f"\n矩阵A的最小值: {min_val}, 最大值: {max_val}")
    
    # 5. 矩阵求和
    def matrix_sum(matrix):
        """计算矩阵所有元素的和"""
        return sum(sum(row) for row in matrix)
    
    total = matrix_sum(matrix_a)
    print(f"矩阵A所有元素的和: {total}")

def demonstrate_three_dimensional_lists():
    """演示三维列表操作"""
    print("\n=== 三维列表操作 ===")
    
    # 1. 创建三维列表（立方体）
    cube = [[[i + j + k for k in range(2)] for j in range(2)] for i in range(2)]
    print(f"2x2x2立方体: {cube}")
    
    # 2. 更直观的三维列表
    classroom = [
        [  # 第一层（第一个班级）
            ['Alice', 'Bob'],      # 第一排
            ['Charlie', 'Diana']   # 第二排
        ],
        [  # 第二层（第二个班级）
            ['Eve', 'Frank'],      # 第一排
            ['Grace', 'Henry']     # 第二排
        ]
    ]
    
    print(f"\n教室布局: {classroom}")
    
    # 3. 访问三维列表元素
    print(f"第一个班级第一排第一个学生: {classroom[0][0][0]}")
    print(f"第二个班级第二排第二个学生: {classroom[1][1][1]}")
    
    # 4. 遍历三维列表
    print("\n遍历所有学生:")
    for class_idx, classroom_class in enumerate(classroom):
        print(f"  班级 {class_idx + 1}:")
        for row_idx, row in enumerate(classroom_class):
            print(f"    第{row_idx + 1}排: {row}")
            for seat_idx, student in enumerate(row):
                print(f"      座位{seat_idx + 1}: {student}")
    
    # 5. 三维列表的实际应用：RGB图像数据
    # 模拟一个2x2像素的RGB图像
    image = [
        [[255, 0, 0], [0, 255, 0]],    # 第一行：红色，绿色
        [[0, 0, 255], [255, 255, 0]]   # 第二行：蓝色，黄色
    ]
    
    print(f"\n2x2 RGB图像数据: {image}")
    print("像素信息:")
    for y in range(len(image)):
        for x in range(len(image[y])):
            r, g, b = image[y][x]
            print(f"  像素({x},{y}): RGB({r},{g},{b})")
    
    # 6. 修改三维列表
    cube[0][0][0] = 999
    print(f"\n修改立方体后: {cube}")
    
    # 7. 三维列表的切片
    print(f"立方体的第一层: {cube[0]}")
    print(f"立方体第一层的第一行: {cube[0][0]}")

def demonstrate_nested_list_traversal():
    """演示嵌套列表的遍历方法"""
    print("\n=== 嵌套列表遍历 ===")
    
    # 复杂的嵌套结构
    complex_nested = [
        [1, 2, [3, 4]],
        [5, [6, 7, [8, 9]]],
        [10, 11, 12]
    ]
    
    print(f"复杂嵌套列表: {complex_nested}")
    
    # 1. 递归遍历
    def recursive_traverse(lst, depth=0):
        """递归遍历嵌套列表"""
        indent = "  " * depth
        for i, item in enumerate(lst):
            if isinstance(item, list):
                print(f"{indent}索引{i}: [列表]")
                recursive_traverse(item, depth + 1)
            else:
                print(f"{indent}索引{i}: {item}")
    
    print("\n递归遍历结果:")
    recursive_traverse(complex_nested)
    
    # 2. 扁平化遍历
    def flatten_list(lst):
        """扁平化嵌套列表"""
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten_list(item))
            else:
                result.append(item)
        return result
    
    flattened = flatten_list(complex_nested)
    print(f"\n扁平化结果: {flattened}")
    
    # 3. 使用生成器扁平化
    def flatten_generator(lst):
        """使用生成器扁平化"""
        for item in lst:
            if isinstance(item, list):
                yield from flatten_generator(item)
            else:
                yield item
    
    gen_flattened = list(flatten_generator(complex_nested))
    print(f"生成器扁平化结果: {gen_flattened}")
    
    # 4. 计算嵌套深度
    def calculate_depth(lst):
        """计算嵌套列表的最大深度"""
        if not isinstance(lst, list):
            return 0
        if not lst:
            return 1
        return 1 + max(calculate_depth(item) for item in lst)
    
    depth = calculate_depth(complex_nested)
    print(f"\n嵌套深度: {depth}")
    
    # 5. 查找特定元素的路径
    def find_path(lst, target, path=[]):
        """查找元素在嵌套列表中的路径"""
        for i, item in enumerate(lst):
            current_path = path + [i]
            if item == target:
                return current_path
            elif isinstance(item, list):
                result = find_path(item, target, current_path)
                if result:
                    return result
        return None
    
    target = 8
    path = find_path(complex_nested, target)
    print(f"\n元素{target}的路径: {path}")
    if path:
        # 验证路径
        value = complex_nested
        for index in path:
            value = value[index]
        print(f"验证路径正确性: {value}")

def demonstrate_practical_applications():
    """演示嵌套列表的实际应用"""
    print("\n=== 实际应用场景 ===")
    
    # 1. 学生成绩管理
    students_grades = [
        ['Alice', [85, 92, 78, 96]],
        ['Bob', [88, 85, 90, 87]],
        ['Charlie', [92, 89, 94, 91]]
    ]
    
    print("学生成绩管理:")
    for student, grades in students_grades:
        average = sum(grades) / len(grades)
        print(f"  {student}: 成绩{grades}, 平均分{average:.1f}")
    
    # 2. 购物车系统
    shopping_cart = [
        ['Electronics', [
            ['Laptop', 1000, 1],
            ['Mouse', 25, 2]
        ]],
        ['Books', [
            ['Python Guide', 30, 1],
            ['Data Science', 45, 1]
        ]]
    ]
    
    print("\n购物车系统:")
    total_cost = 0
    for category, items in shopping_cart:
        print(f"  {category}:")
        category_cost = 0
        for item_name, price, quantity in items:
            item_cost = price * quantity
            category_cost += item_cost
            print(f"    {item_name}: ${price} x {quantity} = ${item_cost}")
        print(f"    {category}小计: ${category_cost}")
        total_cost += category_cost
    print(f"  总计: ${total_cost}")
    
    # 3. 游戏地图
    game_map = [
        ['#', '#', '#', '#', '#'],  # 墙
        ['#', '.', '.', '.', '#'],  # 空地
        ['#', '.', 'P', '.', '#'],  # 玩家位置
        ['#', '.', '.', 'E', '#'],  # 敌人位置
        ['#', '#', '#', '#', '#']   # 墙
    ]
    
    print("\n游戏地图:")
    for row in game_map:
        print('  ' + ' '.join(row))
    
    # 查找玩家和敌人位置
    def find_positions(game_map, symbol):
        """查找地图中特定符号的位置"""
        positions = []
        for y, row in enumerate(game_map):
            for x, cell in enumerate(row):
                if cell == symbol:
                    positions.append((x, y))
        return positions
    
    player_pos = find_positions(game_map, 'P')
    enemy_pos = find_positions(game_map, 'E')
    print(f"  玩家位置: {player_pos}")
    print(f"  敌人位置: {enemy_pos}")
    
    # 4. 数据表格处理
    data_table = [
        ['Name', 'Age', 'City', 'Salary'],
        ['Alice', 25, 'New York', 50000],
        ['Bob', 30, 'London', 60000],
        ['Charlie', 35, 'Tokyo', 70000]
    ]
    
    print("\n数据表格:")
    headers = data_table[0]
    data_rows = data_table[1:]
    
    # 打印表格
    print('  ' + ' | '.join(f"{header:>10}" for header in headers))
    print('  ' + '-' * (len(headers) * 13 - 1))
    for row in data_rows:
        print('  ' + ' | '.join(f"{str(cell):>10}" for cell in row))
    
    # 计算平均工资
    salary_column = 3
    salaries = [row[salary_column] for row in data_rows]
    avg_salary = sum(salaries) / len(salaries)
    print(f"  平均工资: ${avg_salary:,.0f}")

def demonstrate_performance_tips():
    """演示嵌套列表的性能优化技巧"""
    print("\n=== 性能优化技巧 ===")
    
    import time
    
    # 1. 列表推导式 vs 嵌套循环
    size = 100
    
    def nested_loops():
        """使用嵌套循环创建矩阵"""
        result = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(i * j)
            result.append(row)
        return result
    
    def list_comprehension():
        """使用列表推导式创建矩阵"""
        return [[i * j for j in range(size)] for i in range(size)]
    
    # 性能测试
    start_time = time.time()
    matrix1 = nested_loops()
    time1 = time.time() - start_time
    
    start_time = time.time()
    matrix2 = list_comprehension()
    time2 = time.time() - start_time
    
    print(f"创建{size}x{size}矩阵:")
    print(f"  嵌套循环: {time1:.4f}秒")
    print(f"  列表推导式: {time2:.4f}秒")
    print(f"  推导式快了: {time1/time2:.1f}倍")
    
    # 2. 内存使用建议
    print("\n内存使用建议:")
    print("- 避免不必要的深拷贝")
    print("- 使用生成器处理大型嵌套结构")
    print("- 及时删除不需要的嵌套列表")
    
    # 3. 访问模式优化
    print("\n访问模式优化:")
    print("- 按行访问比按列访问更高效")
    print("- 缓存频繁访问的子列表")
    print("- 使用局部变量减少索引查找")
    
    # 演示按行vs按列访问
    matrix = [[i * j for j in range(100)] for i in range(100)]
    
    # 按行访问
    start_time = time.time()
    row_sum = 0
    for row in matrix:
        for element in row:
            row_sum += element
    row_time = time.time() - start_time
    
    # 按列访问
    start_time = time.time()
    col_sum = 0
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            col_sum += matrix[i][j]
    col_time = time.time() - start_time
    
    print(f"\n100x100矩阵求和:")
    print(f"  按行访问: {row_time:.4f}秒")
    print(f"  按列访问: {col_time:.4f}秒")
    print(f"  按行访问快了: {col_time/row_time:.1f}倍")

def main():
    """主函数，演示所有嵌套列表操作"""
    print("Python嵌套列表完全指南")
    print("=" * 50)
    
    demonstrate_creating_nested_lists()
    demonstrate_accessing_nested_elements()
    demonstrate_modifying_nested_lists()
    demonstrate_matrix_operations()
    demonstrate_three_dimensional_lists()
    demonstrate_nested_list_traversal()
    demonstrate_practical_applications()
    demonstrate_performance_tips()
    
    print("\n=== 总结 ===")
    print("嵌套列表关键概念:")
    print("\n创建方法:")
    print("- 直接创建: [[1, 2], [3, 4]]")
    print("- 列表推导式: [[i*j for j in range(3)] for i in range(3)]")
    print("- 避免浅拷贝: 使用 [[] for _ in range(n)]")
    print("\n访问方法:")
    print("- 多重索引: matrix[row][col]")
    print("- 切片操作: matrix[:2] 或 [row[:2] for row in matrix]")
    print("- 安全访问: 使用try-except处理索引错误")
    print("\n遍历方法:")
    print("- 嵌套循环: for row in matrix: for item in row")
    print("- 递归遍历: 处理不规则嵌套")
    print("- 扁平化: 将嵌套结构转为一维")
    print("\n应用场景:")
    print("- 矩阵运算和数学计算")
    print("- 表格数据处理")
    print("- 游戏地图和图像数据")
    print("- 多维数据结构")
    print("\n性能建议:")
    print("- 使用列表推导式提高创建效率")
    print("- 按行访问比按列访问更快")
    print("- 大数据集考虑使用NumPy")
    print("- 避免过深的嵌套层次")

if __name__ == "__main__":
    main()