# 动态类型特性

## 学习目标

通过本节学习，你将掌握：

1. 理解什么是动态类型
2. 了解Python与静态类型语言的区别
3. 掌握变量类型的动态变化
4. 理解动态类型的优缺点
5. 学会在实际编程中合理使用动态类型

## 什么是动态类型？

动态类型是指变量的类型在运行时确定，而不是在编译时确定。同一个变量可以在不同时间存储不同类型的数据。Python是动态类型语言。

## 动态类型的基本演示

```python
# 创建一个变量，初始为整数
variable = 42
print(f"初始值：{variable}，类型：{type(variable)}")

# 同一个变量现在存储字符串
variable = "Hello World"
print(f"现在的值：{variable}，类型：{type(variable)}")

# 同一个变量现在存储浮点数
variable = 3.14
print(f"现在的值：{variable}，类型：{type(variable)}")

# 同一个变量现在存储布尔值
variable = True
print(f"现在的值：{variable}，类型：{type(variable)}")

# 同一个变量现在存储列表
variable = [1, 2, 3, 4, 5]
print(f"现在的值：{variable}，类型：{type(variable)}")
```

**观察**：同一个变量名可以存储完全不同类型的数据！

## 与静态类型语言的对比

**静态类型语言（如C++、Java）：**
```cpp
int number = 42;        // 声明number为整数类型
number = 'hello';       // 错误！不能将字符串赋给整数变量
```

**动态类型语言（Python）：**
```python
number = 42             # number现在是整数
number = 'hello'        # 完全可以！number现在是字符串
```

## 动态类型的实际应用场景

### 场景1：处理不同类型的用户输入

```python
def process_input(user_input):
    """处理用户输入，输入可能是不同类型"""
    print(f"接收到输入：{user_input}，类型：{type(user_input)}")
    
    if isinstance(user_input, int):
        return user_input * 2
    elif isinstance(user_input, str):
        return user_input.upper()
    elif isinstance(user_input, float):
        return round(user_input, 2)
    else:
        return f"未知类型：{type(user_input)}"

# 测试不同类型的输入
inputs = [42, "hello", 3.14159, True, [1, 2, 3]]
for inp in inputs:
    result = process_input(inp)
    print(f"处理结果：{result}")
```

### 场景2：配置参数的灵活处理

```python
config = {}

# 配置可以是不同类型的值
config['debug'] = True          # 布尔值
config['port'] = 8080          # 整数
config['host'] = 'localhost'   # 字符串
config['timeout'] = 30.5       # 浮点数
config['features'] = ['auth', 'logging']  # 列表

print("配置参数：")
for key, value in config.items():
    print(f"  {key}: {value} ({type(value).__name__})")
```

## 动态类型检查和处理

```python
def safe_divide(a, b):
    """安全除法，处理不同类型的输入"""
    print(f"尝试计算 {a} ÷ {b}")
    print(f"a的类型：{type(a)}，b的类型：{type(b)}")
    
    # 检查是否为数字类型
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "错误：参数必须是数字类型"
    
    # 检查除零错误
    if b == 0:
        return "错误：除数不能为零"
    
    result = a / b
    return f"结果：{result}"

# 测试不同类型的参数
test_cases = [
    (10, 2),           # 正常情况
    (10.5, 2.5),       # 浮点数
    (10, 0),           # 除零错误
    ("10", 2),         # 字符串参数
    (10, "2"),         # 字符串参数
]

for a, b in test_cases:
    result = safe_divide(a, b)
    print(f"  {result}")
```

## 变量类型的运行时变化

```python
# 模拟一个数据处理流程
data = "123"  # 开始是字符串
print(f"步骤1 - 原始数据：{data} ({type(data).__name__})")

# 转换为整数进行计算
data = int(data)
print(f"步骤2 - 转换为整数：{data} ({type(data).__name__})")

# 进行数学运算
data = data * 2
print(f"步骤3 - 数学运算后：{data} ({type(data).__name__})")

# 转换为浮点数进行精确计算
data = float(data)
print(f"步骤4 - 转换为浮点数：{data} ({type(data).__name__})")

# 格式化为字符串输出
data = f"最终结果：{data:.2f}"
print(f"步骤5 - 格式化输出：{data} ({type(data).__name__})")
```

