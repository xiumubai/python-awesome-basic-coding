# 02. try-except语法

## 学习目标

- 掌握try-except语句的完整语法结构
- 学会不同形式的异常捕获方法
- 理解异常捕获的执行流程
- 掌握异常处理的最佳实践

## try-except基本语法

### 1. 最简单的形式

```python
try:
    # 可能出现异常的代码
    risky_code()
except:
    # 处理所有异常
    print("发生了异常")
```

**注意**：这种形式会捕获所有异常，通常不推荐使用。

### 2. 捕获特定异常

```python
try:
    number = int(input("请输入一个数字: "))
    result = 10 / number
except ValueError:
    print("输入的不是有效数字")
except ZeroDivisionError:
    print("不能除以零")
```

### 3. 捕获异常对象

```python
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"文件操作失败: {e}")
    print(f"错误代码: {e.errno}")
    print(f"错误描述: {e.strerror}")
```

## 异常捕获的不同形式

### 1. 捕获单个异常

```python
def divide_numbers(a, b):
    """安全的除法运算"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("错误: 除数不能为零")
        return None

# 测试
print(divide_numbers(10, 2))  # 5.0
print(divide_numbers(10, 0))  # None
```

### 2. 捕获多个异常（分别处理）

```python
def safe_conversion(value, target_type):
    """安全的类型转换"""
    try:
        if target_type == "int":
            return int(value)
        elif target_type == "float":
            return float(value)
        elif target_type == "complex":
            return complex(value)
    except ValueError as e:
        print(f"值错误: {e}")
        return None
    except TypeError as e:
        print(f"类型错误: {e}")
        return None
    except OverflowError as e:
        print(f"数值溢出: {e}")
        return None

# 测试不同情况
print(safe_conversion("123", "int"))      # 123
print(safe_conversion("abc", "int"))      # None (ValueError)
print(safe_conversion(None, "int"))       # None (TypeError)
```

### 3. 捕获多个异常（统一处理）

```python
def process_user_input(user_input):
    """处理用户输入"""
    try:
        # 尝试各种处理
        number = float(user_input)
        result = 100 / number
        index = int(number)
        my_list = [1, 2, 3, 4, 5]
        value = my_list[index]
        return {"result": result, "list_value": value}
    except (ValueError, TypeError) as e:
        print(f"输入格式错误: {e}")
        return None
    except (ZeroDivisionError, IndexError) as e:
        print(f"计算或访问错误: {e}")
        return None

# 测试
print(process_user_input("2"))     # {'result': 50.0, 'list_value': 3}
print(process_user_input("abc"))   # None (ValueError)
print(process_user_input("0"))     # None (ZeroDivisionError)
print(process_user_input("10"))    # None (IndexError)
```

### 4. 捕获异常层次结构

```python
def demonstrate_exception_hierarchy():
    """演示异常层次结构的捕获"""
    test_cases = [
        lambda: [][0],                    # IndexError
        lambda: {}["key"],               # KeyError
        lambda: int("abc"),              # ValueError
        lambda: "string" + 5,            # TypeError
    ]
    
    for i, test_func in enumerate(test_cases):
        try:
            test_func()
        except LookupError as e:
            print(f"测试 {i+1}: 捕获到查找错误 - {type(e).__name__}: {e}")
        except ValueError as e:
            print(f"测试 {i+1}: 捕获到值错误 - {type(e).__name__}: {e}")
        except Exception as e:
            print(f"测试 {i+1}: 捕获到其他异常 - {type(e).__name__}: {e}")

demonstrate_exception_hierarchy()
```

## 异常处理的执行流程

### 1. 正常执行流程

```python
def normal_flow_demo():
    """演示正常执行流程"""
    print("1. 开始执行")
    
    try:
        print("2. 进入try块")
        result = 10 / 2
        print(f"3. 计算结果: {result}")
        print("4. try块执行完成")
    except ZeroDivisionError:
        print("5. 这行不会执行（没有异常）")
    
    print("6. 继续执行后续代码")

normal_flow_demo()
```

### 2. 异常执行流程

```python
def exception_flow_demo():
    """演示异常执行流程"""
    print("1. 开始执行")
    
    try:
        print("2. 进入try块")
        result = 10 / 0  # 这里会抛出异常
        print("3. 这行不会执行（异常已抛出）")
    except ZeroDivisionError as e:
        print(f"4. 捕获到异常: {e}")
        print("5. 处理异常")
    
    print("6. 继续执行后续代码")

exception_flow_demo()
```

