# 装饰器基础概念和原理

装饰器是Python中一个强大而优雅的特性，它允许我们在不修改原函数代码的情况下，为函数添加额外的功能。

## 什么是装饰器

装饰器本质上是一个函数，它接受一个函数作为参数，并返回一个新的函数。装饰器可以在函数执行前后添加额外的逻辑，而不需要修改原函数的代码。

## 基本概念

### 1. 函数是一等公民

在Python中，函数是一等公民，这意味着：
- 函数可以作为参数传递给其他函数
- 函数可以作为返回值
- 函数可以赋值给变量
- 函数可以存储在数据结构中

```python
def greet(name):
    return f"Hello, {name}!"

# 函数可以赋值给变量
say_hello = greet
print(say_hello("Alice"))  # 输出: Hello, Alice!

# 函数可以作为参数传递
def call_function(func, arg):
    return func(arg)

result = call_function(greet, "Bob")
print(result)  # 输出: Hello, Bob!
```

### 2. 高阶函数

高阶函数是接受函数作为参数或返回函数的函数：

```python
def make_multiplier(n):
    """返回一个乘法函数"""
    def multiplier(x):
        return x * n
    return multiplier

# 创建一个乘以2的函数
double = make_multiplier(2)
print(double(5))  # 输出: 10

# 创建一个乘以3的函数
triple = make_multiplier(3)
print(triple(4))  # 输出: 12
```

## 装饰器的基本形式

### 1. 手动装饰

```python
def my_decorator(func):
    """一个简单的装饰器"""
    def wrapper():
        print("函数执行前")
        result = func()
        print("函数执行后")
        return result
    return wrapper

def say_hello():
    print("Hello, World!")

# 手动应用装饰器
decorated_function = my_decorator(say_hello)
decorated_function()
```

输出：
```
函数执行前
Hello, World!
函数执行后
```

### 2. 使用@语法糖

```python
def my_decorator(func):
    """一个简单的装饰器"""
    def wrapper():
        print("函数执行前")
        result = func()
        print("函数执行后")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello, World!")

# 直接调用装饰后的函数
say_hello()
```

`@my_decorator` 等价于 `say_hello = my_decorator(say_hello)`

## 装饰器的工作原理

### 执行时机

装饰器在函数定义时就会执行，而不是在函数调用时：

```python
print("开始定义装饰器")

def my_decorator(func):
    print(f"装饰器正在装饰函数: {func.__name__}")
    
    def wrapper():
        print("wrapper函数执行")
        return func()
    
    print("装饰器执行完毕")
    return wrapper

print("开始定义被装饰的函数")

@my_decorator
def greet():
    print("Hello from greet!")

print("函数定义完毕")
print("现在调用函数")
greet()
```

输出：
```
开始定义装饰器
开始定义被装饰的函数
装饰器正在装饰函数: greet
装饰器执行完毕
函数定义完毕
现在调用函数
wrapper函数执行
Hello from greet!
```

## 实际应用示例

### 1. 日志装饰器

```python
import datetime

def log_calls(func):
    """记录函数调用的装饰器"""
    def wrapper():
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] 调用函数: {func.__name__}")
        result = func()
        print(f"[{timestamp}] 函数 {func.__name__} 执行完毕")
        return result
    return wrapper

@log_calls
def calculate_sum():
    """计算1到100的和"""
    return sum(range(1, 101))

result = calculate_sum()
print(f"结果: {result}")
```

### 2. 计时装饰器

```python
import time

def timing_decorator(func):
    """测量函数执行时间的装饰器"""
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"函数 {func.__name__} 执行时间: {execution_time:.4f} 秒")
        return result
    return wrapper

@timing_decorator
def slow_function():
    """一个执行较慢的函数"""
    time.sleep(1)
    return "任务完成"

result = slow_function()
print(result)
```

### 3. 重试装饰器

```python
import random
import time

def retry_decorator(func):
    """重试装饰器，失败时重试"""
    def wrapper():
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                print(f"尝试第 {attempt + 1} 次")
                result = func()
                print("成功!")
                return result
            except Exception as e:
                print(f"失败: {e}")
                if attempt < max_attempts - 1:
                    print("重试中...")
                    time.sleep(1)
                else:
                    print("所有尝试都失败了")
                    raise
    return wrapper

@retry_decorator
def unreliable_function():
    """一个不稳定的函数"""
    if random.random() < 0.7:  # 70%的概率失败
        raise Exception("随机失败")
    return "操作成功"

# 测试重试功能
try:
    result = unreliable_function()
    print(f"最终结果: {result}")
except Exception as e:
    print(f"最终失败: {e}")
```

## 装饰器的优势

1. **代码复用**：同一个装饰器可以应用到多个函数
2. **关注点分离**：将横切关注点（如日志、缓存）从业务逻辑中分离
3. **代码简洁**：使用@语法糖使代码更加简洁易读
4. **不侵入性**：不需要修改原函数的代码

## 注意事项

1. **函数签名**：简单的装饰器可能会改变函数的签名
2. **性能开销**：装饰器会增加函数调用的开销
3. **调试困难**：装饰器可能会使调试变得复杂
4. **元信息丢失**：装饰后的函数可能会丢失原函数的元信息

## 小结

装饰器是Python中一个强大的特性，它基于函数是一等公民和高阶函数的概念。通过装饰器，我们可以：

- 在不修改原函数的情况下添加功能
- 实现代码的复用和模块化
- 优雅地处理横切关注点

掌握装饰器的基本概念和原理是学习更高级装饰器技术的基础。在后续的学习中，我们将探讨如何处理带参数的函数、如何创建带参数的装饰器，以及如何使用functools.wraps来保持函数的元信息。