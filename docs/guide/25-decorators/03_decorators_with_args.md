# 带参数的装饰器

带参数的装饰器是装饰器的高级形式，它们允许我们在应用装饰器时传递参数，从而创建更加灵活和可配置的装饰器。

## 理解三层嵌套结构

带参数的装饰器需要三层函数嵌套：
1. **最外层**：接收装饰器参数的函数（装饰器工厂）
2. **中间层**：接收被装饰函数的函数（真正的装饰器）
3. **最内层**：接收被装饰函数参数的函数（包装器函数）

### 基本结构

```python
def decorator_with_args(arg1, arg2):
    """装饰器工厂函数 - 接收装饰器参数"""
    def decorator(func):
        """真正的装饰器函数 - 接收被装饰的函数"""
        def wrapper(*args, **kwargs):
            """包装器函数 - 接收被装饰函数的参数"""
            # 在这里可以使用 arg1, arg2, func, args, kwargs
            print(f"装饰器参数: {arg1}, {arg2}")
            print(f"被装饰函数: {func.__name__}")
            print(f"函数参数: {args}, {kwargs}")
            
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# 使用方式
@decorator_with_args("参数1", "参数2")
def my_function():
    print("Hello, World!")

# 等价于
# my_function = decorator_with_args("参数1", "参数2")(my_function)
```

## 实际应用示例

### 1. 可配置的日志装饰器

```python
import functools
import datetime

def log_with_level(level="INFO", include_args=True, include_result=True):
    """可配置的日志装饰器
    
    Args:
        level: 日志级别
        include_args: 是否记录函数参数
        include_result: 是否记录函数返回值
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # 记录函数调用开始
            log_message = f"[{timestamp}] [{level}] 调用函数: {func.__name__}"
            
            if include_args and (args or kwargs):
                log_message += f" | 参数: args={args}, kwargs={kwargs}"
            
            print(log_message)
            
            try:
                # 执行函数
                result = func(*args, **kwargs)
                
                # 记录成功结果
                if include_result:
                    print(f"[{timestamp}] [{level}] 函数 {func.__name__} 执行成功 | 返回值: {result}")
                else:
                    print(f"[{timestamp}] [{level}] 函数 {func.__name__} 执行成功")
                
                return result
                
            except Exception as e:
                # 记录异常
                print(f"[{timestamp}] [ERROR] 函数 {func.__name__} 执行失败 | 异常: {e}")
                raise
        
        return wrapper
    return decorator

# 不同配置的使用示例
@log_with_level(level="DEBUG", include_args=True, include_result=True)
def calculate_area(length, width):
    """计算矩形面积"""
    return length * width

@log_with_level(level="INFO", include_args=False, include_result=False)
def send_email(to, subject, body):
    """发送邮件"""
    print(f"发送邮件到 {to}: {subject}")
    return "邮件发送成功"

@log_with_level(level="WARNING", include_args=True, include_result=True)
def divide_numbers(a, b):
    """除法运算"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

# 测试不同配置的日志装饰器
print("=== 测试详细日志 ===")
area = calculate_area(5, 3)
print(f"面积: {area}\n")

print("=== 测试简单日志 ===")
result = send_email("user@example.com", "测试", "这是测试邮件")
print(f"结果: {result}\n")

print("=== 测试异常日志 ===")
try:
    divide_numbers(10, 0)
except ValueError as e:
    print(f"捕获异常: {e}")
```

### 2. 重试装饰器

