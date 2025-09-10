# 列表推导式 (List Comprehensions)

## 学习目标

1. 理解列表推导式的基本语法
2. 掌握列表推导式的各种用法
3. 了解列表推导式的优势和适用场景
4. 学会使用条件表达式和嵌套循环

## 基本语法

列表推导式的基本语法格式：
```python
[expression for item in iterable]
[expression for item in iterable if condition]
```

## 基本列表推导式

### 简单示例

```python
# 基本语法：[expression for item in iterable]
# 创建1到10的平方数列表
squares = [x**2 for x in range(1, 11)]
print(f"1-10的平方数: {squares}")
# 输出: 1-10的平方数: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 传统方法对比
squares_traditional = []
for x in range(1, 11):
    squares_traditional.append(x**2)
print(f"传统方法结果: {squares_traditional}")
```

### 字符串处理

```python
# 字符串处理
words = ['hello', 'world', 'python', 'programming']
uppercase_words = [word.upper() for word in words]
print(f"大写单词: {uppercase_words}")
# 输出: 大写单词: ['HELLO', 'WORLD', 'PYTHON', 'PROGRAMMING']

# 数学运算
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(f"数字翻倍: {doubled}")
# 输出: 数字翻倍: [2, 4, 6, 8, 10]
```

## 带条件的列表推导式

### 条件过滤

```python
# 语法：[expression for item in iterable if condition]
# 筛选偶数
numbers = range(1, 21)
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"1-20中的偶数: {even_numbers}")
# 输出: 1-20中的偶数: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 筛选并转换
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
long_words = [word.upper() for word in words if len(word) > 5]
print(f"长度大于5的单词(大写): {long_words}")
# 输出: 长度大于5的单词(大写): ['BANANA', 'CHERRY', 'ELDERBERRY']
```

### 多重条件

```python
# 多个条件
numbers = range(1, 101)
special_numbers = [x for x in numbers if x % 3 == 0 and x % 5 == 0]
print(f"1-100中能被3和5整除的数: {special_numbers}")
# 输出: 1-100中能被3和5整除的数: [15, 30, 45, 60, 75, 90]

# 条件表达式（三元运算符）
numbers = [-5, -2, 0, 3, 8, -1, 4]
abs_or_zero = [x if x >= 0 else 0 for x in numbers]
print(f"负数变0，正数保持: {abs_or_zero}")
# 输出: 负数变0，正数保持: [0, 0, 0, 3, 8, 0, 4]
```

## 嵌套列表推导式

### 二维列表处理

```python
# 二维列表展平
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]
print(f"矩阵展平: {flattened}")
# 输出: 矩阵展平: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 创建乘法表
multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("5x5乘法表:")
for row in multiplication_table:
    print(row)
# 输出:
# [1, 2, 3, 4, 5]
# [2, 4, 6, 8, 10]
# [3, 6, 9, 12, 15]
# [4, 8, 12, 16, 20]
# [5, 10, 15, 20, 25]
```

### 笛卡尔积

```python
# 笛卡尔积
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
combinations = [(color, size) for color in colors for size in sizes]
print(f"颜色和尺寸组合: {combinations}")
# 输出: 颜色和尺寸组合: [('red', 'S'), ('red', 'M'), ('red', 'L'), ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]

# 带条件的嵌套
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
even_from_matrix = [item for row in matrix for item in row if item % 2 == 0]
print(f"矩阵中的偶数: {even_from_matrix}")
# 输出: 矩阵中的偶数: [2, 4, 6, 8, 10, 12]
```

## 字符串处理

### 字符和单词处理

```python
# 字符处理
text = "Hello World"
chars = [char for char in text if char.isalpha()]
print(f"提取字母: {''.join(chars)}")
# 输出: 提取字母: HelloWorld

# 单词处理
sentence = "Python is a powerful programming language"
words = sentence.split()
word_lengths = [len(word) for word in words]
print(f"单词长度: {word_lengths}")
# 输出: 单词长度: [6, 2, 1, 8, 11, 8]

# 首字母大写
names = ['alice', 'bob', 'charlie', 'diana']
capitalized = [name.capitalize() for name in names]
print(f"首字母大写: {capitalized}")
# 输出: 首字母大写: ['Alice', 'Bob', 'Charlie', 'Diana']
```

## 高级用法

### 使用函数

```python
# 使用函数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(2, 50) if is_prime(x)]
print(f"2-50之间的质数: {primes}")
# 输出: 2-50之间的质数: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

### 使用内置函数

```python
# 使用enumerate
fruits = ['apple', 'banana', 'cherry']
indexed_fruits = [f"{i}: {fruit}" for i, fruit in enumerate(fruits)]
print(f"带索引的水果: {indexed_fruits}")
# 输出: 带索引的水果: ['0: apple', '1: banana', '2: cherry']

