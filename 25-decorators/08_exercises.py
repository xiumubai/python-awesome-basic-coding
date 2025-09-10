#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
装饰器综合练习

这个文件包含了装饰器相关的综合练习题目和解答，
涵盖了从基础到高级的各种装饰器应用场景。

练习内容：
1. 基础装饰器练习
2. 带参数装饰器练习
3. 类装饰器练习
4. 装饰器链练习
5. 实际应用场景练习
6. 高级装饰器练习
7. 性能优化练习
8. 综合项目练习
"""

import functools
import time
import threading
import json
import hashlib
import weakref
from datetime import datetime, timedelta
from typing import Any, Callable, Dict, List, Optional, Union
from collections import defaultdict, Counter
import inspect
import warnings

# 全局配置变量
PROFILING_ENABLED = False


def main():
    """主函数，运行所有练习"""
    print("=" * 60)
    print("装饰器综合练习")
    print("=" * 60)
    
    # 运行所有练习
    exercise_1_basic_decorators()
    exercise_2_parameterized_decorators()
    exercise_3_class_decorators()
    exercise_4_decorator_chains()
    exercise_5_practical_applications()
    exercise_6_advanced_decorators()
    exercise_7_performance_optimization()
    exercise_8_comprehensive_project()


def exercise_1_basic_decorators():
    """练习1：基础装饰器"""
    print("\n" + "=" * 50)
    print("练习1：基础装饰器")
    print("=" * 50)
    
    # 题目1：创建一个简单的日志装饰器
    print("\n题目1：创建一个简单的日志装饰器")
    print("-" * 30)
    
    def log_calls(func):
        """记录函数调用的装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG] 调用函数 {func.__name__}")
            print(f"[LOG] 参数: args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"[LOG] 返回值: {result}")
            return result
        return wrapper
    
    @log_calls
    def add(a, b):
        """加法函数"""
        return a + b
    
    @log_calls
    def greet(name, greeting="Hello"):
        """问候函数"""
        return f"{greeting}, {name}!"
    
    print("测试日志装饰器：")
    result1 = add(3, 5)
    result2 = greet("Alice", greeting="Hi")
    
    # 题目2：创建一个计时装饰器
    print("\n题目2：创建一个计时装饰器")
    print("-" * 30)
    
    def timing(func):
        """计时装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time
            print(f"[TIMING] {func.__name__} 执行时间: {duration:.4f}秒")
            return result
        return wrapper
    
    @timing
    def slow_function():
        """模拟慢函数"""
        time.sleep(0.1)
        return "完成"
    
    @timing
    def calculate_sum(n):
        """计算1到n的和"""
        return sum(range(1, n + 1))
    
    print("测试计时装饰器：")
    result1 = slow_function()
    result2 = calculate_sum(1000000)
    
    # 题目3：创建一个异常处理装饰器
    print("\n题目3：创建一个异常处理装饰器")
    print("-" * 30)
    
    def handle_exceptions(func):
        """异常处理装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"[ERROR] {func.__name__} 发生异常: {type(e).__name__}: {e}")
                return None
        return wrapper
    
    @handle_exceptions
    def divide(a, b):
        """除法函数"""
        return a / b
    
    @handle_exceptions
    def access_list(lst, index):
        """访问列表元素"""
        return lst[index]
    
    print("测试异常处理装饰器：")
    result1 = divide(10, 2)
    print(f"10 / 2 = {result1}")
    
    result2 = divide(10, 0)
    print(f"10 / 0 = {result2}")
    
    result3 = access_list([1, 2, 3], 1)
    print(f"列表[1, 2, 3]的索引1: {result3}")
    
    result4 = access_list([1, 2, 3], 10)
    print(f"列表[1, 2, 3]的索引10: {result4}")


