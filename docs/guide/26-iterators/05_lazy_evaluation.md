# 迭代器的惰性求值

本节详细介绍迭代器的惰性求值特性，这是迭代器最重要的特征之一。惰性求值意味着值只在需要时才计算，这带来了内存效率和性能优势。

## 学习目标

1. 理解惰性求值的概念和优势
2. 掌握惰性求值在迭代器中的应用
3. 学会设计惰性求值的迭代器
4. 了解惰性求值与急切求值的区别

## 1. 惰性求值基础概念

惰性求值与急切求值的对比：

```python
# 急切求值 - 立即计算所有值
def eager_squares(n):
    """急切求值 - 立即计算所有平方数"""
    print(f"急切求值: 立即计算前{n}个平方数")
    result = []
    for i in range(n):
        square = i ** 2
        print(f"  计算 {i}^2 = {square}")
        result.append(square)
    return result

# 惰性求值 - 按需计算
def lazy_squares(n):
    """惰性求值 - 按需计算平方数"""
    print(f"惰性求值: 创建前{n}个平方数的迭代器")
    for i in range(n):
        square = i ** 2
        print(f"  按需计算 {i}^2 = {square}")
        yield square

# 对比演示
print("急切求值示例:")
eager_result = eager_squares(3)
print(f"结果: {eager_result}")

print("\n惰性求值示例:")
lazy_result = lazy_squares(3)
print(f"迭代器对象: {lazy_result}")
print("开始迭代:")
for value in lazy_result:
    print(f"获得值: {value}")
```

## 2. 内存使用对比

惰性求值的最大优势是内存效率：

```python
import sys
import time

def memory_usage_demo():
    """演示内存使用差异"""
    n = 1000000  # 一百万个数
    
    # 急切求值 - 创建完整列表
    print("急切求值 - 创建完整列表:")
    start_time = time.time()
    eager_list = list(range(n))
    creation_time = time.time() - start_time
    list_size = sys.getsizeof(eager_list)
    print(f"  创建时间: {creation_time:.4f} 秒")
    print(f"  内存使用: {list_size:,} 字节 ({list_size/1024/1024:.2f} MB)")
    
    # 惰性求值 - 创建迭代器
    print("惰性求值 - 创建迭代器:")
    start_time = time.time()
    lazy_iter = iter(range(n))
    creation_time = time.time() - start_time
    iter_size = sys.getsizeof(lazy_iter)
    print(f"  创建时间: {creation_time:.6f} 秒")
    print(f"  内存使用: {iter_size} 字节")
    
    print(f"内存效率提升: {list_size / iter_size:.0f} 倍")
```

## 3. 惰性计算的迭代器实现

自定义惰性迭代器的实现：

```python
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

# 使用惰性斐波那契数列
fib_iter = LazyFibonacci(10)
for i, fib in enumerate(fib_iter):
    print(f"F({i}) = {fib}")
```

## 4. 惰性数据处理管道

构建惰性数据处理管道：

```python
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

# 管道: 数据 -> 平方 -> 过滤偶数
squared = LazyMap(lambda x: x**2, data)
even_squares = LazyFilter(lambda x: x % 2 == 0, squared)

# 只处理需要的数据
result = []
for value in even_squares:
    result.append(value)
    if len(result) >= 3:  # 只取前3个
        break

print(f"结果: {result}")
```

## 5. 惰性文件处理

处理大文件时的惰性读取：

```python
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

# 使用惰性文件读取器
file_reader = LazyFileReader('large_file.txt', chunk_size=50)
for chunk_num, chunk in enumerate(file_reader, 1):
    print(f"处理第 {chunk_num} 个块")
    if chunk_num >= 3:  # 只处理前3个块
        break
```

## 6. 惰性数学序列

生成无限数学序列：

```python
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

# 生成前10个质数
primes_iter = LazyPrimes()
first_10_primes = []
for prime in primes_iter:
    first_10_primes.append(prime)
    if len(first_10_primes) >= 10:
        break

print(f"前10个质数: {first_10_primes}")
```

## 7. 惰性求值的组合

组合多个惰性操作：

```python
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
lazy_range = LazyRange(1, 1000000)  # 大范围
squares = LazyMap(lambda x: x**2, lazy_range)  # 平方
even_squares = LazyFilter(lambda x: x % 2 == 0, squares)  # 偶数
first_5 = LazyTake(even_squares, 5)  # 前5个

result = list(first_5)
print(f"结果: {result}")
```

## 8. 惰性求值的性能测试

性能对比分析：

```python
import time
import sys

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
    
    # 惰性求值
    print("惰性求值测试:")
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
    
    print(f"性能提升: {eager_time / lazy_time:.0f} 倍")
```

## 9. 惰性求值的注意事项

### 迭代器的一次性特性

```python
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

# 迭代器只能使用一次
stateful_iter = StatefulLazyIterator([1, 2, 3])

print("第一次迭代:")
first_result = list(stateful_iter)
print(f"结果: {first_result}")

print("第二次迭代:")
second_result = list(stateful_iter)  # 空结果
print(f"结果: {second_result}")
```

### 副作用的执行时机

```python
def side_effect_function(x):
    print(f"  副作用: 处理 {x}")
    return x * 2

print("创建惰性映射（无副作用）:")
lazy_with_side_effect = LazyMap(side_effect_function, [1, 2, 3])
print("映射创建完成")

print("开始迭代（副作用执行）:")
for value in lazy_with_side_effect:
    print(f"获得: {value}")
```

## 10. 实际应用场景

大数据处理的惰性管道：

```python
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

# 处理大数据集
large_dataset = ["apple", None, "banana", "", "cherry", "date", None, "elderberry"]
processor = LazyDataProcessor(large_dataset)

for batch_num, batch in enumerate(processor.batch(2), 1):
    print(f"批次 {batch_num}: {batch}")
```

## 惰性求值的核心优势

### 1. 内存效率
- 不需要将所有数据加载到内存
- 只保存当前处理的数据
- 适合处理大数据集

### 2. 时间效率
- 按需计算，避免不必要的计算
- 可以提前终止处理
- 支持无限序列

### 3. 组合性
- 可以轻松组合多个惰性操作
- 形成高效的数据处理管道
- 保持代码的可读性和模块化

## 学习要点

1. **概念理解**：惰性求值是按需计算，而不是预先计算
2. **内存优势**：惰性求值显著减少内存使用
3. **性能优势**：避免不必要的计算，提高效率
4. **组合能力**：可以组合多个惰性操作形成管道
5. **一次性特性**：迭代器只能使用一次
6. **副作用时机**：副作用在实际迭代时才执行

## 注意事项

- 迭代器具有一次性特性，耗尽后不能重复使用
- 副作用（如打印、文件写入）只在实际迭代时执行
- 惰性求值可能会延迟错误的发现
- 在某些情况下，急切求值可能更合适（如需要多次访问数据）
- 调试惰性代码可能比较困难，因为计算是延迟的

通过掌握惰性求值，你可以编写更加内存高效和性能优化的Python代码，特别是在处理大数据集时。