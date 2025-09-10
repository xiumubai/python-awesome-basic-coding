# functools.wraps 的作用

`functools.wraps` 是 Python 标准库中一个非常重要的装饰器，专门用于解决装饰器会改变被装饰函数元信息的问题。理解和正确使用 `functools.wraps` 是编写高质量装饰器的关键。

## 问题的产生

### 不使用 functools.wraps 的问题

```python
def simple_decorator(func):
    """一个简单的装饰器"""
    def wrapper(*args, **kwargs):
        """包装函数"""
        print(f"调用函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"函数 {func.__name__} 执行完成")
        return result
    return wrapper

@simple_decorator
def greet(name):
    """问候函数
    
    Args:
        name (str): 要问候的人的姓名
    
    Returns:
        str: 问候语
    """
    return f"Hello, {name}!"

# 检查函数的元信息
print(f"函数名: {greet.__name__}")
print(f"文档字符串: {greet.__doc__}")
print(f"模块名: {greet.__module__}")
print(f"注解: {greet.__annotations__}")
print(f"限定名: {greet.__qualname__}")

# 调用函数
result = greet("Alice")
print(f"结果: {result}")
```

**输出分析**：
- 函数名变成了 `wrapper` 而不是 `greet`
- 文档字符串变成了包装函数的文档
- 其他元信息也丢失了

### 使用 functools.wraps 解决问题

```python
import functools

def proper_decorator(func):
    """一个正确的装饰器"""
    @functools.wraps(func)  # 关键：使用 functools.wraps
    def wrapper(*args, **kwargs):
        """包装函数"""
        print(f"调用函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"函数 {func.__name__} 执行完成")
        return result
    return wrapper

@proper_decorator
def greet_proper(name):
    """问候函数
    
    Args:
        name (str): 要问候的人的姓名
    
    Returns:
        str: 问候语
    """
    return f"Hello, {name}!"

# 检查函数的元信息
print(f"函数名: {greet_proper.__name__}")
print(f"文档字符串: {greet_proper.__doc__}")
print(f"模块名: {greet_proper.__module__}")
print(f"限定名: {greet_proper.__qualname__}")

# 调用函数
result = greet_proper("Bob")
print(f"结果: {result}")
```

**改进效果**：
- 函数名正确保持为 `greet_proper`
- 文档字符串完整保留
- 所有元信息都得到正确保留

## functools.wraps 的工作原理

### 手动实现类似功能

```python
def manual_wraps_decorator(func):
    """手动保留函数元信息的装饰器"""
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"函数执行完成")
        return result
    
    # 手动复制元信息
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    wrapper.__module__ = func.__module__
    wrapper.__qualname__ = func.__qualname__
    wrapper.__annotations__ = func.__annotations__
    wrapper.__dict__.update(func.__dict__)
    
    return wrapper

@manual_wraps_decorator
def test_function(x: int, y: int) -> int:
    """测试函数
    
    计算两个数的和
    """
    return x + y

print(f"函数名: {test_function.__name__}")
print(f"文档: {test_function.__doc__}")
print(f"注解: {test_function.__annotations__}")

result = test_function(3, 5)
print(f"结果: {result}")
```

### functools.wraps 的实现原理

```python
import functools

# functools.wraps 实际上是 functools.partial(functools.update_wrapper)
# 它会复制以下属性：
ATTRIBUTES_TO_COPY = (
    '__module__',
    '__name__',
    '__qualname__',
    '__doc__',
    '__annotations__',
)

ASSIGNMENTS_TO_UPDATE = (
    '__dict__',
)

def show_wraps_behavior():
    """展示 functools.wraps 的行为"""
    
    def original_function(a, b=10):
        """原始函数的文档"""
        return a + b
    
    # 添加自定义属性
    original_function.custom_attr = "自定义属性"
    original_function.__dict__['extra_info'] = "额外信息"
    
    def decorator_with_wraps(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """包装函数的文档"""
            return func(*args, **kwargs)
        return wrapper
    
    def decorator_without_wraps(func):
        def wrapper(*args, **kwargs):
            """包装函数的文档"""
            return func(*args, **kwargs)
        return wrapper
    
    # 应用装饰器
    wrapped_with = decorator_with_wraps(original_function)
    wrapped_without = decorator_without_wraps(original_function)
    
    print("=== 原始函数 ===")
    print(f"名称: {original_function.__name__}")
    print(f"文档: {original_function.__doc__}")
    print(f"自定义属性: {getattr(original_function, 'custom_attr', 'None')}")
    print(f"字典: {original_function.__dict__}")
    
    print("\n=== 使用 functools.wraps ===")
    print(f"名称: {wrapped_with.__name__}")
    print(f"文档: {wrapped_with.__doc__}")
    print(f"自定义属性: {getattr(wrapped_with, 'custom_attr', 'None')}")
    print(f"字典: {wrapped_with.__dict__}")
    
    print("\n=== 不使用 functools.wraps ===")
    print(f"名称: {wrapped_without.__name__}")
    print(f"文档: {wrapped_without.__doc__}")
    print(f"自定义属性: {getattr(wrapped_without, 'custom_attr', 'None')}")
    print(f"字典: {wrapped_without.__dict__}")

show_wraps_behavior()
```

