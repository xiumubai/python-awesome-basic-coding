#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
包的导入和使用方法

本模块演示Python包的各种导入方式和使用方法，包括：
- 不同的import语句形式
- 导入包、模块和特定对象
- 使用别名导入
- 条件导入和动态导入

学习要点：
1. 基本导入语法
2. 不同导入方式的区别
3. 导入的最佳实践
4. 动态导入和条件导入
5. 导入路径和搜索机制
"""

import os
import sys
import importlib
from types import ModuleType

def demonstrate_import_syntax():
    """
    演示各种导入语法
    """
    print("=== 包导入语法 ===")
    
    syntax_examples = [
        "1. 导入整个包：",
        "   import package_name",
        "   使用：package_name.module.function()",
        "",
        "2. 导入包中的模块：",
        "   from package_name import module_name",
        "   使用：module_name.function()",
        "",
        "3. 导入模块中的特定对象：",
        "   from package_name.module_name import function_name",
        "   使用：function_name()",
        "",
        "4. 导入多个对象：",
        "   from package_name.module_name import func1, func2, Class1",
        "   使用：func1(), func2(), Class1()",
        "",
        "5. 使用别名导入：",
        "   import package_name as pkg",
        "   from package_name import module_name as mod",
        "   from package_name.module_name import function_name as func",
        "",
        "6. 导入所有公共对象：",
        "   from package_name import *",
        "   注意：不推荐使用，可能导致命名冲突",
        "",
        "7. 导入子包：",
        "   from package_name.subpackage import module_name",
        "   import package_name.subpackage.module_name"
    ]
    
    for line in syntax_examples:
        print(line)

def create_import_demo_package():
    """
    创建用于演示导入的包结构
    """
    print("\n=== 创建导入演示包 ===")
    
    base_path = os.path.dirname(__file__)
    demo_path = os.path.join(base_path, 'import_demo')
    
    # 创建主包
    os.makedirs(demo_path, exist_ok=True)
    
    # 主包的__init__.py
    with open(os.path.join(demo_path, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write('''
# import_demo包的初始化文件
print("正在加载import_demo包")

# 包级别的变量
__version__ = "1.0.0"
__author__ = "Python学习者"

# 从子模块导入常用功能
from .calculator import Calculator
from .text_processor import process_text, reverse_text
from .utilities import get_timestamp, format_number

# 定义公共接口
__all__ = [
    'Calculator',
    'process_text',
    'reverse_text', 
    'get_timestamp',
    'format_number',
    'get_package_info'
]

def get_package_info():
    """获取包信息"""
    return {
        'name': __name__,
        'version': __version__,
        'author': __author__
    }
''')
    
    # 计算器模块
    with open(os.path.join(demo_path, 'calculator.py'), 'w', encoding='utf-8') as f:
        f.write('''
# 计算器模块
class Calculator:
    """简单计算器类"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """加法"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """减法"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """乘法"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """除法"""
        if b == 0:
            raise ValueError("除数不能为零")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        """获取计算历史"""
        return self.history.copy()
    
    def clear_history(self):
        """清空历史"""
        self.history.clear()

# 模块级别的函数
def quick_add(a, b):
    """快速加法"""
    return a + b

def quick_multiply(a, b):
    """快速乘法"""
    return a * b
''')
    
    # 文本处理模块
    with open(os.path.join(demo_path, 'text_processor.py'), 'w', encoding='utf-8') as f:
        f.write('''
# 文本处理模块
import re
from collections import Counter

def process_text(text):
    """处理文本：清理、标准化"""
    # 移除多余空格
    text = re.sub(r'\s+', ' ', text.strip())
    return text

def reverse_text(text):
    """反转文本"""
    return text[::-1]

def count_words(text):
    """统计单词数量"""
    words = text.lower().split()
    return Counter(words)

def capitalize_sentences(text):
    """句子首字母大写"""
    sentences = text.split('. ')
    capitalized = [s.capitalize() for s in sentences]
    return '. '.join(capitalized)

class TextAnalyzer:
    """文本分析器"""
    
    def __init__(self, text):
        self.text = text
        self.words = text.lower().split()
    
    def word_count(self):
        """单词总数"""
        return len(self.words)
    
    def unique_words(self):
        """唯一单词数"""
        return len(set(self.words))
    
    def most_common_words(self, n=5):
        """最常见的n个单词"""
        counter = Counter(self.words)
        return counter.most_common(n)
    
    def average_word_length(self):
        """平均单词长度"""
        if not self.words:
            return 0
        total_length = sum(len(word) for word in self.words)
        return total_length / len(self.words)
''')
    
    # 工具模块
    with open(os.path.join(demo_path, 'utilities.py'), 'w', encoding='utf-8') as f:
        f.write('''
# 工具模块
import datetime
import random
import string

def get_timestamp():
    """获取当前时间戳"""
    return datetime.datetime.now().isoformat()

def format_number(number, decimal_places=2):
    """格式化数字"""
    return f"{number:.{decimal_places}f}"

def generate_random_string(length=10):
    """生成随机字符串"""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def is_prime(n):
    """检查是否为质数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

