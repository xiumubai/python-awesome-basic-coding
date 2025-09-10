#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
迭代器综合练习

本模块包含了一系列迭代器相关的练习题，从基础到高级，帮助巩固迭代器的学习。
每个练习都包含问题描述、解决方案和测试用例。

学习目标：
1. 综合运用迭代器知识
2. 解决实际编程问题
3. 提高代码设计能力
4. 掌握性能优化技巧
"""

import itertools
import random
import time
from typing import Iterator, Any, List, Tuple
from collections import defaultdict

print("=== 迭代器综合练习 ===")

# 练习1: 基础迭代器实现
print("\n练习1: 实现一个倒计数迭代器")
print("要求: 从指定数字开始倒计数到0")

class CountdownIterator:
    """倒计数迭代器"""
    def __init__(self, start):
        self.start = start
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        result = self.current
        self.current -= 1
        return result

# 测试倒计数迭代器
print("\n解决方案:")
countdown = CountdownIterator(5)
print(f"倒计数: {list(countdown)}")

# 练习2: 生成器函数
print("\n练习2: 实现素数生成器")
print("要求: 生成指定范围内的所有素数")

def is_prime(n):
    """判断是否为素数"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(start, end):
    """素数生成器"""
    for num in range(start, end + 1):
        if is_prime(num):
            yield num

# 测试素数生成器
print("\n解决方案:")
primes = list(prime_generator(2, 30))
print(f"2到30的素数: {primes}")

# 练习3: 复杂迭代器
print("\n练习3: 实现矩阵迭代器")
print("要求: 按行、按列、按对角线遍历矩阵")

class MatrixIterator:
    """矩阵迭代器"""
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if matrix else 0
    
    def iterate_by_rows(self):
        """按行遍历"""
        for row in self.matrix:
            for item in row:
                yield item
    
    def iterate_by_columns(self):
        """按列遍历"""
        for col in range(self.cols):
            for row in range(self.rows):
                yield self.matrix[row][col]
    
    def iterate_diagonal(self):
        """对角线遍历"""
        # 主对角线
        for i in range(min(self.rows, self.cols)):
            yield self.matrix[i][i]
        
        # 副对角线
        for i in range(min(self.rows, self.cols)):
            yield self.matrix[i][self.cols - 1 - i]

