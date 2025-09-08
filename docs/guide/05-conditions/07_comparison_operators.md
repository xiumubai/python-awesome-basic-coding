# 比较运算符详解

## 概述

比较运算符是条件语句的基础，用于比较两个值之间的关系。Python提供了丰富的比较运算符，包括基本的数值比较、字符串比较、容器比较，以及特殊的身份运算符和成员运算符。掌握这些运算符的使用方法和特性，是编写有效条件判断的关键。

## 基本比较运算符

### 1. 数值比较运算符

```python
# 基本数值比较运算符
print("=== 基本数值比较运算符 ===")

a = 10
b = 20
c = 10

# 等于 (==)
print(f"{a} == {b}: {a == b}")  # False
print(f"{a} == {c}: {a == c}")  # True

# 不等于 (!=)
print(f"{a} != {b}: {a != b}")  # True
print(f"{a} != {c}: {a != c}")  # False

# 大于 (>)
print(f"{a} > {b}: {a > b}")    # False
print(f"{b} > {a}: {b > a}")    # True

# 小于 (<)
print(f"{a} < {b}: {a < b}")    # True
print(f"{b} < {a}: {b < a}")    # False

# 大于等于 (>=)
print(f"{a} >= {c}: {a >= c}")  # True
print(f"{a} >= {b}: {a >= b}")  # False

# 小于等于 (<=)
print(f"{a} <= {c}: {a <= c}")  # True
print(f"{b} <= {a}: {b <= a}")  # False

# 不同数据类型的比较
print("\n--- 不同数据类型的数值比较 ---")
int_num = 10
float_num = 10.0
print(f"int {int_num} == float {float_num}: {int_num == float_num}")  # True
print(f"int {int_num} is float {float_num}: {int_num is float_num}")  # False

# 布尔值的数值比较
print(f"True == 1: {True == 1}")    # True
print(f"False == 0: {False == 0}")  # True
print(f"True > False: {True > False}")  # True
```

### 2. 字符串比较

```python
# 字符串比较（按字典序）
print("\n=== 字符串比较 ===")

str1 = "apple"
str2 = "banana"
str3 = "Apple"
str4 = "apple"

# 基本字符串比较
print(f"'{str1}' == '{str4}': {str1 == str4}")  # True
print(f"'{str1}' == '{str3}': {str1 == str3}")  # False (大小写敏感)
print(f"'{str1}' < '{str2}': {str1 < str2}")    # True (字典序)
print(f"'{str3}' < '{str1}': {str3 < str1}")    # True (大写字母ASCII值小)

# 字符串长度比较
long_str = "application"
short_str = "app"
print(f"'{short_str}' < '{long_str}': {short_str < long_str}")  # True

# 大小写不敏感比较
print("\n--- 大小写不敏感比较 ---")
name1 = "John"
name2 = "JOHN"
print(f"'{name1}' == '{name2}': {name1 == name2}")  # False
print(f"'{name1}'.lower() == '{name2}'.lower(): {name1.lower() == name2.lower()}")  # True

# 数字字符串比较
num_str1 = "10"
num_str2 = "2"
print(f"\n--- 数字字符串比较 ---")
print(f"'{num_str1}' > '{num_str2}': {num_str1 > num_str2}")  # False (字符串比较)
print(f"int('{num_str1}') > int('{num_str2}'): {int(num_str1) > int(num_str2)}")  # True (数值比较)

# 中文字符串比较
print("\n--- 中文字符串比较 ---")
chinese1 = "苹果"
chinese2 = "香蕉"
print(f"'{chinese1}' < '{chinese2}': {chinese1 < chinese2}")  # 按Unicode编码比较
```

### 3. 列表和元组比较

```python
# 列表和元组的比较
print("\n=== 列表和元组比较 ===")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]
list4 = [1, 2]
list5 = [1, 2, 3, 4]

# 相等比较
print(f"{list1} == {list2}: {list1 == list2}")  # True
print(f"{list1} == {list3}: {list1 == list3}")  # False

# 字典序比较
print(f"{list1} < {list3}: {list1 < list3}")    # True (第三个元素3 < 4)
print(f"{list1} > {list4}: {list1 > list4}")    # True (长度更长)
print(f"{list4} < {list1}: {list4 < list1}")    # True (前缀相同，短的小于长的)

# 不同类型容器比较
tuple1 = (1, 2, 3)
print(f"list {list1} == tuple {tuple1}: {list1 == tuple1}")  # False (不同类型)

# 嵌套列表比较
nested1 = [[1, 2], [3, 4]]
nested2 = [[1, 2], [3, 5]]
print(f"{nested1} < {nested2}: {nested1 < nested2}")  # True

# 混合类型列表比较
mixed1 = [1, "apple", 3.14]
mixed2 = [1, "banana", 3.14]
print(f"{mixed1} < {mixed2}: {mixed1 < mixed2}")  # True ("apple" < "banana")
```

