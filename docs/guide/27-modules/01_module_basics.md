# 01. 模块基础概念

## 学习目标

- 理解什么是Python模块
- 掌握模块的作用和重要性
- 学会创建简单的模块
- 了解模块的基本组成部分

## 什么是模块

模块（Module）是包含Python代码的文件。任何以`.py`为扩展名的Python文件都可以作为模块被其他Python程序导入和使用。模块是Python代码组织和重用的基本单位。

### 模块的作用

1. **代码组织**：将相关的函数、类和变量组织在一起
2. **代码重用**：避免重复编写相同的代码
3. **命名空间**：提供独立的命名空间，避免名称冲突
4. **模块化开发**：支持大型项目的模块化开发

## 模块的基本结构

一个典型的Python模块包含以下组成部分：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模块文档字符串
描述模块的功能和用途
"""

# 导入语句
import os
import sys

# 模块级别的常量
MODULE_VERSION = "1.0.0"
DEFAULT_VALUE = 42

# 模块级别的变量
counter = 0
data_cache = {}

# 函数定义
def my_function():
    """函数文档字符串"""
    pass

# 类定义
class MyClass:
    """类文档字符串"""
    pass

# 模块级别的可执行代码
if __name__ == '__main__':
    # 当模块被直接执行时运行的代码
    print("模块被直接执行")
```

## 创建简单模块示例

让我们看一个完整的模块示例：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数学工具模块 - 提供基本的数学计算功能

这个模块包含了一些常用的数学函数和常量，
用于演示Python模块的基本概念和使用方法。

Author: Python学习者
Version: 1.0.0
Date: 2024
"""

import math
from typing import Union, List

# 模块信息
__version__ = "1.0.0"
__author__ = "Python学习者"

print(f"数学工具模块 v{__version__} 已加载")

# 模块级别的常量
PI = 3.14159265359
E = 2.71828182846
GOLDEN_RATIO = 1.61803398875

# 模块级别的变量
calculation_count = 0
last_result = None

# 基本数学函数
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    计算两个数的和
    
    Args:
        a: 第一个数
        b: 第二个数
    
    Returns:
        两个数的和
    
    Example:
        >>> add(2, 3)
        5
    """
    global calculation_count, last_result
    calculation_count += 1
    last_result = a + b
    return last_result

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    计算两个数的乘积
    
    Args:
        a: 第一个数
        b: 第二个数
    
    Returns:
        两个数的乘积
    
    Example:
        >>> multiply(3, 4)
        12
    """
    global calculation_count, last_result
    calculation_count += 1
    last_result = a * b
    return last_result

def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """
    计算幂运算
    
    Args:
        base: 底数
        exponent: 指数
    
    Returns:
        base的exponent次幂
    
    Example:
        >>> power(2, 3)
        8
    """
    global calculation_count, last_result
    calculation_count += 1
    last_result = base ** exponent
    return last_result

def factorial(n: int) -> int:
    """
    计算阶乘
    
    Args:
        n: 非负整数
    
    Returns:
        n的阶乘
    
    Raises:
        ValueError: 当n为负数时
    
    Example:
        >>> factorial(5)
        120
    """
    if n < 0:
        raise ValueError("阶乘的参数必须是非负整数")
    
    global calculation_count, last_result
    calculation_count += 1
    
    if n == 0 or n == 1:
        last_result = 1
    else:
        last_result = n * factorial(n - 1)
    
    return last_result

# 统计函数
def average(numbers: List[Union[int, float]]) -> float:
    """
    计算数字列表的平均值
    
    Args:
        numbers: 数字列表
    
    Returns:
        平均值
    
    Raises:
        ValueError: 当列表为空时
    
    Example:
        >>> average([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        raise ValueError("列表不能为空")
    
    global calculation_count, last_result
    calculation_count += 1
    last_result = sum(numbers) / len(numbers)
    return last_result

def find_max(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    找到列表中的最大值
    
    Args:
        numbers: 数字列表
    
    Returns:
        最大值
    
    Raises:
        ValueError: 当列表为空时
    
    Example:
        >>> find_max([1, 5, 3, 9, 2])
        9
    """
    if not numbers:
        raise ValueError("列表不能为空")
    
    global calculation_count, last_result
    calculation_count += 1
    last_result = max(numbers)
    return last_result

