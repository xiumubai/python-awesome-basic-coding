#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
元组与列表的比较 - Tuple vs List Comparison

本文件详细比较了Python中元组和列表的区别：
1. 可变性对比
2. 性能对比
3. 内存使用对比
4. 使用场景对比
5. 方法和操作对比
6. 实际应用建议

作者: Python学习教程
日期: 2024
"""

import sys
import time
from collections import namedtuple

def main():
    print("=" * 50)
    print("元组与列表的比较")
    print("=" * 50)
    
    # 1. 可变性对比
    print("1. 可变性对比:")
    
    # 列表是可变的
    my_list = [1, 2, 3]
    print(f"原始列表: {my_list}")
    my_list[0] = 10  # 可以修改
    my_list.append(4)  # 可以添加
    print(f"修改后列表: {my_list}")
    
    # 元组是不可变的
    my_tuple = (1, 2, 3)
    print(f"\n原始元组: {my_tuple}")
    
    try:
        my_tuple[0] = 10  # 尝试修改会报错
    except TypeError as e:
        print(f"修改元组错误: {e}")
    
    try:
        my_tuple.append(4)  # 元组没有append方法
    except AttributeError as e:
        print(f"元组没有append方法: {e}")
    
    # 2. 创建方式对比
    print("\n2. 创建方式对比:")
    
    # 列表创建
    list1 = [1, 2, 3]
    list2 = list([1, 2, 3])
    list3 = list(range(1, 4))
    
    print(f"列表创建方式:")
    print(f"  直接创建: {list1}")
    print(f"  list()函数: {list2}")
    print(f"  从range: {list3}")
    
    # 元组创建
    tuple1 = (1, 2, 3)
    tuple2 = tuple([1, 2, 3])
    tuple3 = 1, 2, 3  # 可以省略括号
    tuple4 = (1,)  # 单元素元组需要逗号
    
    print(f"\n元组创建方式:")
    print(f"  直接创建: {tuple1}")
    print(f"  tuple()函数: {tuple2}")
    print(f"  省略括号: {tuple3}")
    print(f"  单元素元组: {tuple4}")

def compare_performance():
    """性能对比测试"""
    print("\n=" * 30)
    print("性能对比测试")
    print("=" * 30)
    
    # 1. 创建性能对比
    print("1. 创建性能对比:")
    
    def time_creation(data_type, size=1000000):
        """测试创建时间"""
        start_time = time.time()
        
        if data_type == 'list':
            for _ in range(size):
                data = [1, 2, 3, 4, 5]
        else:  # tuple
            for _ in range(size):
                data = (1, 2, 3, 4, 5)
        
        end_time = time.time()
        return end_time - start_time
    
    # 测试创建时间（使用较小的数量以避免过长等待）
    size = 100000
    list_time = time_creation('list', size)
    tuple_time = time_creation('tuple', size)
    
    print(f"创建{size}次包含5个元素的数据结构:")
    print(f"  列表用时: {list_time:.4f}秒")
    print(f"  元组用时: {tuple_time:.4f}秒")
    print(f"  元组比列表快: {(list_time/tuple_time - 1)*100:.1f}%")
    
    # 2. 访问性能对比
    print("\n2. 访问性能对比:")
    
    large_list = list(range(10000))
    large_tuple = tuple(range(10000))
    
    def time_access(data, iterations=100000):
        """测试访问时间"""
        start_time = time.time()
        
        for _ in range(iterations):
            # 访问中间元素
            value = data[5000]
        
        end_time = time.time()
        return end_time - start_time
    
    iterations = 100000
    list_access_time = time_access(large_list, iterations)
    tuple_access_time = time_access(large_tuple, iterations)
    
    print(f"访问{iterations}次元素:")
    print(f"  列表访问用时: {list_access_time:.4f}秒")
    print(f"  元组访问用时: {tuple_access_time:.4f}秒")
    
    # 3. 遍历性能对比
    print("\n3. 遍历性能对比:")
    
    def time_iteration(data, iterations=1000):
        """测试遍历时间"""
        start_time = time.time()
        
        for _ in range(iterations):
            for item in data:
                pass  # 简单遍历
        
        end_time = time.time()
        return end_time - start_time
    
    iterations = 1000
    list_iter_time = time_iteration(large_list, iterations)
    tuple_iter_time = time_iteration(large_tuple, iterations)
    
    print(f"遍历{iterations}次包含10000个元素的数据:")
    print(f"  列表遍历用时: {list_iter_time:.4f}秒")
    print(f"  元组遍历用时: {tuple_iter_time:.4f}秒")

def compare_memory_usage():
    """内存使用对比"""
    print("\n=" * 30)
    print("内存使用对比")
    print("=" * 30)
    
    # 1. 基本内存使用
    print("1. 基本内存使用:")
    
    # 创建相同内容的列表和元组
    data = list(range(1000))
    my_list = data.copy()
    my_tuple = tuple(data)
    
    list_size = sys.getsizeof(my_list)
    tuple_size = sys.getsizeof(my_tuple)
    
    print(f"包含1000个整数的数据结构:")
    print(f"  列表大小: {list_size} 字节")
    print(f"  元组大小: {tuple_size} 字节")
    print(f"  元组节省: {list_size - tuple_size} 字节 ({(1-tuple_size/list_size)*100:.1f}%)")
    
    # 2. 不同大小的对比
    print("\n2. 不同大小的内存对比:")
    
    sizes = [10, 100, 1000, 10000]
    
    for size in sizes:
        data = list(range(size))
        test_list = data.copy()
        test_tuple = tuple(data)
        
        list_mem = sys.getsizeof(test_list)
        tuple_mem = sys.getsizeof(test_tuple)
        savings = (1 - tuple_mem/list_mem) * 100
        
        print(f"  {size:5d}个元素: 列表{list_mem:6d}字节, 元组{tuple_mem:6d}字节, 节省{savings:4.1f}%")
    
    # 3. 嵌套结构内存对比
    print("\n3. 嵌套结构内存对比:")
    
    # 嵌套列表
    nested_list = [[i, i+1, i+2] for i in range(100)]
    nested_tuple = tuple((i, i+1, i+2) for i in range(100))
    
    nested_list_size = sys.getsizeof(nested_list)
    nested_tuple_size = sys.getsizeof(nested_tuple)
    
    print(f"嵌套结构（100个三元素组）:")
    print(f"  嵌套列表: {nested_list_size} 字节")
    print(f"  嵌套元组: {nested_tuple_size} 字节")
    print(f"  差异: {nested_list_size - nested_tuple_size} 字节")

def compare_methods_and_operations():
    """方法和操作对比"""
    print("\n=" * 30)
    print("方法和操作对比")
    print("=" * 30)
    
    # 1. 可用方法对比
    print("1. 可用方法对比:")
    
    my_list = [1, 2, 3, 2, 4]
    my_tuple = (1, 2, 3, 2, 4)
    
    print("列表独有的方法:")
    list_methods = [method for method in dir(my_list) 
                   if not method.startswith('_') and 
                   not hasattr(my_tuple, method)]
    for method in list_methods:
        print(f"  {method}")
    
    print("\n元组独有的方法:")
    tuple_methods = [method for method in dir(my_tuple) 
                    if not method.startswith('_') and 
                    not hasattr(my_list, method)]
    if tuple_methods:
        for method in tuple_methods:
            print(f"  {method}")
    else:
        print("  (元组没有独有方法)")
    
    print("\n共同的方法:")
    common_methods = [method for method in dir(my_list) 
                     if not method.startswith('_') and 
                     hasattr(my_tuple, method)]
    for method in common_methods:
        print(f"  {method}")
    
    # 2. 操作示例对比
    print("\n2. 操作示例对比:")
    
    # 列表操作
    print("列表操作:")
    my_list = [1, 2, 3]
    print(f"  原始: {my_list}")
    
    my_list.append(4)
    print(f"  append(4): {my_list}")
    
    my_list.insert(1, 1.5)
    print(f"  insert(1, 1.5): {my_list}")
    
    my_list.remove(1.5)
    print(f"  remove(1.5): {my_list}")
    
    popped = my_list.pop()
    print(f"  pop(): {my_list}, 弹出的值: {popped}")
    
    my_list.extend([5, 6])
    print(f"  extend([5, 6]): {my_list}")
    
    my_list.reverse()
    print(f"  reverse(): {my_list}")
    
    my_list.sort()
    print(f"  sort(): {my_list}")
    
    # 元组操作（有限）
    print("\n元组操作:")
    my_tuple = (1, 2, 3, 2, 4)
    print(f"  原始: {my_tuple}")
    print(f"  count(2): {my_tuple.count(2)}")
    print(f"  index(3): {my_tuple.index(3)}")
    
    # 元组的"修改"需要创建新元组
    new_tuple = my_tuple + (5, 6)
    print(f"  连接 + (5, 6): {new_tuple}")
    
    repeated_tuple = my_tuple * 2
    print(f"  重复 * 2: {repeated_tuple}")

def demonstrate_use_cases():
    """使用场景演示"""
    print("\n=" * 30)
    print("使用场景演示")
    print("=" * 30)
    
    # 1. 何时使用元组
    print("1. 何时使用元组:")
    
    # 坐标点（不应该改变）
    point = (3, 4)
    print(f"坐标点: {point}")
    
    # RGB颜色值（固定的三个值）
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    print(f"颜色值: 红{red}, 绿{green}, 蓝{blue}")
    
    # 数据库记录（结构固定）
    user_record = (1, "Alice", "alice@email.com", "2024-01-01")
    print(f"用户记录: {user_record}")
    
    # 函数返回多个值
    def get_name_age():
        return "Bob", 25
    
    name, age = get_name_age()
    print(f"函数返回: 姓名={name}, 年龄={age}")
    
    # 字典的键（需要不可变）
    locations = {
        (0, 0): "原点",
        (1, 1): "右上",
        (-1, -1): "左下"
    }
    print(f"位置字典: {locations}")
    
    # 2. 何时使用列表
    print("\n2. 何时使用列表:")
    
    # 购物车（内容会变化）
    shopping_cart = ["苹果", "香蕉"]
    print(f"购物车: {shopping_cart}")
    shopping_cart.append("橙子")
    print(f"添加商品后: {shopping_cart}")
    
    # 学生成绩（可能增减）
    grades = [85, 92, 78]
    print(f"成绩列表: {grades}")
    grades.append(90)
    grades.sort(reverse=True)
    print(f"添加并排序后: {grades}")
    
    # 待办事项（经常修改）
    todo_list = ["买菜", "洗衣服", "写代码"]
    print(f"待办事项: {todo_list}")
    todo_list.remove("买菜")
    todo_list.insert(0, "开会")
    print(f"更新后: {todo_list}")
    
    # 数据处理（需要各种操作）
    numbers = [1, 5, 3, 9, 2, 8]
    print(f"原始数据: {numbers}")
    numbers.sort()
    print(f"排序后: {numbers}")
    
    # 过滤偶数
    even_numbers = [n for n in numbers if n % 2 == 0]
    print(f"偶数: {even_numbers}")

def demonstrate_conversion():
    """类型转换演示"""
    print("\n=" * 30)
    print("类型转换演示")
    print("=" * 30)
    
    # 1. 列表转元组
    print("1. 列表转元组:")
    
    my_list = [1, 2, 3, 4, 5]
    my_tuple = tuple(my_list)
    
    print(f"原始列表: {my_list}")
    print(f"转换后元组: {my_tuple}")
    print(f"类型: {type(my_list)} -> {type(my_tuple)}")
    
    # 2. 元组转列表
    print("\n2. 元组转列表:")
    
    my_tuple = (1, 2, 3, 4, 5)
    my_list = list(my_tuple)
    
    print(f"原始元组: {my_tuple}")
    print(f"转换后列表: {my_list}")
    print(f"类型: {type(my_tuple)} -> {type(my_list)}")
    
    # 3. 转换的应用场景
    print("\n3. 转换的应用场景:")
    
    # 需要对元组数据进行排序
    coordinates = ((3, 1), (1, 4), (2, 2))
    print(f"原始坐标: {coordinates}")
    
    # 转换为列表进行排序
    sorted_coords = sorted(list(coordinates))
    print(f"排序后列表: {sorted_coords}")
    
    # 转换回元组
    sorted_tuple = tuple(sorted_coords)
    print(f"最终元组: {sorted_tuple}")
    
    # 需要修改元组中的某个值
    person = ("Alice", 25, "Engineer")
    print(f"\n原始人员信息: {person}")
    
    # 转换为列表修改年龄
    person_list = list(person)
    person_list[1] = 26  # 修改年龄
    updated_person = tuple(person_list)
    
    print(f"更新后信息: {updated_person}")

def demonstrate_advanced_comparison():
    """高级对比演示"""
    print("\n=" * 30)
    print("高级对比演示")
    print("=" * 30)
    
    # 1. 作为字典键
    print("1. 作为字典键:")
    
    # 元组可以作为字典键
    coordinate_names = {
        (0, 0): "原点",
        (1, 0): "X轴正方向",
        (0, 1): "Y轴正方向"
    }
    
    print("元组作为字典键:")
    for coord, name in coordinate_names.items():
        print(f"  {coord}: {name}")
    
    # 列表不能作为字典键
    try:
        invalid_dict = {[0, 0]: "原点"}  # 这会报错
    except TypeError as e:
        print(f"\n列表作为字典键错误: {e}")
    
    # 2. 集合元素
    print("\n2. 作为集合元素:")
    
    # 元组可以放入集合
    point_set = {(0, 0), (1, 1), (2, 2)}
    print(f"元组集合: {point_set}")
    
    # 列表不能放入集合
    try:
        invalid_set = {[0, 0], [1, 1]}  # 这会报错
    except TypeError as e:
        print(f"列表作为集合元素错误: {e}")
    
    # 3. 函数参数
    print("\n3. 函数参数传递:")
    
    def process_coordinates(*coords):
        """处理坐标点"""
        print(f"接收到 {len(coords)} 个坐标点:")
        for i, coord in enumerate(coords, 1):
            print(f"  点{i}: {coord}")
    
    # 传递元组
    points = [(0, 0), (1, 1), (2, 2)]
    print("传递元组列表:")
    process_coordinates(*points)
    
    # 4. 命名元组 vs 普通元组 vs 列表
    print("\n4. 命名元组对比:")
    
    # 普通元组
    person_tuple = ("Alice", 25, "Engineer")
    
    # 命名元组
    Person = namedtuple('Person', ['name', 'age', 'job'])
    person_named = Person("Alice", 25, "Engineer")
    
    # 列表
    person_list = ["Alice", 25, "Engineer"]
    
    print(f"普通元组: {person_tuple}")
    print(f"命名元组: {person_named}")
    print(f"列表: {person_list}")
    
    # 访问方式对比
    print("\n访问方式对比:")
    print(f"普通元组姓名: {person_tuple[0]}")
    print(f"命名元组姓名: {person_named.name}")
    print(f"列表姓名: {person_list[0]}")

def provide_recommendations():
    """使用建议"""
    print("\n=" * 30)
    print("使用建议")
    print("=" * 30)
    
    recommendations = [
        ("数据不变性", "如果数据在创建后不需要修改，优先使用元组"),
        ("性能要求", "对性能敏感的场景，元组通常更快且占用内存更少"),
        ("字典键", "需要作为字典键或集合元素时，必须使用元组"),
        ("函数返回值", "函数返回多个值时，使用元组更合适"),
        ("配置数据", "配置信息、常量等不变数据适合用元组"),
        ("数据修改", "需要频繁增删改操作时，使用列表"),
        ("排序过滤", "需要排序、过滤等操作时，列表提供更多方法"),
        ("动态大小", "数据大小会动态变化时，列表更灵活"),
        ("数据处理", "复杂的数据处理和分析，列表更适合"),
        ("用户输入", "处理用户输入的动态数据时，使用列表")
    ]
    
    print("选择建议:")
    for category, advice in recommendations:
        print(f"  {category}: {advice}")
    
    print("\n性能总结:")
    print("  • 元组创建更快")
    print("  • 元组占用内存更少")
    print("  • 元组访问速度略快")
    print("  • 列表提供更多操作方法")
    print("  • 列表支持原地修改")
    
    print("\n最佳实践:")
    print("  • 默认使用列表，除非有特殊需求")
    print("  • 不变数据优先考虑元组")
    print("  • 作为字典键时必须使用元组")
    print("  • 函数返回多值时使用元组")
    print("  • 需要频繁修改时使用列表")

if __name__ == "__main__":
    main()
    compare_performance()
    compare_memory_usage()
    compare_methods_and_operations()
    demonstrate_use_cases()
    demonstrate_conversion()
    demonstrate_advanced_comparison()
    provide_recommendations()
    
    print("\n" + "=" * 50)
    print("元组与列表比较学习完成！")
    print("下一步：完成综合练习")
    print("=" * 50)