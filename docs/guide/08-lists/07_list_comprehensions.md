# 列表推导式

## 学习目标

通过本节学习，你将掌握：
- 列表推导式的基本语法和用法
- 带条件的列表推导式
- 条件表达式在推导式中的应用
- 嵌套列表推导式
- 高级推导式技巧和最佳实践
- 性能优势和实际应用场景

## 基本列表推导式

### 语法结构

```python
# 基本语法
[expression for item in iterable]

# 等价的传统写法
result = []
for item in iterable:
    result.append(expression)
```

### 基本示例

```python
# 1. 创建数字列表
numbers = [x for x in range(10)]
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. 数学运算
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# 3. 字符串操作
words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

# 4. 字符串长度
word_lengths = [len(word) for word in words]
print(word_lengths)  # [5, 5, 6]

# 5. 类型转换
str_numbers = ['1', '2', '3', '4', '5']
int_numbers = [int(x) for x in str_numbers]
print(int_numbers)  # [1, 2, 3, 4, 5]
```

## 带条件的列表推导式

### 过滤条件语法

```python
# 带过滤条件的语法
[expression for item in iterable if condition]

# 等价的传统写法
result = []
for item in iterable:
    if condition:
        result.append(expression)
```

### 条件过滤示例

```python
numbers = list(range(1, 21))

# 1. 过滤偶数
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 2. 过滤奇数并平方
odd_squares = [x**2 for x in numbers if x % 2 == 1]
print(odd_squares)  # [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]

# 3. 字符串过滤
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
long_words = [word for word in words if len(word) > 5]
print(long_words)  # ['banana', 'cherry', 'elderberry']

# 4. 多重条件
divisible_by_3_and_5 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(divisible_by_3_and_5)  # [15, 30, 45, 60, 75, 90]

# 5. 复杂对象过滤
students = [
    {'name': 'Alice', 'age': 20, 'grade': 85},
    {'name': 'Bob', 'age': 22, 'grade': 92},
    {'name': 'Charlie', 'age': 19, 'grade': 78},
    {'name': 'Diana', 'age': 21, 'grade': 96}
]

excellent_students = [student['name'] for student in students 
                     if student['grade'] >= 90 and student['age'] >= 20]
print(excellent_students)  # ['Bob', 'Diana']
```

## 条件表达式

### 三元运算符语法

```python
# 条件表达式语法
[expression_if_true if condition else expression_if_false for item in iterable]

# 等价的传统写法
result = []
for item in iterable:
    if condition:
        result.append(expression_if_true)
    else:
        result.append(expression_if_false)
```

### 条件表达式示例

```python
numbers = list(range(1, 11))

# 1. 奇偶标签
even_odd_labels = ['偶数' if x % 2 == 0 else '奇数' for x in numbers]
print(even_odd_labels)
# ['奇数', '偶数', '奇数', '偶数', '奇数', '偶数', '奇数', '偶数', '奇数', '偶数']

# 2. 数值处理
processed_numbers = [x if x % 2 == 0 else x * 2 for x in numbers]
print(processed_numbers)  # [2, 2, 6, 4, 10, 6, 14, 8, 18, 10]

# 3. 字符串格式化
words = ['python', 'java', 'javascript', 'go', 'rust']
formatted_words = [word.upper() if len(word) <= 4 else word.title() 
                  for word in words]
print(formatted_words)  # ['PYTHON', 'JAVA', 'Javascript', 'GO', 'RUST']

# 4. 成绩等级
scores = [85, 92, 78, 96, 88, 73, 91]
grades = ['A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' 
         for score in scores]
print(grades)  # ['B', 'A', 'C', 'A', 'B', 'C', 'A']

# 5. 结合过滤条件
positive_negative = [x if x > 0 else abs(x) for x in [-3, -1, 0, 2, 5, -7] if x != 0]
print(positive_negative)  # [3, 1, 2, 5, 7]
```

## 嵌套列表推导式

### 二维列表操作

```python
# 1. 创建二维列表
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# 2. 扁平化二维列表
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. 带条件的嵌套推导式
even_from_nested = [item for sublist in nested_list for item in sublist if item % 2 == 0]
print(even_from_nested)  # [2, 4, 6, 8]

# 4. 复杂嵌套结构
words_matrix = [['hello', 'world'], ['python', 'programming']]
upper_chars = [[char.upper() for char in word] for row in words_matrix for word in row]
print(upper_chars)
# [['H', 'E', 'L', 'L', 'O'], ['W', 'O', 'R', 'L', 'D'], 
#  ['P', 'Y', 'T', 'H', 'O', 'N'], ['P', 'R', 'O', 'G', 'R', 'A', 'M', 'M', 'I', 'N', 'G']]
```

### 三维列表

