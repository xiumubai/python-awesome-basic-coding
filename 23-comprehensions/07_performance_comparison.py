#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
推导式性能对比 (Performance Comparison)

本模块详细对比推导式与传统循环在不同场景下的性能表现，
帮助开发者理解何时使用推导式，何时使用传统循环。

学习目标：
1. 理解推导式的性能优势
2. 掌握性能测试的方法
3. 了解不同场景下的最佳选择
4. 学会内存使用的对比
5. 理解可读性与性能的平衡
6. 掌握性能优化的技巧
"""

import time
import sys
import gc
import tracemalloc
from functools import wraps
from typing import Callable, Any, List, Dict
import statistics
import random

def performance_timer(func: Callable) -> Callable:
    """性能计时装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        return result, execution_time
    return wrapper

def memory_profiler(func: Callable) -> Callable:
    """内存使用分析装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return result, current, peak
    return wrapper

def run_performance_test(test_name: str, iterations: int = 5):
    """运行性能测试的装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"\n=== {test_name} ===")
            times = []
            
            for i in range(iterations):
                gc.collect()  # 清理垃圾回收
                start_time = time.perf_counter()
                result = func(*args, **kwargs)
                end_time = time.perf_counter()
                times.append(end_time - start_time)
            
            avg_time = statistics.mean(times)
            min_time = min(times)
            max_time = max(times)
            
            print(f"平均时间: {avg_time:.6f}秒")
            print(f"最快时间: {min_time:.6f}秒")
            print(f"最慢时间: {max_time:.6f}秒")
            print(f"标准差: {statistics.stdev(times):.6f}秒")
            
            return result, avg_time
        return wrapper
    return decorator

def basic_list_creation_comparison():
    """基本列表创建性能对比"""
    print("\n" + "=" * 60)
    print("基本列表创建性能对比")
    print("=" * 60)
    
    n = 100000
    
    # 1. 列表推导式 vs for循环
    @run_performance_test("列表推导式 - 简单创建", 5)
    def list_comprehension_simple():
        return [x for x in range(n)]
    
    @run_performance_test("传统for循环 - 简单创建", 5)
    def traditional_loop_simple():
        result = []
        for x in range(n):
            result.append(x)
        return result
    
    @run_performance_test("预分配列表 - 简单创建", 5)
    def preallocated_list_simple():
        result = [None] * n
        for i in range(n):
            result[i] = i
        return result
    
    # 执行测试
    lc_result, lc_time = list_comprehension_simple()
    loop_result, loop_time = traditional_loop_simple()
    pre_result, pre_time = preallocated_list_simple()
    
    # 性能对比
    print(f"\n性能对比:")
    print(f"列表推导式: {lc_time:.6f}秒 (基准)")
    print(f"传统循环: {loop_time:.6f}秒 ({loop_time/lc_time:.2f}x)")
    print(f"预分配列表: {pre_time:.6f}秒 ({pre_time/lc_time:.2f}x)")
    
    # 验证结果一致性
    print(f"结果一致性: {lc_result == loop_result == pre_result}")

def mathematical_operations_comparison():
    """数学运算性能对比"""
    print("\n" + "=" * 60)
    print("数学运算性能对比")
    print("=" * 60)
    
    n = 50000
    
    # 1. 平方运算
    @run_performance_test("列表推导式 - 平方运算", 5)
    def list_comprehension_square():
        return [x**2 for x in range(n)]
    
    @run_performance_test("传统循环 - 平方运算", 5)
    def traditional_loop_square():
        result = []
        for x in range(n):
            result.append(x**2)
        return result
    
    @run_performance_test("map函数 - 平方运算", 5)
    def map_function_square():
        return list(map(lambda x: x**2, range(n)))
    
    # 执行测试
    lc_result, lc_time = list_comprehension_square()
    loop_result, loop_time = traditional_loop_square()
    map_result, map_time = map_function_square()
    
    print(f"\n性能对比:")
    print(f"列表推导式: {lc_time:.6f}秒 (基准)")
    print(f"传统循环: {loop_time:.6f}秒 ({loop_time/lc_time:.2f}x)")
    print(f"map函数: {map_time:.6f}秒 ({map_time/lc_time:.2f}x)")

