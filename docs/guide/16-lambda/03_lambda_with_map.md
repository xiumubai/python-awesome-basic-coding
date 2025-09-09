# Lambda表达式与map函数

本节将详细介绍Lambda表达式与map函数的结合使用，这是函数式编程中最常见和最有用的组合之一。

## map函数基础

### map函数的语法

```python
# map函数的基本语法
# map(function, iterable, ...)
# 返回一个map对象（迭代器）

# 基本示例
numbers = [1, 2, 3, 4, 5]

# 使用map函数应用平方操作
squared = map(lambda x: x**2, numbers)
print(f"map对象: {squared}")
print(f"转换为列表: {list(squared)}")
```

### map函数的工作原理

```python
# map函数的工作原理演示
def demonstrate_map_process():
    """演示map函数的工作过程"""
    numbers = [1, 2, 3, 4]
    
    print("原始数据:", numbers)
    print("\nmap函数处理过程:")
    
    # 手动模拟map的工作过程
    square_func = lambda x: x**2
    result = []
    
    for i, num in enumerate(numbers):
        squared = square_func(num)
        result.append(squared)
        print(f"步骤{i+1}: {num} -> {squared}")
    
    print(f"\n最终结果: {result}")
    
    # 使用真正的map函数
    map_result = list(map(lambda x: x**2, numbers))
    print(f"map函数结果: {map_result}")
    print(f"结果相同: {result == map_result}")

demonstrate_map_process()
```

## Lambda与map的基本结合

### 数值运算

```python
# 各种数值运算示例
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. 平方运算
squares = list(map(lambda x: x**2, numbers))
print(f"平方: {squares}")

# 2. 立方运算
cubes = list(map(lambda x: x**3, numbers))
print(f"立方: {cubes}")

# 3. 平方根运算
import math
sqrt_values = list(map(lambda x: math.sqrt(x), numbers))
print(f"平方根: {[round(x, 2) for x in sqrt_values]}")

# 4. 数学表达式
expression = list(map(lambda x: 2*x + 1, numbers))
print(f"2x+1: {expression}")

# 5. 条件运算
conditional = list(map(lambda x: x if x % 2 == 0 else -x, numbers))
print(f"偶数保持，奇数变负: {conditional}")
```

### 字符串操作

```python
# 字符串处理示例
words = ['hello', 'world', 'python', 'programming', 'lambda']

# 1. 转换为大写
uppercase = list(map(lambda s: s.upper(), words))
print(f"大写: {uppercase}")

# 2. 获取字符串长度
lengths = list(map(lambda s: len(s), words))
print(f"长度: {lengths}")

# 3. 首字母大写
capitalized = list(map(lambda s: s.capitalize(), words))
print(f"首字母大写: {capitalized}")

# 4. 反转字符串
reversed_words = list(map(lambda s: s[::-1], words))
print(f"反转: {reversed_words}")

# 5. 添加前缀
prefixed = list(map(lambda s: f"prefix_{s}", words))
print(f"添加前缀: {prefixed}")

# 6. 字符串格式化
formatted = list(map(lambda s: f"'{s}' has {len(s)} characters", words))
print("格式化:")
for item in formatted:
    print(f"  {item}")
```

## 与普通函数的对比

### 使用普通函数

```python
# 使用普通函数的方式
numbers = [1, 2, 3, 4, 5]

# 定义普通函数
def square(x):
    return x ** 2

def double(x):
    return x * 2

def is_even_str(x):
    return "偶数" if x % 2 == 0 else "奇数"

# 使用普通函数
squares_func = list(map(square, numbers))
doubles_func = list(map(double, numbers))
even_odd_func = list(map(is_even_str, numbers))

print(f"普通函数 - 平方: {squares_func}")
print(f"普通函数 - 双倍: {doubles_func}")
print(f"普通函数 - 奇偶: {even_odd_func}")
```

### 使用Lambda表达式

