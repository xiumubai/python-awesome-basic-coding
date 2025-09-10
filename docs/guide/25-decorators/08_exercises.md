# 装饰器综合练习

本章包含8个综合练习，涵盖了装饰器的各个方面。通过这些练习，你将能够熟练掌握装饰器的设计和实现。

## 练习1：基础装饰器实现

实现三个基础装饰器：日志记录、执行计时和异常处理。

### 日志装饰器

```python
import functools
import time
from datetime import datetime

def log_calls(func):
    """记录函数调用的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        args_str = ', '.join(map(str, args))
        kwargs_str = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        
        print(f"[{timestamp}] 调用函数 {func.__name__}({all_args})")
        
        try:
            result = func(*args, **kwargs)
            print(f"[{timestamp}] 函数 {func.__name__} 返回: {result}")
            return result
        except Exception as e:
            print(f"[{timestamp}] 函数 {func.__name__} 抛出异常: {e}")
            raise
    
    return wrapper

@log_calls
def add_numbers(a, b):
    """加法函数"""
    return a + b

@log_calls
def divide_numbers(a, b):
    """除法函数"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

print("=== 日志装饰器测试 ===")
result1 = add_numbers(5, 3)
print(f"结果: {result1}\n")

try:
    result2 = divide_numbers(10, 0)
except ValueError as e:
    print(f"捕获异常: {e}\n")

result3 = divide_numbers(10, 2)
print(f"结果: {result3}\n")
```

### 计时装饰器

```python
def timing_decorator(func):
    """测量函数执行时间的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        
        print(f"函数 {func.__name__} 执行时间: {execution_time:.6f}秒")
        return result
    
    return wrapper

@timing_decorator
def slow_function():
    """模拟耗时操作"""
    time.sleep(0.1)
    return "操作完成"

@timing_decorator
def fibonacci(n):
    """计算斐波那契数列"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("=== 计时装饰器测试 ===")
result = slow_function()
print(f"结果: {result}\n")

fib_result = fibonacci(10)
print(f"fibonacci(10) = {fib_result}\n")
```

### 异常处理装饰器

```python
def exception_handler(*exception_types):
    """异常处理装饰器工厂"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_types as e:
                print(f"捕获到异常 {type(e).__name__}: {e}")
                print(f"函数 {func.__name__} 执行失败，返回默认值")
                return None
            except Exception as e:
                print(f"未预期的异常 {type(e).__name__}: {e}")
                raise
        return wrapper
    return decorator

@exception_handler(ValueError, TypeError)
def risky_operation(x, y):
    """可能出错的操作"""
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("参数必须是数字")
    if y == 0:
        raise ValueError("除数不能为零")
    return x / y

print("=== 异常处理装饰器测试 ===")
result1 = risky_operation(10, 2)
print(f"正常结果: {result1}\n")

result2 = risky_operation(10, 0)  # ValueError
print(f"异常处理结果: {result2}\n")

result3 = risky_operation("10", 2)  # TypeError
print(f"异常处理结果: {result3}\n")
```

## 练习2：带参数的装饰器

实现可配置的装饰器，支持不同的参数设置。

### 可配置重试装饰器

```python
def retry(max_attempts=3, delay=1.0, exceptions=(Exception,)):
    """重试装饰器
    
    Args:
        max_attempts: 最大重试次数
        delay: 重试间隔（秒）
        exceptions: 需要重试的异常类型
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    print(f"尝试执行 {func.__name__} (第 {attempt + 1} 次)")
                    result = func(*args, **kwargs)
                    if attempt > 0:
                        print(f"函数 {func.__name__} 在第 {attempt + 1} 次尝试后成功")
                    return result
                except exceptions as e:
                    last_exception = e
                    print(f"第 {attempt + 1} 次尝试失败: {e}")
                    if attempt < max_attempts - 1:
                        print(f"等待 {delay} 秒后重试...")
                        time.sleep(delay)
                except Exception as e:
                    print(f"遇到不可重试的异常: {e}")
                    raise
            
            print(f"函数 {func.__name__} 在 {max_attempts} 次尝试后仍然失败")
            raise last_exception
        
        return wrapper
    return decorator

# 模拟不稳定的网络请求
import random

@retry(max_attempts=5, delay=0.5, exceptions=(ConnectionError, TimeoutError))
def unstable_network_request(url):
    """模拟不稳定的网络请求"""
    if random.random() < 0.7:  # 70%的概率失败
        error_type = random.choice([ConnectionError, TimeoutError])
        raise error_type(f"请求 {url} 失败")
    return f"成功获取 {url} 的数据"

print("=== 重试装饰器测试 ===")
try:
    result = unstable_network_request("https://api.example.com/data")
    print(f"最终结果: {result}\n")
except Exception as e:
    print(f"最终失败: {e}\n")
```