## 动态类型的优点

### 1. 灵活性高
- 同一个变量可以存储不同类型的数据
- 函数可以接受多种类型的参数

### 2. 代码简洁
- 不需要声明变量类型
- 减少了类型转换的代码

### 3. 快速开发
- 专注于逻辑实现而不是类型管理
- 适合原型开发和脚本编写

## 动态类型的缺点

### 1. 运行时错误
- 类型错误只在运行时才能发现
- 可能导致程序崩溃

### 2. 性能开销
- 需要在运行时检查类型
- 内存使用可能不够优化

### 3. 调试困难
- 类型相关的错误可能难以追踪
- IDE的代码提示可能不够准确

## 潜在的类型错误示例

```python
try:
    x = "5"
    y = 3
    # 这会导致类型错误
    result = x + y  # 字符串和整数不能直接相加
except TypeError as e:
    print(f"类型错误：{e}")
```

## 最佳实践

### 1. 使用类型检查
- 使用isinstance()检查类型
- 在函数开始处验证参数类型

### 2. 添加类型注解（Python 3.5+）
- 使用类型提示提高代码可读性
- 帮助IDE提供更好的代码提示

### 3. 编写测试
- 测试不同类型的输入
- 确保类型错误被正确处理

## 类型注解示例

```python
def add_numbers(a: int, b: int) -> int:
    """带类型注解的函数示例"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("参数必须是整数类型")
    return a + b

print(f"add_numbers(5, 3) = {add_numbers(5, 3)}")

try:
    add_numbers("5", 3)
except TypeError as e:
    print(f"类型检查捕获错误：{e}")
```

## 实践练习

### 练习1：变量类型变化
创建一个变量，依次赋予不同类型的值，并打印类型：

```python
practice_var = 100
print(f"整数：{practice_var} - {type(practice_var)}")
practice_var = 3.14
print(f"浮点数：{practice_var} - {type(practice_var)}")
practice_var = "Python"
print(f"字符串：{practice_var} - {type(practice_var)}")
```

### 练习2：多类型处理函数
编写一个函数，能够处理整数、浮点数和字符串三种类型的输入：

```python
def flexible_function(value):
    """处理多种类型输入的函数"""
    if isinstance(value, int):
        return f"整数处理：{value} * 2 = {value * 2}"
    elif isinstance(value, float):
        return f"浮点数处理：{value} 的平方根约为 {value ** 0.5:.2f}"
    elif isinstance(value, str):
        return f"字符串处理：'{value}' 的长度是 {len(value)}"
    else:
        return f"未知类型：{type(value)}"

test_values = [42, 16.0, "Hello"]
for val in test_values:
    print(flexible_function(val))
```

### 练习3：类型检查
使用isinstance()函数检查变量类型并进行相应处理。

## 完整代码示例

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
动态类型特性演示

学习目标：
1. 理解什么是动态类型
2. 了解Python与静态类型语言的区别
3. 掌握变量类型的动态变化
4. 理解动态类型的优缺点
5. 学会在实际编程中合理使用动态类型
"""

print("=" * 50)
print("动态类型特性演示")
print("=" * 50)

# 动态类型基本演示
variable = 42
print(f"初始值：{variable}，类型：{type(variable)}")

variable = "Hello World"
print(f"现在的值：{variable}，类型：{type(variable)}")

variable = 3.14
print(f"现在的值：{variable}，类型：{type(variable)}")

variable = True
print(f"现在的值：{variable}，类型：{type(variable)}")

variable = [1, 2, 3, 4, 5]
print(f"现在的值：{variable}，类型：{type(variable)}")

print("\n观察：同一个变量名可以存储完全不同类型的数据！")
```

## 运行方法

在终端中运行：
```bash
python 03_dynamic_typing.py
```

或者在IDE中直接运行该文件。

## 小结

动态类型是Python的重要特性之一，它提供了极大的灵活性，但也需要开发者更加小心地处理类型相关的问题。通过合理使用类型检查、类型注解和异常处理，可以在享受动态类型便利的同时，避免潜在的类型错误。

下一节我们将学习类型转换，了解如何在不同数据类型之间进行转换。