## 身份运算符 (is / is not)

### 1. 基本用法

```python
# 身份运算符基本用法
print("\n=== 身份运算符 (is / is not) ===")

# 基本类型的身份比较
a = 10
b = 10
c = a

print(f"a is b: {a is b}")      # True (小整数缓存)
print(f"a is c: {a is c}")      # True (同一对象)
print(f"a == b: {a == b}")      # True (值相等)

# 大整数的身份比较
big_a = 1000
big_b = 1000
print(f"big_a is big_b: {big_a is big_b}")  # False (不同对象)
print(f"big_a == big_b: {big_a == big_b}")  # True (值相等)

# 字符串的身份比较
str_a = "hello"
str_b = "hello"
str_c = "hel" + "lo"
print(f"str_a is str_b: {str_a is str_b}")  # True (字符串驻留)
print(f"str_a is str_c: {str_a is str_c}")  # 可能True或False (取决于实现)

# 列表的身份比较
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a
print(f"list_a is list_b: {list_a is list_b}")  # False (不同对象)
print(f"list_a is list_c: {list_a is list_c}")  # True (同一对象)
print(f"list_a == list_b: {list_a == list_b}")  # True (值相等)
```

### 2. None 的比较

```python
# None 的正确比较方式
print("\n--- None 的比较 ---")

value = None
other_value = 0
empty_list = []

# 正确的 None 检查
print(f"value is None: {value is None}")          # True
print(f"value is not None: {value is not None}")  # False

# 错误的 None 检查（不推荐）
print(f"value == None: {value == None}")          # True，但不推荐

# None 与其他"假值"的区别
print(f"other_value is None: {other_value is None}")    # False
print(f"empty_list is None: {empty_list is None}")      # False
print(f"bool(other_value): {bool(other_value)}")        # False
print(f"bool(empty_list): {bool(empty_list)}")          # False
print(f"bool(None): {bool(None)}")                      # False

# 实际应用：函数默认参数
def process_data(data=None):
    if data is None:
        data = []  # 创建新列表
        print("使用默认空列表")
    else:
        print(f"处理提供的数据: {data}")
    return data

result1 = process_data()
result2 = process_data([1, 2, 3])
result3 = process_data([])
```

### 3. 身份运算符的实际应用

```python
# 身份运算符的实际应用场景
print("\n--- 身份运算符实际应用 ---")

class Singleton:
    """单例模式示例"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# 测试单例模式
obj1 = Singleton()
obj2 = Singleton()
print(f"obj1 is obj2: {obj1 is obj2}")  # True

# 检查对象类型
class MyClass:
    pass

obj = MyClass()
print(f"type(obj) is MyClass: {type(obj) is MyClass}")  # True
print(f"isinstance(obj, MyClass): {isinstance(obj, MyClass)}")  # True (推荐)

# 检查布尔值
result = True
print(f"result is True: {result is True}")    # True
print(f"result == True: {result == True}")    # True

# 但是对于条件判断，直接使用布尔值更好
if result:  # 推荐
    print("条件为真")

if result is True:  # 不推荐
    print("条件为真")
```

## 成员运算符 (in / not in)

### 1. 基本用法

```python
# 成员运算符基本用法
print("\n=== 成员运算符 (in / not in) ===")

# 列表中的成员检查
fruits = ["apple", "banana", "orange", "grape"]
print(f"'apple' in fruits: {'apple' in fruits}")        # True
print(f"'mango' in fruits: {'mango' in fruits}")        # False
print(f"'mango' not in fruits: {'mango' not in fruits}")  # True

# 字符串中的子串检查
text = "Hello, World!"
print(f"'Hello' in text: {'Hello' in text}")      # True
print(f"'world' in text: {'world' in text}")      # False (大小写敏感)
print(f"'World' in text: {'World' in text}")      # True
print(f"'xyz' not in text: {'xyz' not in text}")  # True

# 字典中的键检查
user_info = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(f"'name' in user_info: {'name' in user_info}")      # True
print(f"'email' in user_info: {'email' in user_info}")    # False
print(f"'Alice' in user_info: {'Alice' in user_info}")    # False (检查键，不是值)

# 检查字典的值
print(f"'Alice' in user_info.values(): {'Alice' in user_info.values()}")  # True

# 元组中的成员检查
coordinates = (10, 20, 30)
print(f"20 in coordinates: {20 in coordinates}")    # True
print(f"40 in coordinates: {40 in coordinates}")    # False

# 集合中的成员检查
tags = {"python", "programming", "tutorial"}
print(f"'python' in tags: {'python' in tags}")      # True
print(f"'java' in tags: {'java' in tags}")          # False
```

