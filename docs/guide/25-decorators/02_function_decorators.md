# 函数装饰器的定义和使用

函数装饰器是装饰器最常见的形式，它们可以处理各种复杂的场景，包括带参数的函数、返回值处理等。

## 处理带参数的函数

在实际应用中，大多数函数都有参数。我们需要创建能够处理任意参数的装饰器。

### 使用*args和**kwargs

```python
def universal_decorator(func):
    """通用装饰器，可以装饰任意函数"""
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        print(f"位置参数: {args}")
        print(f"关键字参数: {kwargs}")
        
        # 调用原函数并获取结果
        result = func(*args, **kwargs)
        
        print(f"函数返回值: {result}")
        return result
    return wrapper

@universal_decorator
def add(a, b):
    """加法函数"""
    return a + b

@universal_decorator
def greet(name, greeting="Hello"):
    """问候函数"""
    return f"{greeting}, {name}!"

# 测试
result1 = add(3, 5)
print(f"加法结果: {result1}\n")

result2 = greet("Alice")
print(f"问候结果: {result2}\n")

result3 = greet("Bob", greeting="Hi")
print(f"自定义问候: {result3}")
```

## 常用装饰器模式

### 1. 日志装饰器

```python
import functools
import datetime

def log_function_call(func):
    """记录函数调用的详细信息"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 记录调用开始
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] 开始调用: {func.__name__}")
        
        # 记录参数
        if args:
            print(f"  位置参数: {args}")
        if kwargs:
            print(f"  关键字参数: {kwargs}")
        
        try:
            # 执行函数
            result = func(*args, **kwargs)
            print(f"[{timestamp}] 成功完成: {func.__name__}，返回值: {result}")
            return result
        except Exception as e:
            print(f"[{timestamp}] 执行失败: {func.__name__}，错误: {e}")
            raise
    
    return wrapper

@log_function_call
def divide(a, b):
    """除法函数"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

# 测试正常情况
result = divide(10, 2)
print(f"结果: {result}\n")

# 测试异常情况
try:
    divide(10, 0)
except ValueError as e:
    print(f"捕获异常: {e}")
```

### 2. 性能监控装饰器

```python
import time
import functools

def performance_monitor(func):
    """监控函数性能的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 记录开始时间
        start_time = time.time()
        start_memory = get_memory_usage()  # 假设有这个函数
        
        print(f"开始执行 {func.__name__}...")
        
        try:
            # 执行函数
            result = func(*args, **kwargs)
            
            # 计算执行时间
            end_time = time.time()
            execution_time = end_time - start_time
            
            print(f"函数 {func.__name__} 执行完成")
            print(f"执行时间: {execution_time:.4f} 秒")
            
            return result
            
        except Exception as e:
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"函数 {func.__name__} 执行失败")
            print(f"执行时间: {execution_time:.4f} 秒")
            raise
    
    return wrapper

def get_memory_usage():
    """获取内存使用情况（简化版）"""
    return 0  # 简化实现

@performance_monitor
def fibonacci(n):
    """计算斐波那契数列"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@performance_monitor
def factorial(n):
    """计算阶乘"""
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 测试性能监控
print("计算斐波那契数列:")
fib_result = fibonacci(10)
print(f"fibonacci(10) = {fib_result}\n")

print("计算阶乘:")
fact_result = factorial(10)
print(f"factorial(10) = {fact_result}")
```

### 3. 缓存装饰器

```python
import functools

def simple_cache(func):
    """简单的缓存装饰器"""
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 创建缓存键
        key = str(args) + str(sorted(kwargs.items()))
        
        # 检查缓存
        if key in cache:
            print(f"缓存命中: {func.__name__}{args}")
            return cache[key]
        
        # 计算结果并缓存
        print(f"计算中: {func.__name__}{args}")
        result = func(*args, **kwargs)
        cache[key] = result
        
        return result
    
    # 添加清除缓存的方法
    wrapper.clear_cache = lambda: cache.clear()
    wrapper.cache_info = lambda: f"缓存大小: {len(cache)}"
    
    return wrapper

@simple_cache
def expensive_calculation(n):
    """模拟耗时计算"""
    time.sleep(1)  # 模拟耗时操作
    return n * n

# 测试缓存功能
print("第一次调用:")
result1 = expensive_calculation(5)
print(f"结果: {result1}\n")

print("第二次调用相同参数:")
result2 = expensive_calculation(5)
print(f"结果: {result2}\n")

print("调用不同参数:")
result3 = expensive_calculation(3)
print(f"结果: {result3}\n")

print(expensive_calculation.cache_info())
```

### 4. 权限检查装饰器

