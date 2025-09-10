#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
包的基本概念和结构

包（Package）是一种组织Python模块的方式，它是一个包含多个模块的目录。
包的主要作用是避免模块名冲突，并提供更好的代码组织结构。

学习要点：
1. 包的定义和作用
2. 包的目录结构
3. __init__.py文件的重要性
4. 包与模块的区别
"""

import os
import sys

def demonstrate_package_concept():
    """
    演示包的基本概念
    """
    print("=== 包的基本概念 ===")
    print("\n1. 什么是包？")
    print("   - 包是一个包含多个模块的目录")
    print("   - 包必须包含一个__init__.py文件（可以为空）")
    print("   - 包可以包含子包，形成层次结构")
    
    print("\n2. 包的作用：")
    print("   - 避免模块名冲突")
    print("   - 提供更好的代码组织结构")
    print("   - 支持分层的模块命名空间")
    
    print("\n3. 包与模块的区别：")
    print("   - 模块：单个.py文件")
    print("   - 包：包含__init__.py的目录，可包含多个模块")

def show_package_structure():
    """
    展示典型的包结构
    """
    print("\n=== 典型的包结构 ===")
    structure = """
    mypackage/                 # 包目录
    ├── __init__.py           # 包初始化文件（必需）
    ├── module1.py            # 模块1
    ├── module2.py            # 模块2
    ├── subpackage/           # 子包
    │   ├── __init__.py       # 子包初始化文件
    │   ├── submodule1.py     # 子模块1
    │   └── submodule2.py     # 子模块2
    └── utils/                # 工具包
        ├── __init__.py       # 工具包初始化文件
        ├── helpers.py        # 辅助函数
        └── constants.py      # 常量定义
    """
    print(structure)

def create_example_package():
    """
    创建一个示例包结构
    """
    print("\n=== 创建示例包结构 ===")
    
    # 定义包结构
    package_structure = {
        'example_package': {
            '__init__.py': '# 这是example_package包的初始化文件\nprint("正在导入example_package包")',
            'math_utils.py': '''
# 数学工具模块
def add(a, b):
    """加法函数"""
    return a + b

def multiply(a, b):
    """乘法函数"""
    return a * b

def factorial(n):
    """计算阶乘"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)
''',
            'string_utils.py': '''
# 字符串工具模块
def reverse_string(s):
    """反转字符串"""
    return s[::-1]

def capitalize_words(s):
    """首字母大写"""
    return ' '.join(word.capitalize() for word in s.split())

def count_words(s):
    """统计单词数量"""
    return len(s.split())
'''
        }
    }
    
    # 创建包目录和文件
    base_path = os.path.dirname(__file__)
    
    for package_name, files in package_structure.items():
        package_path = os.path.join(base_path, package_name)
        
        # 创建包目录
        if not os.path.exists(package_path):
            os.makedirs(package_path)
            print(f"创建包目录: {package_path}")
        
        # 创建文件
        for filename, content in files.items():
            file_path = os.path.join(package_path, filename)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"创建文件: {file_path}")
    
    print("\n示例包结构创建完成！")
    return os.path.join(base_path, 'example_package')

def demonstrate_package_import(package_path):
    """
    演示包的导入
    """
    print("\n=== 包的导入演示 ===")
    
    # 将包路径添加到sys.path
    parent_path = os.path.dirname(package_path)
    if parent_path not in sys.path:
        sys.path.insert(0, parent_path)
    
    try:
        # 导入整个包
        print("\n1. 导入整个包:")
        print("   import example_package")
        import example_package
        
        # 导入包中的模块
        print("\n2. 导入包中的模块:")
        print("   from example_package import math_utils")
        from example_package import math_utils
        
        # 使用导入的模块
        print("\n3. 使用导入的模块:")
        result1 = math_utils.add(5, 3)
        result2 = math_utils.multiply(4, 6)
        result3 = math_utils.factorial(5)
        
        print(f"   math_utils.add(5, 3) = {result1}")
        print(f"   math_utils.multiply(4, 6) = {result2}")
        print(f"   math_utils.factorial(5) = {result3}")
        
        # 导入特定函数
        print("\n4. 导入特定函数:")
        print("   from example_package.string_utils import reverse_string, capitalize_words")
        from example_package.string_utils import reverse_string, capitalize_words
        
        text = "hello world python"
        reversed_text = reverse_string(text)
        capitalized_text = capitalize_words(text)
        
        print(f"   原文本: '{text}'")
        print(f"   反转后: '{reversed_text}'")
        print(f"   首字母大写: '{capitalized_text}'")
        
    except ImportError as e:
        print(f"导入错误: {e}")
    except Exception as e:
        print(f"其他错误: {e}")

def show_package_attributes():
    """
    展示包的属性
    """
    print("\n=== 包的属性 ===")
    
    try:
        import example_package
        
        print("\n包的常用属性:")
        print(f"   __name__: {example_package.__name__}")
        print(f"   __file__: {getattr(example_package, '__file__', 'N/A')}")
        print(f"   __path__: {getattr(example_package, '__path__', 'N/A')}")
        print(f"   __package__: {getattr(example_package, '__package__', 'N/A')}")
        
        # 显示包中的内容
        print("\n包中的内容:")
        for attr in dir(example_package):
            if not attr.startswith('_'):
                print(f"   {attr}")
                
    except ImportError:
        print("请先运行create_example_package()创建示例包")

def cleanup_example_package():
    """
    清理示例包（可选）
    """
    import shutil
    
    base_path = os.path.dirname(__file__)
    package_path = os.path.join(base_path, 'example_package')
    
    if os.path.exists(package_path):
        try:
            shutil.rmtree(package_path)
            print(f"\n已清理示例包: {package_path}")
        except Exception as e:
            print(f"清理失败: {e}")
    else:
        print("\n示例包不存在，无需清理")

def main():
    """
    主函数：演示包的基本概念
    """
    print("Python包的基本概念和结构")
    print("=" * 50)
    
    # 1. 演示包的基本概念
    demonstrate_package_concept()
    
    # 2. 展示包结构
    show_package_structure()
    
    # 3. 创建示例包
    package_path = create_example_package()
    
    # 4. 演示包的导入
    demonstrate_package_import(package_path)
    
    # 5. 展示包的属性
    show_package_attributes()
    
    print("\n=== 学习小结 ===")
    print("1. 包是包含__init__.py文件的目录")
    print("2. 包可以包含多个模块和子包")
    print("3. 包提供了命名空间，避免模块名冲突")
    print("4. 可以通过import语句导入包和包中的模块")
    print("5. 包有自己的属性，如__name__, __file__, __path__等")
    
    # 询问是否清理示例包
    print("\n注意：示例包已创建在当前目录下")
    print("如需清理，请调用cleanup_example_package()函数")

if __name__ == "__main__":
    main()