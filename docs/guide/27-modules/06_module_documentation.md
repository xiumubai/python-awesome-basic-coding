# 06. 模块文档和帮助系统

## 学习目标

- 掌握Python文档字符串的编写规范
- 学会使用help()函数获取帮助信息
- 了解__doc__属性的作用和使用
- 掌握模块、函数、类的文档编写标准
- 学会使用文档生成工具
- 理解文档的最佳实践

## 文档字符串基础

### 什么是文档字符串

文档字符串（docstring）是Python中用于描述模块、函数、类或方法功能的字符串。它们是Python代码自文档化的重要组成部分。

```python
def example_function():
    """这是一个示例函数的文档字符串。
    
    文档字符串应该简洁地描述函数的功能。
    """
    pass
```

### 文档字符串的位置

```python
# 模块级文档字符串
"""这是模块的文档字符串。

描述模块的用途、功能和使用方法。
"""

def function_example():
    """函数的文档字符串。"""
    pass

class ClassExample:
    """类的文档字符串。"""
    
    def method_example(self):
        """方法的文档字符串。"""
        pass
```

## 文档字符串编写规范

### PEP 257规范

PEP 257定义了文档字符串的约定：

```python
def calculate_area(length, width):
    """计算矩形面积。
    
    Args:
        length (float): 矩形的长度
        width (float): 矩形的宽度
    
    Returns:
        float: 矩形的面积
    
    Raises:
        ValueError: 当长度或宽度为负数时
    
    Example:
        >>> calculate_area(5, 3)
        15.0
    """
    if length < 0 or width < 0:
        raise ValueError("长度和宽度必须为非负数")
    return length * width
```

### Google风格文档字符串

```python
def process_data(data, method='default', **kwargs):
    """处理输入数据。
    
    这个函数根据指定的方法处理输入数据，支持多种处理选项。
    
    Args:
        data (list): 要处理的数据列表
        method (str, optional): 处理方法。默认为'default'。
            可选值：'default', 'advanced', 'custom'
        **kwargs: 额外的处理参数
            - threshold (float): 阈值参数
            - normalize (bool): 是否标准化
    
    Returns:
        dict: 处理结果，包含以下键：
            - 'processed_data': 处理后的数据
            - 'metadata': 处理元数据
            - 'status': 处理状态
    
    Raises:
        TypeError: 当data不是列表时
        ValueError: 当method不被支持时
    
    Example:
        基本使用：
        >>> data = [1, 2, 3, 4, 5]
        >>> result = process_data(data)
        >>> result['status']
        'success'
        
        高级使用：
        >>> result = process_data(data, method='advanced', threshold=0.5)
        >>> len(result['processed_data'])
        5
    
    Note:
        这个函数会修改全局状态，请谨慎使用。
    
    Todo:
        * 添加更多处理方法
        * 优化性能
        * 添加并行处理支持
    """
    if not isinstance(data, list):
        raise TypeError("data必须是列表类型")
    
    valid_methods = ['default', 'advanced', 'custom']
    if method not in valid_methods:
        raise ValueError(f"不支持的方法: {method}")
    
    # 处理逻辑
    processed_data = data.copy()
    
    if method == 'advanced':
        threshold = kwargs.get('threshold', 0.0)
        processed_data = [x for x in processed_data if x > threshold]
    
    if kwargs.get('normalize', False):
        max_val = max(processed_data) if processed_data else 1
        processed_data = [x / max_val for x in processed_data]
    
    return {
        'processed_data': processed_data,
        'metadata': {
            'method': method,
            'original_length': len(data),
            'processed_length': len(processed_data)
        },
        'status': 'success'
    }
```

### NumPy风格文档字符串

