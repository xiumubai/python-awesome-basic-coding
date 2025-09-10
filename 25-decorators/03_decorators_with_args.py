#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
带参数的装饰器

带参数的装饰器是装饰器的高级用法，它们允许我们在应用装饰器时传递参数，
从而创建更加灵活和可配置的装饰器。这种装饰器实际上是装饰器工厂函数。

学习要点：
1. 理解装饰器工厂函数的概念
2. 掌握带参数装饰器的实现方式
3. 学会创建可配置的装饰器
4. 了解装饰器参数的传递机制
5. 掌握常见的参数化装饰器模式
"""

import time
import functools
from datetime import datetime
import threading


def main():
    """主函数，演示带参数的装饰器"""
    print("=" * 50)
    print("带参数的装饰器")
    print("=" * 50)
    
    # 1. 装饰器工厂函数的基本概念
    print("\n1. 装饰器工厂函数的基本概念")
    print("-" * 30)
    
    def repeat(times):
        """重复执行装饰器工厂函数"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                results = []
                for i in range(times):
                    print(f"第 {i+1} 次执行:")
                    result = func(*args, **kwargs)
                    results.append(result)
                return results
            return wrapper
        return decorator
    
    @repeat(times=3)
    def say_hello(name):
        """问候函数"""
        message = f"Hello, {name}!"
        print(message)
        return message
    
    print("调用重复执行装饰器：")
    results = say_hello("Alice")
    print(f"所有结果: {results}")
    
    # 2. 带默认参数的装饰器
    print("\n2. 带默认参数的装饰器")
    print("-" * 30)
    
    def timeout(seconds=5):
        """超时装饰器工厂函数"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(f"设置超时时间: {seconds}秒")
                start_time = time.time()
                
                try:
                    result = func(*args, **kwargs)
                    elapsed = time.time() - start_time
                    
                    if elapsed > seconds:
                        print(f"警告: 函数执行时间 {elapsed:.2f}秒 超过了设定的 {seconds}秒")
                    else:
                        print(f"函数在 {elapsed:.2f}秒 内完成执行")
                    
                    return result
                except Exception as e:
                    print(f"函数执行异常: {e}")
                    raise
            return wrapper
        return decorator
    
    @timeout()  # 使用默认参数
    def quick_task():
        """快速任务"""
        time.sleep(0.1)
        return "快速任务完成"
    
    @timeout(seconds=2)  # 指定参数
    def slow_task():
        """慢任务"""
        time.sleep(0.5)
        return "慢任务完成"
    
    print("调用带默认参数的装饰器：")
    result1 = quick_task()
    print(f"结果1: {result1}")
    
    result2 = slow_task()
    print(f"结果2: {result2}")
    
    # 3. 多参数装饰器
    print("\n3. 多参数装饰器")
    print("-" * 30)
    
    def log_calls(log_args=True, log_result=True, log_time=False):
        """多参数日志装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{timestamp}] 调用函数: {func.__name__}")
                
                if log_args:
                    print(f"[{timestamp}] 参数: args={args}, kwargs={kwargs}")
                
                start_time = time.time() if log_time else None
                
                try:
                    result = func(*args, **kwargs)
                    
                    if log_time:
                        elapsed = time.time() - start_time
                        print(f"[{timestamp}] 执行时间: {elapsed:.4f}秒")
                    
                    if log_result:
                        print(f"[{timestamp}] 返回值: {result}")
                    
                    return result
                except Exception as e:
                    print(f"[{timestamp}] 异常: {e}")
                    raise
            return wrapper
        return decorator
    
    @log_calls(log_args=True, log_result=True, log_time=True)
    def calculate(x, y, operation="add"):
        """计算函数"""
        if operation == "add":
            return x + y
        elif operation == "multiply":
            return x * y
        else:
            raise ValueError(f"不支持的操作: {operation}")
    
    print("调用多参数装饰器：")
    result = calculate(5, 3, operation="multiply")
    print(f"计算结果: {result}")
    
    # 4. 条件装饰器
    print("\n4. 条件装饰器")
    print("-" * 30)
    
    def conditional_cache(condition=True, max_size=100):
        """条件缓存装饰器"""
        def decorator(func):
            cache = {}
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if not condition:
                    # 如果条件为False，直接执行函数，不使用缓存
                    print(f"缓存已禁用，直接执行 {func.__name__}")
                    return func(*args, **kwargs)
                
                # 创建缓存键
                key = str(args) + str(sorted(kwargs.items()))
                
                if key in cache:
                    print(f"缓存命中: {func.__name__}{args}")
                    return cache[key]
                
                print(f"缓存未命中，计算中: {func.__name__}{args}")
                result = func(*args, **kwargs)
                
                # 检查缓存大小限制
                if len(cache) >= max_size:
                    # 简单的LRU：删除第一个元素
                    oldest_key = next(iter(cache))
                    del cache[oldest_key]
                    print(f"缓存已满，删除最旧的条目")
                
                cache[key] = result
                print(f"结果已缓存，当前缓存大小: {len(cache)}")
                return result
            
            # 添加缓存管理方法
            wrapper.clear_cache = lambda: cache.clear()
            wrapper.cache_size = lambda: len(cache)
            
            return wrapper
        return decorator
    
    @conditional_cache(condition=True, max_size=3)
    def expensive_calculation(n):
        """昂贵的计算"""
        time.sleep(0.1)  # 模拟耗时计算
        return n ** 2
    
    print("调用条件装饰器（缓存启用）：")
    print(f"计算 5^2 = {expensive_calculation(5)}")
    print(f"计算 5^2 = {expensive_calculation(5)}")  # 应该使用缓存
    print(f"计算 3^2 = {expensive_calculation(3)}")
    print(f"计算 4^2 = {expensive_calculation(4)}")
    print(f"计算 6^2 = {expensive_calculation(6)}")
    print(f"缓存大小: {expensive_calculation.cache_size()}")
    
    # 5. 装饰器参数验证
    print("\n5. 装饰器参数验证")
    print("-" * 30)
    
    def validate_types(**expected_types):
        """类型验证装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 获取函数的参数名
                import inspect
                sig = inspect.signature(func)
                bound_args = sig.bind(*args, **kwargs)
                bound_args.apply_defaults()
                
                # 验证参数类型
                for param_name, expected_type in expected_types.items():
                    if param_name in bound_args.arguments:
                        value = bound_args.arguments[param_name]
                        if not isinstance(value, expected_type):
                            raise TypeError(
                                f"参数 '{param_name}' 期望类型 {expected_type.__name__}, "
                                f"但得到 {type(value).__name__}"
                            )
                        print(f"参数 '{param_name}' 类型验证通过: {type(value).__name__}")
                
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    @validate_types(name=str, age=int, salary=float)
    def create_employee(name, age, salary=0.0):
        """创建员工信息"""
        return {
            "name": name,
            "age": age,
            "salary": salary
        }
    
    print("调用类型验证装饰器：")
    try:
        employee = create_employee("Alice", 30, 50000.0)
        print(f"员工信息: {employee}")
    except TypeError as e:
        print(f"类型错误: {e}")
    
    # 6. 装饰器链与参数传递
    print("\n6. 装饰器链与参数传递")
    print("-" * 30)
    
    def rate_limit(calls_per_second=1):
        """限流装饰器"""
        def decorator(func):
            last_called = [0.0]  # 使用列表来存储可变值
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                now = time.time()
                time_since_last = now - last_called[0]
                min_interval = 1.0 / calls_per_second
                
                if time_since_last < min_interval:
                    sleep_time = min_interval - time_since_last
                    print(f"限流中，等待 {sleep_time:.2f} 秒...")
                    time.sleep(sleep_time)
                
                last_called[0] = time.time()
                print(f"执行 {func.__name__} (限制: {calls_per_second} 次/秒)")
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    def debug(enabled=True):
        """调试装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if enabled:
                    print(f"[DEBUG] 进入函数: {func.__name__}")
                    print(f"[DEBUG] 参数: args={args}, kwargs={kwargs}")
                
                result = func(*args, **kwargs)
                
                if enabled:
                    print(f"[DEBUG] 退出函数: {func.__name__}")
                    print(f"[DEBUG] 返回值: {result}")
                
                return result
            return wrapper
        return decorator
    
    @debug(enabled=True)
    @rate_limit(calls_per_second=2)
    @timeout(seconds=3)
    def api_call(endpoint, data=None):
        """模拟API调用"""
        print(f"调用API: {endpoint}")
        if data:
            print(f"发送数据: {data}")
        time.sleep(0.1)  # 模拟网络延迟
        return f"响应来自 {endpoint}"
    
    print("调用装饰器链：")
    result1 = api_call("/users", {"name": "Alice"})
    print(f"结果1: {result1}\n")
    
    result2 = api_call("/posts")
    print(f"结果2: {result2}")
    
    # 7. 动态参数装饰器
    print("\n7. 动态参数装饰器")
    print("-" * 30)
    
    def flexible_retry(max_attempts=3, delay=1, backoff_factor=1, exceptions=(Exception,)):
        """灵活的重试装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                current_delay = delay
                
                for attempt in range(max_attempts):
                    try:
                        print(f"尝试 {attempt + 1}/{max_attempts}: {func.__name__}")
                        result = func(*args, **kwargs)
                        print(f"成功执行 {func.__name__}")
                        return result
                    except exceptions as e:
                        print(f"第 {attempt + 1} 次尝试失败: {e}")
                        
                        if attempt < max_attempts - 1:
                            print(f"等待 {current_delay} 秒后重试...")
                            time.sleep(current_delay)
                            current_delay *= backoff_factor  # 指数退避
                        else:
                            print(f"所有 {max_attempts} 次尝试都失败了")
                            raise
            return wrapper
        return decorator
    
    class NetworkError(Exception):
        pass
    
    attempt_counter = {"count": 0}
    
    @flexible_retry(
        max_attempts=4,
        delay=0.1,
        backoff_factor=2,
        exceptions=(NetworkError, ConnectionError)
    )
    def unreliable_network_call():
        """不可靠的网络调用"""
        attempt_counter["count"] += 1
        if attempt_counter["count"] < 3:
            raise NetworkError(f"网络连接失败 (尝试 {attempt_counter['count']})")
        return "网络调用成功"
    
    print("调用动态参数装饰器：")
    try:
        result = unreliable_network_call()
        print(f"最终结果: {result}")
    except Exception as e:
        print(f"最终失败: {e}")


if __name__ == "__main__":
    main()