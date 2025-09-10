# 02. 导入语句详解

## 学习目标

- 掌握各种import语句的语法和用法
- 理解不同导入方式的区别和适用场景
- 学会使用别名和选择性导入
- 了解导入的最佳实践

## 导入语句概述

Python提供了多种导入模块的方式，每种方式都有其特定的用途和优势。正确使用导入语句是编写高质量Python代码的基础。

## 基本导入语句

### 1. import 语句

最基本的导入方式，导入整个模块：

```python
import math
import os
import sys

# 使用模块中的功能需要加模块名前缀
result = math.sqrt(16)
print(f"平方根: {result}")  # 输出: 平方根: 4.0

current_dir = os.getcwd()
print(f"当前目录: {current_dir}")

python_version = sys.version
print(f"Python版本: {python_version}")
```

### 2. from...import 语句

从模块中导入特定的名称：

```python
from math import sqrt, pi, sin, cos
from os import getcwd, listdir
from sys import version, path

# 可以直接使用导入的名称，无需模块名前缀
result = sqrt(25)
print(f"平方根: {result}")  # 输出: 平方根: 5.0

print(f"π的值: {pi}")  # 输出: π的值: 3.141592653589793

current_dir = getcwd()
print(f"当前目录: {current_dir}")

files = listdir('.')
print(f"当前目录文件: {files[:3]}...")  # 显示前3个文件
```

### 3. from...import * 语句

导入模块中的所有公共名称（不推荐使用）：

```python
# 不推荐的做法
from math import *

# 可以直接使用所有数学函数
result1 = sqrt(16)
result2 = sin(pi/2)
result3 = log(e)

print(f"结果: {result1}, {result2}, {result3}")

# 问题：可能导致命名空间污染
# 不清楚哪些名称来自哪个模块
```

## 使用别名

### 模块别名

为模块指定别名，简化使用：

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 使用别名
array = np.array([1, 2, 3, 4, 5])
print(f"数组: {array}")

# 常见的别名约定
import datetime as dt
import json as js
import urllib.request as request

# 使用别名
current_time = dt.datetime.now()
print(f"当前时间: {current_time}")
```

### 名称别名

为导入的名称指定别名：

```python
from math import sqrt as square_root
from math import pi as PI
from os import getcwd as get_current_directory

# 使用别名
result = square_root(16)
print(f"平方根: {result}")

print(f"圆周率: {PI}")

current_dir = get_current_directory()
print(f"当前目录: {current_dir}")

# 避免名称冲突
from math import log as math_log
from numpy import log as numpy_log

# 现在可以同时使用两个log函数而不冲突
result1 = math_log(10)
# result2 = numpy_log([1, 2, 3])  # 如果安装了numpy
```

## 条件导入

根据条件动态导入模块：

```python
import sys

# 根据Python版本导入不同的模块
if sys.version_info >= (3, 8):
    from typing import TypedDict
    print("使用Python 3.8+的TypedDict")
else:
    # 为旧版本提供替代方案
    TypedDict = dict
    print("使用dict作为TypedDict的替代")

# 根据平台导入不同的模块
if sys.platform == 'win32':
    import winsound
    print("Windows平台，导入winsound")
elif sys.platform == 'darwin':
    import subprocess
    print("macOS平台，使用subprocess")
else:
    print("Linux或其他平台")

# 可选依赖的处理
try:
    import requests
    HAS_REQUESTS = True
    print("requests库可用")
except ImportError:
    HAS_REQUESTS = False
    print("requests库不可用，将使用urllib")

def fetch_data(url):
    """根据可用的库获取数据"""
    if HAS_REQUESTS:
        response = requests.get(url)
        return response.text
    else:
        import urllib.request
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
```

## 延迟导入

在需要时才导入模块，提高启动性能：

```python
def process_json_data(data):
    """处理JSON数据的函数"""
    # 只在需要时导入json模块
    import json
    
    try:
        parsed_data = json.loads(data)
        return parsed_data
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
        return None

def generate_random_numbers(count):
    """生成随机数的函数"""
    # 只在需要时导入random模块
    import random
    
    return [random.randint(1, 100) for _ in range(count)]

def format_datetime(timestamp):
    """格式化时间戳的函数"""
    # 只在需要时导入datetime模块
    from datetime import datetime
    
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime('%Y-%m-%d %H:%M:%S')

# 测试延迟导入
if __name__ == '__main__':
    # JSON处理测试
    json_str = '{"name": "张三", "age": 25}'
    result = process_json_data(json_str)
    print(f"JSON解析结果: {result}")
    
    # 随机数生成测试
    numbers = generate_random_numbers(5)
    print(f"随机数: {numbers}")
    
    # 时间格式化测试
    import time
    current_timestamp = time.time()
    formatted_time = format_datetime(current_timestamp)
    print(f"格式化时间: {formatted_time}")