def exercise_2_parameterized_decorators():
    """练习2：带参数装饰器"""
    print("\n" + "=" * 50)
    print("练习2：带参数装饰器")
    print("=" * 50)
    
    # 题目1：创建一个可配置的重试装饰器
    print("\n题目1：创建一个可配置的重试装饰器")
    print("-" * 30)
    
    def retry(max_attempts=3, delay=1.0, exceptions=(Exception,)):
        """重试装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                last_exception = None
                for attempt in range(max_attempts):
                    try:
                        return func(*args, **kwargs)
                    except exceptions as e:
                        last_exception = e
                        if attempt < max_attempts - 1:
                            print(f"[RETRY] {func.__name__} 第{attempt + 1}次尝试失败: {e}")
                            print(f"[RETRY] {delay}秒后重试...")
                            time.sleep(delay)
                        else:
                            print(f"[RETRY] {func.__name__} 所有尝试都失败了")
                raise last_exception
            return wrapper
        return decorator
    
    # 模拟不稳定的网络请求
    class NetworkError(Exception):
        pass
    
    # 使用闭包来管理状态
    def create_unstable_request():
        attempt_count = 0
        
        @retry(max_attempts=3, delay=0.5, exceptions=(NetworkError,))
        def unstable_network_request():
            """不稳定的网络请求"""
            nonlocal attempt_count
            attempt_count += 1
            if attempt_count < 3:
                raise NetworkError(f"网络连接失败 (尝试 {attempt_count})")
            return "请求成功"
        
        return unstable_network_request
    
    unstable_network_request = create_unstable_request()
    
    print("测试重试装饰器：")
    try:
        result = unstable_network_request()
        print(f"最终结果: {result}")
    except NetworkError as e:
        print(f"最终失败: {e}")
    
    # 题目2：创建一个缓存装饰器
    print("\n题目2：创建一个缓存装饰器")
    print("-" * 30)
    
    def cache(max_size=128, ttl=None):
        """缓存装饰器
        
        Args:
            max_size: 最大缓存大小
            ttl: 缓存过期时间（秒）
        """
        def decorator(func):
            cache_data = {}
            access_times = {}
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 创建缓存键
                key = str(args) + str(sorted(kwargs.items()))
                current_time = time.time()
                
                # 检查缓存是否存在且未过期
                if key in cache_data:
                    if ttl is None or (current_time - access_times[key]) < ttl:
                        print(f"[CACHE] 缓存命中: {func.__name__}")
                        return cache_data[key]
                    else:
                        print(f"[CACHE] 缓存过期: {func.__name__}")
                        del cache_data[key]
                        del access_times[key]
                
                # 执行函数并缓存结果
                print(f"[CACHE] 缓存未命中，执行函数: {func.__name__}")
                result = func(*args, **kwargs)
                
                # 如果缓存已满，删除最旧的条目
                if len(cache_data) >= max_size:
                    oldest_key = min(access_times.keys(), key=lambda k: access_times[k])
                    del cache_data[oldest_key]
                    del access_times[oldest_key]
                
                cache_data[key] = result
                access_times[key] = current_time
                return result
            
            # 添加缓存信息方法
            def cache_info():
                return {
                    'size': len(cache_data),
                    'max_size': max_size,
                    'ttl': ttl,
                    'keys': list(cache_data.keys())
                }
            
            wrapper.cache_info = cache_info
            wrapper.cache_clear = lambda: (cache_data.clear(), access_times.clear())
            
            return wrapper
        return decorator
    
    @cache(max_size=3, ttl=2.0)
    def expensive_calculation(x, y):
        """昂贵的计算"""
        time.sleep(0.1)  # 模拟耗时计算
        return x ** 2 + y ** 2
    
    print("测试缓存装饰器：")
    
    # 第一次调用
    result1 = expensive_calculation(3, 4)
    print(f"结果1: {result1}")
    
    # 第二次调用（应该使用缓存）
    result2 = expensive_calculation(3, 4)
    print(f"结果2: {result2}")
    
    # 不同参数的调用
    result3 = expensive_calculation(5, 6)
    print(f"结果3: {result3}")
    
    print(f"缓存信息: {expensive_calculation.cache_info()}")
    
    # 等待缓存过期
    print("等待缓存过期...")
    time.sleep(2.1)
    
    # 再次调用（缓存应该过期）
    result4 = expensive_calculation(3, 4)
    print(f"结果4: {result4}")
    
    # 题目3：创建一个权限检查装饰器
    print("\n题目3：创建一个权限检查装饰器")
    print("-" * 30)
    
    def require_permission(permission):
        """权限检查装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if args:
                    # 检查参数中是否有User对象
                    user = None
                    for arg in args:
                        if hasattr(arg, 'permissions'):
                            user = arg
                            break
                    
                    if user is None:
                        raise ValueError("需要用户对象作为参数")
                    
                    if permission in user.permissions:
                        return func(*args, **kwargs)
                    else:
                        raise PermissionError(f"用户缺少权限: {permission}")
                else:
                    raise ValueError("需要用户对象作为参数")
            return wrapper
        return decorator
    
    class User:
        def __init__(self, name, permissions):
            self.name = name
            self.permissions = set(permissions)
        
        def __str__(self):
            return f"User({self.name}, {self.permissions})"
    
    class AdminSystem:
        @require_permission('read')
        def read_data(self, user):
            return f"用户 {user.name} 读取数据成功"
        
        @require_permission('write')
        def write_data(self, user, data):
            return f"用户 {user.name} 写入数据: {data}"
        
        @require_permission('admin')
        def delete_data(self, user, data_id):
            return f"用户 {user.name} 删除数据: {data_id}"
    
    print("测试权限检查装饰器：")
    
    # 创建用户
    normal_user = User("Alice", ['read'])
    power_user = User("Bob", ['read', 'write'])
    admin_user = User("Charlie", ['read', 'write', 'admin'])
    
    system = AdminSystem()
    
    # 测试不同权限
    users = [normal_user, power_user, admin_user]
    operations = [
        ('read_data', lambda s, u: s.read_data(u)),
        ('write_data', lambda s, u: s.write_data(u, "test data")),
        ('delete_data', lambda s, u: s.delete_data(u, "data_123"))
    ]
    
    for user in users:
        print(f"\n测试用户: {user}")
        for op_name, operation in operations:
            try:
                result = operation(system, user)
                print(f"  {op_name}: {result}")
            except PermissionError as e:
                print(f"  {op_name}: 权限不足 - {e}")


