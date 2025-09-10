# 辅助模块：utils.py

## 模块概述

`utils.py` 是一个通用工具模块，包含了各种常用的工具函数和常量定义。这个模块演示了如何组织和编写实用的工具函数，以及如何在模块中定义常量和提供便捷的功能。

## 模块结构

### 常量定义

```python
# 数学常量
PI = 3.14159265359
E = 2.71828182846
GOLDEN_RATIO = 1.61803398875

# 字符串常量
DEFAULT_ENCODING = 'utf-8'
NEWLINE = '\n'
TAB = '\t'

# 配置常量
DEBUG = True
VERSION = '1.0.0'
AUTHOR = 'Python学习者'
```

### 数学工具函数

```python
def add_numbers(a, b):
    """加法运算。
    
    Args:
        a (float): 第一个数
        b (float): 第二个数
    
    Returns:
        float: 两数之和
    """
    return a + b

def multiply_numbers(a, b):
    """乘法运算。
    
    Args:
        a (float): 第一个数
        b (float): 第二个数
    
    Returns:
        float: 两数之积
    """
    return a * b

def power(base, exponent):
    """幂运算。
    
    Args:
        base (float): 底数
        exponent (float): 指数
    
    Returns:
        float: base的exponent次幂
    """
    return base ** exponent

def circle_area(radius):
    """计算圆的面积。
    
    Args:
        radius (float): 圆的半径
    
    Returns:
        float: 圆的面积
    """
    return PI * radius * radius
```

### 字符串工具函数

```python
def reverse_string(s):
    """反转字符串。
    
    Args:
        s (str): 要反转的字符串
    
    Returns:
        str: 反转后的字符串
    """
    return s[::-1]

def capitalize_words(s):
    """将字符串中每个单词的首字母大写。
    
    Args:
        s (str): 输入字符串
    
    Returns:
        str: 处理后的字符串
    """
    return ' '.join(word.capitalize() for word in s.split())

def count_vowels(s):
    """统计字符串中的元音字母数量。
    
    Args:
        s (str): 输入字符串
    
    Returns:
        int: 元音字母的数量
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def remove_spaces(s):
    """移除字符串中的所有空格。
    
    Args:
        s (str): 输入字符串
    
    Returns:
        str: 移除空格后的字符串
    """
    return s.replace(' ', '')
```

### 列表工具函数

```python
def find_max(numbers):
    """找到列表中的最大值。
    
    Args:
        numbers (list): 数字列表
    
    Returns:
        float: 最大值，如果列表为空返回None
    """
    return max(numbers) if numbers else None

def find_min(numbers):
    """找到列表中的最小值。
    
    Args:
        numbers (list): 数字列表
    
    Returns:
        float: 最小值，如果列表为空返回None
    """
    return min(numbers) if numbers else None

def calculate_average(numbers):
    """计算列表的平均值。
    
    Args:
        numbers (list): 数字列表
    
    Returns:
        float: 平均值，如果列表为空返回None
    """
    return sum(numbers) / len(numbers) if numbers else None

def remove_duplicates(lst):
    """移除列表中的重复元素。
    
    Args:
        lst (list): 输入列表
    
    Returns:
        list: 移除重复元素后的列表
    """
    return list(set(lst))
```

### 随机工具函数

```python
def generate_random_number(min_val=1, max_val=100):
    """生成指定范围内的随机整数。
    
    Args:
        min_val (int): 最小值，默认为1
        max_val (int): 最大值，默认为100
    
    Returns:
        int: 随机整数
    """
    import random
    return random.randint(min_val, max_val)

def generate_random_string(length=10):
    """生成指定长度的随机字符串。
    
    Args:
        length (int): 字符串长度，默认为10
    
    Returns:
        str: 随机字符串
    """
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def shuffle_list(lst):
    """随机打乱列表。
    
    Args:
        lst (list): 要打乱的列表
    
    Returns:
        list: 打乱后的新列表
    """
    import random
    new_list = lst.copy()
    random.shuffle(new_list)
    return new_list
```

### 时间工具函数

```python
def get_current_time():
    """获取当前时间字符串。
    
    Returns:
        str: 格式化的当前时间
    """
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_timestamp():
    """获取当前时间戳。
    
    Returns:
        float: 当前时间戳
    """
    import time
    return time.time()

def format_duration(seconds):
    """将秒数格式化为可读的时间格式。
    
    Args:
        seconds (float): 秒数
    
    Returns:
        str: 格式化的时间字符串
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    
    if hours > 0:
        return f"{hours}小时{minutes}分钟{secs}秒"
    elif minutes > 0:
        return f"{minutes}分钟{secs}秒"
    else:
        return f"{secs}秒"
```

### 计数器类

```python
class Counter:
    """简单的计数器类。
    
    用于统计和计数操作。
    
    Attributes:
        count (int): 当前计数值
        name (str): 计数器名称
    """
    
    def __init__(self, name="默认计数器", initial_count=0):
        """初始化计数器。
        
        Args:
            name (str): 计数器名称
            initial_count (int): 初始计数值
        """
        self.name = name
        self.count = initial_count
    
    def increment(self, step=1):
        """增加计数。
        
        Args:
            step (int): 增加的步长，默认为1
        
        Returns:
            int: 增加后的计数值
        """
        self.count += step
        return self.count
    
    def decrement(self, step=1):
        """减少计数。
        
        Args:
            step (int): 减少的步长，默认为1
        
        Returns:
            int: 减少后的计数值
        """
        self.count -= step
        return self.count
    
    def reset(self):
        """重置计数器。
        
        Returns:
            int: 重置后的计数值（0）
        """
        self.count = 0
        return self.count
    
    def get_count(self):
        """获取当前计数值。
        
        Returns:
            int: 当前计数值
        """
        return self.count
    
    def __str__(self):
        """返回计数器的字符串表示。
        
        Returns:
            str: 计数器的字符串表示
        """
        return f"{self.name}: {self.count}"
```