# 使用zip
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
name_age_pairs = [f"{name} is {age} years old" for name, age in zip(names, ages)]
print(f"姓名年龄对: {name_age_pairs}")
# 输出: 姓名年龄对: ['Alice is 25 years old', 'Bob is 30 years old', 'Charlie is 35 years old']

# 字典的键值对
student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 96}
high_achievers = [name for name, grade in student_grades.items() if grade >= 90]
print(f"高分学生: {high_achievers}")
# 输出: 高分学生: ['Bob', 'Diana']
```

## 实际应用示例

### 数据清洗

```python
# 数据清洗
raw_data = ['  Alice  ', 'BOB', '  charlie', 'DIANA  ', '  eve  ']
cleaned_data = [name.strip().title() for name in raw_data]
print(f"清洗后的数据: {cleaned_data}")
# 输出: 清洗后的数据: ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

# 文件扩展名提取
filenames = ['document.pdf', 'image.jpg', 'script.py', 'data.csv', 'readme.txt']
extensions = [filename.split('.')[-1] for filename in filenames]
print(f"文件扩展名: {extensions}")
# 输出: 文件扩展名: ['pdf', 'jpg', 'py', 'csv', 'txt']
```

### 数据转换

```python
# 温度转换
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = [c * 9/5 + 32 for c in celsius_temps]
print(f"摄氏度转华氏度: {list(zip(celsius_temps, fahrenheit_temps))}")
# 输出: 摄氏度转华氏度: [(0, 32.0), (10, 50.0), (20, 68.0), (30, 86.0), (40, 104.0)]

# 购物车总价计算
items = [('apple', 2.5, 3), ('banana', 1.2, 5), ('orange', 3.0, 2)]
total_prices = [price * quantity for name, price, quantity in items]
print(f"商品总价: {total_prices}")
print(f"购物车总计: {sum(total_prices):.2f}")
# 输出: 商品总价: [7.5, 6.0, 6.0]
# 输出: 购物车总计: 19.50
```

## 性能对比

```python
import time

# 大数据量测试
n = 100000

# 列表推导式
start_time = time.time()
squares_comp = [x**2 for x in range(n)]
comp_time = time.time() - start_time

# 传统循环
start_time = time.time()
squares_loop = []
for x in range(n):
    squares_loop.append(x**2)
loop_time = time.time() - start_time

# map函数
start_time = time.time()
squares_map = list(map(lambda x: x**2, range(n)))
map_time = time.time() - start_time

print(f"计算{n}个数的平方:")
print(f"列表推导式: {comp_time:.4f}秒")
print(f"传统循环: {loop_time:.4f}秒")
print(f"map函数: {map_time:.4f}秒")
```

## 常见错误和注意事项

### 避免过度复杂

```python
# ❌ 避免过度复杂的表达式
numbers = [1, 2, 3, 4, 5]
# 不推荐：太复杂
# complex_result = [x**2 + 2*x + 1 if x % 2 == 0 else x**3 - x for x in numbers if x > 2]

# ✅ 推荐：分步骤或使用函数
def process_number(x):
    if x % 2 == 0:
        return x**2 + 2*x + 1
    else:
        return x**3 - x

filtered_numbers = [x for x in numbers if x > 2]
processed_numbers = [process_number(x) for x in filtered_numbers]
print(f"分步处理结果: {processed_numbers}")
```

### 内存使用注意事项

```python
# ⚠️ 大数据量时考虑使用生成器
print("列表推导式会立即创建完整列表，占用内存")
print("生成器表达式按需生成，节省内存")

# 列表推导式 - 立即创建所有元素
large_list = [x**2 for x in range(1000000)]  # 占用大量内存

# 生成器表达式 - 按需生成
large_generator = (x**2 for x in range(1000000))  # 节省内存
```

## 学习要点总结

1. **语法简洁**：列表推导式语法简洁，可读性强
2. **性能优势**：性能通常优于传统循环
3. **适用场景**：适合简单到中等复杂度的数据处理
4. **复杂度控制**：过度复杂时应考虑使用函数或传统循环
5. **内存考虑**：大数据量时考虑使用生成器表达式

## 练习建议

1. 从简单的数值计算开始练习
2. 尝试不同类型的条件过滤
3. 练习嵌套推导式的使用
4. 对比列表推导式与传统循环的性能
5. 在实际项目中应用列表推导式进行数据处理