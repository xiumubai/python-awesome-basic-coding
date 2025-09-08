# 数据类型详解

## 学习目标

1. 了解Python的基本数据类型
2. 掌握整数(int)类型的特点和用法
3. 掌握浮点数(float)类型的特点和用法
4. 掌握字符串(str)类型的特点和用法
5. 掌握布尔值(bool)类型的特点和用法
6. 学会使用type()函数查看数据类型

## Python的基本数据类型概述

Python有四种基本数据类型：
- **int**（整数）
- **float**（浮点数）
- **str**（字符串）
- **bool**（布尔值）

## 1. 整数类型 (int)

整数是没有小数部分的数字。

### 基本用法

```python
# 正整数
positive_num = 42
print(f"正整数：{positive_num}，类型：{type(positive_num)}")

# 负整数
negative_num = -17
print(f"负整数：{negative_num}，类型：{type(negative_num)}")

# 零
zero = 0
print(f"零：{zero}，类型：{type(zero)}")

# 大整数（Python可以处理任意大的整数）
big_num = 123456789012345678901234567890
print(f"大整数：{big_num}")
print(f"大整数类型：{type(big_num)}")
```

### 不同进制表示

```python
# 不同进制的整数
binary_num = 0b1010  # 二进制
octal_num = 0o12     # 八进制
hex_num = 0xa        # 十六进制

print(f"二进制 0b1010 = {binary_num}")
print(f"八进制 0o12 = {octal_num}")
print(f"十六进制 0xa = {hex_num}")
```

### 整数特点

- 没有小数部分
- 可以是正数、负数或零
- 支持任意大的整数
- 支持不同进制表示（二进制、八进制、十六进制）

## 2. 浮点数类型 (float)

浮点数是带有小数部分的数字。

### 基本用法

```python
# 普通浮点数
float_num1 = 3.14
print(f"浮点数：{float_num1}，类型：{type(float_num1)}")

# 负浮点数
float_num2 = -2.5
print(f"负浮点数：{float_num2}，类型：{type(float_num2)}")
```

### 科学计数法

```python
# 科学计数法
scientific_num1 = 1.5e3  # 1.5 × 10^3 = 1500
scientific_num2 = 2.5e-2  # 2.5 × 10^-2 = 0.025

print(f"科学计数法 1.5e3 = {scientific_num1}")
print(f"科学计数法 2.5e-2 = {scientific_num2}")
```

### 特殊浮点数值

```python
# 特殊浮点数值
infinity = float('inf')      # 无穷大
neg_infinity = float('-inf') # 负无穷大
not_a_number = float('nan')  # 非数字

print(f"正无穷：{infinity}")
print(f"负无穷：{neg_infinity}")
print(f"非数字：{not_a_number}")
```

### 浮点数特点

- 有小数部分
- 支持科学计数法
- 有精度限制
- 支持特殊值（inf, -inf, nan）

### 浮点数精度问题

```python
# 浮点数精度演示
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")
print(f"是否等于0.3：{result == 0.3}")
print(f"正确的比较方法：{abs(result - 0.3) < 1e-10}")
```

## 3. 字符串类型 (str)

字符串是用引号包围的文本。

### 基本用法

```python
# 单引号字符串
single_quote_str = 'Hello World'
print(f"单引号字符串：{single_quote_str}，类型：{type(single_quote_str)}")

# 双引号字符串
double_quote_str = "Python编程"
print(f"双引号字符串：{double_quote_str}，类型：{type(double_quote_str)}")

# 空字符串
empty_str = ""
print(f"空字符串：'{empty_str}'，长度：{len(empty_str)}")
```

### 多行字符串

```python
# 三引号字符串（多行字符串）
multi_line_str = """这是一个
多行字符串
可以包含换行符"""
print(f"多行字符串：{multi_line_str}")
```

### 字符串中包含引号

```python
# 字符串中包含引号
quote_in_str1 = "他说：'你好！'"
quote_in_str2 = '她回答："很高兴见到你！"'

print(f"字符串中包含单引号：{quote_in_str1}")
print(f"字符串中包含双引号：{quote_in_str2}")
```

### 转义字符和原始字符串

```python
# 转义字符
escape_str = "第一行\n第二行\t制表符\\反斜杠"
print(f"转义字符示例：{escape_str}")

# 原始字符串（r字符串）
raw_str = r"C:\Users\name\Documents"
print(f"原始字符串：{raw_str}")
```

### 字符串特点

- 用引号包围的文本
- 支持单引号、双引号、三引号
- 支持转义字符
- 不可变类型

## 4. 布尔值类型 (bool)

布尔值只有两个值：True 和 False。

### 基本用法

```python
# 布尔值
bool_true = True
bool_false = False

print(f"True：{bool_true}，类型：{type(bool_true)}")
print(f"False：{bool_false}，类型：{type(bool_false)}")
```

### 布尔值的数值表示

```python
# 布尔值的数值表示
print(f"True 的数值：{int(bool_true)}")
print(f"False 的数值：{int(bool_false)}")

# 布尔运算
print(f"True + True = {True + True}")
print(f"True * 5 = {True * 5}")
```

### 比较运算产生布尔值

```python
# 比较运算产生布尔值
comparison1 = 5 > 3
comparison2 = 10 == 5
comparison3 = "hello" == "world"

print(f"5 > 3 的结果：{comparison1}")
print(f"10 == 5 的结果：{comparison2}")
print(f"'hello' == 'world' 的结果：{comparison3}")
```

