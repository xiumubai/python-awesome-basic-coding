# Lambda表达式基础

Lambda表达式是Python中的匿名函数，它提供了一种简洁的方式来创建小型函数。本节将介绍Lambda表达式的基本语法和用法。

## 什么是Lambda表达式

Lambda表达式是一种创建匿名函数的方式，它可以在需要函数对象的地方使用，而不需要正式定义一个函数。

### 基本语法

```python
lambda arguments: expression
```

- `lambda`：关键字
- `arguments`：参数列表
- `expression`：单个表达式

## 基本用法示例

### 简单的Lambda表达式

```python
# 创建一个简单的Lambda表达式
add = lambda x, y: x + y
print(f"add(3, 5) = {add(3, 5)}")  # 输出: 8

# 平方函数
square = lambda x: x ** 2
print(f"square(4) = {square(4)}")  # 输出: 16

# 判断偶数
is_even = lambda x: x % 2 == 0
print(f"is_even(6) = {is_even(6)}")  # 输出: True
```

### 多参数Lambda表达式

```python
# 多个参数
max_of_three = lambda x, y, z: max(x, y, z)
print(f"max_of_three(10, 25, 15) = {max_of_three(10, 25, 15)}")  # 输出: 25

# 字符串操作
full_name = lambda first, last: f"{first} {last}"
print(f"full_name('John', 'Doe') = {full_name('John', 'Doe')}")  # 输出: John Doe
```

### 带默认参数的Lambda

```python
# 带默认参数
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(f"greet('Alice') = {greet('Alice')}")  # 输出: Hello, Alice!
print(f"greet('Bob', 'Hi') = {greet('Bob', 'Hi')}")  # 输出: Hi, Bob!

# 计算圆面积
circle_area = lambda r, pi=3.14159: pi * r ** 2
print(f"circle_area(5) = {circle_area(5):.2f}")  # 输出: 78.54
```

## Lambda与普通函数的对比

### 普通函数写法

```python
def add_normal(x, y):
    return x + y

def square_normal(x):
    return x ** 2

def is_even_normal(x):
    return x % 2 == 0
```

### Lambda写法

```python
add_lambda = lambda x, y: x + y
square_lambda = lambda x: x ** 2
is_even_lambda = lambda x: x % 2 == 0
```

### 功能验证

```python
# 验证功能相同
print(f"普通函数: add_normal(3, 5) = {add_normal(3, 5)}")
print(f"Lambda: add_lambda(3, 5) = {add_lambda(3, 5)}")

print(f"普通函数: square_normal(4) = {square_normal(4)}")
print(f"Lambda: square_lambda(4) = {square_lambda(4)}")

print(f"普通函数: is_even_normal(6) = {is_even_normal(6)}")
print(f"Lambda: is_even_lambda(6) = {is_even_lambda(6)}")
```

## Lambda的限制

### 1. 只能包含表达式

```python
# 正确：单个表达式
valid_lambda = lambda x: x * 2 + 1

# 错误：不能包含语句
# invalid_lambda = lambda x: print(x); return x * 2  # 语法错误
```

### 2. 不能包含复杂逻辑

```python
# 正确：简单条件表达式
abs_value = lambda x: x if x >= 0 else -x
print(f"abs_value(-5) = {abs_value(-5)}")  # 输出: 5

# 对于复杂逻辑，建议使用普通函数
def complex_logic(x):
    if x > 10:
        result = x * 2
    elif x > 5:
        result = x + 10
    else:
        result = x
    return result
```

### 3. 调试困难

```python
# Lambda函数在错误信息中显示为<lambda>
def named_function(x):
    return x / 0  # 会产生清晰的错误信息

anonymous_function = lambda x: x / 0  # 错误信息不够清晰
```

## 变量作用域

### 访问外部变量

```python
# Lambda可以访问外部作用域的变量
multiplier = 10
multiply_by_ten = lambda x: x * multiplier
print(f"multiply_by_ten(5) = {multiply_by_ten(5)}")  # 输出: 50

# 注意变量绑定的时机
functions = []
for i in range(3):
    functions.append(lambda x: x * i)  # 注意：i的值是循环结束时的值

# 所有函数都使用i的最终值
for func in functions:
    print(f"func(10) = {func(10)}")  # 都输出: 20

# 正确的做法：使用默认参数捕获变量
functions_correct = []
for i in range(3):
    functions_correct.append(lambda x, multiplier=i: x * multiplier)

# 现在每个函数都有正确的乘数
for i, func in enumerate(functions_correct):
    print(f"func_{i}(10) = {func(10)}")  # 输出: 0, 10, 20
```