## 实际应用示例

### 1. 日志装饰器

```python
import functools
import datetime
import inspect

def log_function_calls(log_args=True, log_result=True, log_time=True):
    """记录函数调用的装饰器
    
    Args:
        log_args: 是否记录参数
        log_result: 是否记录返回值
        log_time: 是否记录执行时间
    """
    def decorator(func):
        @functools.wraps(func)  # 保留原函数信息
        def wrapper(*args, **kwargs):
            # 获取函数签名
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # 记录调用开始
            timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
            log_parts = [f"[{timestamp}] 调用 {func.__name__}"]
            
            if log_args:
                args_str = ", ".join(f"{k}={v!r}" for k, v in bound_args.arguments.items())
                log_parts.append(f"参数: ({args_str})")
            
            print(" - ".join(log_parts))
            
            # 执行函数
            start_time = datetime.datetime.now()
            try:
                result = func(*args, **kwargs)
                
                # 记录成功结果
                end_time = datetime.datetime.now()
                execution_time = (end_time - start_time).total_seconds() * 1000
                
                log_parts = [f"[{timestamp}] {func.__name__} 执行成功"]
                
                if log_result:
                    log_parts.append(f"返回: {result!r}")
                
                if log_time:
                    log_parts.append(f"耗时: {execution_time:.2f}ms")
                
                print(" - ".join(log_parts))
                return result
                
            except Exception as e:
                # 记录异常
                end_time = datetime.datetime.now()
                execution_time = (end_time - start_time).total_seconds() * 1000
                
                print(f"[{timestamp}] {func.__name__} 执行失败 - 异常: {e!r} - 耗时: {execution_time:.2f}ms")
                raise
        
        return wrapper
    return decorator

# 使用日志装饰器
@log_function_calls(log_args=True, log_result=True, log_time=True)
def calculate_fibonacci(n: int) -> int:
    """计算斐波那契数列的第n项
    
    Args:
        n: 要计算的项数（从0开始）
    
    Returns:
        斐波那契数列的第n项
    
    Raises:
        ValueError: 当n为负数时
    """
    if n < 0:
        raise ValueError("n必须是非负整数")
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

@log_function_calls(log_args=False, log_result=True, log_time=False)
def greet_user(name: str, greeting: str = "Hello") -> str:
    """问候用户
    
    Args:
        name: 用户姓名
        greeting: 问候语，默认为"Hello"
    
    Returns:
        完整的问候语
    """
    return f"{greeting}, {name}!"

# 测试装饰器效果
print("=== 函数元信息检查 ===")
print(f"函数名: {calculate_fibonacci.__name__}")
print(f"文档: {calculate_fibonacci.__doc__}")
print(f"注解: {calculate_fibonacci.__annotations__}")
print(f"签名: {inspect.signature(calculate_fibonacci)}")

print("\n=== 函数调用测试 ===")
result = calculate_fibonacci(10)
print(f"\n最终结果: {result}")

print("\n=== 问候函数测试 ===")
result = greet_user("Alice")
result = greet_user("Bob", "Hi")

print("\n=== 异常处理测试 ===")
try:
    result = calculate_fibonacci(-1)
except ValueError as e:
    print(f"捕获异常: {e}")
```

### 2. 性能监控装饰器