### 2. 复杂成员检查

```python
# 复杂的成员检查
print("\n--- 复杂成员检查 ---")

# 嵌套列表的成员检查
matrix = [[1, 2], [3, 4], [5, 6]]
print(f"[1, 2] in matrix: {[1, 2] in matrix}")      # True
print(f"1 in matrix: {1 in matrix}")                # False (1不是直接成员)

# 检查嵌套列表中的元素
found = False
for row in matrix:
    if 1 in row:
        found = True
        break
print(f"1 found in matrix: {found}")  # True

# 使用any()简化嵌套检查
found_any = any(1 in row for row in matrix)
print(f"1 found using any(): {found_any}")  # True

# 多维度成员检查
students = [
    {"name": "Alice", "grades": [85, 90, 88]},
    {"name": "Bob", "grades": [78, 85, 92]},
    {"name": "Charlie", "grades": [90, 95, 87]}
]

# 检查是否有学生叫Alice
has_alice = any(student["name"] == "Alice" for student in students)
print(f"Has student named Alice: {has_alice}")  # True

# 检查是否有学生得过满分
has_perfect_score = any(100 in student["grades"] for student in students)
print(f"Has perfect score: {has_perfect_score}")  # False

# 检查是否有学生得过90分以上
has_high_score = any(any(grade >= 90 for grade in student["grades"]) for student in students)
print(f"Has high score (>=90): {has_high_score}")  # True
```

### 3. 成员运算符的性能考虑

```python
# 成员运算符的性能比较
import time

print("\n--- 成员运算符性能比较 ---")

# 创建测试数据
large_list = list(range(10000))
large_set = set(range(10000))
large_dict = {i: f"value_{i}" for i in range(10000)}

target = 9999  # 查找最后一个元素（最坏情况）

# 列表查找性能
start_time = time.time()
for _ in range(1000):
    result = target in large_list
list_time = time.time() - start_time

# 集合查找性能
start_time = time.time()
for _ in range(1000):
    result = target in large_set
set_time = time.time() - start_time

# 字典键查找性能
start_time = time.time()
for _ in range(1000):
    result = target in large_dict
dict_time = time.time() - start_time

print(f"列表查找时间: {list_time:.4f}秒")
print(f"集合查找时间: {set_time:.4f}秒")
print(f"字典查找时间: {dict_time:.4f}秒")
print(f"集合比列表快: {list_time/set_time:.1f}倍")

# 实际应用建议
print("\n性能建议:")
print("- 频繁查找操作使用set或dict")
print("- 少量数据或偶尔查找可以使用list")
print("- 需要保持顺序且频繁查找考虑OrderedDict")
```

## 链式比较

### 1. 基本链式比较

```python
# 链式比较
print("\n=== 链式比较 ===")

age = 25
score = 85
temperature = 22

# 基本链式比较
print(f"18 <= age <= 65: {18 <= age <= 65}")        # True
print(f"0 <= score <= 100: {0 <= score <= 100}")    # True
print(f"20 < temperature < 30: {20 < temperature < 30}")  # True

# 等价的非链式写法
print(f"age >= 18 and age <= 65: {age >= 18 and age <= 65}")  # True

# 复杂链式比较
x, y, z = 5, 10, 15
print(f"x < y < z: {x < y < z}")          # True
print(f"x < y > z: {x < y > z}")          # False (10 > 15 为False)
print(f"x <= y <= z: {x <= y <= z}")      # True

# 字符串链式比较
name = "Bob"
print(f"'A' <= name <= 'Z': {'A' <= name <= 'Z'}")  # False
print(f"'A' <= name[0] <= 'Z': {'A' <= name[0] <= 'Z'}")  # True

# 实际应用：范围检查
def check_grade(grade):
    if 0 <= grade <= 100:
        if 90 <= grade <= 100:
            return "A"
        elif 80 <= grade < 90:
            return "B"
        elif 70 <= grade < 80:
            return "C"
        elif 60 <= grade < 70:
            return "D"
        else:
            return "F"
    else:
        return "Invalid grade"

test_grades = [95, 85, 75, 65, 55, 105, -10]
for grade in test_grades:
    result = check_grade(grade)
    print(f"Grade {grade}: {result}")
```

