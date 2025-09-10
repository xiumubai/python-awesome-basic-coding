# 生成器表达式

生成器表达式是创建生成器的简洁方式，它提供了类似列表推导式的语法，但返回生成器对象而不是列表。本节将详细介绍生成器表达式的语法、应用场景和性能优势。

## 基本语法

生成器表达式的语法与列表推导式相似，但使用圆括号而不是方括号：

```python
# 列表推导式
list_comp = [x**2 for x in range(5)]
print(f"列表推导式: {list_comp}")
print(f"类型: {type(list_comp)}")

# 生成器表达式
gen_exp = (x**2 for x in range(5))
print(f"\n生成器表达式: {gen_exp}")
print(f"类型: {type(gen_exp)}")
print(f"内容: {list(gen_exp)}")
```

### 语法结构

```python
# 基本结构
# (expression for item in iterable)

# 带条件的结构
# (expression for item in iterable if condition)

# 嵌套结构
# (expression for item1 in iterable1 for item2 in iterable2)

print("\n=== 生成器表达式语法示例 ===")

# 基本表达式
squares = (x**2 for x in range(1, 6))
print(f"平方数: {list(squares)}")

# 带条件的表达式
even_squares = (x**2 for x in range(1, 11) if x % 2 == 0)
print(f"偶数平方: {list(even_squares)}")

# 字符串处理
words = ['hello', 'world', 'python', 'generator']
upper_words = (word.upper() for word in words if len(word) > 5)
print(f"长单词大写: {list(upper_words)}")
```

## 与列表推导式的对比

### 内存使用对比

```python
import sys

def memory_comparison(n):
    """比较列表推导式和生成器表达式的内存使用"""
    print(f"\n=== 内存使用对比 (n={n}) ===")
    
    # 列表推导式
    list_comp = [x**2 for x in range(n)]
    list_size = sys.getsizeof(list_comp)
    
    # 生成器表达式
    gen_exp = (x**2 for x in range(n))
    gen_size = sys.getsizeof(gen_exp)
    
    print(f"列表推导式内存: {list_size} 字节")
    print(f"生成器表达式内存: {gen_size} 字节")
    print(f"内存节省: {list_size - gen_size} 字节")
    print(f"节省比例: {(list_size - gen_size) / list_size * 100:.1f}%")
    
    return list_comp, gen_exp

# 不同规模的对比
for size in [100, 1000, 10000]:
    list_result, gen_result = memory_comparison(size)
```

### 执行时机对比

```python
import time

def execution_timing_demo():
    """演示执行时机的差异"""
    print("\n=== 执行时机对比 ===")
    
    def expensive_operation(x):
        """模拟耗时操作"""
        time.sleep(0.01)  # 模拟计算延迟
        return x ** 2
    
    print("创建列表推导式...")
    start_time = time.time()
    list_comp = [expensive_operation(x) for x in range(5)]
    list_creation_time = time.time() - start_time
    print(f"列表创建时间: {list_creation_time:.3f}秒")
    
    print("\n创建生成器表达式...")
    start_time = time.time()
    gen_exp = (expensive_operation(x) for x in range(5))
    gen_creation_time = time.time() - start_time
    print(f"生成器创建时间: {gen_creation_time:.3f}秒")
    
    print("\n使用生成器...")
    start_time = time.time()
    gen_results = list(gen_exp)
    gen_usage_time = time.time() - start_time
    print(f"生成器使用时间: {gen_usage_time:.3f}秒")
    
    print(f"\n结果对比:")
    print(f"列表结果: {list_comp}")
    print(f"生成器结果: {gen_results}")

execution_timing_demo()
```

## 嵌套生成器表达式

### 多层嵌套

```python
print("\n=== 嵌套生成器表达式 ===")

# 二维数据处理
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 展平矩阵
flattened = (item for row in matrix for item in row)
print(f"展平矩阵: {list(flattened)}")

# 带条件的嵌套
even_items = (item for row in matrix for item in row if item % 2 == 0)
print(f"偶数元素: {list(even_items)}")

# 复杂嵌套处理
processed = (item**2 for row in matrix for item in row if item > 3)
print(f"大于3的元素的平方: {list(processed)}")
```

### 笛卡尔积

```python
# 生成笛卡尔积
colors = ['red', 'green', 'blue']
sizes = ['S', 'M', 'L']

# 使用嵌套生成器表达式
products = ((color, size) for color in colors for size in sizes)
print(f"\n产品组合: {list(products)}")

# 带条件的笛卡尔积
filtered_products = ((color, size) for color in colors for size in sizes 
                    if not (color == 'red' and size == 'S'))
print(f"过滤后的组合: {list(filtered_products)}")
```