class Logger:
    """简单日志记录器"""
    
    def __init__(self, name):
        self.name = name
        self.logs = []
    
    def log(self, message, level="INFO"):
        """记录日志"""
        timestamp = get_timestamp()
        log_entry = f"[{timestamp}] {level}: {message}"
        self.logs.append(log_entry)
        print(f"[{self.name}] {log_entry}")
    
    def get_logs(self):
        """获取所有日志"""
        return self.logs.copy()
''')
    
    # 创建子包
    subpackage_path = os.path.join(demo_path, 'advanced')
    os.makedirs(subpackage_path, exist_ok=True)
    
    # 子包的__init__.py
    with open(os.path.join(subpackage_path, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write('''
# advanced子包
print("正在加载import_demo.advanced子包")

from .data_structures import Stack, Queue
from .algorithms import bubble_sort, binary_search

__all__ = ['Stack', 'Queue', 'bubble_sort', 'binary_search']
''')
    
    # 数据结构模块
    with open(os.path.join(subpackage_path, 'data_structures.py'), 'w', encoding='utf-8') as f:
        f.write('''
# 数据结构模块
class Stack:
    """栈数据结构"""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """入栈"""
        self.items.append(item)
    
    def pop(self):
        """出栈"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self.items.pop()
    
    def peek(self):
        """查看栈顶元素"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self.items[-1]
    
    def is_empty(self):
        """检查栈是否为空"""
        return len(self.items) == 0
    
    def size(self):
        """获取栈大小"""
        return len(self.items)

class Queue:
    """队列数据结构"""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """入队"""
        self.items.insert(0, item)
    
    def dequeue(self):
        """出队"""
        if self.is_empty():
            raise IndexError("队列为空")
        return self.items.pop()
    
    def is_empty(self):
        """检查队列是否为空"""
        return len(self.items) == 0
    
    def size(self):
        """获取队列大小"""
        return len(self.items)
''')
    
    # 算法模块
    with open(os.path.join(subpackage_path, 'algorithms.py'), 'w', encoding='utf-8') as f:
        f.write('''
# 算法模块
def bubble_sort(arr):
    """冒泡排序"""
    arr = arr.copy()  # 不修改原数组
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, target):
    """二分查找"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # 未找到

def quick_sort(arr):
    """快速排序"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)