## 实际应用示例

### 1. 简单的数据转换

```python
# 温度转换
celsius_to_fahrenheit = lambda c: c * 9/5 + 32
fahrenheit_to_celsius = lambda f: (f - 32) * 5/9

print(f"25°C = {celsius_to_fahrenheit(25):.1f}°F")
print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")
```

### 2. 字符串处理

```python
# 字符串处理
reverse_string = lambda s: s[::-1]
uppercase_first = lambda s: s[0].upper() + s[1:].lower() if s else s
remove_spaces = lambda s: s.replace(' ', '')

text = "hello world"
print(f"原文: {text}")
print(f"反转: {reverse_string(text)}")
print(f"首字母大写: {uppercase_first(text)}")
print(f"去除空格: {remove_spaces(text)}")
```

### 3. 数学计算

```python
# 数学函数
power = lambda base, exp: base ** exp
percentage = lambda part, total: (part / total) * 100 if total != 0 else 0
distance = lambda x1, y1, x2, y2: ((x2-x1)**2 + (y2-y1)**2)**0.5

print(f"2的3次方: {power(2, 3)}")
print(f"25是100的百分比: {percentage(25, 100)}%")
print(f"点(0,0)到点(3,4)的距离: {distance(0, 0, 3, 4)}")
```

## 最佳实践

### 1. 何时使用Lambda

```python
# 适合使用Lambda的场景：
# - 简单的单行函数
# - 作为高阶函数的参数
# - 临时使用的函数

# 好的例子
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
```

### 2. 何时避免使用Lambda

```python
# 避免使用Lambda的场景：
# - 复杂的逻辑
# - 需要多行代码
# - 需要文档说明的函数
# - 会被多次调用的函数

# 不好的例子（应该使用普通函数）
# complex_calculation = lambda x: x**2 + 2*x + 1 if x > 0 else -x**2 + 2*x - 1 if x < 0 else 0

# 好的做法
def complex_calculation(x):
    """计算复杂的数学表达式"""
    if x > 0:
        return x**2 + 2*x + 1
    elif x < 0:
        return -x**2 + 2*x - 1
    else:
        return 0
```

## 练习题

### 基础练习

```python
# 练习1：创建Lambda表达式计算两个数的差的绝对值
abs_diff = lambda x, y: abs(x - y)
print(f"abs_diff(10, 3) = {abs_diff(10, 3)}")  # 应该输出: 7

# 练习2：创建Lambda表达式判断一个数是否为正数
is_positive = lambda x: x > 0
print(f"is_positive(-5) = {is_positive(-5)}")  # 应该输出: False

# 练习3：创建Lambda表达式返回字符串的长度
str_length = lambda s: len(s)
print(f"str_length('Python') = {str_length('Python')}")  # 应该输出: 6
```

### 进阶练习

```python
# 练习4：创建Lambda表达式计算三个数的平均值
average = lambda x, y, z: (x + y + z) / 3
print(f"average(10, 20, 30) = {average(10, 20, 30):.1f}")  # 应该输出: 20.0

# 练习5：创建Lambda表达式判断年份是否为闰年
is_leap_year = lambda year: year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(f"is_leap_year(2024) = {is_leap_year(2024)}")  # 应该输出: True

# 练习6：创建Lambda表达式格式化货币显示
format_currency = lambda amount: f"${amount:.2f}"
print(f"format_currency(123.456) = {format_currency(123.456)}")  # 应该输出: $123.46
```

## 运行代码

要运行本节的示例代码，请执行：

```bash
python3 01_lambda_basics.py
```

## 小结

Lambda表达式是Python中创建简单匿名函数的强大工具。它们特别适合：

- 简单的单行函数
- 作为高阶函数的参数
- 临时使用的函数

记住Lambda的限制：
- 只能包含单个表达式
- 不能包含语句
- 调试相对困难

在下一节中，我们将详细比较Lambda表达式与普通函数的区别和使用场景。