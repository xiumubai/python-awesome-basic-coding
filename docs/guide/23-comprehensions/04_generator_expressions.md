# 生成器表达式 (Generator Expressions)

## 学习目标

- 理解生成器表达式的基本语法
- 掌握生成器的惰性求值特性
- 学会在不同场景中使用生成器表达式
- 了解生成器表达式的内存优势
- 掌握生成器的迭代和消费方式

## 概述

生成器表达式是一种内存高效的方式来创建生成器对象。它们使用类似列表推导式的语法，但使用圆括号而不是方括号。生成器表达式是惰性求值的，只在需要时才计算值。

## 基本语法

生成器表达式的基本语法是：`(expression for item in iterable)`

```python
# 基本语法演示
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
```

## 惰性求值特性

生成器表达式的一个重要特性是惰性求值，即只有在需要时才会计算值：

```python
import time

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
```

## 内存效率优势

生成器表达式相比列表推导式具有显著的内存优势：

```python
import sys

# 大数据集
n = 1000000

# 列表推导式（占用大量内存）
list_comp = [x**2 for x in range(n)]
list_size = sys.getsizeof(list_comp)
print(f"列表大小: {list_size:,} 字节")

# 生成器表达式（占用很少内存）
gen_exp = (x**2 for x in range(n))
gen_size = sys.getsizeof(gen_exp)
print(f"生成器大小: {gen_size:,} 字节")

print(f"内存节省: {(list_size - gen_size) / list_size * 100:.1f}%")
```

## 条件过滤

生成器表达式支持条件过滤：

```python
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
```

## 嵌套生成器表达式

生成器表达式支持嵌套结构：

```python
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
```

## 生成器方法和操作

生成器提供了多种操作方法：

```python
from itertools import islice

# 使用next()函数
gen = (x**2 for x in range(5))
print("使用next()逐个获取:")
print(f"第一个值: {next(gen)}")
print(f"第二个值: {next(gen)}")
print(f"剩余值: {list(gen)}")

# 使用islice获取部分元素
gen = (x**2 for x in range(100))
first_five = list(islice(gen, 5))
print(f"前5个平方数: {first_five}")

# 生成器表达式作为函数参数
numbers = range(1, 11)
total = sum(x**2 for x in numbers)
print(f"1-10平方和: {total}")

# 检查生成器是否为空
gen = (x for x in [] if x > 0)
try:
    first_value = next(gen)
    print(f"第一个值: {first_value}")
except StopIteration:
    print("生成器为空")
```

## 实际应用场景

### 1. 日志处理

```python
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
```

### 2. 数据转换管道

```python
raw_data = ['  123  ', '  456  ', '  789  ', '  abc  ']

# 清理并转换数据
cleaned_numbers = (int(item.strip()) for item in raw_data 
                  if item.strip().isdigit())
print(f"清理后的数字: {list(cleaned_numbers)}")
```

### 3. 配置文件解析

```python
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
print(f"配置字典: {config_dict}")
```

## 性能对比

生成器表达式在内存使用和某些场景下的性能方面具有优势：

```python
import time
import sys

n = 100000

# 内存使用对比
list_comp = [x**2 for x in range(n)]
gen_exp = (x**2 for x in range(n))

list_memory = sys.getsizeof(list_comp)
gen_memory = sys.getsizeof(gen_exp)

print(f"列表内存: {list_memory:,}字节")
print(f"生成器内存: {gen_memory:,}字节")
print(f"内存节省: {(list_memory - gen_memory) / list_memory * 100:.1f}%")

# 迭代性能对比
start_time = time.time()
total1 = sum(list_comp)
list_iter_time = time.time() - start_time

start_time = time.time()
total2 = sum(gen_exp)
gen_iter_time = time.time() - start_time

print(f"列表迭代: {list_iter_time:.4f}秒")
print(f"生成器迭代: {gen_iter_time:.4f}秒")
```

## 常见错误和注意事项

### 1. 生成器只能消费一次

```python
# ❌ 错误：尝试多次消费同一个生成器
gen = (x**2 for x in range(5))
print(f"第一次消费: {list(gen)}")
print(f"第二次消费: {list(gen)}")  # 结果为空

# ✅ 正确：重新创建生成器
gen = (x**2 for x in range(5))
result1 = list(gen)
gen = (x**2 for x in range(5))  # 重新创建
result2 = list(gen)
```

### 2. 变量作用域问题

```python
# ❌ 错误：所有生成器都会使用最后的i值
generators = []
for i in range(3):
    generators.append((x + i for x in range(3)))

# ✅ 正确：使用默认参数捕获变量
generators = []
for i in range(3):
    generators.append((x + val for x in range(3) for val in [i]))
```

### 3. 过早消费生成器

```python
# ❌ 错误：在函数中消费了生成器
def process_data(data_gen):
    print(f"数据长度: {len(list(data_gen))}")
    return data_gen  # 返回空生成器

# ✅ 正确：转换为列表或使用tee
def process_data_correctly(data_gen):
    data_list = list(data_gen)
    print(f"数据长度: {len(data_list)}")
    return (x for x in data_list)  # 返回新生成器
```

## 学习要点总结

1. **基本语法**：`(expression for item in iterable)`
2. **惰性求值**：只在需要时计算值，提高效率
3. **内存效率**：相比列表推导式节省大量内存
4. **一次性消费**：生成器只能迭代一次，消费后需要重新创建
5. **条件过滤**：支持if条件进行数据筛选
6. **嵌套结构**：支持多层嵌套和复杂逻辑
7. **函数参数**：可以直接作为函数参数使用
8. **作用域陷阱**：注意变量作用域和过早消费的问题
9. **适用场景**：数据流处理、大数据集处理、管道操作
10. **性能优势**：在处理大数据集时具有明显的内存和性能优势

## 注意事项

- 生成器表达式适合处理大数据集或无限序列
- 如果需要多次访问数据，考虑使用列表推导式
- 注意变量作用域问题，特别是在循环中创建生成器时
- 避免过早消费生成器，保持其惰性特性
- 合理使用生成器方法如`next()`、`islice()`等