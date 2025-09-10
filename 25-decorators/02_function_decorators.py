#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
函数装饰器的定义和使用

函数装饰器是最常见的装饰器类型，它们是接受函数作为参数并返回函数的函数。
本模块将详细介绍如何定义和使用各种类型的函数装饰器。

学习要点：
1. 简单函数装饰器的定义
2. 处理带参数的函数
3. 处理带返回值的函数
4. 装饰器的通用模板
5. 常见的装饰器应用场景
"""

import time
import functools
from datetime import datetime


def main():
    """主函数，演示函数装饰器的定义和使用"""
    print("=" * 50)
    print("函数装饰器的定义和使用")
    print("=" * 50)
    
    # 1. 简单函数装饰器
    print("\n1. 简单函数装饰器")
    print("-" * 30)
    
    def simple_decorator(func):
        """最简单的装饰器"""
        @functools.wraps(func)
        def wrapper():
            print("装饰器开始执行")
            result = func()
            print("装饰器执行结束")
            return result
        return wrapper
    
    @simple_decorator
    def hello():
        """简单的问候函数"""
        print("Hello from decorated function!")
        return "greeting"
    
    print("调用简单装饰器：")
    result = hello()
    print(f"返回值: {result}")
    
    # 2. 处理带参数的函数
    print("\n2. 处理带参数的函数")
    print("-" * 30)
    
    def args_decorator(func):
        """处理带参数函数的装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"函数参数: args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"函数执行完成")
            return result
        return wrapper
    
    @args_decorator
    def greet(name, greeting="Hello"):
        """带参数的问候函数"""
        message = f"{greeting}, {name}!"
        print(message)
        return message
    
    print("调用带参数的装饰器：")
    result1 = greet("Alice")
    result2 = greet("Bob", greeting="Hi")
    print(f"返回值1: {result1}")
    print(f"返回值2: {result2}")
    
    # 3. 计时装饰器
    print("\n3. 计时装饰器")
    print("-" * 30)
    
    def timing_decorator(func):
        """计算函数执行时间的装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            print(f"开始执行 {func.__name__}...")
            
            result = func(*args, **kwargs)
            
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"{func.__name__} 执行时间: {execution_time:.4f}秒")
            return result
        return wrapper
    
    @timing_decorator
    def slow_calculation(n):
        """模拟耗时计算"""
        total = 0
        for i in range(n):
            total += i ** 2
        return total
    
    print("调用计时装饰器：")
    result = slow_calculation(100000)
    print(f"计算结果: {result}")
    
    # 4. 缓存装饰器
    print("\n4. 缓存装饰器")
    print("-" * 30)
    
    def cache_decorator(func):
        """简单的缓存装饰器"""
        cache = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 创建缓存键
            key = str(args) + str(sorted(kwargs.items()))
            
            if key in cache:
                print(f"缓存命中: {func.__name__}{args}")
                return cache[key]
            
            print(f"计算中: {func.__name__}{args}")
            result = func(*args, **kwargs)
            cache[key] = result
            return result
        
        # 添加清除缓存的方法
        wrapper.clear_cache = lambda: cache.clear()
        wrapper.cache_info = lambda: f"缓存大小: {len(cache)}"
        
        return wrapper
    
    @cache_decorator
    def fibonacci(n):
        """计算斐波那契数列"""
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print("调用缓存装饰器：")
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"fibonacci(10) = {fibonacci(10)}")  # 第二次调用会使用缓存
    print(fibonacci.cache_info())
    
    # 5. 重试装饰器
    print("\n5. 重试装饰器")
    print("-" * 30)
    
    def retry_decorator(max_attempts=3, delay=1):
        """重试装饰器工厂函数"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for attempt in range(max_attempts):
                    try:
                        print(f"尝试第 {attempt + 1} 次调用 {func.__name__}")
                        result = func(*args, **kwargs)
                        print(f"{func.__name__} 执行成功")
                        return result
                    except Exception as e:
                        print(f"第 {attempt + 1} 次尝试失败: {e}")
                        if attempt < max_attempts - 1:
                            print(f"等待 {delay} 秒后重试...")
                            time.sleep(delay)
                        else:
                            print(f"所有尝试都失败了")
                            raise
            return wrapper
        return decorator
    
    # 模拟不稳定的函数
    class Counter:
        def __init__(self):
            self.count = 0
    
    counter = Counter()
    
    @retry_decorator(max_attempts=3, delay=0.5)
    def unstable_function():
        """模拟不稳定的函数"""
        counter.count += 1
        if counter.count < 3:
            raise Exception("模拟的网络错误")
        return "成功获取数据"
    
    print("调用重试装饰器：")
    try:
        result = unstable_function()
        print(f"最终结果: {result}")
    except Exception as e:
        print(f"最终失败: {e}")
    
    # 6. 日志装饰器
    print("\n6. 日志装饰器")
    print("-" * 30)
    
    def log_decorator(level="INFO"):
        """日志装饰器工厂函数"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{level}] {timestamp} - 调用函数: {func.__name__}")
                print(f"[{level}] {timestamp} - 参数: args={args}, kwargs={kwargs}")
                
                try:
                    result = func(*args, **kwargs)
                    print(f"[{level}] {timestamp} - 函数执行成功")
                    print(f"[{level}] {timestamp} - 返回值: {result}")
                    return result
                except Exception as e:
                    print(f"[ERROR] {timestamp} - 函数执行失败: {e}")
                    raise
            return wrapper
        return decorator
    
    @log_decorator(level="DEBUG")
    def calculate_area(length, width):
        """计算矩形面积"""
        if length <= 0 or width <= 0:
            raise ValueError("长度和宽度必须大于0")
        return length * width
    
    print("调用日志装饰器：")
    try:
        area = calculate_area(5, 3)
        print(f"\n计算结果: {area}")
    except ValueError as e:
        print(f"计算错误: {e}")
    
    # 7. 权限检查装饰器
    print("\n7. 权限检查装饰器")
    print("-" * 30)
    
    # 模拟用户权限
    current_user = {"name": "Alice", "role": "admin"}
    
    def require_permission(required_role):
        """权限检查装饰器工厂函数"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if current_user.get("role") != required_role:
                    raise PermissionError(f"需要 {required_role} 权限才能执行此操作")
                print(f"权限验证通过: {current_user['name']} ({current_user['role']})")
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    @require_permission("admin")
    def delete_user(username):
        """删除用户（需要管理员权限）"""
        return f"用户 {username} 已被删除"
    
    @require_permission("user")
    def view_profile():
        """查看个人资料（需要用户权限）"""
        return "个人资料信息"
    
    print("调用权限检查装饰器：")
    try:
        result = delete_user("Bob")
        print(f"操作结果: {result}")
    except PermissionError as e:
        print(f"权限错误: {e}")
    
    # 8. 装饰器的通用模板
    print("\n8. 装饰器的通用模板")
    print("-" * 30)
    
    def generic_decorator(func):
        """通用装饰器模板"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 前置处理
            print(f"前置处理: 准备调用 {func.__name__}")
            
            try:
                # 调用原函数
                result = func(*args, **kwargs)
                
                # 后置处理（成功情况）
                print(f"后置处理: {func.__name__} 执行成功")
                return result
                
            except Exception as e:
                # 异常处理
                print(f"异常处理: {func.__name__} 执行失败 - {e}")
                # 可以选择重新抛出异常或返回默认值
                raise
            
            finally:
                # 清理工作
                print(f"清理工作: {func.__name__} 调用结束")
        
        return wrapper
    
    @generic_decorator
    def example_function(x, y):
        """示例函数"""
        return x + y
    
    print("调用通用装饰器模板：")
    result = example_function(3, 4)
    print(f"计算结果: {result}")


if __name__ == "__main__":
    main()