def exercise_3_class_decorators():
    """练习3：类装饰器"""
    print("\n" + "=" * 50)
    print("练习3：类装饰器")
    print("=" * 50)
    
    # 题目1：创建一个调用计数器类装饰器
    print("\n题目1：创建一个调用计数器类装饰器")
    print("-" * 30)
    
    class CallCounter:
        """调用计数器装饰器"""
        
        def __init__(self, func):
            self.func = func
            self.count = 0
            functools.update_wrapper(self, func)
        
        def __call__(self, *args, **kwargs):
            self.count += 1
            print(f"[COUNTER] {self.func.__name__} 被调用第 {self.count} 次")
            return self.func(*args, **kwargs)
        
        def get_count(self):
            return self.count
        
        def reset_count(self):
            self.count = 0
    
    @CallCounter
    def say_hello(name):
        return f"Hello, {name}!"
    
    @CallCounter
    def calculate(x, y):
        return x * y
    
    print("测试调用计数器：")
    
    # 多次调用函数
    for i in range(3):
        result = say_hello(f"User{i+1}")
        print(f"  结果: {result}")
    
    print(f"say_hello 总调用次数: {say_hello.get_count()}")
    
    for i in range(2):
        result = calculate(i+1, i+2)
        print(f"  计算结果: {result}")
    
    print(f"calculate 总调用次数: {calculate.get_count()}")
    
    # 重置计数器
    say_hello.reset_count()
    print(f"重置后 say_hello 调用次数: {say_hello.get_count()}")
    
    # 题目2：创建一个单例装饰器
    print("\n题目2：创建一个单例装饰器")
    print("-" * 30)
    
    class Singleton:
        """单例装饰器"""
        
        def __init__(self, cls):
            self.cls = cls
            self.instance = None
            self.lock = threading.Lock()
        
        def __call__(self, *args, **kwargs):
            if self.instance is None:
                with self.lock:
                    if self.instance is None:
                        print(f"[SINGLETON] 创建 {self.cls.__name__} 的新实例")
                        self.instance = self.cls(*args, **kwargs)
                    else:
                        print(f"[SINGLETON] 返回 {self.cls.__name__} 的现有实例")
            else:
                print(f"[SINGLETON] 返回 {self.cls.__name__} 的现有实例")
            return self.instance
        
        def __getattr__(self, name):
            return getattr(self.cls, name)
    
    @Singleton
    class DatabaseConnection:
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
        
        def __str__(self):
            status = "已连接" if self.connected else "未连接"
            return f"DatabaseConnection({self.host}:{self.port}, {status})"
    
    print("测试单例装饰器：")
    
    # 创建多个实例（应该返回同一个对象）
    db1 = DatabaseConnection()
    print(f"db1: {db1}")
    
    db2 = DatabaseConnection("remote_host", 3306)
    print(f"db2: {db2}")
    
    print(f"db1 is db2: {db1 is db2}")
    print(f"id(db1): {id(db1)}, id(db2): {id(db2)}")
    
    # 使用连接
    db1.connect()
    db2.disconnect()  # 实际上操作的是同一个对象
    
    # 题目3：创建一个属性验证装饰器
    print("\n题目3：创建一个属性验证装饰器")
    print("-" * 30)
    
    class ValidatedAttribute:
        """属性验证装饰器"""
        
        def __init__(self, validator, error_message="Invalid value"):
            self.validator = validator
            self.error_message = error_message
        
        def __set_name__(self, owner, name):
            self.name = name
            self.private_name = f'_{name}'
        
        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            return getattr(obj, self.private_name, None)
        
        def __set__(self, obj, value):
            if not self.validator(value):
                raise ValueError(f"{self.error_message}: {value}")
            setattr(obj, self.private_name, value)
    
    # 验证函数
    def positive_number(value):
        return isinstance(value, (int, float)) and value > 0
    
    def valid_email(value):
        return isinstance(value, str) and '@' in value and '.' in value
    
    def age_range(value):
        return isinstance(value, int) and 0 <= value <= 150
    
    class Person:
        # 使用属性验证装饰器
        age = ValidatedAttribute(age_range, "年龄必须在0-150之间")
        email = ValidatedAttribute(valid_email, "邮箱格式不正确")
        salary = ValidatedAttribute(positive_number, "薪资必须是正数")
        
        def __init__(self, name, age, email, salary):
            self.name = name
            self.age = age
            self.email = email
            self.salary = salary
        
        def __str__(self):
            return f"Person(name='{self.name}', age={self.age}, email='{self.email}', salary={self.salary})"
    
    print("测试属性验证装饰器：")
    
    # 创建有效的Person对象
    try:
        person1 = Person("Alice", 25, "alice@example.com", 50000)
        print(f"创建成功: {person1}")
    except ValueError as e:
        print(f"创建失败: {e}")
    
    # 测试无效值
    invalid_cases = [
        ("Bob", -5, "bob@example.com", 60000),  # 无效年龄
        ("Charlie", 30, "invalid-email", 70000),  # 无效邮箱
        ("David", 35, "david@example.com", -1000),  # 无效薪资
    ]
    
    for name, age, email, salary in invalid_cases:
        try:
            person = Person(name, age, email, salary)
            print(f"创建成功: {person}")
        except ValueError as e:
            print(f"创建失败 ({name}): {e}")