## 实际应用场景

### 文件处理

```python
def file_processing_demo():
    """文件处理中的生成器表达式应用"""
    # 创建示例文件
    sample_data = """apple,5,1.2
banana,3,0.8
cherry,10,2.5
date,2,3.0
eggplant,7,1.8"""
    
    with open('products.csv', 'w') as f:
        f.write(sample_data)
    
    print("\n=== 文件处理应用 ===")
    
    # 读取并处理CSV数据
    with open('products.csv', 'r') as f:
        # 解析每行数据
        parsed_lines = (line.strip().split(',') for line in f if line.strip())
        
        # 转换为字典格式
        products = ({'name': parts[0], 'quantity': int(parts[1]), 'price': float(parts[2])}
                   for parts in parsed_lines)
        
        # 过滤和计算
        expensive_products = (f"{p['name']}: ${p['price']:.2f}" 
                            for p in products if p['price'] > 2.0)
        
        print("昂贵的产品:")
        for product in expensive_products:
            print(f"  {product}")

file_processing_demo()
```

### 数据转换管道

```python
def data_pipeline_demo():
    """数据转换管道示例"""
    print("\n=== 数据转换管道 ===")
    
    # 原始数据
    raw_data = [
        "  John Doe, 25, Engineer  ",
        "  Jane Smith, 30, Designer  ",
        "  Bob Johnson, 35, Manager  ",
        "  Alice Brown, 28, Developer  "
    ]
    
    # 数据清理和转换管道
    cleaned = (line.strip() for line in raw_data)
    parsed = (line.split(', ') for line in cleaned if line)
    structured = ({'name': parts[0], 'age': int(parts[1]), 'job': parts[2]}
                 for parts in parsed)
    filtered = (person for person in structured if person['age'] >= 30)
    formatted = (f"{person['name']} ({person['age']}) - {person['job']}"
                for person in filtered)
    
    print("30岁以上的员工:")
    for employee in formatted:
        print(f"  {employee}")

data_pipeline_demo()
```

### 数学计算

```python
def math_applications():
    """数学计算中的应用"""
    print("\n=== 数学计算应用 ===")
    
    # 素数生成器表达式
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = (n for n in range(2, 50) if is_prime(n))
    print(f"50以内的素数: {list(primes)}")
    
    # 斐波那契数列（前n项）
    def fibonacci_pairs(n):
        a, b = 0, 1
        for _ in range(n):
            yield a, b
            a, b = b, a + b
    
    fib_numbers = (a for a, b in fibonacci_pairs(10))
    print(f"斐波那契数列前10项: {list(fib_numbers)}")
    
    # 几何级数
    geometric_series = (2**i for i in range(10))
    print(f"2的幂次: {list(geometric_series)}")

math_applications()
```

## 性能优化技巧

### 链式生成器表达式

```python
def chained_generators_demo():
    """链式生成器表达式演示"""
    print("\n=== 链式生成器表达式 ===")
    
    # 原始数据
    numbers = range(1, 1001)
    
    # 方法1：一次性处理（内存占用大）
    result1 = [x**2 for x in numbers if x % 2 == 0 if x**2 % 3 == 0]
    
    # 方法2：链式生成器（内存占用小）
    evens = (x for x in numbers if x % 2 == 0)
    squares = (x**2 for x in evens)
    divisible_by_3 = (x for x in squares if x % 3 == 0)
    
    result2 = list(divisible_by_3)
    
    print(f"结果相同: {result1 == result2}")
    print(f"符合条件的数量: {len(result2)}")
    print(f"前10个结果: {result2[:10]}")

chained_generators_demo()
```

### 惰性求值的优势

```python
def lazy_evaluation_demo():
    """惰性求值优势演示"""
    print("\n=== 惰性求值优势 ===")
    
    def expensive_function(x):
        """模拟耗时计算"""
        print(f"  计算 {x}...")
        return x ** 3
    
    # 创建生成器（不会立即计算）
    print("创建生成器表达式...")
    cubes = (expensive_function(x) for x in range(1, 11))
    print("生成器创建完成（没有进行实际计算）")
    
    # 只取前3个值
    print("\n只取前3个值:")
    first_three = []
    for i, value in enumerate(cubes):
        if i >= 3:
            break
        first_three.append(value)
    
    print(f"前3个立方数: {first_three}")
    print("注意：只计算了需要的值，节省了计算资源")

lazy_evaluation_demo()
```

## 生成器表达式的限制

### 一次性使用

