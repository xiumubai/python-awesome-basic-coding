#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
import语句的各种用法

本文件演示了Python中import语句的各种用法：
1. 基本的import语句
2. from...import语句
3. import...as语句
4. 导入多个模块和对象
5. 导入模块的所有内容
6. 相对导入和绝对导入
7. 动态导入
8. 导入的最佳实践

理解不同的导入方式对于编写清晰、可维护的Python代码非常重要。
"""

import sys
import os

# 通配符导入需要在模块级别进行
from math import *

# ============================================================================
# 1. 基本的import语句
# ============================================================================

def demonstrate_basic_import():
    """
    演示基本的import语句用法
    """
    print("=" * 60)
    print("1. 基本的import语句")
    print("=" * 60)
    
    # 导入整个模块
    import math
    import datetime
    import random
    
    print("导入的模块:")
    print(f"math模块: {math}")
    print(f"datetime模块: {datetime}")
    print(f"random模块: {random}")
    
    # 使用导入的模块
    print("\n使用导入的模块:")
    print(f"π的值: {math.pi}")
    print(f"2的平方根: {math.sqrt(2)}")
    print(f"当前时间: {datetime.datetime.now()}")
    print(f"随机数: {random.randint(1, 100)}")
    
    # 导入自定义模块（使用importlib处理数字开头的模块名）
    try:
        import importlib
        module_basics = importlib.import_module('01_module_basics')
        print(f"\n导入自定义模块: {module_basics.MODULE_NAME}")
        print(f"模块版本: {module_basics.MODULE_VERSION}")
    except ImportError as e:
        print(f"\n导入自定义模块失败: {e}")
        print("注意: 模块名不能以数字开头，使用importlib动态导入")

# ============================================================================
# 2. from...import语句
# ============================================================================

def demonstrate_from_import():
    """
    演示from...import语句用法
    """
    print("\n" + "=" * 60)
    print("2. from...import语句")
    print("=" * 60)
    
    # 从模块中导入特定的函数或变量
    from math import pi, sqrt, sin, cos
    from datetime import datetime, date, time
    from random import randint, choice, shuffle
    
    print("从模块中导入特定对象:")
    print(f"π的值: {pi}")
    print(f"4的平方根: {sqrt(4)}")
    print(f"sin(π/2): {sin(pi/2)}")
    print(f"cos(0): {cos(0)}")
    
    print(f"\n当前日期时间: {datetime.now()}")
    print(f"今天的日期: {date.today()}")
    
    numbers = [1, 2, 3, 4, 5]
    print(f"\n原始列表: {numbers}")
    shuffle(numbers)
    print(f"打乱后的列表: {numbers}")
    print(f"随机选择: {choice(['苹果', '香蕉', '橙子'])}")
    
    # 从自定义模块导入特定对象
    try:
        # 注意: 由于模块名以数字开头，这里使用importlib动态导入
        import importlib
        module_basics = importlib.import_module('01_module_basics')
        
        # 获取模块中的特定对象
        greet = getattr(module_basics, 'greet')
        Calculator = getattr(module_basics, 'Calculator')
        
        print(f"\n使用导入的函数: {greet('Python')}")
        calc = Calculator("导入的计算器")
        print(f"使用导入的类: {calc.add(10, 20)}")
        
    except Exception as e:
        print(f"\n动态导入示例失败: {e}")

# ============================================================================
# 3. import...as语句
# ============================================================================

def demonstrate_import_as():
    """
    演示import...as语句用法（别名导入）
    """
    print("\n" + "=" * 60)
    print("3. import...as语句（别名导入）")
    print("=" * 60)
    
    # 为模块设置别名
    import numpy as np  # 常见的numpy别名
    import pandas as pd  # 常见的pandas别名
    import matplotlib.pyplot as plt  # 常见的matplotlib别名
    
    # 注意: 这些模块可能没有安装，这里仅作演示
    print("常见的模块别名:")
    print("import numpy as np")
    print("import pandas as pd")
    print("import matplotlib.pyplot as plt")
    
    # 为标准库模块设置别名
    import datetime as dt
    import collections as coll
    import itertools as it
    
    print("\n标准库模块别名示例:")
    now = dt.datetime.now()
    print(f"当前时间 (使用dt别名): {now}")
    
    # 为函数设置别名
    from math import sqrt as square_root
    from random import randint as random_integer
    
    print(f"\n函数别名示例:")
    print(f"16的平方根 (使用square_root别名): {square_root(16)}")
    print(f"随机整数 (使用random_integer别名): {random_integer(1, 10)}")
    
    # 为类设置别名
    from collections import defaultdict as dd
    from collections import Counter as count
    
    print("\n类别名示例:")
    word_count = count(['apple', 'banana', 'apple', 'cherry', 'banana', 'apple'])
    print(f"单词计数 (使用count别名): {dict(word_count)}")

# ============================================================================
# 4. 导入多个模块和对象
# ============================================================================

def demonstrate_multiple_imports():
    """
    演示导入多个模块和对象的方法
    """
    print("\n" + "=" * 60)
    print("4. 导入多个模块和对象")
    print("=" * 60)
    
    # 在一行中导入多个模块
    import json, csv, xml.etree.ElementTree
    
    print("一行导入多个模块:")
    print("import json, csv, xml.etree.ElementTree")
    
    # 从一个模块导入多个对象
    from os import path, getcwd, listdir, environ
    from sys import version, platform, path as sys_path
    
    print("\n从模块导入多个对象:")
    print(f"当前工作目录: {getcwd()}")
    print(f"Python版本: {version}")
    print(f"操作系统平台: {platform}")
    
    # 多行导入（推荐的风格）
    from datetime import (
        datetime,
        date,
        time,
        timedelta,
        timezone
    )
    
    print("\n多行导入示例:")
    now = datetime.now()
    tomorrow = now + timedelta(days=1)
    print(f"现在: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"明天: {tomorrow.strftime('%Y-%m-%d %H:%M:%S')}")

# ============================================================================
# 5. 导入模块的所有内容（不推荐）
# ============================================================================

def demonstrate_wildcard_import():
    """
    演示通配符导入 (不推荐使用)
    """
    print("\n=== 6. 通配符导入 (不推荐) ===")
    
    print(f"使用通配符导入的函数:")
    print(f"sqrt(16) = {sqrt(16)}")
    print(f"sin(pi/2) = {sin(pi/2)}")
    print(f"cos(0) = {cos(0)}")
    
    print("\n注意: 通配符导入可能导致命名冲突，不推荐使用")

# ============================================================================
# 6. 条件导入和异常处理
# ============================================================================

def demonstrate_conditional_import():
    """
    演示条件导入和导入异常处理
    """
    print("\n" + "=" * 60)
    print("6. 条件导入和异常处理")
    print("=" * 60)
    
    # 尝试导入可选的第三方库
    print("尝试导入第三方库:")
    
    # 尝试导入numpy
    try:
        import numpy as np
        print("✓ numpy已安装")
        HAS_NUMPY = True
    except ImportError:
        print("✗ numpy未安装")
        HAS_NUMPY = False
    
    # 尝试导入pandas
    try:
        import pandas as pd
        print("✓ pandas已安装")
        HAS_PANDAS = True
    except ImportError:
        print("✗ pandas未安装")
        HAS_PANDAS = False
    
    # 尝试导入matplotlib
    try:
        import matplotlib.pyplot as plt
        print("✓ matplotlib已安装")
        HAS_MATPLOTLIB = True
    except ImportError:
        print("✗ matplotlib未安装")
        HAS_MATPLOTLIB = False
    
    # 根据导入结果执行不同的代码
    print("\n根据导入结果执行代码:")
    if HAS_NUMPY:
        print("可以使用numpy进行数值计算")
    else:
        print("使用标准库进行数值计算")
    
    # 版本兼容性导入
    print("\n版本兼容性导入:")
    try:
        # Python 3.8+
        from functools import cached_property
        print("✓ 使用cached_property (Python 3.8+)")
    except ImportError:
        # 为旧版本提供替代方案
        print("✗ cached_property不可用，使用property替代")
        cached_property = property
    
    # 平台特定导入
    print("\n平台特定导入:")
    import platform
    if platform.system() == 'Windows':
        try:
            import winsound
            print("✓ Windows特定模块winsound可用")
        except ImportError:
            print("✗ winsound不可用")
    else:
        print(f"当前平台: {platform.system()}，跳过Windows特定模块")

# ============================================================================
# 7. 动态导入
# ============================================================================

def demonstrate_dynamic_import():
    """
    演示动态导入模块
    """
    print("\n" + "=" * 60)
    print("7. 动态导入")
    print("=" * 60)
    
    import importlib
    
    # 动态导入标准库模块
    module_names = ['math', 'random', 'datetime', 'json']
    
    print("动态导入标准库模块:")
    imported_modules = {}
    
    for module_name in module_names:
        try:
            module = importlib.import_module(module_name)
            imported_modules[module_name] = module
            print(f"✓ 成功导入 {module_name}")
        except ImportError as e:
            print(f"✗ 导入 {module_name} 失败: {e}")
    
    # 使用动态导入的模块
    print("\n使用动态导入的模块:")
    if 'math' in imported_modules:
        math_module = imported_modules['math']
        print(f"π的值: {math_module.pi}")
    
    if 'random' in imported_modules:
        random_module = imported_modules['random']
        print(f"随机数: {random_module.randint(1, 100)}")
    
    # 动态获取模块属性
    print("\n动态获取模块属性:")
    if 'math' in imported_modules:
        math_module = imported_modules['math']
        
        # 获取所有以's'开头的函数
        s_functions = [name for name in dir(math_module) 
                      if name.startswith('s') and callable(getattr(math_module, name))]
        print(f"math模块中以's'开头的函数: {s_functions[:5]}...")
        
        # 动态调用函数
        if 'sqrt' in s_functions:
            sqrt_func = getattr(math_module, 'sqrt')
            print(f"动态调用sqrt(16): {sqrt_func(16)}")
    
    # 重新加载模块
    print("\n重新加载模块:")
    if 'math' in imported_modules:
        math_module = imported_modules['math']
        reloaded_module = importlib.reload(math_module)
        print(f"重新加载math模块: {reloaded_module}")

# ============================================================================
# 8. 导入的最佳实践
# ============================================================================

def demonstrate_import_best_practices():
    """
    演示导入的最佳实践
    """
    print("\n" + "=" * 60)
    print("8. 导入的最佳实践")
    print("=" * 60)
    
    print("导入顺序（PEP 8推荐）:")
    print("1. 标准库导入")
    print("2. 相关第三方库导入")
    print("3. 本地应用/库导入")
    print("4. 每组之间用空行分隔")
    
    print("\n推荐的导入风格:")
    print("""