```python
def matrix_multiply(a, b, transpose_a=False, transpose_b=False):
    """矩阵乘法运算。
    
    执行两个矩阵的乘法运算，支持转置选项。
    
    Parameters
    ----------
    a : array_like
        第一个输入矩阵，形状为 (m, n)
    b : array_like
        第二个输入矩阵，形状为 (n, p)
    transpose_a : bool, optional
        是否转置矩阵a，默认为False
    transpose_b : bool, optional
        是否转置矩阵b，默认为False
    
    Returns
    -------
    ndarray
        矩阵乘法的结果，形状为 (m, p)
    
    Raises
    ------
    ValueError
        当矩阵维度不匹配时
    TypeError
        当输入不是数组类型时
    
    See Also
    --------
    numpy.dot : NumPy的点积函数
    numpy.matmul : NumPy的矩阵乘法函数
    
    Notes
    -----
    这个函数实现了标准的矩阵乘法算法。对于大型矩阵，
    建议使用优化的BLAS库。
    
    矩阵乘法的数学定义：
    
    .. math:: C_{ij} = \sum_{k} A_{ik} B_{kj}
    
    Examples
    --------
    基本矩阵乘法：
    
    >>> a = [[1, 2], [3, 4]]
    >>> b = [[5, 6], [7, 8]]
    >>> result = matrix_multiply(a, b)
    >>> print(result)
    [[19, 22], [43, 50]]
    
    使用转置：
    
    >>> a = [[1, 2, 3]]
    >>> b = [[4], [5], [6]]
    >>> result = matrix_multiply(a, b, transpose_a=True)
    >>> print(result)
    [[32]]
    """
    # 简化实现
    if transpose_a:
        a = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
    if transpose_b:
        b = [[b[j][i] for j in range(len(b))] for i in range(len(b[0]))]
    
    # 检查维度
    if len(a[0]) != len(b):
        raise ValueError("矩阵维度不匹配")
    
    # 执行乘法
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            sum_val = sum(a[i][k] * b[k][j] for k in range(len(b)))
            row.append(sum_val)
        result.append(row)
    
    return result
```

## help()函数的使用

### 基本用法

```python
# 获取内置函数的帮助
help(print)
help(len)
help(str.split)

# 获取模块的帮助
import math
help(math)
help(math.sqrt)

# 获取自定义函数的帮助
def my_function():
    """这是我的函数。"""
    pass

help(my_function)
```

### 交互式帮助

```python
# 进入交互式帮助模式
help()

# 在交互式模式中：
# help> modules        # 列出所有模块
# help> keywords       # 列出所有关键字
# help> symbols        # 列出所有符号
# help> topics         # 列出所有主题
# help> quit           # 退出帮助模式
```

### 自定义帮助信息

```python
class DocumentedClass:
    """一个有完整文档的类。
    
    这个类演示了如何编写完整的类文档。
    
    Attributes:
        name (str): 对象的名称
        value (int): 对象的值
    """
    
    def __init__(self, name, value=0):
        """初始化DocumentedClass实例。
        
        Args:
            name (str): 对象的名称
            value (int, optional): 初始值，默认为0
        """
        self.name = name
        self.value = value
    
    def increment(self, amount=1):
        """增加对象的值。
        
        Args:
            amount (int, optional): 增加的数量，默认为1
        
        Returns:
            int: 增加后的值
        """
        self.value += amount
        return self.value
    
    def __str__(self):
        """返回对象的字符串表示。
        
        Returns:
            str: 对象的字符串表示
        """
        return f"{self.name}: {self.value}"
    
    @property
    def info(self):
        """获取对象信息。
        
        Returns:
            dict: 包含对象信息的字典
        """
        return {
            'name': self.name,
            'value': self.value,
            'type': type(self).__name__
        }

# 使用help()查看文档
help(DocumentedClass)
help(DocumentedClass.increment)
```

## __doc__属性

### 访问文档字符串

```python
def example_function():
    """这是示例函数的文档。"""
    pass

class ExampleClass:
    """这是示例类的文档。"""
    
    def method(self):
        """这是方法的文档。"""
        pass

# 访问文档字符串
print(example_function.__doc__)
print(ExampleClass.__doc__)
print(ExampleClass.method.__doc__)

# 模块文档
import math
print(math.__doc__)
```