```python
import functools
import time
import psutil
import os
from collections import defaultdict

class PerformanceMonitor:
    """性能监控器"""
    
    def __init__(self):
        self.stats = defaultdict(list)
        self.call_counts = defaultdict(int)
    
    def monitor(self, track_memory=True, track_cpu=False):
        """性能监控装饰器
        
        Args:
            track_memory: 是否跟踪内存使用
            track_cpu: 是否跟踪CPU使用
        """
        def decorator(func):
            @functools.wraps(func)  # 保留函数元信息
            def wrapper(*args, **kwargs):
                func_name = func.__name__
                self.call_counts[func_name] += 1
                
                # 记录开始状态
                start_time = time.perf_counter()
                process = psutil.Process(os.getpid())
                
                if track_memory:
                    start_memory = process.memory_info().rss / 1024 / 1024  # MB
                
                if track_cpu:
                    start_cpu = process.cpu_percent()
                
                try:
                    # 执行函数
                    result = func(*args, **kwargs)
                    
                    # 记录结束状态
                    end_time = time.perf_counter()
                    execution_time = (end_time - start_time) * 1000  # ms
                    
                    # 收集性能数据
                    perf_data = {
                        'execution_time': execution_time,
                        'call_count': self.call_counts[func_name]
                    }
                    
                    if track_memory:
                        end_memory = process.memory_info().rss / 1024 / 1024  # MB
                        perf_data['memory_usage'] = end_memory
                        perf_data['memory_delta'] = end_memory - start_memory
                    
                    if track_cpu:
                        end_cpu = process.cpu_percent()
                        perf_data['cpu_usage'] = end_cpu
                    
                    self.stats[func_name].append(perf_data)
                    
                    # 输出性能信息
                    print(f"[PERF] {func_name} - 执行时间: {execution_time:.2f}ms", end="")
                    
                    if track_memory:
                        print(f" - 内存: {end_memory:.1f}MB (Δ{perf_data['memory_delta']:+.1f}MB)", end="")
                    
                    if track_cpu:
                        print(f" - CPU: {end_cpu:.1f}%", end="")
                    
                    print(f" - 调用次数: {self.call_counts[func_name]}")
                    
                    return result
                    
                except Exception as e:
                    end_time = time.perf_counter()
                    execution_time = (end_time - start_time) * 1000
                    print(f"[PERF] {func_name} - 执行失败 - 耗时: {execution_time:.2f}ms - 异常: {e}")
                    raise
            
            return wrapper
        return decorator
    
    def get_stats(self, func_name=None):
        """获取性能统计信息"""
        if func_name:
            return self.stats.get(func_name, [])
        return dict(self.stats)
    
    def print_summary(self):
        """打印性能摘要"""
        print("\n=== 性能监控摘要 ===")
        for func_name, records in self.stats.items():
            if not records:
                continue
            
            times = [r['execution_time'] for r in records]
            avg_time = sum(times) / len(times)
            max_time = max(times)
            min_time = min(times)
            
            print(f"\n函数: {func_name}")
            print(f"  调用次数: {len(records)}")
            print(f"  平均执行时间: {avg_time:.2f}ms")
            print(f"  最大执行时间: {max_time:.2f}ms")
            print(f"  最小执行时间: {min_time:.2f}ms")
            
            if records[0].get('memory_usage') is not None:
                memory_usage = [r['memory_usage'] for r in records]
                memory_deltas = [r['memory_delta'] for r in records]
                print(f"  平均内存使用: {sum(memory_usage)/len(memory_usage):.1f}MB")
                print(f"  内存变化范围: {min(memory_deltas):+.1f}MB ~ {max(memory_deltas):+.1f}MB")

# 创建性能监控器实例
monitor = PerformanceMonitor()

# 使用性能监控装饰器
@monitor.monitor(track_memory=True, track_cpu=False)
def memory_intensive_task(size: int) -> list:
    """内存密集型任务
    
    Args:
        size: 列表大小
    
    Returns:
        生成的大列表
    """
    # 创建大列表
    data = list(range(size))
    
    # 进行一些处理
    processed = [x * 2 for x in data if x % 2 == 0]
    
    return processed

@monitor.monitor(track_memory=False, track_cpu=True)
def cpu_intensive_task(iterations: int) -> int:
    """CPU密集型任务
    
    Args:
        iterations: 迭代次数
    
    Returns:
        计算结果
    """
    result = 0
    for i in range(iterations):
        result += i ** 2
    return result

@monitor.monitor(track_memory=True, track_cpu=True)
def mixed_task(data_size: int, compute_iterations: int) -> dict:
    """混合型任务（内存+CPU）
    
    Args:
        data_size: 数据大小
        compute_iterations: 计算迭代次数
    
    Returns:
        处理结果
    """
    # 内存操作
    data = [i for i in range(data_size)]
    
    # CPU计算
    computed = sum(x ** 2 for x in data[:compute_iterations])
    
    return {
        'data_length': len(data),
        'computed_sum': computed,
        'average': computed / min(compute_iterations, data_size) if compute_iterations > 0 else 0
    }

# 测试性能监控
print("=== 函数元信息验证 ===")
print(f"memory_intensive_task.__name__: {memory_intensive_task.__name__}")
print(f"memory_intensive_task.__doc__: {memory_intensive_task.__doc__}")
print(f"mixed_task.__annotations__: {mixed_task.__annotations__}")

print("\n=== 性能测试 ===")

# 测试内存密集型任务
print("\n--- 内存密集型任务 ---")
for size in [100000, 200000, 150000]:
    result = memory_intensive_task(size)
    print(f"处理了 {len(result)} 个元素")

# 测试CPU密集型任务
print("\n--- CPU密集型任务 ---")
for iterations in [100000, 200000, 150000]:
    result = cpu_intensive_task(iterations)
    print(f"计算结果: {result}")

# 测试混合任务
print("\n--- 混合型任务 ---")
for data_size, compute_iter in [(50000, 10000), (100000, 20000)]:
    result = mixed_task(data_size, compute_iter)
    print(f"混合任务结果: {result}")

# 打印性能摘要
monitor.print_summary()
```