```

## 相对导入和绝对导入

### 绝对导入

从项目根目录或Python路径开始的完整路径导入：

```python
# 绝对导入示例（假设项目结构）
# myproject/
#   ├── main.py
#   ├── utils/
#   │   ├── __init__.py
#   │   ├── math_tools.py
#   │   └── string_tools.py
#   └── models/
#       ├── __init__.py
#       └── user.py

# 在main.py中使用绝对导入
from utils.math_tools import add, multiply
from utils.string_tools import capitalize_words
from models.user import User

# 使用导入的功能
result = add(5, 3)
print(f"计算结果: {result}")

formatted_text = capitalize_words("hello world")
print(f"格式化文本: {formatted_text}")

user = User("张三", 25)
print(f"用户信息: {user}")
```

### 相对导入

相对于当前模块位置的导入（只能在包内使用）：

```python
# 在utils/math_tools.py中使用相对导入
# 导入同级模块
from .string_tools import format_number

# 导入上级包中的模块
from ..models.user import User

# 导入当前包
from . import __version__

def calculate_and_format(a, b):
    """计算并格式化结果"""
    result = a + b
    return format_number(result)

def create_calculation_user(name):
    """创建计算用户"""
    return User(name, calculation_count=0)
```

## 导入路径和模块搜索

### 查看和修改模块搜索路径

```python
import sys
import os

print("=== Python模块搜索路径 ===")
for i, path in enumerate(sys.path, 1):
    print(f"{i}. {path}")

# 添加自定义路径到模块搜索路径
custom_path = "/path/to/my/modules"
if custom_path not in sys.path:
    sys.path.append(custom_path)
    print(f"\n已添加自定义路径: {custom_path}")

# 在开头插入路径（优先级更高）
sys.path.insert(0, "/high/priority/path")

# 查看特定模块的位置
import math
print(f"\nmath模块位置: {math.__file__}")

try:
    import numpy
    print(f"numpy模块位置: {numpy.__file__}")
except ImportError:
    print("numpy模块未安装")

# 查看模块搜索过程
def find_module_path(module_name):
    """查找模块路径"""
    import importlib.util
    
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        return f"模块 '{module_name}' 未找到"
    else:
        return f"模块 '{module_name}' 位置: {spec.origin}"

# 测试模块查找
modules_to_find = ['os', 'sys', 'math', 'json', 'datetime']
print("\n=== 模块位置查找 ===")
for module in modules_to_find:
    print(find_module_path(module))
```

## 动态导入

使用importlib动态导入模块：

```python
import importlib
import sys

def dynamic_import(module_name):
    """动态导入模块"""
    try:
        module = importlib.import_module(module_name)
        print(f"成功导入模块: {module_name}")
        return module
    except ImportError as e:
        print(f"导入模块失败: {module_name}, 错误: {e}")
        return None

def dynamic_import_from(module_name, attribute_name):
    """动态导入模块中的特定属性"""
    try:
        module = importlib.import_module(module_name)
        attribute = getattr(module, attribute_name)
        print(f"成功从 {module_name} 导入 {attribute_name}")
        return attribute
    except (ImportError, AttributeError) as e:
        print(f"导入失败: {module_name}.{attribute_name}, 错误: {e}")
        return None

def reload_module(module_name):
    """重新加载模块"""
    if module_name in sys.modules:
        module = sys.modules[module_name]
        importlib.reload(module)
        print(f"模块 {module_name} 已重新加载")
        return module
    else:
        print(f"模块 {module_name} 未加载，无法重新加载")
        return None

# 测试动态导入
if __name__ == '__main__':
    print("=== 动态导入测试 ===")
    
    # 动态导入标准库模块
    math_module = dynamic_import('math')
    if math_module:
        print(f"π的值: {math_module.pi}")
        print(f"sqrt(16) = {math_module.sqrt(16)}")
    
    # 动态导入特定函数
    sqrt_func = dynamic_import_from('math', 'sqrt')
    if sqrt_func:
        print(f"使用动态导入的sqrt: {sqrt_func(25)}")
    
    # 尝试导入不存在的模块
    fake_module = dynamic_import('nonexistent_module')
    
    # 根据条件动态选择模块
    json_modules = ['ujson', 'simplejson', 'json']
    json_module = None
    
    for module_name in json_modules:
        json_module = dynamic_import(module_name)
        if json_module:
            print(f"使用JSON模块: {module_name}")
            break
    
    if json_module:
        test_data = {"name": "测试", "value": 123}
        json_str = json_module.dumps(test_data)
        print(f"JSON序列化结果: {json_str}")
```

## 导入钩子和自定义导入

### 导入钩子示例

```python
import sys
import importlib.util
from importlib.abc import MetaPathFinder, Loader
from importlib.machinery import ModuleSpec