# 标准库导入
import os
import sys
from collections import defaultdict
from datetime import datetime

# 第三方库导入
import numpy as np
import pandas as pd
from requests import get

# 本地导入
from mypackage import mymodule
from . import sibling_module
from ..parent import parent_module
""")
    
    print("\n避免的做法:")
    print("✗ from module import *  # 污染命名空间")
    print("✗ import sys, os, json  # 一行导入多个模块")
    print("✗ 在函数内部导入（除非必要）")
    print("✗ 使用相对导入时不清晰的路径")
    
    print("\n推荐的做法:")
    print("✓ 明确导入需要的对象")
    print("✓ 使用有意义的别名")
    print("✓ 在文件顶部进行导入")
    print("✓ 按照PEP 8的顺序组织导入")
    print("✓ 使用绝对导入而不是相对导入")

# ============================================================================
# 9. 查看导入信息
# ============================================================================

def show_import_information():
    """
    显示当前模块的导入信息
    """
    print("\n" + "=" * 60)
    print("9. 查看导入信息")
    print("=" * 60)
    
    print("当前模块信息:")
    print(f"模块名称: {__name__}")
    print(f"模块文件: {__file__}")
    
    print("\nPython路径:")
    for i, path in enumerate(sys.path[:5], 1):
        print(f"{i}. {path}")
    if len(sys.path) > 5:
        print(f"... 还有 {len(sys.path) - 5} 个路径")
    
    print("\n已导入的模块（部分）:")
    imported_modules = list(sys.modules.keys())[:10]
    for module in imported_modules:
        print(f"  {module}")
    print(f"... 总共 {len(sys.modules)} 个模块")
    
    print("\n当前命名空间中的名称:")
    current_names = [name for name in dir() if not name.startswith('_')]
    print(f"公共名称: {current_names}")

# ============================================================================
# 主函数
# ============================================================================

def main():
    """
    主函数，演示所有import语句的用法
    """
    print("Python Import语句完整演示")
    print("=" * 80)
    
    demonstrate_basic_import()
    demonstrate_from_import()
    demonstrate_import_as()
    demonstrate_multiple_imports()
    demonstrate_wildcard_import()
    demonstrate_conditional_import()
    demonstrate_dynamic_import()
    demonstrate_import_best_practices()
    show_import_information()
    
    print("\n" + "=" * 80)
    print("Import语句演示完成！")
    print("=" * 80)

if __name__ == "__main__":
    main()