```python
import functools
import time
import random

def retry(max_attempts=3, delay=1, backoff=2, exceptions=(Exception,)):
    """重试装饰器
    
    Args:
        max_attempts: 最大重试次数
        delay: 初始延迟时间（秒）
        backoff: 延迟时间倍数
        exceptions: 需要重试的异常类型
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    print(f"[重试] 第 {attempt + 1}/{max_attempts} 次尝试: {func.__name__}")
                    result = func(*args, **kwargs)
                    
                    if attempt > 0:
                        print(f"[重试] 函数 {func.__name__} 在第 {attempt + 1} 次尝试后成功")
                    
                    return result
                    
                except exceptions as e:
                    last_exception = e
                    print(f"[重试] 第 {attempt + 1} 次尝试失败: {e}")
                    
                    if attempt < max_attempts - 1:
                        print(f"[重试] 等待 {current_delay:.1f} 秒后重试...")
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        print(f"[重试] 所有 {max_attempts} 次尝试都失败了")
            
            # 重新抛出最后一个异常
            raise last_exception
        
        return wrapper
    return decorator

# 不同配置的重试装饰器
@retry(max_attempts=3, delay=0.5, backoff=2)
def unstable_api_call():
    """模拟不稳定的API调用"""
    if random.random() < 0.7:  # 70%失败率
        raise ConnectionError("API连接失败")
    return "API调用成功"

@retry(max_attempts=5, delay=0.1, backoff=1.5, exceptions=(ValueError, TypeError))
def data_processing(data):
    """模拟数据处理"""
    if not data:
        raise ValueError("数据为空")
    
    if random.random() < 0.6:  # 60%失败率
        raise ValueError("数据格式错误")
    
    return f"处理完成: {data}"

@retry(max_attempts=2, delay=1, exceptions=(FileNotFoundError,))
def read_config_file(filename):
    """读取配置文件"""
    if random.random() < 0.5:  # 50%失败率
        raise FileNotFoundError(f"找不到文件: {filename}")
    return f"配置文件 {filename} 读取成功"

# 测试重试功能
print("=== 测试API调用重试 ===")
try:
    result = unstable_api_call()
    print(f"最终结果: {result}\n")
except Exception as e:
    print(f"最终失败: {e}\n")

print("=== 测试数据处理重试 ===")
try:
    result = data_processing("test_data")
    print(f"最终结果: {result}\n")
except Exception as e:
    print(f"最终失败: {e}\n")
```

### 3. 缓存装饰器

```python
import functools
import time
from collections import OrderedDict

def cache(max_size=128, ttl=None):
    """缓存装饰器
    
    Args:
        max_size: 最大缓存条目数
        ttl: 缓存生存时间（秒），None表示永不过期
    """
    def decorator(func):
        cache_data = OrderedDict()
        cache_times = {}  # 存储缓存时间
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 创建缓存键
            key = str(args) + str(sorted(kwargs.items()))
            current_time = time.time()
            
            # 检查缓存是否存在且未过期
            if key in cache_data:
                cache_time = cache_times.get(key, 0)
                
                # 检查TTL
                if ttl is None or (current_time - cache_time) < ttl:
                    print(f"[缓存] 命中: {func.__name__}{args}")
                    # 移动到末尾（LRU策略）
                    cache_data.move_to_end(key)
                    return cache_data[key]
                else:
                    print(f"[缓存] 过期: {func.__name__}{args}")
                    del cache_data[key]
                    del cache_times[key]
            
            # 缓存未命中，计算结果
            print(f"[缓存] 计算: {func.__name__}{args}")
            result = func(*args, **kwargs)
            
            # 存储到缓存
            cache_data[key] = result
            cache_times[key] = current_time
            
            # 检查缓存大小限制
            if len(cache_data) > max_size:
                # 删除最旧的条目
                oldest_key = next(iter(cache_data))
                del cache_data[oldest_key]
                del cache_times[oldest_key]
                print(f"[缓存] 删除最旧条目，当前大小: {len(cache_data)}")
            
            return result
        
        # 添加缓存管理方法
        def cache_info():
            return {
                'size': len(cache_data),
                'max_size': max_size,
                'ttl': ttl,
                'keys': list(cache_data.keys())
            }
        
        def clear_cache():
            cache_data.clear()
            cache_times.clear()
            print("[缓存] 已清空")
        
        wrapper.cache_info = cache_info
        wrapper.clear_cache = clear_cache
        
        return wrapper
    return decorator

# 不同配置的缓存装饰器
@cache(max_size=3, ttl=2)  # 最多3个条目，2秒过期
def fibonacci(n):
    """计算斐波那契数"""
    if n <= 1:
        return n
    time.sleep(0.1)  # 模拟计算时间
    return fibonacci(n-1) + fibonacci(n-2)

@cache(max_size=5, ttl=None)  # 最多5个条目，永不过期
def expensive_calculation(x, y):
    """模拟耗时计算"""
    time.sleep(0.5)
    return x ** y

# 测试缓存功能
print("=== 测试斐波那契缓存（带TTL） ===")
print(f"fibonacci(5) = {fibonacci(5)}")
print(f"缓存信息: {fibonacci.cache_info()}\n")

print("再次计算相同值:")
print(f"fibonacci(5) = {fibonacci(5)}")
print(f"缓存信息: {fibonacci.cache_info()}\n")

print("等待缓存过期...")
time.sleep(3)
print(f"fibonacci(5) = {fibonacci(5)}")
print(f"缓存信息: {fibonacci.cache_info()}\n")

print("=== 测试计算缓存（无TTL） ===")
print(f"expensive_calculation(2, 3) = {expensive_calculation(2, 3)}")
print(f"expensive_calculation(3, 2) = {expensive_calculation(3, 2)}")
print(f"缓存信息: {expensive_calculation.cache_info()}")
```