### 3. 缓存装饰器

```python
import functools
import time
import hashlib
import pickle
from typing import Any, Callable, Dict, Optional

class SmartCache:
    """智能缓存装饰器"""
    
    def __init__(self, maxsize: int = 128, ttl: Optional[float] = None):
        self.maxsize = maxsize
        self.ttl = ttl
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.access_times: Dict[str, float] = {}
        self.hit_count = 0
        self.miss_count = 0
    
    def __call__(self, func: Callable) -> Callable:
        @functools.wraps(func)  # 保留原函数的所有元信息
        def wrapper(*args, **kwargs):
            # 生成缓存键
            cache_key = self._generate_key(func, args, kwargs)
            current_time = time.time()
            
            # 检查缓存
            if cache_key in self.cache:
                cache_entry = self.cache[cache_key]
                
                # 检查TTL
                if self.ttl is None or (current_time - cache_entry['timestamp']) < self.ttl:
                    self.hit_count += 1
                    self.access_times[cache_key] = current_time
                    print(f"[CACHE] 缓存命中: {func.__name__} (命中率: {self.hit_rate:.1%})")
                    return cache_entry['result']
                else:
                    # 缓存过期
                    print(f"[CACHE] 缓存过期: {func.__name__}")
                    del self.cache[cache_key]
                    del self.access_times[cache_key]
            
            # 缓存未命中，执行函数
            self.miss_count += 1
            print(f"[CACHE] 缓存未命中: {func.__name__} (命中率: {self.hit_rate:.1%})")
            
            result = func(*args, **kwargs)
            
            # 存储到缓存
            self._store_in_cache(cache_key, result, current_time)
            
            return result
        
        # 添加缓存管理方法到包装函数
        wrapper.cache_info = self.cache_info
        wrapper.cache_clear = self.cache_clear
        wrapper.cache_stats = self.cache_stats
        
        return wrapper
    
    def _generate_key(self, func: Callable, args: tuple, kwargs: dict) -> str:
        """生成缓存键"""
        # 使用函数名、参数创建唯一键
        key_data = {
            'func_name': func.__name__,
            'func_module': func.__module__,
            'args': args,
            'kwargs': sorted(kwargs.items())
        }
        
        # 序列化并生成哈希
        serialized = pickle.dumps(key_data)
        return hashlib.md5(serialized).hexdigest()
    
    def _store_in_cache(self, key: str, result: Any, timestamp: float):
        """存储结果到缓存"""
        # 检查缓存大小限制
        if len(self.cache) >= self.maxsize:
            # 使用LRU策略移除最久未访问的项
            oldest_key = min(self.access_times.keys(), key=self.access_times.get)
            del self.cache[oldest_key]
            del self.access_times[oldest_key]
            print(f"[CACHE] LRU淘汰: {oldest_key[:8]}...")
        
        # 存储新结果
        self.cache[key] = {
            'result': result,
            'timestamp': timestamp
        }
        self.access_times[key] = timestamp
    
    @property
    def hit_rate(self) -> float:
        """计算缓存命中率"""
        total = self.hit_count + self.miss_count
        return self.hit_count / total if total > 0 else 0.0
    
    def cache_info(self) -> dict:
        """获取缓存信息"""
        return {
            'hits': self.hit_count,
            'misses': self.miss_count,
            'hit_rate': self.hit_rate,
            'cache_size': len(self.cache),
            'max_size': self.maxsize
        }
    
    def cache_clear(self):
        """清空缓存"""
        self.cache.clear()
        self.access_times.clear()
        self.hit_count = 0
        self.miss_count = 0
        print("[CACHE] 缓存已清空")
    
    def cache_stats(self):
        """打印缓存统计信息"""
        info = self.cache_info()
        print(f"\n=== 缓存统计 ===")
        print(f"命中次数: {info['hits']}")
        print(f"未命中次数: {info['misses']}")
        print(f"命中率: {info['hit_rate']:.1%}")
        print(f"当前缓存大小: {info['cache_size']}/{info['max_size']}")
        
        if self.cache:
            print(f"\n缓存条目:")
            for i, (key, entry) in enumerate(self.cache.items(), 1):
                age = time.time() - entry['timestamp']
                print(f"  {i}. {key[:12]}... (存储时间: {age:.1f}秒前)")

# 创建缓存装饰器实例
cache_5min = SmartCache(maxsize=10, ttl=300)  # 5分钟TTL
cache_unlimited = SmartCache(maxsize=50, ttl=None)  # 无TTL限制

# 使用缓存装饰器
@cache_5min
def expensive_calculation(n: int, multiplier: float = 1.0) -> float:
    """昂贵的计算函数
    
    Args:
        n: 输入数字
        multiplier: 乘数
    
    Returns:
        计算结果
    """
    print(f"  正在进行复杂计算: {n} * {multiplier}...")
    time.sleep(1)  # 模拟耗时计算
    
    result = 0
    for i in range(n):
        result += i ** 2 * multiplier
    
    return result

@cache_unlimited
def fibonacci_cached(n: int) -> int:
    """缓存版斐波那契函数
    
    Args:
        n: 要计算的项数
    
    Returns:
        斐波那契数列的第n项
    """
    if n <= 1:
        return n
    
    print(f"  计算 fibonacci({n})")
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

# 测试缓存装饰器
print("=== 函数元信息验证 ===")
print(f"expensive_calculation.__name__: {expensive_calculation.__name__}")
print(f"expensive_calculation.__doc__: {expensive_calculation.__doc__}")
print(f"fibonacci_cached.__annotations__: {fibonacci_cached.__annotations__}")

# 验证缓存管理方法
print(f"\n=== 缓存管理方法验证 ===")
print(f"cache_info 方法存在: {hasattr(expensive_calculation, 'cache_info')}")
print(f"cache_clear 方法存在: {hasattr(expensive_calculation, 'cache_clear')}")
print(f"cache_stats 方法存在: {hasattr(expensive_calculation, 'cache_stats')}")

print("\n=== 缓存效果测试 ===")

# 测试昂贵计算的缓存
print("\n--- 昂贵计算测试 ---")
for i in range(3):
    print(f"\n第 {i+1} 次调用:")
    result = expensive_calculation(1000, 2.5)
    print(f"结果: {result}")

# 测试不同参数
print("\n--- 不同参数测试 ---")
result1 = expensive_calculation(500, 1.0)
result2 = expensive_calculation(500, 2.0)  # 不同参数，应该重新计算
result3 = expensive_calculation(500, 1.0)  # 相同参数，应该命中缓存

# 显示缓存统计
expensive_calculation.cache_stats()

# 测试斐波那契缓存
print("\n--- 斐波那契缓存测试 ---")
print("计算 fibonacci(10):")
result = fibonacci_cached(10)
print(f"结果: {result}")

print("\n再次计算 fibonacci(8) (应该全部命中缓存):")
result = fibonacci_cached(8)
print(f"结果: {result}")

fibonacci_cached.cache_stats()

# 清空缓存测试
print("\n=== 缓存清空测试 ===")
expensive_calculation.cache_clear()
print("缓存清空后再次调用:")
result = expensive_calculation(1000, 2.5)  # 应该重新计算
```

