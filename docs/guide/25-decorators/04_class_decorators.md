# 类装饰器

类装饰器是使用类来实现装饰器功能的一种方式。与函数装饰器相比，类装饰器提供了更好的状态管理和更清晰的代码组织结构。

## 类装饰器的基本原理

类装饰器通过实现 `__call__` 方法来工作。当类的实例被调用时，会执行 `__call__` 方法。

### 基本结构

```python
class MyDecorator:
    def __init__(self, func):
        """初始化装饰器，接收被装饰的函数"""
        self.func = func
        # 可以在这里初始化状态变量
        self.call_count = 0
    
    def __call__(self, *args, **kwargs):
        """当装饰后的函数被调用时执行"""
        self.call_count += 1
        print(f"第 {self.call_count} 次调用 {self.func.__name__}")
        
        # 调用原函数
        result = self.func(*args, **kwargs)
        return result

# 使用类装饰器
@MyDecorator
def greet(name):
    return f"Hello, {name}!"

# 测试
print(greet("Alice"))  # 第 1 次调用 greet
print(greet("Bob"))    # 第 2 次调用 greet
```

## 带参数的类装饰器

带参数的类装饰器需要在 `__init__` 方法中接收装饰器参数，并提供一个方法来接收被装饰的函数。

```python
class ParameterizedDecorator:
    def __init__(self, prefix="LOG", include_time=True):
        """初始化装饰器参数"""
        self.prefix = prefix
        self.include_time = include_time
    
    def __call__(self, func):
        """接收被装饰的函数，返回包装器"""
        def wrapper(*args, **kwargs):
            import datetime
            
            message = f"[{self.prefix}] 调用 {func.__name__}"
            if self.include_time:
                timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                message = f"[{timestamp}] {message}"
            
            print(message)
            return func(*args, **kwargs)
        
        return wrapper

# 使用带参数的类装饰器
@ParameterizedDecorator(prefix="DEBUG", include_time=True)
def calculate(x, y):
    return x + y

@ParameterizedDecorator(prefix="INFO", include_time=False)
def process_data(data):
    return f"处理: {data}"

# 测试
result = calculate(5, 3)
print(f"结果: {result}")

result = process_data("test")
print(f"结果: {result}")
```

## 实际应用示例

### 1. 调用计数器装饰器

```python
import functools
from collections import defaultdict

class CallCounter:
    """函数调用计数器装饰器"""
    
    def __init__(self, func):
        self.func = func
        self.count = 0
        self.call_history = []
        # 保持原函数的元数据
        functools.update_wrapper(self, func)
    
    def __call__(self, *args, **kwargs):
        import datetime
        
        self.count += 1
        call_time = datetime.datetime.now()
        
        print(f"[计数器] {self.func.__name__} 被调用第 {self.count} 次")
        
        try:
            result = self.func(*args, **kwargs)
            
            # 记录调用历史
            self.call_history.append({
                'call_number': self.count,
                'timestamp': call_time,
                'args': args,
                'kwargs': kwargs,
                'success': True,
                'result': result
            })
            
            return result
            
        except Exception as e:
            # 记录失败的调用
            self.call_history.append({
                'call_number': self.count,
                'timestamp': call_time,
                'args': args,
                'kwargs': kwargs,
                'success': False,
                'error': str(e)
            })
            raise
    
    def get_stats(self):
        """获取调用统计信息"""
        successful_calls = sum(1 for call in self.call_history if call['success'])
        failed_calls = len(self.call_history) - successful_calls
        
        return {
            'function_name': self.func.__name__,
            'total_calls': self.count,
            'successful_calls': successful_calls,
            'failed_calls': failed_calls,
            'success_rate': successful_calls / self.count if self.count > 0 else 0
        }
    
    def get_history(self, limit=None):
        """获取调用历史"""
        history = self.call_history[-limit:] if limit else self.call_history
        return history
    
    def reset(self):
        """重置计数器"""
        self.count = 0
        self.call_history.clear()
        print(f"[计数器] {self.func.__name__} 的计数器已重置")

# 使用调用计数器
@CallCounter
def fibonacci(n):
    """计算斐波那契数"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@CallCounter
def divide(a, b):
    """除法运算"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

# 测试调用计数器
print("=== 测试斐波那契函数 ===")
result = fibonacci(5)
print(f"fibonacci(5) = {result}")
print(f"统计信息: {fibonacci.get_stats()}\n")

print("=== 测试除法函数 ===")
print(f"divide(10, 2) = {divide(10, 2)}")
print(f"divide(8, 4) = {divide(8, 4)}")

try:
    divide(5, 0)
except ValueError as e:
    print(f"捕获异常: {e}")

print(f"除法统计: {divide.get_stats()}")
print(f"除法历史: {divide.get_history()}")
```

