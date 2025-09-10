# 辅助模块：calculator.py

## 模块概述

`calculator.py` 是一个功能完整的计算器模块，演示了复杂模块的设计和实现。该模块包含了自定义异常类、完整的计算器类、模块级函数以及全面的测试代码，展示了Python模块开发的最佳实践。

## 模块结构

### 模块信息和常量

```python
"""计算器模块 - 提供完整的计算功能。

这个模块包含了一个功能完整的计算器类，支持基本运算、
高级运算、内存功能、历史记录等特性。

Example:
    基本使用：
        from calculator import Calculator
        calc = Calculator()
        result = calc.add(10, 5)
        print(f"结果: {result}")

Author: Python学习者
Version: 2.0.0
Date: 2024
"""

# 模块常量
VERSION = "2.0.0"
AUTHOR = "Python学习者"
DEFAULT_PRECISION = 10
MAX_HISTORY_SIZE = 100

# 数学常量
PI = 3.141592653589793
E = 2.718281828459045

# 模块变量
calculator_instances = []
last_result = None
```

### 自定义异常类

```python
class CalculatorError(Exception):
    """计算器基础异常类。
    
    所有计算器相关异常的基类。
    
    Attributes:
        message (str): 错误消息
        error_code (int): 错误代码
    """
    
    def __init__(self, message, error_code=None):
        """初始化异常。
        
        Args:
            message (str): 错误消息
            error_code (int, optional): 错误代码
        """
        super().__init__(message)
        self.message = message
        self.error_code = error_code
    
    def __str__(self):
        """返回异常的字符串表示。
        
        Returns:
            str: 异常信息
        """
        if self.error_code:
            return f"[错误 {self.error_code}] {self.message}"
        return self.message

class DivisionByZeroError(CalculatorError):
    """除零错误异常。
    
    当尝试除以零时抛出此异常。
    """
    
    def __init__(self, message="除数不能为零"):
        """初始化除零错误。
        
        Args:
            message (str): 错误消息
        """
        super().__init__(message, 1001)

class InvalidOperationError(CalculatorError):
    """无效操作异常。
    
    当执行无效操作时抛出此异常。
    """
    
    def __init__(self, message="无效的操作"):
        """初始化无效操作错误。
        
        Args:
            message (str): 错误消息
        """
        super().__init__(message, 1002)

class MemoryError(CalculatorError):
    """内存操作异常。
    
    当内存操作失败时抛出此异常。
    """
    
    def __init__(self, message="内存操作失败"):
        """初始化内存错误。
        
        Args:
            message (str): 错误消息
        """
        super().__init__(message, 1003)
```

### 计算器主类

