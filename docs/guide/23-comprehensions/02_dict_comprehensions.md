# 字典推导式 (Dictionary Comprehensions)

## 学习目标

1. 理解字典推导式的基本语法
2. 掌握字典推导式的各种用法
3. 学会使用条件表达式创建字典
4. 了解字典推导式在数据处理中的应用

## 基本语法

字典推导式的基本语法格式：
```python
{key_expression: value_expression for item in iterable}
{key_expression: value_expression for item in iterable if condition}
```

## 基本字典推导式

### 简单示例

```python
# 基本语法：{key_expression: value_expression for item in iterable}
# 创建数字和其平方的字典
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"数字平方字典: {squares_dict}")
# 输出: 数字平方字典: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 传统方法对比
squares_traditional = {}
for x in range(1, 6):
    squares_traditional[x] = x**2
print(f"传统方法结果: {squares_traditional}")
```

### 字符串处理

```python
# 字符串长度字典
words = ['apple', 'banana', 'cherry', 'date']
word_lengths = {word: len(word) for word in words}
print(f"单词长度字典: {word_lengths}")
# 输出: 单词长度字典: {'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}

# 字符ASCII码字典
chars = 'ABCDE'
ascii_dict = {char: ord(char) for char in chars}
print(f"字符ASCII码: {ascii_dict}")
# 输出: 字符ASCII码: {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69}
```

## 带条件的字典推导式

### 条件过滤

```python
# 语法：{key: value for item in iterable if condition}
# 筛选偶数平方
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"偶数平方字典: {even_squares}")
# 输出: 偶数平方字典: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# 筛选长单词
words = ['cat', 'elephant', 'dog', 'hippopotamus', 'ant', 'butterfly']
long_words = {word: len(word) for word in words if len(word) > 5}
print(f"长单词字典: {long_words}")
# 输出: 长单词字典: {'elephant': 8, 'hippopotamus': 12, 'butterfly': 9}
```

### 多重条件和条件表达式

```python
# 学生成绩筛选
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
grades = [85, 92, 78, 96, 88]
high_achievers = {student: grade for student, grade in zip(students, grades) if grade >= 90}
print(f"高分学生: {high_achievers}")
# 输出: 高分学生: {'Bob': 92, 'Diana': 96}

# 条件表达式（三元运算符）
numbers = range(-5, 6)
sign_dict = {x: 'positive' if x > 0 else 'negative' if x < 0 else 'zero' for x in numbers}
print(f"数字符号: {sign_dict}")
# 输出: 数字符号: {-5: 'negative', -4: 'negative', ..., 0: 'zero', 1: 'positive', ...}
```

## 从列表创建字典

### 使用zip组合列表

```python
# 使用zip组合两个列表
keys = ['name', 'age', 'city', 'profession']
values = ['Alice', 28, 'New York', 'Engineer']
person_dict = {k: v for k, v in zip(keys, values)}
print(f"个人信息: {person_dict}")
# 输出: 个人信息: {'name': 'Alice', 'age': 28, 'city': 'New York', 'profession': 'Engineer'}

# 使用enumerate创建索引字典
fruits = ['apple', 'banana', 'cherry', 'date']
fruit_index = {fruit: index for index, fruit in enumerate(fruits)}
print(f"水果索引: {fruit_index}")
# 输出: 水果索引: {'apple': 0, 'banana': 1, 'cherry': 2, 'date': 3}
```

### 字典操作

```python
# 反转字典
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
reversed_dict = {v: k for k, v in original_dict.items()}
print(f"原字典: {original_dict}")
print(f"反转字典: {reversed_dict}")
# 输出: 原字典: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# 输出: 反转字典: {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# 多个列表组合
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['New York', 'London', 'Tokyo']
people = {name: {'age': age, 'city': city} for name, age, city in zip(names, ages, cities)}
print(f"人员信息: {people}")
# 输出: 人员信息: {'Alice': {'age': 25, 'city': 'New York'}, 'Bob': {'age': 30, 'city': 'London'}, 'Charlie': {'age': 35, 'city': 'Tokyo'}}
```

## 字符串处理

