# 迭代器与生成器对比

本节详细对比迭代器和生成器的区别、优缺点和使用场景。生成器是创建迭代器的一种简洁方式，理解两者的关系对于编写高效的Python代码非常重要。

## 学习目标

1. 理解迭代器和生成器的区别
2. 掌握生成器的创建方法
3. 学会选择合适的实现方式
4. 了解性能和内存使用差异

## 1. 基本概念对比

### 迭代器实现

传统的迭代器需要实现`__iter__`和`__next__`方法：

```python
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
```

### 生成器函数实现

生成器函数使用`yield`关键字，更加简洁：

```python
def number_generator(start, end):
    """生成器函数实现"""
    current = start
    while current < end:
        yield current
        current += 1
```

### 生成器表达式实现

生成器表达式是最简洁的形式：

```python
def create_number_generator_expr(start, end):
    """生成器表达式实现"""
    return (x for x in range(start, end))
```

### 使用示例

```python
# 测试三种实现
iterator = NumberIterator(1, 6)
generator_func = number_generator(1, 6)
generator_expr = create_number_generator_expr(1, 6)

print(f"迭代器: {list(iterator)}")          # [1, 2, 3, 4, 5]
print(f"生成器函数: {list(generator_func)}")   # [1, 2, 3, 4, 5]
print(f"生成器表达式: {list(generator_expr)}") # [1, 2, 3, 4, 5]
```

## 2. 语法差异

### 复杂示例：斐波那契数列

**迭代器类实现**（约20行代码）：

```python
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
```

**生成器函数实现**（约10行代码）：

```python
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
```

### 代码复杂度对比

- **迭代器类**：约20行代码，需要管理状态变量
- **生成器函数**：约10行代码，代码简化50%
- **可读性**：生成器更直观，逻辑更清晰

## 3. 内存使用对比

### 内存效率测试

```python
import tracemalloc

def memory_usage_test():
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
```

### 内存使用特点

- **列表**：立即分配所有元素的内存
- **生成器**：只保存生成逻辑，按需创建元素
- **内存节省**：生成器通常节省90%以上的内存

## 4. 性能对比

### 性能测试

```python
import time

def performance_comparison():
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
```

### 性能排名（通常情况）

1. **内置range**：C语言实现，最快
2. **生成器表达式**：简洁高效
3. **生成器函数**：Python实现，较快
4. **迭代器类**：开销较大，相对较慢

## 5. 状态管理对比

### 迭代器的状态管理

```python
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
```

### 生成器的状态管理

```python
def stateful_generator(data):
    """有状态的生成器"""
    access_count = 0
    for item in data:
        access_count += 1
        yield item, access_count
```

### 状态管理特点

- **迭代器类**：可以提供外部访问状态的方法
- **生成器**：状态封装在函数内部，通过yield传递
- **灵活性**：迭代器类在状态管理上更灵活

## 6. 错误处理对比

### 迭代器错误处理

```python
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
```

### 生成器错误处理

```python
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
```

### 错误处理特点

- **迭代器**：可以在`__next__`方法中集中处理错误
- **生成器**：错误处理更自然，使用标准的try-except
- **调试**：生成器的错误信息通常更清晰

## 7. 复用性对比

### 复用性测试

```python
# 迭代器复用（需要重新创建）
iterator = NumberIterator(1, 4)
print(f"第一次使用: {list(iterator)}")  # [1, 2, 3]
print(f"第二次使用: {list(iterator)}")  # [] (已耗尽)

# 需要重新创建
iterator = NumberIterator(1, 4)
print(f"重新创建后: {list(iterator)}")  # [1, 2, 3]

# 生成器复用（需要重新调用）
generator = number_generator(1, 4)
print(f"第一次使用: {list(generator)}")  # [1, 2, 3]
print(f"第二次使用: {list(generator)}")  # [] (已耗尽)

# 需要重新调用
generator = number_generator(1, 4)
print(f"重新调用后: {list(generator)}")  # [1, 2, 3]
```

### 复用性特点