```python
# 使用Lambda表达式的方式
numbers = [1, 2, 3, 4, 5]

# 使用Lambda
squares_lambda = list(map(lambda x: x**2, numbers))
doubles_lambda = list(map(lambda x: x*2, numbers))
even_odd_lambda = list(map(lambda x: "偶数" if x % 2 == 0 else "奇数", numbers))

print(f"Lambda - 平方: {squares_lambda}")
print(f"Lambda - 双倍: {doubles_lambda}")
print(f"Lambda - 奇偶: {even_odd_lambda}")

# 验证结果相同
print(f"\n结果验证:")
print(f"平方结果相同: {squares_func == squares_lambda}")
print(f"双倍结果相同: {doubles_func == doubles_lambda}")
print(f"奇偶结果相同: {even_odd_func == even_odd_lambda}")
```

### 代码简洁性对比

```python
# 代码行数对比
data = [1, 2, 3, 4, 5]

# 方法1：使用普通函数
def transform_data_with_functions(data):
    def square(x):
        return x ** 2
    
    def add_ten(x):
        return x + 10
    
    def to_string(x):
        return str(x)
    
    step1 = list(map(square, data))
    step2 = list(map(add_ten, step1))
    step3 = list(map(to_string, step2))
    return step3

# 方法2：使用Lambda表达式
def transform_data_with_lambda(data):
    step1 = list(map(lambda x: x**2, data))
    step2 = list(map(lambda x: x+10, step1))
    step3 = list(map(lambda x: str(x), step2))
    return step3

# 方法3：链式调用
def transform_data_chained(data):
    return list(map(lambda x: str(x), 
                   map(lambda x: x+10, 
                      map(lambda x: x**2, data))))

# 测试三种方法
result1 = transform_data_with_functions(data)
result2 = transform_data_with_lambda(data)
result3 = transform_data_chained(data)

print(f"普通函数结果: {result1}")
print(f"Lambda结果: {result2}")
print(f"链式调用结果: {result3}")
print(f"所有结果相同: {result1 == result2 == result3}")
```

## 处理多种数据类型

### 处理列表和元组

```python
# 处理嵌套数据结构
data_points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# 1. 计算每个点到原点的距离
distances = list(map(lambda point: (point[0]**2 + point[1]**2)**0.5, data_points))
print(f"到原点距离: {[round(d, 2) for d in distances]}")

# 2. 计算每个点的坐标和
coord_sums = list(map(lambda point: point[0] + point[1], data_points))
print(f"坐标和: {coord_sums}")

# 3. 格式化坐标显示
formatted_points = list(map(lambda point: f"({point[0]}, {point[1]})", data_points))
print(f"格式化坐标: {formatted_points}")

# 4. 交换x和y坐标
swapped_points = list(map(lambda point: (point[1], point[0]), data_points))
print(f"交换坐标: {swapped_points}")
```

### 处理字典数据

```python
# 处理字典列表
students = [
    {'name': 'Alice', 'age': 20, 'grade': 85},
    {'name': 'Bob', 'age': 19, 'grade': 92},
    {'name': 'Charlie', 'age': 21, 'grade': 78},
    {'name': 'Diana', 'age': 20, 'grade': 96}
]

# 1. 提取学生姓名
names = list(map(lambda student: student['name'], students))
print(f"学生姓名: {names}")

# 2. 计算年龄+成绩
age_grade_sum = list(map(lambda student: student['age'] + student['grade'], students))
print(f"年龄+成绩: {age_grade_sum}")

# 3. 创建学生简介
profiles = list(map(lambda student: f"{student['name']} ({student['age']}岁): {student['grade']}分", students))
print("学生简介:")
for profile in profiles:
    print(f"  {profile}")

# 4. 判断是否优秀（成绩>=90）
excellent = list(map(lambda student: student['grade'] >= 90, students))
print(f"是否优秀: {excellent}")

# 5. 创建新的字典结构
transformed = list(map(lambda student: {
    'full_info': f"{student['name']}_{student['age']}",
    'performance': 'excellent' if student['grade'] >= 90 else 'good' if student['grade'] >= 80 else 'average'
}, students))
print("转换后的数据:")
for item in transformed:
    print(f"  {item}")
```

