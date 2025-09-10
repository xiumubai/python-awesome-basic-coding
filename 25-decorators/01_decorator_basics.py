#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
装饰器基础概念和原理

装饰器是Python中一个强大的特性，它允许我们在不修改原函数代码的情况下，
为函数添加额外的功能。装饰器本质上是一个函数，它接受一个函数作为参数，
并返回一个新的函数。

学习要点：
1. 理解装饰器的本质
2. 掌握装饰器的基本语法
3. 了解装饰器的执行时机
4. 理解闭包在装饰器中的作用
"""

import time
from functools import wraps


def main():
    """主函数，演示装饰器的基础概念"""
    print("=" * 50)
    print("装饰器基础概念和原理")
    print("=" * 50)
    
    # 1. 理解装饰器的本质
    print("\n1. 装饰器的本质")
    print("-" * 30)
    
    # 装饰器本质上是一个高阶函数
    def my_decorator(func):
        """一个简单的装饰器"""
        def wrapper():
            print("在函数执行前做一些事情")
            result = func()
            print("在函数执行后做一些事情")
            return result
        return wrapper
    
    # 原始函数
    def say_hello():
        print("Hello, World!")
        return "greeting"
    
    # 手动应用装饰器
    decorated_func = my_decorator(say_hello)
    print("手动应用装饰器：")
    result = decorated_func()
    print(f"返回值: {result}")
    
    # 2. 使用@语法糖
    print("\n2. 使用@语法糖")
    print("-" * 30)
    
    @my_decorator
    def say_goodbye():
        print("Goodbye, World!")
        return "farewell"
    
    print("使用@语法糖：")
    result = say_goodbye()
    print(f"返回值: {result}")
    
    # 3. 装饰器的执行时机
    print("\n3. 装饰器的执行时机")
    print("-" * 30)
    
    def timing_decorator(func):
        """计时装饰器"""
        print(f"装饰器正在装饰函数: {func.__name__}")
        
        def wrapper(*args, **kwargs):
            print(f"开始执行函数: {func.__name__}")
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"函数 {func.__name__} 执行时间: {end_time - start_time:.4f}秒")
            return result
        return wrapper
    
    @timing_decorator
    def slow_function():
        """一个慢函数"""
        time.sleep(0.1)
        return "任务完成"
    
    print("调用被装饰的函数：")
    result = slow_function()
    print(f"返回值: {result}")
    
    # 4. 闭包在装饰器中的作用
    print("\n4. 闭包在装饰器中的作用")
    print("-" * 30)
    
    def counter_decorator(func):
        """计数装饰器，演示闭包的作用"""
        count = 0  # 这个变量被闭包捕获
        
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            print(f"函数 {func.__name__} 被调用了 {count} 次")
            return func(*args, **kwargs)
        return wrapper
    
    @counter_decorator
    def greet(name):
        return f"Hello, {name}!"
    
    print("多次调用被装饰的函数：")
    print(greet("Alice"))
    print(greet("Bob"))
    print(greet("Charlie"))
    
    # 5. 装饰器的问题：丢失原函数信息
    print("\n5. 装饰器的问题：丢失原函数信息")
    print("-" * 30)
    
    def simple_decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    
    @simple_decorator
    def original_function():
        """这是原始函数的文档字符串"""
        pass
    
    print(f"原函数名: original_function")
    print(f"装饰后函数名: {original_function.__name__}")
    print(f"原函数文档: '这是原始函数的文档字符串'")
    print(f"装饰后函数文档: {original_function.__doc__}")
    
    # 6. 使用functools.wraps解决问题
    print("\n6. 使用functools.wraps解决问题")
    print("-" * 30)
    
    def better_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    
    @better_decorator
    def better_function():
        """这是改进后函数的文档字符串"""
        pass
    
    print(f"原函数名: better_function")
    print(f"装饰后函数名: {better_function.__name__}")
    print(f"原函数文档: '这是改进后函数的文档字符串'")
    print(f"装饰后函数文档: {better_function.__doc__}")
    
    # 7. 装饰器的实际应用示例
    print("\n7. 装饰器的实际应用示例")
    print("-" * 30)
    
    def log_decorator(func):
        """日志装饰器"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG] 调用函数: {func.__name__}")
            print(f"[LOG] 参数: args={args}, kwargs={kwargs}")
            try:
                result = func(*args, **kwargs)
                print(f"[LOG] 返回值: {result}")
                return result
            except Exception as e:
                print(f"[LOG] 异常: {e}")
                raise
        return wrapper
    
    @log_decorator
    def divide(a, b):
        """除法函数"""
        return a / b
    
    print("正常调用：")
    result = divide(10, 2)
    
    print("\n异常调用：")
    try:
        result = divide(10, 0)
    except ZeroDivisionError:
        print("捕获到除零异常")


if __name__ == "__main__":
    main()