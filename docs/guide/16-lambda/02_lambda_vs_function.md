# Lambda表达式与普通函数的对比

本节将深入比较Lambda表达式与普通函数的区别，帮助你理解何时使用Lambda，何时使用普通函数。

## 语法对比

### 普通函数定义

```python
# 普通函数的完整语法
def add_numbers(x, y):
    """计算两个数的和"""
    result = x + y
    return result

# 调用普通函数
result = add_numbers(3, 5)
print(f"普通函数结果: {result}")
```

### Lambda表达式定义

```python
# Lambda表达式的简洁语法
add_lambda = lambda x, y: x + y

# 调用Lambda表达式
result = add_lambda(3, 5)
print(f"Lambda结果: {result}")
```

### 语法特点对比

```python
# 1. 关键字不同
def normal_function():  # 使用def关键字
    return "普通函数"

lambda_function = lambda: "Lambda函数"  # 使用lambda关键字

# 2. 命名方式不同
# 普通函数有明确的函数名
print(f"普通函数名: {normal_function.__name__}")

# Lambda函数是匿名的
print(f"Lambda函数名: {lambda_function.__name__}")  # 显示为<lambda>

# 3. 文档字符串
def documented_function():
    """这是一个有文档的函数"""
    return "有文档"

# Lambda无法添加文档字符串
undocumented_lambda = lambda: "无文档"

print(f"普通函数文档: {documented_function.__doc__}")
print(f"Lambda文档: {undocumented_lambda.__doc__}")  # None
```

## 功能复杂度对比

### 简单功能实现

```python
# 简单功能：两种方式都很合适

# 普通函数版本
def square_normal(x):
    return x ** 2

# Lambda版本
square_lambda = lambda x: x ** 2

# 测试功能
test_number = 4
print(f"普通函数平方: {square_normal(test_number)}")
print(f"Lambda平方: {square_lambda(test_number)}")
```

### 复杂功能实现

```python
# 复杂功能：普通函数更适合

# 普通函数：可以处理复杂逻辑
def calculate_grade(score):
    """根据分数计算等级"""
    if score >= 90:
        grade = 'A'
        message = "优秀"
    elif score >= 80:
        grade = 'B'
        message = "良好"
    elif score >= 70:
        grade = 'C'
        message = "中等"
    elif score >= 60:
        grade = 'D'
        message = "及格"
    else:
        grade = 'F'
        message = "不及格"
    
    return f"{grade} - {message}"

# Lambda：只能处理简单表达式
grade_lambda = lambda score: 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F'

# 测试复杂功能
test_score = 85
print(f"普通函数等级: {calculate_grade(test_score)}")
print(f"Lambda等级: {grade_lambda(test_score)}")
```

### 多语句处理

```python
# 普通函数：可以包含多个语句
def process_data(data):
    """处理数据的多个步骤"""
    # 步骤1：数据清洗
    cleaned_data = [x for x in data if x is not None]
    
    # 步骤2：数据转换
    transformed_data = [str(x).upper() if isinstance(x, str) else x for x in cleaned_data]
    
    # 步骤3：数据验证
    if not transformed_data:
        return "无有效数据"
    
    # 步骤4：返回结果
    return f"处理了{len(transformed_data)}个数据项"

# Lambda：只能包含单个表达式
# 无法实现上述复杂的多步骤处理

# 测试数据处理
test_data = ["hello", None, "world", 123, None]
print(f"数据处理结果: {process_data(test_data)}")
```

## 可读性对比

### 简单操作的可读性

```python
# 简单操作：Lambda更简洁
numbers = [1, 2, 3, 4, 5]

# 使用普通函数
def double(x):
    return x * 2

doubled_normal = list(map(double, numbers))

# 使用Lambda
doubled_lambda = list(map(lambda x: x * 2, numbers))

print(f"普通函数结果: {doubled_normal}")
print(f"Lambda结果: {doubled_lambda}")
```

### 复杂操作的可读性