### 2. 链式比较的注意事项

```python
# 链式比较的注意事项
print("\n--- 链式比较注意事项 ---")

# 意外的链式比较结果
a, b, c = 1, 2, 1
print(f"a < b > c: {a < b > c}")  # True (1 < 2 and 2 > 1)
print(f"a < b < c: {a < b < c}")  # False (1 < 2 and 2 < 1)

# 混合类型的链式比较（需要小心）
num = 5
text = "10"
# print(f"0 < num < text")  # 会报错，不能比较int和str

# 正确的做法
if isinstance(text, str) and text.isdigit():
    text_num = int(text)
    print(f"0 < num < text_num: {0 < num < text_num}")  # True

# 浮点数精度问题
float_val = 0.1 + 0.2
print(f"float_val: {float_val}")  # 0.30000000000000004
print(f"0.3 <= float_val <= 0.3: {0.3 <= float_val <= 0.3}")  # False

# 正确处理浮点数比较
import math
print(f"math.isclose(float_val, 0.3): {math.isclose(float_val, 0.3)}")  # True
```

## 浮点数比较的特殊考虑

### 1. 浮点数精度问题

```python
# 浮点数比较的特殊处理
print("\n=== 浮点数比较特殊处理 ===")

# 浮点数精度问题演示
a = 0.1 + 0.2
b = 0.3
print(f"0.1 + 0.2 = {a}")
print(f"0.3 = {b}")
print(f"a == b: {a == b}")  # False！
print(f"a - b: {a - b}")    # 很小的差值

# 解决方案1：使用math.isclose()
import math
print(f"math.isclose(a, b): {math.isclose(a, b)}")  # True

# 解决方案2：使用epsilon比较
epsilon = 1e-9
print(f"abs(a - b) < epsilon: {abs(a - b) < epsilon}")  # True

# 解决方案3：使用decimal模块
from decimal import Decimal
dec_a = Decimal('0.1') + Decimal('0.2')
dec_b = Decimal('0.3')
print(f"Decimal comparison: {dec_a == dec_b}")  # True

# 实际应用：金融计算
def safe_float_compare(x, y, tolerance=1e-9):
    """安全的浮点数比较"""
    return abs(x - y) < tolerance

def calculate_discount(price, discount_rate):
    """计算折扣价格"""
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    
    # 检查是否为整数价格
    if safe_float_compare(final_price, round(final_price)):
        return round(final_price)
    else:
        return round(final_price, 2)

test_prices = [99.99, 100.00, 50.50]
test_discount = 0.1  # 10%折扣

for price in test_prices:
    discounted = calculate_discount(price, test_discount)
    print(f"原价: ${price}, 折扣后: ${discounted}")
```

### 2. 浮点数范围比较

```python
# 浮点数范围比较的最佳实践
print("\n--- 浮点数范围比较 ---")

def is_in_range(value, min_val, max_val, tolerance=1e-9):
    """检查浮点数是否在指定范围内"""
    return (min_val - tolerance) <= value <= (max_val + tolerance)

def classify_temperature(temp):
    """根据温度分类天气"""
    if is_in_range(temp, -273.15, -273.15):  # 绝对零度
        return "绝对零度"
    elif temp < 0:
        return "冰点以下"
    elif is_in_range(temp, 0, 0):  # 冰点
        return "冰点"
    elif 0 < temp < 10:
        return "寒冷"
    elif 10 <= temp < 20:
        return "凉爽"
    elif 20 <= temp < 30:
        return "温暖"
    elif temp >= 30:
        return "炎热"
    else:
        return "未知"

# 测试温度分类
test_temps = [-273.15, -10.5, 0.0, 0.000001, 15.7, 25.3, 35.8]
for temp in test_temps:
    category = classify_temperature(temp)
    print(f"温度 {temp}°C: {category}")

# 科学计算中的比较
def compare_scientific_values(a, b, relative_tolerance=1e-6):
    """科学计算中的相对误差比较"""
    if a == 0 and b == 0:
        return True
    if a == 0 or b == 0:
        return abs(a - b) < relative_tolerance
    
    relative_error = abs((a - b) / max(abs(a), abs(b)))
    return relative_error < relative_tolerance

# 测试科学计算比较
scientific_pairs = [
    (1e10, 1e10 + 1),      # 大数值的小差异
    (1e-10, 1.1e-10),      # 小数值的相对差异
    (0, 1e-15),            # 零值比较
    (3.14159, 22/7)        # π的近似值
]

for a, b in scientific_pairs:
    is_close = compare_scientific_values(a, b)
    print(f"{a} ≈ {b}: {is_close}")
```