### 可配置缓存装饰器

```python
def cache_with_ttl(ttl_seconds=60, max_size=128):
    """带TTL的缓存装饰器
    
    Args:
        ttl_seconds: 缓存过期时间（秒）
        max_size: 最大缓存条目数
    """
    def decorator(func):
        cache = {}
        access_times = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 创建缓存键
            key = str(args) + str(sorted(kwargs.items()))
            current_time = time.time()
            
            # 检查缓存是否存在且未过期
            if key in cache:
                cached_time = access_times[key]
                if current_time - cached_time < ttl_seconds:
                    print(f"缓存命中: {func.__name__}{args}")
                    return cache[key]
                else:
                    print(f"缓存过期: {func.__name__}{args}")
                    del cache[key]
                    del access_times[key]
            
            # 检查缓存大小限制
            if len(cache) >= max_size:
                # 删除最旧的缓存项
                oldest_key = min(access_times.keys(), key=access_times.get)
                del cache[oldest_key]
                del access_times[oldest_key]
                print(f"缓存已满，删除最旧项")
            
            # 执行函数并缓存结果
            print(f"执行函数: {func.__name__}{args}")
            result = func(*args, **kwargs)
            cache[key] = result
            access_times[key] = current_time
            
            return result
        
        # 添加缓存管理方法
        def clear_cache():
            cache.clear()
            access_times.clear()
            print("缓存已清空")
        
        def cache_info():
            return {
                'cache_size': len(cache),
                'max_size': max_size,
                'ttl_seconds': ttl_seconds,
                'cached_keys': list(cache.keys())
            }
        
        wrapper.clear_cache = clear_cache
        wrapper.cache_info = cache_info
        
        return wrapper
    return decorator

@cache_with_ttl(ttl_seconds=3, max_size=3)
def expensive_calculation(n):
    """模拟昂贵的计算"""
    time.sleep(0.1)  # 模拟计算时间
    return n ** 2 + n + 1

print("=== TTL缓存装饰器测试 ===")

# 测试缓存功能
for i in range(3):
    result = expensive_calculation(i)
    print(f"expensive_calculation({i}) = {result}")

print(f"\n缓存信息: {expensive_calculation.cache_info()}")

# 测试缓存命中
print("\n--- 测试缓存命中 ---")
result = expensive_calculation(1)
print(f"expensive_calculation(1) = {result}")

# 等待缓存过期
print("\n--- 等待缓存过期 ---")
time.sleep(4)
result = expensive_calculation(1)
print(f"expensive_calculation(1) = {result}")

# 测试缓存大小限制
print("\n--- 测试缓存大小限制 ---")
for i in range(5):
    result = expensive_calculation(i + 10)
    print(f"expensive_calculation({i + 10}) = {result}")
    print(f"当前缓存大小: {expensive_calculation.cache_info()['cache_size']}")
```

## 练习3：类装饰器实现

实现类装饰器来增强类的功能。

### 单例装饰器