### 3. 未捕获异常的流程

```python
def uncaught_exception_demo():
    """演示未捕获异常的处理"""
    try:
        print("尝试执行可能出错的代码")
        
        try:
            result = 10 / 0
        except ValueError:  # 这个except不会捕获ZeroDivisionError
            print("这个except不会执行")
        
        print("这行也不会执行")
    except ZeroDivisionError as e:
        print(f"外层捕获到异常: {e}")

uncaught_exception_demo()
```

## 异常信息的详细获取

### 1. 基本异常信息

```python
def get_exception_info():
    """获取详细的异常信息"""
    try:
        # 故意触发异常
        my_dict = {"a": 1, "b": 2}
        value = my_dict["c"]
    except KeyError as e:
        print(f"异常类型: {type(e).__name__}")
        print(f"异常消息: {str(e)}")
        print(f"异常参数: {e.args}")
        print(f"异常表示: {repr(e)}")

get_exception_info()
```

### 2. 使用traceback模块

```python
import traceback
import sys

def detailed_exception_info():
    """获取详细的异常追踪信息"""
    try:
        def level_1():
            level_2()
        
        def level_2():
            level_3()
        
        def level_3():
            raise ValueError("这是一个测试异常")
        
        level_1()
    except ValueError as e:
        print("=== 异常基本信息 ===")
        print(f"异常类型: {type(e).__name__}")
        print(f"异常消息: {e}")
        
        print("\n=== 异常追踪信息 ===")
        traceback.print_exc()
        
        print("\n=== 格式化的追踪信息 ===")
        tb_lines = traceback.format_exception(*sys.exc_info())
        for line in tb_lines:
            print(line.rstrip())

detailed_exception_info()
```

## 实际应用场景

### 1. 网络请求处理

```python
import urllib.request
import urllib.error
import json

def fetch_data_from_api(url):
    """从API获取数据的安全方法"""
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = response.read().decode('utf-8')
            return json.loads(data)
    except urllib.error.HTTPError as e:
        print(f"HTTP错误 {e.code}: {e.reason}")
        return None
    except urllib.error.URLError as e:
        print(f"URL错误: {e.reason}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
        return None
    except Exception as e:
        print(f"未知错误: {e}")
        return None

# 模拟使用（实际使用时需要有效的URL）
# data = fetch_data_from_api("https://api.example.com/data")
# if data:
#     print("获取数据成功:", data)
```

### 2. 数据库操作

```python
class DatabaseConnection:
    """模拟数据库连接类"""
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connected = False
    
    def connect(self):
        # 模拟连接过程
        if "invalid" in self.connection_string:
            raise ConnectionError("无法连接到数据库")
        self.connected = True
    
    def execute_query(self, query):
        if not self.connected:
            raise RuntimeError("数据库未连接")
        if "DROP" in query.upper():
            raise PermissionError("没有删除权限")
        return f"执行查询: {query}"
    
    def close(self):
        self.connected = False

def safe_database_operation(connection_string, query):
    """安全的数据库操作"""
    db = None
    try:
        print("正在连接数据库...")
        db = DatabaseConnection(connection_string)
        db.connect()
        print("数据库连接成功")
        
        print("正在执行查询...")
        result = db.execute_query(query)
        print(f"查询结果: {result}")
        return result
        
    except ConnectionError as e:
        print(f"连接错误: {e}")
        return None
    except PermissionError as e:
        print(f"权限错误: {e}")
        return None
    except RuntimeError as e:
        print(f"运行时错误: {e}")
        return None
    except Exception as e:
        print(f"未知错误: {e}")
        return None
    finally:
        if db and db.connected:
            db.close()
            print("数据库连接已关闭")

# 测试不同情况
print("=== 正常情况 ===")
safe_database_operation("valid_connection", "SELECT * FROM users")

print("\n=== 连接错误 ===")
safe_database_operation("invalid_connection", "SELECT * FROM users")

print("\n=== 权限错误 ===")
safe_database_operation("valid_connection", "DROP TABLE users")
```

### 3. 配置文件处理

