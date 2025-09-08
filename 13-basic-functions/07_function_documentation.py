#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
函数文档和注释详解

本文件演示Python函数的文档字符串和注释，包括：
1. 文档字符串（docstring）的基本用法
2. 不同风格的文档字符串
3. 函数注释和类型提示
4. 文档生成工具
5. 最佳实践

作者：Python学习教程
日期：2024年
"""

print("=" * 50)
print("Python 函数文档和注释详解")
print("=" * 50)

# 1. 基本文档字符串
print("\n1. 基本文档字符串")
print("-" * 30)

def simple_function():
    """这是一个简单的函数。"""
    return "Hello, World!"

def add_numbers(a, b):
    """将两个数字相加并返回结果。"""
    return a + b

def greet_user(name, greeting="Hello"):
    """
    向用户问候。
    
    这个函数接受用户名和可选的问候语，
    然后返回格式化的问候消息。
    """
    return f"{greeting}, {name}!"

print("基本文档字符串演示：")
print(f"simple_function文档：{simple_function.__doc__}")
print(f"add_numbers文档：{add_numbers.__doc__}")
print(f"greet_user文档：{greet_user.__doc__}")

# 使用help()函数查看文档
print("\n使用help()查看文档：")
help(greet_user)
print()

# 2. Google风格的文档字符串
print("\n2. Google风格的文档字符串")
print("-" * 30)

def calculate_area(length, width, unit="m"):
    """
    计算矩形面积。
    
    Args:
        length (float): 矩形的长度
        width (float): 矩形的宽度
        unit (str, optional): 长度单位. Defaults to "m".
    
    Returns:
        dict: 包含面积和单位的字典
        
    Raises:
        ValueError: 当长度或宽度为负数时
        TypeError: 当参数不是数字类型时
    
    Example:
        >>> calculate_area(5, 3)
        {'area': 15, 'unit': 'm²'}
        
        >>> calculate_area(10, 8, "cm")
        {'area': 80, 'unit': 'cm²'}
    """
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("长度和宽度必须是数字")
    
    if length < 0 or width < 0:
        raise ValueError("长度和宽度不能为负数")
    
    area = length * width
    return {
        "area": area,
        "unit": f"{unit}²"
    }

def process_data(data, operation="sum", **kwargs):
    """
    处理数据列表。
    
    Args:
        data (list): 要处理的数据列表
        operation (str, optional): 操作类型 ('sum', 'avg', 'max', 'min'). 
            Defaults to "sum".
        **kwargs: 额外的配置选项
            - round_digits (int): 结果保留的小数位数
            - filter_negative (bool): 是否过滤负数
    
    Returns:
        float: 处理后的结果
        
    Raises:
        ValueError: 当数据为空或操作类型无效时
        
    Note:
        这个函数支持多种数学操作，可以通过kwargs传递额外配置。
        
    Example:
        >>> process_data([1, 2, 3, 4, 5])
        15
        
        >>> process_data([1, 2, 3, 4, 5], "avg", round_digits=2)
        3.0
    """
    if not data:
        raise ValueError("数据列表不能为空")
    
    # 过滤负数（如果需要）
    if kwargs.get("filter_negative", False):
        data = [x for x in data if x >= 0]
    
    # 执行操作
    if operation == "sum":
        result = sum(data)
    elif operation == "avg":
        result = sum(data) / len(data)
    elif operation == "max":
        result = max(data)
    elif operation == "min":
        result = min(data)
    else:
        raise ValueError(f"不支持的操作类型：{operation}")
    
    # 四舍五入（如果需要）
    round_digits = kwargs.get("round_digits")
    if round_digits is not None:
        result = round(result, round_digits)
    
    return result

print("Google风格文档演示：")
print("calculate_area函数文档：")
help(calculate_area)

print("\nprocess_data函数使用示例：")
test_data = [1, 2, 3, 4, 5, -1, -2]
print(f"原始数据：{test_data}")
print(f"求和：{process_data(test_data)}")
print(f"平均值（保留2位小数）：{process_data(test_data, 'avg', round_digits=2)}")
print(f"最大值（过滤负数）：{process_data(test_data, 'max', filter_negative=True)}")
print()

# 3. NumPy/SciPy风格的文档字符串
print("\n3. NumPy/SciPy风格的文档字符串")
print("-" * 30)

def linear_regression(x_values, y_values):
    """
    执行简单线性回归。
    
    Parameters
    ----------
    x_values : list of float
        自变量值列表
    y_values : list of float
        因变量值列表
        
    Returns
    -------
    dict
        包含以下键的字典：
        - 'slope' : float
            回归线的斜率
        - 'intercept' : float
            回归线的截距
        - 'r_squared' : float
            决定系数（R²）
            
    Raises
    ------
    ValueError
        当输入列表长度不匹配或为空时
        
    Notes
    -----
    使用最小二乘法计算线性回归。公式为：
    
    .. math:: y = mx + b
    
    其中 m 是斜率，b 是截距。
    
    Examples
    --------
    >>> x = [1, 2, 3, 4, 5]
    >>> y = [2, 4, 6, 8, 10]
    >>> result = linear_regression(x, y)
    >>> print(f"斜率：{result['slope']}")
    斜率：2.0
    
    References
    ----------
    .. [1] 统计学习方法，李航著
    """
    if len(x_values) != len(y_values) or len(x_values) == 0:
        raise ValueError("x和y的长度必须相同且不为空")
    
    n = len(x_values)
    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_xy = sum(x * y for x, y in zip(x_values, y_values))
    sum_x2 = sum(x * x for x in x_values)
    
    # 计算斜率和截距
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
    intercept = (sum_y - slope * sum_x) / n
    
    # 计算R²
    y_mean = sum_y / n
    ss_tot = sum((y - y_mean) ** 2 for y in y_values)
    ss_res = sum((y - (slope * x + intercept)) ** 2 for x, y in zip(x_values, y_values))
    r_squared = 1 - (ss_res / ss_tot) if ss_tot != 0 else 1
    
    return {
        "slope": slope,
        "intercept": intercept,
        "r_squared": r_squared
    }

def matrix_multiply(matrix_a, matrix_b):
    """
    矩阵乘法。
    
    Parameters
    ----------
    matrix_a : list of list of float
        第一个矩阵，形状为 (m, n)
    matrix_b : list of list of float
        第二个矩阵，形状为 (n, p)
        
    Returns
    -------
    list of list of float
        结果矩阵，形状为 (m, p)
        
    Raises
    ------
    ValueError
        当矩阵维度不匹配时
        
    See Also
    --------
    linear_regression : 线性回归函数
    
    Examples
    --------
    >>> a = [[1, 2], [3, 4]]
    >>> b = [[5, 6], [7, 8]]
    >>> result = matrix_multiply(a, b)
    >>> print(result)
    [[19, 22], [43, 50]]
    """
    if not matrix_a or not matrix_b:
        raise ValueError("矩阵不能为空")
    
    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])
    
    if cols_a != rows_b:
        raise ValueError(f"矩阵维度不匹配：({rows_a}, {cols_a}) x ({rows_b}, {cols_b})")
    
    # 初始化结果矩阵
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    # 执行矩阵乘法
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    
    return result

print("NumPy风格文档演示：")
print("linear_regression函数使用：")
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 6, 8, 10]
regression_result = linear_regression(x_data, y_data)
print(f"回归结果：{regression_result}")

print("\nmatrix_multiply函数使用：")
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
multiply_result = matrix_multiply(matrix1, matrix2)
print(f"矩阵乘法结果：{multiply_result}")
print()

# 4. 类型提示和注释
print("\n4. 类型提示和注释")
print("-" * 30)

from typing import List, Dict, Optional, Union, Tuple, Callable

def typed_function(name: str, age: int, scores: List[float]) -> Dict[str, Union[str, int, float]]:
    """
    带类型提示的函数。
    
    Args:
        name: 学生姓名
        age: 学生年龄
        scores: 成绩列表
        
    Returns:
        包含学生信息和统计数据的字典
    """
    return {
        "name": name,
        "age": age,
        "average_score": sum(scores) / len(scores) if scores else 0,
        "max_score": max(scores) if scores else 0,
        "min_score": min(scores) if scores else 0
    }

def process_callback(data: List[int], 
                    callback: Callable[[int], int], 
                    filter_func: Optional[Callable[[int], bool]] = None) -> List[int]:
    """
    使用回调函数处理数据。
    
    Args:
        data: 要处理的整数列表
        callback: 处理每个元素的回调函数
        filter_func: 可选的过滤函数
        
    Returns:
        处理后的数据列表
    """
    # 应用过滤器（如果提供）
    if filter_func:
        data = [x for x in data if filter_func(x)]
    
    # 应用回调函数
    return [callback(x) for x in data]

def create_user_profile(user_id: int, 
                       personal_info: Dict[str, str],
                       preferences: Optional[Dict[str, bool]] = None) -> Tuple[bool, str, Dict]:
    """
    创建用户档案。
    
    Args:
        user_id: 用户ID
        personal_info: 个人信息字典
        preferences: 可选的用户偏好设置
        
    Returns:
        元组包含：(成功标志, 消息, 用户档案字典)
    """
    # 验证必需字段
    required_fields = {"name", "email"}
    if not required_fields.issubset(personal_info.keys()):
        missing = required_fields - personal_info.keys()
        return False, f"缺少必需字段：{missing}", {}
    
    # 创建档案
    profile = {
        "user_id": user_id,
        "personal_info": personal_info,
        "preferences": preferences or {"notifications": True, "theme": "light"},
        "created_at": "2024-01-01"  # 模拟时间戳
    }
    
    return True, "用户档案创建成功", profile

print("类型提示函数演示：")
student_info = typed_function("张三", 20, [85.5, 92.0, 78.5, 88.0])
print(f"学生信息：{student_info}")

print("\n回调函数处理：")
test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_evens = process_callback(test_data, 
                               lambda x: x ** 2,  # 平方
                               lambda x: x % 2 == 0)  # 只处理偶数
print(f"偶数平方：{squared_evens}")

print("\n用户档案创建：")
success, message, profile = create_user_profile(
    123,
    {"name": "李四", "email": "lisi@example.com", "phone": "13800138000"},
    {"notifications": False, "theme": "dark"}
)
print(f"创建结果：{success}, {message}")
if success:
    print(f"用户档案：{profile}")
print()

# 5. 文档生成和内省
print("\n5. 文档生成和内省")
print("-" * 30)

import inspect

def documented_function(param1: str, param2: int = 10, *args, **kwargs) -> str:
    """
    这是一个完整文档的示例函数。
    
    Args:
        param1: 第一个参数（字符串）
        param2: 第二个参数（整数，默认为10）
        *args: 可变位置参数
        **kwargs: 可变关键字参数
        
    Returns:
        格式化的字符串结果
        
    Example:
        >>> documented_function("hello", 20, "extra", option=True)
        'hello-20-extra-option:True'
    """
    result_parts = [param1, str(param2)]
    result_parts.extend(str(arg) for arg in args)
    result_parts.extend(f"{k}:{v}" for k, v in kwargs.items())
    return "-".join(result_parts)

def inspect_function(func):
    """
    检查函数的详细信息。
    
    Args:
        func: 要检查的函数
    """
    print(f"函数名：{func.__name__}")
    print(f"文档字符串：{func.__doc__}")
    
    # 获取函数签名
    sig = inspect.signature(func)
    print(f"函数签名：{sig}")
    
    # 获取参数信息
    print("参数详情：")
    for param_name, param in sig.parameters.items():
        print(f"  {param_name}:")
        print(f"    类型：{param.annotation if param.annotation != param.empty else '未指定'}")
        print(f"    默认值：{param.default if param.default != param.empty else '无'}")
        print(f"    参数类型：{param.kind}")
    
    # 返回类型
    return_annotation = sig.return_annotation
    if return_annotation != sig.empty:
        print(f"返回类型：{return_annotation}")
    
    # 源代码（如果可用）
    try:
        source_lines = inspect.getsourcelines(func)
        print(f"源代码行数：{len(source_lines[0])}")
        print(f"起始行号：{source_lines[1]}")
    except OSError:
        print("无法获取源代码")

print("函数内省演示：")
inspect_function(documented_function)

print("\n函数调用示例：")
result = documented_function("hello", 20, "extra", "more", option=True, flag=False)
print(f"调用结果：{result}")
print()

# 6. 最佳实践示例
print("\n6. 文档最佳实践")
print("-" * 30)

class Calculator:
    """
    简单计算器类。
    
    这个类提供基本的数学运算功能，包括加法、减法、乘法和除法。
    所有操作都会记录在历史记录中。
    
    Attributes:
        history (List[str]): 操作历史记录
        
    Example:
        >>> calc = Calculator()
        >>> result = calc.add(5, 3)
        >>> print(result)
        8
        >>> print(calc.get_history())
        ['5 + 3 = 8']
    """
    
    def __init__(self):
        """初始化计算器。"""
        self.history: List[str] = []
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        执行加法运算。
        
        Args:
            a: 第一个数字
            b: 第二个数字
            
        Returns:
            两数之和
            
        Example:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        执行除法运算。
        
        Args:
            a: 被除数
            b: 除数
            
        Returns:
            除法结果
            
        Raises:
            ZeroDivisionError: 当除数为0时
            
        Example:
            >>> calc = Calculator()
            >>> calc.divide(10, 2)
            5.0
        """
        if b == 0:
            raise ZeroDivisionError("除数不能为0")
        
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self) -> List[str]:
        """
        获取操作历史记录。
        
        Returns:
            历史记录列表的副本
        """
        return self.history.copy()
    
    def clear_history(self) -> None:
        """
        清空操作历史记录。
        
        Note:
            此操作不可逆，请谨慎使用。
        """
        self.history.clear()