```python
def singleton(cls):
    """单例装饰器"""
    instances = {}
    
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            print(f"创建 {cls.__name__} 的新实例")
            instances[cls] = cls(*args, **kwargs)
        else:
            print(f"返回 {cls.__name__} 的现有实例")
        return instances[cls]
    
    return get_instance

@singleton
class DatabaseConnection:
    """数据库连接类（单例）"""
    
    def __init__(self, host="localhost", port=5432):
        self.host = host
        self.port = port
        self.connected = False
        print(f"初始化数据库连接: {host}:{port}")
    
    def connect(self):
        if not self.connected:
            print(f"连接到数据库 {self.host}:{self.port}")
            self.connected = True
        else:
            print("数据库已连接")
    
    def disconnect(self):
        if self.connected:
            print(f"断开数据库连接 {self.host}:{self.port}")
            self.connected = False
        else:
            print("数据库未连接")

print("=== 单例装饰器测试 ===")

# 创建多个实例，应该返回同一个对象
db1 = DatabaseConnection()
db2 = DatabaseConnection("remote_host", 3306)  # 参数会被忽略
db3 = DatabaseConnection()

print(f"db1 is db2: {db1 is db2}")
print(f"db2 is db3: {db2 is db3}")
print(f"db1.host: {db1.host}, db2.host: {db2.host}")

db1.connect()
db2.connect()  # 同一个实例，已经连接
```

### 自动属性装饰器

```python
def auto_property(cls):
    """自动为类的属性添加getter和setter的装饰器"""
    
    # 获取所有以下划线开头的属性（私有属性）
    private_attrs = [attr for attr in dir(cls) if attr.startswith('_') and not attr.startswith('__')]
    
    for attr in private_attrs:
        prop_name = attr[1:]  # 去掉下划线前缀
        
        # 创建getter
        def make_getter(attribute):
            def getter(self):
                return getattr(self, attribute)
            return getter
        
        # 创建setter
        def make_setter(attribute):
            def setter(self, value):
                print(f"设置 {attribute[1:]} = {value}")
                setattr(self, attribute, value)
            return setter
        
        # 创建property并添加到类中
        prop = property(make_getter(attr), make_setter(attr))
        setattr(cls, prop_name, prop)
    
    return cls

@auto_property
class Person:
    """人员类（自动属性）"""
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._email = None
    
    def __str__(self):
        return f"Person(name={self._name}, age={self._age}, email={self._email})"

print("\n=== 自动属性装饰器测试 ===")

person = Person("Alice", 25)
print(f"初始状态: {person}")

# 使用自动生成的属性
print(f"姓名: {person.name}")
print(f"年龄: {person.age}")

# 设置属性值
person.name = "Alice Smith"
person.age = 26
person.email = "alice@example.com"

print(f"更新后: {person}")
```

## 练习4：装饰器嵌套使用

演示多个装饰器的组合使用。

```python
# 组合使用多个装饰器
@log_calls
@timing_decorator
@retry(max_attempts=3, delay=0.1)
@cache_with_ttl(ttl_seconds=5, max_size=10)
def complex_calculation(x, y, operation="add"):
    """复杂计算函数（组合多个装饰器）"""
    print(f"执行复杂计算: {x} {operation} {y}")
    
    # 模拟可能失败的操作
    if random.random() < 0.3:  # 30%概率失败
        raise ValueError(f"计算失败: {operation} 操作出错")
    
    # 模拟耗时计算
    time.sleep(0.05)
    
    if operation == "add":
        return x + y
    elif operation == "multiply":
        return x * y
    elif operation == "power":
        return x ** y
    else:
        raise ValueError(f"不支持的操作: {operation}")

print("\n=== 装饰器嵌套使用测试 ===")

# 测试组合装饰器
for i in range(3):
    try:
        result = complex_calculation(2, 3, "add")
        print(f"计算结果: {result}\n")
    except Exception as e:
        print(f"计算失败: {e}\n")

# 测试缓存效果
print("--- 测试缓存效果 ---")
result = complex_calculation(2, 3, "add")  # 应该命中缓存
print(f"缓存结果: {result}\n")
```

## 练习5：高级装饰器模式

实现一些高级的装饰器模式。

### 条件装饰器

