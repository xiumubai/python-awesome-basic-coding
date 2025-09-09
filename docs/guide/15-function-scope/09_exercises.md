# 综合练习（Exercises）

本章提供了一系列综合练习，帮助你巩固和深化对Python函数作用域的理解。这些练习涵盖了从基础概念到高级应用的各个方面，通过实际编程来掌握作用域的核心知识。

## 练习概述

练习分为以下几个层次：
1. **基础练习**：局部、全局、内置作用域的基本使用
2. **进阶练习**：LEGB规则、作用域修改、闭包应用
3. **高级练习**：复杂嵌套、性能优化、实际应用
4. **挑战练习**：综合应用、调试技巧、最佳实践

## 代码示例

### 综合练习集合

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
函数作用域综合练习

本文件包含了一系列练习题，涵盖Python函数作用域的各个方面：
- 基础作用域概念
- LEGB规则应用
- 闭包和装饰器
- 作用域修改
- 实际应用场景
- 调试和优化
- 高级应用

每个练习都包含问题描述、示例代码、预期输出和解析说明。
"""

import time
import functools
import builtins
from typing import Callable, Any, List, Dict

# ============================================================================
# 基础练习：作用域基本概念
# ============================================================================

def exercise_1_basic_scopes():
    """
    练习1：基础作用域识别
    
    问题：分析下面的代码，说明每个变量属于哪个作用域，
    并预测输出结果。
    """
    print("=== 练习1：基础作用域识别 ===")
    
    # 全局变量
    global_var = "我是全局变量"
    
    def outer_function():
        # 外层函数的局部变量
        outer_local = "我是外层局部变量"
        
        def inner_function():
            # 内层函数的局部变量
            inner_local = "我是内层局部变量"
            
            print(f"内层函数中访问:")
            print(f"  inner_local: {inner_local}")      # L - 局部
            print(f"  outer_local: {outer_local}")      # E - 嵌套
            print(f"  global_var: {global_var}")        # G - 全局
            print(f"  len: {len}")                      # B - 内置
        
        inner_function()
        print(f"外层函数中访问:")
        print(f"  outer_local: {outer_local}")          # L - 局部
        print(f"  global_var: {global_var}")            # G - 全局
    
    outer_function()
    print(f"全局作用域中访问:")
    print(f"  global_var: {global_var}")                # G - 全局
    
    print("\n解析：")
    print("- inner_local: 内层函数的局部变量（L）")
    print("- outer_local: 外层函数的局部变量，对内层函数是嵌套作用域（E）")
    print("- global_var: 模块级全局变量（G）")
    print("- len: Python内置函数（B）")

def exercise_2_variable_shadowing():
    """
    练习2：变量遮蔽分析
    
    问题：分析变量遮蔽现象，理解不同作用域中同名变量的行为。
    """
    print("\n=== 练习2：变量遮蔽分析 ===")
    
    name = "全局的name"
    
    def test_shadowing():
        print(f"函数开始时的name: {name}")  # 访问全局变量
        
        # 在函数中创建同名的局部变量
        name = "局部的name"
        print(f"创建局部变量后的name: {name}")  # 访问局部变量
        
        def inner_function():
            print(f"内层函数中的name: {name}")  # 访问外层的局部变量
            
            # 再次遮蔽
            name = "内层局部的name"
            print(f"内层创建局部变量后的name: {name}")
        
        inner_function()
        print(f"内层函数调用后的name: {name}")  # 仍然是外层的局部变量
    
    test_shadowing()
    print(f"函数调用后的全局name: {name}")  # 全局变量未受影响
    
    print("\n解析：")
    print("- 每个作用域中的同名变量是独立的")
    print("- 内层作用域的变量会遮蔽外层的同名变量")
    print("- 变量遮蔽不会影响外层作用域的原变量")

def exercise_3_builtin_shadowing():
    """
    练习3：内置函数遮蔽
    
    问题：演示内置函数被遮蔽的情况及其解决方法。
    """
    print("\n=== 练习3：内置函数遮蔽 ===")
    
    def demonstrate_builtin_shadowing():
        # 意外遮蔽内置函数
        print("1. 遮蔽内置函数的问题:")
        
        list = [1, 2, 3, 4, 5]  # 遮蔽了内置的list函数
        print(f"  创建了变量list: {list}")
        
        try:
            # 尝试使用list函数
            new_list = list((6, 7, 8))
        except TypeError as e:
            print(f"  错误: {e}")
            print("  原因: list变量遮蔽了内置的list函数")
        
        print("\n2. 解决方法:")
        
        # 方法1: 使用不同的变量名
        data_list = [1, 2, 3, 4, 5]
        new_list = list((6, 7, 8))
        print(f"  方法1 - 使用不同名称: data_list={data_list}")
        print(f"  现在可以使用list函数: {new_list}")
        
        # 方法2: 通过builtins模块访问
        list = [1, 2, 3, 4, 5]  # 再次遮蔽
        builtin_list = builtins.list((9, 10, 11))
        print(f"  方法2 - 通过builtins访问: {builtin_list}")
        
        # 方法3: 删除遮蔽变量
        del list
        restored_list = list((12, 13, 14))
        print(f"  方法3 - 删除遮蔽变量: {restored_list}")
    
    demonstrate_builtin_shadowing()
    
    print("\n解析：")
    print("- 避免使用内置函数名作为变量名")
    print("- 可以通过builtins模块访问被遮蔽的内置函数")
    print("- 删除遮蔽变量可以恢复对内置函数的访问")

# ============================================================================
# 进阶练习：LEGB规则和作用域修改
# ============================================================================

def exercise_4_legb_resolution():
    """
    练习4：LEGB规则解析
    
    问题：分析复杂的嵌套函数中的变量查找过程。
    """
    print("\n=== 练习4：LEGB规则解析 ===")
    
    # 在不同作用域定义同名变量
    x = "全局x"
    
    def level1():
        x = "level1的x"
        
        def level2():
            # 注意：这里没有定义x
            
            def level3():
                x = "level3的x"
                
                def level4():
                    # 这里也没有定义x
                    print(f"level4中的x: {x}")  # 会找到哪个x？
                    
                    # 分析查找过程
                    print("查找过程分析:")
                    print("  L (Local): level4没有x")
                    print("  E (Enclosing): level3有x ← 找到了！")
                    print("  G (Global): 不会查找到这里")
                    print("  B (Built-in): 不会查找到这里")
                
                level4()
            
            level3()
            
            # 在level2中访问x
            print(f"level2中的x: {x}")  # 会找到哪个x？
            print("查找过程分析:")
            print("  L (Local): level2没有x")
            print("  E (Enclosing): level1有x ← 找到了！")
        
        level2()
    
    level1()
    
    print("\n解析：")
    print("- Python按照L→E→G→B的顺序查找变量")
    print("- 找到第一个匹配的变量后停止搜索")
    print("- 嵌套作用域可能跨越多个函数层级")

def exercise_5_global_nonlocal():
    """
    练习5：global和nonlocal关键字
    
    问题：正确使用global和nonlocal修改外层作用域的变量。
    """
    print("\n=== 练习5：global和nonlocal关键字 ===")
    
    # 全局计数器
    global_counter = 0
    
    def test_global_nonlocal():
        # 外层函数的计数器
        enclosing_counter = 0
        
        def increment_counters():
            nonlocal enclosing_counter
            global global_counter
            
            # 局部计数器
            local_counter = 0
            
            # 修改各个作用域的计数器
            local_counter += 1
            enclosing_counter += 1
            global_counter += 1
            
            print(f"increment_counters执行后:")
            print(f"  local_counter: {local_counter}")
            print(f"  enclosing_counter: {enclosing_counter}")
            print(f"  global_counter: {global_counter}")
            
            return local_counter
        
        print(f"初始状态:")
        print(f"  enclosing_counter: {enclosing_counter}")
        print(f"  global_counter: {global_counter}")
        
        # 多次调用
        for i in range(3):
            print(f"\n第{i+1}次调用:")
            local_result = increment_counters()
            print(f"  返回的local_counter: {local_result}")
            print(f"  外层enclosing_counter: {enclosing_counter}")
    
    test_global_nonlocal()
    print(f"\n最终全局计数器: {global_counter}")
    
    print("\n解析：")
    print("- local_counter每次都重新创建，所以始终是1")
    print("- enclosing_counter通过nonlocal修改，会累积")
    print("- global_counter通过global修改，会累积")

def exercise_6_unbound_local_error():
    """
    练习6：UnboundLocalError分析
    
    问题：理解和解决UnboundLocalError。
    """
    print("\n=== 练习6：UnboundLocalError分析 ===")
    
    counter = 10
    
    def demonstrate_unbound_local():
        print("1. 产生UnboundLocalError的情况:")
        
        def problematic_function():
            try:
                print(f"尝试读取counter: {counter}")  # 这里会出错
                counter += 1  # Python看到这行，认为counter是局部变量
            except UnboundLocalError as e:
                print(f"  错误: {e}")
                print("  原因: Python发现counter被赋值，认为它是局部变量")
                print("       但在赋值前尝试读取，导致UnboundLocalError")
        
        problematic_function()
        
        print("\n2. 解决方法:")
        
        def solution1_nonlocal():
            nonlocal counter
            print(f"使用nonlocal - 读取counter: {counter}")
            counter += 1
            print(f"使用nonlocal - 修改后counter: {counter}")
        
        def solution2_global():
            global counter
            print(f"使用global - 读取counter: {counter}")
            # 注意：这里counter已经被solution1修改了
        
        def solution3_parameter(c):
            print(f"使用参数传递 - 读取c: {c}")
            c += 1
            print(f"使用参数传递 - 修改后c: {c}")
            return c
        
        solution1_nonlocal()
        solution2_global()
        new_counter = solution3_parameter(counter)
        print(f"参数传递返回值: {new_counter}")
    
    demonstrate_unbound_local()
    print(f"最终counter值: {counter}")
    
    print("\n解析：")
    print("- Python在编译时分析变量赋值，确定变量的作用域")
    print("- 如果函数中有对变量的赋值，Python认为它是局部变量")
    print("- 在赋值前读取局部变量会导致UnboundLocalError")
    print("- 使用nonlocal/global声明可以明确变量的作用域")

# ============================================================================
# 高级练习：闭包和装饰器
# ============================================================================

def exercise_7_closure_applications():
    """
    练习7：闭包应用
    
    问题：创建和使用闭包来实现各种功能。
    """
    print("\n=== 练习7：闭包应用 ===")
    
    def create_counter(initial=0, step=1):
        """创建一个计数器闭包"""
        count = initial
        
        def counter():
            nonlocal count
            count += step
            return count
        
        # 添加额外的方法
        def reset():
            nonlocal count
            count = initial
        
        def get_current():
            return count
        
        # 将方法附加到counter函数上
        counter.reset = reset
        counter.get_current = get_current
        
        return counter
    
    def create_accumulator():
        """创建一个累加器闭包"""
        total = 0
        history = []
        
        def accumulate(value):
            nonlocal total
            total += value
            history.append(value)
            return total
        
        def get_history():
            return history.copy()
        
        def get_average():
            return total / len(history) if history else 0
        
        accumulate.get_history = get_history
        accumulate.get_average = get_average
        
        return accumulate
    
    def create_validator(min_val, max_val):
        """创建一个验证器闭包"""
        def validate(value):
            if min_val <= value <= max_val:
                return True, f"值{value}在有效范围[{min_val}, {max_val}]内"
            else:
                return False, f"值{value}超出有效范围[{min_val}, {max_val}]"
        
        return validate
    
    # 测试计数器
    print("1. 计数器闭包测试:")
    counter1 = create_counter(0, 1)
    counter2 = create_counter(100, 5)
    
    for i in range(3):
        print(f"  counter1(): {counter1()}, counter2(): {counter2()}")
    
    print(f"  counter1当前值: {counter1.get_current()}")
    counter1.reset()
    print(f"  counter1重置后: {counter1.get_current()}")
    
    # 测试累加器
    print("\n2. 累加器闭包测试:")
    acc = create_accumulator()
    
    values = [10, 20, 30, 40]
    for val in values:
        total = acc(val)
        print(f"  添加{val}, 总计: {total}")
    
    print(f"  历史记录: {acc.get_history()}")
    print(f"  平均值: {acc.get_average():.2f}")
    
    # 测试验证器
    print("\n3. 验证器闭包测试:")
    age_validator = create_validator(0, 120)
    score_validator = create_validator(0, 100)
    
    test_values = [25, 150, 85, -5]
    for val in test_values:
        age_valid, age_msg = age_validator(val)
        score_valid, score_msg = score_validator(val)
        print(f"  值{val}: 年龄验证-{age_msg}, 分数验证-{score_msg}")
    
    print("\n解析：")
    print("- 闭包可以保持状态，实现数据封装")
    print("- 可以为闭包函数添加额外的方法和属性")
    print("- 每个闭包实例都有独立的状态")

def exercise_8_decorator_with_scope():
    """
    练习8：基于作用域的装饰器
    
    问题：创建利用作用域特性的装饰器。
    """
    print("\n=== 练习8：基于作用域的装饰器 ===")
    
    def memoize(func):
        """记忆化装饰器，利用闭包缓存结果"""
        cache = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 创建缓存键
            key = str(args) + str(sorted(kwargs.items()))
            
            if key in cache:
                print(f"  缓存命中: {func.__name__}{args}")
                return cache[key]
            
            print(f"  计算结果: {func.__name__}{args}")
            result = func(*args, **kwargs)
            cache[key] = result
            return result
        
        # 添加缓存管理方法
        wrapper.cache_clear = lambda: cache.clear()
        wrapper.cache_info = lambda: f"缓存大小: {len(cache)}, 内容: {list(cache.keys())}"
        
        return wrapper
    
    def retry(max_attempts=3, delay=0.1):
        """重试装饰器，利用闭包保存重试配置"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                last_exception = None
                
                for attempt in range(max_attempts):
                    try:
                        result = func(*args, **kwargs)
                        if attempt > 0:
                            print(f"  第{attempt + 1}次尝试成功")
                        return result
                    except Exception as e:
                        last_exception = e
                        print(f"  第{attempt + 1}次尝试失败: {e}")
                        if attempt < max_attempts - 1:
                            time.sleep(delay)
                
                print(f"  所有{max_attempts}次尝试都失败了")
                raise last_exception
            
            return wrapper
        return decorator
    
    def rate_limit(calls_per_second=1):
        """限流装饰器，利用闭包保存调用历史"""
        def decorator(func):
            call_times = []
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                current_time = time.time()
                
                # 清理过期的调用记录
                call_times[:] = [t for t in call_times if current_time - t < 1.0]
                
                if len(call_times) >= calls_per_second:
                    wait_time = 1.0 - (current_time - call_times[0])
                    print(f"  限流等待 {wait_time:.2f} 秒")
                    time.sleep(wait_time)
                    current_time = time.time()
                
                call_times.append(current_time)
                return func(*args, **kwargs)
            
            return wrapper
        return decorator
    
    # 测试装饰器
    @memoize
    def fibonacci(n):
        """计算斐波那契数列（递归版本）"""
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    @retry(max_attempts=3, delay=0.1)
    def unreliable_function(success_rate=0.3):
        """模拟不稳定的函数"""
        import random
        if random.random() < success_rate:
            return "成功!"
        else:
            raise Exception("随机失败")
    
    @rate_limit(calls_per_second=2)
    def api_call(data):
        """模拟API调用"""
        return f"处理数据: {data}"
    
    # 测试记忆化装饰器
    print("1. 记忆化装饰器测试:")
    print(f"  fibonacci(10) = {fibonacci(10)}")
    print(f"  {fibonacci.cache_info()}")
    
    # 测试重试装饰器
    print("\n2. 重试装饰器测试:")
    try:
        result = unreliable_function(0.8)  # 80%成功率
        print(f"  结果: {result}")
    except Exception as e:
        print(f"  最终失败: {e}")
    
    # 测试限流装饰器
    print("\n3. 限流装饰器测试:")
    for i in range(3):
        result = api_call(f"数据{i}")
        print(f"  {result}")
    
    print("\n解析：")
    print("- 装饰器利用闭包保存状态和配置")
    print("- 每个装饰器实例都有独立的状态")
    print("- 可以为装饰器添加额外的管理方法")

