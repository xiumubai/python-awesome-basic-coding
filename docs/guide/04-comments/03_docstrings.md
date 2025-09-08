# 文档字符串（Docstrings）

## 学习目标

通过本节学习，你将掌握：
- 理解文档字符串的概念和作用
- 掌握模块、函数、类的文档字符串写法
- 了解不同风格的文档字符串格式
- 学会使用help()函数查看文档
- 掌握文档字符串的最佳实践

## 主要内容

文档字符串（Docstrings）是Python中用于描述模块、类、函数或方法功能的特殊字符串。它们使用三重引号定义，并且可以通过`__doc__`属性访问。

### 核心特点
- 使用三重引号（"""或'''）定义
- 位于模块、类或函数的开头
- 可通过`__doc__`属性访问
- 支持多种格式风格
- 是代码自文档化的重要工具

## 完整代码

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文档字符串（Docstrings）的使用

本文件演示Python中文档字符串的各种使用方法和规范。
文档字符串是Python中用于描述模块、类、函数或方法功能的特殊字符串。
它们使用三重引号定义，并且可以通过__doc__属性访问。

作者: Python学习教程
日期: 2024
版本: 1.0
"""

import math

# ============================================================
# 1. 模块级文档字符串（已在文件顶部定义）
# ============================================================

print("模块文档字符串:")
print(__doc__)
print("=" * 50)

# ============================================================
# 2. 函数文档字符串
# ============================================================

def calculate_area(radius):
    """
    计算圆的面积。
    
    这个函数接受一个半径值，返回对应圆的面积。
    使用数学公式：面积 = π × 半径²
    
    参数:
        radius (float): 圆的半径，必须为正数
    
    返回:
        float: 圆的面积
    
    异常:
        ValueError: 当半径为负数时抛出
    
    示例:
        >>> calculate_area(5)
        78.53981633974483
        >>> calculate_area(0)
        0.0
    """
    if radius < 0:
        raise ValueError("半径不能为负数")
    
    return math.pi * radius ** 2

# 测试函数并显示其文档字符串
print("函数文档字符串:")
print(calculate_area.__doc__)
print(f"圆的面积（半径=5）: {calculate_area(5)}")
print("=" * 50)

# ============================================================
# 3. 类文档字符串
# ============================================================

class Student:
    """
    学生类，用于管理学生信息。
    
    这个类提供了创建和管理学生对象的功能，包括姓名、年龄、成绩等信息。
    支持添加成绩、计算平均分、获取学生信息等操作。
    
    属性:
        name (str): 学生姓名
        age (int): 学生年龄
        grades (list): 学生成绩列表
    
    示例:
        >>> student = Student("张三", 18)
        >>> student.add_grade(85)
        >>> student.get_average()
        85.0
    """
    
    def __init__(self, name, age):
        """
        初始化学生对象。
        
        参数:
            name (str): 学生姓名
            age (int): 学生年龄
        """
        self.name = name
        self.age = age
        self.grades = []
    
    def add_grade(self, grade):
        """
        添加一个成绩到学生的成绩列表中。
        
        参数:
            grade (float): 要添加的成绩，范围应在0-100之间
        
        异常:
            ValueError: 当成绩不在有效范围内时抛出
        """
        if not 0 <= grade <= 100:
            raise ValueError("成绩必须在0-100之间")
        
        self.grades.append(grade)
    
    def get_average(self):
        """
        计算学生的平均成绩。
        
        返回:
            float: 平均成绩，如果没有成绩则返回0
        """
        if not self.grades:
            return 0
        
        return sum(self.grades) / len(self.grades)
    
    def get_info(self):
        """
        获取学生的详细信息。
        
        返回:
            str: 包含学生姓名、年龄、成绩数量和平均分的字符串
        """
        avg = self.get_average()
        return f"姓名: {self.name}, 年龄: {self.age}, 成绩数量: {len(self.grades)}, 平均分: {avg:.2f}"

# 测试类并显示其文档字符串
print("类文档字符串:")
print(Student.__doc__)
print("\n方法文档字符串:")
print(Student.add_grade.__doc__)

# 创建学生对象并测试
student = Student("李四", 19)
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)
print(f"\n学生信息: {student.get_info()}")
print("=" * 50)

# ============================================================
# 4. 不同风格的文档字符串
# ============================================================

# Google风格的文档字符串
def google_style_function(param1, param2):
    """
    Google风格的文档字符串示例。
    
    Args:
        param1 (int): 第一个参数的描述
        param2 (str): 第二个参数的描述
    
    Returns:
        bool: 返回值的描述
    
    Raises:
        ValueError: 异常情况的描述
    """
    return True

# NumPy风格的文档字符串
def numpy_style_function(param1, param2):
    """
    NumPy风格的文档字符串示例。
    
    Parameters
    ----------
    param1 : int
        第一个参数的描述
    param2 : str
        第二个参数的描述
    
    Returns
    -------
    bool
        返回值的描述
    
    Raises
    ------
    ValueError
        异常情况的描述
    """
    return True