### 4. 权限控制装饰器

```python
import functools
from enum import Enum

class Permission(Enum):
    READ = "read"
    WRITE = "write"
    DELETE = "delete"
    ADMIN = "admin"

# 模拟当前用户
current_user = {
    "id": 1,
    "name": "Alice",
    "role": "admin",
    "permissions": [Permission.READ, Permission.WRITE, Permission.DELETE, Permission.ADMIN]
}

def require_permissions(*required_permissions, allow_admin=True, raise_exception=True):
    """权限控制装饰器
    
    Args:
        required_permissions: 需要的权限列表
        allow_admin: 是否允许管理员绕过权限检查
        raise_exception: 权限不足时是否抛出异常
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_permissions = current_user.get("permissions", [])
            user_role = current_user.get("role", "guest")
            
            # 检查管理员权限
            if allow_admin and user_role == "admin":
                print(f"[权限] 管理员 {current_user['name']} 访问 {func.__name__}")
                return func(*args, **kwargs)
            
            # 检查具体权限
            missing_permissions = []
            for perm in required_permissions:
                if perm not in user_permissions:
                    missing_permissions.append(perm.value)
            
            if missing_permissions:
                error_msg = f"用户 {current_user['name']} 缺少权限: {missing_permissions}"
                print(f"[权限] 拒绝访问: {error_msg}")
                
                if raise_exception:
                    raise PermissionError(error_msg)
                else:
                    return None
            
            print(f"[权限] 允许用户 {current_user['name']} 访问 {func.__name__}")
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

# 不同权限要求的函数
@require_permissions(Permission.READ)
def view_data(data_id):
    """查看数据"""
    return f"数据 {data_id} 的内容"

@require_permissions(Permission.WRITE)
def create_data(data):
    """创建数据"""
    return f"已创建数据: {data}"

@require_permissions(Permission.READ, Permission.WRITE)
def update_data(data_id, new_data):
    """更新数据"""
    return f"已更新数据 {data_id}: {new_data}"

@require_permissions(Permission.DELETE, allow_admin=False)
def delete_data(data_id):
    """删除数据（管理员也需要删除权限）"""
    return f"已删除数据 {data_id}"

@require_permissions(Permission.ADMIN, raise_exception=False)
def admin_operation():
    """管理员操作（权限不足时返回None而不抛异常）"""
    return "管理员操作完成"

# 测试权限控制
print(f"当前用户: {current_user['name']} ({current_user['role']})")
print(f"用户权限: {[p.value for p in current_user['permissions']]}\n")

print("=== 测试各种权限操作 ===")
try:
    result = view_data(123)
    print(f"查看结果: {result}\n")
    
    result = create_data("新数据")
    print(f"创建结果: {result}\n")
    
    result = update_data(123, "更新的数据")
    print(f"更新结果: {result}\n")
    
    result = delete_data(123)
    print(f"删除结果: {result}\n")
    
except PermissionError as e:
    print(f"权限错误: {e}\n")

# 切换到普通用户
current_user = {
    "id": 2,
    "name": "Bob",
    "role": "user",
    "permissions": [Permission.READ]
}

print(f"切换用户: {current_user['name']} ({current_user['role']})")
print(f"用户权限: {[p.value for p in current_user['permissions']]}\n")

print("=== 测试权限限制 ===")
try:
    result = view_data(456)
    print(f"查看结果: {result}\n")
    
    result = create_data("新数据2")
    print(f"创建结果: {result}\n")
    
except PermissionError as e:
    print(f"权限错误: {e}\n")

# 测试不抛异常的情况
result = admin_operation()
print(f"管理员操作结果: {result}")
```

### 5. 性能监控装饰器