### 2. 缓存装饰器类

```python
import functools
import time
from collections import OrderedDict
import hashlib
import pickle

class LRUCache:
    """LRU缓存装饰器类"""
    
    def __init__(self, max_size=128, ttl=None):
        self.max_size = max_size
        self.ttl = ttl
        self.cache = OrderedDict()
        self.timestamps = {}
        self.hits = 0
        self.misses = 0
    
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 生成缓存键
            key = self._make_key(args, kwargs)
            current_time = time.time()
            
            # 检查缓存
            if key in self.cache:
                # 检查TTL
                if self.ttl is None or (current_time - self.timestamps[key]) < self.ttl:
                    self.hits += 1
                    # 移动到末尾（最近使用）
                    self.cache.move_to_end(key)
                    print(f"[缓存] 命中: {func.__name__}")
                    return self.cache[key]
                else:
                    # 缓存过期
                    print(f"[缓存] 过期: {func.__name__}")
                    del self.cache[key]
                    del self.timestamps[key]
            
            # 缓存未命中
            self.misses += 1
            print(f"[缓存] 未命中: {func.__name__}")
            
            # 计算结果
            result = func(*args, **kwargs)
            
            # 存储到缓存
            self.cache[key] = result
            self.timestamps[key] = current_time
            
            # 检查缓存大小
            if len(self.cache) > self.max_size:
                # 删除最旧的项
                oldest_key = next(iter(self.cache))
                del self.cache[oldest_key]
                del self.timestamps[oldest_key]
                print(f"[缓存] 删除最旧项，当前大小: {len(self.cache)}")
            
            return result
        
        # 添加缓存管理方法
        wrapper.cache_info = self.cache_info
        wrapper.cache_clear = self.cache_clear
        wrapper.cache_get = self.cache_get
        
        return wrapper
    
    def _make_key(self, args, kwargs):
        """生成缓存键"""
        key_data = (args, tuple(sorted(kwargs.items())))
        # 使用pickle序列化后计算hash，处理复杂对象
        try:
            serialized = pickle.dumps(key_data)
            return hashlib.md5(serialized).hexdigest()
        except (pickle.PicklingError, TypeError):
            # 如果无法序列化，使用字符串表示
            return str(key_data)
    
    def cache_info(self):
        """获取缓存统计信息"""
        total_calls = self.hits + self.misses
        hit_rate = self.hits / total_calls if total_calls > 0 else 0
        
        return {
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': hit_rate,
            'current_size': len(self.cache),
            'max_size': self.max_size,
            'ttl': self.ttl
        }
    
    def cache_clear(self):
        """清空缓存"""
        self.cache.clear()
        self.timestamps.clear()
        self.hits = 0
        self.misses = 0
        print("[缓存] 已清空")
    
    def cache_get(self, *args, **kwargs):
        """获取缓存值（不执行函数）"""
        key = self._make_key(args, kwargs)
        return self.cache.get(key)

# 使用LRU缓存
@LRUCache(max_size=3, ttl=5)
def expensive_function(x, y):
    """模拟耗时函数"""
    print(f"  正在计算 {x} + {y}...")
    time.sleep(0.5)
    return x + y

@LRUCache(max_size=5)
def factorial(n):
    """计算阶乘"""
    print(f"  正在计算 {n}!...")
    if n <= 1:
        return 1
    time.sleep(0.1)
    return n * factorial(n-1)

# 测试LRU缓存
print("=== 测试LRU缓存 ===")
print(f"expensive_function(2, 3) = {expensive_function(2, 3)}")
print(f"expensive_function(2, 3) = {expensive_function(2, 3)}")
print(f"expensive_function(4, 5) = {expensive_function(4, 5)}")
print(f"缓存信息: {expensive_function.cache_info()}\n")

print("=== 测试阶乘缓存 ===")
print(f"factorial(5) = {factorial(5)}")
print(f"factorial(4) = {factorial(4)}")
print(f"缓存信息: {factorial.cache_info()}")
```

### 3. 重试装饰器类