# Sphinx风格的文档字符串
def sphinx_style_function(param1, param2):
    """
    Sphinx风格的文档字符串示例。
    
    :param param1: 第一个参数的描述
    :type param1: int
    :param param2: 第二个参数的描述
    :type param2: str
    :returns: 返回值的描述
    :rtype: bool
    :raises ValueError: 异常情况的描述
    """
    return True

print("不同风格的文档字符串:")
print("\nGoogle风格:")
print(google_style_function.__doc__)
print("\nNumPy风格:")
print(numpy_style_function.__doc__)
print("\nSphinx风格:")
print(sphinx_style_function.__doc__)
print("=" * 50)

# ============================================================
# 5. 使用help()函数查看文档
# ============================================================

def demo_function(x, y=10):
    """
    演示函数，用于展示help()的效果。
    
    参数:
        x (int): 必需参数
        y (int, optional): 可选参数，默认值为10
    
    返回:
        int: x和y的和
    """
    return x + y

print("使用help()函数查看文档:")
print("help(demo_function)的输出:")
help(demo_function)
print("=" * 50)

# ============================================================
# 6. 文档字符串的最佳实践
# ============================================================

def best_practice_example(data, threshold=0.5, normalize=True):
    """
    文档字符串最佳实践示例。
    
    这个函数演示了如何编写高质量的文档字符串。
    应该包含简洁的一行摘要，详细的描述，参数说明，
    返回值说明，异常说明和使用示例。
    
    参数:
        data (list): 输入数据列表，包含数值
        threshold (float, optional): 阈值，默认为0.5
        normalize (bool, optional): 是否标准化数据，默认为True
    
    返回:
        list: 处理后的数据列表
    
    异常:
        TypeError: 当data不是列表时抛出
        ValueError: 当threshold不在0-1范围内时抛出
    
    示例:
        >>> data = [1, 2, 3, 4, 5]
        >>> result = best_practice_example(data)
        >>> print(result)
        [0.0, 0.25, 0.5, 0.75, 1.0]
    
    注意:
        这个函数会修改原始数据，如果需要保留原数据，
        请传入数据的副本。
    
    版本:
        添加于版本1.0
    """
    if not isinstance(data, list):
        raise TypeError("data必须是列表类型")
    
    if not 0 <= threshold <= 1:
        raise ValueError("threshold必须在0-1之间")
    
    if normalize and data:
        min_val = min(data)
        max_val = max(data)
        if max_val != min_val:
            data = [(x - min_val) / (max_val - min_val) for x in data]
    
    return [x for x in data if x >= threshold]

# 测试最佳实践示例
test_data = [1, 2, 3, 4, 5]
result = best_practice_example(test_data.copy())
print(f"最佳实践示例结果: {result}")

print("\n=== 文档字符串演示完成 ===")
print("文档字符串是Python代码自文档化的重要工具")
print("良好的文档字符串可以大大提高代码的可维护性")
print("建议使用一致的风格和格式来编写文档字符串")

# 运行这个文件来查看文档字符串的效果
# 在终端中执行: python 03_docstrings.py
# 也可以在Python交互式环境中使用help()函数查看文档
```

## 代码解释

### 1. 模块级文档字符串
- 位于文件开头，描述整个模块的功能
- 可通过`__doc__`属性访问
- 应包含模块的用途、作者、版本等信息

### 2. 函数文档字符串
- 位于函数定义后的第一行
- 描述函数的功能、参数、返回值和异常
- 可包含使用示例

### 3. 类文档字符串
- 位于类定义后的第一行
- 描述类的功能、属性和使用方法
- 方法也可以有自己的文档字符串

### 4. 不同风格的文档字符串
- **Google风格**：使用Args、Returns、Raises等标签
- **NumPy风格**：使用分隔线和结构化格式
- **Sphinx风格**：使用:param、:returns等指令

### 5. help()函数
- 可以查看对象的文档字符串
- 提供格式化的文档显示
- 是Python内置的帮助系统

## 最佳实践

1. **一行摘要**：第一行应该是简洁的功能描述
2. **详细描述**：空一行后提供详细的功能说明
3. **参数说明**：清楚地描述每个参数的类型和用途
4. **返回值说明**：说明返回值的类型和含义
5. **异常说明**：列出可能抛出的异常
6. **使用示例**：提供实际的使用例子
7. **保持一致**：在项目中使用统一的风格

## 运行示例

```bash
# 运行完整示例
python 03_docstrings.py

# 在Python交互式环境中查看文档
python
>>> import 03_docstrings
>>> help(03_docstrings.calculate_area)
>>> help(03_docstrings.Student)
```

## 学习要点

- 文档字符串是代码自文档化的重要工具
- 使用三重引号定义，位于模块、类、函数的开头
- 可通过`__doc__`属性或help()函数访问
- 应该包含功能描述、参数说明、返回值和异常信息
- 选择一种风格并在项目中保持一致
- 良好的文档字符串可以大大提高代码的可维护性

---

## 导航

- [上一节：多行注释](./multi-line-comments.md)
- [下一节：行内注释](./inline-comments.md)
- [返回目录](./index.md)