### 动态设置文档字符串

```python
def create_documented_function(name, operation):
    """动态创建带文档的函数。"""
    
    def dynamic_function(x, y):
        return operation(x, y)
    
    # 动态设置文档字符串
    dynamic_function.__doc__ = f"""
    执行{name}操作。
    
    Args:
        x: 第一个操作数
        y: 第二个操作数
    
    Returns:
        操作结果
    """
    
    dynamic_function.__name__ = f"{name}_operation"
    
    return dynamic_function

# 创建函数
add_func = create_documented_function("加法", lambda x, y: x + y)
mul_func = create_documented_function("乘法", lambda x, y: x * y)

# 查看文档
print(add_func.__doc__)
print(mul_func.__doc__)

help(add_func)
```

## 文档生成工具

### Sphinx文档生成

```python
# sphinx_example.py
"""Sphinx文档生成示例模块。

这个模块演示了如何编写适合Sphinx的文档字符串。

.. moduleauthor:: Your Name <your.email@example.com>
.. versionadded:: 1.0
.. versionchanged:: 1.1
   添加了新的功能

Example:
    使用这个模块：:
    
        from sphinx_example import Calculator
        calc = Calculator()
        result = calc.add(1, 2)

Attributes:
    MODULE_VERSION (str): 模块版本号
    DEFAULT_PRECISION (int): 默认精度
"""

MODULE_VERSION = "1.1.0"
DEFAULT_PRECISION = 2

class Calculator:
    """一个简单的计算器类。
    
    这个类提供基本的数学运算功能。
    
    .. versionadded:: 1.0
    
    Args:
        precision (int, optional): 计算精度。默认为 :data:`DEFAULT_PRECISION`
    
    Attributes:
        precision (int): 当前计算精度
        history (list): 计算历史记录
    
    Example:
        创建计算器实例：:
        
            calc = Calculator(precision=3)
            result = calc.add(1.234, 5.678)
            print(f"结果: {result:.3f}")
    
    Note:
        所有计算结果都会自动记录到历史中。
    
    Warning:
        除法运算时请注意除零错误。
    """
    
    def __init__(self, precision=None):
        """初始化计算器。
        
        Args:
            precision (int, optional): 计算精度
        """
        self.precision = precision or DEFAULT_PRECISION
        self.history = []
    
    def add(self, a, b):
        """执行加法运算。
        
        .. versionadded:: 1.0
        
        Args:
            a (float): 第一个加数
            b (float): 第二个加数
        
        Returns:
            float: 加法结果，精度为 :attr:`precision`
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(1.5, 2.3)
            3.8
        
        See Also:
            :meth:`subtract`: 减法运算
            :meth:`multiply`: 乘法运算
        """
        result = round(a + b, self.precision)
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def divide(self, a, b):
        """执行除法运算。
        
        .. versionadded:: 1.0
        .. versionchanged:: 1.1
           添加了除零检查
        
        Args:
            a (float): 被除数
            b (float): 除数
        
        Returns:
            float: 除法结果
        
        Raises:
            ZeroDivisionError: 当除数为零时
        
        Example:
            >>> calc = Calculator()
            >>> calc.divide(10, 2)
            5.0
            
            >>> calc.divide(10, 0)  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ZeroDivisionError: 除数不能为零
        
        Warning:
            请确保除数不为零。
        """
        if b == 0:
            raise ZeroDivisionError("除数不能为零")
        
        result = round(a / b, self.precision)
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        """获取计算历史。
        
        Returns:
            list[str]: 计算历史记录列表
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3.0
            >>> calc.get_history()
            ['1 + 2 = 3.0']
        """
        return self.history.copy()
    
    def clear_history(self):
        """清空计算历史。
        
        .. versionadded:: 1.1
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3.0
            >>> calc.clear_history()
            >>> calc.get_history()
            []
        """
        self.history.clear()

def factorial(n):
    """计算阶乘。
    
    .. versionadded:: 1.0
    
    这个函数计算给定数字的阶乘。
    
    Args:
        n (int): 要计算阶乘的非负整数
    
    Returns:
        int: n的阶乘值
    
    Raises:
        ValueError: 当n为负数时
        TypeError: 当n不是整数时
    
    Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    
    Note:
        根据数学定义，0! = 1。
    
    .. math::
        n! = \prod_{i=1}^{n} i = 1 \times 2 \times 3 \times \ldots \times n
    """
    if not isinstance(n, int):
        raise TypeError("n必须是整数")
    
    if n < 0:
        raise ValueError("n必须是非负整数")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result
```