```python
# 复杂操作：普通函数更清晰
students = [
    {'name': 'Alice', 'age': 20, 'grade': 85},
    {'name': 'Bob', 'age': 19, 'grade': 92},
    {'name': 'Charlie', 'age': 21, 'grade': 78}
]

# 普通函数：清晰易懂
def get_student_summary(student):
    """获取学生摘要信息"""
    name = student['name']
    age = student['age']
    grade = student['grade']
    status = "优秀" if grade >= 90 else "良好" if grade >= 80 else "一般"
    return f"{name}({age}岁): {grade}分-{status}"

# Lambda：难以阅读
get_summary_lambda = lambda s: f"{s['name']}({s['age']}岁): {s['grade']}分-{'优秀' if s['grade'] >= 90 else '良好' if s['grade'] >= 80 else '一般'}"

# 测试可读性
for student in students:
    print(f"普通函数: {get_student_summary(student)}")
    print(f"Lambda: {get_summary_lambda(student)}")
    print()
```

## 性能对比

### 执行速度测试

```python
import time

# 准备测试数据
test_data = list(range(1000000))

# 普通函数版本
def square_func(x):
    return x * x

# Lambda版本
square_lambda = lambda x: x * x

# 测试普通函数性能
start_time = time.time()
result_func = [square_func(x) for x in test_data[:1000]]
func_time = time.time() - start_time

# 测试Lambda性能
start_time = time.time()
result_lambda = [square_lambda(x) for x in test_data[:1000]]
lambda_time = time.time() - start_time

print(f"普通函数执行时间: {func_time:.6f}秒")
print(f"Lambda执行时间: {lambda_time:.6f}秒")
print(f"性能差异: {abs(func_time - lambda_time):.6f}秒")
```

### 内存占用对比

```python
import sys

# 普通函数
def simple_func(x):
    return x + 1

# Lambda函数
simple_lambda = lambda x: x + 1

# 比较内存占用
func_size = sys.getsizeof(simple_func)
lambda_size = sys.getsizeof(simple_lambda)

print(f"普通函数内存占用: {func_size} bytes")
print(f"Lambda内存占用: {lambda_size} bytes")
print(f"内存差异: {abs(func_size - lambda_size)} bytes")

# 函数对象的属性比较
print(f"\n普通函数属性数量: {len(dir(simple_func))}")
print(f"Lambda属性数量: {len(dir(simple_lambda))}")

# 显示一些关键属性
print(f"\n普通函数名称: {simple_func.__name__}")
print(f"Lambda名称: {simple_lambda.__name__}")
print(f"普通函数模块: {simple_func.__module__}")
print(f"Lambda模块: {simple_lambda.__module__}")
```

## 调试和错误处理对比

### 错误信息的差异

```python
# 普通函数的错误处理
def divide_normal(a, b):
    """普通除法函数"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

# Lambda的错误处理（有限）
divide_lambda = lambda a, b: a / b if b != 0 else None

# 测试错误情况
try:
    result = divide_normal(10, 0)
except ValueError as e:
    print(f"普通函数错误: {e}")

try:
    result = divide_lambda(10, 0)
    print(f"Lambda结果: {result}")
except Exception as e:
    print(f"Lambda错误: {e}")

# 调试信息的差异
def debug_function(x):
    print(f"调试: 输入值为 {x}")
    result = x * 2
    print(f"调试: 计算结果为 {result}")
    return result

# Lambda无法轻松添加调试信息
debug_lambda = lambda x: x * 2  # 无法添加print语句

print("\n普通函数调试:")
result1 = debug_function(5)

print("\nLambda调试:")
result2 = debug_lambda(5)
print(f"Lambda结果: {result2}")
```

### 异常追踪

```python
# 创建会产生错误的函数
def error_function():
    """会产生错误的普通函数"""
    return 1 / 0

error_lambda = lambda: 1 / 0

# 比较错误追踪信息
print("普通函数错误追踪:")
try:
    error_function()
except ZeroDivisionError as e:
    import traceback
    traceback.print_exc()

print("\nLambda错误追踪:")
try:
    error_lambda()
except ZeroDivisionError as e:
    import traceback
    traceback.print_exc()
```

## 文档和注释对比

### 文档字符串支持