```python
def single_use_limitation():
    """演示生成器表达式的一次性使用限制"""
    print("\n=== 一次性使用限制 ===")
    
    # 创建生成器表达式
    squares = (x**2 for x in range(1, 6))
    
    # 第一次使用
    print("第一次遍历:")
    for value in squares:
        print(f"  {value}")
    
    # 第二次使用（已经耗尽）
    print("\n第二次遍历:")
    for value in squares:
        print(f"  {value}")
    print("生成器已耗尽，没有输出")
    
    # 解决方案：重新创建或使用函数
    def create_squares():
        return (x**2 for x in range(1, 6))
    
    print("\n使用函数重新创建:")
    for value in create_squares():
        print(f"  {value}")

single_use_limitation()
```

### 调试困难

```python
def debugging_challenges():
    """演示生成器表达式的调试挑战"""
    print("\n=== 调试挑战 ===")
    
    # 复杂的生成器表达式（难以调试）
    complex_gen = (x**2 for x in range(1, 11) if x % 2 == 0 if x**2 > 10)
    
    # 调试技巧1：分步创建
    print("分步调试:")
    numbers = range(1, 11)
    evens = (x for x in numbers if x % 2 == 0)
    squares = (x**2 for x in evens)
    filtered = (x for x in squares if x > 10)
    
    print(f"结果: {list(filtered)}")
    
    # 调试技巧2：添加打印语句
    def debug_function(x):
        result = x**2
        print(f"  {x}^2 = {result}")
        return result
    
    print("\n带调试信息:")
    debug_gen = (debug_function(x) for x in range(1, 6) if x % 2 == 0)
    result = list(debug_gen)
    print(f"最终结果: {result}")

debugging_challenges()
```

## 高级应用模式

### 生成器表达式作为函数参数

```python
def generator_as_argument():
    """生成器表达式作为函数参数"""
    print("\n=== 生成器表达式作为函数参数 ===")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 直接传递给函数
    total = sum(x**2 for x in numbers if x % 2 == 0)
    print(f"偶数平方和: {total}")
    
    # 最大值
    max_cube = max(x**3 for x in numbers)
    print(f"最大立方数: {max_cube}")
    
    # 任意条件检查
    has_large_square = any(x**2 > 50 for x in numbers)
    print(f"是否有平方数大于50: {has_large_square}")
    
    # 所有条件检查
    all_positive = all(x > 0 for x in numbers)
    print(f"是否都是正数: {all_positive}")

generator_as_argument()
```

### 条件生成器表达式

```python
def conditional_generators():
    """条件生成器表达式"""
    print("\n=== 条件生成器表达式 ===")
    
    data = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
    
    # 根据条件选择不同的处理方式
    processed = (x**2 if x > 0 else abs(x) for x in data)
    print(f"条件处理结果: {list(processed)}")
    
    # 多重条件
    categorized = ('large' if x > 5 else 'medium' if x > 2 else 'small' 
                  for x in range(1, 11))
    print(f"分类结果: {list(categorized)}")
    
    # 复杂条件组合
    words = ['python', 'java', 'c++', 'javascript', 'go', 'rust']
    filtered_words = (word.upper() if len(word) > 4 else word 
                     for word in words if 'a' in word)
    print(f"包含'a'的单词处理: {list(filtered_words)}")

conditional_generators()
```

## 学习要点总结

### 关键概念

1. **语法结构**：`(expression for item in iterable [if condition])`
2. **惰性求值**：只在需要时计算值，节省内存和计算资源
3. **一次性使用**：生成器表达式只能遍历一次
4. **链式处理**：可以将多个生成器表达式链接起来

### 使用场景

- **大数据处理**：处理无法完全加载到内存的数据
- **数据转换管道**：多步骤的数据处理流程
- **文件处理**：逐行处理大文件
- **数学计算**：生成数学序列和进行复杂计算

### 性能优势

1. **内存效率**：不需要存储所有中间结果
2. **计算效率**：只计算需要的值
3. **响应速度**：立即返回生成器对象
4. **可组合性**：易于构建处理管道

### 最佳实践

1. **适当使用**：在处理大量数据时优先考虑生成器表达式
2. **分步调试**：复杂表达式分步创建便于调试
3. **函数封装**：需要重复使用时封装为函数
4. **性能测试**：在关键场景下进行性能对比

## 练习建议

1. **基础练习**：将列表推导式改写为生成器表达式
2. **性能练习**：比较不同数据规模下的内存使用
3. **应用练习**：使用生成器表达式处理实际数据
4. **管道练习**：构建多层数据处理管道

生成器表达式是Python中一个非常实用的特性，掌握它可以让你编写更高效、更优雅的代码，特别是在数据处理和分析场景中。