```python
def conditional_decorator(condition):
    """条件装饰器：只有满足条件时才应用装饰器"""
    def decorator(func):
        if condition:
            # 应用装饰器
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(f"条件装饰器生效: 调用 {func.__name__}")
                return func(*args, **kwargs)
            return wrapper
        else:
            # 不应用装饰器，直接返回原函数
            print(f"条件装饰器未生效: {func.__name__} 保持原样")
            return func
    return decorator

# 根据环境变量决定是否启用调试
DEBUG_MODE = True

@conditional_decorator(DEBUG_MODE)
def debug_function(x):
    """调试函数"""
    return x * 2

@conditional_decorator(not DEBUG_MODE)
def production_function(x):
    """生产函数"""
    return x * 3

print("=== 条件装饰器测试 ===")
result1 = debug_function(5)
print(f"debug_function(5) = {result1}")

result2 = production_function(5)
print(f"production_function(5) = {result2}\n")
```

### 装饰器链

```python
class DecoratorChain:
    """装饰器链类"""
    
    def __init__(self, func):
        self.func = func
        self.decorators = []
    
    def add_decorator(self, decorator):
        """添加装饰器到链中"""
        self.decorators.append(decorator)
        return self
    
    def build(self):
        """构建最终的装饰器函数"""
        result = self.func
        for decorator in reversed(self.decorators):  # 反向应用装饰器
            result = decorator(result)
        return result

def chain_decorator(func):
    """创建装饰器链的便捷函数"""
    return DecoratorChain(func)

# 使用装饰器链
@chain_decorator
def chained_function(x, y):
    """被装饰器链装饰的函数"""
    return x + y

# 动态添加装饰器
decorated_func = (chained_function
                 .add_decorator(log_calls)
                 .add_decorator(timing_decorator)
                 .add_decorator(lambda f: cache_with_ttl(ttl_seconds=10)(f))
                 .build())

print("=== 装饰器链测试 ===")
result = decorated_func(10, 20)
print(f"链式装饰结果: {result}\n")

# 再次调用测试缓存
result = decorated_func(10, 20)
print(f"缓存命中结果: {result}\n")
```

## 练习6：装饰器与元编程

结合元编程技术实现高级装饰器。

### 自动验证装饰器

```python
import inspect
from typing import get_type_hints

def validate_types(func):
    """自动类型验证装饰器"""
    # 获取函数的类型提示
    type_hints = get_type_hints(func)
    sig = inspect.signature(func)
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 绑定参数
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        # 验证每个参数的类型
        for param_name, value in bound_args.arguments.items():
            if param_name in type_hints:
                expected_type = type_hints[param_name]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"参数 {param_name} 期望类型 {expected_type.__name__}, "
                        f"但得到 {type(value).__name__}"
                    )
        
        # 执行函数
        result = func(*args, **kwargs)
        
        # 验证返回值类型
        if 'return' in type_hints:
            expected_return_type = type_hints['return']
            if not isinstance(result, expected_return_type):
                raise TypeError(
                    f"返回值期望类型 {expected_return_type.__name__}, "
                    f"但得到 {type(result).__name__}"
                )
        
        return result
    
    return wrapper

@validate_types
def typed_function(name: str, age: int, height: float = 1.75) -> str:
    """带类型提示的函数"""
    return f"{name} is {age} years old and {height}m tall"

print("=== 类型验证装饰器测试 ===")

# 正确的调用
result = typed_function("Alice", 25, 1.68)
print(f"正确调用: {result}")

# 错误的类型
try:
    result = typed_function("Bob", "25")  # age应该是int
except TypeError as e:
    print(f"类型错误: {e}")

try:
    result = typed_function(123, 25)  # name应该是str
except TypeError as e:
    print(f"类型错误: {e}\n")
```

### 性能监控装饰器