## 实际应用场景

### 1. 成绩评定系统

```python
# 完整的成绩评定系统
class GradeEvaluator:
    def __init__(self):
        self.grade_boundaries = {
            'A+': (97, 100),
            'A': (93, 96),
            'A-': (90, 92),
            'B+': (87, 89),
            'B': (83, 86),
            'B-': (80, 82),
            'C+': (77, 79),
            'C': (73, 76),
            'C-': (70, 72),
            'D+': (67, 69),
            'D': (63, 66),
            'D-': (60, 62),
            'F': (0, 59)
        }
    
    def get_letter_grade(self, score):
        """根据分数获取字母等级"""
        if not (0 <= score <= 100):
            return "Invalid Score"
        
        for grade, (min_score, max_score) in self.grade_boundaries.items():
            if min_score <= score <= max_score:
                return grade
        
        return "Unknown"
    
    def get_gpa_point(self, letter_grade):
        """根据字母等级获取GPA点数"""
        gpa_mapping = {
            'A+': 4.0, 'A': 4.0, 'A-': 3.7,
            'B+': 3.3, 'B': 3.0, 'B-': 2.7,
            'C+': 2.3, 'C': 2.0, 'C-': 1.7,
            'D+': 1.3, 'D': 1.0, 'D-': 0.7,
            'F': 0.0
        }
        return gpa_mapping.get(letter_grade, 0.0)
    
    def evaluate_student(self, student_data):
        """评估学生综合成绩"""
        name = student_data['name']
        scores = student_data['scores']
        weights = student_data.get('weights', [1] * len(scores))
        
        # 计算加权平均分
        if len(scores) != len(weights):
            raise ValueError("分数和权重数量不匹配")
        
        weighted_sum = sum(score * weight for score, weight in zip(scores, weights))
        total_weight = sum(weights)
        average_score = weighted_sum / total_weight
        
        # 获取等级和GPA
        letter_grade = self.get_letter_grade(average_score)
        gpa_point = self.get_gpa_point(letter_grade)
        
        # 生成评价
        evaluation = self.generate_evaluation(average_score, scores)
        
        return {
            'name': name,
            'average_score': round(average_score, 2),
            'letter_grade': letter_grade,
            'gpa_point': gpa_point,
            'evaluation': evaluation,
            'individual_scores': scores
        }
    
    def generate_evaluation(self, average_score, individual_scores):
        """生成详细评价"""
        evaluation = []
        
        # 总体表现评价
        if average_score >= 90:
            evaluation.append("优秀的学术表现")
        elif average_score >= 80:
            evaluation.append("良好的学术表现")
        elif average_score >= 70:
            evaluation.append("中等的学术表现")
        elif average_score >= 60:
            evaluation.append("及格的学术表现")
        else:
            evaluation.append("需要改进的学术表现")
        
        # 成绩稳定性分析
        if len(individual_scores) > 1:
            score_range = max(individual_scores) - min(individual_scores)
            if score_range <= 5:
                evaluation.append("成绩非常稳定")
            elif score_range <= 10:
                evaluation.append("成绩较为稳定")
            elif score_range <= 20:
                evaluation.append("成绩有一定波动")
            else:
                evaluation.append("成绩波动较大，需要关注")
        
        # 具体建议
        if average_score < 60:
            evaluation.append("建议加强基础知识学习")
        elif 60 <= average_score < 80:
            evaluation.append("建议提高学习方法效率")
        elif 80 <= average_score < 90:
            evaluation.append("继续保持，争取更大进步")
        else:
            evaluation.append("表现卓越，可以挑战更高难度")
        
        return "; ".join(evaluation)

# 测试成绩评定系统
print("\n=== 成绩评定系统测试 ===")
evaluator = GradeEvaluator()

test_students = [
    {
        'name': '张三',
        'scores': [95, 88, 92, 90],
        'weights': [0.3, 0.2, 0.3, 0.2]  # 期末、期中、作业、出勤
    },
    {
        'name': '李四',
        'scores': [78, 82, 75, 85],
        'weights': [0.3, 0.2, 0.3, 0.2]
    },
    {
        'name': '王五',
        'scores': [65, 70, 68, 72],
        'weights': [0.3, 0.2, 0.3, 0.2]
    },
    {
        'name': '赵六',
        'scores': [45, 55, 50, 60],
        'weights': [0.3, 0.2, 0.3, 0.2]
    }
]

for student in test_students:
    result = evaluator.evaluate_student(student)
    print(f"\n学生: {result['name']}")
    print(f"各科成绩: {result['individual_scores']}")
    print(f"平均分: {result['average_score']}")
    print(f"等级: {result['letter_grade']}")
    print(f"GPA: {result['gpa_point']}")
    print(f"评价: {result['evaluation']}")
```