# 几何函数
def circle_area(radius: Union[int, float]) -> float:
    """
    计算圆的面积
    
    Args:
        radius: 圆的半径
    
    Returns:
        圆的面积
    
    Raises:
        ValueError: 当半径为负数时
    
    Example:
        >>> circle_area(5)
        78.53981633974483
    """
    if radius < 0:
        raise ValueError("半径必须是非负数")
    
    global calculation_count, last_result
    calculation_count += 1
    last_result = PI * radius * radius
    return last_result

def rectangle_area(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
    """
    计算矩形的面积
    
    Args:
        length: 矩形的长
        width: 矩形的宽
    
    Returns:
        矩形的面积
    
    Raises:
        ValueError: 当长或宽为负数时
    
    Example:
        >>> rectangle_area(4, 6)
        24
    """
    if length < 0 or width < 0:
        raise ValueError("长和宽必须是非负数")
    
    global calculation_count, last_result
    calculation_count += 1
    last_result = length * width
    return last_result

# 计算器类
class SimpleCalculator:
    """
    简单计算器类
    
    提供基本的四则运算功能，并记录计算历史。
    
    Attributes:
        history: 计算历史记录
        result: 当前结果
    
    Example:
        >>> calc = SimpleCalculator()
        >>> calc.add(5, 3)
        8
        >>> calc.get_history()
        ['5 + 3 = 8']
    """
    
    def __init__(self):
        """
        初始化计算器
        """
        self.history = []
        self.result = 0
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        加法运算
        
        Args:
            a: 第一个数
            b: 第二个数
        
        Returns:
            计算结果
        """
        self.result = a + b
        self.history.append(f"{a} + {b} = {self.result}")
        return self.result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        减法运算
        
        Args:
            a: 被减数
            b: 减数
        
        Returns:
            计算结果
        """
        self.result = a - b
        self.history.append(f"{a} - {b} = {self.result}")
        return self.result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        乘法运算
        
        Args:
            a: 第一个数
            b: 第二个数
        
        Returns:
            计算结果
        """
        self.result = a * b
        self.history.append(f"{a} × {b} = {self.result}")
        return self.result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        除法运算
        
        Args:
            a: 被除数
            b: 除数
        
        Returns:
            计算结果
        
        Raises:
            ZeroDivisionError: 当除数为0时
        """
        if b == 0:
            raise ZeroDivisionError("除数不能为0")
        
        self.result = a / b
        self.history.append(f"{a} ÷ {b} = {self.result}")
        return self.result
    
    def get_result(self) -> Union[int, float]:
        """
        获取当前结果
        
        Returns:
            当前计算结果
        """
        return self.result
    
    def get_history(self) -> List[str]:
        """
        获取计算历史
        
        Returns:
            计算历史记录列表
        """
        return self.history.copy()
    
    def clear_history(self) -> None:
        """
        清空计算历史
        """
        self.history.clear()
        self.result = 0

# 工具函数
def get_module_info() -> dict:
    """
    获取模块信息
    
    Returns:
        包含模块信息的字典
    
    Example:
        >>> info = get_module_info()
        >>> info['version']
        '1.0.0'
    """
    return {
        'name': '数学工具模块',
        'version': __version__,
        'author': __author__,
        'calculation_count': calculation_count,
        'last_result': last_result,
        'constants': {
            'PI': PI,
            'E': E,
            'GOLDEN_RATIO': GOLDEN_RATIO
        }
    }

def reset_module_state() -> None:
    """
    重置模块状态
    
    将计算计数器和最后结果重置为初始状态。
    
    Example:
        >>> reset_module_state()
    """
    global calculation_count, last_result
    calculation_count = 0
    last_result = None
    print("模块状态已重置")

def print_module_info() -> None:
    """
    打印模块信息
    
    Example:
        >>> print_module_info()
    """
    info = get_module_info()
    print(f"\n=== {info['name']} ===")
    print(f"版本: {info['version']}")
    print(f"作者: {info['author']}")
    print(f"计算次数: {info['calculation_count']}")
    print(f"最后结果: {info['last_result']}")
    print(f"常量: PI={info['constants']['PI']}, E={info['constants']['E']}")
    print("=" * 30)

# 模块级别的测试代码
if __name__ == '__main__':
    print("\n=== 数学工具模块测试 ===")
    
    # 测试基本函数
    print("\n1. 基本数学函数测试：")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"multiply(4, 6) = {multiply(4, 6)}")
    print(f"power(2, 8) = {power(2, 8)}")
    print(f"factorial(5) = {factorial(5)}")
    
    # 测试统计函数
    print("\n2. 统计函数测试：")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"numbers = {numbers}")
    print(f"average(numbers) = {average(numbers)}")
    print(f"find_max(numbers) = {find_max(numbers)}")
    
    # 测试几何函数
    print("\n3. 几何函数测试：")
    print(f"circle_area(5) = {circle_area(5)}")
    print(f"rectangle_area(4, 6) = {rectangle_area(4, 6)}")
    
    # 测试计算器类
    print("\n4. 计算器类测试：")
    calc = SimpleCalculator()
    print(f"calc.add(10, 5) = {calc.add(10, 5)}")
    print(f"calc.subtract(20, 8) = {calc.subtract(20, 8)}")
    print(f"calc.multiply(3, 7) = {calc.multiply(3, 7)}")
    print(f"calc.divide(15, 3) = {calc.divide(15, 3)}")
    
    print("\n计算历史：")
    for record in calc.get_history():
        print(f"  {record}")
    
    # 显示模块信息
    print("\n5. 模块信息：")
    print_module_info()
    
    print("\n=== 测试完成 ===")