# 测试矩阵迭代器
print("\n解决方案:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
mat_iter = MatrixIterator(matrix)

print(f"原矩阵:")
for row in matrix:
    print(f"  {row}")

print(f"按行遍历: {list(mat_iter.iterate_by_rows())}")
print(f"按列遍历: {list(mat_iter.iterate_by_columns())}")
print(f"对角线遍历: {list(mat_iter.iterate_diagonal())}")

# 练习4: 数据流处理
print("\n练习4: 实现数据流处理管道")
print("要求: 处理数据流，支持过滤、转换、聚合")

class DataPipeline:
    """数据处理管道"""
    def __init__(self, data_source):
        self.data_source = data_source
    
    def filter(self, predicate):
        """过滤数据"""
        return DataPipeline(filter(predicate, self.data_source))
    
    def map(self, func):
        """转换数据"""
        return DataPipeline(map(func, self.data_source))
    
    def take(self, n):
        """取前n个元素"""
        return DataPipeline(itertools.islice(self.data_source, n))
    
    def skip(self, n):
        """跳过前n个元素"""
        return DataPipeline(itertools.islice(self.data_source, n, None))
    
    def collect(self):
        """收集结果"""
        return list(self.data_source)
    
    def reduce(self, func, initial=None):
        """聚合操作"""
        import functools
        if initial is not None:
            return functools.reduce(func, self.data_source, initial)
        else:
            return functools.reduce(func, self.data_source)

# 测试数据管道
print("\n解决方案:")
data = range(1, 21)  # 1到20
print(f"原始数据: {list(data)}")

# 构建处理管道
result = (DataPipeline(data)
          .filter(lambda x: x % 2 == 0)  # 过滤偶数
          .map(lambda x: x ** 2)         # 平方
          .take(5)                       # 取前5个
          .collect())                    # 收集结果

print(f"处理结果: {result}")

# 聚合操作
sum_result = (DataPipeline(range(1, 11))
              .filter(lambda x: x % 2 == 1)  # 奇数
              .reduce(lambda a, b: a + b))    # 求和

print(f"奇数求和: {sum_result}")

# 练习5: 文件处理迭代器
print("\n练习5: 实现文件内容处理迭代器")
print("要求: 模拟文件读取，支持按行、按块、按模式处理")

class FileProcessor:
    """文件处理器（模拟）"""
    def __init__(self, content):
        self.content = content.split('\n')
    
    def lines(self):
        """按行处理"""
        for line_num, line in enumerate(self.content, 1):
            yield line_num, line.strip()
    
    def chunks(self, size):
        """按块处理"""
        for i in range(0, len(self.content), size):
            yield self.content[i:i+size]
    
    def grep(self, pattern):
        """模式匹配"""
        for line_num, line in enumerate(self.content, 1):
            if pattern in line:
                yield line_num, line.strip()
    
    def word_count(self):
        """词频统计"""
        word_counts = defaultdict(int)
        for line in self.content:
            words = line.strip().split()
            for word in words:
                word_counts[word.lower()] += 1
        return dict(word_counts)

# 测试文件处理器
print("\n解决方案:")
file_content = """Python是一种编程语言
它简单易学
Python广泛应用于数据科学
机器学习和Web开发
Python社区活跃"""

processor = FileProcessor(file_content)

print("按行处理:")
for line_num, line in processor.lines():
    print(f"  第{line_num}行: {line}")

print("\n按块处理（每块2行）:")
for i, chunk in enumerate(processor.chunks(2), 1):
    print(f"  块{i}: {chunk}")

print("\n模式匹配（包含'Python'）:")
for line_num, line in processor.grep('Python'):
    print(f"  第{line_num}行: {line}")

print(f"\n词频统计: {processor.word_count()}")

# 练习6: 树形结构迭代器
print("\n练习6: 实现树形结构遍历迭代器")
print("要求: 支持深度优先和广度优先遍历")

class TreeNode:
    """树节点"""
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []
    
    def add_child(self, child):
        self.children.append(child)
    
    def dfs_iterator(self):
        """深度优先遍历"""
        yield self.value
        for child in self.children:
            yield from child.dfs_iterator()
    
    def bfs_iterator(self):
        """广度优先遍历"""
        queue = [self]
        while queue:
            node = queue.pop(0)
            yield node.value
            queue.extend(node.children)

# 测试树遍历
print("\n解决方案:")
# 构建树结构
root = TreeNode('A')
root.add_child(TreeNode('B'))
root.add_child(TreeNode('C'))
root.children[0].add_child(TreeNode('D'))
root.children[0].add_child(TreeNode('E'))
root.children[1].add_child(TreeNode('F'))

print("树结构: A -> [B -> [D, E], C -> [F]]")
print(f"深度优先遍历: {list(root.dfs_iterator())}")
print(f"广度优先遍历: {list(root.bfs_iterator())}")

# 练习7: 缓存迭代器
print("\n练习7: 实现带缓存的迭代器")
print("要求: 缓存已访问的元素，支持重复访问")

class CachedIterator:
    """带缓存的迭代器"""
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.cache = []
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        # 如果缓存中有数据，直接返回
        if self.index < len(self.cache):
            result = self.cache[self.index]
            self.index += 1
            return result
        
        # 从原迭代器获取新数据
        try:
            value = next(self.iterator)
            self.cache.append(value)
            self.index += 1
            return value
        except StopIteration:
            raise StopIteration
    
    def reset(self):
        """重置到开始位置"""
        self.index = 0
    
    def get_cache(self):
        """获取缓存内容"""
        return self.cache.copy()

# 测试缓存迭代器
print("\n解决方案:")
cached_iter = CachedIterator(range(5))

print("第一次遍历:")
first_pass = []
for item in cached_iter:
    first_pass.append(item)
    print(f"  访问: {item}")
    if len(first_pass) >= 3:  # 只访问前3个
        break

print(f"缓存内容: {cached_iter.get_cache()}")

# 重置并再次遍历
cached_iter.reset()
print("\n重置后遍历:")
for item in cached_iter:
    print(f"  访问: {item}")

# 练习8: 性能优化挑战
print("\n练习8: 性能优化挑战")
print("要求: 优化大数据集的处理性能")

def performance_challenge():
    """性能挑战"""
    # 生成大数据集
    data_size = 100000
    
    # 方法1: 传统方法（内存密集）
    def traditional_approach():
        data = list(range(data_size))
        filtered = [x for x in data if x % 2 == 0]
        squared = [x**2 for x in filtered]
        return sum(squared[:1000])
    
    # 方法2: 迭代器方法（内存友好）
    def iterator_approach():
        data = range(data_size)
        filtered = filter(lambda x: x % 2 == 0, data)
        squared = map(lambda x: x**2, filtered)
        limited = itertools.islice(squared, 1000)
        return sum(limited)
    
    # 方法3: 生成器方法
    def generator_approach():
        def process_data():
            for x in range(data_size):
                if x % 2 == 0:
                    yield x**2
        
        return sum(itertools.islice(process_data(), 1000))
    
    # 性能测试
    methods = [
        ('传统方法', traditional_approach),
        ('迭代器方法', iterator_approach),
        ('生成器方法', generator_approach)
    ]
    
    results = []
    for name, method in methods:
        start_time = time.time()
        result = method()
        end_time = time.time()
        results.append((name, end_time - start_time, result))
    
    print("\n性能对比:")
    for name, duration, result in results:
        print(f"  {name}: {duration:.6f} 秒, 结果: {result}")
    
    # 找出最快的方法
    fastest = min(results, key=lambda x: x[1])
    print(f"\n最快方法: {fastest[0]}")

performance_challenge()

# 练习9: 实际应用 - 日志分析器
print("\n练习9: 实际应用 - 日志分析器")
print("要求: 分析日志文件，统计访问模式")

class LogAnalyzer:
    """日志分析器"""
    def __init__(self, log_entries):
        self.log_entries = log_entries
    
    def parse_entries(self):
        """解析日志条目"""
        for entry in self.log_entries:
            parts = entry.split(' - ')
            if len(parts) >= 4:
                timestamp, ip, method, url = parts[:4]
                yield {
                    'timestamp': timestamp,
                    'ip': ip,
                    'method': method,
                    'url': url
                }
    
    def filter_by_method(self, method):
        """按请求方法过滤"""
        for entry in self.parse_entries():
            if entry['method'] == method:
                yield entry
    
    def group_by_ip(self):
        """按IP分组"""
        ip_groups = defaultdict(list)
        for entry in self.parse_entries():
            ip_groups[entry['ip']].append(entry)
        return dict(ip_groups)
    
    def top_urls(self, n=5):
        """最热门的URL"""
        url_counts = defaultdict(int)
        for entry in self.parse_entries():
            url_counts[entry['url']] += 1
        
        sorted_urls = sorted(url_counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_urls[:n]

# 测试日志分析器
print("\n解决方案:")
log_data = [
    "2023-01-01 10:00:00 - 192.168.1.1 - GET - /home",
    "2023-01-01 10:01:00 - 192.168.1.2 - POST - /login",
    "2023-01-01 10:02:00 - 192.168.1.1 - GET - /home",
    "2023-01-01 10:03:00 - 192.168.1.3 - GET - /about",
    "2023-01-01 10:04:00 - 192.168.1.2 - GET - /home",
    "2023-01-01 10:05:00 - 192.168.1.1 - POST - /contact"
]

analyzer = LogAnalyzer(log_data)

print("GET请求:")
for entry in analyzer.filter_by_method('GET'):
    print(f"  {entry['timestamp']} - {entry['ip']} - {entry['url']}")

print(f"\n按IP分组: {len(analyzer.group_by_ip())} 个不同IP")
for ip, entries in analyzer.group_by_ip().items():
    print(f"  {ip}: {len(entries)} 次访问")

print(f"\n热门URL:")
for url, count in analyzer.top_urls(3):
    print(f"  {url}: {count} 次访问")

# 练习10: 高级挑战 - 并发安全的迭代器
print("\n练习10: 高级挑战 - 线程安全的迭代器")
print("要求: 实现线程安全的迭代器")

import threading

class ThreadSafeIterator:
    """线程安全的迭代器"""
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.lock = threading.Lock()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        with self.lock:
            try:
                return next(self.iterator)
            except StopIteration:
                raise StopIteration

# 测试线程安全迭代器
print("\n解决方案:")
thread_safe_iter = ThreadSafeIterator(range(10))

# 模拟多线程访问
results = []

def worker(iterator, worker_id):
    """工作线程"""
    try:
        while True:
            value = next(iterator)
            results.append(f"Worker-{worker_id}: {value}")
            time.sleep(0.001)  # 模拟处理时间
    except StopIteration:
        pass

# 创建多个线程
threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(thread_safe_iter, i+1))
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print("多线程处理结果:")
for result in sorted(results):
    print(f"  {result}")

# 总结和评估
print("\n=== 练习总结 ===")
print("\n完成的练习:")
exercises = [
    "1. 倒计数迭代器 - 基础迭代器实现",
    "2. 素数生成器 - 生成器函数应用",
    "3. 矩阵迭代器 - 复杂数据结构遍历",
    "4. 数据流处理管道 - 函数式编程",
    "5. 文件处理迭代器 - 实际应用场景",
    "6. 树形结构遍历 - 递归和迭代",
    "7. 缓存迭代器 - 性能优化",
    "8. 性能优化挑战 - 大数据处理",
    "9. 日志分析器 - 实际项目应用",
    "10. 线程安全迭代器 - 并发编程"
]

for exercise in exercises:
    print(f"  ✓ {exercise}")

print("\n学习要点:")
learning_points = [
    "迭代器协议的实现",
    "生成器的使用技巧",
    "内存效率优化",
    "性能测试和对比",
    "实际应用场景",
    "错误处理和边界情况",
    "线程安全考虑",
    "代码可读性和维护性"
]

for point in learning_points:
    print(f"  • {point}")

if __name__ == "__main__":
    print("\n=== 最终总结 ===")
    print("1. 迭代器是Python中强大的编程工具")
    print("2. 生成器提供了简洁的迭代器实现方式")
    print("3. 合理使用迭代器可以显著提高程序性能")
    print("4. 迭代器特别适合处理大数据集和流数据")
    print("5. 在实际项目中要考虑线程安全和错误处理")
    print("6. 持续练习是掌握迭代器的关键")
    print("\n恭喜完成所有迭代器练习！🎉")