### 2. 用户权限检查系统

```python
# 用户权限检查系统
class UserPermissionChecker:
    def __init__(self):
        self.permission_levels = {
            'guest': 0,
            'user': 1,
            'moderator': 2,
            'admin': 3,
            'superadmin': 4
        }
        
        self.resource_requirements = {
            'public_content': 0,
            'user_profile': 1,
            'user_content': 1,
            'moderate_content': 2,
            'admin_panel': 3,
            'system_config': 4
        }
    
    def check_basic_permission(self, user_role, required_resource):
        """检查基础权限"""
        user_level = self.permission_levels.get(user_role, -1)
        required_level = self.resource_requirements.get(required_resource, 999)
        
        if user_level == -1:
            return False, "无效的用户角色"
        
        if required_level == 999:
            return False, "无效的资源类型"
        
        if user_level >= required_level:
            return True, "权限检查通过"
        else:
            return False, f"权限不足，需要 {required_level} 级权限，当前为 {user_level} 级"
    
    def check_advanced_permission(self, user_data, resource, action):
        """高级权限检查"""
        # 基础权限检查
        basic_ok, basic_msg = self.check_basic_permission(user_data['role'], resource)
        if not basic_ok:
            return False, basic_msg
        
        # 账户状态检查
        if not user_data.get('is_active', False):
            return False, "账户未激活"
        
        if user_data.get('is_banned', False):
            return False, "账户已被禁用"
        
        # 时间限制检查
        import datetime
        last_login = user_data.get('last_login')
        if last_login:
            days_since_login = (datetime.datetime.now() - last_login).days
            if days_since_login > 90:
                return False, "账户长时间未登录，需要重新验证"
        
        # 特殊操作的额外检查
        if action in ['delete', 'ban_user', 'modify_system']:
            if not user_data.get('has_2fa', False):
                return False, "敏感操作需要双因素认证"
        
        # 部门限制检查
        if resource == 'department_data':
            user_dept = user_data.get('department')
            resource_dept = user_data.get('target_department')
            
            if user_data['role'] != 'superadmin':
                if user_dept != resource_dept:
                    return False, "无法访问其他部门的数据"
        
        # 时间窗口限制
        if action == 'financial_operation':
            current_hour = datetime.datetime.now().hour
            if not (9 <= current_hour <= 17):  # 工作时间
                return False, "财务操作仅限工作时间（9:00-17:00）"
        
        return True, "高级权限检查通过"
    
    def get_accessible_resources(self, user_data):
        """获取用户可访问的资源列表"""
        accessible = []
        
        for resource in self.resource_requirements:
            can_access, _ = self.check_advanced_permission(user_data, resource, 'read')
            if can_access:
                accessible.append(resource)
        
        return accessible

# 测试权限检查系统
print("\n=== 用户权限检查系统测试 ===")
import datetime

permission_checker = UserPermissionChecker()

test_users = [
    {
        'name': '普通用户',
        'role': 'user',
        'is_active': True,
        'is_banned': False,
        'has_2fa': False,
        'last_login': datetime.datetime.now() - datetime.timedelta(days=5),
        'department': 'sales'
    },
    {
        'name': '管理员',
        'role': 'admin',
        'is_active': True,
        'is_banned': False,
        'has_2fa': True,
        'last_login': datetime.datetime.now() - datetime.timedelta(days=1),
        'department': 'IT'
    },
    {
        'name': '被禁用用户',
        'role': 'user',
        'is_active': True,
        'is_banned': True,
        'has_2fa': False,
        'last_login': datetime.datetime.now() - datetime.timedelta(days=10),
        'department': 'marketing'
    },
    {
        'name': '长期未登录用户',
        'role': 'moderator',
        'is_active': True,
        'is_banned': False,
        'has_2fa': False,
        'last_login': datetime.datetime.now() - datetime.timedelta(days=100),
        'department': 'support'
    }
]

test_scenarios = [
    ('public_content', 'read'),
    ('user_profile', 'read'),
    ('admin_panel', 'read'),
    ('system_config', 'delete'),
    ('department_data', 'read')
]

for user in test_users:
    print(f"\n--- {user['name']} ({user['role']}) ---")
    
    # 测试各种权限场景
    for resource, action in test_scenarios:
        # 为部门数据测试设置目标部门
        if resource == 'department_data':
            user['target_department'] = user['department']  # 同部门
        
        can_access, message = permission_checker.check_advanced_permission(user, resource, action)
        status = "✅" if can_access else "❌"
        print(f"{status} {resource} ({action}): {message}")
    
    # 显示可访问的资源
    accessible = permission_checker.get_accessible_resources(user)
    print(f"可访问资源: {', '.join(accessible) if accessible else '无'}")
```

