# 04. __name__变量的作用

## 学习目标

- 理解__name__变量的含义和作用
- 掌握if __name__ == '__main__'的使用
- 学会区分模块导入和直接执行
- 了解模块执行的不同方式

## __name__变量概述

`__name__`是Python中的一个特殊变量，它表示当前模块的名称。当模块被直接执行时，`__name__`的值为`'__main__'`；当模块被导入时，`__name__`的值为模块的实际名称。

## 基本概念和用法

### __name__变量的值

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
__name__变量详解

本模块演示__name__变量在不同情况下的值和用法
"""

import sys
import os

def show_name_info():
    """显示__name__变量的信息"""
    print("=== __name__变量信息 ===")
    print(f"当前模块的__name__值: {__name__}")
    print(f"__name__的类型: {type(__name__)}")
    print(f"模块文件路径: {__file__ if '__file__' in globals() else '未定义'}")
    
    # 显示执行方式
    if __name__ == '__main__':
        print("执行方式: 直接执行 (python script.py)")
    else:
        print(f"执行方式: 作为模块导入 (import {__name__})")
    
    print()

def demonstrate_name_behavior():
    """演示__name__变量的行为"""
    print("=== __name__变量行为演示 ===")
    
    # 显示当前状态
    print(f"1. 当前__name__的值: '{__name__}'")
    
    # 解释不同的值
    print("\n2. __name__可能的值:")
    print("   - '__main__': 当前模块被直接执行")
    print("   - '模块名': 当前模块被其他模块导入")
    print("   - '包名.模块名': 模块在包中被导入")
    
    # 显示相关的特殊变量
    print("\n3. 相关的特殊变量:")
    special_vars = ['__name__', '__file__', '__package__', '__doc__', '__spec__']
    
    for var_name in special_vars:
        if var_name in globals():
            value = globals()[var_name]
            if isinstance(value, str) and len(value) > 50:
                value = value[:50] + "..."
            print(f"   {var_name}: {value}")
        else:
            print(f"   {var_name}: 未定义")
    
    print()

def create_example_modules():
    """创建示例模块用于演示"""
    print("=== 创建示例模块 ===")
    
    # 创建测试目录
    test_dir = '/tmp/name_test'
    os.makedirs(test_dir, exist_ok=True)
    
    # 示例模块1: 简单模块
    module1_content = '''
#!/usr/bin/env python3
"""示例模块1 - 演示__name__变量"""

print(f"模块1: __name__ = {__name__}")

def module1_function():
    return f"来自模块1的函数，__name__ = {__name__}"

if __name__ == '__main__':
    print("模块1被直接执行")
    print(f"执行模块1的测试: {module1_function()}")
else:
    print("模块1被导入")
'''
    
    module1_path = os.path.join(test_dir, 'example_module1.py')
    with open(module1_path, 'w') as f:
        f.write(module1_content)
    
    # 示例模块2: 带有类的模块
    module2_content = '''
#!/usr/bin/env python3
"""示例模块2 - 带有类定义"""

print(f"模块2加载: __name__ = {__name__}")

class ExampleClass:
    def __init__(self):
        self.module_name = __name__
    
    def get_info(self):
        return f"类实例来自模块: {self.module_name}"

def main():
    """模块的主函数"""
    print("=== 模块2主函数 ===")
    obj = ExampleClass()
    print(obj.get_info())
    print(f"当前__name__: {__name__}")

if __name__ == '__main__':
    print("模块2被直接执行，调用main()函数")
    main()
else:
    print(f"模块2被导入到 {__name__}")
'''
    
    module2_path = os.path.join(test_dir, 'example_module2.py')
    with open(module2_path, 'w') as f:
        f.write(module2_content)
    
    # 示例模块3: 包结构
    package_dir = os.path.join(test_dir, 'example_package')
    os.makedirs(package_dir, exist_ok=True)
    
    # 包的__init__.py
    init_content = '''
"""示例包"""
print(f"包初始化: __name__ = {__name__}")

__version__ = "1.0.0"
'''
    
    init_path = os.path.join(package_dir, '__init__.py')
    with open(init_path, 'w') as f:
        f.write(init_content)
    
    # 包中的模块
    package_module_content = '''
"""包中的模块"""
print(f"包模块加载: __name__ = {__name__}")

def package_function():
    return f"包函数，__name__ = {__name__}"

if __name__ == '__main__':
    print("包模块被直接执行")
    print(package_function())
else:
    print(f"包模块被导入: {__name__}")
'''
    
    package_module_path = os.path.join(package_dir, 'submodule.py')
    with open(package_module_path, 'w') as f:
        f.write(package_module_content)
    
    print(f"创建了示例模块:")
    print(f"  {module1_path}")
    print(f"  {module2_path}")
    print(f"  {package_dir}/")
    print(f"    __init__.py")
    print(f"    submodule.py")
    
    return test_dir

def test_module_import(test_dir):
    """测试模块导入时的__name__行为"""
    print("\n=== 测试模块导入 ===")
    
    # 添加到搜索路径
    if test_dir not in sys.path:
        sys.path.insert(0, test_dir)
    
    try:
        print("1. 导入示例模块1:")
        import example_module1
        print(f"   导入后，模块的__name__: {example_module1.__name__}")
        print(f"   调用模块函数: {example_module1.module1_function()}")
        
        print("\n2. 导入示例模块2:")
        import example_module2
        print(f"   导入后，模块的__name__: {example_module2.__name__}")
        obj = example_module2.ExampleClass()
        print(f"   类实例信息: {obj.get_info()}")
        
        print("\n3. 导入包和包模块:")
        import example_package
        print(f"   包的__name__: {example_package.__name__}")
        
        from example_package import submodule
        print(f"   包模块的__name__: {submodule.__name__}")
        print(f"   包函数调用: {submodule.package_function()}")
        
    except ImportError as e:
        print(f"导入失败: {e}")
    
    # 清理
    if test_dir in sys.path:
        sys.path.remove(test_dir)

def demonstrate_execution_methods():
    """演示不同的执行方法"""
    print("\n=== 不同执行方法的__name__值 ===")
    
    execution_methods = [
        ("直接执行", "python script.py", "__main__"),
        ("模块执行", "python -m module_name", "__main__"),
        ("导入执行", "import module_name", "module_name"),
        ("交互式导入", ">>> import module_name", "module_name"),
        ("exec执行", "exec(open('script.py').read())", "__main__"),
        ("runpy执行", "runpy.run_path('script.py')", "<run_path>"),
    ]
    
    print("执行方法对比:")
    print(f"{'方法':<12} {'命令':<30} {'__name__值':<15}")
    print("-" * 60)
    
    for method, command, name_value in execution_methods:
        print(f"{method:<12} {command:<30} {name_value:<15}")
    
    print()

def practical_examples():
    """实际应用示例"""
    print("=== 实际应用示例 ===")
    
    print("1. 模块既可导入又可执行:")
    print("```python")
    print("def main_function():")
    print("    # 主要功能")
    print("    pass")
    print("")
    print("if __name__ == '__main__':")
    print("    main_function()")
    print("```")
    
    print("\n2. 测试代码分离:")
    print("```python")
    print("def my_function(x):")
    print("    return x * 2")
    print("")
    print("if __name__ == '__main__':")
    print("    # 测试代码")
    print("    assert my_function(5) == 10")
    print("    print('所有测试通过')")
    print("```")
    
    print("\n3. 命令行工具:")
    print("```python")
    print("import argparse")
    print("")
    print("def main():")
    print("    parser = argparse.ArgumentParser()")
    print("    # 添加参数...")
    print("    args = parser.parse_args()")
    print("    # 处理逻辑...")
    print("")
    print("if __name__ == '__main__':")
    print("    main()")
    print("```")
    
    print("\n4. 配置和初始化:")
    print("```python")
    print("# 模块级配置")
    print("CONFIG = {'debug': False}")
    print("")
    print("if __name__ == '__main__':")
    print("    # 直接执行时的特殊配置")
    print("    CONFIG['debug'] = True")
    print("    print('调试模式启用')")
    print("```")

def advanced_name_usage():
    """高级__name__用法"""
    print("\n=== 高级__name__用法 ===")
    
    # 动态获取模块名
    current_module = sys.modules[__name__]
    print(f"1. 动态获取当前模块: {current_module}")
    
    # 检查调用栈
    import inspect
    frame = inspect.currentframe()
    if frame and frame.f_back:
        caller_name = frame.f_back.f_globals.get('__name__', 'unknown')
        print(f"2. 调用者模块: {caller_name}")
    
    # 模块名解析
    module_parts = __name__.split('.')
    print(f"3. 模块名解析: {module_parts}")
    if len(module_parts) > 1:
        print(f"   包名: {'.'.join(module_parts[:-1])}")
        print(f"   模块名: {module_parts[-1]}")
    
    # 条件导入
    print("\n4. 条件导入示例:")
    if __name__ == '__main__':
        print("   直接执行时导入额外的调试模块")
        # import pdb; pdb.set_trace()  # 调试器
        # import cProfile  # 性能分析
    else:
        print("   作为模块导入时的正常行为")

def cleanup_examples(test_dir):
    """清理示例文件"""
    import shutil
    try:
        shutil.rmtree(test_dir)
        print(f"\n清理测试目录: {test_dir}")
    except OSError:
        pass

# 模块级代码 - 总是执行
print(f"模块加载: {__name__}")

# 主执行块
if __name__ == '__main__':
    print("=== __name__变量演示程序 ===")
    print(f"当前模块被直接执行，__name__ = '{__name__}'")
    print()
    
    # 执行所有演示
    show_name_info()
    demonstrate_name_behavior()
    
    # 创建和测试示例模块
    test_directory = create_example_modules()
    test_module_import(test_directory)
    
    # 其他演示
    demonstrate_execution_methods()
    practical_examples()
    advanced_name_usage()
    
    # 清理
    cleanup_examples(test_directory)
    
    print("\n=== 演示完成 ===")
else:
    print(f"模块 {__name__} 被导入")
```

## 常见使用模式

### 1. 基本模式

```python
# 模块功能代码
def my_function():
    return "Hello, World!"

class MyClass:
    pass

# 直接执行时的代码
if __name__ == '__main__':
    # 测试代码或主程序逻辑
    result = my_function()
    print(result)
```

### 2. 命令行工具模式

```python
import argparse
import sys

def process_data(input_file, output_file):
    """处理数据的主要函数"""
    # 实际的数据处理逻辑
    pass

def main():
    """命令行入口点"""
    parser = argparse.ArgumentParser(description='数据处理工具')
    parser.add_argument('input', help='输入文件')
    parser.add_argument('output', help='输出文件')
    parser.add_argument('--verbose', '-v', action='store_true', help='详细输出')
    
    args = parser.parse_args()
    
    if args.verbose:
        print(f"处理文件: {args.input} -> {args.output}")
    
    process_data(args.input, args.output)

if __name__ == '__main__':
    main()
```

### 3. 测试模式

```python
def add(a, b):
    """加法函数"""
    return a + b

def multiply(a, b):
    """乘法函数"""
    return a * b

def run_tests():
    """运行测试"""
    # 测试add函数
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("✓ add函数测试通过")
    
    # 测试multiply函数
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    print("✓ multiply函数测试通过")
    
    print("所有测试通过！")

if __name__ == '__main__':
    run_tests()
```

### 4. 配置模式

```python
# 默认配置
DEBUG = False
LOG_LEVEL = 'INFO'
DATABASE_URL = 'sqlite:///app.db'

def get_config():
    """获取配置"""
    return {
        'debug': DEBUG,
        'log_level': LOG_LEVEL,
        'database_url': DATABASE_URL
    }

if __name__ == '__main__':
    # 直接执行时启用调试模式
    DEBUG = True
    LOG_LEVEL = 'DEBUG'
    print("调试模式启用")
    print(f"当前配置: {get_config()}")
```

## 模块执行的不同方式

### 1. 直接执行

```bash
# __name__ == '__main__'
python my_module.py
```

### 2. 模块方式执行

```bash
# __name__ == '__main__'
python -m my_module
```

### 3. 导入执行

```python
# __name__ == 'my_module'
import my_module
```

### 4. 动态执行

```python
import runpy

# __name__ == '<run_path>'
runpy.run_path('my_module.py')

# __name__ == '__main__'
runpy.run_module('my_module', run_name='__main__')
```

## 调试和诊断

### 检查模块状态

```python
import sys
import inspect

def debug_module_info():
    """调试模块信息"""
    print("=== 模块调试信息 ===")
    
    # 基本信息
    print(f"__name__: {__name__}")
    print(f"__file__: {globals().get('__file__', 'N/A')}")
    print(f"__package__: {globals().get('__package__', 'N/A')}")
    
    # 调用栈信息
    frame = inspect.currentframe()
    if frame:
        print(f"当前函数: {frame.f_code.co_name}")
        print(f"文件名: {frame.f_code.co_filename}")
        print(f"行号: {frame.f_lineno}")
    
    # 模块搜索路径
    print(f"模块在sys.modules中: {'__main__' in sys.modules}")
    if __name__ in sys.modules:
        print(f"模块对象: {sys.modules[__name__]}")

if __name__ == '__main__':
    debug_module_info()
```

### 跟踪模块加载

```python
import sys
import importlib.util

class ModuleTracker:
    """模块加载跟踪器"""
    
    def __init__(self):
        self.loaded_modules = set(sys.modules.keys())
    
    def track_new_imports(self):
        """跟踪新导入的模块"""
        current_modules = set(sys.modules.keys())
        new_modules = current_modules - self.loaded_modules
        
        if new_modules:
            print(f"新导入的模块: {sorted(new_modules)}")
            for module_name in sorted(new_modules):
                module = sys.modules[module_name]
                if hasattr(module, '__file__') and module.__file__:
                    print(f"  {module_name}: {module.__file__}")
        
        self.loaded_modules = current_modules
        return new_modules

def trace_import_behavior():
    """跟踪导入行为"""
    tracker = ModuleTracker()
    
    print("导入前的模块状态:")
    print(f"已加载模块数量: {len(sys.modules)}")
    
    # 模拟导入
    print("\n导入json模块...")
    import json
    tracker.track_new_imports()
    
    print(f"json模块的__name__: {json.__name__}")

if __name__ == '__main__':
    trace_import_behavior()
```

## 最佳实践

### 1. 标准结构

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模块文档字符串
"""

