# 生成器函数

生成器函数是包含yield关键字的函数，它们返回生成器对象而不是直接返回值。本节将深入探讨生成器函数的定义、参数传递、返回值处理以及生命周期管理。

## 生成器函数的定义

生成器函数看起来像普通函数，但包含一个或多个yield语句。当调用生成器函数时，它返回一个生成器对象，而不是立即执行函数体。

### 基本定义规则

```python
def my_generator():
    """基本的生成器函数"""
    yield 1
    yield 2
    yield 3

# 调用生成器函数返回生成器对象
gen = my_generator()
print(f"生成器对象: {gen}")
print(f"类型: {type(gen)}")

# 使用生成器
for value in gen:
    print(f"值: {value}")
```

### 混合yield和return

```python
def generator_with_return():
    """包含return语句的生成器"""
    yield 1
    yield 2
    return "生成器结束"  # return会触发StopIteration异常
    yield 3  # 这行永远不会执行

print("\n=== 包含return的生成器 ===")
gen = generator_with_return()
try:
    print(f"值1: {next(gen)}")
    print(f"值2: {next(gen)}")
    print(f"值3: {next(gen)}")  # 这里会引发StopIteration
except StopIteration as e:
    print(f"生成器结束，返回值: {e.value}")
```

## 参数传递

生成器函数可以像普通函数一样接收参数，这些参数在生成器的整个生命周期中都可以使用。

### 基本参数传递

```python
def parameterized_generator(start, end, step=1):
    """带参数的生成器函数"""
    print(f"生成器初始化: start={start}, end={end}, step={step}")
    current = start
    while current < end:
        yield current
        current += step
    print("生成器执行完毕")

# 使用不同参数创建生成器
print("\n=== 参数传递示例 ===")
gen1 = parameterized_generator(0, 10, 2)
print("偶数生成器:")
for num in gen1:
    print(f"  {num}")

gen2 = parameterized_generator(1, 10, 3)
print("\n步长为3的生成器:")
for num in gen2:
    print(f"  {num}")
```

### 复杂参数示例

```python
def data_processor(data_source, transform_func=None, filter_func=None):
    """数据处理生成器"""
    print(f"开始处理数据源: {type(data_source).__name__}")
    
    for item in data_source:
        # 应用过滤函数
        if filter_func and not filter_func(item):
            continue
        
        # 应用转换函数
        if transform_func:
            item = transform_func(item)
        
        yield item
    
    print("数据处理完成")

# 使用示例
print("\n=== 数据处理生成器 ===")
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 只处理偶数，并计算平方
processed = data_processor(
    data,
    transform_func=lambda x: x ** 2,
    filter_func=lambda x: x % 2 == 0
)

print("处理结果:")
for result in processed:
    print(f"  {result}")
```

## 多个yield语句

生成器函数可以包含多个yield语句，每次调用next()时会执行到下一个yield。

### 顺序执行多个yield

```python
def multi_yield_generator():
    """包含多个yield的生成器"""
    print("开始执行生成器")
    
    yield "第一个值"
    print("第一个yield之后")
    
    yield "第二个值"
    print("第二个yield之后")
    
    yield "第三个值"
    print("第三个yield之后")
    
    print("生成器执行完毕")

# 逐步执行
print("\n=== 多个yield执行流程 ===")
gen = multi_yield_generator()

print(f"第1次next(): {next(gen)}")
print(f"第2次next(): {next(gen)}")
print(f"第3次next(): {next(gen)}")

try:
    print(f"第4次next(): {next(gen)}")
except StopIteration:
    print("生成器已耗尽")
```

### 条件yield

```python
def conditional_generator(items, condition):
    """根据条件yield值"""
    for item in items:
        if condition(item):
            yield f"符合条件: {item}"
        else:
            yield f"不符合条件: {item}"

# 使用条件生成器
print("\n=== 条件yield示例 ===")
numbers = [1, 2, 3, 4, 5]
gen = conditional_generator(numbers, lambda x: x % 2 == 0)

for result in gen:
    print(result)
```

## 生成器的生命周期

理解生成器的生命周期对于正确使用生成器非常重要。

### 生命周期状态

```python
import inspect

def lifecycle_demo():
    """演示生成器生命周期"""
    print("生成器函数开始执行")
    
    try:
        yield 1
        print("第一个yield之后")
        
        yield 2
        print("第二个yield之后")
        
        yield 3
        print("第三个yield之后")
        
    except GeneratorExit:
        print("生成器被关闭")
    finally:
        print("生成器清理工作")
    
    print("生成器函数结束")

# 检查生成器状态
print("\n=== 生成器生命周期 ===")
gen = lifecycle_demo()

# 检查初始状态
print(f"初始状态: {inspect.getgeneratorstate(gen)}")

# 执行第一步
value1 = next(gen)
print(f"第一个值: {value1}")
print(f"执行后状态: {inspect.getgeneratorstate(gen)}")

# 执行第二步
value2 = next(gen)
print(f"第二个值: {value2}")
print(f"执行后状态: {inspect.getgeneratorstate(gen)}")

# 关闭生成器
gen.close()
print(f"关闭后状态: {inspect.getgeneratorstate(gen)}")
```

## 生成器函数的高级特性

### 嵌套生成器

