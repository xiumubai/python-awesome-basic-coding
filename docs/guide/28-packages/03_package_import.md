# 包的导入和使用方法

## 概述

本节学习Python包的各种导入方式和使用方法，包括基本导入语法、别名导入、子包导入、动态导入等高级技巧。

## 学习要点

- 掌握各种导入语法：`import`、`from...import`
- 理解不同导入方式的区别和适用场景
- 学会使用别名避免命名冲突
- 了解子包的导入方式
- 掌握动态导入的使用方法
- 理解Python的模块搜索机制
- 遵循导入的最佳实践

## 导入语法类型

### 1. 基本导入语法

```python
# 1. 导入整个包
import package_name

# 2. 导入包中的模块
from package_name import module_name

# 3. 导入模块中的特定对象
from package_name.module_name import function_name, ClassName

# 4. 导入所有公开对象（不推荐）
from package_name import *
```

### 2. 别名导入

```python
# 包别名
import package_name as alias

# 模块别名
from package_name import module_name as mod

# 对象别名
from package_name.module_name import function_name as func
```

## 演示包结构

程序会创建以下演示包结构：

```
import_demo/
├── __init__.py
├── calculator.py
├── text_processor.py
├── utilities.py
└── advanced/
    ├── __init__.py
    ├── data_structures.py
    └── algorithms.py
```

## 代码示例

### 基本导入演示

```python
def demonstrate_basic_imports():
    """
    演示基本导入方式
    """
    print("\n=== 基本导入方式演示 ===")
    
    try:
        # 1. 导入整个包
        print("\n1. 导入整个包:")
        print("   import import_demo")
        import import_demo
        print(f"   包信息: {import_demo.get_package_info()}")
        
        # 2. 导入包中的模块
        print("\n2. 导入包中的模块:")
        print("   from import_demo import calculator")
        from import_demo import calculator
        
        calc = calculator.Calculator()
        result = calc.add(10, 5)
        print(f"   Calculator().add(10, 5) = {result}")
        
        # 3. 导入特定类
        print("\n3. 导入特定类:")
        print("   from import_demo.calculator import Calculator")
        from import_demo.calculator import Calculator
        
        calc2 = Calculator()
        result2 = calc2.multiply(3, 7)
        print(f"   Calculator().multiply(3, 7) = {result2}")
        
    except ImportError as e:
        print(f"导入错误: {e}")
```

### 别名导入演示

```python
def demonstrate_alias_imports():
    """
    演示别名导入
    """
    print("\n=== 别名导入演示 ===")
    
    try:
        # 1. 包别名
        print("\n1. 包别名:")
        print("   import import_demo as demo")
        import import_demo as demo
        info = demo.get_package_info()
        print(f"   demo.get_package_info(): {info}")
        
        # 2. 模块别名
        print("\n2. 模块别名:")
        print("   from import_demo import utilities as utils")
        from import_demo import utilities as utils
        
        timestamp = utils.get_timestamp()
        formatted = utils.format_number(3.14159, 3)
        print(f"   utils.get_timestamp(): {timestamp}")
        print(f"   utils.format_number(3.14159, 3): {formatted}")
        
    except ImportError as e:
        print(f"导入错误: {e}")
```

### 子包导入演示

```python
def demonstrate_subpackage_imports():
    """
    演示子包导入
    """
    print("\n=== 子包导入演示 ===")
    
    try:
        # 1. 导入子包
        print("\n1. 导入子包:")
        print("   from import_demo import advanced")
        from import_demo import advanced
        
        stack = advanced.Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        print(f"   创建栈并添加元素: [1, 2, 3]")
        print(f"   栈顶元素: {stack.peek()}")
        print(f"   栈大小: {stack.size()}")
        
        # 2. 导入子包中的模块
        print("\n2. 导入子包中的模块:")
        print("   from import_demo.advanced import algorithms")
        from import_demo.advanced import algorithms
        
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr = algorithms.bubble_sort(arr)
        print(f"   原数组: {arr}")
        print(f"   冒泡排序后: {sorted_arr}")
        
    except ImportError as e:
        print(f"导入错误: {e}")
```