```python
import functools

# 模拟用户权限系统
current_user = {"name": "Alice", "role": "admin"}

def require_permission(permission):
    """权限检查装饰器工厂"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 检查用户权限
            user_permissions = get_user_permissions(current_user)
            
            if permission not in user_permissions:
                raise PermissionError(f"用户 {current_user['name']} 没有 '{permission}' 权限")
            
            print(f"权限检查通过: {permission}")
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

def get_user_permissions(user):
    """获取用户权限"""
    permissions_map = {
        "admin": ["read", "write", "delete"],
        "user": ["read"],
        "guest": []
    }
    return permissions_map.get(user["role"], [])

@require_permission("read")
def read_data():
    """读取数据"""
    return "数据内容"

@require_permission("write")
def write_data(data):
    """写入数据"""
    return f"已写入: {data}"

@require_permission("delete")
def delete_data(data_id):
    """删除数据"""
    return f"已删除ID为 {data_id} 的数据"

# 测试权限系统
print(f"当前用户: {current_user['name']} ({current_user['role']})\n")

try:
    # 测试读取权限
    data = read_data()
    print(f"读取成功: {data}\n")
    
    # 测试写入权限
    write_result = write_data("新数据")
    print(f"写入成功: {write_result}\n")
    
    # 测试删除权限
    delete_result = delete_data(123)
    print(f"删除成功: {delete_result}\n")
    
except PermissionError as e:
    print(f"权限错误: {e}")

# 切换到普通用户
current_user = {"name": "Bob", "role": "user"}
print(f"切换用户: {current_user['name']} ({current_user['role']})\n")

try:
    # 普通用户尝试删除
    delete_data(456)
except PermissionError as e:
    print(f"权限错误: {e}")
```

### 5. 重试装饰器

```python
import functools
import time
import random

def retry(max_attempts=3, delay=1, backoff=2):
    """重试装饰器
    
    Args:
        max_attempts: 最大重试次数
        delay: 初始延迟时间（秒）
        backoff: 延迟时间倍数
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            
            for attempt in range(max_attempts):
                try:
                    print(f"尝试第 {attempt + 1} 次调用 {func.__name__}")
                    result = func(*args, **kwargs)
                    print(f"成功完成 {func.__name__}")
                    return result
                    
                except Exception as e:
                    print(f"第 {attempt + 1} 次尝试失败: {e}")
                    
                    if attempt < max_attempts - 1:
                        print(f"等待 {current_delay} 秒后重试...")
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        print(f"所有 {max_attempts} 次尝试都失败了")
                        raise
        
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5, backoff=2)
def unstable_network_request():
    """模拟不稳定的网络请求"""
    if random.random() < 0.7:  # 70%的概率失败
        raise ConnectionError("网络连接失败")
    return "请求成功"

@retry(max_attempts=2, delay=1)
def database_operation():
    """模拟数据库操作"""
    if random.random() < 0.5:  # 50%的概率失败
        raise Exception("数据库连接超时")
    return "数据库操作成功"

# 测试重试功能
print("测试网络请求重试:")
try:
    result = unstable_network_request()
    print(f"最终结果: {result}\n")
except Exception as e:
    print(f"最终失败: {e}\n")

print("测试数据库操作重试:")
try:
    result = database_operation()
    print(f"最终结果: {result}")
except Exception as e:
    print(f"最终失败: {e}")
```

## 装饰器的最佳实践

### 1. 使用functools.wraps

```python
import functools

def good_decorator(func):
    """正确的装饰器实现"""
    @functools.wraps(func)  # 保持原函数的元信息
    def wrapper(*args, **kwargs):
        # 装饰器逻辑
        return func(*args, **kwargs)
    return wrapper

def bad_decorator(func):
    """不好的装饰器实现"""
    def wrapper(*args, **kwargs):
        # 装饰器逻辑
        return func(*args, **kwargs)
    return wrapper  # 没有使用functools.wraps

@good_decorator
def example_function():
    """这是一个示例函数"""
    pass

print(f"函数名: {example_function.__name__}")  # 输出: example_function
print(f"文档字符串: {example_function.__doc__}")  # 输出: 这是一个示例函数
```

### 2. 处理异常

```python
import functools

def safe_decorator(func):
    """安全的装饰器，处理异常"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"函数 {func.__name__} 执行时发生异常: {e}")
            # 可以选择重新抛出异常或返回默认值
            raise
    return wrapper
```

### 3. 提供配置选项

```python
import functools

def configurable_decorator(enabled=True, log_level="INFO"):
    """可配置的装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if enabled:
                if log_level == "DEBUG":
                    print(f"DEBUG: 调用 {func.__name__} with args={args}, kwargs={kwargs}")
                elif log_level == "INFO":
                    print(f"INFO: 调用 {func.__name__}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@configurable_decorator(enabled=True, log_level="DEBUG")
def test_function(x, y=10):
    return x + y

result = test_function(5, y=15)
print(f"结果: {result}")
```

## 小结

函数装饰器是Python中非常强大的工具，通过本章的学习，我们掌握了：

1. **通用装饰器模式**：使用*args和**kwargs处理任意参数
2. **常用装饰器类型**：日志、性能监控、缓存、权限检查、重试等
3. **最佳实践**：使用functools.wraps、异常处理、提供配置选项

这些模式和技术为我们在实际项目中使用装饰器提供了坚实的基础。在下一章中，我们将学习如何创建带参数的装饰器，进一步提高装饰器的灵活性。