```python
import psutil
import threading
from collections import defaultdict

class PerformanceMonitor:
    """性能监控器"""
    
    def __init__(self):
        self.stats = defaultdict(list)
        self.lock = threading.Lock()
    
    def record(self, func_name, execution_time, memory_usage, cpu_percent):
        """记录性能数据"""
        with self.lock:
            self.stats[func_name].append({
                'execution_time': execution_time,
                'memory_usage': memory_usage,
                'cpu_percent': cpu_percent,
                'timestamp': time.time()
            })
    
    def get_stats(self, func_name):
        """获取函数的性能统计"""
        with self.lock:
            if func_name not in self.stats:
                return None
            
            data = self.stats[func_name]
            if not data:
                return None
            
            execution_times = [d['execution_time'] for d in data]
            memory_usages = [d['memory_usage'] for d in data]
            cpu_percents = [d['cpu_percent'] for d in data]
            
            return {
                'call_count': len(data),
                'avg_execution_time': sum(execution_times) / len(execution_times),
                'max_execution_time': max(execution_times),
                'min_execution_time': min(execution_times),
                'avg_memory_usage': sum(memory_usages) / len(memory_usages),
                'max_memory_usage': max(memory_usages),
                'avg_cpu_percent': sum(cpu_percents) / len(cpu_percents),
                'max_cpu_percent': max(cpu_percents)
            }
    
    def clear_stats(self, func_name=None):
        """清空统计数据"""
        with self.lock:
            if func_name:
                self.stats.pop(func_name, None)
            else:
                self.stats.clear()

# 全局性能监控器
performance_monitor = PerformanceMonitor()

def monitor_performance(func):
    """性能监控装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 获取初始状态
        process = psutil.Process()
        initial_memory = process.memory_info().rss / 1024 / 1024  # MB
        initial_cpu = process.cpu_percent()
        
        # 执行函数
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        
        # 获取最终状态
        final_memory = process.memory_info().rss / 1024 / 1024  # MB
        final_cpu = process.cpu_percent()
        
        # 计算性能指标
        execution_time = end_time - start_time
        memory_usage = final_memory - initial_memory
        cpu_percent = final_cpu
        
        # 记录性能数据
        performance_monitor.record(
            func.__name__, execution_time, memory_usage, cpu_percent
        )
        
        return result
    
    return wrapper

@monitor_performance
def cpu_intensive_task(n):
    """CPU密集型任务"""
    result = 0
    for i in range(n):
        result += i ** 2
    return result

@monitor_performance
def memory_intensive_task(size):
    """内存密集型任务"""
    data = [i for i in range(size)]
    return len(data)

print("=== 性能监控装饰器测试 ===")

# 执行一些任务
for i in range(3):
    result1 = cpu_intensive_task(100000)
    result2 = memory_intensive_task(50000)
    time.sleep(0.1)  # 避免CPU使用率测量不准确

# 查看性能统计
print("\nCPU密集型任务统计:")
cpu_stats = performance_monitor.get_stats('cpu_intensive_task')
if cpu_stats:
    for key, value in cpu_stats.items():
        if 'time' in key:
            print(f"  {key}: {value:.6f}秒")
        elif 'memory' in key:
            print(f"  {key}: {value:.2f}MB")
        elif 'cpu' in key:
            print(f"  {key}: {value:.2f}%")
        else:
            print(f"  {key}: {value}")

print("\n内存密集型任务统计:")
memory_stats = performance_monitor.get_stats('memory_intensive_task')
if memory_stats:
    for key, value in memory_stats.items():
        if 'time' in key:
            print(f"  {key}: {value:.6f}秒")
        elif 'memory' in key:
            print(f"  {key}: {value:.2f}MB")
        elif 'cpu' in key:
            print(f"  {key}: {value:.2f}%")
        else:
            print(f"  {key}: {value}")
```

## 练习7：装饰器与异步编程

实现支持异步函数的装饰器。

