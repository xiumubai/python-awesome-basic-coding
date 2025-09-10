# 迭代器综合练习

本章包含了一系列迭代器相关的练习题，从基础到高级，帮助巩固迭代器的学习。每个练习都包含问题描述、解决方案和测试用例。

## 学习目标

- 综合运用迭代器知识
- 解决实际编程问题
- 提高代码设计能力
- 掌握性能优化技巧

## 练习1: 倒计数迭代器

**要求**: 从指定数字开始倒计数到0

```python
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
countdown = CountdownIterator(5)
print(f"倒计数: {list(countdown)}")  # [5, 4, 3, 2, 1, 0]
```

## 练习2: 素数生成器

**要求**: 生成指定范围内的所有素数

```python
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
primes = list(prime_generator(2, 30))
print(f"2到30的素数: {primes}")
```

## 练习3: 矩阵迭代器

**要求**: 按行、按列、按对角线遍历矩阵

```python
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
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
mat_iter = MatrixIterator(matrix)

print(f"按行遍历: {list(mat_iter.iterate_by_rows())}")
print(f"按列遍历: {list(mat_iter.iterate_by_columns())}")
print(f"对角线遍历: {list(mat_iter.iterate_diagonal())}")
```

## 练习4: 数据流处理管道

**要求**: 处理数据流，支持过滤、转换、聚合

```python
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
data = range(1, 21)  # 1到20

# 构建处理管道
result = (DataPipeline(data)
          .filter(lambda x: x % 2 == 0)  # 过滤偶数
          .map(lambda x: x ** 2)         # 平方
          .take(5)                       # 取前5个
          .collect())                    # 收集结果

print(f"处理结果: {result}")
```

## 练习5: 文件处理迭代器

**要求**: 模拟文件读取，支持按行、按块、按模式处理

```python
from collections import defaultdict

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
file_content = """Python是一种编程语言
它简单易学
Python广泛应用于数据科学
机器学习和Web开发
Python社区活跃"""

processor = FileProcessor(file_content)

# 按行处理
for line_num, line in processor.lines():
    print(f"第{line_num}行: {line}")

# 模式匹配
for line_num, line in processor.grep('Python'):
    print(f"第{line_num}行: {line}")
```

## 练习6: 树形结构遍历迭代器

**要求**: 支持深度优先和广度优先遍历

```python
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

# 构建树结构
root = TreeNode('A')
root.add_child(TreeNode('B'))
root.add_child(TreeNode('C'))
root.children[0].add_child(TreeNode('D'))
root.children[0].add_child(TreeNode('E'))
root.children[1].add_child(TreeNode('F'))

print(f"深度优先遍历: {list(root.dfs_iterator())}")
print(f"广度优先遍历: {list(root.bfs_iterator())}")
```

## 练习7: 缓存迭代器

**要求**: 缓存已访问的元素，支持重复访问

```python
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
cached_iter = CachedIterator(range(5))

# 第一次遍历（部分）
for i, item in enumerate(cached_iter):
    print(f"访问: {item}")
    if i >= 2:  # 只访问前3个
        break

# 重置并完整遍历
cached_iter.reset()
for item in cached_iter:
    print(f"重新访问: {item}")
```

## 练习8: 性能优化挑战

**要求**: 优化大数据集的处理性能

```python
import time
import itertools

def performance_challenge():
    """性能挑战"""
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
    
    for name, method in methods:
        start_time = time.time()
        result = method()
        end_time = time.time()
        print(f"{name}: {end_time - start_time:.6f} 秒, 结果: {result}")

performance_challenge()
```

## 练习9: 日志分析器

**要求**: 分析日志文件，统计访问模式

```python
from collections import defaultdict

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
log_data = [
    "2023-01-01 10:00:00 - 192.168.1.1 - GET - /home",
    "2023-01-01 10:01:00 - 192.168.1.2 - POST - /login",
    "2023-01-01 10:02:00 - 192.168.1.1 - GET - /home",
    "2023-01-01 10:03:00 - 192.168.1.3 - GET - /about",
    "2023-01-01 10:04:00 - 192.168.1.2 - GET - /home",
    "2023-01-01 10:05:00 - 192.168.1.1 - POST - /contact"
]

analyzer = LogAnalyzer(log_data)

# 分析GET请求
for entry in analyzer.filter_by_method('GET'):
    print(f"{entry['timestamp']} - {entry['ip']} - {entry['url']}")

# 热门URL统计
for url, count in analyzer.top_urls(3):
    print(f"{url}: {count} 次访问")
```

## 练习10: 线程安全的迭代器

**要求**: 实现线程安全的迭代器

```python
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
thread_safe_iter = ThreadSafeIterator(range(10))

def worker(iterator, worker_id):
    """工作线程"""
    try:
        while True:
            value = next(iterator)
            print(f"Worker-{worker_id}: {value}")
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
```

## 学习要点

### 核心概念

1. **迭代器协议实现**
   - `__iter__()` 和 `__next__()` 方法
   - StopIteration 异常处理
   - 状态管理和重置机制

2. **生成器应用**
   - yield 关键字的使用
   - 生成器表达式
   - yield from 语法

3. **性能优化**
   - 内存效率对比
   - 惰性求值的优势
   - 大数据集处理策略

### 实际应用

1. **数据处理管道**
   - 函数式编程思想
   - 链式操作设计
   - 流式数据处理

2. **文件和日志处理**
   - 按行读取大文件
   - 模式匹配和过滤
   - 统计分析功能

3. **复杂数据结构遍历**
   - 树形结构遍历
   - 矩阵操作
   - 图形算法应用

### 高级特性

1. **缓存机制**
   - 重复访问支持
   - 内存管理策略
   - 性能权衡考虑

2. **线程安全**
   - 并发访问控制
   - 锁机制使用
   - 竞态条件避免

## 注意事项

1. **内存管理**
   - 避免一次性加载大数据集
   - 合理使用缓存机制
   - 及时释放不需要的资源

2. **错误处理**
   - 正确处理 StopIteration 异常
   - 边界条件检查
   - 异常信息的传递

3. **性能考虑**
   - 选择合适的迭代器类型
   - 避免不必要的计算
   - 测试和优化关键路径

4. **代码质量**
   - 保持代码可读性
   - 添加适当的文档
   - 编写单元测试

## 总结

通过这些综合练习，你应该能够：

- 熟练实现各种类型的迭代器
- 理解迭代器在实际项目中的应用
- 掌握性能优化的技巧和方法
- 具备解决复杂问题的能力

迭代器是Python中非常强大的工具，掌握它们将大大提高你的编程效率和代码质量。继续练习和探索，你会发现更多有趣的应用场景！