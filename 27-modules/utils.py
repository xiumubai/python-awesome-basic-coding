#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
工具模块 - 用于演示模块导入

这个模块包含一些实用的工具函数和类，
用于演示不同的导入方式和模块使用方法。

Author: Python学习者
Version: 1.0.0
Date: 2024
"""

import math
import random
from datetime import datetime

# 模块级别的常量
MODULE_NAME = "utils"
MODULE_VERSION = "1.0.0"
PI = 3.14159265359
E = 2.71828182846

# 模块级别的变量
counter = 0
last_access_time = None

print(f"工具模块 {MODULE_NAME} v{MODULE_VERSION} 已加载")

# ============================================================================
# 数学工具函数
# ============================================================================

def add(a, b):
    """
    计算两个数的和
    
    Args:
        a (float): 第一个数
        b (float): 第二个数
    
    Returns:
        float: 两数之和
    
    Example:
        >>> add(3, 5)
        8
    """
    return a + b

def multiply(a, b):
    """
    计算两个数的乘积
    
    Args:
        a (float): 第一个数
        b (float): 第二个数
    
    Returns:
        float: 两数之积
    
    Example:
        >>> multiply(3, 4)
        12
    """
    return a * b

def power(base, exponent):
    """
    计算幂运算
    
    Args:
        base (float): 底数
        exponent (float): 指数
    
    Returns:
        float: base的exponent次幂
    
    Example:
        >>> power(2, 3)
        8
    """
    return base ** exponent

def factorial(n):
    """
    计算阶乘
    
    Args:
        n (int): 非负整数
    
    Returns:
        int: n的阶乘
    
    Raises:
        ValueError: 当n为负数时
    
    Example:
        >>> factorial(5)
        120
    """
    if n < 0:
        raise ValueError("阶乘的参数必须是非负整数")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    """
    判断一个数是否为质数
    
    Args:
        n (int): 要判断的整数
    
    Returns:
        bool: 如果是质数返回True，否则返回False
    
    Example:
        >>> is_prime(17)
        True
        >>> is_prime(15)
        False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# ============================================================================
# 字符串工具函数
# ============================================================================

def reverse_string(s):
    """
    反转字符串
    
    Args:
        s (str): 要反转的字符串
    
    Returns:
        str: 反转后的字符串
    
    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    return s[::-1]

def capitalize_words(s):
    """
    将字符串中每个单词的首字母大写
    
    Args:
        s (str): 输入字符串
    
    Returns:
        str: 处理后的字符串
    
    Example:
        >>> capitalize_words("hello world")
        'Hello World'
    """
    return ' '.join(word.capitalize() for word in s.split())

def count_words(s):
    """
    统计字符串中的单词数量
    
    Args:
        s (str): 输入字符串
    
    Returns:
        int: 单词数量
    
    Example:
        >>> count_words("hello world python")
        3
    """
    return len(s.split())

def remove_duplicates(s):
    """
    移除字符串中的重复字符（保持顺序）
    
    Args:
        s (str): 输入字符串
    
    Returns:
        str: 移除重复字符后的字符串
    
    Example:
        >>> remove_duplicates("hello")
        'helo'
    """
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

# ============================================================================
# 列表工具函数
# ============================================================================

def find_max(lst):
    """
    找到列表中的最大值
    
    Args:
        lst (list): 数字列表
    
    Returns:
        float: 最大值
    
    Raises:
        ValueError: 当列表为空时
    
    Example:
        >>> find_max([1, 5, 3, 9, 2])
        9
    """
    if not lst:
        raise ValueError("列表不能为空")
    return max(lst)

def find_min(lst):
    """
    找到列表中的最小值
    
    Args:
        lst (list): 数字列表
    
    Returns:
        float: 最小值
    
    Raises:
        ValueError: 当列表为空时
    
    Example:
        >>> find_min([1, 5, 3, 9, 2])
        1
    """
    if not lst:
        raise ValueError("列表不能为空")
    return min(lst)

def calculate_average(lst):
    """
    计算列表的平均值
    
    Args:
        lst (list): 数字列表
    
    Returns:
        float: 平均值
    
    Raises:
        ValueError: 当列表为空时
    
    Example:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
    """
    if not lst:
        raise ValueError("列表不能为空")
    return sum(lst) / len(lst)

def remove_duplicates_list(lst):
    """
    移除列表中的重复元素（保持顺序）
    
    Args:
        lst (list): 输入列表
    
    Returns:
        list: 移除重复元素后的列表
    
    Example:
        >>> remove_duplicates_list([1, 2, 2, 3, 1, 4])
        [1, 2, 3, 4]
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# ============================================================================
# 随机工具函数
# ============================================================================

def generate_random_number(min_val=0, max_val=100):
    """
    生成指定范围内的随机整数
    
    Args:
        min_val (int): 最小值，默认为0
        max_val (int): 最大值，默认为100
    
    Returns:
        int: 随机整数
    
    Example:
        >>> num = generate_random_number(1, 10)
        >>> 1 <= num <= 10
        True
    """
    return random.randint(min_val, max_val)

def generate_random_list(length=10, min_val=0, max_val=100):
    """
    生成随机数字列表
    
    Args:
        length (int): 列表长度，默认为10
        min_val (int): 最小值，默认为0
        max_val (int): 最大值，默认为100
    
    Returns:
        list: 随机数字列表
    
    Example:
        >>> lst = generate_random_list(5, 1, 10)
        >>> len(lst)
        5
    """
    return [random.randint(min_val, max_val) for _ in range(length)]