def filtering_operations_comparison():
    """过滤操作性能对比"""
    print("\n" + "=" * 60)
    print("过滤操作性能对比")
    print("=" * 60)
    
    n = 100000
    data = list(range(n))
    
    # 1. 偶数过滤
    @run_performance_test("列表推导式 - 偶数过滤", 5)
    def list_comprehension_filter():
        return [x for x in data if x % 2 == 0]
    
    @run_performance_test("传统循环 - 偶数过滤", 5)
    def traditional_loop_filter():
        result = []
        for x in data:
            if x % 2 == 0:
                result.append(x)
        return result
    
    @run_performance_test("filter函数 - 偶数过滤", 5)
    def filter_function():
        return list(filter(lambda x: x % 2 == 0, data))
    
    # 执行测试
    lc_result, lc_time = list_comprehension_filter()
    loop_result, loop_time = traditional_loop_filter()
    filter_result, filter_time = filter_function()
    
    print(f"\n性能对比:")
    print(f"列表推导式: {lc_time:.6f}秒 (基准)")
    print(f"传统循环: {loop_time:.6f}秒 ({loop_time/lc_time:.2f}x)")
    print(f"filter函数: {filter_time:.6f}秒 ({filter_time/lc_time:.2f}x)")
    
    print(f"结果数量: {len(lc_result)} (一致性: {len(lc_result) == len(loop_result) == len(filter_result)})")

def nested_loops_comparison():
    """嵌套循环性能对比"""
    print("\n" + "=" * 60)
    print("嵌套循环性能对比")
    print("=" * 60)
    
    n = 200
    
    # 1. 矩阵创建
    @run_performance_test("列表推导式 - 矩阵创建", 3)
    def list_comprehension_matrix():
        return [[i*j for j in range(n)] for i in range(n)]
    
    @run_performance_test("传统嵌套循环 - 矩阵创建", 3)
    def traditional_nested_loop():
        result = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(i*j)
            result.append(row)
        return result
    
    @run_performance_test("预分配矩阵 - 矩阵创建", 3)
    def preallocated_matrix():
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[i][j] = i*j
        return result
    
    # 执行测试
    lc_result, lc_time = list_comprehension_matrix()
    loop_result, loop_time = traditional_nested_loop()
    pre_result, pre_time = preallocated_matrix()
    
    print(f"\n性能对比:")
    print(f"列表推导式: {lc_time:.6f}秒 (基准)")
    print(f"传统嵌套循环: {loop_time:.6f}秒 ({loop_time/lc_time:.2f}x)")
    print(f"预分配矩阵: {pre_time:.6f}秒 ({pre_time/lc_time:.2f}x)")

def dictionary_operations_comparison():
    """字典操作性能对比"""
    print("\n" + "=" * 60)
    print("字典操作性能对比")
    print("=" * 60)
    
    n = 50000
    keys = [f"key_{i}" for i in range(n)]
    values = list(range(n))
    
    # 1. 字典创建
    @run_performance_test("字典推导式 - 创建", 5)
    def dict_comprehension():
        return {k: v for k, v in zip(keys, values)}
    
    @run_performance_test("传统循环 - 字典创建", 5)
    def traditional_dict_loop():
        result = {}
        for k, v in zip(keys, values):
            result[k] = v
        return result
    
    @run_performance_test("dict构造函数 - 创建", 5)
    def dict_constructor():
        return dict(zip(keys, values))
    
    # 执行测试
    dc_result, dc_time = dict_comprehension()
    loop_result, loop_time = traditional_dict_loop()
    dict_result, dict_time = dict_constructor()
    
    print(f"\n性能对比:")
    print(f"字典推导式: {dc_time:.6f}秒 (基准)")
    print(f"传统循环: {loop_time:.6f}秒 ({loop_time/dc_time:.2f}x)")
    print(f"dict构造函数: {dict_time:.6f}秒 ({dict_time/dc_time:.2f}x)")