### 动态导入演示

```python
def demonstrate_dynamic_import():
    """
    演示动态导入
    """
    print("\n=== 动态导入演示 ===")
    
    print("\n1. 使用importlib.import_module():")
    try:
        # 动态导入模块
        module_name = "import_demo.calculator"
        calc_module = importlib.import_module(module_name)
        print(f"   动态导入: {module_name}")
        
        # 使用动态导入的模块
        calc = calc_module.Calculator()
        result = calc.add(15, 25)
        print(f"   Calculator().add(15, 25) = {result}")
        
        # 动态获取属性
        Calculator = getattr(calc_module, 'Calculator')
        calc2 = Calculator()
        result2 = calc2.subtract(50, 20)
        print(f"   动态获取Calculator类并使用: {result2}")
        
    except ImportError as e:
        print(f"动态导入错误: {e}")
```

## 模块搜索机制

### Python模块搜索路径

```python
def demonstrate_import_path():
    """
    演示导入路径和搜索机制
    """
    print("\n=== 导入路径和搜索机制 ===")
    
    print("\nPython模块搜索路径 (sys.path):")
    for i, path in enumerate(sys.path[:5]):  # 只显示前5个路径
        print(f"   {i+1}. {path}")
    
    print("\n搜索顺序:")
    print("1. 当前工作目录")
    print("2. PYTHONPATH环境变量中的目录")
    print("3. Python标准库目录")
    print("4. site-packages目录（第三方包）")
```

## 导入最佳实践

### 1. 导入顺序
```python
# 标准库模块
import os
import sys

# 第三方库模块
import numpy as np
import pandas as pd

# 本地应用/库模块
from mypackage import mymodule
from . import local_module
```

### 2. 导入风格
- ✅ 优先使用 `import module`
- ✅ 使用有意义的别名
- ❌ 避免使用 `from module import *`
- ✅ 明确导入需要的对象

### 3. 性能考虑
- 避免在函数内部导入（除非必要）
- 考虑延迟导入大型模块
- 使用条件导入处理可选依赖

### 4. 错误处理
```python
try:
    import optional_module
except ImportError:
    optional_module = None
    print("可选模块未安装，使用备选方案")
```

## 星号导入的问题

### 为什么不推荐使用 `from module import *`

1. **命名冲突**：可能覆盖现有变量
2. **可读性差**：难以追踪函数来源
3. **性能影响**：导入不需要的对象
4. **维护困难**：代码依赖关系不明确

### 更好的替代方案
```python
# 不推荐
from math import *
result = sin(pi/2)  # 不清楚sin和pi来自哪里

# 推荐
import math
result = math.sin(math.pi/2)  # 清楚来源

# 或者
from math import sin, pi
result = sin(pi/2)  # 明确导入
```

## 常见问题

### 1. 循环导入问题
```python
# 避免循环导入
# module_a.py
from module_b import function_b  # 可能导致循环导入

# 解决方案：延迟导入
def my_function():
    from module_b import function_b  # 在函数内导入
    return function_b()
```

### 2. 相对导入 vs 绝对导入
```python
# 绝对导入（推荐）
from mypackage.subpackage import module

# 相对导入（在包内使用）
from .subpackage import module
from ..parent_package import module
```

## 学习总结

1. **掌握基本语法**：理解各种导入方式的用法和区别
2. **合理使用别名**：避免命名冲突，提高代码可读性
3. **了解搜索机制**：理解Python如何查找和加载模块
4. **遵循最佳实践**：保持代码整洁、可读、可维护
5. **处理导入错误**：妥善处理ImportError，提供备选方案
6. **避免常见陷阱**：如星号导入、循环导入等问题
7. **使用动态导入**：在需要时灵活加载模块

通过掌握这些导入技巧，你可以更好地组织和使用Python包，编写更加模块化和可维护的代码。