### pydoc工具使用

```python
# 使用pydoc生成文档
# 命令行使用：
# python -m pydoc module_name
# python -m pydoc -w module_name  # 生成HTML文档
# python -m pydoc -p 8080         # 启动文档服务器

# 在代码中使用pydoc
import pydoc

def generate_module_doc(module_name):
    """生成模块文档。"""
    try:
        # 获取模块文档
        doc = pydoc.render_doc(module_name)
        print(doc)
        
        # 生成HTML文档
        html_doc = pydoc.html.document(module_name)
        
        # 保存到文件
        with open(f"{module_name}_doc.html", 'w', encoding='utf-8') as f:
            f.write(html_doc)
        
        print(f"HTML文档已保存到 {module_name}_doc.html")
        
    except ImportError:
        print(f"无法导入模块: {module_name}")

# 示例使用
if __name__ == '__main__':
    generate_module_doc('math')
```

## 文档测试（doctest）

### 基本doctest

```python
def fibonacci(n):
    """计算斐波那契数列的第n项。
    
    Args:
        n (int): 项数（从0开始）
    
    Returns:
        int: 第n项的值
    
    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(5)
        5
        >>> fibonacci(10)
        55
        
        测试边界情况：
        >>> fibonacci(-1)
        Traceback (most recent call last):
        ValueError: n必须是非负整数
    """
    if n < 0:
        raise ValueError("n必须是非负整数")
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

def is_prime(n):
    """检查一个数是否为质数。
    
    Args:
        n (int): 要检查的数
    
    Returns:
        bool: 如果是质数返回True，否则返回False
    
    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
        >>> is_prime(1)
        False
        
        测试大数：
        >>> is_prime(97)
        True
        >>> is_prime(100)
        False
    """
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

# 运行doctest
if __name__ == '__main__':
    import doctest
    
    print("运行doctest...")
    result = doctest.testmod(verbose=True)
    
    if result.failed == 0:
        print(f"\n✓ 所有 {result.attempted} 个测试通过！")
    else:
        print(f"\n✗ {result.failed}/{result.attempted} 个测试失败")
```

### 高级doctest功能