def memory_usage_comparison():
    """内存使用对比"""
    print("\n" + "=" * 60)
    print("内存使用对比")
    print("=" * 60)
    
    n = 100000
    
    # 1. 列表创建内存使用
    @memory_profiler
    def list_comprehension_memory():
        return [x**2 for x in range(n)]
    
    @memory_profiler
    def traditional_loop_memory():
        result = []
        for x in range(n):
            result.append(x**2)
        return result
    
    @memory_profiler
    def generator_expression_memory():
        return list(x**2 for x in range(n))
    
    # 执行测试
    lc_result, lc_current, lc_peak = list_comprehension_memory()
    loop_result, loop_current, loop_peak = traditional_loop_memory()
    gen_result, gen_current, gen_peak = generator_expression_memory()
    
    print(f"内存使用对比:")
    print(f"列表推导式:")
    print(f"  当前内存: {lc_current / 1024 / 1024:.2f} MB")
    print(f"  峰值内存: {lc_peak / 1024 / 1024:.2f} MB")
    
    print(f"传统循环:")
    print(f"  当前内存: {loop_current / 1024 / 1024:.2f} MB")
    print(f"  峰值内存: {loop_peak / 1024 / 1024:.2f} MB")
    
    print(f"生成器表达式:")
    print(f"  当前内存: {gen_current / 1024 / 1024:.2f} MB")
    print(f"  峰值内存: {gen_peak / 1024 / 1024:.2f} MB")

def generator_vs_list_comparison():
    """生成器与列表性能对比"""
    print("\n" + "=" * 60)
    print("生成器与列表性能对比")
    print("=" * 60)
    
    n = 1000000
    
    # 1. 创建时间对比
    @run_performance_test("列表推导式 - 创建", 3)
    def create_list():
        return [x for x in range(n)]
    
    @run_performance_test("生成器表达式 - 创建", 3)
    def create_generator():
        return (x for x in range(n))
    
    # 2. 迭代时间对比
    test_list = [x for x in range(n)]
    test_gen = (x for x in range(n))
    
    @run_performance_test("列表 - 迭代", 3)
    def iterate_list():
        total = 0
        for x in test_list:
            total += x
        return total
    
    @run_performance_test("生成器 - 迭代", 3)
    def iterate_generator():
        total = 0
        gen = (x for x in range(n))  # 重新创建生成器
        for x in gen:
            total += x
        return total
    
    # 执行测试
    list_result, list_time = create_list()
    gen_result, gen_time = create_generator()
    
    print(f"\n创建时间对比:")
    print(f"列表推导式: {list_time:.6f}秒")
    print(f"生成器表达式: {gen_time:.6f}秒 ({gen_time/list_time:.2f}x)")
    
    iter_list_result, iter_list_time = iterate_list()
    iter_gen_result, iter_gen_time = iterate_generator()
    
    print(f"\n迭代时间对比:")
    print(f"列表迭代: {iter_list_time:.6f}秒")
    print(f"生成器迭代: {iter_gen_time:.6f}秒 ({iter_gen_time/iter_list_time:.2f}x)")

