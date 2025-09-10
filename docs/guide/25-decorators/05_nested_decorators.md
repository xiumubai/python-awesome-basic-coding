# 装饰器的嵌套使用

装饰器可以嵌套使用，即在一个函数上应用多个装饰器。理解装饰器的执行顺序和相互作用对于正确使用嵌套装饰器至关重要。

## 装饰器的执行顺序

当多个装饰器应用于同一个函数时，它们的执行顺序是**从下到上**（从内到外）。

### 基本示例

```python
def decorator_a(func):
    print("装饰器A：装饰阶段")
    def wrapper(*args, **kwargs):
        print("装饰器A：执行前")
        result = func(*args, **kwargs)
        print("装饰器A：执行后")
        return result
    return wrapper

def decorator_b(func):
    print("装饰器B：装饰阶段")
    def wrapper(*args, **kwargs):
        print("装饰器B：执行前")
        result = func(*args, **kwargs)
        print("装饰器B：执行后")
        return result
    return wrapper

def decorator_c(func):
    print("装饰器C：装饰阶段")
    def wrapper(*args, **kwargs):
        print("装饰器C：执行前")
        result = func(*args, **kwargs)
        print("装饰器C：执行后")
        return result
    return wrapper

# 嵌套装饰器
@decorator_a
@decorator_b
@decorator_c
def my_function():
    print("原函数执行")
    return "函数结果"

print("\n=== 函数定义完成，开始调用 ===")
result = my_function()
print(f"\n最终结果: {result}")
```

**输出分析**：
1. **装饰阶段**（从下到上）：C → B → A
2. **执行阶段**（从外到内）：A → B → C → 原函数 → C → B → A

等价于：`decorator_a(decorator_b(decorator_c(my_function)))`

## 实际应用示例

### 1. 日志 + 计时 + 异常处理

```python
import functools
import time
import datetime

def log_calls(func):
    """记录函数调用日志"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] [LOG] 调用函数: {func.__name__}")
        
        result = func(*args, **kwargs)
        
        print(f"[{timestamp}] [LOG] 函数 {func.__name__} 执行完成")
        return result
    return wrapper

def measure_time(func):
    """测量函数执行时间"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[TIMER] 开始计时: {func.__name__}")
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"[TIMER] {func.__name__} 执行时间: {execution_time:.4f} 秒")
        return result
    return wrapper

def handle_exceptions(func):
    """处理函数异常"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print(f"[EXCEPTION] 开始执行: {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[EXCEPTION] {func.__name__} 执行成功")
            return result
        except Exception as e:
            print(f"[EXCEPTION] {func.__name__} 发生异常: {e}")
            print(f"[EXCEPTION] 异常类型: {type(e).__name__}")
            # 可以选择重新抛出异常或返回默认值
            raise
    return wrapper

# 组合使用装饰器
@log_calls
@measure_time
@handle_exceptions
def calculate_factorial(n):
    """计算阶乘"""
    if n < 0:
        raise ValueError("阶乘不能计算负数")
    
    print(f"  正在计算 {n} 的阶乘...")
    time.sleep(0.1)  # 模拟计算时间
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result

@log_calls
@measure_time
@handle_exceptions
def divide_numbers(a, b):
    """除法运算"""
    print(f"  正在计算 {a} ÷ {b}...")
    time.sleep(0.05)
    
    if b == 0:
        raise ZeroDivisionError("除数不能为零")
    
    return a / b

# 测试嵌套装饰器
print("=== 测试正常执行 ===")
result = calculate_factorial(5)
print(f"结果: {result}\n")

print("=== 测试异常处理 ===")
try:
    result = calculate_factorial(-3)
except ValueError as e:
    print(f"捕获异常: {e}\n")

print("=== 测试除法运算 ===")
result = divide_numbers(10, 2)
print(f"结果: {result}\n")

print("=== 测试除零异常 ===")
try:
    result = divide_numbers(5, 0)
except ZeroDivisionError as e:
    print(f"捕获异常: {e}")
```

### 2. 权限验证 + 缓存 + 重试