def shuffle_list(lst):
    """
    随机打乱列表顺序
    
    Args:
        lst (list): 要打乱的列表
    
    Returns:
        list: 打乱后的新列表
    
    Example:
        >>> original = [1, 2, 3, 4, 5]
        >>> shuffled = shuffle_list(original)
        >>> len(shuffled) == len(original)
        True
    """
    new_list = lst.copy()
    random.shuffle(new_list)
    return new_list

# ============================================================================
# 时间工具函数
# ============================================================================

def get_current_time():
    """
    获取当前时间
    
    Returns:
        datetime: 当前时间对象
    
    Example:
        >>> time = get_current_time()
        >>> isinstance(time, datetime)
        True
    """
    global last_access_time
    last_access_time = datetime.now()
    return last_access_time

def format_time(dt=None, format_str="%Y-%m-%d %H:%M:%S"):
    """
    格式化时间
    
    Args:
        dt (datetime, optional): 时间对象，默认为当前时间
        format_str (str): 格式字符串
    
    Returns:
        str: 格式化后的时间字符串
    
    Example:
        >>> time_str = format_time()
        >>> len(time_str) > 0
        True
    """
    if dt is None:
        dt = datetime.now()
    return dt.strftime(format_str)

def time_difference(start_time, end_time):
    """
    计算两个时间之间的差值（秒）
    
    Args:
        start_time (datetime): 开始时间
        end_time (datetime): 结束时间
    
    Returns:
        float: 时间差（秒）
    
    Example:
        >>> from datetime import datetime, timedelta
        >>> start = datetime.now()
        >>> end = start + timedelta(seconds=5)
        >>> diff = time_difference(start, end)
        >>> diff
        5.0
    """
    return (end_time - start_time).total_seconds()

# ============================================================================
# 计数器工具函数
# ============================================================================

def increment_counter():
    """
    递增模块计数器
    
    Returns:
        int: 递增后的计数器值
    
    Example:
        >>> count = increment_counter()
        >>> isinstance(count, int)
        True
    """
    global counter
    counter += 1
    return counter

def get_counter():
    """
    获取当前计数器值
    
    Returns:
        int: 当前计数器值
    
    Example:
        >>> count = get_counter()
        >>> isinstance(count, int)
        True
    """
    return counter

def reset_counter():
    """
    重置计数器为0
    
    Returns:
        int: 重置后的计数器值（0）
    
    Example:
        >>> reset_counter()
        0
    """
    global counter
    counter = 0
    return counter

# ============================================================================
# 模块信息函数
# ============================================================================

def get_module_info():
    """
    获取模块信息
    
    Returns:
        dict: 包含模块信息的字典
    
    Example:
        >>> info = get_module_info()
        >>> 'name' in info
        True
    """
    return {
        'name': MODULE_NAME,
        'version': MODULE_VERSION,
        'counter': counter,
        'last_access': last_access_time,
        'constants': {
            'PI': PI,
            'E': E
        },
        'functions': [
            'add', 'multiply', 'power', 'factorial', 'is_prime',
            'reverse_string', 'capitalize_words', 'count_words',
            'find_max', 'find_min', 'calculate_average',
            'generate_random_number', 'get_current_time'
        ]
    }

def print_module_info():
    """
    打印模块信息
    
    Example:
        >>> print_module_info()
        # 输出模块详细信息
    """
    info = get_module_info()
    print(f"模块名称: {info['name']}")
    print(f"模块版本: {info['version']}")
    print(f"访问计数: {info['counter']}")
    print(f"最后访问: {info['last_access']}")
    print(f"常量数量: {len(info['constants'])}")
    print(f"函数数量: {len(info['functions'])}")

# ============================================================================
# 模块初始化
# ============================================================================

# 模块加载时的初始化操作
def _initialize_module():
    """
    模块初始化函数（私有）
    """
    global counter, last_access_time
    counter = 0
    last_access_time = datetime.now()
    print(f"模块 {MODULE_NAME} 初始化完成")

# 执行初始化
_initialize_module()

# ============================================================================
# 模块级别的测试代码
# ============================================================================

if __name__ == '__main__':
    print("\n=== 工具模块测试 ===")
    
    # 测试数学函数
    print("\n数学函数测试：")
    print(f"add(3, 5) = {add(3, 5)}")
    print(f"multiply(4, 6) = {multiply(4, 6)}")
    print(f"power(2, 3) = {power(2, 3)}")
    print(f"factorial(5) = {factorial(5)}")
    print(f"is_prime(17) = {is_prime(17)}")
    
    # 测试字符串函数
    print("\n字符串函数测试：")
    print(f"reverse_string('hello') = {reverse_string('hello')}")
    print(f"capitalize_words('hello world') = {capitalize_words('hello world')}")
    print(f"count_words('hello world python') = {count_words('hello world python')}")
    
    # 测试列表函数
    print("\n列表函数测试：")
    test_list = [1, 5, 3, 9, 2]
    print(f"find_max({test_list}) = {find_max(test_list)}")
    print(f"find_min({test_list}) = {find_min(test_list)}")
    print(f"calculate_average({test_list}) = {calculate_average(test_list)}")
    
    # 测试随机函数
    print("\n随机函数测试：")
    print(f"generate_random_number(1, 10) = {generate_random_number(1, 10)}")
    print(f"generate_random_list(5, 1, 10) = {generate_random_list(5, 1, 10)}")
    
    # 测试时间函数
    print("\n时间函数测试：")
    current_time = get_current_time()
    print(f"get_current_time() = {current_time}")
    print(f"format_time() = {format_time()}")
    
    # 测试计数器函数
    print("\n计数器函数测试：")
    print(f"increment_counter() = {increment_counter()}")
    print(f"increment_counter() = {increment_counter()}")
    print(f"get_counter() = {get_counter()}")
    
    # 显示模块信息
    print("\n模块信息：")
    print_module_info()
    
    print("\n=== 测试完成 ===")