```python
class Calculator:
    """功能完整的计算器类。
    
    提供基本运算、高级运算、内存功能、历史记录等特性。
    
    Attributes:
        precision (int): 计算精度
        memory (float): 内存中存储的值
        history (list): 计算历史记录
        last_result (float): 最后一次计算结果
        name (str): 计算器名称
    
    Example:
        >>> calc = Calculator("我的计算器")
        >>> result = calc.add(10, 5)
        >>> print(f"10 + 5 = {result}")
        10 + 5 = 15.0
    """
    
    def __init__(self, name="计算器", precision=None):
        """初始化计算器。
        
        Args:
            name (str): 计算器名称
            precision (int, optional): 计算精度，默认使用模块常量
        """
        self.name = name
        self.precision = precision or DEFAULT_PRECISION
        self.memory = 0.0
        self.history = []
        self.last_result = 0.0
        
        # 注册到全局实例列表
        calculator_instances.append(self)
        
        print(f"计算器 '{self.name}' 已创建，精度: {self.precision}")
    
    def _record_operation(self, operation, result):
        """记录操作到历史。
        
        Args:
            operation (str): 操作描述
            result (float): 操作结果
        """
        if len(self.history) >= MAX_HISTORY_SIZE:
            self.history.pop(0)  # 移除最旧的记录
        
        self.history.append({
            'operation': operation,
            'result': result,
            'timestamp': self._get_timestamp()
        })
        
        self.last_result = result
        global last_result
        last_result = result
    
    def _get_timestamp(self):
        """获取当前时间戳。
        
        Returns:
            str: 格式化的时间戳
        """
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def _round_result(self, value):
        """根据精度四舍五入结果。
        
        Args:
            value (float): 要四舍五入的值
        
        Returns:
            float: 四舍五入后的值
        """
        return round(value, self.precision)
    
    # 基本运算方法
    def add(self, a, b):
        """加法运算。
        
        Args:
            a (float): 第一个加数
            b (float): 第二个加数
        
        Returns:
            float: 加法结果
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(10, 5)
            15.0
        """
        result = self._round_result(a + b)
        self._record_operation(f"{a} + {b}", result)
        return result
    
    def subtract(self, a, b):
        """减法运算。
        
        Args:
            a (float): 被减数
            b (float): 减数
        
        Returns:
            float: 减法结果
        """
        result = self._round_result(a - b)
        self._record_operation(f"{a} - {b}", result)
        return result
    
    def multiply(self, a, b):
        """乘法运算。
        
        Args:
            a (float): 第一个乘数
            b (float): 第二个乘数
        
        Returns:
            float: 乘法结果
        """
        result = self._round_result(a * b)
        self._record_operation(f"{a} × {b}", result)
        return result
    
    def divide(self, a, b):
        """除法运算。
        
        Args:
            a (float): 被除数
            b (float): 除数
        
        Returns:
            float: 除法结果
        
        Raises:
            DivisionByZeroError: 当除数为零时
        
        Example:
            >>> calc = Calculator()
            >>> calc.divide(10, 2)
            5.0
            >>> calc.divide(10, 0)  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            DivisionByZeroError: 除数不能为零
        """
        if b == 0:
            raise DivisionByZeroError()
        
        result = self._round_result(a / b)
        self._record_operation(f"{a} ÷ {b}", result)
        return result
    
    # 高级运算方法
    def power(self, base, exponent):
        """幂运算。
        
        Args:
            base (float): 底数
            exponent (float): 指数
        
        Returns:
            float: 幂运算结果
        
        Example:
            >>> calc = Calculator()
            >>> calc.power(2, 3)
            8.0
        """
        result = self._round_result(base ** exponent)
        self._record_operation(f"{base} ^ {exponent}", result)
        return result
    
    def square_root(self, number):
        """平方根运算。
        
        Args:
            number (float): 要开方的数
        
        Returns:
            float: 平方根结果
        
        Raises:
            InvalidOperationError: 当数字为负数时
        """
        if number < 0:
            raise InvalidOperationError("不能对负数开平方根")
        
        result = self._round_result(number ** 0.5)
        self._record_operation(f"√{number}", result)
        return result
    
    def factorial(self, n):
        """阶乘运算。
        
        Args:
            n (int): 要计算阶乘的非负整数
        
        Returns:
            int: 阶乘结果
        
        Raises:
            InvalidOperationError: 当n为负数或非整数时
        """
        if not isinstance(n, int) or n < 0:
            raise InvalidOperationError("阶乘只能计算非负整数")
        
        if n <= 1:
            result = 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
        
        self._record_operation(f"{n}!", result)
        return result
    
    def percentage(self, number, percent):
        """百分比计算。
        
        Args:
            number (float): 基数
            percent (float): 百分比
        
        Returns:
            float: 百分比结果
        
        Example:
            >>> calc = Calculator()
            >>> calc.percentage(200, 15)  # 200的15%
            30.0
        """
        result = self._round_result(number * percent / 100)
        self._record_operation(f"{number}的{percent}%", result)
        return result
    
    # 批量运算方法
    def sum_list(self, numbers):
        """计算数字列表的和。
        
        Args:
            numbers (list): 数字列表
        
        Returns:
            float: 列表元素的和
        
        Example:
            >>> calc = Calculator()
            >>> calc.sum_list([1, 2, 3, 4, 5])
            15.0
        """
        if not numbers:
            return 0.0
        
        result = self._round_result(sum(numbers))
        self._record_operation(f"sum({numbers})", result)
        return result
    
    def average(self, numbers):
        """计算数字列表的平均值。
        
        Args:
            numbers (list): 数字列表
        
        Returns:
            float: 平均值
        
        Raises:
            InvalidOperationError: 当列表为空时
        """
        if not numbers:
            raise InvalidOperationError("不能计算空列表的平均值")
        
        result = self._round_result(sum(numbers) / len(numbers))
        self._record_operation(f"avg({numbers})", result)
        return result
    
    # 内存功能
    def memory_store(self, value):
        """将值存储到内存。
        
        Args:
            value (float): 要存储的值
        
        Example:
            >>> calc = Calculator()
            >>> calc.memory_store(42)
            >>> calc.memory_recall()
            42.0
        """
        self.memory = value
        self._record_operation(f"M+ {value}", value)
        print(f"已将 {value} 存储到内存")
    
    def memory_recall(self):
        """从内存中取出值。
        
        Returns:
            float: 内存中的值
        """
        self._record_operation("MR", self.memory)
        return self.memory
    
    def memory_clear(self):
        """清空内存。
        
        Example:
            >>> calc = Calculator()
            >>> calc.memory_store(42)
            >>> calc.memory_clear()
            >>> calc.memory_recall()
            0.0
        """
        self.memory = 0.0
        self._record_operation("MC", 0.0)
        print("内存已清空")
    
    def memory_add(self, value):
        """将值加到内存中。
        
        Args:
            value (float): 要加到内存的值
        
        Returns:
            float: 更新后的内存值
        """
        self.memory += value
        self._record_operation(f"M+ {value}", self.memory)
        return self.memory
    
    # 历史记录功能
    def get_history(self, count=None):
        """获取计算历史。
        
        Args:
            count (int, optional): 获取的记录数量，默认全部
        
        Returns:
            list: 历史记录列表
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3.0
            >>> history = calc.get_history()
            >>> len(history)
            1
        """
        if count is None:
            return self.history.copy()
        return self.history[-count:] if count > 0 else []
    
    def clear_history(self):
        """清空计算历史。
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3.0
            >>> calc.clear_history()
            >>> len(calc.get_history())
            0
        """
        self.history.clear()
        print("计算历史已清空")
    
    def print_history(self, count=10):
        """打印计算历史。
        
        Args:
            count (int): 打印的记录数量，默认10条
        """
        recent_history = self.get_history(count)
        
        if not recent_history:
            print("暂无计算历史")
            return
        
        print(f"\n=== {self.name} 计算历史 (最近{len(recent_history)}条) ===")
        for i, record in enumerate(recent_history, 1):
            print(f"{i:2d}. {record['timestamp']} | {record['operation']} = {record['result']}")
        print()
    
    # 工具方法
    def reset(self):
        """重置计算器。
        
        清空历史记录、内存和最后结果。
        """
        self.history.clear()
        self.memory = 0.0
        self.last_result = 0.0
        print(f"计算器 '{self.name}' 已重置")
    
    def get_info(self):
        """获取计算器信息。
        
        Returns:
            dict: 计算器信息字典
        """
        return {
            'name': self.name,
            'precision': self.precision,
            'memory': self.memory,
            'last_result': self.last_result,
            'history_count': len(self.history),
            'version': VERSION
        }
    
    def __str__(self):
        """返回计算器的字符串表示。
        
        Returns:
            str: 计算器信息
        """
        return f"Calculator(name='{self.name}', precision={self.precision}, memory={self.memory})"
    
    def __repr__(self):
        """返回计算器的详细表示。
        
        Returns:
            str: 计算器详细信息
        """
        return (f"Calculator(name='{self.name}', precision={self.precision}, "
                f"memory={self.memory}, history_count={len(self.history)})")
```

