#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
functools.wraps的作用

functools.wraps是Python标准库中的一个重要工具，用于解决装饰器中原函数
元信息丢失的问题。正确使用wraps可以保持函数的原始属性，提高代码的可维护性。

学习要点：
1. 理解装饰器导致的元信息丢失问题
2. 掌握functools.wraps的基本用法
3. 了解wraps保留的函数属性
4. 学会在复杂装饰器中正确使用wraps
5. 掌握自定义wraps的实现原理
"""

import functools
import inspect
from typing import Any, Callable
import time
from datetime import datetime


def main():
    """主函数，演示functools.wraps的作用"""
    print("=" * 50)
    print("functools.wraps的作用")
    print("=" * 50)
    
    # 1. 装饰器导致的元信息丢失问题
    print("\n1. 装饰器导致的元信息丢失问题")
    print("-" * 30)
    
    def simple_decorator_without_wraps(func):
        """不使用wraps的装饰器"""
        def wrapper(*args, **kwargs):
            """包装函数"""
            print(f"调用函数: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    
    def simple_decorator_with_wraps(func):
        """使用wraps的装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """包装函数"""
            print(f"调用函数: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    
    @simple_decorator_without_wraps
    def original_function_without_wraps(x, y):
        """原始函数：计算两个数的和
        
        Args:
            x (int): 第一个数
            y (int): 第二个数
            
        Returns:
            int: 两个数的和
        """
        return x + y
    
    @simple_decorator_with_wraps
    def original_function_with_wraps(x, y):
        """原始函数：计算两个数的和
        
        Args:
            x (int): 第一个数
            y (int): 第二个数
            
        Returns:
            int: 两个数的和
        """
        return x + y
    
    print("不使用wraps的装饰器：")
    print(f"函数名: {original_function_without_wraps.__name__}")
    print(f"文档字符串: {original_function_without_wraps.__doc__}")
    print(f"模块名: {original_function_without_wraps.__module__}")
    
    print("\n使用wraps的装饰器：")
    print(f"函数名: {original_function_with_wraps.__name__}")
    print(f"文档字符串: {original_function_with_wraps.__doc__}")
    print(f"模块名: {original_function_with_wraps.__module__}")
    
    # 2. wraps保留的函数属性详解
    print("\n2. wraps保留的函数属性详解")
    print("-" * 30)
    
    def detailed_function(a: int, b: str = "default", *args, **kwargs) -> str:
        """详细的函数示例
        
        这是一个用于演示函数属性的详细函数。
        
        Args:
            a (int): 整数参数
            b (str, optional): 字符串参数，默认为"default"
            *args: 可变位置参数
            **kwargs: 可变关键字参数
            
        Returns:
            str: 格式化的字符串结果
            
        Raises:
            ValueError: 当a为负数时抛出
            
        Examples:
            >>> detailed_function(1, "test")
            'Result: 1, test'
        """
        if a < 0:
            raise ValueError("a不能为负数")
        return f"Result: {a}, {b}"
    
    # 添加自定义属性
    detailed_function.custom_attr = "这是自定义属性"
    detailed_function.version = "1.0.0"
    
    def attribute_preserving_decorator(func):
        """保留属性的装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[装饰器] 调用 {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    
    @attribute_preserving_decorator
    def decorated_detailed_function(a: int, b: str = "default", *args, **kwargs) -> str:
        """详细的函数示例
        
        这是一个用于演示函数属性的详细函数。
        
        Args:
            a (int): 整数参数
            b (str, optional): 字符串参数，默认为"default"
            *args: 可变位置参数
            **kwargs: 可变关键字参数
            
        Returns:
            str: 格式化的字符串结果
            
        Raises:
            ValueError: 当a为负数时抛出
            
        Examples:
            >>> detailed_function(1, "test")
            'Result: 1, test'
        """
        if a < 0:
            raise ValueError("a不能为负数")
        return f"Result: {a}, {b}"
    
    # 添加自定义属性
    decorated_detailed_function.custom_attr = "这是自定义属性"
    decorated_detailed_function.version = "1.0.0"
    
    print("原始函数属性：")
    print(f"__name__: {detailed_function.__name__}")
    print(f"__doc__: {detailed_function.__doc__[:50]}...")
    print(f"__module__: {detailed_function.__module__}")
    print(f"__qualname__: {detailed_function.__qualname__}")
    print(f"__annotations__: {detailed_function.__annotations__}")
    
    # 获取函数签名
    sig = inspect.signature(detailed_function)
    print(f"函数签名: {sig}")
    
    print(f"自定义属性 custom_attr: {getattr(detailed_function, 'custom_attr', 'Not found')}")
    print(f"自定义属性 version: {getattr(detailed_function, 'version', 'Not found')}")
    
    print("\n装饰后函数属性：")
    print(f"__name__: {decorated_detailed_function.__name__}")
    print(f"__doc__: {decorated_detailed_function.__doc__[:50]}...")
    print(f"__module__: {decorated_detailed_function.__module__}")
    print(f"__qualname__: {decorated_detailed_function.__qualname__}")
    print(f"__annotations__: {decorated_detailed_function.__annotations__}")
    
    # 获取装饰后函数签名
    decorated_sig = inspect.signature(decorated_detailed_function)
    print(f"函数签名: {decorated_sig}")
    
    print(f"自定义属性 custom_attr: {getattr(decorated_detailed_function, 'custom_attr', 'Not found')}")
    print(f"自定义属性 version: {getattr(decorated_detailed_function, 'version', 'Not found')}")
    
    # 3. wraps在复杂装饰器中的应用
    print("\n3. wraps在复杂装饰器中的应用")
    print("-" * 30)
    
    def timing_decorator(func):
        """计时装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"[计时] {func.__name__} 执行时间: {end_time - start_time:.4f}秒")
            return result
        return wrapper
    
    def logging_decorator(func):
        """日志装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[日志] {datetime.now()} - 开始执行 {func.__name__}")
            print(f"[日志] 参数: args={args}, kwargs={kwargs}")
            try:
                result = func(*args, **kwargs)
                print(f"[日志] {func.__name__} 执行成功")
                return result
            except Exception as e:
                print(f"[日志] {func.__name__} 执行失败: {e}")
                raise
        return wrapper
    
    def retry_decorator(max_attempts=3):
        """重试装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for attempt in range(max_attempts):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        if attempt == max_attempts - 1:
                            raise
                        print(f"[重试] 第 {attempt + 1} 次尝试失败: {e}")
                        time.sleep(0.1)
            return wrapper
        return decorator
    
    @timing_decorator
    @logging_decorator
    @retry_decorator(max_attempts=2)
    def complex_calculation(x: float, y: float, operation: str = "add") -> float:
        """复杂计算函数
        
        执行指定的数学运算。
        
        Args:
            x (float): 第一个操作数
            y (float): 第二个操作数
            operation (str): 运算类型，支持 'add', 'subtract', 'multiply', 'divide'
            
        Returns:
            float: 计算结果
            
        Raises:
            ValueError: 不支持的运算类型
            ZeroDivisionError: 除零错误
        """
        if operation == "add":
            return x + y
        elif operation == "subtract":
            return x - y
        elif operation == "multiply":
            return x * y
        elif operation == "divide":
            if y == 0:
                raise ZeroDivisionError("不能除以零")
            return x / y
        else:
            raise ValueError(f"不支持的运算: {operation}")
    
    print("复杂装饰器链中的函数属性：")
    print(f"函数名: {complex_calculation.__name__}")
    print(f"文档字符串: {complex_calculation.__doc__[:50]}...")
    print(f"函数签名: {inspect.signature(complex_calculation)}")
    print(f"类型注解: {complex_calculation.__annotations__}")
    
    print("\n调用复杂装饰器函数：")
    result = complex_calculation(10.0, 3.0, "divide")
    print(f"计算结果: {result}")
    
    # 4. 自定义wraps实现
    print("\n4. 自定义wraps实现")
    print("-" * 30)
    
    # functools.WRAPPER_ASSIGNMENTS 和 functools.WRAPPER_UPDATES 的内容
    print(f"WRAPPER_ASSIGNMENTS: {functools.WRAPPER_ASSIGNMENTS}")
    print(f"WRAPPER_UPDATES: {functools.WRAPPER_UPDATES}")
    
    def custom_wraps(wrapped, assigned=functools.WRAPPER_ASSIGNMENTS, updated=functools.WRAPPER_UPDATES):
        """自定义的wraps实现"""
        def decorator(wrapper):
            # 复制指定的属性
            for attr in assigned:
                try:
                    original_value = getattr(wrapped, attr)
                    setattr(wrapper, attr, original_value)
                except AttributeError:
                    pass
            
            # 更新指定的属性（通常是__dict__）
            for attr in updated:
                getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
            
            # 设置__wrapped__属性，指向原始函数
            wrapper.__wrapped__ = wrapped
            
            return wrapper
        return decorator
    
    def custom_decorator(func):
        """使用自定义wraps的装饰器"""
        @custom_wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[自定义装饰器] 调用 {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    
    @custom_decorator
    def test_custom_wraps(message: str) -> str:
        """测试自定义wraps的函数
        
        Args:
            message (str): 输入消息
            
        Returns:
            str: 处理后的消息
        """
        return f"处理消息: {message}"
    
    print("\n自定义wraps测试：")
    print(f"函数名: {test_custom_wraps.__name__}")
    print(f"文档字符串: {test_custom_wraps.__doc__[:30]}...")
    print(f"原始函数: {test_custom_wraps.__wrapped__.__name__}")
    
    result = test_custom_wraps("Hello World")
    print(f"执行结果: {result}")
    
    # 5. wraps的高级用法
    print("\n5. wraps的高级用法")
    print("-" * 30)
    
    def partial_wraps_decorator(func):
        """部分属性复制的装饰器"""
        # 只复制部分属性
        @functools.wraps(func, assigned=('__name__', '__doc__'), updated=())
        def wrapper(*args, **kwargs):
            print(f"[部分wraps] 调用 {func.__name__}")
            return func(*args, **kwargs)
        
        # 手动设置一些属性
        wrapper.__custom_info__ = f"这是装饰器添加的信息，原函数: {func.__name__}"
        return wrapper
    
    @partial_wraps_decorator
    def test_partial_wraps(x: int, y: int = 10) -> int:
        """测试部分wraps的函数"""
        return x + y
    
    print("部分wraps测试：")
    print(f"函数名: {test_partial_wraps.__name__}")
    print(f"文档字符串: {test_partial_wraps.__doc__}")
    print(f"自定义信息: {getattr(test_partial_wraps, '__custom_info__', 'Not found')}")
    print(f"类型注解: {getattr(test_partial_wraps, '__annotations__', 'Not found')}")
    
    # 6. 调试和内省
    print("\n6. 调试和内省")
    print("-" * 30)
    
    def debug_decorator(func):
        """调试装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 获取调用信息
            frame = inspect.currentframe()
            caller_frame = frame.f_back
            caller_info = inspect.getframeinfo(caller_frame)
            
            print(f"[调试] 函数 {func.__name__} 被调用")
            print(f"[调试] 调用位置: {caller_info.filename}:{caller_info.lineno}")
            print(f"[调试] 参数绑定:")
            
            # 使用inspect.signature进行参数绑定
            sig = inspect.signature(func)
            try:
                bound_args = sig.bind(*args, **kwargs)
                bound_args.apply_defaults()
                for name, value in bound_args.arguments.items():
                    print(f"[调试]   {name} = {value}")
            except TypeError as e:
                print(f"[调试] 参数绑定失败: {e}")
            
            result = func(*args, **kwargs)
            print(f"[调试] 返回值: {result}")
            return result
        return wrapper
    
    @debug_decorator
    def debugged_function(name: str, age: int, city: str = "Unknown") -> str:
        """被调试的函数
        
        Args:
            name (str): 姓名
            age (int): 年龄
            city (str): 城市
            
        Returns:
            str: 格式化的个人信息
        """
        return f"{name}, {age}岁, 来自{city}"
    
    print("调试装饰器测试：")
    result = debugged_function("张三", 25, city="北京")
    print(f"最终结果: {result}")
    
    # 7. 性能对比
    print("\n7. 性能对比")
    print("-" * 30)
    
    def performance_test():
        """性能测试"""
        
        def no_wraps_decorator(func):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        
        def with_wraps_decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        
        @no_wraps_decorator
        def test_func_no_wraps():
            return "test"
        
        @with_wraps_decorator
        def test_func_with_wraps():
            return "test"
        
        # 测试函数调用性能
        iterations = 100000
        
        # 不使用wraps的性能
        start_time = time.time()
        for _ in range(iterations):
            test_func_no_wraps()
        no_wraps_time = time.time() - start_time
        
        # 使用wraps的性能
        start_time = time.time()
        for _ in range(iterations):
            test_func_with_wraps()
        with_wraps_time = time.time() - start_time
        
        print(f"不使用wraps: {no_wraps_time:.4f}秒 ({iterations} 次调用)")
        print(f"使用wraps: {with_wraps_time:.4f}秒 ({iterations} 次调用)")
        print(f"性能差异: {((with_wraps_time - no_wraps_time) / no_wraps_time * 100):.2f}%")
    
    performance_test()
    
    # 8. 最佳实践总结
    print("\n8. 最佳实践总结")
    print("-" * 30)
    
    print("functools.wraps 最佳实践：")
    print("1. 总是在装饰器中使用 @functools.wraps(func)")
    print("2. 保持原函数的元信息完整性")
    print("3. 便于调试和文档生成")
    print("4. 支持函数内省和签名检查")
    print("5. 在复杂装饰器链中尤其重要")
    print("6. 性能影响微乎其微，但带来的好处巨大")
    
    def best_practice_decorator(func):
        """最佳实践装饰器模板"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 装饰器逻辑
            print(f"[最佳实践] 执行 {func.__name__}")
            
            # 调用原函数
            result = func(*args, **kwargs)
            
            # 后处理逻辑
            print(f"[最佳实践] {func.__name__} 执行完成")
            
            return result
        return wrapper
    
    @best_practice_decorator
    def example_function(data: list) -> int:
        """示例函数：计算列表长度
        
        Args:
            data (list): 输入列表
            
        Returns:
            int: 列表长度
        """
        return len(data)
    
    print("\n最佳实践示例：")
    print(f"函数名: {example_function.__name__}")
    print(f"文档: {example_function.__doc__[:30]}...")
    print(f"签名: {inspect.signature(example_function)}")
    
    result = example_function([1, 2, 3, 4, 5])
    print(f"结果: {result}")


if __name__ == "__main__":
    main()