```python
import functools
import time
import random
from typing import Tuple, Type, Union

class RetryDecorator:
    """重试装饰器类"""
    
    def __init__(self, 
                 max_attempts: int = 3,
                 delay: float = 1.0,
                 backoff: float = 2.0,
                 exceptions: Union[Type[Exception], Tuple[Type[Exception], ...]] = (Exception,),
                 on_retry=None,
                 on_failure=None):
        self.max_attempts = max_attempts
        self.delay = delay
        self.backoff = backoff
        self.exceptions = exceptions if isinstance(exceptions, tuple) else (exceptions,)
        self.on_retry = on_retry  # 重试时的回调函数
        self.on_failure = on_failure  # 最终失败时的回调函数
        
        # 统计信息
        self.total_calls = 0
        self.successful_calls = 0
        self.failed_calls = 0
        self.total_retries = 0
    
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.total_calls += 1
            current_delay = self.delay
            last_exception = None
            
            for attempt in range(self.max_attempts):
                try:
                    if attempt > 0:
                        print(f"[重试] 第 {attempt + 1}/{self.max_attempts} 次尝试: {func.__name__}")
                    
                    result = func(*args, **kwargs)
                    
                    if attempt > 0:
                        print(f"[重试] {func.__name__} 在第 {attempt + 1} 次尝试后成功")
                        self.total_retries += attempt
                    
                    self.successful_calls += 1
                    return result
                    
                except self.exceptions as e:
                    last_exception = e
                    
                    if attempt < self.max_attempts - 1:
                        print(f"[重试] 第 {attempt + 1} 次尝试失败: {e}")
                        
                        # 调用重试回调
                        if self.on_retry:
                            self.on_retry(func, attempt + 1, e, args, kwargs)
                        
                        print(f"[重试] 等待 {current_delay:.1f} 秒后重试...")
                        time.sleep(current_delay)
                        current_delay *= self.backoff
                    else:
                        print(f"[重试] 所有 {self.max_attempts} 次尝试都失败了")
                        self.failed_calls += 1
                        self.total_retries += attempt
                        
                        # 调用失败回调
                        if self.on_failure:
                            self.on_failure(func, self.max_attempts, last_exception, args, kwargs)
            
            # 重新抛出最后一个异常
            raise last_exception
        
        # 添加统计方法
        wrapper.get_stats = self.get_stats
        wrapper.reset_stats = self.reset_stats
        
        return wrapper
    
    def get_stats(self):
        """获取重试统计信息"""
        success_rate = self.successful_calls / self.total_calls if self.total_calls > 0 else 0
        avg_retries = self.total_retries / self.total_calls if self.total_calls > 0 else 0
        
        return {
            'total_calls': self.total_calls,
            'successful_calls': self.successful_calls,
            'failed_calls': self.failed_calls,
            'success_rate': success_rate,
            'total_retries': self.total_retries,
            'average_retries_per_call': avg_retries
        }
    
    def reset_stats(self):
        """重置统计信息"""
        self.total_calls = 0
        self.successful_calls = 0
        self.failed_calls = 0
        self.total_retries = 0
        print("[重试] 统计信息已重置")

# 回调函数示例
def retry_callback(func, attempt, exception, args, kwargs):
    print(f"  📞 重试回调: {func.__name__} 第 {attempt} 次失败，异常: {exception}")

def failure_callback(func, max_attempts, exception, args, kwargs):
    print(f"  💥 失败回调: {func.__name__} 经过 {max_attempts} 次尝试后最终失败")
    print(f"     最后异常: {exception}")
    print(f"     调用参数: args={args}, kwargs={kwargs}")

# 使用重试装饰器
@RetryDecorator(
    max_attempts=3,
    delay=0.5,
    backoff=2,
    exceptions=(ConnectionError, TimeoutError),
    on_retry=retry_callback,
    on_failure=failure_callback
)
def unstable_network_call(url):
    """模拟不稳定的网络调用"""
    if random.random() < 0.7:  # 70%失败率
        raise ConnectionError(f"无法连接到 {url}")
    return f"成功获取 {url} 的数据"

@RetryDecorator(max_attempts=4, delay=0.2, exceptions=(ValueError,))
def data_validation(data):
    """数据验证函数"""
    if not data:
        raise ValueError("数据不能为空")
    
    if random.random() < 0.5:  # 50%失败率
        raise ValueError("数据格式不正确")
    
    return f"数据验证通过: {data}"

# 测试重试装饰器
print("=== 测试网络调用重试 ===")
try:
    result = unstable_network_call("https://api.example.com")
    print(f"最终结果: {result}")
except Exception as e:
    print(f"最终失败: {e}")

print(f"网络调用统计: {unstable_network_call.get_stats()}\n")

print("=== 测试数据验证重试 ===")
try:
    result = data_validation("test_data")
    print(f"最终结果: {result}")
except Exception as e:
    print(f"最终失败: {e}")

print(f"数据验证统计: {data_validation.get_stats()}")
```

### 4. 单例装饰器类

