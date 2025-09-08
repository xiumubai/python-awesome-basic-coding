# 算术运算符

算术运算符是Python中最基础也是最常用的运算符，用于执行数学计算。本章将详细介绍Python中的七种算术运算符及其应用。

## 学习目标

通过本章学习，你将掌握：
- 七种算术运算符的使用方法
- 整除和取模运算的特点和应用
- 幂运算的多种用法
- 不同数据类型间的算术运算
- 运算符优先级和结合性
- 算术运算符的实际应用场景

## 算术运算符概览

Python提供了以下七种算术运算符：

| 运算符 | 名称 | 示例 | 结果 |
|--------|------|------|------|
| `+` | 加法 | `5 + 3` | `8` |
| `-` | 减法 | `5 - 3` | `2` |
| `*` | 乘法 | `5 * 3` | `15` |
| `/` | 除法 | `5 / 3` | `1.6666666666666667` |
| `//` | 整除 | `5 // 3` | `1` |
| `%` | 取模 | `5 % 3` | `2` |
| `**` | 幂运算 | `5 ** 3` | `125` |

## 基本算术运算

### 加法、减法、乘法、除法

```python
a = 10
b = 3

print(f"加法 (a + b): {a} + {b} = {a + b}")  # 13
print(f"减法 (a - b): {a} - {b} = {a - b}")  # 7
print(f"乘法 (a * b): {a} * {b} = {a * b}")  # 30
print(f"除法 (a / b): {a} / {b} = {a / b}")  # 3.3333333333333335
```

**重要提示：** 在Python 3中，`/` 运算符总是返回浮点数，即使两个操作数都是整数。

## 整除运算符 (//)

整除运算符返回除法结果的整数部分（向下取整）：

```python
print(f"10 // 3 = {10 // 3}")    # 3
print(f"10 // 4 = {10 // 4}")    # 2
print(f"10.5 // 3 = {10.5 // 3}")  # 3.0
```

### 负数的整除

需要特别注意负数的整除行为：

```python
print(f"7 // 3 = {7 // 3}")      # 2
print(f"-7 // 3 = {-7 // 3}")    # -3 (向下取整)
print(f"7 // -3 = {7 // -3}")    # -3 (向下取整)
print(f"-7 // -3 = {-7 // -3}")  # 2
```

## 取模运算符 (%)

取模运算符返回除法的余数：

```python
print(f"10 % 3 = {10 % 3}")  # 1
print(f"10 % 4 = {10 % 4}")  # 2
print(f"10 % 5 = {10 % 5}")  # 0
```

### 取模运算的实际应用

**1. 判断奇偶数：**
```python
def is_even(num):
    return num % 2 == 0

print(f"8 是偶数吗？{is_even(8)}")  # True
print(f"7 是偶数吗？{is_even(7)}")  # False
```

**2. 循环索引：**
```python
# 在长度为5的列表中循环
for i in range(10):
    index = i % 5
    print(f"i={i}, 循环索引={index}")
```

## 幂运算符 (**)

幂运算符用于计算乘方：

```python
print(f"2 ** 3 = {2 ** 3}")      # 8
print(f"5 ** 2 = {5 ** 2}")      # 25
print(f"3 ** 3 = {3 ** 3}")      # 27
```

### 开方运算

幂运算符也可以用于开方：

```python
print(f"9 ** 0.5 = {9 ** 0.5}")        # 3.0 (平方根)
print(f"27 ** (1/3) = {27 ** (1/3)}")  # 3.0 (立方根)
print(f"16 ** 0.25 = {16 ** 0.25}")    # 2.0 (四次方根)
```

## 不同数据类型的算术运算

### 数值类型混合运算

```python
int_num = 5
float_num = 2.5

result = int_num + float_num
print(f"整数 + 浮点数: {int_num} + {float_num} = {result}")
print(f"结果类型: {type(result)}")  # <class 'float'>
```

### 字符串的算术运算

```python
# 字符串连接
str1 = "Hello"
str2 = "World"
print(f"字符串相加: '{str1}' + ' ' + '{str2}' = '{str1 + ' ' + str2}'")

# 字符串重复
print(f"字符串重复: '{str1}' * 3 = '{str1 * 3}'")
```

### 列表的算术运算

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 列表连接
print(f"列表相加: {list1} + {list2} = {list1 + list2}")

# 列表重复
print(f"列表重复: {list1} * 2 = {list1 * 2}")
```

## 运算符优先级

算术运算符的优先级（从高到低）：
1. `**` (幂运算)
2. `*`, `/`, `//`, `%` (乘法、除法、整除、取模)
3. `+`, `-` (加法、减法)