### 处理混合数据类型

```python
# 处理混合数据类型
mixed_data = [1, '2', 3.0, '4', 5, '6.5', 7, '8.2']

# 1. 转换所有元素为浮点数
float_values = list(map(lambda x: float(x), mixed_data))
print(f"转换为浮点数: {float_values}")

# 2. 转换所有元素为字符串
string_values = list(map(lambda x: str(x), mixed_data))
print(f"转换为字符串: {string_values}")

# 3. 获取每个元素的类型
types = list(map(lambda x: type(x).__name__, mixed_data))
print(f"数据类型: {types}")

# 4. 安全的数值转换
def safe_float_convert(x):
    try:
        return float(x)
    except (ValueError, TypeError):
        return 0.0

safe_floats = list(map(safe_float_convert, mixed_data))
print(f"安全转换: {safe_floats}")

# 使用Lambda实现安全转换（有限制）
safe_lambda = list(map(lambda x: float(x) if str(x).replace('.', '').replace('-', '').isdigit() else 0.0, mixed_data))
print(f"Lambda安全转换: {safe_lambda}")
```

## 多个可迭代对象的处理

### 使用多个参数

```python
# map函数可以接受多个可迭代对象
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
list3 = [100, 200, 300, 400, 500]

# 1. 两个列表相加
sums = list(map(lambda x, y: x + y, list1, list2))
print(f"两列表相加: {sums}")

# 2. 两个列表相乘
products = list(map(lambda x, y: x * y, list1, list2))
print(f"两列表相乘: {products}")

# 3. 三个列表运算
triple_sum = list(map(lambda x, y, z: x + y + z, list1, list2, list3))
print(f"三列表相加: {triple_sum}")

# 4. 复杂运算
complex_calc = list(map(lambda x, y, z: (x * y) + z, list1, list2, list3))
print(f"复杂运算 (x*y)+z: {complex_calc}")

# 5. 格式化输出
formatted = list(map(lambda x, y, z: f"{x} + {y} + {z} = {x+y+z}", list1, list2, list3))
print("格式化输出:")
for item in formatted:
    print(f"  {item}")
```

### 不同长度的可迭代对象

```python
# 处理不同长度的列表
short_list = [1, 2, 3]
long_list = [10, 20, 30, 40, 50, 60]

# map会在最短的列表结束时停止
result = list(map(lambda x, y: x + y, short_list, long_list))
print(f"不同长度列表处理: {result}")
print(f"结果长度: {len(result)}")

# 演示处理过程
print("\n处理过程:")
for i, (x, y) in enumerate(zip(short_list, long_list)):
    print(f"步骤{i+1}: {x} + {y} = {x+y}")
print(f"long_list剩余元素: {long_list[len(short_list):]}")
```

## 实际应用案例

### 数据清洗和转换

```python
# 数据清洗示例
raw_data = [' Alice ', '  BOB  ', 'charlie', '  DIANA ', 'eve  ']

# 1. 清理空格并标准化格式
cleaned_names = list(map(lambda name: name.strip().title(), raw_data))
print(f"清理后的姓名: {cleaned_names}")

# 2. 处理数值数据
raw_scores = ['85', '92.5', '78', '96.2', '88.8']
scores = list(map(lambda score: round(float(score)), raw_scores))
print(f"处理后的分数: {scores}")

# 3. 处理日期字符串
date_strings = ['2024-01-15', '2024-02-20', '2024-03-10']
formatted_dates = list(map(lambda date: date.replace('-', '/'), date_strings))
print(f"格式化日期: {formatted_dates}")

# 4. 处理URL
urls = ['http://example.com', 'https://test.org', 'ftp://files.net']
domains = list(map(lambda url: url.split('//')[1] if '//' in url else url, urls))
print(f"提取域名: {domains}")
```

### 数学和科学计算