- **一次性**：迭代器和生成器都是一次性的
- **重新创建**：使用完毕后需要重新创建或调用
- **内存效率**：一次性特性保证了内存效率

## 8. 适用场景

### 使用迭代器类的场景

1. **复杂的状态管理**：需要多个状态变量和复杂逻辑
2. **多个方法和属性**：需要提供额外的方法和属性
3. **继承和多态**：需要利用面向对象特性
4. **外部状态访问**：状态需要在迭代过程中被外部访问

```python
class ComplexIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.stats = {'accessed': 0, 'filtered': 0}
    
    def get_progress(self):
        return f"{self.index}/{len(self.data)}"
    
    def get_statistics(self):
        return self.stats.copy()
```

### 使用生成器的场景

1. **简单的序列生成**：逻辑简单，状态管理简单
2. **数据流处理**：处理大量数据流
3. **内存敏感的应用**：需要节省内存
4. **快速原型开发**：快速实现和测试

```python
def simple_data_processor(data):
    for item in data:
        if item > 0:
            yield item * 2
```

## 9. 实际应用示例

### 文件处理示例

**迭代器方式**：

```python
class FileLineIterator:
    """文件行迭代器"""
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
```

**生成器方式**：

```python
def file_line_generator(lines):
    """文件行生成器"""
    line_count = 0
    char_count = 0
    
    for line in lines:
        line_count += 1
        char_count += len(line)
        yield line, {'line_number': line_count, 'char_count': char_count}
```

### 数据转换管道

生成器特别适合构建数据处理管道：

```python
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
pipeline = format_output(square_numbers(filter_even(data_source())))
for result in pipeline:
    print(result)
# 输出: 结果: 0, 结果: 4, 结果: 16, 结果: 36, 结果: 64
```

## 10. 性能优化建议

### 优化示例

```python
def optimization_examples():
    data = range(1000)
    
    # 避免：转换为列表
    result1 = sum([x**2 for x in data if x % 2 == 0])  # 内存消耗大
    
    # 推荐：使用生成器表达式
    result2 = sum(x**2 for x in data if x % 2 == 0)    # 内存效率高
    
    # 推荐：使用生成器函数
    def optimized_generator(data):
        for x in data:
            if x % 2 == 0:
                yield x**2
    
    result3 = sum(optimized_generator(data))            # 逻辑清晰
```

### 优化原则

1. **避免不必要的列表转换**：优先使用生成器表达式
2. **选择合适的实现方式**：简单场景用生成器，复杂场景用迭代器类
3. **利用内置函数**：`map()`, `filter()`, `zip()`等返回迭代器
4. **链式操作**：构建数据处理管道

## 选择指南

### 决策树

```
需要迭代器吗？
├─ 是
│  ├─ 需要复杂状态管理？
│  │  ├─ 是 → 使用迭代器类
│  │  └─ 否
│  │     ├─ 逻辑复杂？
│  │     │  ├─ 是 → 使用生成器函数
│  │     │  └─ 否 → 使用生成器表达式
│  └─ 需要外部访问状态？
│     ├─ 是 → 使用迭代器类
│     └─ 否 → 使用生成器
└─ 否 → 考虑其他数据结构
```

## 学习要点

1. **语法差异**：迭代器类需要实现协议，生成器使用yield
2. **内存效率**：生成器在内存使用上更高效
3. **代码简洁性**：生成器代码更简洁，可读性更好
4. **状态管理**：迭代器类在复杂状态管理上更灵活
5. **性能特点**：生成器表达式通常性能最佳
6. **适用场景**：根据复杂度和需求选择合适的实现方式

## 注意事项

- 迭代器和生成器都是一次性的，使用完毕后需要重新创建
- 生成器函数每次调用都会创建新的生成器对象
- 在需要多次遍历同一数据时，考虑使用列表或其他可重复迭代的数据结构
- 生成器的调试可能比迭代器类更困难，因为状态封装在函数内部
- 选择实现方式时要平衡代码简洁性、性能和功能需求

通过理解迭代器和生成器的区别，你可以根据具体需求选择最合适的实现方式，编写更高效和优雅的Python代码。