### 字符频率统计

```python
# 字符频率统计
text = "hello world"
char_count = {char: text.count(char) for char in set(text) if char != ' '}
print(f"字符频率: {char_count}")
# 输出: 字符频率: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

# 文件扩展名统计
filenames = ['doc1.txt', 'image.jpg', 'script.py', 'data.csv', 'doc2.txt', 'photo.jpg']
extensions = [filename.split('.')[-1] for filename in filenames]
ext_count_comp = {ext: extensions.count(ext) for ext in set(extensions)}
print(f"推导式统计: {ext_count_comp}")
# 输出: 推导式统计: {'txt': 2, 'jpg': 2, 'py': 1, 'csv': 1}
```

## 嵌套字典推导式

### 二维数据结构

```python
# 创建乘法表字典
multiplication_dict = {i: {j: i*j for j in range(1, 6)} for i in range(1, 6)}
print("乘法表字典:")
for i, row in multiplication_dict.items():
    print(f"{i}: {row}")
# 输出:
# 1: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# 2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
# ...

# 学生成绩字典
students = ['Alice', 'Bob', 'Charlie']
subjects = ['Math', 'Science', 'English']
import random
random.seed(42)  # 固定随机种子

grades = {student: {subject: random.randint(70, 100) for subject in subjects} for student in students}
print(f"学生成绩: {grades}")

# 计算平均分
averages = {student: sum(scores.values()) / len(scores) for student, scores in grades.items()}
print(f"平均分: {averages}")
```

### 矩阵操作

```python
# 矩阵转置
matrix_dict = {f'row_{i}': {f'col_{j}': i*3 + j + 1 for j in range(3)} for i in range(3)}
print(f"原矩阵: {matrix_dict}")

# 转置矩阵
transposed = {f'col_{j}': {f'row_{i}': matrix_dict[f'row_{i}'][f'col_{j}'] for i in range(3)} for j in range(3)}
print(f"转置矩阵: {transposed}")
```

## 高级用法

### 使用函数处理

```python
# 使用函数处理
def categorize_number(n):
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'

numbers = range(1, 11)
number_categories = {n: categorize_number(n) for n in numbers}
print(f"数字分类: {number_categories}")
# 输出: 数字分类: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', ...}
```

### 复杂数据处理

```python
# 多条件筛选
products = [
    {'name': 'laptop', 'price': 1000, 'category': 'electronics'},
    {'name': 'book', 'price': 20, 'category': 'education'},
    {'name': 'phone', 'price': 800, 'category': 'electronics'},
    {'name': 'desk', 'price': 300, 'category': 'furniture'}
]

expensive_electronics = {
    product['name']: product['price'] 
    for product in products 
    if product['category'] == 'electronics' and product['price'] > 500
}
print(f"昂贵电子产品: {expensive_electronics}")
# 输出: 昂贵电子产品: {'laptop': 1000, 'phone': 800}
```

### 字典合并和过滤

```python
# 字典合并和过滤
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

# 合并字典，dict2的值覆盖dict1
merged = {k: dict2.get(k, dict1.get(k)) for k in set(dict1) | set(dict2)}
print(f"合并字典: {merged}")
# 输出: 合并字典: {'a': 1, 'b': 4, 'c': 5, 'd': 6}

# 筛选共同键
common_keys = {k: (dict1[k], dict2[k]) for k in dict1 if k in dict2}
print(f"共同键值: {common_keys}")
# 输出: 共同键值: {'b': (2, 4), 'c': (3, 5)}
```

## 数据转换应用

### CSV数据处理

```python
# CSV数据转换
csv_data = [
    ['Name', 'Age', 'City'],
    ['Alice', '25', 'New York'],
    ['Bob', '30', 'London'],
    ['Charlie', '35', 'Tokyo']
]

# 转换为字典列表
headers = csv_data[0]
data_dicts = [{headers[i]: row[i] for i in range(len(headers))} for row in csv_data[1:]]
print(f"CSV转字典: {data_dicts}")
# 输出: CSV转字典: [{'Name': 'Alice', 'Age': '25', 'City': 'New York'}, ...]
```