### 布尔值特点

- 只有True和False两个值
- 用于逻辑判断
- 可以转换为数字（True=1, False=0）
- 在数学运算中被当作数字使用

## 5. 使用type()函数查看数据类型

```python
# 创建不同类型的变量
num_int = 100
num_float = 3.14
text = "Hello"
is_valid = True

# 使用type()函数查看变量类型
print(f"type({num_int}) = {type(num_int)}")
print(f"type({num_float}) = {type(num_float)}")
print(f"type('{text}') = {type(text)}")
print(f"type({is_valid}) = {type(is_valid)}")
```

## 实践练习

请尝试创建以下变量并查看它们的类型：

1. 一个表示年龄的整数
2. 一个表示身高的浮点数
3. 一个表示姓名的字符串
4. 一个表示是否成年的布尔值

### 练习示例

```python
# 练习答案示例
age = 25
height = 175.5
name = "张三"
is_adult = True

print(f"年龄：{age}，类型：{type(age)}")
print(f"身高：{height}，类型：{type(height)}")
print(f"姓名：{name}，类型：{type(name)}")
print(f"是否成年：{is_adult}，类型：{type(is_adult)}")
```

## 思考题

1. 为什么 3.0 是 float 类型而不是 int 类型？
2. 字符串 '123' 和 整数 123 有什么区别？
3. True + True 的结果是什么？为什么？
4. 如何判断一个变量是否为字符串类型？

### 思考题答案

1. **因为有小数点**，Python将其识别为浮点数
2. **'123'是字符串**，不能进行数学运算；**123是整数**，可以进行数学运算
3. **True + True = 2**，因为True在数学运算中被当作1
4. **使用 type(变量) == str 或 isinstance(变量, str)**

## 常见错误和注意事项

### 常见错误

1. **混淆字符串和数字**：'123' + 456 会报错
2. **浮点数精度问题**：0.1 + 0.2 可能不等于 0.3
3. **大小写敏感**：true 和 True 是不同的

### 注意事项

- 字符串和数字不能直接相加，需要类型转换
- 浮点数比较时要考虑精度问题
- Python区分大小写，布尔值必须是True/False
- 使用type()函数可以准确判断数据类型

## 完整代码示例

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第二课：数据类型详解

学习目标：
1. 了解Python的基本数据类型
2. 掌握整数(int)类型的特点和用法
3. 掌握浮点数(float)类型的特点和用法
4. 掌握字符串(str)类型的特点和用法
5. 掌握布尔值(bool)类型的特点和用法
6. 学会使用type()函数查看数据类型
"""

print("=" * 50)
print("第二课：数据类型详解")
print("=" * 50)

# 1. 整数类型演示
print("\n1. 整数类型 (int)")
positive_num = 42
negative_num = -17
zero = 0
big_num = 123456789012345678901234567890

print(f"正整数：{positive_num}，类型：{type(positive_num)}")
print(f"负整数：{negative_num}，类型：{type(negative_num)}")
print(f"零：{zero}，类型：{type(zero)}")
print(f"大整数：{big_num}")

# 不同进制
binary_num = 0b1010
octal_num = 0o12
hex_num = 0xa
print(f"二进制 0b1010 = {binary_num}")
print(f"八进制 0o12 = {octal_num}")
print(f"十六进制 0xa = {hex_num}")

# 2. 浮点数类型演示
print("\n2. 浮点数类型 (float)")
float_num1 = 3.14
float_num2 = -2.5
scientific_num1 = 1.5e3
scientific_num2 = 2.5e-2

print(f"浮点数：{float_num1}，类型：{type(float_num1)}")
print(f"负浮点数：{float_num2}，类型：{type(float_num2)}")
print(f"科学计数法 1.5e3 = {scientific_num1}")
print(f"科学计数法 2.5e-2 = {scientific_num2}")

# 3. 字符串类型演示
print("\n3. 字符串类型 (str)")
single_quote_str = 'Hello World'
double_quote_str = "Python编程"
multi_line_str = """这是一个
多行字符串"""
empty_str = ""

print(f"单引号字符串：{single_quote_str}")
print(f"双引号字符串：{double_quote_str}")
print(f"多行字符串：{multi_line_str}")
print(f"空字符串长度：{len(empty_str)}")

# 4. 布尔值类型演示
print("\n4. 布尔值类型 (bool)")
bool_true = True
bool_false = False
comparison = 5 > 3

print(f"True：{bool_true}，类型：{type(bool_true)}")
print(f"False：{bool_false}，类型：{type(bool_false)}")
print(f"5 > 3 的结果：{comparison}")
print(f"True + True = {True + True}")

# 5. 类型检查
print("\n5. 使用type()函数")
variables = [100, 3.14, "Hello", True]
for var in variables:
    print(f"type({var}) = {type(var)}")

print("\n=" * 50)
print("第二课学习完成！")
print("下一课将学习Python的动态类型特性")
print("=" * 50)
```

## 运行方法

在终端中输入以下命令运行代码：

```bash
python 02_data_types.py
```

## 学习要点

1. **掌握四种基本数据类型**：int、float、str、bool
2. **理解每种类型的特点和用法**
3. **学会使用type()函数检查类型**
4. **注意浮点数精度问题**
5. **理解布尔值的数值特性**
6. **掌握字符串的多种表示方法**

## 下一步

学习完数据类型后，继续学习：[动态类型特性演示](./03_dynamic_typing)