```python
def advanced_doctest_example():
    """高级doctest功能演示。
    
    Examples:
        测试浮点数比较：
        >>> import math
        >>> result = math.sqrt(2) ** 2
        >>> abs(result - 2.0) < 1e-10
        True
        
        测试异常：
        >>> 1 / 0  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ZeroDivisionError: ...
        
        测试输出格式：
        >>> print("Hello\nWorld")  # doctest: +NORMALIZE_WHITESPACE
        Hello
        World
        
        跳过测试：
        >>> import sys
        >>> if sys.platform == 'win32':  # doctest: +SKIP
        ...     print("Windows specific code")
        
        测试省略输出：
        >>> list(range(20))  # doctest: +ELLIPSIS
        [0, 1, 2, ..., 17, 18, 19]
    """
    pass

class DocumentedDataStructure:
    """带文档测试的数据结构。
    
    Examples:
        创建和使用：
        >>> ds = DocumentedDataStructure()
        >>> ds.add(1)
        >>> ds.add(2)
        >>> ds.add(3)
        >>> ds.size()
        3
        >>> ds.contains(2)
        True
        >>> ds.contains(4)
        False
        
        测试删除：
        >>> ds.remove(2)
        True
        >>> ds.size()
        2
        >>> ds.contains(2)
        False
        
        测试清空：
        >>> ds.clear()
        >>> ds.size()
        0
    """
    
    def __init__(self):
        """初始化数据结构。
        
        Examples:
            >>> ds = DocumentedDataStructure()
            >>> ds.size()
            0
        """
        self._data = set()
    
    def add(self, item):
        """添加元素。
        
        Args:
            item: 要添加的元素
        
        Examples:
            >>> ds = DocumentedDataStructure()
            >>> ds.add("hello")
            >>> ds.contains("hello")
            True
        """
        self._data.add(item)
    
    def remove(self, item):
        """删除元素。
        
        Args:
            item: 要删除的元素
        
        Returns:
            bool: 如果元素存在并被删除返回True，否则返回False
        
        Examples:
            >>> ds = DocumentedDataStructure()
            >>> ds.add("test")
            >>> ds.remove("test")
            True
            >>> ds.remove("nonexistent")
            False
        """
        if item in self._data:
            self._data.remove(item)
            return True
        return False
    
    def contains(self, item):
        """检查元素是否存在。
        
        Args:
            item: 要检查的元素
        
        Returns:
            bool: 如果元素存在返回True，否则返回False
        
        Examples:
            >>> ds = DocumentedDataStructure()
            >>> ds.contains("anything")
            False
            >>> ds.add(42)
            >>> ds.contains(42)
            True
        """
        return item in self._data
    
    def size(self):
        """获取元素数量。
        
        Returns:
            int: 元素数量
        
        Examples:
            >>> ds = DocumentedDataStructure()
            >>> ds.size()
            0
            >>> ds.add(1)
            >>> ds.add(2)
            >>> ds.size()
            2
        """
        return len(self._data)
    
    def clear(self):
        """清空所有元素。
        
        Examples:
            >>> ds = DocumentedDataStructure()
            >>> ds.add(1)
            >>> ds.add(2)
            >>> ds.clear()
            >>> ds.size()
            0
        """
        self._data.clear()
```

## 文档最佳实践

### 1. 文档结构规范

```python
def well_documented_function(param1, param2, *args, **kwargs):
    """函数的简短描述（一行）。
    
    更详细的描述，可以包含多行。解释函数的用途、
    算法、注意事项等。
    
    Args:
        param1 (type): 参数1的描述
        param2 (type): 参数2的描述
        *args: 可变位置参数的描述
        **kwargs: 可变关键字参数的描述
    
    Returns:
        type: 返回值的描述
    
    Raises:
        ExceptionType: 异常的描述
    
    Yields:
        type: 生成器函数的yield值描述
    
    Example:
        >>> result = well_documented_function(1, 2)
        >>> print(result)
        3
    
    Note:
        重要的注意事项
    
    Todo:
        * 待完成的功能
        * 需要改进的地方
    
    .. versionadded:: 1.0
    .. versionchanged:: 1.1
       添加了新参数
    .. deprecated:: 1.2
       使用new_function替代
    """
    return param1 + param2
```

### 2. 模块级文档

```python
# module_example.py
"""模块标题：简短描述模块功能。

更详细的模块描述，包括：
- 模块的主要功能
- 使用场景
- 依赖关系
- 版本信息

Example:
    典型的使用方式：:
    
        from module_example import MainClass
        obj = MainClass()
        result = obj.process()

Attributes:
    module_level_variable1 (str): 模块级变量的描述
    module_level_variable2 (int): 另一个模块级变量

Todo:
    * 添加更多功能
    * 优化性能
    * 完善文档

.. moduleauthor:: Your Name <your.email@example.com>
.. versionadded:: 1.0
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"
__all__ = ['MainClass', 'helper_function']

module_level_variable1 = "example"
module_level_variable2 = 42

class MainClass:
    """主要的类。
    
    详细描述类的功能和用途。
    """
    pass

def helper_function():
    """辅助函数。
    
    描述函数的功能。
    """
    pass
```