## functools.wraps 的高级用法

### 1. 自定义要复制的属性

```python
import functools

# 自定义要复制的属性
CUSTOM_WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__',
                             '__doc__', '__annotations__', '__custom_attr__')
CUSTOM_WRAPPER_UPDATES = ('__dict__',)

def custom_wraps(wrapped,
                assigned=CUSTOM_WRAPPER_ASSIGNMENTS,
                updated=CUSTOM_WRAPPER_UPDATES):
    """自定义的 wraps 装饰器"""
    return functools.partial(functools.update_wrapper,
                           wrapped=wrapped,
                           assigned=assigned,
                           updated=updated)

def my_decorator(func):
    @custom_wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def test_func():
    """测试函数"""
    pass

# 添加自定义属性
test_func.__custom_attr__ = "自定义属性值"

print(f"自定义属性: {getattr(test_func, '__custom_attr__', 'Not found')}")
```

### 2. 条件性使用 functools.wraps

```python
import functools

def conditional_decorator(preserve_metadata=True):
    """条件性保留元数据的装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"调用 {func.__name__}")
            return func(*args, **kwargs)
        
        # 根据条件决定是否保留元数据
        if preserve_metadata:
            return functools.wraps(func)(wrapper)
        else:
            return wrapper
    
    return decorator

@conditional_decorator(preserve_metadata=True)
def func_with_metadata(x):
    """保留元数据的函数"""
    return x * 2

@conditional_decorator(preserve_metadata=False)
def func_without_metadata(x):
    """不保留元数据的函数"""
    return x * 3

print(f"保留元数据: {func_with_metadata.__name__} - {func_with_metadata.__doc__}")
print(f"不保留元数据: {func_without_metadata.__name__} - {func_without_metadata.__doc__}")
```

