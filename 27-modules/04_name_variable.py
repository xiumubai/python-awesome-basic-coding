#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__name__变量演示

本文件演示Python中__name__变量的作用和用法，包括：
1. __name__变量的基本概念
2. 直接运行vs导入时的区别
3. if __name__ == '__main__'的用法
4. 模块的执行控制
5. 实际应用场景
6. 最佳实践

学习目标：
- 理解__name__变量的作用机制
- 掌握模块执行控制的方法
- 学会编写可执行和可导入的模块
- 了解模块初始化的最佳实践
"""

import sys
import os

# ============================================================================
# 模块级别的代码（总是会执行）
# ============================================================================

print(f"模块 {__file__} 正在被加载...")
print(f"当前 __name__ 的值: {__name__}")

# 模块级别的变量和函数定义
MODULE_NAME = "__name__变量演示模块"
MODULE_VERSION = "1.0.0"
LOAD_COUNT = 0

# 每次导入时都会执行的代码
LOAD_COUNT += 1
print(f"这是第 {LOAD_COUNT} 次加载此模块")

# ============================================================================
# 1. __name__变量的基本概念
# ============================================================================

def explain_name_variable():
    """
    解释__name__变量的基本概念
    """
    print("\n=== 1. __name__变量的基本概念 ===")
    
    print("__name__是Python的内置变量，用于标识当前模块的名称：")
    print(f"  当前模块的__name__: {__name__}")
    
    print("\n__name__的两种可能值：")
    print("  1. '__main__' - 当模块被直接运行时")
    print("  2. '模块名' - 当模块被导入时")
    
    print("\n其他相关的内置变量：")
    print(f"  __file__: {__file__}")
    print(f"  __doc__: {__doc__[:50]}..." if __doc__ else "  __doc__: None")
    
    # 检查当前的执行方式
    if __name__ == '__main__':
        print("\n当前状态: 模块被直接运行")
    else:
        print("\n当前状态: 模块被导入")

# ============================================================================
# 2. 演示不同执行方式的区别
# ============================================================================

def demonstrate_execution_modes():
    """
    演示直接运行和导入时的区别
    """
    print("\n=== 2. 执行方式演示 ===")
    
    print("执行方式检测：")
    
    if __name__ == '__main__':
        print("  ✓ 这个模块正在被直接运行")
        print("  ✓ 可以执行测试代码、示例代码等")
        print("  ✓ 通常用于模块的主要功能演示")
    else:
        print("  ✓ 这个模块正在被导入")
        print("  ✓ 只会执行函数和类的定义")
        print("  ✓ 不会执行测试或示例代码")
    
    print(f"\n模块标识信息：")
    print(f"  模块名称: {__name__}")
    print(f"  文件路径: {__file__}")
    print(f"  所在目录: {os.path.dirname(__file__)}")

# ============================================================================
# 3. 创建可执行和可导入的函数
# ============================================================================

def greet(name="World"):
    """
    问候函数 - 可以被导入使用
    """
    return f"Hello, {name}! 来自模块 {__name__}"

def calculate_factorial(n):
    """
    计算阶乘 - 可以被导入使用
    """
    if n < 0:
        raise ValueError("阶乘不能计算负数")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)

class Calculator:
    """
    计算器类 - 可以被导入使用
    """
    def __init__(self, name="Calculator"):
        self.name = name
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def get_history(self):
        return self.history.copy()

# ============================================================================
# 4. 模块测试函数（只在直接运行时执行）
# ============================================================================

def run_module_tests():
    """
    运行模块测试 - 只在直接运行时执行
    """
    print("\n=== 3. 模块功能测试 ===")
    
    # 测试问候函数
    print("\n测试问候函数：")
    print(f"  {greet()}")
    print(f"  {greet('Python')}")
    print(f"  {greet('模块学习者')}")
    
    # 测试阶乘函数
    print("\n测试阶乘函数：")
    test_numbers = [0, 1, 5, 10]
    for num in test_numbers:
        try:
            result = calculate_factorial(num)
            print(f"  {num}! = {result}")
        except ValueError as e:
            print(f"  {num}! = 错误: {e}")
    
    # 测试计算器类
    print("\n测试计算器类：")
    calc = Calculator("测试计算器")
    print(f"  创建计算器: {calc.name}")
    print(f"  5 + 3 = {calc.add(5, 3)}")
    print(f"  4 × 6 = {calc.multiply(4, 6)}")
    print(f"  计算历史: {calc.get_history()}")

# ============================================================================
# 5. 演示模块导入行为
# ============================================================================

def demonstrate_import_behavior():
    """
    演示模块导入时的行为
    """
    print("\n=== 4. 模块导入行为演示 ===")
    
    print("当前模块信息：")
    print(f"  模块名: {__name__}")
    print(f"  是否为主模块: {__name__ == '__main__'}")
    
    # 显示模块的属性
    print("\n模块属性：")
    module_attrs = [attr for attr in dir() if not attr.startswith('_') or attr in ['__name__', '__file__', '__doc__']]
    for attr in sorted(module_attrs):
        value = globals()[attr]
        attr_type = type(value).__name__
        print(f"  {attr:20s}: {attr_type}")
    
    # 演示导入其他模块时的__name__
    print("\n导入其他模块时的__name__：")
    import json
    import os
    print(f"  json模块的__name__: {json.__name__}")
    print(f"  os模块的__name__: {os.__name__}")

# ============================================================================
# 6. 实际应用场景演示
# ============================================================================

def demonstrate_practical_usage():
    """
    演示__name__的实际应用场景
    """
    print("\n=== 5. 实际应用场景 ===")
    
    print("__name__的常见用途：")
    print("\n1. 模块测试：")
    print("   if __name__ == '__main__':")
    print("       run_tests()")
    
    print("\n2. 命令行工具：")
    print("   if __name__ == '__main__':")
    print("       main()")
    
    print("\n3. 示例代码：")
    print("   if __name__ == '__main__':")
    print("       demonstrate_features()")
    
    print("\n4. 配置初始化：")
    print("   if __name__ == '__main__':")
    print("       setup_configuration()")
    
    print("\n5. 调试代码：")
    print("   if __name__ == '__main__':")
    print("       debug_module()")

# ============================================================================
# 7. 最佳实践建议
# ============================================================================

def show_best_practices():
    """
    显示使用__name__的最佳实践
    """
    print("\n=== 6. 最佳实践建议 ===")
    
    practices = [
        "1. 总是使用 if __name__ == '__main__': 来保护执行代码",
        "2. 将主要逻辑放在函数中，而不是模块级别",
        "3. 在主执行块中调用main()函数",
        "4. 使用主执行块进行模块测试和演示",
        "5. 避免在模块级别执行耗时操作",
        "6. 保持模块级别代码简洁",
        "7. 使用文档字符串说明模块用途",
        "8. 在主执行块中处理命令行参数",
        "9. 将配置和初始化代码放在适当位置",
        "10. 考虑模块的可重用性和可测试性"
    ]
    
    for practice in practices:
        print(f"  {practice}")
    
    print("\n推荐的模块结构：")
    print("""
  #!/usr/bin/env python3
  # -*- coding: utf-8 -*-
  \"\"\"
  模块文档字符串
  \"\"\"
  
  # 导入语句
  import sys
  
  # 模块级别常量
  CONSTANT = "value"
  
  # 函数和类定义
  def function():
      pass
  
  class MyClass:
      pass
  
  # 主执行块
  if __name__ == '__main__':
      main()
    """)

# ============================================================================
# 8. 创建辅助演示文件
# ============================================================================

def create_demo_files():
    """
    创建辅助演示文件来展示导入行为
    """
    print("\n=== 7. 创建演示文件 ===")
    
    # 创建一个简单的演示模块
    demo_content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
演示模块 - 用于展示__name__变量的行为
"""