## 模块初始化和测试

### 模块初始化代码

```python
# 模块初始化
print(f"正在加载 {__name__} 模块...")
print(f"模块版本: {VERSION}")
print(f"作者: {AUTHOR}")

# 创建全局计数器实例
global_counter = Counter("全局计数器")

print(f"{__name__} 模块加载完成！")
```

### 模块级测试代码

```python
if __name__ == '__main__':
    print("=== Utils模块测试 ===")
    print()
    
    # 测试数学函数
    print("1. 数学函数测试:")
    print(f"   5 + 3 = {add_numbers(5, 3)}")
    print(f"   4 * 6 = {multiply_numbers(4, 6)}")
    print(f"   2^3 = {power(2, 3)}")
    print(f"   半径为5的圆面积 = {circle_area(5):.2f}")
    print()
    
    # 测试字符串函数
    print("2. 字符串函数测试:")
    test_string = "hello world python"
    print(f"   原字符串: '{test_string}'")
    print(f"   反转: '{reverse_string(test_string)}'")
    print(f"   首字母大写: '{capitalize_words(test_string)}'")
    print(f"   元音字母数量: {count_vowels(test_string)}")
    print(f"   移除空格: '{remove_spaces(test_string)}'")
    print()
    
    # 测试列表函数
    print("3. 列表函数测试:")
    test_numbers = [1, 5, 3, 9, 2, 7, 5, 1]
    print(f"   原列表: {test_numbers}")
    print(f"   最大值: {find_max(test_numbers)}")
    print(f"   最小值: {find_min(test_numbers)}")
    print(f"   平均值: {calculate_average(test_numbers):.2f}")
    print(f"   去重后: {remove_duplicates(test_numbers)}")
    print()
    
    # 测试随机函数
    print("4. 随机函数测试:")
    print(f"   随机数(1-10): {generate_random_number(1, 10)}")
    print(f"   随机字符串(长度5): '{generate_random_string(5)}'")
    shuffled = shuffle_list([1, 2, 3, 4, 5])
    print(f"   打乱列表[1,2,3,4,5]: {shuffled}")
    print()
    
    # 测试时间函数
    print("5. 时间函数测试:")
    print(f"   当前时间: {get_current_time()}")
    print(f"   时间戳: {get_timestamp():.2f}")
    print(f"   3661秒格式化: {format_duration(3661)}")
    print()
    
    # 测试计数器类
    print("6. 计数器类测试:")
    counter = Counter("测试计数器")
    print(f"   初始状态: {counter}")
    counter.increment(5)
    print(f"   增加5后: {counter}")
    counter.decrement(2)
    print(f"   减少2后: {counter}")
    counter.reset()
    print(f"   重置后: {counter}")
    print()
    
    # 测试全局计数器
    print("7. 全局计数器测试:")
    print(f"   全局计数器: {global_counter}")
    global_counter.increment(10)
    print(f"   增加10后: {global_counter}")
    print()
    
    # 显示模块信息
    print("8. 模块信息:")
    print(f"   模块名称: {__name__}")
    print(f"   版本: {VERSION}")
    print(f"   作者: {AUTHOR}")
    print(f"   调试模式: {DEBUG}")
    print(f"   PI常量: {PI}")
    print(f"   E常量: {E}")
    print(f"   黄金比例: {GOLDEN_RATIO}")
```

## 使用示例

### 基本导入和使用

```python
# 导入整个模块
import utils

# 使用模块中的函数
result = utils.add_numbers(10, 20)
print(f"10 + 20 = {result}")

# 使用模块中的常量
print(f"圆周率: {utils.PI}")

# 使用模块中的类
counter = utils.Counter("我的计数器")
counter.increment(5)
print(counter)
```

### 选择性导入

```python
# 导入特定函数
from utils import add_numbers, multiply_numbers, PI

# 直接使用导入的函数和常量
result1 = add_numbers(5, 3)
result2 = multiply_numbers(4, 6)
area = PI * 5 * 5

print(f"加法结果: {result1}")
print(f"乘法结果: {result2}")
print(f"圆面积: {area}")
```

### 使用别名导入

```python
# 使用别名导入
from utils import Counter as MyCounter
from utils import generate_random_string as random_str

# 使用别名
counter = MyCounter("别名计数器")
random_string = random_str(8)

print(f"计数器: {counter}")
print(f"随机字符串: {random_string}")
```

## 学习要点

1. **模块组织**：如何将相关功能组织到一个模块中
2. **常量定义**：在模块级别定义常量的最佳实践
3. **函数设计**：编写通用、可重用的工具函数
4. **类的使用**：在模块中定义和使用类
5. **模块初始化**：模块加载时的初始化代码
6. **文档编写**：为模块、函数、类编写清晰的文档
7. **测试代码**：在模块中包含测试代码的方法

## 扩展练习

1. **添加新功能**：为utils模块添加文件操作工具函数
2. **错误处理**：为现有函数添加适当的错误处理
3. **性能优化**：优化某些函数的性能
4. **单元测试**：为模块编写完整的单元测试
5. **配置管理**：添加配置文件读取功能
6. **日志功能**：集成日志记录功能

这个utils模块展示了如何创建一个实用的工具模块，包含了常用的功能和良好的代码组织结构，是学习Python模块开发的很好示例。