```python
# 优先级示例
result1 = 2 + 3 * 4      # 14 (先乘后加)
result2 = (2 + 3) * 4    # 20 (括号优先)

print(f"2 + 3 * 4 = {result1}")
print(f"(2 + 3) * 4 = {result2}")

# 幂运算的右结合性
result3 = 2 ** 3 ** 2    # 512 (等价于 2 ** (3 ** 2))
result4 = (2 ** 3) ** 2  # 64

print(f"2 ** 3 ** 2 = {result3}")
print(f"(2 ** 3) ** 2 = {result4}")
```

## 实际应用示例

### 1. 几何计算

```python
import math

# 计算圆的面积
radius = 5
area = math.pi * radius ** 2
print(f"半径为 {radius} 的圆的面积: {area:.2f}")

# 计算球的体积
volume = 4/3 * math.pi * radius ** 3
print(f"半径为 {radius} 的球的体积: {volume:.2f}")
```

### 2. 温度转换

```python
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"摄氏度 {celsius}°C = 华氏度 {fahrenheit}°F")
```

### 3. 复利计算

```python
def compound_interest(principal, rate, time):
    return principal * (1 + rate) ** time

principal = 1000  # 本金
rate = 0.05      # 年利率 5%
time = 3         # 3年

amount = compound_interest(principal, rate, time)
interest = amount - principal

print(f"本金: {principal}")
print(f"年利率: {rate*100}%")
print(f"时间: {time} 年")
print(f"最终金额: {amount:.2f}")
print(f"利息: {interest:.2f}")
```

### 4. 时间转换

```python
def convert_seconds(total_seconds):
    """将秒数转换为小时、分钟和秒"""
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

test_seconds = 3661
h, m, s = convert_seconds(test_seconds)
print(f"{test_seconds} 秒 = {h} 小时 {m} 分钟 {s} 秒")
```

## 练习题

### 基础练习

1. 计算以下表达式的结果：
   - `15 + 4 * 3 - 2`
   - `(8 + 2) * 3 / 5`
   - `17 % 5`
   - `17 // 5`
   - `2 ** 3 ** 2`

2. 编写函数判断一个数是否为偶数

3. 编写函数计算一个数的平方和立方

### 应用练习

1. 编写程序计算矩形的面积和周长
2. 编写程序将华氏度转换为摄氏度
3. 编写程序计算单利和复利
4. 编写程序将秒数转换为天、小时、分钟和秒

### 练习答案

```python
# 基础练习答案
print("基础练习答案：")
print(f"1. 15 + 4 * 3 - 2 = {15 + 4 * 3 - 2}")  # 25
print(f"2. (8 + 2) * 3 / 5 = {(8 + 2) * 3 / 5}")  # 6.0
print(f"3. 17 % 5 = {17 % 5}")  # 2
print(f"4. 17 // 5 = {17 // 5}")  # 3
print(f"5. 2 ** 3 ** 2 = {2 ** 3 ** 2}")  # 512

# 判断偶数
def is_even(num):
    return num % 2 == 0

# 计算平方和立方
def calculate_powers(num):
    return num ** 2, num ** 3

# 矩形计算
def rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
```

## 常见错误和注意事项

### 1. 除零错误

```python
# 错误示例
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除零错误！")

# 安全的除法
def safe_divide(a, b):
    if b == 0:
        return None
    return a / b
```

### 2. 浮点数精度问题

```python
# 浮点数精度问题
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")  # 0.30000000000000004

# 解决方案
from decimal import Decimal
result = Decimal('0.1') + Decimal('0.2')
print(f"使用Decimal: {result}")  # 0.3

# 或者使用round函数
result = round(0.1 + 0.2, 1)
print(f"使用round: {result}")  # 0.3
```

### 3. 整除的向下取整特性

```python
# 注意负数的整除行为
print(f"7 // 3 = {7 // 3}")      # 2
print(f"-7 // 3 = {-7 // 3}")    # -3 (不是-2!)

# 如果需要向零取整，使用int(a/b)
print(f"int(-7/3) = {int(-7/3)}")  # -2
```

## 学习要点总结

1. **基本运算符**：掌握 `+`、`-`、`*`、`/` 的基本用法
2. **整除和取模**：理解 `//` 和 `%` 的特殊性质和应用场景
3. **幂运算**：学会使用 `**` 进行乘方和开方运算
4. **类型转换**：了解不同数据类型运算时的类型提升规则
5. **运算符优先级**：记住基本的优先级规则，复杂表达式使用括号
6. **实际应用**：将算术运算符应用到实际问题中
7. **错误处理**：注意除零错误和浮点数精度问题

通过大量的练习和实际应用，你将能够熟练掌握Python中的算术运算符，为后续学习打下坚实的基础。