def validate_email(email: str) -> Tuple[bool, str]:
    """
    验证电子邮件地址格式。
    
    这个函数执行基本的电子邮件格式验证，检查是否包含@符号
    和域名部分。注意这不是完整的RFC标准验证。
    
    Args:
        email: 要验证的电子邮件地址
        
    Returns:
        元组包含：
        - bool: 验证是否通过
        - str: 验证消息
        
    Raises:
        TypeError: 当输入不是字符串时
        
    Example:
        >>> validate_email("user@example.com")
        (True, '电子邮件格式有效')
        
        >>> validate_email("invalid-email")
        (False, '缺少@符号')
        
    Note:
        这是一个简化的验证函数，生产环境中应使用更严格的验证。
        
    See Also:
        - RFC 5322: Internet Message Format
        - Python email.utils module
    """
    if not isinstance(email, str):
        raise TypeError("电子邮件必须是字符串类型")
    
    if not email:
        return False, "电子邮件不能为空"
    
    if "@" not in email:
        return False, "缺少@符号"
    
    parts = email.split("@")
    if len(parts) != 2:
        return False, "@符号数量不正确"
    
    local, domain = parts
    if not local or not domain:
        return False, "本地部分或域名部分为空"
    
    if "." not in domain:
        return False, "域名缺少点号"
    
    return True, "电子邮件格式有效"

