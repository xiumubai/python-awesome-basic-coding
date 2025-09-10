# 条件推导式 (Conditional Comprehensions)

## 学习目标

条件推导式是在推导式中使用条件语句来过滤或转换数据的技术。它包括条件过滤（if语句）和条件表达式（三元运算符）两种形式，可以让推导式更加灵活和强大。

通过本节学习，你将掌握：
1. 掌握条件过滤的语法和应用
2. 理解条件表达式在推导式中的使用
3. 学会组合多个条件
4. 掌握复杂条件逻辑的处理
5. 了解条件推导式的性能特点
6. 学会在不同数据类型中应用条件推导式

## 基本条件过滤

条件过滤是推导式中最常用的功能，语法为：`[expression for item in iterable if condition]`

```python
numbers = list(range(1, 21))
print(f"原始数据: {numbers}")

# 1. 基本过滤语法：[expression for item in iterable if condition]
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"偶数: {even_numbers}")

# 2. 多个条件（and）
even_and_greater_than_10 = [x for x in numbers if x % 2 == 0 and x > 10]
print(f"偶数且>10: {even_and_greater_than_10}")

# 3. 多个条件（or）
divisible_by_3_or_5 = [x for x in numbers if x % 3 == 0 or x % 5 == 0]
print(f"能被3或5整除: {divisible_by_3_or_5}")

# 4. 复杂条件
complex_condition = [x for x in numbers 
                    if (x % 2 == 0 and x < 10) or (x % 3 == 0 and x > 15)]
print(f"复杂条件: {complex_condition}")
```

## 使用函数作为条件

可以将函数调用作为过滤条件，提高代码的可读性和复用性：

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(range(1, 21))
primes = [x for x in numbers if is_prime(x)]
print(f"质数: {primes}")
```

## 条件表达式（三元运算符）

条件表达式允许在推导式中进行条件转换，语法为：`[expr1 if condition else expr2 for item in iterable]`

```python
numbers = list(range(-5, 6))
print(f"原始数据: {numbers}")

# 1. 基本条件表达式语法：[expr1 if condition else expr2 for item in iterable]
abs_values = [x if x >= 0 else -x for x in numbers]
print(f"绝对值: {abs_values}")

# 2. 字符串条件表达式
signs = ['positive' if x > 0 else 'negative' if x < 0 else 'zero' for x in numbers]
print(f"符号: {signs}")

# 3. 数值转换
normalized = [x/10 if abs(x) > 3 else x for x in numbers]
print(f"标准化: {normalized}")

# 4. 复杂表达式
processed = [x**2 if x > 0 else abs(x) if x < 0 else 1 for x in numbers]
print(f"复杂处理: {processed}")

# 5. 组合条件过滤和条件表达式
filtered_and_transformed = [x**2 if x % 2 == 0 else x**3 
                           for x in numbers if x != 0]
print(f"过滤并转换: {filtered_and_transformed}")
```

## 字符串条件过滤

字符串数据的条件过滤有很多实用的应用场景：

```python
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
print(f"原始单词: {words}")

# 1. 长度过滤
long_words = [word for word in words if len(word) > 5]
print(f"长单词(>5字符): {long_words}")

# 2. 字母过滤
words_with_a = [word for word in words if 'a' in word]
print(f"包含字母'a': {words_with_a}")

# 3. 开头字母过滤
words_start_with_vowel = [word for word in words if word[0] in 'aeiou']
print(f"元音开头: {words_start_with_vowel}")

# 4. 正则表达式过滤
import re
pattern_words = [word for word in words if re.match(r'^[a-d]', word)]
print(f"a-d开头: {pattern_words}")

# 5. 条件转换
capitalized = [word.upper() if len(word) > 5 else word.lower() for word in words]
print(f"条件大小写: {capitalized}")
```

## 复杂数据结构的条件过滤

处理字典、列表等复杂数据结构时的条件过滤：

```python
# 学生数据
students = [
    {'name': 'Alice', 'age': 20, 'grade': 85, 'subjects': ['Math', 'Science']},
    {'name': 'Bob', 'age': 19, 'grade': 92, 'subjects': ['Math', 'English']},
    {'name': 'Charlie', 'age': 21, 'grade': 78, 'subjects': ['Science', 'History']},
    {'name': 'Diana', 'age': 20, 'grade': 95, 'subjects': ['Math', 'Science', 'English']}
]

# 1. 基于单个属性过滤
high_achievers = [student['name'] for student in students if student['grade'] > 90]
print(f"高分学生: {high_achievers}")