### 模块级函数

```python
def quick_calculate(expression):
    """快速计算简单表达式。
    
    Args:
        expression (str): 数学表达式字符串
    
    Returns:
        float: 计算结果
    
    Raises:
        InvalidOperationError: 当表达式无效时
    
    Example:
        >>> quick_calculate("2 + 3 * 4")
        14.0
        >>> quick_calculate("10 / 2")
        5.0
    
    Warning:
        此函数使用eval()，在生产环境中请谨慎使用。
    """
    try:
        # 安全检查：只允许数字、运算符和括号
        allowed_chars = set('0123456789+-*/().() ')
        if not all(c in allowed_chars for c in expression):
            raise InvalidOperationError("表达式包含不允许的字符")
        
        result = eval(expression)
        
        # 记录到全局变量
        global last_result
        last_result = result
        
        return float(result)
    
    except ZeroDivisionError:
        raise DivisionByZeroError()
    except Exception as e:
        raise InvalidOperationError(f"无效的表达式: {expression}")

def create_calculator(name=None, precision=None):
    """创建新的计算器实例。
    
    Args:
        name (str, optional): 计算器名称
        precision (int, optional): 计算精度
    
    Returns:
        Calculator: 新的计算器实例
    
    Example:
        >>> calc = create_calculator("测试计算器", 5)
        >>> calc.name
        '测试计算器'
        >>> calc.precision
        5
    """
    if name is None:
        name = f"计算器_{len(calculator_instances) + 1}"
    
    return Calculator(name, precision)

def get_all_calculators():
    """获取所有计算器实例。
    
    Returns:
        list: 所有计算器实例的列表
    
    Example:
        >>> calc1 = create_calculator("计算器1")
        >>> calc2 = create_calculator("计算器2")
        >>> calculators = get_all_calculators()
        >>> len(calculators) >= 2
        True
    """
    return calculator_instances.copy()

def clear_all_calculators():
    """清空所有计算器实例。
    
    Warning:
        此操作将清空全局计算器实例列表。
    """
    global calculator_instances
    calculator_instances.clear()
    print("所有计算器实例已清空")

def get_module_info():
    """获取模块信息。
    
    Returns:
        dict: 模块信息字典
    """
    return {
        'name': __name__,
        'version': VERSION,
        'author': AUTHOR,
        'calculator_count': len(calculator_instances),
        'last_result': last_result,
        'constants': {
            'PI': PI,
            'E': E,
            'DEFAULT_PRECISION': DEFAULT_PRECISION,
            'MAX_HISTORY_SIZE': MAX_HISTORY_SIZE
        }
    }
```