print(f"演示模块被加载，__name__ = {__name__}")

DEMO_MESSAGE = "这是演示模块"

def demo_function():
    return f"演示函数被调用，来自模块 {__name__}"

if __name__ == '__main__':
    print("演示模块被直接运行")
    print(demo_function())
else:
    print("演示模块被导入")
'''
    
    demo_file = "demo_module.py"
    try:
        with open(demo_file, 'w', encoding='utf-8') as f:
            f.write(demo_content)
        print(f"创建演示文件: {demo_file}")
        
        # 尝试导入演示模块
        print("\n导入演示模块：")
        import demo_module
        print(f"演示模块的__name__: {demo_module.__name__}")
        print(f"调用演示函数: {demo_module.demo_function()}")
        
    except Exception as e:
        print(f"创建或导入演示文件时出错: {e}")
    
    # 清理演示文件
    try:
        if os.path.exists(demo_file):
            os.remove(demo_file)
            print(f"\n清理演示文件: {demo_file}")
    except Exception as e:
        print(f"清理演示文件时出错: {e}")

# ============================================================================
# 主函数
# ============================================================================

def main():
    """
    主函数：演示所有__name__变量相关功能
    """
    print("\nPython __name__变量演示")
    print("=" * 60)
    
    explain_name_variable()
    demonstrate_execution_modes()
    run_module_tests()
    demonstrate_import_behavior()
    demonstrate_practical_usage()
    show_best_practices()
    create_demo_files()
    
    print("\n" + "=" * 60)
    print("__name__变量演示完成！")
    print("=" * 60)

# ============================================================================
# 模块执行控制
# ============================================================================

# 这里是关键：只有当模块被直接运行时才执行主函数
if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("模块被直接运行，开始执行主程序...")
    print("=" * 60)
    main()
else:
    print(f"模块被导入到 {__name__}，只加载定义，不执行主程序")

# 模块级别的最后一行代码
print(f"模块 {__name__} 加载完成")