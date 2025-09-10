#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
装饰器的嵌套使用

装饰器的嵌套使用是指在一个函数上应用多个装饰器。理解装饰器的执行顺序
和相互作用对于正确使用嵌套装饰器至关重要。

学习要点：
1. 理解装饰器的执行顺序（从下到上应用，从上到下执行）
2. 掌握装饰器链的工作原理
3. 学会处理装饰器之间的相互影响
4. 了解装饰器顺序对功能的影响
5. 掌握复杂装饰器组合的最佳实践
"""

import time
import functools
from datetime import datetime
import threading
import json
from typing import Any, Callable


def main():
    """主函数，演示装饰器的嵌套使用"""
    print("=" * 50)
    print("装饰器的嵌套使用")
    print("=" * 50)
    
    # 1. 基本的装饰器嵌套
    print("\n1. 基本的装饰器嵌套")
    print("-" * 30)
    
    def decorator_a(func):
        """装饰器A"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("装饰器A: 执行前")
            result = func(*args, **kwargs)
            print("装饰器A: 执行后")
            return result
        return wrapper
    
    def decorator_b(func):
        """装饰器B"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("装饰器B: 执行前")
            result = func(*args, **kwargs)
            print("装饰器B: 执行后")
            return result
        return wrapper
    
    def decorator_c(func):
        """装饰器C"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("装饰器C: 执行前")
            result = func(*args, **kwargs)
            print("装饰器C: 执行后")
            return result
        return wrapper
    
    @decorator_a
    @decorator_b
    @decorator_c
    def simple_function():
        """简单函数"""
        print("执行原始函数")
        return "函数结果"
    
    print("调用嵌套装饰器函数：")
    print("装饰器应用顺序：C -> B -> A（从下到上）")
    print("执行顺序：A -> B -> C -> 原函数 -> C -> B -> A")
    result = simple_function()
    print(f"最终结果: {result}")
    
    # 2. 装饰器执行顺序详解
    print("\n2. 装饰器执行顺序详解")
    print("-" * 30)
    
    def order_decorator(name):
        """带名称的装饰器，用于观察执行顺序"""
        def decorator(func):
            print(f"装饰器 {name} 正在装饰函数 {func.__name__}")
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(f"[{name}] 进入装饰器")
                result = func(*args, **kwargs)
                print(f"[{name}] 退出装饰器")
                return result
            return wrapper
        return decorator
    
    print("装饰器应用阶段（定义时）：")
    
    @order_decorator("第一层")
    @order_decorator("第二层")
    @order_decorator("第三层")
    def ordered_function(message):
        """有序函数"""
        print(f"[原函数] {message}")
        return f"处理完成: {message}"
    
    print("\n函数执行阶段（调用时）：")
    result = ordered_function("测试消息")
    print(f"返回结果: {result}")
    
    # 3. 实用装饰器组合
    print("\n3. 实用装饰器组合")
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
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[日志] {timestamp} - 调用 {func.__name__}")
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
                        print(f"[重试] 第 {attempt + 1} 次尝试")
                        result = func(*args, **kwargs)
                        return result
                    except Exception as e:
                        print(f"[重试] 第 {attempt + 1} 次尝试失败: {e}")
                        if attempt == max_attempts - 1:
                            print(f"[重试] 所有 {max_attempts} 次尝试都失败")
                            raise
                        time.sleep(0.1)  # 短暂延迟
            return wrapper
        return decorator
    
    def cache_decorator(func):
        """简单缓存装饰器"""
        cache = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(sorted(kwargs.items()))
            if key in cache:
                print(f"[缓存] 缓存命中: {func.__name__}")
                return cache[key]
            
            print(f"[缓存] 缓存未命中，执行函数")
            result = func(*args, **kwargs)
            cache[key] = result
            print(f"[缓存] 结果已缓存")
            return result
        return wrapper
    
    # 模拟一个可能失败的函数
    failure_count = {"count": 0}
    
    @timing_decorator
    @logging_decorator
    @retry_decorator(max_attempts=3)
    @cache_decorator
    def unreliable_calculation(x, y):
        """不可靠的计算函数"""
        failure_count["count"] += 1
        
        # 前两次调用会失败
        if failure_count["count"] <= 2:
            raise ValueError(f"计算失败 (第 {failure_count['count']} 次)")
        
        # 模拟计算
        time.sleep(0.1)
        result = x * y + (x + y)
        print(f"[计算] {x} * {y} + ({x} + {y}) = {result}")
        return result
    
    print("调用实用装饰器组合：")
    try:
        result = unreliable_calculation(5, 3)
        print(f"计算结果: {result}")
    except Exception as e:
        print(f"计算最终失败: {e}")
    
    print("\n再次调用（应该使用缓存）：")
    failure_count["count"] = 10  # 重置失败计数，确保不会再失败
    result = unreliable_calculation(5, 3)
    print(f"缓存结果: {result}")
    
    # 4. 装饰器顺序的重要性
    print("\n4. 装饰器顺序的重要性")
    print("-" * 30)
    
    def validation_decorator(func):
        """参数验证装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("[验证] 检查参数")
            if not args or not isinstance(args[0], (int, float)):
                raise ValueError("第一个参数必须是数字")
            if len(args) < 2 or not isinstance(args[1], (int, float)):
                raise ValueError("第二个参数必须是数字")
            print("[验证] 参数验证通过")
            return func(*args, **kwargs)
        return wrapper
    
    def conversion_decorator(func):
        """类型转换装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("[转换] 转换参数类型")
            # 将前两个参数转换为浮点数
            converted_args = list(args)
            if len(converted_args) >= 1:
                converted_args[0] = float(converted_args[0])
            if len(converted_args) >= 2:
                converted_args[1] = float(converted_args[1])
            print(f"[转换] 转换后的参数: {converted_args}")
            return func(*converted_args, **kwargs)
        return wrapper
    
    # 正确的顺序：先转换，再验证
    print("正确的装饰器顺序（验证 -> 转换）：")
    
    @validation_decorator
    @conversion_decorator
    def calculate_correct(x, y):
        """正确顺序的计算函数"""
        result = x / y
        print(f"[计算] {x} / {y} = {result}")
        return result
    
    try:
        result = calculate_correct("10", "2")  # 字符串输入
        print(f"正确顺序结果: {result}")
    except Exception as e:
        print(f"正确顺序错误: {e}")
    
    # 错误的顺序：先验证，再转换
    print("\n错误的装饰器顺序（转换 -> 验证）：")
    
    @conversion_decorator
    @validation_decorator
    def calculate_wrong(x, y):
        """错误顺序的计算函数"""
        result = x / y
        print(f"[计算] {x} / {y} = {result}")
        return result
    
    try:
        result = calculate_wrong("10", "2")  # 字符串输入
        print(f"错误顺序结果: {result}")
    except Exception as e:
        print(f"错误顺序错误: {e}")
    
    # 5. 装饰器间的数据传递
    print("\n5. 装饰器间的数据传递")
    print("-" * 30)
    
    def context_decorator(func):
        """上下文装饰器，添加执行上下文"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 在kwargs中添加上下文信息
            context = {
                'timestamp': datetime.now().isoformat(),
                'thread_id': threading.current_thread().ident,
                'function_name': func.__name__
            }
            kwargs['_context'] = context
            print(f"[上下文] 添加执行上下文: {context['timestamp']}")
            return func(*args, **kwargs)
        return wrapper
    
    def metadata_decorator(func):
        """元数据装饰器，处理上下文信息"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            context = kwargs.pop('_context', None)
            if context:
                print(f"[元数据] 处理上下文: 函数 {context['function_name']} 在 {context['timestamp']} 执行")
                print(f"[元数据] 线程ID: {context['thread_id']}")
            
            result = func(*args, **kwargs)
            
            # 在结果中添加元数据
            if isinstance(result, dict):
                result['_metadata'] = context
            
            return result
        return wrapper
    
    @context_decorator
    @metadata_decorator
    def process_data(data, operation="sum"):
        """数据处理函数"""
        print(f"[处理] 执行 {operation} 操作")
        
        if operation == "sum":
            result = sum(data)
        elif operation == "average":
            result = sum(data) / len(data)
        else:
            result = data
        
        return {
            'operation': operation,
            'input_data': data,
            'result': result
        }
    
    print("调用装饰器间数据传递：")
    result = process_data([1, 2, 3, 4, 5], operation="average")
    print(f"处理结果: {json.dumps(result, indent=2, default=str)}")
    
    # 6. 复杂装饰器链的最佳实践
    print("\n6. 复杂装饰器链的最佳实践")
    print("-" * 30)
    
    def error_handling_decorator(func):
        """错误处理装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                print(f"[错误处理] 值错误: {e}")
                return {'error': 'ValueError', 'message': str(e)}
            except ZeroDivisionError as e:
                print(f"[错误处理] 除零错误: {e}")
                return {'error': 'ZeroDivisionError', 'message': str(e)}
            except Exception as e:
                print(f"[错误处理] 未知错误: {e}")
                return {'error': 'Exception', 'message': str(e)}
        return wrapper
    
    def result_formatting_decorator(func):
        """结果格式化装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            if isinstance(result, dict) and 'error' in result:
                # 错误结果，不进行格式化
                print(f"[格式化] 检测到错误，跳过格式化")
                return result
            
            # 正常结果，进行格式化
            formatted_result = {
                'success': True,
                'data': result,
                'timestamp': datetime.now().isoformat()
            }
            print(f"[格式化] 结果已格式化")
            return formatted_result
        return wrapper
    
    def performance_monitoring_decorator(func):
        """性能监控装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            start_memory = 0  # 简化版，实际应用中可以使用psutil等库
            
            result = func(*args, **kwargs)
            
            end_time = time.time()
            execution_time = end_time - start_time
            
            print(f"[性能监控] 执行时间: {execution_time:.4f}秒")
            
            # 如果结果是字典且包含success字段，添加性能信息
            if isinstance(result, dict) and 'success' in result:
                result['performance'] = {
                    'execution_time': execution_time,
                    'memory_usage': 0  # 简化版
                }
            
            return result
        return wrapper
    
    # 最佳实践：按照逻辑顺序排列装饰器
    # 1. 性能监控（最外层，监控整个执行过程）
    # 2. 错误处理（处理所有可能的错误）
    # 3. 结果格式化（格式化最终结果）
    # 4. 核心业务逻辑（最内层）
    
    @performance_monitoring_decorator
    @error_handling_decorator
    @result_formatting_decorator
    def complex_business_logic(operation, x, y):
        """复杂业务逻辑"""
        print(f"[业务逻辑] 执行 {operation} 操作")
        
        if operation == "divide":
            if y == 0:
                raise ZeroDivisionError("不能除以零")
            return x / y
        elif operation == "multiply":
            return x * y
        elif operation == "power":
            if x < 0 and not isinstance(y, int):
                raise ValueError("负数不能进行非整数次幂运算")
            return x ** y
        else:
            raise ValueError(f"不支持的操作: {operation}")
    
    print("调用复杂装饰器链：")
    
    # 正常情况
    result1 = complex_business_logic("multiply", 5, 3)
    print(f"正常结果: {json.dumps(result1, indent=2)}\n")
    
    # 除零错误
    result2 = complex_business_logic("divide", 10, 0)
    print(f"除零错误结果: {json.dumps(result2, indent=2)}\n")
    
    # 值错误
    result3 = complex_business_logic("invalid", 1, 2)
    print(f"值错误结果: {json.dumps(result3, indent=2)}")


if __name__ == "__main__":
    main()