```python
# 三维列表推导式
cube = [[[i+j+k for k in range(2)] for j in range(2)] for i in range(2)]
print(cube)
# [[[0, 1], [1, 2]], [[1, 2], [2, 3]]]
```

### 处理表格数据

```python
table_data = [
    ['Name', 'Age', 'City'],
    ['Alice', '25', 'New York'],
    ['Bob', '30', 'London'],
    ['Charlie', '35', 'Tokyo']
]

# 提取数据行（跳过标题）
data_rows = [row for row in table_data[1:]]
print(data_rows)

# 提取特定列（年龄）
ages = [int(row[1]) for row in table_data[1:]]
print(ages)  # [25, 30, 35]
```

## 高级推导式技巧

### 使用内置函数

```python
# 1. 使用enumerate
words = ['apple', 'banana', 'cherry']
indexed_words = [f"{i}: {word}" for i, word in enumerate(words)]
print(indexed_words)  # ['0: apple', '1: banana', '2: cherry']

# 2. 使用zip
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
name_age_pairs = [f"{name}({age})" for name, age in zip(names, ages)]
print(name_age_pairs)  # ['Alice(25)', 'Bob(30)', 'Charlie(35)']

# 3. 字符串方法链
sentences = ['  hello world  ', '  PYTHON programming  ']
cleaned = [sentence.strip().title() for sentence in sentences]
print(cleaned)  # ['Hello World', 'Python Programming']
```

### 使用自定义函数

```python
def is_prime(n):
    """判断是否为质数"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 找出质数
primes = [x for x in range(2, 50) if is_prime(x)]
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

### 处理复杂数据结构

```python
products = [
    {'name': 'Laptop', 'price': 1000, 'category': 'Electronics'},
    {'name': 'Book', 'price': 20, 'category': 'Education'},
    {'name': 'Phone', 'price': 800, 'category': 'Electronics'},
    {'name': 'Desk', 'price': 300, 'category': 'Furniture'}
]

# 提取电子产品名称
electronics = [product['name'] for product in products 
              if product['category'] == 'Electronics']
print(electronics)  # ['Laptop', 'Phone']

# 计算折扣价格
discounted_prices = [{'name': p['name'], 'discounted_price': p['price'] * 0.9} 
                    for p in products if p['price'] > 100]
print(discounted_prices)
# [{'name': 'Laptop', 'discounted_price': 900.0}, 
#  {'name': 'Phone', 'discounted_price': 720.0}, 
#  {'name': 'Desk', 'discounted_price': 270.0}]
```

## 集合和字典推导式

### 集合推导式

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# 集合推导式（自动去重）
unique_squares = {x**2 for x in numbers}
print(unique_squares)  # {1, 4, 9, 16}
```

### 字典推导式

```python
# 字典推导式
words = ['apple', 'banana', 'cherry']
word_lengths = {word: len(word) for word in words}
print(word_lengths)  # {'apple': 5, 'banana': 6, 'cherry': 6}
```

## 性能比较

### 不同方法的性能对比

```python
import time

def time_function(func, description):
    """测量函数执行时间"""
    start_time = time.time()
    result = func()
    end_time = time.time()
    print(f"{description}: {end_time - start_time:.4f}秒")
    return result

size = 100000

# 方法1：传统for循环
def traditional_method():
    result = []
    for i in range(size):
        if i % 2 == 0:
            result.append(i**2)
    return result

# 方法2：列表推导式
def comprehension_method():
    return [i**2 for i in range(size) if i % 2 == 0]

# 方法3：filter + map
def filter_map_method():
    return list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(size))))

# 性能测试
result1 = time_function(traditional_method, "传统for循环")
result2 = time_function(comprehension_method, "列表推导式")
result3 = time_function(filter_map_method, "filter+map")

print(f"结果一致性: {result1 == result2 == result3}")
```

## 最佳实践

### 1. 保持简洁

```python
# ✓ 好的做法 - 简洁明了
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]

# ✗ 避免过于复杂的表达式
# 复杂的推导式应该拆分为函数
complex_result = [x**2 + 2*x + 1 if x % 2 == 0 else x**3 - x**2 + x - 1 
                 for x in range(10) if x > 2 and x < 8]
```

### 2. 使用有意义的变量名

```python
# ✓ 好的做法
students = ['Alice', 'Bob', 'Charlie']
student_lengths = [len(name) for name in students]

# ✗ 不好的做法
# x_lengths = [len(x) for x in students]
```

### 3. 适当使用括号提高可读性

```python
# ✓ 使用括号提高可读性
result = [
    (x, x**2, x**3) 
    for x in range(1, 6) 
    if x % 2 == 1
]
```

### 4. 何时避免使用列表推导式

- 逻辑过于复杂时
- 需要异常处理时
- 有副作用的操作时
- 嵌套层次过深时

### 5. 内存考虑