### 配置文件处理

```python
# 配置文件处理
config_lines = [
    'database_host=localhost',
    'database_port=5432',
    'debug_mode=true',
    'max_connections=100'
]

config_dict = {line.split('=')[0]: line.split('=')[1] for line in config_lines}
print(f"配置字典: {config_dict}")
# 输出: 配置字典: {'database_host': 'localhost', 'database_port': '5432', 'debug_mode': 'true', 'max_connections': '100'}

# 类型转换
def convert_value(value):
    if value.isdigit():
        return int(value)
    elif value.lower() in ['true', 'false']:
        return value.lower() == 'true'
    else:
        return value

typed_config = {k: convert_value(v) for k, v in config_dict.items()}
print(f"类型转换后: {typed_config}")
# 输出: 类型转换后: {'database_host': 'localhost', 'database_port': 5432, 'debug_mode': True, 'max_connections': 100}
```

## 性能对比

```python
import time

# 大数据量测试
n = 50000

# 字典推导式
start_time = time.time()
squares_dict_comp = {x: x**2 for x in range(n)}
comp_time = time.time() - start_time

# 传统循环
start_time = time.time()
squares_dict_loop = {}
for x in range(n):
    squares_dict_loop[x] = x**2
loop_time = time.time() - start_time

# dict()构造函数
start_time = time.time()
squares_dict_constructor = dict((x, x**2) for x in range(n))
constructor_time = time.time() - start_time

print(f"创建{n}个键值对的字典:")
print(f"字典推导式: {comp_time:.4f}秒")
print(f"传统循环: {loop_time:.4f}秒")
print(f"dict构造函数: {constructor_time:.4f}秒")
```

## 常见错误和注意事项

### 键的唯一性

```python
# ❌ 注意键的唯一性
words = ['apple', 'banana', 'apricot', 'blueberry']
# 这会导致键重复，后面的值会覆盖前面的
first_letter_dict = {word[0]: word for word in words}
print(f"首字母字典（有覆盖）: {first_letter_dict}")
# 输出: 首字母字典（有覆盖）: {'a': 'apricot', 'b': 'blueberry'}

# ✅ 正确做法：使用列表存储多个值
from collections import defaultdict
first_letter_groups = defaultdict(list)
for word in words:
    first_letter_groups[word[0]].append(word)
print(f"首字母分组（正确）: {dict(first_letter_groups)}")
# 输出: 首字母分组（正确）: {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}
```

### 空值和异常处理

```python
# ⚠️ 注意空值和异常处理
data = [('a', 1), ('b', None), ('c', 3), ('d', 0)]
# 过滤空值
filtered_dict = {k: v for k, v in data if v is not None}
print(f"过滤空值: {filtered_dict}")
# 输出: 过滤空值: {'a': 1, 'c': 3, 'd': 0}

# 处理除零错误
numbers = [1, 2, 0, 4, 5]
safe_reciprocals = {n: 1/n if n != 0 else float('inf') for n in numbers}
print(f"安全倒数: {safe_reciprocals}")
# 输出: 安全倒数: {1: 1.0, 2: 0.5, 0: inf, 4: 0.25, 5: 0.2}
```

## 学习要点总结

1. **基本语法**：`{key: value for item in iterable}`
2. **条件筛选**：可以添加条件筛选和复杂表达式
3. **数据转换**：适合数据转换和映射操作
4. **键唯一性**：注意键的唯一性，重复键会被覆盖
5. **性能优势**：性能优于传统循环，代码更简洁
6. **复杂逻辑**：复杂逻辑时考虑使用函数或传统方法

## 实际应用场景

1. **数据清洗**：过滤和转换数据
2. **配置处理**：解析配置文件
3. **数据分组**：按某个属性分组数据
4. **格式转换**：在不同数据格式间转换
5. **统计分析**：计算频率、分布等统计信息

## 练习建议

1. 从简单的键值对创建开始练习
2. 尝试不同类型的条件过滤
3. 练习嵌套字典推导式
4. 应用于实际数据处理场景
5. 对比字典推导式与传统方法的性能差异