### 3. 数据验证系统

```python
# 数据验证系统
class DataValidator:
    def __init__(self):
        self.validation_rules = {}
    
    def add_rule(self, field_name, rule_func, error_message):
        """添加验证规则"""
        if field_name not in self.validation_rules:
            self.validation_rules[field_name] = []
        self.validation_rules[field_name].append((rule_func, error_message))
    
    def validate_data(self, data):
        """验证数据"""
        errors = {}
        
        for field_name, rules in self.validation_rules.items():
            field_value = data.get(field_name)
            field_errors = []
            
            for rule_func, error_message in rules:
                try:
                    if not rule_func(field_value):
                        field_errors.append(error_message)
                except Exception as e:
                    field_errors.append(f"验证规则执行错误: {str(e)}")
            
            if field_errors:
                errors[field_name] = field_errors
        
        return len(errors) == 0, errors
    
    def validate_email(self, email):
        """邮箱验证规则"""
        if not email:
            return False
        
        # 基本格式检查
        if '@' not in email or '.' not in email:
            return False
        
        # 长度检查
        if not (5 <= len(email) <= 100):
            return False
        
        # 分割检查
        parts = email.split('@')
        if len(parts) != 2:
            return False
        
        local, domain = parts
        if len(local) < 1 or len(domain) < 3:
            return False
        
        # 域名检查
        if '.' not in domain:
            return False
        
        return True
    
    def validate_phone(self, phone):
        """手机号验证规则"""
        if not phone:
            return False
        
        # 移除非数字字符
        digits = ''.join(filter(str.isdigit, phone))
        
        # 中国手机号格式
        if len(digits) == 11 and digits.startswith('1'):
            return digits[1] in '3456789'
        
        return False
    
    def validate_password_strength(self, password):
        """密码强度验证"""
        if not password:
            return False
        
        # 长度检查
        if not (8 <= len(password) <= 50):
            return False
        
        # 复杂度检查
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password)
        
        complexity_count = sum([has_upper, has_lower, has_digit, has_special])
        return complexity_count >= 3
    
    def validate_age_range(self, age_str, min_age=0, max_age=150):
        """年龄范围验证"""
        try:
            age = int(age_str)
            return min_age <= age <= max_age
        except (ValueError, TypeError):
            return False
    
    def validate_url(self, url):
        """URL格式验证"""
        if not url:
            return False
        
        url = url.lower()
        return url.startswith(('http://', 'https://')) and '.' in url
    
    def validate_credit_card(self, card_number):
        """信用卡号验证（Luhn算法）"""
        if not card_number:
            return False
        
        # 移除非数字字符
        digits = ''.join(filter(str.isdigit, card_number))
        
        # 长度检查
        if not (13 <= len(digits) <= 19):
            return False
        
        # Luhn算法验证
        def luhn_check(card_num):
            digits = [int(d) for d in card_num]
            for i in range(len(digits) - 2, -1, -2):
                digits[i] *= 2
                if digits[i] > 9:
                    digits[i] -= 9
            return sum(digits) % 10 == 0
        
        return luhn_check(digits)

# 创建验证器并添加规则
print("\n=== 数据验证系统测试 ===")
validator = DataValidator()

# 添加验证规则
validator.add_rule('email', validator.validate_email, '邮箱格式不正确')
validator.add_rule('phone', validator.validate_phone, '手机号格式不正确')
validator.add_rule('password', validator.validate_password_strength, '密码强度不足')
validator.add_rule('age', lambda x: validator.validate_age_range(x, 13, 100), '年龄必须在13-100岁之间')
validator.add_rule('website', validator.validate_url, '网站URL格式不正确')
validator.add_rule('credit_card', validator.validate_credit_card, '信用卡号格式不正确')

# 添加自定义规则
validator.add_rule('username', 
                  lambda x: x and 3 <= len(x) <= 20 and x.isalnum(), 
                  '用户名必须是3-20位字母数字组合')

validator.add_rule('confirm_password', 
                  lambda x: x == test_data.get('password', ''), 
                  '确认密码与密码不一致')

# 测试数据
test_datasets = [
    {
        'name': '有效数据',
        'data': {
            'username': 'john123',
            'email': 'john@example.com',
            'phone': '13812345678',
            'password': 'SecurePass123!',
            'confirm_password': 'SecurePass123!',
            'age': '25',
            'website': 'https://example.com',
            'credit_card': '4532015112830366'  # 有效的测试卡号
        }
    },
    {
        'name': '无效数据',
        'data': {
            'username': 'jo',  # 太短
            'email': 'invalid-email',  # 格式错误
            'phone': '123',  # 格式错误
            'password': '123',  # 太简单
            'confirm_password': '456',  # 不匹配
            'age': '200',  # 超出范围
            'website': 'not-a-url',  # 格式错误
            'credit_card': '1234567890'  # 无效卡号
        }
    },
    {
        'name': '部分有效数据',
        'data': {
            'username': 'alice2024',
            'email': 'alice@company.org',
            'phone': '13987654321',
            'password': 'WeakPass',  # 缺少数字和特殊字符
            'confirm_password': 'WeakPass',
            'age': '30',
            'website': 'http://alice-blog.com',
            'credit_card': ''  # 空值
        }
    }
]

for test_case in test_datasets:
    print(f"\n--- {test_case['name']} ---")
    test_data = test_case['data']
    
    # 为确认密码验证更新规则
    validator.validation_rules['confirm_password'] = [
        (lambda x: x == test_data.get('password', ''), '确认密码与密码不一致')
    ]
    
    is_valid, errors = validator.validate_data(test_data)
    
    if is_valid:
        print("✅ 所有数据验证通过")
    else:
        print("❌ 数据验证失败")
        for field, field_errors in errors.items():
            print(f"  {field}: {', '.join(field_errors)}")
    
    print(f"验证结果: {'通过' if is_valid else '失败'}")
```