''')
    
    print(f"创建导入演示包: {demo_path}")
    print("包结构:")
    print("import_demo/")
    print("├── __init__.py")
    print("├── calculator.py")
    print("├── text_processor.py")
    print("├── utilities.py")
    print("└── advanced/")
    print("    ├── __init__.py")
    print("    ├── data_structures.py")
    print("    └── algorithms.py")
    
    return demo_path

def demonstrate_basic_imports():
    """
    演示基本导入方式
    """
    print("\n=== 基本导入方式演示 ===")
    
    # 添加路径
    base_path = os.path.dirname(__file__)
    if base_path not in sys.path:
        sys.path.insert(0, base_path)
    
    try:
        print("\n1. 导入整个包:")
        print("   import import_demo")
        import import_demo
        
        print(f"   包信息: {import_demo.get_package_info()}")
        
        print("\n2. 导入包中的模块:")
        print("   from import_demo import calculator")
        from import_demo import calculator
        
        calc = calculator.Calculator()
        result = calc.add(10, 5)
        print(f"   Calculator().add(10, 5) = {result}")
        
        print("\n3. 导入特定类:")
        print("   from import_demo.calculator import Calculator")
        from import_demo.calculator import Calculator
        
        calc2 = Calculator()
        result2 = calc2.multiply(3, 7)
        print(f"   Calculator().multiply(3, 7) = {result2}")
        
        print("\n4. 导入多个对象:")
        print("   from import_demo.text_processor import process_text, reverse_text")
        from import_demo.text_processor import process_text, reverse_text
        
        text = "  hello   world  "
        processed = process_text(text)
        reversed_text = reverse_text(processed)
        print(f"   原文本: '{text}'")
        print(f"   处理后: '{processed}'")
        print(f"   反转后: '{reversed_text}'")
        
    except ImportError as e:
        print(f"导入错误: {e}")

def demonstrate_alias_imports():
    """
    演示别名导入
    """
    print("\n=== 别名导入演示 ===")
    
    try:
        print("\n1. 包别名:")
        print("   import import_demo as demo")
        import import_demo as demo
        
        info = demo.get_package_info()
        print(f"   demo.get_package_info(): {info}")
        
        print("\n2. 模块别名:")
        print("   from import_demo import utilities as utils")
        from import_demo import utilities as utils
        
        timestamp = utils.get_timestamp()
        formatted = utils.format_number(3.14159, 3)
        print(f"   utils.get_timestamp(): {timestamp}")
        print(f"   utils.format_number(3.14159, 3): {formatted}")
        
        print("\n3. 函数别名:")
        print("   from import_demo.utilities import generate_random_string as gen_str")
        from import_demo.utilities import generate_random_string as gen_str
        
        random_str = gen_str(8)
        print(f"   gen_str(8): {random_str}")
        
        print("\n4. 类别名:")
        print("   from import_demo.text_processor import TextAnalyzer as TA")
        from import_demo.text_processor import TextAnalyzer as TA
        
        analyzer = TA("hello world python programming")
        word_count = analyzer.word_count()
        unique_count = analyzer.unique_words()
        print(f"   TA('hello world python programming').word_count(): {word_count}")
        print(f"   TA('hello world python programming').unique_words(): {unique_count}")
        
    except ImportError as e:
        print(f"导入错误: {e}")

def demonstrate_subpackage_imports():
    """
    演示子包导入
    """
    print("\n=== 子包导入演示 ===")
    
    try:
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
        
        print("\n2. 导入子包中的模块:")
        print("   from import_demo.advanced import algorithms")
        from import_demo.advanced import algorithms
        
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr = algorithms.bubble_sort(arr)
        print(f"   原数组: {arr}")
        print(f"   冒泡排序后: {sorted_arr}")
        
        index = algorithms.binary_search(sorted_arr, 25)
        print(f"   在排序数组中查找25的位置: {index}")
        
        print("\n3. 直接导入子包中的类:")
        print("   from import_demo.advanced.data_structures import Queue")
        from import_demo.advanced.data_structures import Queue
        
        queue = Queue()
        queue.enqueue("first")
        queue.enqueue("second")
        queue.enqueue("third")
        print(f"   创建队列并添加元素")
        print(f"   队列大小: {queue.size()}")
        print(f"   出队: {queue.dequeue()}")
        
    except ImportError as e:
        print(f"导入错误: {e}")

def demonstrate_star_import():
    """
    演示星号导入（不推荐）
    """
    print("\n=== 星号导入演示（不推荐使用） ===")
    
    print("\n星号导入的问题:")
    print("1. 可能导致命名冲突")
    print("2. 使代码可读性降低")
    print("3. 难以追踪函数来源")
    print("4. 可能导入不需要的对象")
    
    print("\n更好的替代方案:")
    print("1. 明确导入需要的对象")
    print("2. 使用别名避免冲突")
    print("3. 导入模块而不是模块中的对象")
    
    # 演示__all__的作用
    try:
        import import_demo
        if hasattr(import_demo, '__all__'):
            print(f"\nimport_demo.__all__ = {import_demo.__all__}")
            print("from import_demo import * 只会导入__all__中定义的对象")
    except ImportError as e:
        print(f"导入错误: {e}")

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
        
        print("\n2. 动态获取属性:")
        # 动态获取类
        Calculator = getattr(calc_module, 'Calculator')
        calc2 = Calculator()
        result2 = calc2.subtract(50, 20)
        print(f"   动态获取Calculator类并使用: {result2}")
        
        print("\n3. 条件导入:")
        # 条件导入示例
        modules_to_try = [
            'import_demo.utilities',
            'import_demo.nonexistent',
            'import_demo.text_processor'
        ]
        
        for module_name in modules_to_try:
            try:
                module = importlib.import_module(module_name)
                print(f"   成功导入: {module_name}")
            except ImportError:
                print(f"   导入失败: {module_name}")
        
        print("\n4. 运行时导入决策:")
        # 根据条件决定导入哪个模块
        use_advanced = True
        if use_advanced:
            advanced = importlib.import_module('import_demo.advanced')
            stack = advanced.Stack()
            stack.push("动态导入的栈")
            print(f"   使用高级模块: {stack.peek()}")
        
    except ImportError as e:
        print(f"动态导入错误: {e}")
    except Exception as e:
        print(f"其他错误: {e}")

def demonstrate_import_path():
    """
    演示导入路径和搜索机制
    """
    print("\n=== 导入路径和搜索机制 ===")
    
    print("\nPython模块搜索路径 (sys.path):")
    for i, path in enumerate(sys.path[:5]):  # 只显示前5个路径
        print(f"   {i+1}. {path}")
    if len(sys.path) > 5:
        print(f"   ... 还有 {len(sys.path) - 5} 个路径")
    
    print("\n搜索顺序:")
    print("1. 当前工作目录")
    print("2. PYTHONPATH环境变量中的目录")
    print("3. Python标准库目录")
    print("4. site-packages目录（第三方包）")
    
    print("\n查看模块位置:")
    try:
        import import_demo
        print(f"   import_demo.__file__: {import_demo.__file__}")
        print(f"   import_demo.__path__: {getattr(import_demo, '__path__', 'N/A')}")
        
        from import_demo import calculator
        print(f"   calculator.__file__: {calculator.__file__}")
        
    except ImportError as e:
        print(f"导入错误: {e}")

def show_import_best_practices():
    """
    展示导入的最佳实践
    """
    print("\n=== 导入最佳实践 ===")
    
    practices = [
        "1. 导入顺序：",
        "   - 标准库模块",
        "   - 第三方库模块",
        "   - 本地应用/库模块",
        "   - 每组之间用空行分隔",
        "",
        "2. 导入风格：",
        "   - 优先使用 import module",
        "   - 避免使用 from module import *",
        "   - 使用有意义的别名",
        "",
        "3. 性能考虑：",
        "   - 避免在函数内部导入（除非必要）",
        "   - 考虑延迟导入大型模块",
        "   - 使用条件导入处理可选依赖",
        "",
        "4. 可读性：",
        "   - 明确导入需要的对象",
        "   - 使用绝对导入而非相对导入（在包外）",
        "   - 保持导入语句简洁明了",
        "",
        "5. 错误处理：",
        "   - 妥善处理ImportError",
        "   - 提供有意义的错误信息",
        "   - 考虑提供备选方案"
    ]
    
    for practice in practices:
        print(practice)

def cleanup_demo_package():
    """
    清理演示包
    """
    import shutil
    
    base_path = os.path.dirname(__file__)
    demo_path = os.path.join(base_path, 'import_demo')
    
    if os.path.exists(demo_path):
        try:
            shutil.rmtree(demo_path)
            print(f"\n已清理演示包: {demo_path}")
        except Exception as e:
            print(f"清理失败: {e}")
    else:
        print("\n演示包不存在，无需清理")

def main():
    """
    主函数：演示包的导入和使用方法
    """
    print("包的导入和使用方法")
    print("=" * 50)
    
    # 1. 演示导入语法
    demonstrate_import_syntax()
    
    # 2. 创建演示包
    create_import_demo_package()
    
    # 3. 演示基本导入
    demonstrate_basic_imports()
    
    # 4. 演示别名导入
    demonstrate_alias_imports()
    
    # 5. 演示子包导入
    demonstrate_subpackage_imports()
    
    # 6. 演示星号导入
    demonstrate_star_import()
    
    # 7. 演示动态导入
    demonstrate_dynamic_import()
    
    # 8. 演示导入路径
    demonstrate_import_path()
    
    # 9. 最佳实践
    show_import_best_practices()
    
    print("\n=== 学习小结 ===")
    print("1. 掌握各种导入语法：import, from...import")
    print("2. 合理使用别名避免命名冲突")
    print("3. 了解子包的导入方式")
    print("4. 避免使用星号导入")
    print("5. 学会使用动态导入处理复杂场景")
    print("6. 理解Python的模块搜索机制")
    print("7. 遵循导入的最佳实践")
    
    print("\n注意：演示包已创建在import_demo目录下")
    print("如需清理，请调用cleanup_demo_package()函数")

if __name__ == "__main__":
    main()