# ============================================================================
# 挑战练习：复杂应用和优化
# ============================================================================

def exercise_9_scope_performance():
    """
    练习9：作用域性能优化
    
    问题：分析和优化不同作用域访问的性能。
    """
    print("\n=== 练习9：作用域性能优化 ===")
    
    # 全局变量
    global_data = list(range(1000))
    global_len = len
    
    def performance_comparison():
        """比较不同作用域访问的性能"""
        iterations = 100000
        
        def test_global_access():
            """测试全局变量访问"""
            start_time = time.time()
            for _ in range(iterations):
                result = len(global_data)  # 访问全局变量和内置函数
            end_time = time.time()
            return end_time - start_time
        
        def test_local_cache():
            """测试局部变量缓存"""
            local_data = global_data  # 缓存全局变量
            local_len = len           # 缓存内置函数
            
            start_time = time.time()
            for _ in range(iterations):
                result = local_len(local_data)  # 访问局部变量
            end_time = time.time()
            return end_time - start_time
        
        def test_attribute_access():
            """测试属性访问优化"""
            class DataContainer:
                def __init__(self):
                    self.data = global_data
                    self.len_func = len
            
            container = DataContainer()
            
            start_time = time.time()
            for _ in range(iterations):
                result = container.len_func(container.data)
            end_time = time.time()
            return end_time - start_time
        
        # 执行性能测试
        global_time = test_global_access()
        local_time = test_local_cache()
        attribute_time = test_attribute_access()
        
        print(f"性能测试结果（{iterations}次迭代）:")
        print(f"  全局访问: {global_time:.6f}秒")
        print(f"  局部缓存: {local_time:.6f}秒")
        print(f"  属性访问: {attribute_time:.6f}秒")
        
        print(f"\n性能提升:")
        print(f"  局部缓存比全局访问快: {global_time/local_time:.2f}倍")
        print(f"  局部缓存比属性访问快: {attribute_time/local_time:.2f}倍")
        
        return {
            'global': global_time,
            'local': local_time,
            'attribute': attribute_time
        }
    
    def optimization_techniques():
        """演示各种优化技巧"""
        print("\n优化技巧演示:")
        
        # 技巧1: 循环中的局部变量缓存
        def unoptimized_loop():
            result = []
            for i in range(1000):
                result.append(len(str(i)))  # 每次都查找len和str
            return result
        
        def optimized_loop():
            result = []
            local_len = len  # 缓存内置函数
            local_str = str
            for i in range(1000):
                result.append(local_len(local_str(i)))
            return result
        
        # 测试循环优化
        start_time = time.time()
        unoptimized_result = unoptimized_loop()
        unoptimized_time = time.time() - start_time
        
        start_time = time.time()
        optimized_result = optimized_loop()
        optimized_time = time.time() - start_time
        
        print(f"  循环优化测试:")
        print(f"    未优化版本: {unoptimized_time:.6f}秒")
        print(f"    优化版本: {optimized_time:.6f}秒")
        print(f"    性能提升: {unoptimized_time/optimized_time:.2f}倍")
        
        # 技巧2: 避免重复的全局查找
        def create_optimized_function():
            # 在函数创建时缓存常用的全局对象
            _len = len
            _str = str
            _int = int
            
            def process_data(data):
                return [_int(_str(item)) for item in data if _len(_str(item)) > 2]
            
            return process_data
        
        optimized_func = create_optimized_function()
        test_data = range(100, 1000)
        
        start_time = time.time()
        result1 = [int(str(item)) for item in test_data if len(str(item)) > 2]
        time1 = time.time() - start_time
        
        start_time = time.time()
        result2 = optimized_func(test_data)
        time2 = time.time() - start_time
        
        print(f"  全局查找优化:")
        print(f"    普通版本: {time1:.6f}秒")
        print(f"    优化版本: {time2:.6f}秒")
        print(f"    性能提升: {time1/time2:.2f}倍")
    
    # 执行性能测试
    performance_results = performance_comparison()
    optimization_techniques()
    
    print("\n解析：")
    print("- 局部变量访问比全局变量访问更快")
    print("- 缓存频繁使用的全局变量和内置函数可以提高性能")
    print("- 在循环中避免重复的作用域查找")
    print("- 属性访问通常比直接变量访问慢")