print("最佳实践演示：")
print("计算器类使用：")
calc = Calculator()
print(f"加法：{calc.add(10, 5)}")
print(f"除法：{calc.divide(20, 4)}")
print(f"历史记录：{calc.get_history()}")

print("\n电子邮件验证：")
test_emails = ["user@example.com", "invalid-email", "test@domain.co.uk", ""]
for email in test_emails:
    try:
        is_valid, message = validate_email(email)
        print(f"{email}: {is_valid} - {message}")
    except TypeError as e:
        print(f"{email}: 错误 - {e}")

print("\n查看Calculator类文档：")
help(Calculator.add)
print()

# 7. 文档字符串的访问和使用
print("\n7. 文档字符串的访问和使用")
print("-" * 30)

def get_function_info(func):
    """
    获取函数的文档信息。
    
    Args:
        func: 要分析的函数
        
    Returns:
        包含函数信息的字典
    """
    info = {
        "name": func.__name__,
        "doc": func.__doc__,
        "module": func.__module__,
        "annotations": getattr(func, '__annotations__', {})
    }
    
    # 获取参数信息
    try:
        sig = inspect.signature(func)
        info["parameters"] = {
            name: {
                "annotation": param.annotation if param.annotation != param.empty else None,
                "default": param.default if param.default != param.empty else None
            }
            for name, param in sig.parameters.items()
        }
        info["return_annotation"] = sig.return_annotation if sig.return_annotation != sig.empty else None
    except (ValueError, TypeError):
        info["parameters"] = {}
        info["return_annotation"] = None
    
    return info

print("函数信息分析：")
functions_to_analyze = [calculate_area, process_data, validate_email]

for func in functions_to_analyze:
    print(f"\n分析函数：{func.__name__}")
    info = get_function_info(func)
    print(f"模块：{info['module']}")
    print(f"文档长度：{len(info['doc']) if info['doc'] else 0} 字符")
    print(f"参数数量：{len(info['parameters'])}")
    print(f"返回类型注释：{info['return_annotation']}")
    
    if info['doc']:
        # 显示文档的前100个字符
        doc_preview = info['doc'][:100].replace('\n', ' ').strip()
        print(f"文档预览：{doc_preview}...")

print("\n=" * 50)
print("函数文档和注释学习完成！")
print("=" * 50)
print("\n总结：")
print("1. 文档字符串是函数的第一个字符串字面量")
print("2. 使用三重引号创建多行文档字符串")
print("3. Google、NumPy等风格提供了标准化的文档格式")
print("4. 类型提示增强了代码的可读性和IDE支持")
print("5. help()函数和__doc__属性可以访问文档")
print("6. inspect模块提供了强大的内省功能")
print("7. 良好的文档是代码维护的关键")
print("8. 文档应该说明函数的目的、参数、返回值和异常")