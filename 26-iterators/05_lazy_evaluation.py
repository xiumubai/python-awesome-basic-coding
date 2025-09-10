#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
迭代器的惰性求值

本模块详细介绍迭代器的惰性求值特性，这是迭代器最重要的特征之一。
惰性求值意味着值只在需要时才计算，这带来了内存效率和性能优势。

学习目标：
1. 理解惰性求值的概念和优势
2. 掌握惰性求值在迭代器中的应用
3. 学会设计惰性求值的迭代器
4. 了解惰性求值与急切求值的区别
"""

import time
import sys
from typing import Iterator, Iterable

# 1. 惰性求值基础概念
print("=== 1. 惰性求值基础概念 ===")

# 急切求值 vs 惰性求值
def eager_squares(n):
    """急切求值 - 立即计算所有平方数"""
    print(f"急切求值: 立即计算前{n}个平方数")
    result = []
    for i in range(n):
        square = i ** 2
        print(f"  计算 {i}^2 = {square}")
        result.append(square)
    return result

def lazy_squares(n):
    """惰性求值 - 按需计算平方数"""
    print(f"惰性求值: 创建前{n}个平方数的迭代器")
    for i in range(n):
        square = i ** 2
        print(f"  按需计算 {i}^2 = {square}")
        yield square

print("急切求值示例:")
eager_result = eager_squares(3)
print(f"结果: {eager_result}")

print("\n惰性求值示例:")
lazy_result = lazy_squares(3)
print(f"迭代器对象: {lazy_result}")
print("开始迭代:")
for value in lazy_result:
    print(f"获得值: {value}")

# 2. 内存使用对比
print("\n=== 2. 内存使用对比 ===")

def memory_usage_demo():
    """演示内存使用差异"""
    n = 1000000  # 一百万个数
    
    print(f"处理{n:,}个数的内存使用对比:")
    
    # 急切求值 - 创建完整列表
    print("\n急切求值 - 创建完整列表:")
    start_time = time.time()
    eager_list = list(range(n))
    creation_time = time.time() - start_time
    list_size = sys.getsizeof(eager_list)
    print(f"  创建时间: {creation_time:.4f} 秒")
    print(f"  内存使用: {list_size:,} 字节 ({list_size/1024/1024:.2f} MB)")
    
    # 惰性求值 - 创建迭代器
    print("\n惰性求值 - 创建迭代器:")
    start_time = time.time()
    lazy_iter = iter(range(n))
    creation_time = time.time() - start_time
    iter_size = sys.getsizeof(lazy_iter)
    print(f"  创建时间: {creation_time:.6f} 秒")
    print(f"  内存使用: {iter_size} 字节")
    
    print(f"\n内存节省: {(list_size - iter_size):,} 字节")
    print(f"内存效率提升: {list_size / iter_size:.0f} 倍")

memory_usage_demo()

# 3. 惰性计算的迭代器实现
print("\n=== 3. 惰性计算的迭代器实现 ===")

class LazyFibonacci:
    """惰性斐波那契数列迭代器"""
    def __init__(self, max_count=None):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.max_count and self.count >= self.max_count:
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

print("惰性斐波那契数列:")
fib_iter = LazyFibonacci(10)
for i, fib in enumerate(fib_iter):
    print(f"F({i}) = {fib}")

# 4. 惰性数据处理管道
print("\n=== 4. 惰性数据处理管道 ===")

class LazyMap:
    """惰性映射迭代器"""
    def __init__(self, func, iterable):
        self.func = func
        self.iterator = iter(iterable)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        value = next(self.iterator)
        print(f"  惰性应用函数到: {value}")
        return self.func(value)

class LazyFilter:
    """惰性过滤迭代器"""
    def __init__(self, predicate, iterable):
        self.predicate = predicate
        self.iterator = iter(iterable)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            value = next(self.iterator)
            print(f"  惰性检查条件: {value}")
            if self.predicate(value):
                return value

# 创建惰性处理管道
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"原始数据: {data}")

print("\n创建惰性处理管道:")
# 管道: 数据 -> 平方 -> 过滤偶数
squared = LazyMap(lambda x: x**2, data)
even_squares = LazyFilter(lambda x: x % 2 == 0, squared)

print("管道创建完成，开始处理:")
result = []
for value in even_squares:
    result.append(value)
    if len(result) >= 3:  # 只取前3个
        break

print(f"结果: {result}")

# 5. 惰性文件处理
print("\n=== 5. 惰性文件处理 ===")

class LazyFileReader:
    """惰性文件读取器"""
    def __init__(self, filename, chunk_size=1024):
        self.filename = filename
        self.chunk_size = chunk_size
        self.file = None
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.file is None:
            self.file = open(self.filename, 'r')
        
        chunk = self.file.read(self.chunk_size)
        if not chunk:
            self.file.close()
            raise StopIteration
        
        print(f"  惰性读取 {len(chunk)} 个字符")
        return chunk
    
    def __del__(self):
        if self.file and not self.file.closed:
            self.file.close()

# 创建测试文件
test_content = "这是一个测试文件。\n" * 100
with open('lazy_test.txt', 'w') as f:
    f.write(test_content)

print("惰性文件读取:")
file_reader = LazyFileReader('lazy_test.txt', chunk_size=50)
chunk_count = 0
for chunk in file_reader:
    chunk_count += 1
    print(f"处理第 {chunk_count} 个块")
    if chunk_count >= 3:  # 只处理前3个块
        break

# 清理文件
import os
if os.path.exists('lazy_test.txt'):
    os.remove('lazy_test.txt')

# 6. 惰性数学序列
print("\n=== 6. 惰性数学序列 ===")

class LazyPrimes:
    """惰性质数生成器"""
    def __init__(self):
        self.primes = []
        self.candidate = 2
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            if self._is_prime(self.candidate):
                prime = self.candidate
                self.primes.append(prime)
                self.candidate += 1
                print(f"  发现质数: {prime}")
                return prime
            self.candidate += 1
    
    def _is_prime(self, n):
        if n < 2:
            return False
        for p in self.primes:
            if p * p > n:
                break
            if n % p == 0:
                return False
        return True

print("惰性质数生成:")
primes_iter = LazyPrimes()
first_10_primes = []
for prime in primes_iter:
    first_10_primes.append(prime)
    if len(first_10_primes) >= 10:
        break

print(f"前10个质数: {first_10_primes}")

# 7. 惰性求值的组合
print("\n=== 7. 惰性求值的组合 ===")

class LazyRange:
    """惰性范围迭代器"""
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        
        value = self.current
        self.current += self.step
        return value

class LazyTake:
    """惰性取前N个元素"""
    def __init__(self, iterable, n):
        self.iterator = iter(iterable)
        self.n = n
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        
        value = next(self.iterator)
        self.count += 1
        return value

# 组合惰性操作
print("组合惰性操作:")
lazy_range = LazyRange(1, 1000000)  # 大范围
squares = LazyMap(lambda x: x**2, lazy_range)  # 平方
even_squares = LazyFilter(lambda x: x % 2 == 0, squares)  # 偶数
first_5 = LazyTake(even_squares, 5)  # 前5个

print("开始惰性计算:")
result = list(first_5)
print(f"结果: {result}")

# 8. 惰性求值的性能测试
print("\n=== 8. 惰性求值的性能测试 ===")

def performance_comparison():
    """性能对比测试"""
    n = 1000000
    
    # 急切求值
    print("急切求值测试:")
    start_time = time.time()
    eager_data = [x**2 for x in range(n) if x % 2 == 0]
    eager_result = eager_data[:5]
    eager_time = time.time() - start_time
    print(f"  处理时间: {eager_time:.4f} 秒")
    print(f"  内存使用: {sys.getsizeof(eager_data):,} 字节")
    print(f"  结果: {eager_result}")
    
    # 惰性求值
    print("\n惰性求值测试:")
    start_time = time.time()
    lazy_data = (x**2 for x in range(n) if x % 2 == 0)
    lazy_result = []
    for i, value in enumerate(lazy_data):
        lazy_result.append(value)
        if i >= 4:  # 只取前5个
            break
    lazy_time = time.time() - start_time
    print(f"  处理时间: {lazy_time:.6f} 秒")
    print(f"  内存使用: {sys.getsizeof(lazy_data)} 字节")
    print(f"  结果: {lazy_result}")
    
    print(f"\n性能提升: {eager_time / lazy_time:.0f} 倍")

performance_comparison()

# 9. 惰性求值的注意事项
print("\n=== 9. 惰性求值的注意事项 ===")

class StatefulLazyIterator:
    """有状态的惰性迭代器"""
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
        value = self.data[self.index]
        self.index += 1
        print(f"  访问第 {self.access_count} 次: {value}")
        return value

# 注意事项1: 迭代器只能使用一次
print("注意事项1: 迭代器只能使用一次")
stateful_iter = StatefulLazyIterator([1, 2, 3])

print("第一次迭代:")
first_result = list(stateful_iter)
print(f"结果: {first_result}")

print("第二次迭代:")
second_result = list(stateful_iter)
print(f"结果: {second_result}")

# 注意事项2: 副作用的执行时机
print("\n注意事项2: 副作用的执行时机")

def side_effect_function(x):
    print(f"  副作用: 处理 {x}")
    return x * 2

print("创建惰性映射（无副作用）:")
lazy_with_side_effect = LazyMap(side_effect_function, [1, 2, 3])
print("映射创建完成")

print("\n开始迭代（副作用执行）:")
for value in lazy_with_side_effect:
    print(f"获得: {value}")

# 10. 实际应用场景
print("\n=== 10. 实际应用场景 ===")

class LazyDataProcessor:
    """惰性数据处理器"""
    def __init__(self, data_source):
        self.data_source = data_source
    
    def filter_valid(self):
        """过滤有效数据"""
        for item in self.data_source:
            if item is not None and item != "":
                yield item
    
    def transform(self, func):
        """转换数据"""
        for item in self.filter_valid():
            yield func(item)
    
    def batch(self, size):
        """分批处理"""
        batch = []
        for item in self.transform(str.upper):
            batch.append(item)
            if len(batch) >= size:
                yield batch
                batch = []
        if batch:
            yield batch

# 模拟大数据集
large_dataset = ["apple", None, "banana", "", "cherry", "date", None, "elderberry"]
print(f"原始数据: {large_dataset}")

processor = LazyDataProcessor(large_dataset)
print("\n惰性批处理:")
for batch_num, batch in enumerate(processor.batch(2), 1):
    print(f"批次 {batch_num}: {batch}")

if __name__ == "__main__":
    print("\n=== 总结 ===")
    print("1. 惰性求值按需计算，节省内存和时间")
    print("2. 迭代器天然支持惰性求值")
    print("3. 惰性求值适合处理大数据集")
    print("4. 注意迭代器的一次性特性")
    print("5. 副作用在实际迭代时才执行")
    print("6. 惰性求值可以组合形成处理管道")