# 2. 基于多个属性过滤
young_high_achievers = [student['name'] for student in students 
                       if student['age'] < 21 and student['grade'] > 85]
print(f"年轻高分学生: {young_high_achievers}")

# 3. 基于列表属性过滤
math_students = [student['name'] for student in students 
                if 'Math' in student['subjects']]
print(f"数学学生: {math_students}")

# 4. 复杂条件过滤
versatile_students = [student['name'] for student in students 
                     if len(student['subjects']) >= 3 or student['grade'] > 90]
print(f"多才多艺学生: {versatile_students}")

# 5. 条件转换
student_status = [f"{student['name']}: {'优秀' if student['grade'] >= 90 else '良好' if student['grade'] >= 80 else '及格'}" 
                 for student in students]
print(f"学生状态: {student_status}")
```

## 数值条件处理

数值数据的各种条件处理技巧：

```python
import statistics
import math

# 测试数据
data = [1.5, 2.8, 3.2, 4.7, 5.1, 6.9, 7.3, 8.6, 9.1, 10.4]
print(f"原始数据: {data}")

# 1. 范围过滤
in_range = [x for x in data if 3.0 <= x <= 8.0]
print(f"3.0-8.0范围: {in_range}")

# 2. 精度处理
rounded_filtered = [round(x) for x in data if x % 1 > 0.5]
print(f"小数部分>0.5的四舍五入: {rounded_filtered}")

# 3. 统计条件
mean_val = statistics.mean(data)
above_average = [x for x in data if x > mean_val]
print(f"平均值: {mean_val:.2f}, 高于平均值: {above_average}")

# 4. 数学函数条件
special_values = [x for x in data if math.sin(x) > 0.5]
print(f"sin值>0.5: {special_values}")

# 5. 分组处理
categorized = [('small', x) if x < 4 else ('medium', x) if x < 8 else ('large', x) 
              for x in data]
print(f"分类: {categorized[:5]}...")  # 只显示前5个
```

## 日期时间条件过滤

处理日期时间数据的条件过滤：

```python
from datetime import datetime, timedelta

# 生成测试日期
base_date = datetime(2024, 1, 1)
dates = [base_date + timedelta(days=i*7) for i in range(20)]  # 每周一个日期

print(f"日期范围: {dates[0].strftime('%Y-%m-%d')} 到 {dates[-1].strftime('%Y-%m-%d')}")

# 1. 月份过滤
spring_dates = [date for date in dates if date.month in [3, 4, 5]]
print(f"春季日期: {[d.strftime('%Y-%m-%d') for d in spring_dates]}")

# 2. 星期过滤
weekends = [date for date in dates if date.weekday() >= 5]  # 5=Saturday, 6=Sunday
print(f"周末日期: {[d.strftime('%Y-%m-%d') for d in weekends]}")

# 3. 日期范围过滤
q1_dates = [date for date in dates 
           if datetime(2024, 1, 1) <= date <= datetime(2024, 3, 31)]
print(f"第一季度: {[d.strftime('%Y-%m-%d') for d in q1_dates]}")

# 4. 条件格式化
formatted_dates = [date.strftime('%Y-%m-%d (周末)') if date.weekday() >= 5 
                  else date.strftime('%Y-%m-%d (工作日)') for date in dates[:5]]
print(f"格式化日期: {formatted_dates}")
```

## 嵌套条件处理

处理复杂嵌套数据结构的条件过滤：

```python
# 复杂数据结构
departments = [
    {
        'name': 'Engineering',
        'employees': [
            {'name': 'Alice', 'salary': 80000, 'experience': 5},
            {'name': 'Bob', 'salary': 95000, 'experience': 8},
            {'name': 'Charlie', 'salary': 70000, 'experience': 3}
        ]
    },
    {
        'name': 'Marketing',
        'employees': [
            {'name': 'Diana', 'salary': 75000, 'experience': 6},
            {'name': 'Eve', 'salary': 85000, 'experience': 7}
        ]
    }
]

# 1. 嵌套过滤
high_earners = [emp['name'] for dept in departments 
               for emp in dept['employees'] 
               if emp['salary'] > 80000]
print(f"高薪员工: {high_earners}")

# 2. 部门条件过滤
eng_employees = [emp['name'] for dept in departments 
                if dept['name'] == 'Engineering'
                for emp in dept['employees']]
print(f"工程部员工: {eng_employees}")