def exercise_10_advanced_debugging():
    """
    练习10：高级调试技巧
    
    问题：使用高级技巧调试作用域相关的问题。
    """
    print("\n=== 练习10：高级调试技巧 ===")
    
    def scope_inspector():
        """作用域检查器"""
        import inspect
        
        def analyze_current_scope():
            """分析当前的作用域链"""
            frame = inspect.currentframe()
            scope_chain = []
            
            try:
                while frame:
                    scope_info = {
                        'function': frame.f_code.co_name,
                        'filename': frame.f_code.co_filename.split('/')[-1],
                        'lineno': frame.f_lineno,
                        'locals': dict(frame.f_locals),
                        'globals_count': len(frame.f_globals)
                    }
                    scope_chain.append(scope_info)
                    frame = frame.f_back
            finally:
                del frame
            
            return scope_chain
        
        def trace_variable_lookup(var_name):
            """追踪变量查找过程"""
            frame = inspect.currentframe().f_back
            
            print(f"追踪变量 '{var_name}' 的查找过程:")
            
            # L - Local
            if var_name in frame.f_locals:
                print(f"  ✓ L (Local): 在局部作用域找到 = {frame.f_locals[var_name]}")
                return frame.f_locals[var_name]
            else:
                print(f"  ✗ L (Local): 局部作用域没有 '{var_name}'")
            
            # E - Enclosing
            outer_frame = frame.f_back
            enclosing_level = 1
            while outer_frame:
                if var_name in outer_frame.f_locals:
                    print(f"  ✓ E (Enclosing-{enclosing_level}): 在嵌套作用域找到 = {outer_frame.f_locals[var_name]}")
                    return outer_frame.f_locals[var_name]
                outer_frame = outer_frame.f_back
                enclosing_level += 1
            
            print(f"  ✗ E (Enclosing): 嵌套作用域没有 '{var_name}'")
            
            # G - Global
            if var_name in frame.f_globals:
                print(f"  ✓ G (Global): 在全局作用域找到 = {frame.f_globals[var_name]}")
                return frame.f_globals[var_name]
            else:
                print(f"  ✗ G (Global): 全局作用域没有 '{var_name}'")
            
            # B - Built-in
            if hasattr(builtins, var_name):
                builtin_value = getattr(builtins, var_name)
                print(f"  ✓ B (Built-in): 在内置作用域找到 = {builtin_value}")
                return builtin_value
            else:
                print(f"  ✗ B (Built-in): 内置作用域没有 '{var_name}'")
            
            print(f"  ❌ 变量 '{var_name}' 在所有作用域中都未找到")
            return None
        
        return analyze_current_scope, trace_variable_lookup
    
    def debug_closure_issues():
        """调试闭包相关问题"""
        print("1. 闭包调试演示:")
        
        def create_problematic_closures():
            """创建有问题的闭包（经典的循环变量绑定问题）"""
            functions = []
            
            # 问题版本
            for i in range(3):
                functions.append(lambda: f"问题版本: i = {i}")
            
            return functions
        
        def create_correct_closures():
            """创建正确的闭包"""
            functions = []
            
            # 正确版本1: 使用默认参数
            for i in range(3):
                functions.append(lambda x=i: f"正确版本1: x = {x}")
            
            return functions
        
        def analyze_closure(func):
            """分析闭包的变量捕获"""
            if hasattr(func, '__closure__') and func.__closure__:
                print(f"    闭包变量:")
                for j, cell in enumerate(func.__closure__):
                    try:
                        print(f"      变量{j}: {cell.cell_contents}")
                    except ValueError:
                        print(f"      变量{j}: <空单元格>")
            else:
                print(f"    没有闭包变量")
        
        # 测试问题版本
        problematic_funcs = create_problematic_closures()
        print("  问题版本的闭包:")
        for i, func in enumerate(problematic_funcs):
            print(f"    函数{i}: {func()}")
            analyze_closure(func)
        
        # 测试正确版本
        correct_funcs = create_correct_closures()
        print("\n  正确版本的闭包:")
        for i, func in enumerate(correct_funcs):
            print(f"    函数{i}: {func()}")
            analyze_closure(func)
    
    def debug_scope_pollution():
        """调试作用域污染问题"""
        print("\n2. 作用域污染调试:")
        
        def check_name_conflicts():
            """检查命名冲突"""
            builtin_names = set(dir(builtins))
            
            # 获取当前作用域的变量
            frame = inspect.currentframe().f_back
            local_names = set(frame.f_locals.keys())
            global_names = set(frame.f_globals.keys())
            
            # 检查冲突
            local_conflicts = local_names & builtin_names
            global_conflicts = global_names & builtin_names
            
            if local_conflicts:
                print(f"  ⚠️  局部变量与内置名称冲突: {local_conflicts}")
            
            if global_conflicts:
                print(f"  ⚠️  全局变量与内置名称冲突: {global_conflicts}")
            
            if not local_conflicts and not global_conflicts:
                print(f"  ✅ 没有发现命名冲突")
            
            return local_conflicts, global_conflicts
        
        # 故意创建一些冲突
        list = [1, 2, 3]  # 遮蔽内置list
        dict = {'a': 1}   # 遮蔽内置dict
        
        conflicts = check_name_conflicts()
        
        # 清理冲突
        del list, dict
        print("  清理冲突后:")
        check_name_conflicts()
    
    # 执行调试演示
    analyze_scope, trace_lookup = scope_inspector()
    
    # 创建一些测试变量
    test_var = "测试变量"
    
    def outer_debug_function():
        outer_var = "外层变量"
        
        def inner_debug_function():
            inner_var = "内层变量"
            
            print("作用域链分析:")
            scope_chain = analyze_scope()
            for i, scope in enumerate(scope_chain[:3]):
                print(f"  层级{i}: {scope['function']} (行{scope['lineno']})")
                local_vars = {k: v for k, v in scope['locals'].items() 
                             if not k.startswith('_') and k != 'scope_chain'}
                print(f"    局部变量: {list(local_vars.keys())}")
            
            print("\n变量查找演示:")
            trace_lookup('inner_var')
            trace_lookup('outer_var')
            trace_lookup('test_var')
            trace_lookup('len')
            trace_lookup('nonexistent_var')
        
        inner_debug_function()
    
    outer_debug_function()
    debug_closure_issues()
    debug_scope_pollution()
    
    print("\n解析：")
    print("- 使用inspect模块可以分析作用域链")
    print("- 闭包问题通常与变量绑定时机有关")
    print("- 定期检查命名冲突可以避免作用域污染")
    print("- 理解变量查找过程有助于调试复杂问题")