```python
def inner_generator(n):
    """内部生成器"""
    for i in range(n):
        yield f"内部-{i}"

def outer_generator(count):
    """外部生成器，包含嵌套生成器"""
    yield "开始"
    
    # 使用yield from委托给另一个生成器
    yield from inner_generator(count)
    
    yield "结束"

# 使用嵌套生成器
print("\n=== 嵌套生成器 ===")
gen = outer_generator(3)
for value in gen:
    print(value)
```

### 递归生成器

```python
def recursive_generator(data, level=0):
    """递归生成器，处理嵌套结构"""
    indent = "  " * level
    
    if isinstance(data, (list, tuple)):
        yield f"{indent}容器开始 ({type(data).__name__})"
        for item in data:
            yield from recursive_generator(item, level + 1)
        yield f"{indent}容器结束"
    else:
        yield f"{indent}值: {data}"

# 使用递归生成器
print("\n=== 递归生成器 ===")
nested_data = [1, [2, 3, [4, 5]], 6, (7, 8)]
gen = recursive_generator(nested_data)

for item in gen:
    print(item)
```

## 实际应用示例

### 批处理生成器

```python
def batch_generator(iterable, batch_size):
    """将数据分批处理的生成器"""
    iterator = iter(iterable)
    while True:
        batch = []
        try:
            for _ in range(batch_size):
                batch.append(next(iterator))
            yield batch
        except StopIteration:
            if batch:  # 如果还有剩余数据
                yield batch
            break

# 使用批处理生成器
print("\n=== 批处理生成器 ===")
data = list(range(1, 23))  # 1到22的数字
print(f"原始数据: {data}")

print("\n分批处理 (每批5个):")
for batch_num, batch in enumerate(batch_generator(data, 5), 1):
    print(f"批次 {batch_num}: {batch}")
```

### 文件处理生成器

```python
def file_processor(filename, chunk_size=1024):
    """按块读取文件的生成器"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            chunk_num = 1
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                yield chunk_num, chunk
                chunk_num += 1
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
        return

# 创建测试文件
test_content = "这是一个测试文件。" * 50  # 创建较长的内容
with open('test_file.txt', 'w', encoding='utf-8') as f:
    f.write(test_content)

# 使用文件处理生成器
print("\n=== 文件处理生成器 ===")
for chunk_num, content in file_processor('test_file.txt', 20):
    print(f"块 {chunk_num}: {content[:30]}..." if len(content) > 30 else f"块 {chunk_num}: {content}")
    if chunk_num >= 3:  # 只显示前3块
        break
```

### 数据管道生成器

```python
def data_source():
    """数据源生成器"""
    for i in range(1, 11):
        yield i

def filter_even(source):
    """过滤偶数的生成器"""
    for value in source:
        if value % 2 == 0:
            yield value

def square_values(source):
    """计算平方的生成器"""
    for value in source:
        yield value ** 2

def add_prefix(source, prefix="结果"):
    """添加前缀的生成器"""
    for value in source:
        yield f"{prefix}: {value}"

# 构建数据处理管道
print("\n=== 数据管道生成器 ===")
pipeline = add_prefix(
    square_values(
        filter_even(
            data_source()
        )
    ),
    "平方结果"
)

print("处理管道结果:")
for result in pipeline:
    print(result)
```

## 性能考虑

### 内存使用对比

```python
import sys
import time

def list_approach(n):
    """列表方式处理数据"""
    return [i ** 2 for i in range(n)]

def generator_approach(n):
    """生成器方式处理数据"""
    for i in range(n):
        yield i ** 2

# 性能对比
print("\n=== 性能对比 ===")
n = 10000

# 测试列表方式
start_time = time.time()
list_result = list_approach(n)
list_time = time.time() - start_time
list_memory = sys.getsizeof(list_result)

# 测试生成器方式
start_time = time.time()
gen_result = generator_approach(n)
gen_time = time.time() - start_time
gen_memory = sys.getsizeof(gen_result)

print(f"数据量: {n}")
print(f"列表方式 - 时间: {list_time:.6f}秒, 内存: {list_memory}字节")
print(f"生成器方式 - 时间: {gen_time:.6f}秒, 内存: {gen_memory}字节")
print(f"内存节省: {list_memory - gen_memory}字节 ({(list_memory - gen_memory) / list_memory * 100:.1f}%)")
```

## 学习要点总结

### 关键概念

1. **生成器函数定义**：包含yield关键字的函数
2. **参数传递**：生成器函数可以接收参数，在整个生命周期中使用
3. **多个yield**：函数可以包含多个yield语句，按顺序执行
4. **生命周期管理**：理解生成器的创建、执行、暂停和结束

### 最佳实践

1. **合理使用参数**：通过参数控制生成器的行为
2. **处理异常**：在生成器中适当处理异常情况
3. **资源管理**：使用try-finally确保资源正确释放
4. **文档说明**：为生成器函数编写清晰的文档

### 常见模式

- **数据转换管道**：多个生成器串联处理数据
- **批处理**：将大数据集分批处理
- **文件处理**：逐行或分块读取文件
- **无限序列**：生成无限长的数据序列

## 练习建议

1. **参数练习**：创建接收不同参数的生成器函数
2. **管道练习**：构建多层生成器处理管道
3. **文件练习**：使用生成器处理大文件
4. **性能练习**：比较生成器和列表的性能差异

通过掌握生成器函数的这些特性，你可以编写更高效、更优雅的Python代码，特别是在处理大量数据时。