# 3. 复合条件
experienced_high_earners = [emp['name'] for dept in departments 
                           for emp in dept['employees'] 
                           if emp['salary'] > 75000 and emp['experience'] > 5]
print(f"经验丰富的高薪员工: {experienced_high_earners}")

# 4. 部门统计
dept_stats = [(dept['name'], 
              len([emp for emp in dept['employees'] if emp['salary'] > 80000]))
             for dept in departments]
print(f"各部门高薪员工数: {dept_stats}")
```

## 常见模式和最佳实践

### 类型过滤模式

```python
mixed_data = [1, 'hello', 3.14, None, 'world', 42, [], 'python', 0, False]

# 类型过滤
strings_only = [item for item in mixed_data if isinstance(item, str)]
numbers_only = [item for item in mixed_data if isinstance(item, (int, float)) and item]
print(f"字符串: {strings_only}")
print(f"非零数字: {numbers_only}")

# 真值过滤
truthy_values = [item for item in mixed_data if item]
falsy_values = [item for item in mixed_data if not item]
print(f"真值: {truthy_values}")
print(f"假值: {falsy_values}")
```

### 安全访问模式

```python
data_with_attrs = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob'},  # 缺少age
    {'name': 'Charlie', 'age': 30}
]

# 安全获取年龄
ages = [person.get('age', 0) for person in data_with_attrs]
adults = [person['name'] for person in data_with_attrs 
         if person.get('age', 0) >= 18]
print(f"年龄: {ages}")
print(f"成年人: {adults}")
```

### 范围检查模式

```python
scores = [85, 92, 78, 96, 88, 73, 91, 87]
grade_distribution = {
    'A': [score for score in scores if score >= 90],
    'B': [score for score in scores if 80 <= score < 90],
    'C': [score for score in scores if 70 <= score < 80],
    'F': [score for score in scores if score < 70]
}

print(f"成绩分布:")
for grade, score_list in grade_distribution.items():
    print(f"  {grade}: {len(score_list)}个 {score_list}")
```

## 错误处理

在条件推导式中处理可能的错误：

```python
# 可能出错的数据
mixed_numbers = ['1', '2', 'abc', '4', None, '5.5', '']

# 1. 安全转换模式
def safe_float(value):
    try:
        return float(value) if value else 0.0
    except (ValueError, TypeError):
        return 0.0

safe_numbers = [safe_float(x) for x in mixed_numbers]
print(f"安全转换: {safe_numbers}")

# 2. 过滤有效值
valid_numbers = [float(x) for x in mixed_numbers 
                if x and str(x).replace('.', '').replace('-', '').isdigit()]
print(f"有效数字: {valid_numbers}")

# 3. 分离有效和无效数据
valid_data = [x for x in mixed_numbers if x and str(x).replace('.', '').replace('-', '').isdigit()]
invalid_data = [x for x in mixed_numbers if not (x and str(x).replace('.', '').replace('-', '').isdigit())]
print(f"有效数据: {valid_data}")
print(f"无效数据: {invalid_data}")
```

## 性能优化建议

1. **早期过滤**：在数据转换之前进行过滤
2. **避免复杂函数调用**：在条件中使用简单的内联表达式
3. **合理使用条件**：避免过于复杂的条件逻辑

```python
import time

large_data = list(range(10000))

# 早期过滤（推荐）
start_time = time.time()
early_filter = [x**2 for x in large_data if x % 100 == 0]
early_time = time.time() - start_time

# 后期过滤（不推荐）
start_time = time.time()
late_filter = [x for x in [y**2 for y in large_data] if (x**0.5) % 100 == 0]
late_time = time.time() - start_time

print(f"早期过滤: {early_time:.4f}秒")
print(f"后期过滤: {late_time:.4f}秒")
```

## 学习要点总结

1. **条件过滤语法**：`[expr for item in iterable if condition]`
2. **条件表达式语法**：`[expr1 if condition else expr2 for item in iterable]`
3. **支持复杂的逻辑条件**（and, or, not）
4. **可以使用函数作为条件**
5. **适合各种数据类型的过滤和转换**
6. **注意性能优化，避免复杂的函数调用**
7. **合理处理异常和边界情况**
8. **保持代码的可读性和简洁性**

## 注意事项

- 条件过滤在数据量大时要注意性能
- 复杂条件可以考虑提取为函数
- 嵌套条件要注意可读性
- 处理可能为None的数据时要小心
- 合理使用条件表达式，避免过于复杂