```python
import functools
import time
import psutil
import os

def performance_monitor(log_memory=True, log_time=True, threshold_seconds=None):
    """性能监控装饰器
    
    Args:
        log_memory: 是否记录内存使用
        log_time: 是否记录执行时间
        threshold_seconds: 执行时间阈值，超过时发出警告
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 记录开始状态
            start_time = time.time()
            
            if log_memory:
                process = psutil.Process(os.getpid())
                start_memory = process.memory_info().rss / 1024 / 1024  # MB
            
            print(f"[性能] 开始执行: {func.__name__}")
            
            try:
                # 执行函数
                result = func(*args, **kwargs)
                
                # 记录结束状态
                end_time = time.time()
                execution_time = end_time - start_time
                
                # 记录执行时间
                if log_time:
                    print(f"[性能] 执行时间: {execution_time:.4f} 秒")
                    
                    # 检查阈值
                    if threshold_seconds and execution_time > threshold_seconds:
                        print(f"[性能] ⚠️  警告: 执行时间 {execution_time:.4f}s 超过阈值 {threshold_seconds}s")
                
                # 记录内存使用
                if log_memory:
                    end_memory = process.memory_info().rss / 1024 / 1024  # MB
                    memory_diff = end_memory - start_memory
                    print(f"[性能] 内存使用: {end_memory:.2f} MB (变化: {memory_diff:+.2f} MB)")
                
                return result
                
            except Exception as e:
                end_time = time.time()
                execution_time = end_time - start_time
                print(f"[性能] 执行失败，耗时: {execution_time:.4f} 秒")
                raise
        
        return wrapper
    return decorator

# 不同配置的性能监控
@performance_monitor(log_memory=True, log_time=True, threshold_seconds=0.5)
def cpu_intensive_task(n):
    """CPU密集型任务"""
    result = 0
    for i in range(n):
        result += i ** 2
    return result

@performance_monitor(log_memory=True, log_time=True)
def memory_intensive_task(size):
    """内存密集型任务"""
    # 创建大列表
    big_list = [i for i in range(size)]
    # 进行一些操作
    result = sum(big_list)
    return result

@performance_monitor(log_memory=False, log_time=True, threshold_seconds=0.1)
def io_task():
    """IO任务"""
    time.sleep(0.2)  # 模拟IO等待
    return "IO完成"

# 测试性能监控
print("=== 测试CPU密集型任务 ===")
result = cpu_intensive_task(100000)
print(f"结果: {result}\n")

print("=== 测试内存密集型任务 ===")
result = memory_intensive_task(1000000)
print(f"结果前10位: {str(result)[:10]}...\n")

print("=== 测试IO任务（会触发时间阈值警告） ===")
result = io_task()
print(f"结果: {result}")
```

## 装饰器参数的最佳实践

### 1. 提供默认值

```python
def my_decorator(param1="default", param2=None):
    """提供合理的默认值"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 使用参数
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 可以不传参数
@my_decorator()
def func1():
    pass

# 也可以传部分参数
@my_decorator(param1="custom")
def func2():
    pass
```

### 2. 参数验证

```python
def validated_decorator(max_retries=3, delay=1.0):
    """带参数验证的装饰器"""
    # 验证参数
    if not isinstance(max_retries, int) or max_retries < 1:
        raise ValueError("max_retries必须是正整数")
    
    if not isinstance(delay, (int, float)) or delay < 0:
        raise ValueError("delay必须是非负数")
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 装饰器逻辑
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### 3. 支持无参数调用

```python
def flexible_decorator(func=None, *, param1="default", param2=None):
    """支持有参数和无参数两种调用方式的装饰器"""
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            print(f"参数: {param1}, {param2}")
            return f(*args, **kwargs)
        return wrapper
    
    if func is None:
        # 带参数调用: @flexible_decorator(param1="value")
        return decorator
    else:
        # 无参数调用: @flexible_decorator
        return decorator(func)

# 两种使用方式
@flexible_decorator
def func1():
    pass

@flexible_decorator(param1="custom")
def func2():
    pass
```

## 小结

带参数的装饰器通过三层嵌套结构提供了强大的灵活性：

1. **装饰器工厂**：接收配置参数，返回真正的装饰器
2. **装饰器函数**：接收被装饰的函数，返回包装器
3. **包装器函数**：接收函数参数，执行实际逻辑

通过合理使用带参数的装饰器，我们可以创建高度可配置和可重用的代码组件。在下一章中，我们将学习类装饰器，探索另一种实现装饰器的方式。