# 导入语句
import sys
import os

# 常量定义
CONSTANT = "value"

# 函数定义
def function1():
    pass

def function2():
    pass

# 类定义
class MyClass:
    pass

# 主函数
def main():
    """主函数"""
    pass

# 执行块
if __name__ == '__main__':
    main()
```

### 2. 错误处理

```python
def main():
    try:
        # 主要逻辑
        pass
    except KeyboardInterrupt:
        print("\n程序被用户中断")
        return 1
    except Exception as e:
        print(f"错误: {e}")
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
```

### 3. 日志配置

```python
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    logger.info("程序开始执行")
    # 主要逻辑
    logger.info("程序执行完成")

if __name__ == '__main__':
    # 直接执行时启用调试日志
    logging.getLogger().setLevel(logging.DEBUG)
    main()
```

## 学习要点

1. **理解__name__的含义**：模块名称的动态标识
2. **掌握执行检测**：区分导入和直接执行
3. **合理组织代码**：分离可导入功能和执行逻辑
4. **命令行工具设计**：使用main函数模式
5. **测试代码分离**：在执行块中放置测试
6. **调试和诊断**：利用__name__进行调试

## 注意事项

1. **避免副作用**：模块导入时不应有副作用
2. **性能考虑**：避免在模块级放置耗时操作
3. **跨平台兼容**：注意路径和编码问题
4. **文档完整**：为模块和函数提供完整文档
5. **错误处理**：妥善处理异常情况

通过掌握`__name__`变量的使用，你可以编写既可以作为模块导入，又可以独立执行的Python代码，这是Python编程的重要技能。