## 模块测试代码

### 完整的测试示例

```python
if __name__ == '__main__':
    print("=== 计算器模块测试 ===")
    print(f"模块版本: {VERSION}")
    print(f"作者: {AUTHOR}")
    print()
    
    try:
        # 1. 基本运算测试
        print("1. 基本运算测试:")
        calc = Calculator("基本计算器")
        
        print(f"   10 + 5 = {calc.add(10, 5)}")
        print(f"   10 - 3 = {calc.subtract(10, 3)}")
        print(f"   4 * 6 = {calc.multiply(4, 6)}")
        print(f"   15 / 3 = {calc.divide(15, 3)}")
        print()
        
        # 2. 高级运算测试
        print("2. 高级运算测试:")
        print(f"   2^8 = {calc.power(2, 8)}")
        print(f"   √16 = {calc.square_root(16)}")
        print(f"   5! = {calc.factorial(5)}")
        print(f"   200的15% = {calc.percentage(200, 15)}")
        print()
        
        # 3. 批量运算测试
        print("3. 批量运算测试:")
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(f"   数字列表: {numbers}")
        print(f"   求和: {calc.sum_list(numbers)}")
        print(f"   平均值: {calc.average(numbers)}")
        print()
        
        # 4. 内存功能测试
        print("4. 内存功能测试:")
        calc.memory_store(42)
        print(f"   内存回调: {calc.memory_recall()}")
        calc.memory_add(8)
        print(f"   内存+8后: {calc.memory_recall()}")
        calc.memory_clear()
        print(f"   清空内存后: {calc.memory_recall()}")
        print()
        
        # 5. 历史记录测试
        print("5. 历史记录测试:")
        calc.add(100, 200)
        calc.multiply(5, 6)
        calc.divide(50, 2)
        calc.print_history(5)
        
        # 6. 异常处理测试
        print("6. 异常处理测试:")
        try:
            calc.divide(10, 0)
        except DivisionByZeroError as e:
            print(f"   捕获除零异常: {e}")
        
        try:
            calc.square_root(-4)
        except InvalidOperationError as e:
            print(f"   捕获无效操作异常: {e}")
        
        try:
            calc.factorial(-1)
        except InvalidOperationError as e:
            print(f"   捕获阶乘异常: {e}")
        print()
        
        # 7. 快速计算测试
        print("7. 快速计算测试:")
        expressions = ["2 + 3 * 4", "(10 + 5) / 3", "2 ** 3 + 1"]
        for expr in expressions:
            try:
                result = quick_calculate(expr)
                print(f"   {expr} = {result}")
            except Exception as e:
                print(f"   {expr} -> 错误: {e}")
        print()
        
        # 8. 多计算器实例测试
        print("8. 多计算器实例测试:")
        calc2 = create_calculator("科学计算器", 5)
        calc3 = create_calculator("简单计算器", 2)
        
        calc2.add(1.23456789, 2.87654321)
        calc3.add(1.23456789, 2.87654321)
        
        print(f"   高精度计算器结果: {calc2.last_result}")
        print(f"   低精度计算器结果: {calc3.last_result}")
        print()
        
        # 9. 模块信息测试
        print("9. 模块信息:")
        info = get_module_info()
        print(f"   模块名: {info['name']}")
        print(f"   版本: {info['version']}")
        print(f"   作者: {info['author']}")
        print(f"   计算器实例数: {info['calculator_count']}")
        print(f"   最后结果: {info['last_result']}")
        print(f"   PI常量: {info['constants']['PI']}")
        print(f"   E常量: {info['constants']['E']}")
        print()
        
        # 10. 所有计算器实例
        print("10. 所有计算器实例:")
        all_calcs = get_all_calculators()
        for i, c in enumerate(all_calcs, 1):
            print(f"    {i}. {c}")
        
    except Exception as e:
        print(f"测试过程中发生错误: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n=== 测试完成 ===")
```

