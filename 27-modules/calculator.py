#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
计算器模块 - 用于演示模块的类和高级功能

这个模块包含一个完整的计算器类，演示了面向对象编程
在模块中的应用，以及模块的高级特性。

Author: Python学习者
Version: 2.0.0
Date: 2024
"""

import math
import operator
from functools import reduce
from typing import List, Union, Optional

# 模块级别的常量
MODULE_NAME = "calculator"
MODULE_VERSION = "2.0.0"
MAX_HISTORY_SIZE = 100
DEFAULT_PRECISION = 2

# 模块级别的变量
_global_calculator_count = 0
_all_calculators = []

print(f"计算器模块 {MODULE_NAME} v{MODULE_VERSION} 已加载")

# ============================================================================
# 异常类定义
# ============================================================================

class CalculatorError(Exception):
    """
    计算器基础异常类
    """
    pass

class DivisionByZeroError(CalculatorError):
    """
    除零错误异常
    """
    def __init__(self, message="不能除以零"):
        self.message = message
        super().__init__(self.message)

class InvalidOperationError(CalculatorError):
    """
    无效操作异常
    """
    def __init__(self, operation, message=None):
        self.operation = operation
        self.message = message or f"无效的操作: {operation}"
        super().__init__(self.message)

# ============================================================================
# 计算器类定义
# ============================================================================

class Calculator:
    """
    高级计算器类
    
    提供基本的数学运算功能，包括历史记录、内存功能等。
    
    Attributes:
        precision (int): 计算精度
        history (list): 计算历史记录
        memory (float): 内存值
        name (str): 计算器名称
    
    Example:
        >>> calc = Calculator("我的计算器")
        >>> result = calc.add(5, 3)
        >>> print(result)
        8.0
    """
    
    def __init__(self, name: str = "默认计算器", precision: int = DEFAULT_PRECISION):
        """
        初始化计算器
        
        Args:
            name (str): 计算器名称
            precision (int): 计算精度（小数位数）
        """
        global _global_calculator_count, _all_calculators
        
        self.name = name
        self.precision = precision
        self.history = []
        self.memory = 0.0
        self.last_result = 0.0
        self.id = _global_calculator_count
        
        _global_calculator_count += 1
        _all_calculators.append(self)
        
        print(f"计算器 '{self.name}' (ID: {self.id}) 已创建")
    
    def __str__(self) -> str:
        """
        字符串表示
        """
        return f"Calculator(name='{self.name}', id={self.id}, precision={self.precision})"
    
    def __repr__(self) -> str:
        """
        详细字符串表示
        """
        return (f"Calculator(name='{self.name}', id={self.id}, "
                f"precision={self.precision}, memory={self.memory}, "
                f"history_count={len(self.history)})")
    
    def _record_operation(self, operation: str, operands: List[float], result: float) -> None:
        """
        记录操作到历史记录（私有方法）
        
        Args:
            operation (str): 操作名称
            operands (List[float]): 操作数列表
            result (float): 计算结果
        """
        if len(self.history) >= MAX_HISTORY_SIZE:
            self.history.pop(0)  # 移除最旧的记录
        
        record = {
            'operation': operation,
            'operands': operands.copy(),
            'result': result,
            'timestamp': self._get_timestamp()
        }
        self.history.append(record)
        self.last_result = result
    
    def _get_timestamp(self) -> str:
        """
        获取当前时间戳（私有方法）
        
        Returns:
            str: 格式化的时间戳
        """
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def _round_result(self, value: float) -> float:
        """
        根据精度设置四舍五入结果（私有方法）
        
        Args:
            value (float): 原始值
        
        Returns:
            float: 四舍五入后的值
        """
        return round(value, self.precision)
    
    # 基本运算方法
    def add(self, a: float, b: float) -> float:
        """
        加法运算
        
        Args:
            a (float): 第一个加数
            b (float): 第二个加数
        
        Returns:
            float: 和
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(3, 5)
            8.0
        """
        result = self._round_result(a + b)
        self._record_operation('add', [a, b], result)
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """
        减法运算
        
        Args:
            a (float): 被减数
            b (float): 减数
        
        Returns:
            float: 差
        
        Example:
            >>> calc = Calculator()
            >>> calc.subtract(10, 3)
            7.0
        """
        result = self._round_result(a - b)
        self._record_operation('subtract', [a, b], result)
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """
        乘法运算
        
        Args:
            a (float): 第一个因数
            b (float): 第二个因数
        
        Returns:
            float: 积
        
        Example:
            >>> calc = Calculator()
            >>> calc.multiply(4, 6)
            24.0
        """
        result = self._round_result(a * b)
        self._record_operation('multiply', [a, b], result)
        return result
    
    def divide(self, a: float, b: float) -> float:
        """
        除法运算
        
        Args:
            a (float): 被除数
            b (float): 除数
        
        Returns:
            float: 商
        
        Raises:
            DivisionByZeroError: 当除数为0时
        
        Example:
            >>> calc = Calculator()
            >>> calc.divide(15, 3)
            5.0
        """
        if b == 0:
            raise DivisionByZeroError(f"不能用 {a} 除以 0")
        
        result = self._round_result(a / b)
        self._record_operation('divide', [a, b], result)
        return result
    
    def power(self, base: float, exponent: float) -> float:
        """
        幂运算
        
        Args:
            base (float): 底数
            exponent (float): 指数
        
        Returns:
            float: 幂
        
        Example:
            >>> calc = Calculator()
            >>> calc.power(2, 3)
            8.0
        """
        result = self._round_result(base ** exponent)
        self._record_operation('power', [base, exponent], result)
        return result
    
    def sqrt(self, value: float) -> float:
        """
        平方根运算
        
        Args:
            value (float): 被开方数
        
        Returns:
            float: 平方根
        
        Raises:
            ValueError: 当值为负数时
        
        Example:
            >>> calc = Calculator()
            >>> calc.sqrt(16)
            4.0
        """
        if value < 0:
            raise ValueError(f"不能计算负数 {value} 的平方根")
        
        result = self._round_result(math.sqrt(value))
        self._record_operation('sqrt', [value], result)
        return result
    
    # 高级运算方法
    def factorial(self, n: int) -> int:
        """
        阶乘运算
        
        Args:
            n (int): 非负整数
        
        Returns:
            int: 阶乘结果
        
        Raises:
            ValueError: 当n为负数时
        
        Example:
            >>> calc = Calculator()
            >>> calc.factorial(5)
            120
        """
        if n < 0:
            raise ValueError(f"不能计算负数 {n} 的阶乘")
        
        result = math.factorial(n)
        self._record_operation('factorial', [n], result)
        return result
    
    def sin(self, angle: float, degrees: bool = False) -> float:
        """
        正弦函数
        
        Args:
            angle (float): 角度值
            degrees (bool): 是否为度数，默认为弧度
        
        Returns:
            float: 正弦值
        
        Example:
            >>> calc = Calculator()
            >>> calc.sin(90, degrees=True)
            1.0
        """
        if degrees:
            angle = math.radians(angle)
        
        result = self._round_result(math.sin(angle))
        self._record_operation('sin', [angle], result)
        return result
    
    def cos(self, angle: float, degrees: bool = False) -> float:
        """
        余弦函数
        
        Args:
            angle (float): 角度值
            degrees (bool): 是否为度数，默认为弧度
        
        Returns:
            float: 余弦值
        
        Example:
            >>> calc = Calculator()
            >>> calc.cos(0, degrees=True)
            1.0
        """
        if degrees:
            angle = math.radians(angle)
        
        result = self._round_result(math.cos(angle))
        self._record_operation('cos', [angle], result)
        return result
    
    def log(self, value: float, base: float = math.e) -> float:
        """
        对数函数
        
        Args:
            value (float): 真数
            base (float): 底数，默认为自然对数
        
        Returns:
            float: 对数值
        
        Raises:
            ValueError: 当值小于等于0或底数小于等于0或等于1时
        
        Example:
            >>> calc = Calculator()
            >>> calc.log(100, 10)
            2.0
        """
        if value <= 0:
            raise ValueError(f"对数的真数必须大于0，得到: {value}")
        if base <= 0 or base == 1:
            raise ValueError(f"对数的底数必须大于0且不等于1，得到: {base}")
        
        result = self._round_result(math.log(value, base))
        self._record_operation('log', [value, base], result)
        return result
    
    # 批量运算方法
    def sum_list(self, numbers: List[float]) -> float:
        """
        计算列表中所有数字的和
        
        Args:
            numbers (List[float]): 数字列表
        
        Returns:
            float: 总和
        
        Example:
            >>> calc = Calculator()
            >>> calc.sum_list([1, 2, 3, 4, 5])
            15.0
        """
        if not numbers:
            return 0.0
        
        result = self._round_result(sum(numbers))
        self._record_operation('sum_list', numbers, result)
        return result
    
    def average(self, numbers: List[float]) -> float:
        """
        计算列表中数字的平均值
        
        Args:
            numbers (List[float]): 数字列表
        
        Returns:
            float: 平均值
        
        Raises:
            ValueError: 当列表为空时
        
        Example:
            >>> calc = Calculator()
            >>> calc.average([1, 2, 3, 4, 5])
            3.0
        """
        if not numbers:
            raise ValueError("不能计算空列表的平均值")
        
        result = self._round_result(sum(numbers) / len(numbers))
        self._record_operation('average', numbers, result)
        return result
    
    def product(self, numbers: List[float]) -> float:
        """
        计算列表中所有数字的乘积
        
        Args:
            numbers (List[float]): 数字列表
        
        Returns:
            float: 乘积
        
        Example:
            >>> calc = Calculator()
            >>> calc.product([2, 3, 4])
            24.0
        """
        if not numbers:
            return 0.0
        
        result = self._round_result(reduce(operator.mul, numbers, 1))
        self._record_operation('product', numbers, result)
        return result
    
    # 内存功能
    def memory_store(self, value: float) -> None:
        """
        将值存储到内存
        
        Args:
            value (float): 要存储的值
        
        Example:
            >>> calc = Calculator()
            >>> calc.memory_store(42)
            >>> calc.memory_recall()
            42.0
        """
        self.memory = value
        print(f"已将 {value} 存储到内存")
    
    def memory_recall(self) -> float:
        """
        从内存中取出值
        
        Returns:
            float: 内存中的值
        
        Example:
            >>> calc = Calculator()
            >>> calc.memory_store(42)
            >>> calc.memory_recall()
            42.0
        """
        return self.memory
    
    def memory_clear(self) -> None:
        """
        清除内存
        
        Example:
            >>> calc = Calculator()
            >>> calc.memory_clear()
            >>> calc.memory_recall()
            0.0
        """
        self.memory = 0.0
        print("内存已清除")
    
    def memory_add(self, value: float) -> None:
        """
        将值加到内存中
        
        Args:
            value (float): 要加到内存的值
        
        Example:
            >>> calc = Calculator()
            >>> calc.memory_store(10)
            >>> calc.memory_add(5)
            >>> calc.memory_recall()
            15.0
        """
        self.memory += value
        print(f"已将 {value} 加到内存，当前内存值: {self.memory}")
    
    # 历史记录功能
    def get_history(self, count: Optional[int] = None) -> List[dict]:
        """
        获取历史记录
        
        Args:
            count (Optional[int]): 获取的记录数量，None表示全部
        
        Returns:
            List[dict]: 历史记录列表
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            >>> history = calc.get_history()
            >>> len(history)
            1
        """
        if count is None:
            return self.history.copy()
        return self.history[-count:] if count > 0 else []
    
    def clear_history(self) -> None:
        """
        清除历史记录
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            >>> calc.clear_history()
            >>> len(calc.get_history())
            0
        """
        self.history.clear()
        print("历史记录已清除")
    
    def print_history(self, count: Optional[int] = None) -> None:
        """
        打印历史记录
        
        Args:
            count (Optional[int]): 打印的记录数量，None表示全部
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            >>> calc.print_history()
        """
        history = self.get_history(count)
        if not history:
            print("没有历史记录")
            return
        
        print(f"\n=== {self.name} 历史记录 ===")
        for i, record in enumerate(history, 1):
            operands_str = ', '.join(map(str, record['operands']))
            print(f"{i:2d}. {record['operation']}({operands_str}) = {record['result']} [{record['timestamp']}]")
        print("=" * 40)
    
    # 设置和状态方法
    def set_precision(self, precision: int) -> None:
        """
        设置计算精度
        
        Args:
            precision (int): 小数位数
        
        Example:
            >>> calc = Calculator()
            >>> calc.set_precision(4)
        """
        if precision < 0:
            raise ValueError("精度必须是非负整数")
        
        old_precision = self.precision
        self.precision = precision
        print(f"精度已从 {old_precision} 位更改为 {precision} 位")
    
    def get_last_result(self) -> float:
        """
        获取最后一次计算的结果
        
        Returns:
            float: 最后一次计算的结果
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            >>> calc.get_last_result()
            3.0
        """
        return self.last_result
    
    def get_info(self) -> dict:
        """
        获取计算器信息
        
        Returns:
            dict: 包含计算器信息的字典
        
        Example:
            >>> calc = Calculator()
            >>> info = calc.get_info()
            >>> 'name' in info
            True
        """
        return {
            'name': self.name,
            'id': self.id,
            'precision': self.precision,
            'memory': self.memory,
            'last_result': self.last_result,
            'history_count': len(self.history),
            'max_history_size': MAX_HISTORY_SIZE
        }
    
    def reset(self) -> None:
        """
        重置计算器（清除历史记录和内存）
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            >>> calc.memory_store(10)
            >>> calc.reset()
            >>> calc.memory_recall()
            0.0
        """
        self.history.clear()
        self.memory = 0.0
        self.last_result = 0.0
        print(f"计算器 '{self.name}' 已重置")

# ============================================================================
# 模块级别的函数
# ============================================================================

def get_all_calculators() -> List[Calculator]:
    """
    获取所有创建的计算器实例
    
    Returns:
        List[Calculator]: 所有计算器实例的列表
    
    Example:
        >>> calc1 = Calculator("计算器1")
        >>> calc2 = Calculator("计算器2")
        >>> all_calcs = get_all_calculators()
        >>> len(all_calcs)
        2
    """
    return _all_calculators.copy()

def get_calculator_count() -> int:
    """
    获取已创建的计算器总数
    
    Returns:
        int: 计算器总数
    
    Example:
        >>> count_before = get_calculator_count()
        >>> calc = Calculator()
        >>> get_calculator_count() == count_before + 1
        True
    """
    return _global_calculator_count

def find_calculator_by_name(name: str) -> Optional[Calculator]:
    """
    根据名称查找计算器
    
    Args:
        name (str): 计算器名称
    
    Returns:
        Optional[Calculator]: 找到的计算器实例，如果没找到则返回None
    
    Example:
        >>> calc = Calculator("我的计算器")
        >>> found = find_calculator_by_name("我的计算器")
        >>> found is not None
        True
    """
    for calc in _all_calculators:
        if calc.name == name:
            return calc
    return None

def create_calculator(name: str = None, precision: int = DEFAULT_PRECISION) -> Calculator:
    """
    创建新的计算器实例的工厂函数
    
    Args:
        name (str, optional): 计算器名称
        precision (int): 计算精度
    
    Returns:
        Calculator: 新的计算器实例
    
    Example:
        >>> calc = create_calculator("高精度计算器", 4)
        >>> calc.precision
        4
    """
    if name is None:
        name = f"计算器_{_global_calculator_count + 1}"
    
    return Calculator(name, precision)

def quick_calculate(operation: str, *args) -> float:
    """
    快速计算函数（不创建计算器实例）
    
    Args:
        operation (str): 操作名称
        *args: 操作参数
    
    Returns:
        float: 计算结果
    
    Raises:
        InvalidOperationError: 当操作无效时
    
    Example:
        >>> quick_calculate('add', 3, 5)
        8.0
        >>> quick_calculate('multiply', 4, 6)
        24.0
    """
    temp_calc = Calculator("临时计算器")
    
    operations = {
        'add': temp_calc.add,
        'subtract': temp_calc.subtract,
        'multiply': temp_calc.multiply,
        'divide': temp_calc.divide,
        'power': temp_calc.power,
        'sqrt': temp_calc.sqrt
    }
    
    if operation not in operations:
        raise InvalidOperationError(operation)
    
    try:
        return operations[operation](*args)
    except TypeError as e:
        raise InvalidOperationError(operation, f"参数错误: {e}")

def get_module_info() -> dict:
    """
    获取模块信息
    
    Returns:
        dict: 包含模块信息的字典
    
    Example:
        >>> info = get_module_info()
        >>> info['name']
        'calculator'
    """
    return {
        'name': MODULE_NAME,
        'version': MODULE_VERSION,
        'calculator_count': _global_calculator_count,
        'max_history_size': MAX_HISTORY_SIZE,
        'default_precision': DEFAULT_PRECISION,
        'available_operations': [
            'add', 'subtract', 'multiply', 'divide', 'power', 'sqrt',
            'factorial', 'sin', 'cos', 'log', 'sum_list', 'average', 'product'
        ],
        'exception_classes': ['CalculatorError', 'DivisionByZeroError', 'InvalidOperationError']
    }

def print_module_info() -> None:
    """
    打印模块信息
    
    Example:
        >>> print_module_info()
    """
    info = get_module_info()
    print(f"\n=== {info['name']} 模块信息 ===")
    print(f"版本: {info['version']}")
    print(f"已创建计算器数量: {info['calculator_count']}")
    print(f"最大历史记录数: {info['max_history_size']}")
    print(f"默认精度: {info['default_precision']}")
    print(f"可用操作: {', '.join(info['available_operations'])}")
    print(f"异常类: {', '.join(info['exception_classes'])}")
    print("=" * 40)

# ============================================================================
# 模块级别的测试代码
# ============================================================================

if __name__ == '__main__':
    print("\n=== 计算器模块测试 ===")
    
    # 创建计算器实例
    print("\n1. 创建计算器实例：")
    calc1 = Calculator("基础计算器")
    calc2 = Calculator("高精度计算器", precision=4)
    
    # 测试基本运算
    print("\n2. 基本运算测试：")
    print(f"加法: {calc1.add(10, 5)}")
    print(f"减法: {calc1.subtract(10, 3)}")
    print(f"乘法: {calc1.multiply(4, 6)}")
    print(f"除法: {calc1.divide(15, 3)}")
    print(f"幂运算: {calc1.power(2, 3)}")
    print(f"平方根: {calc1.sqrt(16)}")
    
    # 测试高级运算
    print("\n3. 高级运算测试：")
    print(f"阶乘: {calc1.factorial(5)}")
    print(f"正弦: {calc1.sin(90, degrees=True)}")
    print(f"余弦: {calc1.cos(0, degrees=True)}")
    print(f"对数: {calc1.log(100, 10)}")
    
    # 测试批量运算
    print("\n4. 批量运算测试：")
    numbers = [1, 2, 3, 4, 5]
    print(f"列表 {numbers}:")
    print(f"  求和: {calc1.sum_list(numbers)}")
    print(f"  平均值: {calc1.average(numbers)}")
    print(f"  乘积: {calc1.product(numbers)}")
    
    # 测试内存功能
    print("\n5. 内存功能测试：")
    calc1.memory_store(42)
    print(f"内存回调: {calc1.memory_recall()}")
    calc1.memory_add(8)
    print(f"内存回调: {calc1.memory_recall()}")
    
    # 测试历史记录
    print("\n6. 历史记录测试：")
    calc1.print_history(5)
    
    # 测试异常处理
    print("\n7. 异常处理测试：")
    try:
        calc1.divide(10, 0)
    except DivisionByZeroError as e:
        print(f"捕获除零异常: {e}")
    
    try:
        calc1.sqrt(-4)
    except ValueError as e:
        print(f"捕获值错误: {e}")
    
    # 测试快速计算
    print("\n8. 快速计算测试：")
    print(f"快速加法: {quick_calculate('add', 7, 3)}")
    print(f"快速乘法: {quick_calculate('multiply', 6, 7)}")
    
    # 显示模块信息
    print("\n9. 模块信息：")
    print_module_info()
    
    # 显示所有计算器
    print("\n10. 所有计算器：")
    all_calcs = get_all_calculators()
    for calc in all_calcs:
        print(f"  {calc}")
    
    print("\n=== 测试完成 ===")