```python
import functools
import threading
from typing import Dict, Any

class Singleton:
    """单例装饰器类"""
    
    def __init__(self, cls):
        self.cls = cls
        self._instances: Dict[Any, Any] = {}
        self._lock = threading.Lock()
        functools.update_wrapper(self, cls)
    
    def __call__(self, *args, **kwargs):
        # 创建实例键（基于参数）
        key = (args, tuple(sorted(kwargs.items())))
        
        if key not in self._instances:
            with self._lock:
                # 双重检查锁定
                if key not in self._instances:
                    print(f"[单例] 创建新实例: {self.cls.__name__}")
                    self._instances[key] = self.cls(*args, **kwargs)
                else:
                    print(f"[单例] 返回现有实例: {self.cls.__name__}")
        else:
            print(f"[单例] 返回现有实例: {self.cls.__name__}")
        
        return self._instances[key]
    
    def get_instances(self):
        """获取所有实例"""
        return dict(self._instances)
    
    def clear_instances(self):
        """清除所有实例"""
        with self._lock:
            count = len(self._instances)
            self._instances.clear()
            print(f"[单例] 已清除 {count} 个实例")

# 使用单例装饰器
@Singleton
class DatabaseConnection:
    """数据库连接类"""
    
    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.database = database
        self.connected = False
        print(f"初始化数据库连接: {host}:{port}/{database}")
    
    def connect(self):
        if not self.connected:
            print(f"连接到数据库: {self.host}:{self.port}/{self.database}")
            self.connected = True
        else:
            print("数据库已连接")
    
    def disconnect(self):
        if self.connected:
            print(f"断开数据库连接: {self.host}:{self.port}/{self.database}")
            self.connected = False
        else:
            print("数据库未连接")
    
    def query(self, sql):
        if self.connected:
            return f"执行查询: {sql}"
        else:
            raise RuntimeError("数据库未连接")

@Singleton
class Logger:
    """日志记录器类"""
    
    def __init__(self, name="default", level="INFO"):
        self.name = name
        self.level = level
        self.logs = []
        print(f"初始化日志记录器: {name} (级别: {level})")
    
    def log(self, message, level="INFO"):
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] [{self.name}] {message}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def get_logs(self):
        return self.logs.copy()

# 测试单例装饰器
print("=== 测试数据库连接单例 ===")
db1 = DatabaseConnection("localhost", 5432, "mydb")
db2 = DatabaseConnection("localhost", 5432, "mydb")
db3 = DatabaseConnection("localhost", 3306, "otherdb")  # 不同参数，新实例

print(f"db1 is db2: {db1 is db2}")  # True
print(f"db1 is db3: {db1 is db3}")  # False

db1.connect()
db2.query("SELECT * FROM users")  # 使用同一个连接

print(f"\n当前实例数量: {len(DatabaseConnection.get_instances())}")

print("\n=== 测试日志记录器单例 ===")
logger1 = Logger("app", "DEBUG")
logger2 = Logger("app", "DEBUG")
logger3 = Logger("db", "INFO")  # 不同参数，新实例

print(f"logger1 is logger2: {logger1 is logger2}")  # True
print(f"logger1 is logger3: {logger1 is logger3}")  # False

logger1.log("应用启动")
logger2.log("处理请求")  # 使用同一个记录器
logger3.log("数据库查询")

print(f"\nlogger1 日志数量: {len(logger1.get_logs())}")
print(f"logger3 日志数量: {len(logger3.get_logs())}")
```

## 类装饰器 vs 函数装饰器

### 优势

1. **状态管理**：类装饰器可以轻松维护状态信息
2. **方法丰富**：可以提供额外的方法来管理装饰器行为
3. **代码组织**：复杂逻辑可以分解为多个方法
4. **可扩展性**：容易通过继承来扩展功能

### 劣势

1. **性能开销**：创建类实例比函数调用稍慢
2. **内存使用**：需要存储实例状态
3. **复杂性**：对于简单装饰器来说可能过于复杂

### 选择建议

- **使用类装饰器**：需要维护状态、提供管理方法、复杂逻辑
- **使用函数装饰器**：简单逻辑、无状态、性能敏感

## 小结

类装饰器通过 `__call__` 方法提供了一种面向对象的装饰器实现方式：

1. **基本类装饰器**：实现 `__call__` 方法处理函数调用
2. **带参数类装饰器**：`__init__` 接收参数，`__call__` 接收函数
3. **状态管理**：可以维护调用统计、缓存等状态信息
4. **方法扩展**：提供额外方法来管理装饰器行为

类装饰器特别适合需要复杂状态管理和丰富功能的场景。在下一章中，我们将学习装饰器的嵌套使用。