### 3. 文档维护策略

```python
class DocumentationManager:
    """文档管理器。
    
    用于管理和维护项目文档的工具类。
    """
    
    def __init__(self):
        """初始化文档管理器。"""
        self.docs = {}
        self.version = "1.0.0"
    
    def validate_docstrings(self, module):
        """验证模块的文档字符串。
        
        Args:
            module: 要验证的模块
        
        Returns:
            dict: 验证结果
        """
        results = {
            'missing_docs': [],
            'incomplete_docs': [],
            'good_docs': []
        }
        
        # 检查模块文档
        if not module.__doc__:
            results['missing_docs'].append(module.__name__)
        elif len(module.__doc__.strip()) < 10:
            results['incomplete_docs'].append(module.__name__)
        else:
            results['good_docs'].append(module.__name__)
        
        # 检查函数和类的文档
        for name in dir(module):
            obj = getattr(module, name)
            if callable(obj) and not name.startswith('_'):
                if not obj.__doc__:
                    results['missing_docs'].append(f"{module.__name__}.{name}")
                elif len(obj.__doc__.strip()) < 10:
                    results['incomplete_docs'].append(f"{module.__name__}.{name}")
                else:
                    results['good_docs'].append(f"{module.__name__}.{name}")
        
        return results
    
    def generate_doc_report(self, modules):
        """生成文档报告。
        
        Args:
            modules (list): 要检查的模块列表
        
        Returns:
            str: 文档报告
        """
        report = ["# 文档质量报告\n"]
        
        total_missing = 0
        total_incomplete = 0
        total_good = 0
        
        for module in modules:
            results = self.validate_docstrings(module)
            
            report.append(f"## {module.__name__}\n")
            
            if results['missing_docs']:
                report.append("### 缺少文档：")
                for item in results['missing_docs']:
                    report.append(f"- {item}")
                report.append("")
            
            if results['incomplete_docs']:
                report.append("### 文档不完整：")
                for item in results['incomplete_docs']:
                    report.append(f"- {item}")
                report.append("")
            
            if results['good_docs']:
                report.append("### 文档良好：")
                for item in results['good_docs']:
                    report.append(f"- {item}")
                report.append("")
            
            total_missing += len(results['missing_docs'])
            total_incomplete += len(results['incomplete_docs'])
            total_good += len(results['good_docs'])
        
        # 添加总结
        total = total_missing + total_incomplete + total_good
        if total > 0:
            good_percentage = (total_good / total) * 100
            report.append(f"## 总结\n")
            report.append(f"- 文档良好: {total_good} ({good_percentage:.1f}%)")
            report.append(f"- 文档不完整: {total_incomplete}")
            report.append(f"- 缺少文档: {total_missing}")
        
        return "\n".join(report)

# 使用示例
if __name__ == '__main__':
    import sys
    import math
    
    doc_manager = DocumentationManager()
    
    # 检查一些模块的文档
    modules_to_check = [sys, math]
    report = doc_manager.generate_doc_report(modules_to_check)
    print(report)
```

## 学习要点

1. **文档字符串规范**：遵循PEP 257和项目约定
2. **help()函数使用**：获取交互式帮助信息
3. **__doc__属性**：访问和设置文档字符串
4. **文档生成工具**：Sphinx、pydoc等工具的使用
5. **doctest测试**：在文档中编写可执行的测试
6. **文档维护**：保持文档的准确性和完整性

## 最佳实践

1. **简洁明了**：文档应该简洁但完整
2. **及时更新**：代码变更时同步更新文档
3. **示例丰富**：提供实用的代码示例
4. **格式统一**：遵循项目的文档格式规范
5. **测试文档**：使用doctest验证文档中的示例
6. **分层文档**：模块、类、函数都应有适当的文档

通过掌握Python的文档和帮助系统，你可以编写更易维护和使用的代码，同时也能更好地理解和使用其他人的代码。