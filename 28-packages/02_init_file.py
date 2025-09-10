#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__init__.py文件的作用和使用

__init__.py文件是Python包的标识文件，它的存在使得目录被Python识别为包。
这个文件可以为空，也可以包含初始化代码。

学习要点：
1. __init__.py文件的作用
2. 包的初始化过程
3. 控制包的导入行为
4. __all__变量的使用
5. 包级别的变量和函数
"""

import os
import sys

def demonstrate_init_file_purpose():
    """
    演示__init__.py文件的作用
    """
    print("=== __init__.py文件的作用 ===")
    print("\n1. 标识包：")
    print("   - 使目录被Python识别为包")
    print("   - 没有__init__.py的目录不是包")
    
    print("\n2. 初始化包：")
    print("   - 包被首次导入时执行__init__.py中的代码")
    print("   - 可以进行包级别的初始化操作")
    
    print("\n3. 控制导入：")
    print("   - 定义__all__变量控制from package import *的行为")
    print("   - 可以在包级别定义变量和函数")
    
    print("\n4. 简化导入：")
    print("   - 可以在__init__.py中导入子模块")
    print("   - 提供更简洁的导入接口")

def create_init_examples():
    """
    创建不同类型的__init__.py示例
    """
    print("\n=== 创建__init__.py示例 ===")
    
    base_path = os.path.dirname(__file__)
    
    # 示例1：空的__init__.py
    example1_path = os.path.join(base_path, 'init_examples', 'empty_package')
    os.makedirs(example1_path, exist_ok=True)
    
    with open(os.path.join(example1_path, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write('# 空的__init__.py文件\n# 这个文件使目录成为一个包\n')
    
    with open(os.path.join(example1_path, 'module1.py'), 'w', encoding='utf-8') as f:
        f.write('''
# 简单模块
def hello():
    return "Hello from module1"

VERSION = "1.0.0"
''')
    
    print("创建示例1：空的__init__.py包")
    
    # 示例2：带初始化代码的__init__.py
    example2_path = os.path.join(base_path, 'init_examples', 'init_package')
    os.makedirs(example2_path, exist_ok=True)
    
    with open(os.path.join(example2_path, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write('''
# 带初始化代码的__init__.py
print("正在初始化init_package包")

# 包级别的变量
PACKAGE_NAME = "init_package"
VERSION = "2.0.0"

# 包级别的函数
def get_package_info():
    return f"{PACKAGE_NAME} v{VERSION}"

# 初始化时执行的代码
print(f"包信息: {get_package_info()}")
''')
    
    with open(os.path.join(example2_path, 'utils.py'), 'w', encoding='utf-8') as f:
        f.write('''
# 工具模块
def format_text(text):
    return text.upper()

def calculate_sum(numbers):
    return sum(numbers)
''')
    
    print("创建示例2：带初始化代码的__init__.py包")
    
    # 示例3：使用__all__的__init__.py
    example3_path = os.path.join(base_path, 'init_examples', 'controlled_package')
    os.makedirs(example3_path, exist_ok=True)
    
    with open(os.path.join(example3_path, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write('''
# 使用__all__控制导入的__init__.py

# 导入子模块
from .math_ops import add, multiply
from .string_ops import reverse, capitalize

# 定义__all__变量
__all__ = ['add', 'multiply', 'reverse', 'get_version']

# 包级别的变量
__version__ = "3.0.0"

# 包级别的函数
def get_version():
    return __version__

print(f"controlled_package v{__version__} 已加载")
''')
    
    with open(os.path.join(example3_path, 'math_ops.py'), 'w', encoding='utf-8') as f:
        f.write('''
# 数学操作模块
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else None
''')
    
    with open(os.path.join(example3_path, 'string_ops.py'), 'w', encoding='utf-8') as f:
        f.write('''
# 字符串操作模块
def reverse(s):
    return s[::-1]

def capitalize(s):
    return s.capitalize()

def lowercase(s):
    return s.lower()
''')
    
    print("创建示例3：使用__all__控制导入的__init__.py包")
    
    # 示例4：复杂的__init__.py
    example4_path = os.path.join(base_path, 'init_examples', 'complex_package')
    os.makedirs(example4_path, exist_ok=True)
    
    with open(os.path.join(example4_path, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write('''
# 复杂的__init__.py示例
import os
import sys
from datetime import datetime

# 包信息
__version__ = "4.0.0"
__author__ = "Python学习者"
__email__ = "learner@python.org"

print(f"正在加载 {__name__} 包...")

# 动态导入模块
try:
    from .core import CoreClass
    from .helpers import helper_function
    CORE_AVAILABLE = True
except ImportError as e:
    print(f"警告：核心模块导入失败 - {e}")
    CORE_AVAILABLE = False

# 包级别的配置
CONFIG = {
    'debug': False,
    'log_level': 'INFO',
    'created_at': datetime.now().isoformat()
}

# 包级别的函数
def get_info():
    return {
        'name': __name__,
        'version': __version__,
        'author': __author__,
        'core_available': CORE_AVAILABLE,
        'config': CONFIG
    }

def configure(debug=None, log_level=None):
    if debug is not None:
        CONFIG['debug'] = debug
    if log_level is not None:
        CONFIG['log_level'] = log_level
    print(f"包配置已更新: {CONFIG}")

# 定义公共接口
__all__ = ['CoreClass', 'helper_function', 'get_info', 'configure', 'CONFIG']

print(f"{__name__} v{__version__} 加载完成")
''')
    
    with open(os.path.join(example4_path, 'core.py'), 'w', encoding='utf-8') as f:
        f.write('''
# 核心模块
class CoreClass:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello from {self.name}"
    
    def __str__(self):
        return f"CoreClass({self.name})"
''')
    
    with open(os.path.join(example4_path, 'helpers.py'), 'w', encoding='utf-8') as f:
        f.write('''
# 辅助函数模块
def helper_function(data):
    """辅助函数"""
    if isinstance(data, str):
        return data.strip().title()
    elif isinstance(data, (list, tuple)):
        return len(data)
    else:
        return str(data)
''')
    
    print("创建示例4：复杂的__init__.py包")
    print("\n所有示例包已创建完成！")

def demonstrate_empty_init():
    """
    演示空__init__.py的行为
    """
    print("\n=== 空__init__.py的行为 ===")
    
    # 添加路径
    base_path = os.path.dirname(__file__)
    examples_path = os.path.join(base_path, 'init_examples')
    if examples_path not in sys.path:
        sys.path.insert(0, examples_path)
    
    try:
        print("\n导入空__init__.py包:")
        import empty_package
        print(f"包名: {empty_package.__name__}")
        print(f"包文件: {empty_package.__file__}")
        
        # 导入包中的模块
        from empty_package import module1
        result = module1.hello()
        print(f"模块函数调用结果: {result}")
        print(f"模块版本: {module1.VERSION}")
        
    except ImportError as e:
        print(f"导入失败: {e}")

def demonstrate_init_with_code():
    """
    演示带初始化代码的__init__.py
    """
    print("\n=== 带初始化代码的__init__.py ===")
    
    try:
        print("\n导入带初始化代码的包:")
        import init_package
        
        print(f"\n包级别变量:")
        print(f"  PACKAGE_NAME: {init_package.PACKAGE_NAME}")
        print(f"  VERSION: {init_package.VERSION}")
        
        print(f"\n包级别函数:")
        info = init_package.get_package_info()
        print(f"  get_package_info(): {info}")
        
        # 使用包中的模块
        from init_package import utils
        formatted = utils.format_text("hello world")
        total = utils.calculate_sum([1, 2, 3, 4, 5])
        print(f"\n模块函数:")
        print(f"  format_text('hello world'): {formatted}")
        print(f"  calculate_sum([1,2,3,4,5]): {total}")
        
    except ImportError as e:
        print(f"导入失败: {e}")

def demonstrate_all_variable():
    """
    演示__all__变量的使用
    """
    print("\n=== __all__变量的使用 ===")
    
    try:
        print("\n1. 导入controlled_package包:")
        import controlled_package
        
        print(f"\n2. 查看__all__定义:")
        if hasattr(controlled_package, '__all__'):
            print(f"   __all__ = {controlled_package.__all__}")
        
        print(f"\n3. 使用from package import *:")
        # 注意：在函数内部使用from ... import *会有限制
        # 这里我们手动演示__all__的效果
        available_items = []
        for item in controlled_package.__all__:
            if hasattr(controlled_package, item):
                available_items.append(item)
        
        print(f"   可导入的项目: {available_items}")
        
        print(f"\n4. 使用导入的函数:")
        result1 = controlled_package.add(10, 20)
        result2 = controlled_package.multiply(5, 6)
        result3 = controlled_package.reverse("Python")
        version = controlled_package.get_version()
        
        print(f"   add(10, 20) = {result1}")
        print(f"   multiply(5, 6) = {result2}")
        print(f"   reverse('Python') = {result3}")
        print(f"   get_version() = {version}")
        
        print(f"\n5. 注意：capitalize函数不在__all__中，但仍可直接访问:")
        # capitalize不在__all__中，但仍然可以访问
        if hasattr(controlled_package, 'capitalize'):
            result4 = controlled_package.capitalize("hello")
            print(f"   capitalize('hello') = {result4}")
        else:
            print("   capitalize函数不可直接访问")
        
    except ImportError as e:
        print(f"导入失败: {e}")

def demonstrate_complex_init():
    """
    演示复杂的__init__.py
    """
    print("\n=== 复杂的__init__.py ===")
    
    try:
        print("\n导入复杂包:")
        import complex_package
        
        print(f"\n包信息:")
        info = complex_package.get_info()
        for key, value in info.items():
            print(f"  {key}: {value}")
        
        print(f"\n使用核心类:")
        if complex_package.CORE_AVAILABLE:
            core = complex_package.CoreClass("测试实例")
            print(f"  创建实例: {core}")
            print(f"  调用方法: {core.greet()}")
        
        print(f"\n使用辅助函数:")
        result1 = complex_package.helper_function("  hello world  ")
        result2 = complex_package.helper_function([1, 2, 3, 4, 5])
        result3 = complex_package.helper_function(42)
        
        print(f"  helper_function('  hello world  ') = '{result1}'")
        print(f"  helper_function([1,2,3,4,5]) = {result2}")
        print(f"  helper_function(42) = '{result3}'")
        
        print(f"\n配置包:")
        print(f"  当前配置: {complex_package.CONFIG}")
        complex_package.configure(debug=True, log_level='DEBUG')
        
    except ImportError as e:
        print(f"导入失败: {e}")

def show_init_best_practices():
    """
    展示__init__.py的最佳实践
    """
    print("\n=== __init__.py最佳实践 ===")
    
    practices = [
        "1. 保持简洁：避免在__init__.py中放置复杂的逻辑",
        "2. 明确导入：使用__all__明确定义公共接口",
        "3. 延迟导入：对于大型模块，考虑延迟导入以提高性能",
        "4. 版本信息：在__init__.py中定义版本和元信息",
        "5. 错误处理：妥善处理导入错误，提供友好的错误信息",
        "6. 文档字符串：为包提供清晰的文档说明",
        "7. 向后兼容：谨慎修改__init__.py，保持API稳定性",
        "8. 避免循环导入：注意模块间的依赖关系"
    ]
    
    for practice in practices:
        print(f"   {practice}")

def cleanup_examples():
    """
    清理示例文件
    """
    import shutil
    
    base_path = os.path.dirname(__file__)
    examples_path = os.path.join(base_path, 'init_examples')
    
    if os.path.exists(examples_path):
        try:
            shutil.rmtree(examples_path)
            print(f"\n已清理示例目录: {examples_path}")
        except Exception as e:
            print(f"清理失败: {e}")
    else:
        print("\n示例目录不存在，无需清理")

def main():
    """
    主函数：演示__init__.py文件的作用和使用
    """
    print("__init__.py文件的作用和使用")
    print("=" * 50)
    
    # 1. 演示__init__.py文件的作用
    demonstrate_init_file_purpose()
    
    # 2. 创建示例
    create_init_examples()
    
    # 3. 演示空__init__.py
    demonstrate_empty_init()
    
    # 4. 演示带初始化代码的__init__.py
    demonstrate_init_with_code()
    
    # 5. 演示__all__变量
    demonstrate_all_variable()
    
    # 6. 演示复杂的__init__.py
    demonstrate_complex_init()
    
    # 7. 最佳实践
    show_init_best_practices()
    
    print("\n=== 学习小结 ===")
    print("1. __init__.py使目录成为Python包")
    print("2. 包被导入时会执行__init__.py中的代码")
    print("3. __all__变量控制from package import *的行为")
    print("4. 可以在__init__.py中定义包级别的变量和函数")
    print("5. __init__.py可以简化包的导入接口")
    print("6. 遵循最佳实践，保持__init__.py简洁明了")
    
    print("\n注意：示例包已创建在init_examples目录下")
    print("如需清理，请调用cleanup_examples()函数")

if __name__ == "__main__":
    main()