```python
import functools
import time
import random
from collections import OrderedDict

# 模拟用户权限系统
current_user = {
    "id": 1,
    "name": "Alice",
    "role": "admin",
    "permissions": ["read", "write", "delete"]
}

def require_permission(permission):
    """权限验证装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_permissions = current_user.get("permissions", [])
            
            if permission not in user_permissions:
                raise PermissionError(f"用户 {current_user['name']} 缺少权限: {permission}")
            
            print(f"[AUTH] 权限验证通过: {permission}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def cache_result(max_size=10, ttl=60):
    """结果缓存装饰器"""
    def decorator(func):
        cache = OrderedDict()
        timestamps = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 生成缓存键
            key = str(args) + str(sorted(kwargs.items()))
            current_time = time.time()
            
            # 检查缓存
            if key in cache:
                cache_time = timestamps.get(key, 0)
                if (current_time - cache_time) < ttl:
                    print(f"[CACHE] 缓存命中: {func.__name__}")
                    cache.move_to_end(key)  # LRU
                    return cache[key]
                else:
                    print(f"[CACHE] 缓存过期: {func.__name__}")
                    del cache[key]
                    del timestamps[key]
            
            print(f"[CACHE] 缓存未命中: {func.__name__}")
            result = func(*args, **kwargs)
            
            # 存储到缓存
            cache[key] = result
            timestamps[key] = current_time
            
            # 检查缓存大小
            if len(cache) > max_size:
                oldest_key = next(iter(cache))
                del cache[oldest_key]
                del timestamps[oldest_key]
            
            return result
        return wrapper
    return decorator

def retry_on_failure(max_attempts=3, delay=1):
    """失败重试装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    if attempt > 0:
                        print(f"[RETRY] 第 {attempt + 1}/{max_attempts} 次重试: {func.__name__}")
                        time.sleep(delay)
                    
                    result = func(*args, **kwargs)
                    
                    if attempt > 0:
                        print(f"[RETRY] 重试成功: {func.__name__}")
                    
                    return result
                    
                except Exception as e:
                    last_exception = e
                    print(f"[RETRY] 第 {attempt + 1} 次尝试失败: {e}")
                    
                    if attempt == max_attempts - 1:
                        print(f"[RETRY] 所有重试都失败了: {func.__name__}")
            
            raise last_exception
        return wrapper
    return decorator

# 组合使用多个装饰器
@require_permission("read")
@cache_result(max_size=5, ttl=10)
@retry_on_failure(max_attempts=3, delay=0.5)
def fetch_user_data(user_id):
    """获取用户数据"""
    print(f"  正在从数据库获取用户 {user_id} 的数据...")
    
    # 模拟网络不稳定
    if random.random() < 0.4:  # 40%失败率
        raise ConnectionError("数据库连接失败")
    
    time.sleep(0.2)  # 模拟数据库查询时间
    return {
        "id": user_id,
        "name": f"User_{user_id}",
        "email": f"user{user_id}@example.com"
    }

@require_permission("write")
@retry_on_failure(max_attempts=2, delay=0.3)
def update_user_data(user_id, data):
    """更新用户数据"""
    print(f"  正在更新用户 {user_id} 的数据: {data}")
    
    # 模拟更新操作可能失败
    if random.random() < 0.3:  # 30%失败率
        raise RuntimeError("数据更新失败")
    
    time.sleep(0.1)
    return f"用户 {user_id} 数据更新成功"

@require_permission("delete")
@cache_result(max_size=3, ttl=5)
@retry_on_failure(max_attempts=4, delay=0.2)
def delete_user_data(user_id):
    """删除用户数据"""
    print(f"  正在删除用户 {user_id} 的数据...")
    
    # 模拟删除操作
    if random.random() < 0.5:  # 50%失败率
        raise RuntimeError("删除操作失败")
    
    time.sleep(0.15)
    return f"用户 {user_id} 已删除"

# 测试嵌套装饰器的组合效果
print(f"当前用户: {current_user['name']} (权限: {current_user['permissions']})\n")

print("=== 测试获取用户数据（权限+缓存+重试） ===")
try:
    # 第一次调用
    result = fetch_user_data(123)
    print(f"结果: {result}\n")
    
    # 第二次调用（应该命中缓存）
    result = fetch_user_data(123)
    print(f"结果: {result}\n")
    
except Exception as e:
    print(f"最终失败: {e}\n")

print("=== 测试更新用户数据（权限+重试） ===")
try:
    result = update_user_data(123, {"name": "New Name"})
    print(f"结果: {result}\n")
except Exception as e:
    print(f"最终失败: {e}\n")

print("=== 测试删除用户数据（权限+缓存+重试） ===")
try:
    result = delete_user_data(456)
    print(f"结果: {result}\n")
except Exception as e:
    print(f"最终失败: {e}\n")

# 测试权限不足的情况
print("=== 测试权限不足 ===")
current_user["permissions"] = ["read"]  # 移除写权限

try:
    result = update_user_data(789, {"email": "new@example.com"})
except PermissionError as e:
    print(f"权限错误: {e}")
```

### 3. 装饰器顺序的重要性

```python
import functools
import time

def timing_decorator(func):
    """计时装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMING] {func.__name__} 执行时间: {end - start:.4f} 秒")
        return result
    return wrapper

def caching_decorator(func):
    """缓存装饰器"""
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in cache:
            print(f"[CACHE] 缓存命中: {func.__name__}")
            return cache[key]
        
        print(f"[CACHE] 缓存未命中: {func.__name__}")
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

def slow_function(n):
    """模拟耗时函数"""
    print(f"  正在计算 {n}...")
    time.sleep(0.5)
    return n * n

# 顺序1：先计时，后缓存
print("=== 顺序1：@timing_decorator @caching_decorator ===")

@timing_decorator
@caching_decorator
def func1(n):
    return slow_function(n)

print("第一次调用:")
result = func1(5)
print(f"结果: {result}\n")

print("第二次调用（缓存命中）:")
result = func1(5)
print(f"结果: {result}\n")

# 顺序2：先缓存，后计时
print("=== 顺序2：@caching_decorator @timing_decorator ===")

@caching_decorator
@timing_decorator
def func2(n):
    return slow_function(n)

print("第一次调用:")
result = func2(10)
print(f"结果: {result}\n")

print("第二次调用（缓存命中）:")
result = func2(10)
print(f"结果: {result}\n")
```

