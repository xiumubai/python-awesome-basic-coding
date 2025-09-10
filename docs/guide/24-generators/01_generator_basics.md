# 生成器基础

生成器是Python中一个强大的特性，它提供了一种内存高效的方式来创建迭代器。本节将介绍生成器的基本概念、yield关键字的使用，以及生成器与普通函数的区别。

## 什么是生成器？

生成器是一种特殊的迭代器，它可以在需要时生成值，而不是一次性创建所有值。这种"惰性求值"的特性使得生成器在处理大量数据时具有显著的内存优势。

### 生成器的特点

1. **惰性求值**：只在需要时计算和返回值
2. **内存高效**：不需要将所有值存储在内存中
3. **状态保持**：能够记住上次执行的位置
4. **一次性使用**：生成器对象只能遍历一次

## yield关键字

yield关键字是生成器的核心，它的作用类似于return，但有重要区别：

- **return**：结束函数执行，返回值
- **yield**：暂停函数执行，返回值，保持状态

### 基本的生成器函数

```python
def simple_generator():
    """最简单的生成器示例"""
    print("生成器开始执行")
    yield 1
    print("第一次yield后继续执行")
    yield 2
    print("第二次yield后继续执行")
    yield 3
    print("生成器执行完毕")

# 创建生成器对象
gen = simple_generator()
print(f"生成器对象: {gen}")
print(f"生成器类型: {type(gen)}")

# 逐个获取值
print("\n=== 逐个获取值 ===")
print(f"第一个值: {next(gen)}")
print(f"第二个值: {next(gen)}")
print(f"第三个值: {next(gen)}")

# 尝试获取第四个值会引发StopIteration异常
try:
    print(f"第四个值: {next(gen)}")
except StopIteration:
    print("生成器已耗尽")
```

### 数字序列生成器

```python
def number_generator(start, end, step=1):
    """生成指定范围的数字序列"""
    current = start
    while current < end:
        yield current
        current += step

# 使用生成器
print("\n=== 数字序列生成器 ===")
for num in number_generator(1, 10, 2):
    print(f"生成的数字: {num}")

# 生成器可以创建无限序列
def infinite_counter(start=0):
    """无限计数器"""
    count = start
    while True:
        yield count
        count += 1

# 使用无限生成器（注意要有退出条件）
print("\n=== 无限计数器 ===")
counter = infinite_counter(10)
for i, value in enumerate(counter):
    if i >= 5:  # 只取前5个值
        break
    print(f"计数: {value}")
```

## 生成器 vs 普通函数

让我们通过对比来理解生成器与普通函数的区别：

### 普通函数返回列表

```python
def create_squares_list(n):
    """普通函数：返回平方数列表"""
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# 使用普通函数
print("\n=== 普通函数返回列表 ===")
squares_list = create_squares_list(5)
print(f"列表: {squares_list}")
print(f"内存中的完整列表: {list(squares_list)}")
```

### 生成器函数

```python
def create_squares_generator(n):
    """生成器函数：生成平方数"""
    for i in range(n):
        yield i ** 2

# 使用生成器
print("\n=== 生成器函数 ===")
squares_gen = create_squares_generator(5)
print(f"生成器对象: {squares_gen}")
print(f"转换为列表: {list(squares_gen)}")

# 注意：生成器只能使用一次
squares_gen2 = create_squares_generator(5)
print("\n逐个获取生成器的值:")
for square in squares_gen2:
    print(f"平方数: {square}")
```

## 内存使用对比

```python
import sys

def memory_comparison():
    """比较列表和生成器的内存使用"""
    n = 1000
    
    # 创建列表
    squares_list = [i ** 2 for i in range(n)]
    list_size = sys.getsizeof(squares_list)
    
    # 创建生成器
    squares_gen = (i ** 2 for i in range(n))
    gen_size = sys.getsizeof(squares_gen)
    
    print("\n=== 内存使用对比 ===")
    print(f"列表大小 ({n}个元素): {list_size} 字节")
    print(f"生成器大小: {gen_size} 字节")
    print(f"内存节省: {list_size - gen_size} 字节")
    print(f"节省比例: {(list_size - gen_size) / list_size * 100:.1f}%")

memory_comparison()
```

## 生成器的状态保持

```python
def stateful_generator():
    """演示生成器的状态保持"""
    print("生成器初始化")
    count = 0
    
    while count < 3:
        print(f"准备yield值: {count}")
        received = yield count
        print(f"收到的值: {received}")
        count += 1
    
    print("生成器结束")

# 演示状态保持
print("\n=== 生成器状态保持 ===")
gen = stateful_generator()

# 启动生成器
value1 = next(gen)
print(f"获得值: {value1}")

# 继续执行
value2 = next(gen)
print(f"获得值: {value2}")

# 再次继续
value3 = next(gen)
print(f"获得值: {value3}")
```

## 实际应用示例

### 文件行读取器

```python
def file_line_generator(filename):
    """逐行读取文件的生成器"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            line_number = 1
            for line in file:
                yield line_number, line.strip()
                line_number += 1
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
        return

# 创建示例文件
sample_content = """第一行内容
第二行内容
第三行内容
第四行内容"""

with open('sample.txt', 'w', encoding='utf-8') as f:
    f.write(sample_content)

# 使用文件读取生成器
print("\n=== 文件行读取器 ===")
for line_num, content in file_line_generator('sample.txt'):
    print(f"第{line_num}行: {content}")
```

### 斐波那契数列生成器

```python
def fibonacci_generator(max_count=None):
    """斐波那契数列生成器"""
    a, b = 0, 1
    count = 0
    
    while max_count is None or count < max_count:
        yield a
        a, b = b, a + b
        count += 1

# 使用斐波那契生成器
print("\n=== 斐波那契数列生成器 ===")
fib_gen = fibonacci_generator(10)
for i, fib_num in enumerate(fib_gen):
    print(f"F({i}) = {fib_num}")
```

## 生成器表达式预览

生成器表达式是创建生成器的简洁方式，语法类似列表推导式，但使用圆括号：

```python
# 列表推导式
squares_list = [x**2 for x in range(5)]
print(f"\n列表推导式: {squares_list}")

# 生成器表达式
squares_gen = (x**2 for x in range(5))
print(f"生成器表达式: {squares_gen}")
print(f"生成器内容: {list(squares_gen)}")

# 条件过滤
even_squares = (x**2 for x in range(10) if x % 2 == 0)
print(f"偶数平方: {list(even_squares)}")
```

## 学习要点总结

### 关键概念

1. **yield关键字**：暂停函数执行并返回值，保持函数状态
2. **惰性求值**：只在需要时计算值，节省内存
3. **状态保持**：生成器记住上次执行的位置和局部变量
4. **一次性使用**：生成器对象耗尽后不能重复使用

### 使用场景

- 处理大量数据时节省内存
- 创建无限序列
- 实现复杂的迭代逻辑
- 文件处理和数据流处理

### 注意事项

1. 生成器对象只能使用一次
2. 无法获取生成器的长度（len()不适用）
3. 无法通过索引访问元素
4. 调试时要注意生成器的状态

## 练习建议

1. **基础练习**：创建简单的生成器函数，理解yield的作用
2. **对比练习**：比较生成器和列表在内存使用上的差异
3. **应用练习**：使用生成器处理文件或创建数学序列
4. **调试练习**：学会调试生成器，理解其执行流程

通过这些基础知识的学习，你已经掌握了生成器的核心概念。接下来可以学习更高级的生成器特性，如生成器方法和协程应用。