```python
import asyncio
import aiohttp
from functools import wraps

def async_retry(max_attempts=3, delay=1.0):
    """异步重试装饰器"""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    print(f"异步尝试执行 {func.__name__} (第 {attempt + 1} 次)")
                    result = await func(*args, **kwargs)
                    if attempt > 0:
                        print(f"异步函数 {func.__name__} 在第 {attempt + 1} 次尝试后成功")
                    return result
                except Exception as e:
                    last_exception = e
                    print(f"第 {attempt + 1} 次异步尝试失败: {e}")
                    if attempt < max_attempts - 1:
                        print(f"等待 {delay} 秒后重试...")
                        await asyncio.sleep(delay)
            
            print(f"异步函数 {func.__name__} 在 {max_attempts} 次尝试后仍然失败")
            raise last_exception
        
        return wrapper
    return decorator

def async_timing(func):
    """异步计时装饰器"""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        
        print(f"异步函数 {func.__name__} 执行时间: {execution_time:.6f}秒")
        return result
    
    return wrapper

@async_timing
@async_retry(max_attempts=3, delay=0.5)
async def fetch_data(url):
    """异步获取数据"""
    print(f"正在获取数据: {url}")
    
    # 模拟网络请求可能失败
    if random.random() < 0.6:  # 60%概率失败
        raise aiohttp.ClientError(f"请求 {url} 失败")
    
    # 模拟网络延迟
    await asyncio.sleep(0.1)
    return f"来自 {url} 的数据"

@async_timing
async def process_multiple_urls(urls):
    """并发处理多个URL"""
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    successful_results = []
    failed_results = []
    
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            failed_results.append((urls[i], str(result)))
        else:
            successful_results.append((urls[i], result))
    
    return successful_results, failed_results

print("\n=== 异步装饰器测试 ===")

# 运行异步测试
async def run_async_tests():
    urls = [
        "https://api1.example.com/data",
        "https://api2.example.com/data",
        "https://api3.example.com/data"
    ]
    
    successful, failed = await process_multiple_urls(urls)
    
    print(f"\n成功获取 {len(successful)} 个URL的数据:")
    for url, data in successful:
        print(f"  {url}: {data}")
    
    print(f"\n失败的URL ({len(failed)} 个):")
    for url, error in failed:
        print(f"  {url}: {error}")

# 如果在支持asyncio的环境中运行
try:
    asyncio.run(run_async_tests())
except RuntimeError:
    print("当前环境不支持asyncio.run()，跳过异步测试")
```

## 练习8：权限控制装饰器

实现一个完整的权限控制系统。