**顺序分析**：
- **顺序1**：计时包含缓存查找时间，缓存命中时仍会显示很小的执行时间
- **顺序2**：计时只包含实际函数执行时间，缓存命中时不会触发计时

### 4. 装饰器参数传递

```python
import functools

def validate_input(input_type=str, min_value=None, max_value=None):
    """输入验证装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 验证第一个参数
            if args:
                value = args[0]
                
                # 类型检查
                if not isinstance(value, input_type):
                    raise TypeError(f"参数类型错误，期望 {input_type.__name__}，得到 {type(value).__name__}")
                
                # 范围检查
                if input_type in (int, float):
                    if min_value is not None and value < min_value:
                        raise ValueError(f"参数值 {value} 小于最小值 {min_value}")
                    if max_value is not None and value > max_value:
                        raise ValueError(f"参数值 {value} 大于最大值 {max_value}")
                
                print(f"[VALIDATE] 输入验证通过: {value}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def format_output(format_type="json", precision=2):
    """输出格式化装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            if format_type == "json":
                import json
                if isinstance(result, dict):
                    formatted = json.dumps(result, indent=2)
                else:
                    formatted = json.dumps({"result": result}, indent=2)
            elif format_type == "xml":
                formatted = f"<result>{result}</result>"
            elif format_type == "csv":
                if isinstance(result, dict):
                    formatted = ",".join(f"{k}={v}" for k, v in result.items())
                else:
                    formatted = str(result)
            else:
                formatted = str(result)
            
            print(f"[FORMAT] 输出格式: {format_type}")
            return formatted
        return wrapper
    return decorator

# 组合使用带参数的装饰器
@format_output(format_type="json", precision=3)
@validate_input(input_type=int, min_value=1, max_value=100)
def calculate_circle_area(radius):
    """计算圆的面积"""
    import math
    area = math.pi * radius ** 2
    return {
        "radius": radius,
        "area": round(area, 3),
        "circumference": round(2 * math.pi * radius, 3)
    }

@format_output(format_type="xml")
@validate_input(input_type=str)
def process_text(text):
    """处理文本"""
    return {
        "original": text,
        "length": len(text),
        "uppercase": text.upper(),
        "word_count": len(text.split())
    }

# 测试组合装饰器
print("=== 测试圆面积计算 ===")
try:
    result = calculate_circle_area(5)
    print(f"结果:\n{result}\n")
except (TypeError, ValueError) as e:
    print(f"验证错误: {e}\n")

print("=== 测试无效输入 ===")
try:
    result = calculate_circle_area(150)  # 超出范围
except ValueError as e:
    print(f"验证错误: {e}\n")

print("=== 测试文本处理 ===")
try:
    result = process_text("Hello World Python")
    print(f"结果: {result}\n")
except TypeError as e:
    print(f"验证错误: {e}")
```

## 嵌套装饰器的最佳实践

### 1. 合理安排装饰器顺序

```python
# 推荐顺序（从外到内）：
# 1. 权限验证（最外层，优先检查）
# 2. 输入验证（验证参数）
# 3. 缓存（避免重复计算）
# 4. 重试（处理失败）
# 5. 计时/日志（记录执行过程）
# 6. 异常处理（最内层，捕获所有异常）

@require_permission("admin")
@validate_input(int, min_value=1)
@cache_result(ttl=300)
@retry_on_failure(max_attempts=3)
@measure_time
@handle_exceptions
def complex_operation(data_id):
    # 函数实现
    pass
```

### 2. 避免装饰器冲突

```python
# 注意：某些装饰器组合可能产生意外行为

# 问题：缓存装饰器可能缓存异常
@caching_decorator  # 可能缓存异常结果
@handle_exceptions  # 异常处理
def risky_function():
    pass

# 解决：调整顺序
@handle_exceptions  # 先处理异常
@caching_decorator  # 再缓存正常结果
def safe_function():
    pass
```

### 3. 保持装饰器的独立性

```python
# 好的做法：每个装饰器功能单一，互不依赖
def log_decorator(func):
    # 只负责日志记录
    pass

def cache_decorator(func):
    # 只负责缓存
    pass

# 避免：装饰器之间有依赖关系
def dependent_decorator(func):
    # 不要依赖其他装饰器的行为
    pass
```

## 小结

装饰器嵌套使用的关键点：

1. **执行顺序**：装饰时从下到上，执行时从外到内
2. **顺序重要性**：不同顺序可能产生不同效果
3. **功能组合**：权限验证、缓存、重试、日志等可以有效组合
4. **避免冲突**：注意装饰器之间的相互影响
5. **保持独立**：每个装饰器应该功能单一，互不依赖

通过合理使用嵌套装饰器，我们可以构建功能强大且模块化的代码。在下一章中，我们将学习 `functools.wraps` 的重要作用。