def exercise_11_real_world_applications():
    """
    练习11：实际应用场景
    
    问题：在实际项目中应用作用域知识。
    """
    print("\n=== 练习11：实际应用场景 ===")
    
    def create_plugin_system():
        """创建一个基于作用域的插件系统"""
        print("1. 插件系统实现:")
        
        class PluginManager:
            def __init__(self):
                self.plugins = {}
                self.hooks = {}
            
            def register_plugin(self, name, plugin_func):
                """注册插件"""
                self.plugins[name] = plugin_func
                print(f"  注册插件: {name}")
            
            def register_hook(self, event, callback):
                """注册事件钩子"""
                if event not in self.hooks:
                    self.hooks[event] = []
                self.hooks[event].append(callback)
                print(f"  注册钩子: {event}")
            
            def execute_plugin(self, name, *args, **kwargs):
                """执行插件"""
                if name in self.plugins:
                    return self.plugins[name](*args, **kwargs)
                else:
                    raise ValueError(f"插件 '{name}' 未找到")
            
            def trigger_hooks(self, event, *args, **kwargs):
                """触发事件钩子"""
                results = []
                if event in self.hooks:
                    for callback in self.hooks[event]:
                        result = callback(*args, **kwargs)
                        results.append(result)
                return results
        
        # 创建插件管理器
        pm = PluginManager()
        
        # 创建一些插件（利用闭包保存状态）
        def create_logger_plugin(log_level='INFO'):
            logs = []
            
            def logger(message, level='INFO'):
                if level == log_level or log_level == 'DEBUG':
                    log_entry = f"[{level}] {message}"
                    logs.append(log_entry)
                    print(f"    日志: {log_entry}")
                    return log_entry
                return None
            
            logger.get_logs = lambda: logs.copy()
            logger.clear_logs = lambda: logs.clear()
            return logger
        
        def create_cache_plugin(max_size=100):
            cache = {}
            access_order = []
            
            def cache_func(key, value=None):
                if value is None:
                    # 获取缓存
                    if key in cache:
                        access_order.remove(key)
                        access_order.append(key)
                        print(f"    缓存命中: {key}")
                        return cache[key]
                    else:
                        print(f"    缓存未命中: {key}")
                        return None
                else:
                    # 设置缓存
                    if len(cache) >= max_size and key not in cache:
                        # 移除最久未使用的项
                        oldest_key = access_order.pop(0)
                        del cache[oldest_key]
                        print(f"    缓存满，移除: {oldest_key}")
                    
                    cache[key] = value
                    if key in access_order:
                        access_order.remove(key)
                    access_order.append(key)
                    print(f"    缓存设置: {key} = {value}")
                    return value
            
            cache_func.get_stats = lambda: f"缓存大小: {len(cache)}/{max_size}"
            return cache_func
        
        # 注册插件
        logger = create_logger_plugin('DEBUG')
        cache = create_cache_plugin(3)
        
        pm.register_plugin('logger', logger)
        pm.register_plugin('cache', cache)
        
        # 注册钩子
        pm.register_hook('before_request', lambda req: print(f"    请求前处理: {req}"))
        pm.register_hook('after_request', lambda resp: print(f"    请求后处理: {resp}"))
        
        # 测试插件系统
        print("\n  测试插件系统:")
        
        # 测试日志插件
        pm.execute_plugin('logger', '系统启动', 'INFO')
        pm.execute_plugin('logger', '调试信息', 'DEBUG')
        
        # 测试缓存插件
        pm.execute_plugin('cache', 'user:1', {'name': 'Alice', 'age': 30})
        pm.execute_plugin('cache', 'user:2', {'name': 'Bob', 'age': 25})
        user1 = pm.execute_plugin('cache', 'user:1')
        print(f"    获取用户1: {user1}")
        
        # 测试钩子
        pm.trigger_hooks('before_request', 'GET /api/users')
        pm.trigger_hooks('after_request', '200 OK')
        
        print(f"    {pm.execute_plugin('cache').get_stats()}")
    
    def create_configuration_system():
        """创建基于作用域的配置系统"""
        print("\n2. 配置系统实现:")
        
        class ConfigManager:
            def __init__(self):
                self._configs = {}
                self._defaults = {}
                self._validators = {}
            
            def set_default(self, key, value, validator=None):
                """设置默认配置"""
                self._defaults[key] = value
                if validator:
                    self._validators[key] = validator
                print(f"  设置默认配置: {key} = {value}")
            
            def set_config(self, key, value):
                """设置配置值"""
                if key in self._validators:
                    if not self._validators[key](value):
                        raise ValueError(f"配置值 {value} 不符合验证规则")
                
                self._configs[key] = value
                print(f"  设置配置: {key} = {value}")
            
            def get_config(self, key, default=None):
                """获取配置值（按优先级：用户配置 > 默认配置 > 参数默认值）"""
                if key in self._configs:
                    return self._configs[key]
                elif key in self._defaults:
                    return self._defaults[key]
                else:
                    return default
            
            def create_scoped_config(self, scope_name):
                """创建作用域配置（利用闭包）"""
                scoped_configs = {}
                
                def scoped_get(key, default=None):
                    # 查找顺序：作用域配置 > 全局配置 > 默认配置
                    if key in scoped_configs:
                        return scoped_configs[key]
                    else:
                        return self.get_config(key, default)
                
                def scoped_set(key, value):
                    if key in self._validators:
                        if not self._validators[key](value):
                            raise ValueError(f"配置值 {value} 不符合验证规则")
                    scoped_configs[key] = value
                    print(f"  设置作用域配置 [{scope_name}]: {key} = {value}")
                
                def scoped_info():
                    return {
                        'scope': scope_name,
                        'scoped_configs': scoped_configs.copy(),
                        'available_globals': list(self._configs.keys()),
                        'defaults': list(self._defaults.keys())
                    }
                
                return {
                    'get': scoped_get,
                    'set': scoped_set,
                    'info': scoped_info
                }
        
        # 创建配置管理器
        config_mgr = ConfigManager()
        
        # 设置默认配置和验证器
        config_mgr.set_default('debug', False, lambda x: isinstance(x, bool))
        config_mgr.set_default('max_connections', 100, lambda x: isinstance(x, int) and x > 0)
        config_mgr.set_default('timeout', 30.0, lambda x: isinstance(x, (int, float)) and x > 0)
        
        # 设置全局配置
        config_mgr.set_config('debug', True)
        config_mgr.set_config('app_name', 'MyApp')
        
        # 创建不同作用域的配置
        db_config = config_mgr.create_scoped_config('database')
        api_config = config_mgr.create_scoped_config('api')
        
        # 设置作用域特定的配置
        db_config['set']('max_connections', 50)
        db_config['set']('timeout', 60.0)
        
        api_config['set']('timeout', 10.0)
        api_config['set']('rate_limit', 1000)
        
        # 测试配置查找
        print("\n  测试配置查找:")
        print(f"    全局debug: {config_mgr.get_config('debug')}")
        print(f"    数据库debug: {db_config['get']('debug')}")
        print(f"    数据库max_connections: {db_config['get']('max_connections')}")
        print(f"    API timeout: {api_config['get']('timeout')}")
        print(f"    API max_connections: {api_config['get']('max_connections')}")
        
        # 显示配置信息
        print(f"\n  数据库配置信息: {db_config['info']()}")
        print(f"  API配置信息: {api_config['info']()}")
    
    def create_state_machine():
        """创建基于作用域的状态机"""
        print("\n3. 状态机实现:")
        
        def create_finite_state_machine(initial_state, states, transitions):
            """创建有限状态机"""
            current_state = initial_state
            state_history = [initial_state]
            
            def get_current_state():
                return current_state
            
            def get_history():
                return state_history.copy()
            
            def transition(event):
                nonlocal current_state
                
                if current_state in transitions and event in transitions[current_state]:
                    new_state = transitions[current_state][event]
                    print(f"    状态转换: {current_state} --{event}--> {new_state}")
                    current_state = new_state
                    state_history.append(new_state)
                    
                    # 执行状态进入动作
                    if new_state in states and 'on_enter' in states[new_state]:
                        states[new_state]['on_enter']()
                    
                    return True
                else:
                    print(f"    无效转换: {current_state} --{event}--> ???")
                    return False
            
            def can_transition(event):
                return (current_state in transitions and 
                       event in transitions[current_state])
            
            def get_available_events():
                return list(transitions.get(current_state, {}).keys())
            
            # 执行初始状态的进入动作
            if initial_state in states and 'on_enter' in states[initial_state]:
                states[initial_state]['on_enter']()
            
            return {
                'get_state': get_current_state,
                'transition': transition,
                'can_transition': can_transition,
                'get_available_events': get_available_events,
                'get_history': get_history
            }
        
        # 定义订单状态机
        order_states = {
            'pending': {
                'on_enter': lambda: print("      进入待处理状态")
            },
            'processing': {
                'on_enter': lambda: print("      进入处理中状态")
            },
            'shipped': {
                'on_enter': lambda: print("      进入已发货状态")
            },
            'delivered': {
                'on_enter': lambda: print("      进入已送达状态")
            },
            'cancelled': {
                'on_enter': lambda: print("      进入已取消状态")
            }
        }
        
        order_transitions = {
            'pending': {
                'confirm': 'processing',
                'cancel': 'cancelled'
            },
            'processing': {
                'ship': 'shipped',
                'cancel': 'cancelled'
            },
            'shipped': {
                'deliver': 'delivered'
            }
        }
        
        # 创建订单状态机
        order_fsm = create_finite_state_machine('pending', order_states, order_transitions)
        
        # 测试状态机
        print("  测试订单状态机:")
        print(f"    初始状态: {order_fsm['get_state']()}")
        print(f"    可用事件: {order_fsm['get_available_events']()}")
        
        # 执行状态转换
        events = ['confirm', 'ship', 'deliver', 'cancel']  # 最后一个应该失败
        
        for event in events:
            if order_fsm['can_transition'](event):
                order_fsm['transition'](event)
            else:
                print(f"    无法执行事件: {event}")
            
            print(f"    当前状态: {order_fsm['get_state']()}")
            print(f"    可用事件: {order_fsm['get_available_events']()}")
        
        print(f"    状态历史: {' -> '.join(order_fsm['get_history']())}")
    
    # 执行所有实际应用演示
    create_plugin_system()
    create_configuration_system()
    create_state_machine()
    
    print("\n解析：")
    print("- 作用域知识在实际项目中有广泛应用")
    print("- 闭包可以用来创建有状态的函数和对象")
    print("- 合理的作用域设计可以提高代码的模块化程度")
    print("- 理解作用域有助于设计更好的API和架构")