```python
import json
import os

def load_config(config_file):
    """安全地加载配置文件"""
    default_config = {
        "host": "localhost",
        "port": 8080,
        "debug": False
    }
    
    try:
        # 检查文件是否存在
        if not os.path.exists(config_file):
            print(f"配置文件 {config_file} 不存在，使用默认配置")
            return default_config
        
        # 读取配置文件
        with open(config_file, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
        
        # 验证配置
        if not isinstance(config_data, dict):
            raise ValueError("配置文件格式错误：根元素必须是对象")
        
        # 合并默认配置
        final_config = default_config.copy()
        final_config.update(config_data)
        
        print(f"成功加载配置文件: {config_file}")
        return final_config
        
    except FileNotFoundError:
        print(f"配置文件 {config_file} 未找到")
        return default_config
    except PermissionError:
        print(f"没有权限读取配置文件 {config_file}")
        return default_config
    except json.JSONDecodeError as e:
        print(f"配置文件JSON格式错误: {e}")
        return default_config
    except ValueError as e:
        print(f"配置文件内容错误: {e}")
        return default_config
    except Exception as e:
        print(f"加载配置文件时发生未知错误: {e}")
        return default_config

# 测试配置加载
config = load_config("app_config.json")
print(f"最终配置: {config}")
```

## 异常处理的最佳实践

### 1. 具体异常优于通用异常

```python
# 好的做法
def good_exception_handling(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
    except PermissionError:
        print(f"没有权限读取文件 {filename}")
    except IsADirectoryError:
        print(f"{filename} 是一个目录，不是文件")
    return None

# 不推荐的做法
def bad_exception_handling(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except Exception as e:  # 过于宽泛
        print(f"出现错误: {e}")
    return None
```

### 2. 不要忽略异常

```python
# 不好的做法
def bad_ignore_exception():
    try:
        risky_operation()
    except:
        pass  # 静默忽略所有异常

# 好的做法
def good_exception_logging():
    import logging
    
    try:
        risky_operation()
    except SpecificException as e:
        logging.error(f"操作失败: {e}")
        # 进行适当的清理或恢复操作
    except Exception as e:
        logging.critical(f"未预期的错误: {e}")
        raise  # 重新抛出未知异常
```

### 3. 异常处理要有意义

```python
def meaningful_exception_handling(user_data):
    """有意义的异常处理示例"""
    try:
        # 验证用户数据
        age = int(user_data.get('age', 0))
        if age < 0:
            raise ValueError("年龄不能为负数")
        if age > 150:
            raise ValueError("年龄不能超过150")
        
        # 处理数据
        return process_user_age(age)
        
    except ValueError as e:
        # 提供有用的错误信息
        error_msg = f"用户年龄数据无效: {e}"
        print(error_msg)
        
        # 记录错误用于调试
        import logging
        logging.warning(error_msg, extra={'user_data': user_data})
        
        # 返回安全的默认值
        return None
    except KeyError as e:
        print(f"缺少必要的用户数据字段: {e}")
        return None

def process_user_age(age):
    """模拟处理用户年龄的函数"""
    return f"用户年龄: {age}岁"

# 测试
test_data = [
    {'age': '25'},      # 正常情况
    {'age': 'abc'},     # ValueError
    {'age': '-5'},      # ValueError
    {'name': 'John'},   # KeyError
]

for data in test_data:
    result = meaningful_exception_handling(data)
    print(f"处理结果: {result}\n")
```

## 学习要点总结

### 核心语法
1. **基本结构**: `try-except`是异常处理的基础语法
2. **异常捕获**: 可以捕获特定异常、多个异常或异常对象
3. **执行流程**: 理解异常发生时的程序执行路径
4. **异常信息**: 学会获取和使用异常的详细信息

### 最佳实践
1. **具体异常**: 优先捕获具体的异常类型
2. **有意义处理**: 异常处理要提供有用的信息和恢复机制
3. **不要忽略**: 即使无法处理也要记录异常
4. **层次结构**: 利用异常的继承关系进行分层处理

### 实际应用
- 网络请求的错误处理
- 数据库操作的异常管理
- 文件操作的安全处理
- 用户输入的验证和处理

## 下一步学习

掌握了基本的try-except语法后，接下来将学习：
- [03. 多异常处理](./03_multiple_except.md) - 更复杂的异常处理场景
- [04. else和finally子句](./04_else_finally.md) - 完整的异常处理结构
- [05. 抛出异常](./05_raise_exception.md) - 主动抛出异常的技巧

通过掌握try-except语法，你已经具备了处理大多数异常情况的能力，这是编写健壮Python程序的重要基础。