class CustomImportHook(MetaPathFinder):
    """自定义导入钩子"""
    
    def find_spec(self, fullname, path, target=None):
        """查找模块规范"""
        if fullname.startswith('custom_'):
            print(f"自定义导入钩子处理: {fullname}")
            # 这里可以实现自定义的模块查找逻辑
            return None
        return None

def install_import_hook():
    """安装自定义导入钩子"""
    hook = CustomImportHook()
    if hook not in sys.meta_path:
        sys.meta_path.insert(0, hook)
        print("自定义导入钩子已安装")

def remove_import_hook():
    """移除自定义导入钩子"""
    sys.meta_path = [hook for hook in sys.meta_path 
                     if not isinstance(hook, CustomImportHook)]
    print("自定义导入钩子已移除")

# 测试导入钩子
if __name__ == '__main__':
    print("=== 导入钩子测试 ===")
    
    # 安装钩子
    install_import_hook()
    
    # 尝试导入自定义模块（会触发钩子）
    try:
        import custom_test_module
    except ImportError:
        print("custom_test_module 导入失败（预期行为）")
    
    # 移除钩子
    remove_import_hook()
```

## 导入性能优化

### 导入时间测量

```python
import time
import sys

def measure_import_time(module_name):
    """测量模块导入时间"""
    start_time = time.time()
    
    try:
        __import__(module_name)
        end_time = time.time()
        import_time = (end_time - start_time) * 1000  # 转换为毫秒
        print(f"{module_name}: {import_time:.2f}ms")
        return import_time
    except ImportError as e:
        print(f"{module_name}: 导入失败 - {e}")
        return None

def compare_import_methods():
    """比较不同导入方法的性能"""
    print("=== 导入性能比较 ===")
    
    # 测试不同的导入方式
    modules_to_test = [
        'os', 'sys', 'math', 'json', 'datetime',
        'collections', 'itertools', 'functools'
    ]
    
    total_time = 0
    for module in modules_to_test:
        import_time = measure_import_time(module)
        if import_time:
            total_time += import_time
    
    print(f"\n总导入时间: {total_time:.2f}ms")
    print(f"平均导入时间: {total_time/len(modules_to_test):.2f}ms")

# 导入优化建议
def import_optimization_tips():
    """导入优化建议"""
    print("\n=== 导入优化建议 ===")
    print("1. 避免在函数内部进行重复导入")
    print("2. 使用延迟导入减少启动时间")
    print("3. 避免使用 'from module import *'")
    print("4. 将导入语句放在文件顶部")
    print("5. 按照标准库、第三方库、本地模块的顺序组织导入")
    print("6. 使用绝对导入而不是相对导入（在可能的情况下）")
    print("7. 避免循环导入")

if __name__ == '__main__':
    compare_import_methods()
    import_optimization_tips()
```

## 导入最佳实践

### 1. 导入顺序

```python
# 1. 标准库导入
import os
import sys
import json
from datetime import datetime
from typing import List, Dict, Optional

# 2. 第三方库导入
import requests
import numpy as np
import pandas as pd

# 3. 本地应用/库导入
from .utils import helper_function
from ..models import User
from myapp.config import settings
```

### 2. 导入风格指南

```python
# 推荐的导入方式
import os
import sys
from math import sqrt, pi
from typing import List, Dict

# 不推荐的导入方式
# from math import *  # 避免使用
# import os, sys     # 避免在一行导入多个模块
```

### 3. 错误处理

```python
# 优雅地处理可选依赖
try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("matplotlib未安装，图表功能将不可用")

def plot_data(data):
    """绘制数据图表"""
    if not HAS_MATPLOTLIB:
        print("需要安装matplotlib才能使用绘图功能")
        return
    
    plt.plot(data)
    plt.show()
```

## 学习要点

1. **选择合适的导入方式**：根据使用频率和代码可读性选择
2. **使用别名**：为长模块名或避免冲突使用别名
3. **避免通配符导入**：`from module import *` 可能导致命名空间污染
4. **延迟导入**：在需要时才导入，提高启动性能
5. **处理导入错误**：优雅地处理可选依赖和导入失败
6. **遵循PEP 8**：按照标准组织导入语句

## 常见问题和解决方案

### 1. 循环导入问题

```python
# 问题：模块A导入模块B，模块B又导入模块A
# 解决方案：
# 1. 重新设计模块结构
# 2. 使用延迟导入
# 3. 将共同依赖提取到第三个模块

# 延迟导入解决循环导入
def get_user_data():
    from .models import User  # 延迟导入
    return User.get_all()
```

### 2. 模块未找到错误

```python
# 检查模块是否存在
import importlib.util

def check_module_exists(module_name):
    """检查模块是否存在"""
    spec = importlib.util.find_spec(module_name)
    return spec is not None

# 使用示例
if check_module_exists('requests'):
    import requests
else:
    print("请安装requests库: pip install requests")
```

通过掌握这些导入语句的用法，你可以更好地组织和管理Python代码，提高代码的可读性和可维护性。