```python
# 科学计算示例
import math

# 1. 角度转弧度
angles_degrees = [0, 30, 45, 60, 90, 180, 270, 360]
angles_radians = list(map(lambda deg: math.radians(deg), angles_degrees))
print(f"角度转弧度: {[round(rad, 3) for rad in angles_radians]}")

# 2. 计算三角函数值
sin_values = list(map(lambda rad: math.sin(rad), angles_radians))
cos_values = list(map(lambda rad: math.cos(rad), angles_radians))
print(f"正弦值: {[round(val, 3) for val in sin_values]}")
print(f"余弦值: {[round(val, 3) for val in cos_values]}")

# 3. 温度转换
celsius_temps = [0, 10, 20, 30, 37, 100]
fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, celsius_temps))
kelvin_temps = list(map(lambda c: c + 273.15, celsius_temps))

print("温度转换:")
for c, f, k in zip(celsius_temps, fahrenheit_temps, kelvin_temps):
    print(f"  {c}°C = {f}°F = {k}K")

# 4. 统计计算
data_points = [1.2, 2.5, 3.8, 4.1, 5.9, 6.3, 7.7, 8.2, 9.4, 10.1]
mean = sum(data_points) / len(data_points)
deviations = list(map(lambda x: x - mean, data_points))
squared_deviations = list(map(lambda x: x**2, deviations))
variance = sum(squared_deviations) / len(squared_deviations)
std_dev = math.sqrt(variance)

print(f"\n统计计算:")
print(f"平均值: {mean:.2f}")
print(f"方差: {variance:.2f}")
print(f"标准差: {std_dev:.2f}")
print(f"偏差: {[round(d, 2) for d in deviations]}")
```

### 文本处理

```python
# 文本处理示例
sentences = [
    "Hello world",
    "Python is awesome",
    "Lambda functions are useful",
    "Map function is powerful"
]

# 1. 统计每句话的单词数
word_counts = list(map(lambda sentence: len(sentence.split()), sentences))
print(f"单词数统计: {word_counts}")

# 2. 提取每句话的第一个单词
first_words = list(map(lambda sentence: sentence.split()[0], sentences))
print(f"首单词: {first_words}")

# 3. 转换为标题格式
title_case = list(map(lambda sentence: sentence.title(), sentences))
print(f"标题格式: {title_case}")

# 4. 创建缩写
abbreviations = list(map(lambda sentence: ''.join([word[0].upper() for word in sentence.split()]), sentences))
print(f"缩写: {abbreviations}")

# 5. 统计元音字母数量
vowel_counts = list(map(lambda sentence: sum(1 for char in sentence.lower() if char in 'aeiou'), sentences))
print(f"元音字母数: {vowel_counts}")

# 6. 创建词汇表
vocabulary = list(map(lambda sentence: set(word.lower() for word in sentence.split()), sentences))
print("词汇表:")
for i, vocab in enumerate(vocabulary):
    print(f"  句子{i+1}: {vocab}")
```

## 性能考虑

### map vs 列表推导式

```python
import time

# 准备测试数据
test_data = list(range(100000))

# 方法1：使用map + lambda
start_time = time.time()
result_map = list(map(lambda x: x**2, test_data))
map_time = time.time() - start_time

# 方法2：使用列表推导式
start_time = time.time()
result_comprehension = [x**2 for x in test_data]
comprehension_time = time.time() - start_time

# 方法3：使用普通循环
start_time = time.time()
result_loop = []
for x in test_data:
    result_loop.append(x**2)
loop_time = time.time() - start_time

print(f"性能对比（处理{len(test_data)}个元素）:")
print(f"map + lambda: {map_time:.4f}秒")
print(f"列表推导式: {comprehension_time:.4f}秒")
print(f"普通循环: {loop_time:.4f}秒")

# 验证结果相同
print(f"\n结果验证:")
print(f"map == 推导式: {result_map == result_comprehension}")
print(f"map == 循环: {result_map == result_loop}")

# 内存使用对比
import sys

print(f"\n内存使用对比:")
print(f"map对象大小: {sys.getsizeof(map(lambda x: x**2, test_data[:1000]))} bytes")
print(f"列表大小: {sys.getsizeof([x**2 for x in test_data[:1000]])} bytes")
```