def exercise_4_decorator_chains():
    """练习4：装饰器链"""
    print("\n" + "=" * 50)
    print("练习4：装饰器链")
    print("=" * 50)
    
    # 题目1：创建多个装饰器并组合使用
    print("\n题目1：创建多个装饰器并组合使用")
    print("-" * 30)
    
    def debug_info(func):
        """调试信息装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[DEBUG] 函数: {func.__name__}")
            print(f"[DEBUG] 参数: args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"[DEBUG] 返回: {result}")
            return result
        return wrapper
    
    def validate_positive(func):
        """验证参数为正数的装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if isinstance(arg, (int, float)) and arg <= 0:
                    raise ValueError(f"参数必须为正数: {arg}")
            for value in kwargs.values():
                if isinstance(value, (int, float)) and value <= 0:
                    raise ValueError(f"参数必须为正数: {value}")
            return func(*args, **kwargs)
        return wrapper
    
    def convert_to_int(func):
        """将浮点数参数转换为整数的装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            new_args = []
            for arg in args:
                if isinstance(arg, float):
                    print(f"[CONVERT] 转换 {arg} -> {int(arg)}")
                    new_args.append(int(arg))
                else:
                    new_args.append(arg)
            
            new_kwargs = {}
            for key, value in kwargs.items():
                if isinstance(value, float):
                    print(f"[CONVERT] 转换 {key}={value} -> {int(value)}")
                    new_kwargs[key] = int(value)
                else:
                    new_kwargs[key] = value
            
            return func(*new_args, **new_kwargs)
        return wrapper
    
    # 组合使用装饰器（注意顺序）
    @debug_info
    @validate_positive
    @convert_to_int
    def calculate_power(base, exponent):
        """计算幂运算"""
        return base ** exponent
    
    print("测试装饰器链：")
    
    # 正常情况
    try:
        result1 = calculate_power(2.7, 3.2)
        print(f"结果1: {result1}\n")
    except Exception as e:
        print(f"错误1: {e}\n")
    
    # 负数参数（应该被验证装饰器拦截）
    try:
        result2 = calculate_power(-2, 3)
        print(f"结果2: {result2}\n")
    except Exception as e:
        print(f"错误2: {e}\n")
    
    # 题目2：创建可配置的装饰器链
    print("\n题目2：创建可配置的装饰器链")
    print("-" * 30)
    
    def create_decorator_chain(*decorators):
        """创建装饰器链的工厂函数"""
        def chain_decorator(func):
            for decorator in reversed(decorators):
                func = decorator(func)
            return func
        return chain_decorator
    
    def log_level(level):
        """可配置日志级别的装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(f"[{level}] 执行 {func.__name__}")
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    def measure_memory(func):
        """内存使用测量装饰器（模拟）"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import sys
            before = sys.getsizeof(args) + sys.getsizeof(kwargs)
            result = func(*args, **kwargs)
            after = sys.getsizeof(result)
            print(f"[MEMORY] {func.__name__} 内存使用: 输入 {before} bytes, 输出 {after} bytes")
            return result
        return wrapper
    
    def timing(func):
        """计时装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time
            print(f"[TIMING] {func.__name__} 执行时间: {duration:.4f}秒")
            return result
        return wrapper
    
    def handle_exceptions(func):
        """异常处理装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"[ERROR] {func.__name__} 发生异常: {type(e).__name__}: {e}")
                return None
        return wrapper
    
    # 创建不同的装饰器链
    basic_chain = create_decorator_chain(
        log_level("INFO"),
        timing
    )
    
    advanced_chain = create_decorator_chain(
        log_level("DEBUG"),
        measure_memory,
        timing,
        handle_exceptions
    )
    
    @basic_chain
    def simple_function(x):
        return x * 2
    
    @advanced_chain
    def complex_function(data):
        # 模拟复杂处理
        result = []
        for item in data:
            result.append(item ** 2)
        return result
    
    print("测试可配置装饰器链：")
    
    print("基础链测试：")
    result1 = simple_function(5)
    print(f"简单函数结果: {result1}\n")
    
    print("高级链测试：")
    result2 = complex_function([1, 2, 3, 4, 5])
    print(f"复杂函数结果: {result2}\n")


def exercise_5_practical_applications():
    """练习5：实际应用场景"""
    print("\n" + "=" * 50)
    print("练习5：实际应用场景")
    print("=" * 50)
    
    # 题目1：Web API 装饰器
    print("\n题目1：Web API 装饰器")
    print("-" * 30)
    
    def api_endpoint(method="GET", auth_required=True):
        """API端点装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(f"[API] {method} /{func.__name__}")
                
                # 模拟认证检查
                if auth_required:
                    # 假设第一个参数包含认证信息
                    if not args or not hasattr(args[0], 'authenticated'):
                        return {"error": "Authentication required", "status": 401}
                    if not args[0].authenticated:
                        return {"error": "Invalid credentials", "status": 403}
                
                try:
                    result = func(*args, **kwargs)
                    return {"data": result, "status": 200}
                except Exception as e:
                    return {"error": str(e), "status": 500}
            
            # 添加元数据
            wrapper.method = method
            wrapper.auth_required = auth_required
            wrapper.endpoint = f"/{func.__name__}"
            
            return wrapper
        return decorator
    
    def rate_limit(max_calls=10, window=60):
        """速率限制装饰器"""
        call_history = defaultdict(list)
        
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 假设第一个参数包含客户端ID
                client_id = getattr(args[0], 'client_id', 'anonymous') if args else 'anonymous'
                current_time = time.time()
                
                # 清理过期的调用记录
                call_history[client_id] = [
                    call_time for call_time in call_history[client_id]
                    if current_time - call_time < window
                ]
                
                # 检查速率限制
                if len(call_history[client_id]) >= max_calls:
                    return {"error": "Rate limit exceeded", "status": 429}
                
                # 记录当前调用
                call_history[client_id].append(current_time)
                
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    class Request:
        def __init__(self, client_id, authenticated=True):
            self.client_id = client_id
            self.authenticated = authenticated
    
    class UserAPI:
        @api_endpoint("GET", auth_required=True)
        @rate_limit(max_calls=3, window=10)
        def get_user_profile(self, request, user_id):
            return {"user_id": user_id, "name": f"User {user_id}", "email": f"user{user_id}@example.com"}
        
        @api_endpoint("POST", auth_required=True)
        def create_user(self, request, user_data):
            return {"message": "User created", "user_id": 123, "data": user_data}
        
        @api_endpoint("GET", auth_required=False)
        def public_info(self, request):
            return {"message": "This is public information", "timestamp": time.time()}
    
    print("测试Web API装饰器：")
    
    api = UserAPI()
    
    # 认证用户请求
    auth_request = Request("client_1", authenticated=True)
    
    print("认证用户请求：")
    for i in range(5):  # 超过速率限制
        result = api.get_user_profile(auth_request, 456)
        print(f"  请求 {i+1}: {result}")
    
    # 未认证用户请求
    unauth_request = Request("client_2", authenticated=False)
    
    print("\n未认证用户请求：")
    result = api.get_user_profile(unauth_request, 789)
    print(f"  结果: {result}")
    
    # 公开接口请求
    print("\n公开接口请求：")
    result = api.public_info(unauth_request)
    print(f"  结果: {result}")
    
    # 题目2：数据库操作装饰器
    print("\n题目2：数据库操作装饰器")
    print("-" * 30)
    
    def database_transaction(func):
        """数据库事务装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[DB] 开始事务: {func.__name__}")
            try:
                result = func(*args, **kwargs)
                print(f"[DB] 提交事务: {func.__name__}")
                return result
            except Exception as e:
                print(f"[DB] 回滚事务: {func.__name__} - {e}")
                raise
        return wrapper
    
    def connection_pool(func):
        """连接池装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[POOL] 获取数据库连接")
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                print(f"[POOL] 释放数据库连接")
        return wrapper
    
    def query_cache(ttl=300):
        """查询缓存装饰器"""
        cache = {}
        
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 创建缓存键
                cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
                current_time = time.time()
                
                # 检查缓存
                if cache_key in cache:
                    cached_result, cached_time = cache[cache_key]
                    if current_time - cached_time < ttl:
                        print(f"[CACHE] 查询缓存命中: {func.__name__}")
                        return cached_result
                    else:
                        del cache[cache_key]
                
                # 执行查询并缓存
                print(f"[CACHE] 执行数据库查询: {func.__name__}")
                result = func(*args, **kwargs)
                cache[cache_key] = (result, current_time)
                return result
            return wrapper
        return decorator
    
    class UserRepository:
        @connection_pool
        @query_cache(ttl=60)
        def get_user_by_id(self, user_id):
            # 模拟数据库查询
            time.sleep(0.1)
            return {"id": user_id, "name": f"User {user_id}", "active": True}
        
        @database_transaction
        @connection_pool
        def create_user(self, user_data):
            # 模拟用户创建
            if user_data.get('name') == 'invalid':
                raise ValueError("Invalid user data")
            return {"id": 123, "created": True, **user_data}
        
        @database_transaction
        @connection_pool
        def update_user(self, user_id, updates):
            # 模拟用户更新
            return {"id": user_id, "updated": True, **updates}
    
    print("测试数据库操作装饰器：")
    
    repo = UserRepository()
    
    # 测试查询缓存
    print("查询缓存测试：")
    user1 = repo.get_user_by_id(1)
    print(f"  第一次查询: {user1}")
    
    user2 = repo.get_user_by_id(1)  # 应该使用缓存
    print(f"  第二次查询: {user2}")
    
    # 测试事务成功
    print("\n事务成功测试：")
    try:
        new_user = repo.create_user({"name": "Alice", "email": "alice@example.com"})
        print(f"  创建用户: {new_user}")
    except Exception as e:
        print(f"  创建失败: {e}")
    
    # 测试事务失败
    print("\n事务失败测试：")
    try:
        invalid_user = repo.create_user({"name": "invalid"})
        print(f"  创建用户: {invalid_user}")
    except Exception as e:
        print(f"  创建失败: {e}")