```python
from enum import Enum
from typing import Set, Optional

class Permission(Enum):
    """权限枚举"""
    READ = "read"
    WRITE = "write"
    DELETE = "delete"
    ADMIN = "admin"

class User:
    """用户类"""
    
    def __init__(self, username: str, permissions: Set[Permission] = None):
        self.username = username
        self.permissions = permissions or set()
    
    def has_permission(self, permission: Permission) -> bool:
        """检查用户是否有指定权限"""
        return permission in self.permissions or Permission.ADMIN in self.permissions
    
    def add_permission(self, permission: Permission):
        """添加权限"""
        self.permissions.add(permission)
    
    def remove_permission(self, permission: Permission):
        """移除权限"""
        self.permissions.discard(permission)
    
    def __str__(self):
        return f"User({self.username}, permissions={[p.value for p in self.permissions]})"

class AdminSystem:
    """管理系统类"""
    
    def __init__(self):
        self.current_user: Optional[User] = None
        self.data = {"secret": "这是机密数据"}
    
    def login(self, user: User):
        """用户登录"""
        self.current_user = user
        print(f"用户 {user.username} 已登录")
    
    def logout(self):
        """用户登出"""
        if self.current_user:
            print(f"用户 {self.current_user.username} 已登出")
            self.current_user = None
    
    def get_current_user(self) -> Optional[User]:
        """获取当前用户"""
        return self.current_user

def require_permission(permission: Permission):
    """权限检查装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 查找AdminSystem实例和User实例
            system = None
            user = None
            
            # 检查参数中是否有AdminSystem和User实例
            for arg in args:
                if isinstance(arg, AdminSystem):
                    system = arg
                elif isinstance(arg, User):
                    user = arg
            
            # 如果找到了system，尝试获取当前用户
            if system and not user:
                user = system.get_current_user()
            
            # 检查权限
            if not user:
                raise PermissionError("未找到用户信息，访问被拒绝")
            
            if not user.has_permission(permission):
                raise PermissionError(
                    f"用户 {user.username} 没有 {permission.value} 权限，访问被拒绝"
                )
            
            print(f"权限检查通过: 用户 {user.username} 有 {permission.value} 权限")
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

def require_login(func):
    """登录检查装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 查找AdminSystem实例
        system = None
        for arg in args:
            if isinstance(arg, AdminSystem):
                system = arg
                break
        
        if not system:
            raise ValueError("未找到AdminSystem实例")
        
        if not system.get_current_user():
            raise PermissionError("用户未登录，访问被拒绝")
        
        return func(*args, **kwargs)
    
    return wrapper

class SecureOperations:
    """安全操作类"""
    
    @staticmethod
    @require_login
    @require_permission(Permission.READ)
    def read_data(system: AdminSystem):
        """读取数据"""
        user = system.get_current_user()
        print(f"用户 {user.username} 正在读取数据")
        return system.data
    
    @staticmethod
    @require_login
    @require_permission(Permission.WRITE)
    def write_data(system: AdminSystem, key: str, value: str):
        """写入数据"""
        user = system.get_current_user()
        print(f"用户 {user.username} 正在写入数据: {key} = {value}")
        system.data[key] = value
        return f"数据已写入: {key} = {value}"
    
    @staticmethod
    @require_login
    @require_permission(Permission.DELETE)
    def delete_data(system: AdminSystem, key: str):
        """删除数据"""
        user = system.get_current_user()
        print(f"用户 {user.username} 正在删除数据: {key}")
        if key in system.data:
            del system.data[key]
            return f"数据已删除: {key}"
        else:
            return f"数据不存在: {key}"
    
    @staticmethod
    @require_login
    @require_permission(Permission.ADMIN)
    def admin_operation(system: AdminSystem, operation: str):
        """管理员操作"""
        user = system.get_current_user()
        print(f"管理员 {user.username} 正在执行操作: {operation}")
        return f"管理员操作完成: {operation}"

print("\n=== 权限控制装饰器测试 ===")

# 创建用户和系统
regular_user = User("alice", {Permission.READ})
writer_user = User("bob", {Permission.READ, Permission.WRITE})
admin_user = User("admin", {Permission.ADMIN})
system = AdminSystem()

# 测试未登录访问
print("\n--- 测试未登录访问 ---")
try:
    SecureOperations.read_data(system)
except PermissionError as e:
    print(f"权限错误: {e}")

# 测试普通用户权限
print("\n--- 测试普通用户权限 ---")
system.login(regular_user)

# 读取数据（有权限）
try:
    data = SecureOperations.read_data(system)
    print(f"读取成功: {data}")
except PermissionError as e:
    print(f"权限错误: {e}")

# 写入数据（无权限）
try:
    SecureOperations.write_data(system, "new_key", "new_value")
except PermissionError as e:
    print(f"权限错误: {e}")

# 测试写入用户权限
print("\n--- 测试写入用户权限 ---")
system.login(writer_user)

# 写入数据（有权限）
try:
    result = SecureOperations.write_data(system, "user_data", "用户数据")
    print(f"写入成功: {result}")
except PermissionError as e:
    print(f"权限错误: {e}")

# 删除数据（无权限）
try:
    SecureOperations.delete_data(system, "secret")
except PermissionError as e:
    print(f"权限错误: {e}")

# 测试管理员权限
print("\n--- 测试管理员权限 ---")
system.login(admin_user)

# 管理员可以执行所有操作
try:
    data = SecureOperations.read_data(system)
    print(f"管理员读取: {data}")
    
    SecureOperations.write_data(system, "admin_data", "管理员数据")
    SecureOperations.delete_data(system, "user_data")
    SecureOperations.admin_operation(system, "系统维护")
    
    print(f"最终数据: {system.data}")
except PermissionError as e:
    print(f"权限错误: {e}")

system.logout()
```

## 小结

通过这8个综合练习，我们学习了：

1. **基础装饰器**：日志记录、计时、异常处理
2. **带参数装饰器**：重试机制、TTL缓存
3. **类装饰器**：单例模式、自动属性生成
4. **装饰器嵌套**：多个装饰器的组合使用
5. **高级模式**：条件装饰器、装饰器链
6. **元编程结合**：类型验证、性能监控
7. **异步支持**：异步函数的装饰器实现
8. **权限控制**：完整的权限管理系统

这些练习涵盖了装饰器的各个方面，从基础应用到高级技巧，帮助你全面掌握Python装饰器的使用。在实际项目中，你可以根据需要选择合适的装饰器模式来解决具体问题。