```

## 模块的组成部分详解

### 1. 模块文档字符串

模块的第一个字符串字面量作为模块的文档字符串，用于描述模块的功能和用途：

```python
"""
这是模块的文档字符串
描述模块的功能、用途、作者等信息
"""
```

### 2. 导入语句

在模块开头导入所需的其他模块：

```python
import os
import sys
from typing import List, Dict
```

### 3. 模块级别的变量和常量

定义模块级别的变量和常量：

```python
# 常量（按惯例使用大写字母）
VERSION = "1.0.0"
DEFAULT_SIZE = 100

# 变量
counter = 0
data_cache = {}
```

### 4. 函数定义

定义模块提供的函数：

```python
def my_function(param1, param2):
    """
    函数文档字符串
    """
    # 函数实现
    return result
```

### 5. 类定义

定义模块提供的类：

```python
class MyClass:
    """
    类文档字符串
    """
    
    def __init__(self):
        # 初始化方法
        pass
    
    def method(self):
        # 类方法
        pass
```

### 6. 条件执行代码

使用`if __name__ == '__main__':`来定义只在模块被直接执行时运行的代码：

```python
if __name__ == '__main__':
    # 测试代码或主程序逻辑
    print("模块被直接执行")
    # 运行测试或示例代码
```

## 模块的使用

### 导入整个模块

```python
import math_tools

# 使用模块中的函数
result = math_tools.add(5, 3)
print(result)  # 输出: 8

# 使用模块中的类
calc = math_tools.SimpleCalculator()
result = calc.add(10, 20)
print(result)  # 输出: 30

# 访问模块中的常量
print(math_tools.PI)  # 输出: 3.14159265359
```

### 导入特定的名称

```python
from math_tools import add, multiply, PI

# 直接使用导入的名称
result1 = add(5, 3)
result2 = multiply(4, 6)
print(f"PI = {PI}")
```

### 使用别名

```python
import math_tools as mt
from math_tools import SimpleCalculator as Calc

# 使用别名
result = mt.add(5, 3)
calc = Calc()
```

## 学习要点

1. **模块就是文件**：任何`.py`文件都可以作为模块
2. **命名空间**：模块提供独立的命名空间，避免名称冲突
3. **代码组织**：将相关功能组织在同一个模块中
4. **文档重要性**：编写清晰的文档字符串
5. **测试代码**：使用`if __name__ == '__main__':`添加测试代码

## 最佳实践

1. **模块命名**：使用小写字母和下划线，避免与标准库冲突
2. **文档字符串**：为模块、函数、类编写详细的文档
3. **导入顺序**：标准库 → 第三方库 → 本地模块
4. **避免循环导入**：合理设计模块依赖关系
5. **保持简洁**：一个模块应该专注于一个特定的功能领域

通过学习模块的基础概念，你已经掌握了Python代码组织的基本方法。接下来我们将学习各种导入语句的使用方法。