def main():
    """
    主函数：执行所有练习
    """
    print("Python 函数作用域综合练习")
    print("=" * 60)
    
    # 基础练习
    exercise_1_basic_scopes()
    exercise_2_variable_shadowing()
    exercise_3_builtin_shadowing()
    
    # 进阶练习
    exercise_4_legb_resolution()
    exercise_5_global_nonlocal()
    exercise_6_unbound_local_error()
    
    # 高级练习
    exercise_7_closure_applications()
    exercise_8_decorator_with_scope()
    
    # 挑战练习
    exercise_9_scope_performance()
    exercise_10_advanced_debugging()
    exercise_11_real_world_applications()
    
    print("\n" + "=" * 60)
    print("练习总结")
    print("=" * 60)
    
    print("\n🎯 学习成果:")
    print("1. ✅ 掌握了Python作用域的基本概念")
    print("2. ✅ 理解了LEGB规则的工作原理")
    print("3. ✅ 学会了使用global和nonlocal关键字")
    print("4. ✅ 掌握了闭包和装饰器的高级应用")
    print("5. ✅ 了解了作用域相关的性能优化技巧")
    print("6. ✅ 学会了调试作用域相关问题的方法")
    print("7. ✅ 能够在实际项目中应用作用域知识")
    
    print("\n🚀 进阶方向:")
    print("- 深入学习装饰器的高级用法")
    print("- 研究元类和描述符中的作用域")
    print("- 探索异步编程中的作用域问题")
    print("- 学习函数式编程的作用域概念")
    
    print("\n💡 最佳实践提醒:")
    print("- 避免使用内置函数名作为变量名")
    print("- 在循环中缓存频繁访问的全局变量")
    print("- 合理使用闭包，避免内存泄漏")
    print("- 定期检查和清理作用域污染")
    print("- 使用工具辅助调试作用域问题")

