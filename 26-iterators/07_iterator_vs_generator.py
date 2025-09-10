#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
迭代器与生成器对比

本模块详细对比迭代器和生成器的区别、优缺点和使用场景。
生成器是创建迭代器的一种简洁方式，理解两者的关系对于编写高效的Python代码非常重要。

学习目标：
1. 理解迭代器和生成器的区别
2. 掌握生成器的创建方法
3. 学会选择合适的实现方式
4. 了解性能和内存使用差异
"""

import sys
import time
import tracemalloc
from typing import Iterator, Generator

# 1. 基本概念对比
print("=== 1. 基本概念对比 ===")

# 迭代器实现
class NumberIterator:
    """传统迭代器实现"""
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.current
        self.current += 1
        return result

# 生成器函数实现
def number_generator(start, end):
    """生成器函数实现"""
    current = start
    while current < end:
        yield current
        current += 1

# 生成器表达式实现
def create_number_generator_expr(start, end):
    """生成器表达式实现"""
    return (x for x in range(start, end))

print("三种实现方式的对比:")

# 测试三种实现
iterator = NumberIterator(1, 6)
generator_func = number_generator(1, 6)
generator_expr = create_number_generator_expr(1, 6)

print(f"迭代器: {list(iterator)}")
print(f"生成器函数: {list(generator_func)}")
print(f"生成器表达式: {list(generator_expr)}")

# 2. 语法差异
print("\n=== 2. 语法差异 ===")

# 迭代器类 - 需要实现__iter__和__next__
class FibonacciIterator:
    """斐波那契数列迭代器"""
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        
        if self.count == 0:
            self.count += 1
            return self.a
        elif self.count == 1:
            self.count += 1
            return self.b
        else:
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return self.b

# 生成器函数 - 使用yield关键字
def fibonacci_generator(max_count):
    """斐波那契数列生成器"""
    count = 0
    a, b = 0, 1
    
    while count < max_count:
        if count == 0:
            yield a
        elif count == 1:
            yield b
        else:
            a, b = b, a + b
            yield b
        count += 1

print("斐波那契数列实现对比:")
fib_iter = FibonacciIterator(8)
fib_gen = fibonacci_generator(8)

print(f"迭代器实现: {list(fib_iter)}")
print(f"生成器实现: {list(fib_gen)}")

# 代码行数对比
print("\n代码复杂度对比:")
print(f"迭代器类: 约20行代码")
print(f"生成器函数: 约10行代码")
print(f"代码简化: 50%")

# 3. 内存使用对比
print("\n=== 3. 内存使用对比 ===")

def memory_usage_test():
    """内存使用测试"""
    # 测试大数据集的内存使用
    n = 100000
    
    # 方法1: 列表（立即创建所有元素）
    tracemalloc.start()
    list_data = list(range(n))
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    list_memory = current
    
    # 方法2: 生成器（惰性创建）
    tracemalloc.start()
    gen_data = (x for x in range(n))
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    gen_memory = current
    
    print(f"数据量: {n:,} 个整数")
    print(f"列表内存使用: {list_memory:,} 字节")
    print(f"生成器内存使用: {gen_memory:,} 字节")
    print(f"内存节省: {(list_memory - gen_memory) / list_memory * 100:.1f}%")
    
    # 验证功能相同
    print(f"\n功能验证:")
    print(f"列表前5个: {list_data[:5]}")
    print(f"生成器前5个: {list(x for i, x in enumerate(gen_data) if i < 5)}")

memory_usage_test()

# 4. 性能对比
print("\n=== 4. 性能对比 ===")

def performance_comparison():
    """性能对比测试"""
    n = 50000
    
    # 迭代器类性能
    start_time = time.time()
    iterator = NumberIterator(0, n)
    iter_sum = sum(iterator)
    iter_time = time.time() - start_time
    
    # 生成器函数性能
    start_time = time.time()
    generator = number_generator(0, n)
    gen_sum = sum(generator)
    gen_time = time.time() - start_time
    
    # 生成器表达式性能
    start_time = time.time()
    gen_expr = (x for x in range(n))
    expr_sum = sum(gen_expr)
    expr_time = time.time() - start_time
    
    # 内置range性能
    start_time = time.time()
    range_sum = sum(range(n))
    range_time = time.time() - start_time
    
    print(f"数据量: {n:,}")
    print(f"迭代器类: {iter_time:.6f} 秒, 结果: {iter_sum:,}")
    print(f"生成器函数: {gen_time:.6f} 秒, 结果: {gen_sum:,}")
    print(f"生成器表达式: {expr_time:.6f} 秒, 结果: {expr_sum:,}")
    print(f"内置range: {range_time:.6f} 秒, 结果: {range_sum:,}")
    
    # 性能排名
    times = [('迭代器类', iter_time), ('生成器函数', gen_time), 
             ('生成器表达式', expr_time), ('内置range', range_time)]
    times.sort(key=lambda x: x[1])
    
    print("\n性能排名（从快到慢）:")
    for i, (name, time_taken) in enumerate(times, 1):
        print(f"  {i}. {name}: {time_taken:.6f} 秒")

performance_comparison()

# 5. 状态管理对比
print("\n=== 5. 状态管理对比 ===")

# 迭代器的状态管理
class StatefulIterator:
    """有状态的迭代器"""
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.access_count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        
        self.access_count += 1
        result = self.data[self.index]
        self.index += 1
        return result
    
    def get_stats(self):
        return f"访问次数: {self.access_count}, 当前位置: {self.index}"

# 生成器的状态管理
def stateful_generator(data):
    """有状态的生成器"""
    access_count = 0
    for item in data:
        access_count += 1
        yield item, access_count

print("状态管理对比:")
data = ['a', 'b', 'c', 'd', 'e']

# 迭代器状态
print("\n迭代器状态管理:")
stateful_iter = StatefulIterator(data)
for item in stateful_iter:
    print(f"  项目: {item}, {stateful_iter.get_stats()}")
    if stateful_iter.access_count >= 3:
        break

# 生成器状态
print("\n生成器状态管理:")
stateful_gen = stateful_generator(data)
for item, count in stateful_gen:
    print(f"  项目: {item}, 访问次数: {count}")
    if count >= 3:
        break

# 6. 错误处理对比
print("\n=== 6. 错误处理对比 ===")

# 迭代器错误处理
class SafeIterator:
    """安全的迭代器"""
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            if self.index >= len(self.data):
                raise StopIteration
            
            result = self.data[self.index]
            if result < 0:
                raise ValueError(f"负数不被允许: {result}")
            
            self.index += 1
            return result
        except (IndexError, TypeError) as e:
            raise StopIteration(f"迭代器错误: {e}")

# 生成器错误处理
def safe_generator(data):
    """安全的生成器"""
    try:
        for item in data:
            if item < 0:
                raise ValueError(f"负数不被允许: {item}")
            yield item
    except (TypeError, ValueError) as e:
        print(f"生成器错误: {e}")
        return

print("错误处理对比:")
test_data = [1, 2, -3, 4, 5]

# 迭代器错误处理
print("\n迭代器错误处理:")
try:
    safe_iter = SafeIterator(test_data)
    for item in safe_iter:
        print(f"  处理: {item}")
except StopIteration as e:
    print(f"  迭代停止: {e}")
except ValueError as e:
    print(f"  值错误: {e}")

# 生成器错误处理
print("\n生成器错误处理:")
safe_gen = safe_generator(test_data)
for item in safe_gen:
    print(f"  处理: {item}")

# 7. 复用性对比
print("\n=== 7. 复用性对比 ===")

print("复用性测试:")

# 迭代器复用（需要重新创建）
print("\n迭代器复用:")
iterator = NumberIterator(1, 4)
print(f"第一次使用: {list(iterator)}")
print(f"第二次使用: {list(iterator)}")
print("需要重新创建:")
iterator = NumberIterator(1, 4)
print(f"重新创建后: {list(iterator)}")

# 生成器复用（需要重新调用）
print("\n生成器复用:")
generator = number_generator(1, 4)
print(f"第一次使用: {list(generator)}")
print(f"第二次使用: {list(generator)}")
print("需要重新调用:")
generator = number_generator(1, 4)
print(f"重新调用后: {list(generator)}")

# 8. 适用场景
print("\n=== 8. 适用场景 ===")

print("选择指南:")
print("\n使用迭代器类的场景:")
print("  1. 需要复杂的状态管理")
print("  2. 需要多个方法和属性")
print("  3. 需要继承和多态")
print("  4. 状态需要在迭代过程中被外部访问")

print("\n使用生成器的场景:")
print("  1. 简单的序列生成")
print("  2. 数据流处理")
print("  3. 内存敏感的应用")
print("  4. 快速原型开发")

# 9. 实际应用示例
print("\n=== 9. 实际应用示例 ===")

# 示例1: 文件处理
class FileLineIterator:
    """文件行迭代器（模拟）"""
    def __init__(self, lines):
        self.lines = lines
        self.index = 0
        self.line_count = 0
        self.char_count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.lines):
            raise StopIteration
        
        line = self.lines[self.index]
        self.line_count += 1
        self.char_count += len(line)
        self.index += 1
        return line
    
    def get_statistics(self):
        return {
            'lines_processed': self.line_count,
            'characters_processed': self.char_count,
            'current_position': self.index
        }

def file_line_generator(lines):
    """文件行生成器（模拟）"""
    line_count = 0
    char_count = 0
    
    for line in lines:
        line_count += 1
        char_count += len(line)
        yield line, {'line_number': line_count, 'char_count': char_count}

print("文件处理示例:")
file_lines = ["第一行内容", "第二行内容", "第三行内容"]

# 迭代器方式
print("\n迭代器方式:")
file_iter = FileLineIterator(file_lines)
for line in file_iter:
    print(f"  处理: {line}")
print(f"  统计: {file_iter.get_statistics()}")

# 生成器方式
print("\n生成器方式:")
file_gen = file_line_generator(file_lines)
for line, stats in file_gen:
    print(f"  处理: {line}, 统计: {stats}")

# 示例2: 数据转换管道
print("\n数据转换管道示例:")

# 生成器管道
def data_source():
    """数据源生成器"""
    for i in range(10):
        yield i

def filter_even(data_iter):
    """过滤偶数"""
    for item in data_iter:
        if item % 2 == 0:
            yield item

def square_numbers(data_iter):
    """平方数字"""
    for item in data_iter:
        yield item ** 2

def format_output(data_iter):
    """格式化输出"""
    for item in data_iter:
        yield f"结果: {item}"

# 构建管道
print("生成器管道:")
pipeline = format_output(square_numbers(filter_even(data_source())))
for result in pipeline:
    print(f"  {result}")

# 10. 性能优化建议
print("\n=== 10. 性能优化建议 ===")

def optimization_examples():
    """性能优化示例"""
    data = range(1000)
    
    # 避免：转换为列表
    start_time = time.time()
    result1 = sum([x**2 for x in data if x % 2 == 0])
    time1 = time.time() - start_time
    
    # 推荐：使用生成器表达式
    start_time = time.time()
    result2 = sum(x**2 for x in data if x % 2 == 0)
    time2 = time.time() - start_time
    
    # 推荐：使用生成器函数
    def optimized_generator(data):
        for x in data:
            if x % 2 == 0:
                yield x**2
    
    start_time = time.time()
    result3 = sum(optimized_generator(data))
    time3 = time.time() - start_time
    
    print("性能优化对比:")
    print(f"  列表推导式: {time1:.6f} 秒, 结果: {result1}")
    print(f"  生成器表达式: {time2:.6f} 秒, 结果: {result2}")
    print(f"  生成器函数: {time3:.6f} 秒, 结果: {result3}")
    
    if time1 > time2:
        print(f"  生成器表达式比列表推导式快 {time1/time2:.2f} 倍")

optimization_examples()

if __name__ == "__main__":
    print("\n=== 总结 ===")
    print("1. 生成器是创建迭代器的简洁方式")
    print("2. 生成器在内存使用上更高效")
    print("3. 迭代器类适合复杂状态管理")
    print("4. 生成器适合简单序列和数据流")
    print("5. 选择合适的实现方式很重要")
    print("6. 生成器表达式通常是最佳选择")
    print("7. 避免不必要的列表转换")