```python
# 大数据集使用生成器表达式
gen = (x**2 for x in range(1000000))  # 生成器，节省内存
lst = [x**2 for x in range(1000000)]  # 列表，占用更多内存
```

## 实际应用场景

### 1. 数据清洗

```python
raw_data = ['  Alice  ', '', '  Bob  ', None, '  Charlie  ', '   ']
cleaned_data = [name.strip() for name in raw_data 
               if name and name.strip()]
print(cleaned_data)  # ['Alice', 'Bob', 'Charlie']
```

### 2. 文件处理

```python
file_names = ['document.txt', 'image.jpg', 'script.py', 'data.csv', 'photo.png']
python_files = [name for name in file_names if name.endswith('.py')]
image_files = [name for name in file_names if name.endswith(('.jpg', '.png'))]

print(python_files)  # ['script.py']
print(image_files)   # ['image.jpg', 'photo.png']
```

### 3. 数据转换

```python
csv_row = "Alice,25,Engineer,New York"
fields = [field.strip() for field in csv_row.split(',')]
print(fields)  # ['Alice', '25', 'Engineer', 'New York']
```

### 4. 数学计算

```python
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
distances = [((x**2 + y**2)**0.5) for x, y in coordinates]
print([round(d, 2) for d in distances])  # [2.24, 5.0, 7.81, 10.63]
```

### 5. 文本处理

```python
text = "Hello World Python Programming"
words = text.split()
word_info = [{'word': word, 'length': len(word), 'upper': word.upper()} 
            for word in words]
print(word_info)
# [{'word': 'Hello', 'length': 5, 'upper': 'HELLO'}, 
#  {'word': 'World', 'length': 5, 'upper': 'WORLD'}, 
#  {'word': 'Python', 'length': 6, 'upper': 'PYTHON'}, 
#  {'word': 'Programming', 'length': 11, 'upper': 'PROGRAMMING'}]
```

## 完整示例代码

```python
def demonstrate_list_comprehensions():
    """演示列表推导式的各种用法"""
    
    print("=== 基本列表推导式 ===")
    # 基本用法
    squares = [x**2 for x in range(1, 6)]
    print(f"平方数: {squares}")
    
    print("\n=== 带条件的推导式 ===")
    # 过滤偶数
    numbers = range(1, 11)
    evens = [x for x in numbers if x % 2 == 0]
    print(f"偶数: {evens}")
    
    print("\n=== 条件表达式 ===")
    # 奇偶标签
    labels = ['偶数' if x % 2 == 0 else '奇数' for x in range(1, 6)]
    print(f"标签: {labels}")
    
    print("\n=== 嵌套推导式 ===")
    # 扁平化
    nested = [[1, 2], [3, 4], [5, 6]]
    flat = [item for sublist in nested for item in sublist]
    print(f"扁平化: {flat}")
    
    print("\n=== 实际应用 ===")
    # 数据处理
    students = [
        {'name': 'Alice', 'grade': 85},
        {'name': 'Bob', 'grade': 92},
        {'name': 'Charlie', 'grade': 78}
    ]
    
    excellent = [s['name'] for s in students if s['grade'] >= 90]
    print(f"优秀学生: {excellent}")

if __name__ == "__main__":
    demonstrate_list_comprehensions()
```

## 学习要点

### 语法总结

| 类型 | 语法 | 说明 |
|------|------|------|
| 基本推导式 | `[expr for item in iterable]` | 对每个元素应用表达式 |
| 带过滤条件 | `[expr for item in iterable if condition]` | 先过滤再应用表达式 |
| 条件表达式 | `[expr1 if condition else expr2 for item in iterable]` | 根据条件选择表达式 |
| 嵌套推导式 | `[item for sublist in nested for item in sublist]` | 处理嵌套结构 |

### 优势

1. **简洁性**：代码更短，更易读
2. **性能**：通常比传统循环更快
3. **Pythonic**：符合Python编程风格
4. **安全性**：减少错误可能性

### 注意事项

1. **复杂度控制**：避免过于复杂的表达式
2. **内存使用**：大数据集考虑生成器
3. **可读性**：复杂逻辑建议使用传统循环
4. **副作用**：避免在推导式中执行有副作用的操作

## 练习建议

### 基础练习

1. 创建1-100中所有偶数的平方列表
2. 从字符串列表中提取长度大于5的单词
3. 将温度列表从摄氏度转换为华氏度
4. 创建九九乘法表的二维列表

### 进阶练习

1. 扁平化任意嵌套的列表结构
2. 从字典列表中提取满足多个条件的数据
3. 使用推导式实现矩阵转置
4. 处理CSV数据，提取和转换特定字段

### 实战练习

1. 分析日志文件，提取错误信息
2. 处理学生成绩数据，计算统计信息
3. 从API响应中提取和格式化数据
4. 实现一个数据清洗工具

通过掌握列表推导式，你将能够写出更简洁、高效的Python代码！