### 惰性求值的优势

```python
# 演示map的惰性求值
def expensive_operation(x):
    """模拟耗时操作"""
    print(f"处理 {x}...")
    time.sleep(0.01)  # 模拟耗时
    return x ** 2

data = [1, 2, 3, 4, 5]

print("创建map对象（惰性求值）:")
map_obj = map(expensive_operation, data)
print(f"map对象已创建: {map_obj}")
print("注意：此时还没有执行expensive_operation")

print("\n开始消费map对象:")
result = list(map_obj)
print(f"最终结果: {result}")

# 对比：列表推导式会立即执行
print("\n使用列表推导式（立即执行）:")
result_comprehension = [expensive_operation(x) for x in data]
print(f"结果: {result_comprehension}")
```

## 错误处理和调试

### 常见错误

```python
# 常见错误示例
data = [1, 2, 3, 4, 5]

# 错误1：忘记转换为列表
print("错误1 - 忘记转换为列表:")
map_result = map(lambda x: x**2, data)
print(f"map对象: {map_result}")  # 显示map对象，不是结果
print(f"正确做法: {list(map_result)}")

# 错误2：Lambda语法错误
try:
    # 错误的Lambda语法
    # wrong_lambda = map(lambda x: return x**2, data)  # 语法错误
    pass
except SyntaxError as e:
    print(f"错误2 - Lambda语法错误: {e}")

# 错误3：参数数量不匹配
try:
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    # 错误：Lambda需要两个参数，但只提供了一个列表
    # wrong_result = list(map(lambda x, y: x + y, list1))  # TypeError
except TypeError as e:
    print(f"错误3 - 参数不匹配: {e}")

# 错误4：处理None值
data_with_none = [1, 2, None, 4, 5]
try:
    # 这会导致TypeError
    result = list(map(lambda x: x**2, data_with_none))
except TypeError as e:
    print(f"错误4 - None值处理: {e}")
    
    # 正确的处理方式
    safe_result = list(map(lambda x: x**2 if x is not None else 0, data_with_none))
    print(f"安全处理结果: {safe_result}")
```

### 调试技巧

```python
# 调试技巧
data = [1, 2, 3, 4, 5]

# 技巧1：使用普通函数进行调试
def debug_square(x):
    print(f"调试: 输入 {x}")
    result = x ** 2
    print(f"调试: 输出 {result}")
    return result

print("使用普通函数调试:")
debug_result = list(map(debug_square, data[:3]))  # 只处理前3个元素
print(f"调试结果: {debug_result}")

# 技巧2：分步骤验证
print("\n分步骤验证:")
step1 = map(lambda x: x**2, data)
print(f"步骤1 - 创建map对象: {step1}")

step2 = list(step1)
print(f"步骤2 - 转换为列表: {step2}")

# 技巧3：使用简单的测试数据
print("\n使用简单测试数据:")
simple_data = [1, 2]
simple_result = list(map(lambda x: x**2, simple_data))
print(f"简单测试: {simple_data} -> {simple_result}")

# 技巧4：验证Lambda表达式
print("\n验证Lambda表达式:")
test_lambda = lambda x: x**2
print(f"Lambda测试: test_lambda(3) = {test_lambda(3)}")
print(f"预期结果: 9")
print(f"测试通过: {test_lambda(3) == 9}")
```

## 最佳实践

### 何时使用map + lambda

```python
# ✅ 适合使用map + lambda的场景

# 1. 简单的数据转换
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))  # 简洁明了

# 2. 类型转换
string_numbers = ['1', '2', '3', '4', '5']
integers = list(map(lambda x: int(x), string_numbers))
# 或者更简洁：integers = list(map(int, string_numbers))

# 3. 格式化输出
names = ['alice', 'bob', 'charlie']
formatted = list(map(lambda name: name.title(), names))

# 4. 简单的数学运算
temperatures_c = [0, 10, 20, 30, 40]
temperatures_f = list(map(lambda c: c * 9/5 + 32, temperatures_c))

print(f"适合的场景:")
print(f"平方: {squares}")
print(f"类型转换: {integers}")
print(f"格式化: {formatted}")
print(f"温度转换: {temperatures_f}")
```

