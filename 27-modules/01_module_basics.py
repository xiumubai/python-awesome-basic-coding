#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模块基础 - Module Basics

本文件演示Python模块的基本概念和作用：
1. 模块的定义和作用
2. 模块的基本组成部分
3. 如何在模块中定义变量、函数和类
4. 模块的使用示例

学习目标：
- 理解什么是模块以及模块的作用
- 掌握模块的基本结构
- 学会在模块中定义和使用各种元素
- 了解模块的命名空间概念

作者: Python学习教程
日期: 2024
"""

# ============================================================================
# 1. 模块的基本概念
# ============================================================================

"""
什么是模块？
- 模块是包含Python定义和语句的文件
- 文件名就是模块名加上.py后缀
- 模块可以包含可执行语句和函数定义
- 这些语句用于初始化模块，它们只在模块第一次被导入时执行

模块的作用：
1. 代码复用：避免重复编写相同的代码
2. 命名空间：避免变量名冲突
3. 代码组织：将相关功能组织在一起
4. 模块化开发：便于团队协作和维护
"""

# ============================================================================
# 2. 模块变量 - 模块级别的变量
# ============================================================================

# 模块常量（通常用大写字母命名）
MODULE_NAME = "模块基础示例"
VERSION = "1.0.0"
AUTHOR = "Python学习教程"

# 模块变量
counter = 0
data_list = []
config = {
    'debug': True,
    'max_items': 100,
    'default_encoding': 'utf-8'
}

print(f"模块 {MODULE_NAME} 正在初始化...")

# ============================================================================
# 3. 模块函数 - 在模块中定义的函数
# ============================================================================

def greet(name="World"):
    """
    问候函数
    
    Args:
        name (str): 要问候的名字，默认为"World"
    
    Returns:
        str: 问候语
    """
    return f"Hello, {name}! 欢迎学习Python模块！"


def increment_counter():
    """
    增加计数器的值
    
    Returns:
        int: 增加后的计数器值
    """
    global counter
    counter += 1
    return counter


def add_data(item):
    """
    向数据列表添加项目
    
    Args:
        item: 要添加的项目
    
    Returns:
        list: 更新后的数据列表
    """
    data_list.append(item)
    return data_list.copy()


def get_module_info():
    """
    获取模块信息
    
    Returns:
        dict: 包含模块信息的字典
    """
    return {
        'name': MODULE_NAME,
        'version': VERSION,
        'author': AUTHOR,
        'counter': counter,
        'data_count': len(data_list),
        'config': config.copy()
    }


def calculate_area(length, width):
    """
    计算矩形面积
    
    Args:
        length (float): 长度
        width (float): 宽度
    
    Returns:
        float: 面积
    """
    if length <= 0 or width <= 0:
        raise ValueError("长度和宽度必须大于0")
    return length * width


# ============================================================================
# 4. 模块类 - 在模块中定义的类
# ============================================================================

class SimpleCalculator:
    """
    简单计算器类
    
    这个类演示了如何在模块中定义类
    """
    
    def __init__(self, name="计算器"):
        """
        初始化计算器
        
        Args:
            name (str): 计算器名称
        """
        self.name = name
        self.history = []
    
    def add(self, a, b):
        """
        加法运算
        
        Args:
            a (float): 第一个数
            b (float): 第二个数
        
        Returns:
            float: 运算结果
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """
        减法运算
        
        Args:
            a (float): 被减数
            b (float): 减数
        
        Returns:
            float: 运算结果
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """
        乘法运算
        
        Args:
            a (float): 第一个数
            b (float): 第二个数
        
        Returns:
            float: 运算结果
        """
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """
        除法运算
        
        Args:
            a (float): 被除数
            b (float): 除数
        
        Returns:
            float: 运算结果
        
        Raises:
            ValueError: 当除数为0时
        """
        if b == 0:
            raise ValueError("除数不能为0")
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def get_history(self):
        """
        获取计算历史
        
        Returns:
            list: 计算历史列表
        """
        return self.history.copy()
    
    def clear_history(self):
        """
        清空计算历史
        """
        self.history.clear()
    
    def __str__(self):
        return f"{self.name} - 已执行 {len(self.history)} 次计算"


class DataManager:
    """
    数据管理器类
    
    演示如何在模块中创建数据管理类
    """
    
    def __init__(self):
        """
        初始化数据管理器
        """
        self.data = {}
        self.created_time = None
        self._import_time()
    
    def _import_time(self):
        """
        导入时间模块（私有方法示例）
        """
        import datetime
        self.created_time = datetime.datetime.now()
    
    def set_data(self, key, value):
        """
        设置数据
        
        Args:
            key (str): 键
            value: 值
        """
        self.data[key] = value
    
    def get_data(self, key, default=None):
        """
        获取数据
        
        Args:
            key (str): 键
            default: 默认值
        
        Returns:
            数据值或默认值
        """
        return self.data.get(key, default)
    
    def get_all_data(self):
        """
        获取所有数据
        
        Returns:
            dict: 所有数据的副本
        """
        return self.data.copy()
    
    def clear_data(self):
        """
        清空所有数据
        """
        self.data.clear()
    
    def get_info(self):
        """
        获取管理器信息
        
        Returns:
            dict: 管理器信息
        """
        return {
            'data_count': len(self.data),
            'created_time': self.created_time.strftime('%Y-%m-%d %H:%M:%S') if self.created_time else None,
            'keys': list(self.data.keys())
        }


# ============================================================================
# 5. 模块初始化代码
# ============================================================================

# 模块级别的初始化代码
# 这些代码在模块第一次被导入时执行

print(f"模块变量初始化完成:")
print(f"  - MODULE_NAME: {MODULE_NAME}")
print(f"  - VERSION: {VERSION}")
print(f"  - 初始计数器值: {counter}")
print(f"  - 配置项数量: {len(config)}")

# 创建一些默认实例
default_calculator = SimpleCalculator("默认计算器")
default_data_manager = DataManager()

print("默认实例创建完成")


# ============================================================================
# 6. 模块使用示例（当作为脚本运行时）
# ============================================================================

def demo_module_usage():
    """
    演示模块的使用方法
    """
    print("\n" + "="*60)
    print("模块使用示例演示")
    print("="*60)
    
    # 1. 使用模块变量
    print("\n1. 模块变量使用:")
    print(f"模块名称: {MODULE_NAME}")
    print(f"版本: {VERSION}")
    print(f"当前计数器: {counter}")
    
    # 2. 使用模块函数
    print("\n2. 模块函数使用:")
    print(greet("Python学习者"))
    
    # 增加计数器
    for i in range(3):
        count = increment_counter()
        print(f"计数器增加到: {count}")
    
    # 添加数据
    add_data("第一项数据")
    add_data("第二项数据")
    add_data(42)
    print(f"数据列表: {data_list}")
    
    # 计算面积
    try:
        area = calculate_area(5, 3)
        print(f"矩形面积 (5×3): {area}")
    except ValueError as e:
        print(f"计算错误: {e}")
    
    # 获取模块信息
    info = get_module_info()
    print(f"模块信息: {info}")
    
    # 3. 使用模块类
    print("\n3. 模块类使用:")
    
    # 使用计算器类
    calc = SimpleCalculator("演示计算器")
    print(f"创建计算器: {calc}")
    
    # 执行一些计算
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 3 = {calc.subtract(10, 3)}")
    print(f"4 × 6 = {calc.multiply(4, 6)}")
    print(f"15 ÷ 3 = {calc.divide(15, 3)}")
    
    print(f"\n计算历史:")
    for record in calc.get_history():
        print(f"  {record}")
    
    print(f"\n计算器状态: {calc}")
    
    # 使用数据管理器类
    print("\n4. 数据管理器使用:")
    dm = DataManager()
    
    # 设置一些数据
    dm.set_data("name", "Python模块学习")
    dm.set_data("level", "初级")
    dm.set_data("progress", 25)
    
    print(f"设置的数据:")
    for key in ['name', 'level', 'progress']:
        print(f"  {key}: {dm.get_data(key)}")
    
    print(f"\n数据管理器信息: {dm.get_info()}")
    
    # 5. 使用默认实例
    print("\n5. 默认实例使用:")
    print(f"默认计算器: {default_calculator}")
    result = default_calculator.add(100, 200)
    print(f"使用默认计算器计算: 100 + 200 = {result}")
    
    print(f"默认数据管理器信息: {default_data_manager.get_info()}")
    
    print("\n" + "="*60)
    print("模块演示完成！")
    print("="*60)


# ============================================================================
# 7. 模块测试代码
# ============================================================================

def test_module_functions():
    """
    测试模块中的函数
    """
    print("\n开始测试模块函数...")
    
    # 测试问候函数
    assert greet() == "Hello, World! 欢迎学习Python模块！"
    assert greet("张三") == "Hello, 张三! 欢迎学习Python模块！"
    print("✓ greet函数测试通过")
    
    # 测试计数器函数
    initial_counter = counter
    new_count = increment_counter()
    assert new_count == initial_counter + 1
    print("✓ increment_counter函数测试通过")
    
    # 测试数据添加函数
    initial_length = len(data_list)
    result_list = add_data("测试数据")
    assert len(result_list) == initial_length + 1
    assert "测试数据" in result_list
    print("✓ add_data函数测试通过")
    
    # 测试面积计算函数
    assert calculate_area(4, 5) == 20
    try:
        calculate_area(-1, 5)
        assert False, "应该抛出ValueError"
    except ValueError:
        pass
    print("✓ calculate_area函数测试通过")
    
    print("所有函数测试通过！")


def test_module_classes():
    """
    测试模块中的类
    """
    print("\n开始测试模块类...")
    
    # 测试计算器类
    calc = SimpleCalculator("测试计算器")
    assert calc.add(2, 3) == 5
    assert calc.subtract(10, 4) == 6
    assert calc.multiply(3, 4) == 12
    assert calc.divide(15, 3) == 5
    
    # 测试除零错误
    try:
        calc.divide(10, 0)
        assert False, "应该抛出ValueError"
    except ValueError:
        pass
    
    assert len(calc.get_history()) == 4  # 4次成功计算
    print("✓ SimpleCalculator类测试通过")
    
    # 测试数据管理器类
    dm = DataManager()
    dm.set_data("test_key", "test_value")
    assert dm.get_data("test_key") == "test_value"
    assert dm.get_data("nonexistent", "default") == "default"
    
    info = dm.get_info()
    assert info['data_count'] == 1
    assert 'test_key' in info['keys']
    print("✓ DataManager类测试通过")
    
    print("所有类测试通过！")


# ============================================================================
# 8. 主程序入口
# ============================================================================

if __name__ == "__main__":
    """
    当模块作为脚本直接运行时执行的代码
    
    这部分代码只有在直接运行此文件时才会执行，
    当作为模块被导入时不会执行。
    """
    print("\n" + "="*60)
    print(f"直接运行模块: {__file__}")
    print(f"模块名称: {__name__}")
    print("="*60)
    
    # 运行演示
    demo_module_usage()
    
    # 运行测试
    test_module_functions()
    test_module_classes()
    
    print("\n" + "="*60)
    print("模块运行完成！")
    print("\n提示：")
    print("- 你可以在其他Python文件中导入这个模块")
    print("- 使用 'import 01_module_basics' 来导入")
    print("- 然后使用 '01_module_basics.函数名()' 来调用函数")
    print("- 或使用 'from 01_module_basics import 函数名' 来直接导入函数")
    print("="*60)
else:
    print(f"模块 {MODULE_NAME} 已被导入到 {__name__} 命名空间")