```python
# 普通函数：支持完整的文档
def calculate_bmi(weight, height):
    """
    计算身体质量指数(BMI)
    
    参数:
        weight (float): 体重，单位为千克
        height (float): 身高，单位为米
    
    返回:
        float: BMI值
    
    示例:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    return weight / (height ** 2)

# Lambda：无法添加文档字符串
calculate_bmi_lambda = lambda weight, height: weight / (height ** 2)

# 查看文档
print("普通函数文档:")
print(calculate_bmi.__doc__)

print("\nLambda文档:")
print(calculate_bmi_lambda.__doc__)  # None

# 使用help()函数
print("\n普通函数帮助:")
help(calculate_bmi)

print("\nLambda帮助:")
help(calculate_bmi_lambda)
```

### 代码注释

```python
# 普通函数：可以添加详细注释
def process_text(text):
    """处理文本数据"""
    # 步骤1：去除首尾空格
    text = text.strip()
    
    # 步骤2：转换为小写
    text = text.lower()
    
    # 步骤3：替换特殊字符
    text = text.replace('-', '_')
    
    # 步骤4：返回处理结果
    return text

# Lambda：无法添加内部注释
process_text_lambda = lambda text: text.strip().lower().replace('-', '_')  # 只能在行尾注释

# 测试文本处理
test_text = "  Hello-World  "
print(f"普通函数结果: '{process_text(test_text)}'")
print(f"Lambda结果: '{process_text_lambda(test_text)}'")
```

## 使用场景对比

### 适合使用Lambda的场景

```python
# 1. 作为高阶函数的参数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 使用Lambda进行数据处理
squares = list(map(lambda x: x**2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
sum_result = reduce(lambda x, y: x + y, numbers)

print(f"平方: {squares}")
print(f"偶数: {even_numbers}")
print(f"求和: {sum_result}")

# 2. 简单的排序键函数
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
sorted_by_grade = sorted(students, key=lambda student: student[1])
print(f"按成绩排序: {sorted_by_grade}")

# 3. 事件处理（在GUI编程中）
# button.onclick = lambda: print("按钮被点击")

# 4. 配置和设置
operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y if y != 0 else None
}

result = operations['add'](10, 5)
print(f"计算结果: {result}")
```

### 适合使用普通函数的场景

```python
# 1. 复杂的业务逻辑
def calculate_tax(income, tax_brackets):
    """
    根据税率表计算所得税
    
    参数:
        income: 收入
        tax_brackets: 税率表
    
    返回:
        计算出的税额
    """
    total_tax = 0
    remaining_income = income
    
    for bracket in tax_brackets:
        if remaining_income <= 0:
            break
            
        taxable_amount = min(remaining_income, bracket['limit'])
        tax_amount = taxable_amount * bracket['rate']
        total_tax += tax_amount
        remaining_income -= taxable_amount
        
        print(f"税率 {bracket['rate']*100}%: 应税额 {taxable_amount}, 税额 {tax_amount}")
    
    return total_tax

# 2. 需要错误处理的函数
def safe_divide(a, b):
    """
    安全的除法运算
    """
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("参数必须是数字")
        
        if b == 0:
            raise ValueError("除数不能为零")
        
        result = a / b
        print(f"计算成功: {a} ÷ {b} = {result}")
        return result
        
    except Exception as e:
        print(f"计算错误: {e}")
        return None

# 3. 需要多次调用的函数
def format_currency(amount, currency='USD'):
    """
    格式化货币显示
    """
    symbols = {'USD': '$', 'EUR': '€', 'CNY': '¥'}
    symbol = symbols.get(currency, currency)
    return f"{symbol}{amount:,.2f}"

# 测试复杂函数
tax_brackets = [
    {'limit': 10000, 'rate': 0.1},
    {'limit': 30000, 'rate': 0.2},
    {'limit': float('inf'), 'rate': 0.3}
]

print("税额计算:")
tax = calculate_tax(50000, tax_brackets)
print(f"总税额: {format_currency(tax)}")

print("\n安全除法:")
safe_divide(10, 2)
safe_divide(10, 0)
safe_divide("10", 2)
```

## 最佳实践建议

### 选择Lambda的原则