if __name__ == "__main__":
    main()
```

## 学习要点

### 核心概念掌握
1. **作用域层次理解**：深入理解L-E-G-B四个作用域层次
2. **变量查找机制**：掌握Python变量查找的完整过程
3. **作用域修改**：熟练使用global和nonlocal关键字
4. **闭包应用**：理解闭包的工作原理和实际应用

### 实践技能
1. **调试技巧**：学会使用各种工具调试作用域问题
2. **性能优化**：掌握基于作用域的性能优化方法
3. **设计模式**：能够设计基于作用域的软件架构
4. **最佳实践**：遵循作用域相关的编程最佳实践

## 运行示例

在终端中运行练习代码：

```bash
# 运行完整的综合练习
python3 15-function-scope/08_exercises.py

# 或者在Python交互环境中逐个测试
python3
>>> exec(open('15-function-scope/08_exercises.py').read())
```

预期输出将包括：
- 各种作用域概念的演示
- LEGB规则的详细分析
- 闭包和装饰器的实际应用
- 性能测试和优化建议
- 调试技巧的演示
- 实际项目应用场景

## 注意事项

### 常见错误
1. **UnboundLocalError**：在函数中修改全局变量前忘记声明
2. **变量遮蔽**：意外遮蔽内置函数或重要变量
3. **闭包陷阱**：循环中创建闭包时的变量绑定问题
4. **作用域污染**：全局命名空间被不必要的变量污染

### 最佳实践
1. **命名规范**：避免使用内置函数名作为变量名
2. **性能考虑**：在循环中缓存频繁访问的全局变量
3. **内存管理**：合理使用闭包，避免循环引用
4. **代码组织**：保持清晰的作用域层次结构

### 调试建议
1. 使用`locals()`和`globals()`函数检查当前作用域
2. 利用`inspect`模块分析复杂的作用域链
3. 通过IDE的调试器观察变量的作用域
4. 编写单元测试验证作用域行为

## 扩展练习

### 进阶挑战
1. **实现一个简单的模板引擎**，利用作用域管理变量
2. **创建一个配置管理系统**，支持多层级的配置覆盖
3. **设计一个插件架构**，使用闭包实现插件隔离
4. **开发一个简单的DSL解释器**，处理变量作用域

### 性能优化项目
1. 分析现有代码中的作用域性能瓶颈
2. 实现基于作用域的缓存策略
3. 优化大型项目中的全局变量访问
4. 设计高效的变量查找算法

## 下一步学习

### 相关主题
1. **装饰器高级应用** → 学习更复杂的装饰器模式
2. **元编程** → 了解元类和描述符中的作用域
3. **异步编程** → 探索async/await中的作用域问题
4. **函数式编程** → 学习函数式编程的作用域概念

### 推荐资源
1. Python官方文档：执行模型和作用域
2. 《Fluent Python》：闭包和装饰器章节
3. 《Effective Python》：作用域相关的最佳实践
4. 在线调试工具：Python Tutor可视化作用域

### 实践项目
1. 开发一个基于作用域的权限管理系统
2. 实现一个支持嵌套作用域的配置文件解析器
3. 创建一个利用闭包的事件系统
4. 设计一个基于作用域的缓存框架

通过这些综合练习，你将全面掌握Python函数作用域的各个方面，为进一步学习高级Python特性打下坚实基础。