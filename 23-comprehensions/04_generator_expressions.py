#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成器表达式 (Generator Expressions)

生成器表达式是一种内存高效的方式来创建生成器对象。
它们使用类似列表推导式的语法，但使用圆括号而不是方括号。
生成器表达式是惰性求值的，只在需要时才计算值。

学习目标：
1. 理解生成器表达式的基本语法
2. 掌握生成器的惰性求值特性
3. 学会在不同场景中使用生成器表达式
4. 了解生成器表达式的内存优势
5. 掌握生成器的迭代和消费方式
"""

import sys
import time
from itertools import islice

def demonstrate_basic_syntax():
    """演示生成器表达式的基本语法"""
    print("=== 生成器表达式基本语法 ===")
    
    # 基本语法：(expression for item in iterable)
    numbers = [1, 2, 3, 4, 5]
    
    # 创建生成器表达式
    squares_gen = (x**2 for x in numbers)
    print(f"生成器对象: {squares_gen}")
    print(f"生成器类型: {type(squares_gen)}")
    
    # 消费生成器
    print("平方数:", list(squares_gen))
    
    # 注意：生成器只能消费一次
    print("再次消费（已空）:", list(squares_gen))
    
    # 重新创建生成器
    squares_gen = (x**2 for x in numbers)
    print("重新创建后:", list(squares_gen))
    
    print()

def demonstrate_lazy_evaluation():
    """演示生成器的惰性求值特性"""
    print("=== 惰性求值演示 ===")
    
    def expensive_function(x):
        """模拟耗时操作"""
        print(f"  正在处理 {x}...")
        time.sleep(0.1)  # 模拟耗时
        return x * 2
    
    # 创建生成器（不会立即执行函数）
    print("创建生成器表达式...")
    gen = (expensive_function(x) for x in range(3))
    print("生成器已创建，但函数还未执行")
    
    # 只有在迭代时才会执行
    print("\n开始迭代:")
    for value in gen:
        print(f"  得到值: {value}")
    
    print()

def demonstrate_memory_efficiency():
    """演示生成器表达式的内存效率"""
    print("=== 内存效率对比 ===")
    
    # 大数据集
    n = 1000000
    
    # 列表推导式（占用大量内存）
    print("创建列表推导式...")
    list_comp = [x**2 for x in range(n)]
    list_size = sys.getsizeof(list_comp)
    print(f"列表大小: {list_size:,} 字节")
    
    # 生成器表达式（占用很少内存）
    print("\n创建生成器表达式...")
    gen_exp = (x**2 for x in range(n))
    gen_size = sys.getsizeof(gen_exp)
    print(f"生成器大小: {gen_size:,} 字节")
    
    print(f"\n内存节省: {(list_size - gen_size) / list_size * 100:.1f}%")
    
    # 清理内存
    del list_comp
    del gen_exp
    print()

def demonstrate_conditional_generators():
    """演示带条件的生成器表达式"""
    print("=== 条件生成器表达式 ===")
    
    numbers = range(1, 21)
    
    # 偶数的平方
    even_squares = (x**2 for x in numbers if x % 2 == 0)
    print("偶数的平方:", list(even_squares))
    
    # 质数生成器
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = (x for x in range(2, 50) if is_prime(x))
    print("50以内的质数:", list(primes))
    
    # 字符串处理
    words = ['hello', 'world', 'python', 'generator', 'expression']
    long_words = (word.upper() for word in words if len(word) > 5)
    print("长单词（大写）:", list(long_words))
    
    print()

def demonstrate_nested_generators():
    """演示嵌套生成器表达式"""
    print("=== 嵌套生成器表达式 ===")
    
    # 矩阵展平
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = (item for row in matrix for item in row)
    print("展平矩阵:", list(flattened))
    
    # 笛卡尔积
    colors = ['red', 'blue']
    sizes = ['S', 'M', 'L']
    combinations = ((color, size) for color in colors for size in sizes)
    print("颜色尺寸组合:", list(combinations))
    
    # 条件嵌套
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    even_items = (item for row in matrix for item in row if item % 2 == 0)
    print("矩阵中的偶数:", list(even_items))
    
    print()

def demonstrate_generator_methods():
    """演示生成器的方法和操作"""
    print("=== 生成器方法和操作 ===")
    
    # 使用next()函数
    gen = (x**2 for x in range(5))
    print("使用next()逐个获取:")
    print(f"第一个值: {next(gen)}")
    print(f"第二个值: {next(gen)}")
    print(f"剩余值: {list(gen)}")
    
    # 使用islice获取部分元素
    gen = (x**2 for x in range(100))
    first_five = list(islice(gen, 5))
    print(f"\n前5个平方数: {first_five}")
    
    # 生成器表达式作为函数参数
    numbers = range(1, 11)
    total = sum(x**2 for x in numbers)
    print(f"\n1-10平方和: {total}")
    
    # 检查生成器是否为空
    gen = (x for x in [] if x > 0)
    try:
        first_value = next(gen)
        print(f"第一个值: {first_value}")
    except StopIteration:
        print("生成器为空")
    
    print()

def demonstrate_practical_applications():
    """演示生成器表达式的实际应用"""
    print("=== 实际应用场景 ===")
    
    # 1. 文件处理（模拟）
    log_lines = [
        "2024-01-01 10:00:00 INFO User login",
        "2024-01-01 10:01:00 ERROR Database connection failed",
        "2024-01-01 10:02:00 INFO User logout",
        "2024-01-01 10:03:00 WARNING Low memory",
        "2024-01-01 10:04:00 ERROR File not found"
    ]
    
    # 提取错误日志
    error_logs = (line for line in log_lines if 'ERROR' in line)
    print("错误日志:")
    for log in error_logs:
        print(f"  {log}")
    
    # 2. 数据转换管道
    raw_data = ['  123  ', '  456  ', '  789  ', '  abc  ']
    
    # 清理并转换数据
    cleaned_numbers = (int(item.strip()) for item in raw_data 
                      if item.strip().isdigit())
    print(f"\n清理后的数字: {list(cleaned_numbers)}")
    
    # 3. 配置文件解析（模拟）
    config_lines = [
        "# 这是注释",
        "host=localhost",
        "port=8080",
        "",  # 空行
        "debug=true",
        "# 另一个注释"
    ]
    
    # 解析配置
    config_pairs = (line.split('=') for line in config_lines 
                   if line and not line.startswith('#') and '=' in line)
    config_dict = {key.strip(): value.strip() for key, value in config_pairs}
    print(f"\n配置字典: {config_dict}")
    
    # 4. 数学序列生成
    # 斐波那契数列（前10项）
    def fibonacci_gen(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
    
    fib_squares = (x**2 for x in fibonacci_gen(10))
    print(f"\n斐波那契数列平方: {list(fib_squares)}")
    
    print()

def demonstrate_performance_comparison():
    """演示生成器表达式与其他方法的性能对比"""
    print("=== 性能对比 ===")
    
    n = 100000
    
    # 测试内存使用
    print("内存使用对比:")
    
    # 列表推导式
    start_time = time.time()
    list_comp = [x**2 for x in range(n)]
    list_time = time.time() - start_time
    list_memory = sys.getsizeof(list_comp)
    
    # 生成器表达式
    start_time = time.time()
    gen_exp = (x**2 for x in range(n))
    gen_time = time.time() - start_time
    gen_memory = sys.getsizeof(gen_exp)
    
    print(f"列表推导式: {list_time:.4f}秒, {list_memory:,}字节")
    print(f"生成器表达式: {gen_time:.4f}秒, {gen_memory:,}字节")
    
    # 测试迭代性能
    print("\n迭代性能对比:")
    
    # 列表迭代
    start_time = time.time()
    total1 = sum(list_comp)
    list_iter_time = time.time() - start_time
    
    # 生成器迭代
    start_time = time.time()
    total2 = sum(gen_exp)
    gen_iter_time = time.time() - start_time
    
    print(f"列表迭代: {list_iter_time:.4f}秒, 总和: {total1}")
    print(f"生成器迭代: {gen_iter_time:.4f}秒, 总和: {total2}")
    print(f"结果一致: {total1 == total2}")
    
    # 清理内存
    del list_comp
    del gen_exp
    print()

def demonstrate_common_pitfalls():
    """演示常见错误和注意事项"""
    print("=== 常见错误和注意事项 ===")
    
    # 1. 生成器只能消费一次
    print("❌ 生成器只能消费一次")
    gen = (x**2 for x in range(5))
    print(f"第一次消费: {list(gen)}")
    print(f"第二次消费: {list(gen)}")
    print("解决方案：重新创建生成器或使用tee()")
    
    # 2. 变量作用域问题
    print("\n❌ 变量作用域陷阱")
    generators = []
    for i in range(3):
        # 错误：所有生成器都会使用最后的i值
        generators.append((x + i for x in range(3)))
    
    print("错误结果:")
    for gen in generators:
        print(f"  {list(gen)}")
    
    # 正确做法：使用默认参数捕获变量
    generators = []
    for i in range(3):
        generators.append((x + val for x in range(3) for val in [i]))
    
    print("正确结果:")
    for gen in generators:
        print(f"  {list(gen)}")
    
    # 3. 过早消费生成器
    print("\n❌ 过早消费生成器")
    def process_data(data_gen):
        # 错误：在函数中消费了生成器
        print(f"数据长度: {len(list(data_gen))}")
        return data_gen  # 返回空生成器
    
    gen = (x for x in range(5))
    processed_gen = process_data(gen)
    print(f"处理后的数据: {list(processed_gen)}")
    
    print("\n⚠️ 正确的做法")
    def process_data_correctly(data_gen):
        # 转换为列表或使用tee
        data_list = list(data_gen)
        print(f"数据长度: {len(data_list)}")
        return (x for x in data_list)  # 返回新生成器
    
    gen = (x for x in range(5))
    processed_gen = process_data_correctly(gen)
    print(f"处理后的数据: {list(processed_gen)}")
    
    print()

def main():
    """主函数"""
    print("Python 生成器表达式详解\n")
    print("=" * 50)
    
    demonstrate_basic_syntax()
    demonstrate_lazy_evaluation()
    demonstrate_memory_efficiency()
    demonstrate_conditional_generators()
    demonstrate_nested_generators()
    demonstrate_generator_methods()
    demonstrate_practical_applications()
    demonstrate_performance_comparison()
    demonstrate_common_pitfalls()
    
    print("学习要点总结:")
    print("1. 生成器表达式语法：(expression for item in iterable)")
    print("2. 惰性求值，只在需要时计算值")
    print("3. 内存效率高，适合处理大数据集")
    print("4. 只能迭代一次，消费后需要重新创建")
    print("5. 支持条件过滤和嵌套结构")
    print("6. 可以作为函数参数直接使用")
    print("7. 注意变量作用域和过早消费的问题")
    print("8. 适合数据流处理和管道操作")

if __name__ == "__main__":
    main()