```python
# ✅ 好的Lambda使用
# 1. 简单的单行操作
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))

# 2. 作为参数传递
data = [('apple', 5), ('banana', 2), ('cherry', 8)]
sorted_data = sorted(data, key=lambda item: item[1])

# 3. 简单的条件判断
filtered_numbers = list(filter(lambda x: x > 3, numbers))

print(f"平方: {squares}")
print(f"排序: {sorted_data}")
print(f"过滤: {filtered_numbers}")
```

### 选择普通函数的原则

```python
# ✅ 好的普通函数使用
# 1. 复杂逻辑
def validate_email(email):
    """验证邮箱格式"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not isinstance(email, str):
        return False, "邮箱必须是字符串"
    
    if not email.strip():
        return False, "邮箱不能为空"
    
    if re.match(pattern, email):
        return True, "邮箱格式正确"
    else:
        return False, "邮箱格式不正确"

# 2. 需要文档的函数
def fibonacci(n):
    """
    计算斐波那契数列的第n项
    
    参数:
        n (int): 项数（从0开始）
    
    返回:
        int: 第n项的值
    
    示例:
        >>> fibonacci(5)
        5
        >>> fibonacci(10)
        55
    """
    if n < 0:
        raise ValueError("n必须是非负整数")
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

# 3. 会被多次调用的函数
def log_message(message, level='INFO'):
    """记录日志消息"""
    import datetime
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {level}: {message}")

# 测试最佳实践
print("邮箱验证:")
valid, msg = validate_email("test@example.com")
print(f"结果: {valid}, 消息: {msg}")

print(f"\n斐波那契数列第10项: {fibonacci(10)}")

print("\n日志记录:")
log_message("程序开始执行")
log_message("发生错误", "ERROR")
log_message("程序结束执行")
```

### 避免的反模式

```python
# ❌ 不好的Lambda使用
# 1. 过于复杂的Lambda
# bad_lambda = lambda x: x**2 + 2*x + 1 if x > 0 else -x**2 + 2*x - 1 if x < 0 else 0

# ✅ 应该使用普通函数
def quadratic_function(x):
    """二次函数计算"""
    if x > 0:
        return x**2 + 2*x + 1
    elif x < 0:
        return -x**2 + 2*x - 1
    else:
        return 0

# ❌ 不好的普通函数使用
# 过于简单的普通函数
def add_one(x):
    return x + 1

# ✅ 应该使用Lambda
add_one_lambda = lambda x: x + 1

# 演示正确用法
test_value = 5
print(f"复杂计算: {quadratic_function(test_value)}")
print(f"简单计算: {add_one_lambda(test_value)}")
```

## 性能和内存优化

### 函数缓存

```python
from functools import lru_cache

# 普通函数可以使用装饰器
@lru_cache(maxsize=128)
def expensive_calculation(n):
    """耗时的计算函数"""
    print(f"计算 {n}...")
    result = sum(i**2 for i in range(n))
    return result

# Lambda无法直接使用装饰器
# 但可以这样包装
expensive_lambda = lru_cache(maxsize=128)(lambda n: sum(i**2 for i in range(n)))

# 测试缓存效果
print("普通函数缓存测试:")
print(expensive_calculation(1000))  # 第一次计算
print(expensive_calculation(1000))  # 使用缓存

print("\nLambda缓存测试:")
print(expensive_lambda(1000))  # 第一次计算
print(expensive_lambda(1000))  # 使用缓存
```

## 运行代码

要运行本节的示例代码，请执行：

```bash
python3 02_lambda_vs_function.py
```

## 小结

通过本节的对比，我们可以总结出以下要点：

### Lambda表达式的优势：
- 语法简洁，适合简单操作
- 作为参数传递时很方便
- 减少代码行数
- 适合函数式编程风格

### 普通函数的优势：
- 支持复杂逻辑和多语句
- 可以添加文档字符串和注释
- 错误信息更清晰
- 便于调试和维护
- 支持装饰器

### 选择建议：
- **使用Lambda**：简单的单行操作、作为高阶函数参数、临时使用
- **使用普通函数**：复杂逻辑、需要文档、会被多次调用、需要错误处理

在下一节中，我们将学习Lambda表达式与map函数的结合使用。