def exercise_6_advanced_decorators():
    """练习6：高级装饰器技巧"""
    print("\n" + "=" * 50)
    print("练习6：高级装饰器技巧")
    print("=" * 50)
    
    # 定义所需的装饰器
    def timing(func):
        """计时装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time
            print(f"[TIMING] {func.__name__} 执行时间: {duration:.4f}秒")
            return result
        return wrapper
    
    def debug_info(func):
        """调试信息装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[DEBUG] 调用 {func.__name__} 参数: {args}, {kwargs}")
            result = func(*args, **kwargs)
            print(f"[DEBUG] {func.__name__} 返回: {result}")
            return result
        return wrapper
    
    def handle_exceptions(func):
        """异常处理装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"[ERROR] {func.__name__} 发生异常: {type(e).__name__}: {e}")
                return None
        return wrapper
    
    # 题目1：元装饰器（装饰器的装饰器）
    print("\n题目1：元装饰器（装饰器的装饰器）")
    print("-" * 30)
    
    def decorator_with_logging(decorator_name):
        """为装饰器添加日志的元装饰器"""
        def meta_decorator(decorator_func):
            @functools.wraps(decorator_func)
            def wrapper(*args, **kwargs):
                print(f"[META] 应用装饰器: {decorator_name}")
                result = decorator_func(*args, **kwargs)
                print(f"[META] 装饰器 {decorator_name} 应用完成")
                return result
            return wrapper
        return meta_decorator
    
    @decorator_with_logging("timing_decorator")
    def advanced_timing(func):
        """高级计时装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            duration = end_time - start_time
            print(f"[TIMING] {func.__name__} 执行时间: {duration:.6f}秒")
            return result
        return wrapper
    
    @decorator_with_logging("validation_decorator")
    def type_validator(*expected_types):
        """类型验证装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 验证位置参数类型
                for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                    if not isinstance(arg, expected_type):
                        raise TypeError(f"参数 {i+1} 期望类型 {expected_type.__name__}, 得到 {type(arg).__name__}")
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    @advanced_timing
    @type_validator(int, int)
    def multiply_numbers(a, b):
        """乘法函数"""
        time.sleep(0.01)  # 模拟计算时间
        return a * b
    
    print("测试元装饰器：")
    
    # 正确类型
    try:
        result1 = multiply_numbers(5, 3)
        print(f"5 * 3 = {result1}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 错误类型
    try:
        result2 = multiply_numbers(5.0, 3)
        print(f"5.0 * 3 = {result2}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 题目2：条件装饰器
    print("\n题目2：条件装饰器")
    print("-" * 30)
    
    def conditional_decorator(condition):
        """条件装饰器 - 只在满足条件时应用装饰器"""
        def decorator_factory(decorator):
            def conditional_wrapper(func):
                if condition():
                    print(f"[CONDITIONAL] 条件满足，应用装饰器到 {func.__name__}")
                    return decorator(func)
                else:
                    print(f"[CONDITIONAL] 条件不满足，跳过装饰器 {func.__name__}")
                    return func
            return conditional_wrapper
        return decorator_factory
    
    # 环境变量模拟
    DEBUG_MODE = True
    PROFILING_ENABLED = False
    
    def is_debug_mode():
        return DEBUG_MODE
    
    def is_profiling_enabled():
        return PROFILING_ENABLED
    
    @conditional_decorator(is_debug_mode)
    def debug_logger(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[DEBUG] 调用 {func.__name__} 参数: {args}, {kwargs}")
            result = func(*args, **kwargs)
            print(f"[DEBUG] {func.__name__} 返回: {result}")
            return result
        return wrapper
    
    @conditional_decorator(is_profiling_enabled)
    def profiler(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[PROFILER] 开始分析 {func.__name__}")
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"[PROFILER] {func.__name__} 分析完成: {end_time - start_time:.4f}秒")
            return result
        return wrapper
    
    @debug_logger  # 会被应用，因为 DEBUG_MODE = True
    @profiler     # 不会被应用，因为 PROFILING_ENABLED = False
    def calculate_fibonacci(n):
        if n <= 1:
            return n
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
    
    print("测试条件装饰器：")
    result = calculate_fibonacci(5)
    print(f"fibonacci(5) = {result}")
    
    # 改变条件
    print("\n改变条件后：")
    PROFILING_ENABLED = True
    
    @debug_logger
    @profiler
    def calculate_factorial(n):
        if n <= 1:
            return 1
        return n * calculate_factorial(n-1)
    
    result = calculate_factorial(5)
    print(f"factorial(5) = {result}")
    
    # 题目3：装饰器注册系统
    print("\n题目3：装饰器注册系统")
    print("-" * 30)
    
    class DecoratorRegistry:
        """装饰器注册系统"""
        
        def __init__(self):
            self.decorators = {}
            self.functions = {}
        
        def register_decorator(self, name, decorator):
            """注册装饰器"""
            self.decorators[name] = decorator
            print(f"[REGISTRY] 注册装饰器: {name}")
        
        def apply_decorators(self, *decorator_names):
            """应用多个已注册的装饰器"""
            def decorator(func):
                print(f"[REGISTRY] 为 {func.__name__} 应用装饰器: {decorator_names}")
                
                # 按顺序应用装饰器
                decorated_func = func
                for name in reversed(decorator_names):
                    if name in self.decorators:
                        decorated_func = self.decorators[name](decorated_func)
                    else:
                        print(f"[REGISTRY] 警告: 装饰器 '{name}' 未注册")
                
                # 注册函数
                self.functions[func.__name__] = {
                    'original': func,
                    'decorated': decorated_func,
                    'decorators': list(decorator_names)
                }
                
                return decorated_func
            return decorator
        
        def get_function_info(self, func_name):
            """获取函数信息"""
            return self.functions.get(func_name, {})
        
        def list_decorators(self):
            """列出所有注册的装饰器"""
            return list(self.decorators.keys())
        
        def list_functions(self):
            """列出所有注册的函数"""
            return list(self.functions.keys())
    
    # 创建注册系统
    registry = DecoratorRegistry()
    
    # 注册一些装饰器
    registry.register_decorator('timer', timing)
    registry.register_decorator('logger', debug_info)
    registry.register_decorator('exception_handler', handle_exceptions)
    
    def custom_cache(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key not in cache:
                cache[key] = func(*args, **kwargs)
                print(f"[CACHE] 缓存 {func.__name__} 结果")
            else:
                print(f"[CACHE] 使用 {func.__name__} 缓存")
            return cache[key]
        return wrapper
    
    registry.register_decorator('cache', custom_cache)
    
    print(f"已注册的装饰器: {registry.list_decorators()}")
    
    # 使用注册系统
    @registry.apply_decorators('timer', 'logger', 'cache')
    def expensive_operation(x, y):
        """昂贵的操作"""
        time.sleep(0.1)
        return x ** y
    
    @registry.apply_decorators('exception_handler', 'timer')
    def risky_operation(x):
        """有风险的操作"""
        if x < 0:
            raise ValueError("x 不能为负数")
        return x ** 0.5
    
    print("\n测试装饰器注册系统：")
    
    # 测试昂贵操作
    print("昂贵操作测试：")
    result1 = expensive_operation(2, 3)
    print(f"第一次调用结果: {result1}")
    
    result2 = expensive_operation(2, 3)  # 应该使用缓存
    print(f"第二次调用结果: {result2}")
    
    # 测试有风险操作
    print("\n有风险操作测试：")
    result3 = risky_operation(9)
    print(f"正常情况结果: {result3}")
    
    result4 = risky_operation(-1)  # 应该被异常处理器捕获
    print(f"异常情况结果: {result4}")
    
    # 查看函数信息
    print(f"\n已注册的函数: {registry.list_functions()}")
    
    expensive_info = registry.get_function_info('expensive_operation')
    print(f"expensive_operation 信息: {expensive_info['decorators']}")


def exercise_7_performance_optimization():
    """练习7：性能优化"""
    print("\n" + "=" * 50)
    print("练习7：性能优化")
    print("=" * 50)
    
    # 题目1：智能缓存装饰器
    print("\n题目1：智能缓存装饰器")
    print("-" * 30)
    
    class SmartCache:
        """智能缓存装饰器"""
        
        def __init__(self, max_size=128, ttl=None, strategy='lru'):
            self.max_size = max_size
            self.ttl = ttl
            self.strategy = strategy
            self.cache = {}
            self.access_times = {}
            self.access_counts = Counter()
            self.hits = 0
            self.misses = 0
        
        def __call__(self, func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                key = self._make_key(args, kwargs)
                current_time = time.time()
                
                # 检查缓存
                if key in self.cache:
                    # 检查TTL
                    if self.ttl is None or (current_time - self.access_times[key]) < self.ttl:
                        self.hits += 1
                        self.access_counts[key] += 1
                        self.access_times[key] = current_time
                        print(f"[SMART_CACHE] 缓存命中: {func.__name__}")
                        return self.cache[key]
                    else:
                        # 缓存过期
                        self._remove_key(key)
                
                # 缓存未命中
                self.misses += 1
                print(f"[SMART_CACHE] 缓存未命中，执行函数: {func.__name__}")
                result = func(*args, **kwargs)
                
                # 添加到缓存
                self._add_to_cache(key, result, current_time)
                
                return result
            
            # 添加缓存管理方法
            wrapper.cache_info = self.cache_info
            wrapper.cache_clear = self.cache_clear
            wrapper.cache_stats = self.cache_stats
            
            return wrapper
        
        def _make_key(self, args, kwargs):
            """创建缓存键"""
            return hashlib.md5(str((args, tuple(sorted(kwargs.items())))).encode()).hexdigest()
        
        def _add_to_cache(self, key, value, timestamp):
            """添加到缓存"""
            # 如果缓存已满，根据策略删除条目
            if len(self.cache) >= self.max_size:
                self._evict_cache()
            
            self.cache[key] = value
            self.access_times[key] = timestamp
            self.access_counts[key] = 1
        
        def _evict_cache(self):
            """根据策略清理缓存"""
            if self.strategy == 'lru':  # Least Recently Used
                oldest_key = min(self.access_times.keys(), key=lambda k: self.access_times[k])
                self._remove_key(oldest_key)
            elif self.strategy == 'lfu':  # Least Frequently Used
                least_used_key = min(self.access_counts.keys(), key=lambda k: self.access_counts[k])
                self._remove_key(least_used_key)
            elif self.strategy == 'fifo':  # First In First Out
                # 简化实现：删除第一个键
                first_key = next(iter(self.cache))
                self._remove_key(first_key)
        
        def _remove_key(self, key):
            """删除缓存键"""
            if key in self.cache:
                del self.cache[key]
                del self.access_times[key]
                del self.access_counts[key]
        
        def cache_info(self):
            """缓存信息"""
            hit_rate = self.hits / (self.hits + self.misses) if (self.hits + self.misses) > 0 else 0
            return {
                'hits': self.hits,
                'misses': self.misses,
                'hit_rate': f'{hit_rate:.2%}',
                'cache_size': len(self.cache),
                'max_size': self.max_size,
                'strategy': self.strategy
            }
        
        def cache_clear(self):
            """清空缓存"""
            self.cache.clear()
            self.access_times.clear()
            self.access_counts.clear()
            self.hits = 0
            self.misses = 0
        
        def cache_stats(self):
            """详细统计"""
            return {
                'cache_keys': list(self.cache.keys()),
                'access_counts': dict(self.access_counts),
                'access_times': {k: time.ctime(v) for k, v in self.access_times.items()}
            }
    
    # 测试不同缓存策略
    @SmartCache(max_size=3, strategy='lru')
    def fibonacci_lru(n):
        if n <= 1:
            return n
        return fibonacci_lru(n-1) + fibonacci_lru(n-2)
    
    @SmartCache(max_size=3, ttl=2.0, strategy='lfu')
    def expensive_calc(x, y):
        time.sleep(0.05)
        return x ** 2 + y ** 2
    
    print("测试智能缓存装饰器：")
    
    # 测试LRU缓存
    print("LRU缓存测试：")
    for i in range(8):
        result = fibonacci_lru(i)
        print(f"  fibonacci({i}) = {result}")
    
    print(f"LRU缓存信息: {fibonacci_lru.cache_info()}")
    
    # 测试LFU缓存
    print("\nLFU缓存测试：")
    test_cases = [(1, 2), (2, 3), (1, 2), (3, 4), (1, 2), (2, 3)]
    for x, y in test_cases:
        result = expensive_calc(x, y)
        print(f"  calc({x}, {y}) = {result}")
    
    print(f"LFU缓存信息: {expensive_calc.cache_info()}")
    
    # 题目2：异步装饰器（模拟）
    print("\n题目2：异步装饰器（模拟）")
    print("-" * 30)
    
    def async_executor(max_workers=3):
        """异步执行装饰器（模拟）"""
        import concurrent.futures
        
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 检查是否需要异步执行
                if kwargs.pop('async_exec', False):
                    print(f"[ASYNC] 异步执行 {func.__name__}")
                    
                    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                        future = executor.submit(func, *args, **kwargs)
                        return future.result()
                else:
                    print(f"[ASYNC] 同步执行 {func.__name__}")
                    return func(*args, **kwargs)
            return wrapper
        return decorator
    
    @async_executor(max_workers=2)
    def cpu_intensive_task(n, task_name):
        """CPU密集型任务"""
        print(f"[TASK] 开始执行 {task_name}")
        total = 0
        for i in range(n):
            total += i ** 2
        print(f"[TASK] 完成执行 {task_name}")
        return total
    
    print("测试异步装饰器：")
    
    # 同步执行
    start_time = time.time()
    result1 = cpu_intensive_task(100000, "任务1")
    result2 = cpu_intensive_task(100000, "任务2")
    sync_time = time.time() - start_time
    print(f"同步执行时间: {sync_time:.4f}秒")
    
    # 异步执行（模拟）
    start_time = time.time()
    result3 = cpu_intensive_task(100000, "任务3", async_exec=True)
    result4 = cpu_intensive_task(100000, "任务4", async_exec=True)
    async_time = time.time() - start_time
    print(f"异步执行时间: {async_time:.4f}秒")


def exercise_8_comprehensive_project():
    """练习8：综合项目练习"""
    print("\n" + "=" * 50)
    print("练习8：综合项目练习")
    print("=" * 50)
    
    # 综合项目：构建一个完整的装饰器系统
    print("\n综合项目：用户管理系统")
    print("-" * 30)
    
    # 权限系统
    class Permission:
        READ = "read"
        WRITE = "write"
        DELETE = "delete"
        ADMIN = "admin"
    
    class User:
        def __init__(self, username, permissions=None, role="user"):
            self.username = username
            self.permissions = set(permissions or [])
            self.role = role
            self.login_time = time.time()
        
        def has_permission(self, permission):
            return permission in self.permissions or Permission.ADMIN in self.permissions
        
        def __str__(self):
            return f"User({self.username}, {self.role}, {self.permissions})"
    
    # 装饰器组合
    def require_auth(func):
        """认证装饰器"""
        @functools.wraps(func)
        def wrapper(self, user, *args, **kwargs):
            if not isinstance(user, User):
                raise ValueError("需要有效的用户对象")
            return func(self, user, *args, **kwargs)
        return wrapper
    
    def require_permission(permission):
        """权限检查装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(self, user, *args, **kwargs):
                if not user.has_permission(permission):
                    raise PermissionError(f"用户 {user.username} 缺少权限: {permission}")
                return func(self, user, *args, **kwargs)
            return wrapper
        return decorator
    
    def audit_log(action):
        """审计日志装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(self, user, *args, **kwargs):
                start_time = time.time()
                try:
                    result = func(self, user, *args, **kwargs)
                    end_time = time.time()
                    print(f"[AUDIT] {user.username} 执行 {action} 成功 - 耗时: {end_time - start_time:.4f}秒")
                    return result
                except Exception as e:
                    end_time = time.time()
                    print(f"[AUDIT] {user.username} 执行 {action} 失败: {e} - 耗时: {end_time - start_time:.4f}秒")
                    raise
            return wrapper
        return decorator
    
    def rate_limit_user(max_calls=5, window=60):
        """用户级别的速率限制"""
        user_calls = defaultdict(list)
        
        def decorator(func):
            @functools.wraps(func)
            def wrapper(self, user, *args, **kwargs):
                current_time = time.time()
                username = user.username
                
                # 清理过期记录
                user_calls[username] = [
                    call_time for call_time in user_calls[username]
                    if current_time - call_time < window
                ]
                
                # 检查速率限制
                if len(user_calls[username]) >= max_calls:
                    raise Exception(f"用户 {username} 超过速率限制")
                
                # 记录调用
                user_calls[username].append(current_time)
                
                return func(self, user, *args, **kwargs)
            return wrapper
        return decorator
    
    def cache_result(ttl=300):
        """结果缓存装饰器"""
        cache = {}
        
        def decorator(func):
            @functools.wraps(func)
            def wrapper(self, user, *args, **kwargs):
                # 创建缓存键
                cache_key = f"{func.__name__}:{user.username}:{str(args)}:{str(kwargs)}"
                current_time = time.time()
                
                # 检查缓存
                if cache_key in cache:
                    result, cached_time = cache[cache_key]
                    if current_time - cached_time < ttl:
                        print(f"[CACHE] 返回缓存结果: {func.__name__}")
                        return result
                    else:
                        del cache[cache_key]
                
                # 执行函数并缓存
                result = func(self, user, *args, **kwargs)
                cache[cache_key] = (result, current_time)
                return result
            return wrapper
        return decorator
    
    # 用户管理系统
    class UserManagementSystem:
        def __init__(self):
            self.users_db = {}
            self.next_user_id = 1
        
        @require_auth
        @require_permission(Permission.READ)
        @audit_log("查看用户信息")
        @rate_limit_user(max_calls=10, window=60)
        @cache_result(ttl=30)
        def get_user_info(self, user, target_username):
            """获取用户信息"""
            time.sleep(0.1)  # 模拟数据库查询
            if target_username in self.users_db:
                target_user = self.users_db[target_username]
                return {
                    "username": target_user.username,
                    "role": target_user.role,
                    "permissions": list(target_user.permissions),
                    "login_time": time.ctime(target_user.login_time)
                }
            else:
                raise ValueError(f"用户 {target_username} 不存在")
        
        @require_auth
        @require_permission(Permission.WRITE)
        @audit_log("创建用户")
        @rate_limit_user(max_calls=3, window=60)
        def create_user(self, user, username, permissions=None, role="user"):
            """创建用户"""
            if username in self.users_db:
                raise ValueError(f"用户 {username} 已存在")
            
            new_user = User(username, permissions, role)
            self.users_db[username] = new_user
            
            return {
                "message": f"用户 {username} 创建成功",
                "user_id": self.next_user_id,
                "username": username
            }
        
        @require_auth
        @require_permission(Permission.DELETE)
        @audit_log("删除用户")
        @rate_limit_user(max_calls=2, window=60)
        def delete_user(self, user, target_username):
            """删除用户"""
            if target_username not in self.users_db:
                raise ValueError(f"用户 {target_username} 不存在")
            
            if target_username == user.username:
                raise ValueError("不能删除自己")
            
            del self.users_db[target_username]
            return {"message": f"用户 {target_username} 删除成功"}
        
        @require_auth
        @require_permission(Permission.ADMIN)
        @audit_log("获取系统统计")
        def get_system_stats(self, user):
            """获取系统统计信息"""
            return {
                "total_users": len(self.users_db),
                "users_by_role": {
                    role: len([u for u in self.users_db.values() if u.role == role])
                    for role in set(u.role for u in self.users_db.values())
                },
                "admin_user": user.username,
                "timestamp": time.ctime()
            }
    
    print("测试综合项目：")
    
    # 创建系统和用户
    system = UserManagementSystem()
    
    # 创建不同权限的用户
    admin_user = User("admin", [Permission.ADMIN], "admin")
    normal_user = User("alice", [Permission.READ], "user")
    power_user = User("bob", [Permission.READ, Permission.WRITE], "moderator")
    
    # 添加用户到系统
    system.users_db["admin"] = admin_user
    system.users_db["alice"] = normal_user
    system.users_db["bob"] = power_user
    
    print("\n1. 管理员操作测试：")
    try:
        # 管理员创建用户
        result = system.create_user(admin_user, "charlie", [Permission.READ], "user")
        print(f"  创建用户: {result}")
        
        # 管理员查看系统统计
        stats = system.get_system_stats(admin_user)
        print(f"  系统统计: {stats}")
        
    except Exception as e:
        print(f"  管理员操作失败: {e}")
    
    print("\n2. 普通用户操作测试：")
    try:
        # 普通用户查看信息（有权限）
        info = system.get_user_info(normal_user, "bob")
        print(f"  查看用户信息: {info}")
        
        # 普通用户尝试创建用户（无权限）
        system.create_user(normal_user, "david")
        
    except Exception as e:
        print(f"  普通用户操作失败: {e}")
    
    print("\n3. 缓存测试：")
    try:
        # 第一次查询
        info1 = system.get_user_info(normal_user, "bob")
        print(f"  第一次查询: 获取到信息")
        
        # 第二次查询（应该使用缓存）
        info2 = system.get_user_info(normal_user, "bob")
        print(f"  第二次查询: 获取到信息")
        
    except Exception as e:
        print(f"  缓存测试失败: {e}")
    
    print("\n4. 速率限制测试：")
    try:
        # 快速连续调用
        for i in range(12):
            try:
                info = system.get_user_info(normal_user, "bob")
                print(f"  调用 {i+1}: 成功")
            except Exception as e:
                print(f"  调用 {i+1}: 失败 - {e}")
                break
                
    except Exception as e:
        print(f"  速率限制测试失败: {e}")
    
    print("\n综合项目演示完成！")
    print("这个项目展示了如何组合使用多个装饰器来构建一个完整的系统：")
    print("- 认证和授权")
    print("- 审计日志")
    print("- 速率限制")
    print("- 结果缓存")
    print("- 错误处理")


if __name__ == "__main__":
    main()