## 使用示例

### 基本使用

```python
# 导入模块
from calculator import Calculator, quick_calculate

# 创建计算器实例
calc = Calculator("我的计算器")

# 基本运算
result1 = calc.add(10, 5)
result2 = calc.multiply(3, 4)
result3 = calc.divide(20, 4)

print(f"加法: {result1}")
print(f"乘法: {result2}")
print(f"除法: {result3}")

# 查看历史
calc.print_history()
```

### 高级功能使用

```python
from calculator import Calculator, create_calculator

# 创建高精度计算器
scientific_calc = create_calculator("科学计算器", precision=15)

# 高级运算
power_result = scientific_calc.power(2, 10)
sqrt_result = scientific_calc.square_root(144)
fact_result = scientific_calc.factorial(6)

# 内存操作
scientific_calc.memory_store(power_result)
scientific_calc.memory_add(sqrt_result)
memory_value = scientific_calc.memory_recall()

print(f"内存中的值: {memory_value}")

# 批量计算
numbers = [1, 4, 9, 16, 25]
avg_result = scientific_calc.average(numbers)
sum_result = scientific_calc.sum_list(numbers)

print(f"平均值: {avg_result}")
print(f"总和: {sum_result}")
```

### 异常处理

```python
from calculator import Calculator, DivisionByZeroError, InvalidOperationError

calc = Calculator("安全计算器")

try:
    # 可能引发异常的操作
    result = calc.divide(10, 0)
except DivisionByZeroError as e:
    print(f"除零错误: {e}")

try:
    result = calc.square_root(-1)
except InvalidOperationError as e:
    print(f"无效操作: {e}")
```

## 学习要点

1. **模块设计**：如何设计一个功能完整的模块
2. **异常处理**：自定义异常类的设计和使用
3. **类的设计**：复杂类的结构和方法组织
4. **模块变量**：全局变量的使用和管理
5. **文档编写**：完整的文档字符串编写
6. **测试代码**：全面的模块测试策略
7. **最佳实践**：Python模块开发的最佳实践

## 扩展练习

1. **添加三角函数**：为计算器添加sin、cos、tan等函数
2. **表达式解析**：改进quick_calculate函数，支持更复杂的表达式
3. **数据持久化**：添加保存和加载计算历史的功能
4. **图形界面**：为计算器创建GUI界面
5. **单位转换**：添加长度、重量、温度等单位转换功能
6. **科学记数法**：支持科学记数法的输入和输出
7. **插件系统**：设计插件架构，允许扩展新功能

这个calculator模块展示了如何创建一个功能完整、结构良好的Python模块，包含了异常处理、类设计、文档编写等多个重要概念，是学习Python模块开发的优秀示例。