def complex_operations_comparison():
    """复杂操作性能对比"""
    print("\n" + "=" * 60)
    print("复杂操作性能对比")
    print("=" * 60)
    
    # 生成测试数据
    n = 10000
    data = [random.randint(1, 1000) for _ in range(n)]
    
    # 1. 复杂条件过滤和转换
    @run_performance_test("列表推导式 - 复杂操作", 3)
    def complex_list_comprehension():
        return [x**2 + x//2 for x in data if x % 3 == 0 and x > 100]
    
    @run_performance_test("传统循环 - 复杂操作", 3)
    def complex_traditional_loop():
        result = []
        for x in data:
            if x % 3 == 0 and x > 100:
                result.append(x**2 + x//2)
        return result
    
    @run_performance_test("函数式编程 - 复杂操作", 3)
    def complex_functional():
        filtered = filter(lambda x: x % 3 == 0 and x > 100, data)
        return list(map(lambda x: x**2 + x//2, filtered))
    
    # 执行测试
    lc_result, lc_time = complex_list_comprehension()
    loop_result, loop_time = complex_traditional_loop()
    func_result, func_time = complex_functional()
    
    print(f"\n性能对比:")
    print(f"列表推导式: {lc_time:.6f}秒 (基准)")
    print(f"传统循环: {loop_time:.6f}秒 ({loop_time/lc_time:.2f}x)")
    print(f"函数式编程: {func_time:.6f}秒 ({func_time/lc_time:.2f}x)")
    
    print(f"结果一致性: {lc_result == loop_result == func_result}")
    print(f"结果数量: {len(lc_result)}")

def string_operations_comparison():
    """字符串操作性能对比"""
    print("\n" + "=" * 60)
    print("字符串操作性能对比")
    print("=" * 60)
    
    # 生成测试数据
    words = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(3, 10))) 
             for _ in range(10000)]
    
    # 1. 字符串处理
    @run_performance_test("列表推导式 - 字符串处理", 3)
    def string_list_comprehension():
        return [word.upper() for word in words if len(word) > 5 and 'a' in word]
    
    @run_performance_test("传统循环 - 字符串处理", 3)
    def string_traditional_loop():
        result = []
        for word in words:
            if len(word) > 5 and 'a' in word:
                result.append(word.upper())
        return result
    
    # 执行测试
    lc_result, lc_time = string_list_comprehension()
    loop_result, loop_time = string_traditional_loop()
    
    print(f"\n性能对比:")
    print(f"列表推导式: {lc_time:.6f}秒 (基准)")
    print(f"传统循环: {loop_time:.6f}秒 ({loop_time/lc_time:.2f}x)")
    
    print(f"结果一致性: {lc_result == loop_result}")
    print(f"处理结果数量: {len(lc_result)}")

def performance_best_practices():
    """性能最佳实践"""
    print("\n" + "=" * 60)
    print("性能最佳实践")
    print("=" * 60)
    
    n = 50000
    
    print("1. 避免重复计算:")
    
    # 不好的做法：重复计算
    @run_performance_test("重复计算 (不推荐)", 3)
    def bad_repeated_calculation():
        return [len(str(x)) + len(str(x)) for x in range(n)]
    
    # 好的做法：避免重复计算
    @run_performance_test("避免重复计算 (推荐)", 3)
    def good_avoid_repetition():
        return [2 * len(str(x)) for x in range(n)]
    
    bad_result, bad_time = bad_repeated_calculation()
    good_result, good_time = good_avoid_repetition()
    
    print(f"重复计算: {bad_time:.6f}秒")
    print(f"避免重复: {good_time:.6f}秒 (提升 {bad_time/good_time:.2f}x)")
    
    print("\n2. 使用内置函数:")
    
    data = list(range(n))
    
    # 使用内置函数
    @run_performance_test("使用内置函数 sum()", 3)
    def use_builtin_sum():
        return sum(x for x in data if x % 2 == 0)
    
    # 手动累加
    @run_performance_test("手动累加", 3)
    def manual_accumulation():
        total = 0
        for x in data:
            if x % 2 == 0:
                total += x
        return total
    
    builtin_result, builtin_time = use_builtin_sum()
    manual_result, manual_time = manual_accumulation()
    
    print(f"内置函数: {builtin_time:.6f}秒")
    print(f"手动累加: {manual_time:.6f}秒")
    print(f"结果一致: {builtin_result == manual_result}")
    
    print("\n3. 选择合适的数据结构:")
    
    # 集合查找 vs 列表查找
    lookup_data = set(range(0, n, 100))  # 集合
    lookup_list = list(range(0, n, 100))  # 列表
    test_values = [random.randint(0, n) for _ in range(1000)]
    
    @run_performance_test("集合查找", 3)
    def set_lookup():
        return [x for x in test_values if x in lookup_data]
    
    @run_performance_test("列表查找", 3)
    def list_lookup():
        return [x for x in test_values if x in lookup_list]
    
    set_result, set_time = set_lookup()
    list_result, list_time = list_lookup()
    
    print(f"集合查找: {set_time:.6f}秒")
    print(f"列表查找: {list_time:.6f}秒 (慢 {list_time/set_time:.2f}x)")

def readability_vs_performance():
    """可读性与性能的平衡"""
    print("\n" + "=" * 60)
    print("可读性与性能的平衡")
    print("=" * 60)
    
    data = list(range(10000))
    
    print("示例：处理复杂逻辑")
    
    # 高度优化但可读性差
    @run_performance_test("高度优化版本", 3)
    def highly_optimized():
        return [x*x + x//2 - x%3 for x in data if x & 1 and x % 3]
    
    # 可读性好但性能稍差
    @run_performance_test("可读性优先版本", 3)
    def readable_version():
        def is_odd(n):
            return n % 2 == 1
        
        def is_not_divisible_by_3(n):
            return n % 3 != 0
        
        def complex_calculation(n):
            return n * n + n // 2 - n % 3
        
        return [complex_calculation(x) for x in data 
               if is_odd(x) and is_not_divisible_by_3(x)]
    
    # 平衡版本
    @run_performance_test("平衡版本", 3)
    def balanced_version():
        return [x*x + x//2 - x%3 for x in data 
               if x % 2 == 1 and x % 3 != 0]
    
    opt_result, opt_time = highly_optimized()
    read_result, read_time = readable_version()
    bal_result, bal_time = balanced_version()
    
    print(f"\n性能对比:")
    print(f"高度优化: {opt_time:.6f}秒 (基准)")
    print(f"可读性优先: {read_time:.6f}秒 ({read_time/opt_time:.2f}x)")
    print(f"平衡版本: {bal_time:.6f}秒 ({bal_time/opt_time:.2f}x)")
    
    print(f"\n结果一致性: {opt_result == read_result == bal_result}")
    print(f"结果数量: {len(opt_result)}")
    
    print("\n建议:")
    print("- 优先考虑代码可读性和维护性")
    print("- 只在性能瓶颈处进行优化")
    print("- 使用性能分析工具定位真正的瓶颈")
    print("- 平衡版本通常是最好的选择")

def main():
    """主函数"""
    print("Python 推导式性能对比分析")
    print("=" * 80)
    
    # 运行所有性能测试
    basic_list_creation_comparison()
    mathematical_operations_comparison()
    filtering_operations_comparison()
    nested_loops_comparison()
    dictionary_operations_comparison()
    memory_usage_comparison()
    generator_vs_list_comparison()
    complex_operations_comparison()
    string_operations_comparison()
    performance_best_practices()
    readability_vs_performance()
    
    print("\n" + "=" * 80)
    print("性能总结和建议:")
    print("=" * 80)
    
    print("\n1. 推导式的优势:")
    print("   - 通常比传统循环快 10-30%")
    print("   - 代码更简洁，可读性更好")
    print("   - 内存使用更高效")
    print("   - 减少函数调用开销")
    
    print("\n2. 何时使用推导式:")
    print("   - 简单的数据转换和过滤")
    print("   - 创建新的数据结构")
    print("   - 一次性处理数据")
    print("   - 代码逻辑相对简单")
    
    print("\n3. 何时使用传统循环:")
    print("   - 复杂的逻辑处理")
    print("   - 需要中间变量")
    print("   - 错误处理和调试")
    print("   - 可读性比性能更重要")
    
    print("\n4. 性能优化技巧:")
    print("   - 避免重复计算")
    print("   - 使用内置函数")
    print("   - 选择合适的数据结构")
    print("   - 考虑使用生成器表达式")
    print("   - 在性能关键路径上进行优化")
    
    print("\n5. 最佳实践:")
    print("   - 优先考虑代码可读性")
    print("   - 使用性能分析工具")
    print("   - 在实际场景中测试性能")
    print("   - 平衡性能和维护性")

if __name__ == "__main__":
    main()