## 最佳实践

### 1. 总是使用 functools.wraps

```python
# ✅ 好的做法
import functools

def good_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# ❌ 不好的做法
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### 2. 在类装饰器中也要保留元信息

```python
import functools

class ClassDecorator:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)  # 保留元信息
    
    def __call__(self, *args, **kwargs):
        print(f"调用 {self.func.__name__}")
        return self.func(*args, **kwargs)

@ClassDecorator
def decorated_function():
    """被类装饰器装饰的函数"""
    return "Hello"

print(f"函数名: {decorated_function.__name__}")
print(f"文档: {decorated_function.__doc__}")
```

### 3. 处理装饰器链

```python
import functools

def decorator_a(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("装饰器A")
        return func(*args, **kwargs)
    return wrapper

def decorator_b(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("装饰器B")
        return func(*args, **kwargs)
    return wrapper

@decorator_a
@decorator_b
def chained_function():
    """被多个装饰器装饰的函数"""
    return "原函数"

# 即使有多个装饰器，元信息仍然正确保留
print(f"函数名: {chained_function.__name__}")
print(f"文档: {chained_function.__doc__}")
```

## 小结

`functools.wraps` 的重要性：

1. **保留元信息**：确保装饰后的函数保持原有的名称、文档等信息
2. **调试友好**：错误信息和日志中显示正确的函数名
3. **工具兼容**：确保IDE、文档生成工具等能正确识别函数
4. **反射支持**：支持运行时检查函数的元信息
5. **专业标准**：这是编写装饰器的行业标准做法

**记住**：每当你编写装饰器时，都应该使用 `@functools.wraps(func)` 来装饰内部的包装函数。这是一个简单但重要的最佳实践，能让你的代码更加专业和可维护。

在下一章中，我们将学习Python内置的常用装饰器。