### 何时避免使用map + lambda

```python
# ❌ 不适合使用map + lambda的场景

# 1. 复杂的逻辑 - 应该使用普通函数
def complex_grade_calculation(score):
    """复杂的成绩计算"""
    if score >= 90:
        grade = 'A'
        bonus = 5
    elif score >= 80:
        grade = 'B'
        bonus = 3
    elif score >= 70:
        grade = 'C'
        bonus = 1
    else:
        grade = 'F'
        bonus = 0
    
    final_score = min(score + bonus, 100)
    return {'grade': grade, 'final_score': final_score}

scores = [85, 92, 78, 65]
# 好的做法：使用普通函数
complex_results = list(map(complex_grade_calculation, scores))

# 2. 需要错误处理的情况
def safe_divide(x):
    """安全的除法运算"""
    try:
        return 100 / x
    except ZeroDivisionError:
        return float('inf')
    except TypeError:
        return None

data_with_issues = [1, 2, 0, '4', 5]
safe_results = list(map(safe_divide, data_with_issues))

# 3. 需要多个步骤的处理
def multi_step_processing(text):
    """多步骤文本处理"""
    # 步骤1：清理
    cleaned = text.strip().lower()
    # 步骤2：验证
    if not cleaned:
        return None
    # 步骤3：转换
    words = cleaned.split()
    # 步骤4：格式化
    return '_'.join(words)

texts = ['  Hello World  ', 'Python Programming', '  ', 'Lambda Functions']
processed_texts = list(map(multi_step_processing, texts))

print(f"\n复杂场景处理:")
print(f"成绩计算: {complex_results}")
print(f"安全除法: {safe_results}")
print(f"文本处理: {processed_texts}")
```

### 性能优化建议

```python
# 性能优化建议

# 1. 对于简单操作，考虑使用内置函数
string_numbers = ['1', '2', '3', '4', '5']

# 较慢：使用lambda
integers_lambda = list(map(lambda x: int(x), string_numbers))

# 更快：直接使用内置函数
integers_builtin = list(map(int, string_numbers))

# 2. 对于大数据集，考虑使用生成器
def process_large_dataset(data):
    """处理大数据集"""
    # 返回生成器，节省内存
    return map(lambda x: x**2, data)

large_data = range(1000000)
processed_generator = process_large_dataset(large_data)

# 只在需要时消费数据
first_10_results = [next(processed_generator) for _ in range(10)]
print(f"前10个结果: {first_10_results}")

# 3. 链式操作的优化
data = [1, 2, 3, 4, 5]

# 较慢：多次map调用
result1 = list(map(lambda x: str(x), 
                  map(lambda x: x + 10, 
                     map(lambda x: x**2, data))))

# 更快：单次map调用
result2 = list(map(lambda x: str(x**2 + 10), data))

print(f"链式操作结果1: {result1}")
print(f"链式操作结果2: {result2}")
print(f"结果相同: {result1 == result2}")
```

## 运行代码

要运行本节的示例代码，请执行：

```bash
python3 03_lambda_with_map.py
```

## 小结

Lambda表达式与map函数的结合是函数式编程的重要组成部分。主要要点包括：

### 优势：
- 代码简洁，适合简单的数据转换
- 惰性求值，节省内存
- 函数式编程风格，代码更加声明式
- 可以处理多个可迭代对象

### 适用场景：
- 简单的数学运算
- 数据类型转换
- 字符串格式化
- 基本的数据清洗

### 注意事项：
- 复杂逻辑应使用普通函数
- 需要错误处理时要谨慎
- 记住将map对象转换为列表
- 考虑性能和可读性的平衡

在下一节中，我们将学习Lambda表达式与filter函数的结合使用。