## 练习题

### 基础练习

1. **数值比较练习**：
   - 编写函数判断三个数的大小关系
   - 实现数值范围检查功能
   - 处理不同数据类型的比较

2. **字符串比较练习**：
   - 实现大小写不敏感的字符串比较
   - 编写字符串排序函数
   - 实现模糊匹配功能

3. **容器比较练习**：
   - 比较两个列表的相似度
   - 实现集合的包含关系检查
   - 编写字典差异比较函数

### 进阶练习

1. **身份运算符练习**：
   - 实现对象缓存系统
   - 编写单例模式检查器
   - 实现内存优化的数据结构

2. **成员运算符练习**：
   - 实现高效的数据查找系统
   - 编写权限检查中间件
   - 实现标签过滤功能

3. **链式比较练习**：
   - 实现复杂的数据验证规则
   - 编写数学区间运算
   - 实现多维度数据筛选

### 挑战练习

1. **浮点数比较系统**：
   - 实现科学计算中的精确比较
   - 编写金融计算的安全比较
   - 实现自适应精度的比较算法

2. **综合比较系统**：
   - 实现通用的数据比较框架
   - 编写性能优化的比较算法
   - 实现可配置的比较规则引擎

## 学习要点

1. **基础运算符**：熟练掌握所有比较运算符的使用
2. **数据类型**：理解不同数据类型比较的特点和注意事项
3. **身份vs相等**：区分`is`和`==`的使用场景
4. **成员检查**：掌握`in`运算符在不同容器中的行为
5. **链式比较**：学会使用链式比较简化复杂条件
6. **浮点数陷阱**：了解浮点数比较的精度问题和解决方案
7. **性能考虑**：理解不同比较操作的性能特点
8. **实际应用**：能够在实际项目中正确使用各种比较运算符

通过掌握比较运算符的各种用法和特性，你可以编写更加精确和高效的条件判断代码。接下来学习条件表达式，进一步提升代码的简洁性和可读性。