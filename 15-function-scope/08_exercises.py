#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
函数作用域综合练习 (Function Scope Comprehensive Exercises)

本文件包含各种难度的函数作用域练习题，帮助巩固和深化理解。

练习内容：
1. 基础作用域练习
2. LEGB规则应用
3. 闭包和嵌套函数
4. 作用域修改练习
5. 实际应用场景
6. 调试和错误修复
7. 高级应用练习
"""

# 全局变量（用于练习）
global_counter = 0
global_message = "全局消息"

# ==================== 基础练习 ====================

def exercise_1_basic_scope():
    """
    练习1：基础作用域理解
    
    任务：预测下面代码的输出，然后运行验证
    """
    print("=== 练习1：基础作用域理解 ===")
    
    x = "全局x"
    
    def outer():
        x = "外层x"
        print(f"外层函数中的x: {x}")
        
        def inner():
            x = "内层x"
            print(f"内层函数中的x: {x}")
        
        inner()
        print(f"调用inner后，外层x: {x}")
    
    print(f"调用outer前，全局x: {x}")
    outer()
    print(f"调用outer后，全局x: {x}")
    
    # 思考题：为什么每个函数中的x都不同？
    print("\n思考：每个作用域的x都是独立的，互不影响")

def exercise_2_variable_lookup():
    """
    练习2：变量查找顺序
    
    任务：分析变量查找的LEGB顺序
    """
    print("\n=== 练习2：变量查找顺序 ===")
    
    # 请预测每个print语句的输出
    builtin_name = "全局的len"  # 遮蔽内置的len
    
    def test_lookup():
        enclosing_name = "外层变量"
        
        def inner_test():
            local_name = "局部变量"
            
            # 这些变量分别来自哪个作用域？
            print(f"local_name: {local_name}")  # L - Local
            print(f"enclosing_name: {enclosing_name}")  # E - Enclosing
            print(f"global_message: {global_message}")  # G - Global
            print(f"abs: {abs}")  # B - Built-in
            
            # 这个会访问哪个？
            print(f"builtin_name: {builtin_name}")  # G - Global (遮蔽了内置)
        
        inner_test()
    
    test_lookup()

# ==================== LEGB规则练习 ====================

def exercise_3_legb_challenge():
    """
    练习3：LEGB规则挑战
    
    任务：完成函数，使其按照LEGB规则正确查找变量
    """
    print("\n=== 练习3：LEGB规则挑战 ===")
    
    def create_legb_demo(global_val):
        """创建一个演示LEGB规则的函数"""
        
        enclosing_val = f"enclosing_{global_val}"
        
        def middle_function(middle_param):
            middle_val = f"middle_{middle_param}"
            
            def inner_function(local_param):
                local_val = f"local_{local_param}"
                
                # TODO: 创建一个字典，包含从不同作用域获取的值
                # 提示：使用LEGB顺序
                result = {
                    'local': local_val,
                    'enclosing': enclosing_val,
                    'middle': middle_val,
                    'global': global_val,
                    'builtin': str  # 内置类型
                }
                
                return result
            
            return inner_function
        
        return middle_function
    
    # 测试LEGB演示
    demo_func = create_legb_demo("global_value")
    middle_func = demo_func("middle_param")
    result = middle_func("local_param")
    
    print("LEGB演示结果:")
    for scope, value in result.items():
        print(f"  {scope}: {value}")

def exercise_4_scope_modification():
    """
    练习4：作用域修改练习
    
    任务：正确使用global和nonlocal关键字
    """
    print("\n=== 练习4：作用域修改练习 ===")
    
    # 全局计数器
    global global_counter
    
    def create_counter():
        """创建一个计数器函数"""
        count = 0
        
        def increment(step=1):
            # TODO: 修改外层的count变量
            nonlocal count
            count += step
            
            # TODO: 同时修改全局计数器
            global global_counter
            global_counter += step
            
            return count
        
        def get_count():
            return count
        
        def reset():
            # TODO: 重置局部计数器
            nonlocal count
            count = 0
        
        return increment, get_count, reset
    
    # 测试计数器
    inc1, get1, reset1 = create_counter()
    inc2, get2, reset2 = create_counter()
    
    print(f"初始状态 - 全局计数器: {global_counter}")
    
    print(f"计数器1增加5: {inc1(5)}")
    print(f"计数器2增加3: {inc2(3)}")
    print(f"计数器1当前值: {get1()}")
    print(f"计数器2当前值: {get2()}")
    print(f"全局计数器: {global_counter}")
    
    reset1()
    print(f"重置计数器1后: {get1()}")
    print(f"全局计数器: {global_counter}")

# ==================== 闭包练习 ====================

def exercise_5_closure_practice():
    """
    练习5：闭包实践
    
    任务：创建实用的闭包函数
    """
    print("\n=== 练习5：闭包实践 ===")
    
    def create_accumulator(initial_value=0):
        """
        TODO: 创建一个累加器闭包
        
        要求：
        1. 返回一个函数，可以累加数值
        2. 支持获取当前总和
        3. 支持重置功能
        """
        total = initial_value
        
        def accumulator(value=None, action='add'):
            nonlocal total
            
            if action == 'add' and value is not None:
                total += value
                return total
            elif action == 'get':
                return total
            elif action == 'reset':
                total = initial_value
                return total
            else:
                return total
        
        return accumulator
    
    def create_multiplier_factory():
        """
        TODO: 创建乘法器工厂
        
        要求：
        1. 返回一个函数，该函数可以创建不同倍数的乘法器
        2. 每个乘法器记住自己的倍数
        """
        def make_multiplier(factor):
            def multiply(value):
                return value * factor
            
            # 添加一些元信息
            multiply.factor = factor
            multiply.__name__ = f'multiply_by_{factor}'
            
            return multiply
        
        return make_multiplier
    
    # 测试累加器
    acc1 = create_accumulator(10)
    acc2 = create_accumulator()
    
    print("累加器测试:")
    print(f"acc1初始值: {acc1(action='get')}")
    print(f"acc1加5: {acc1(5)}")
    print(f"acc1加3: {acc1(3)}")
    print(f"acc2加10: {acc2(10)}")
    print(f"acc1当前值: {acc1(action='get')}")
    print(f"acc2当前值: {acc2(action='get')}")
    
    # 测试乘法器工厂
    multiplier_factory = create_multiplier_factory()
    
    double = multiplier_factory(2)
    triple = multiplier_factory(3)
    
    print("\n乘法器测试:")
    print(f"double(5): {double(5)}")
    print(f"triple(5): {triple(5)}")
    print(f"double的倍数: {double.factor}")
    print(f"triple的名称: {triple.__name__}")

def exercise_6_closure_loops():
    """
    练习6：闭包与循环
    
    任务：解决闭包在循环中的常见问题
    """
    print("\n=== 练习6：闭包与循环 ===")
    
    # 问题演示：错误的闭包创建
    print("问题演示 - 错误的闭包:")
    functions_wrong = []
    for i in range(5):
        functions_wrong.append(lambda: i)  # 所有函数都引用同一个i
    
    for j, func in enumerate(functions_wrong):
        print(f"  函数{j}返回: {func()}")
    
    # TODO: 修复上面的问题
    print("\n修复方案1 - 使用默认参数:")
    functions_fixed1 = []
    for i in range(5):
        functions_fixed1.append(lambda x=i: x)
    
    for j, func in enumerate(functions_fixed1):
        print(f"  函数{j}返回: {func()}")
    
    # TODO: 使用另一种修复方案
    print("\n修复方案2 - 使用闭包工厂:")
    def make_function(value):
        return lambda: value
    
    functions_fixed2 = []
    for i in range(5):
        functions_fixed2.append(make_function(i))
    
    for j, func in enumerate(functions_fixed2):
        print(f"  函数{j}返回: {func()}")
    
    # TODO: 创建一个更复杂的例子
    print("\n复杂示例 - 操作函数列表:")
    operations = []
    
    for op_name, op_func in [('add', lambda x, y: x + y), 
                            ('mul', lambda x, y: x * y),
                            ('sub', lambda x, y: x - y)]:
        # 创建带有操作名称的闭包
        def make_operation(name, func):
            def operation(a, b):
                result = func(a, b)
                print(f"  {name}({a}, {b}) = {result}")
                return result
            operation.__name__ = name
            return operation
        
        operations.append(make_operation(op_name, op_func))
    
    # 测试操作函数
    for op in operations:
        op(10, 3)

# ==================== 实际应用练习 ====================

def exercise_7_decorator_scopes():
    """
    练习7：装饰器中的作用域
    
    任务：创建使用作用域的装饰器
    """
    print("\n=== 练习7：装饰器中的作用域 ===")
    
    def create_cache_decorator():
        """
        TODO: 创建一个缓存装饰器
        
        要求：
        1. 缓存函数调用结果
        2. 支持查看缓存统计
        3. 支持清除缓存
        """
        def cache_decorator(func):
            cache = {}  # 每个被装饰的函数都有自己的缓存
            stats = {'hits': 0, 'misses': 0}
            
            def wrapper(*args, **kwargs):
                # 创建缓存键
                key = str(args) + str(sorted(kwargs.items()))
                
                if key in cache:
                    stats['hits'] += 1
                    print(f"  缓存命中: {func.__name__}{args}")
                    return cache[key]
                else:
                    stats['misses'] += 1
                    print(f"  缓存未命中: {func.__name__}{args}")
                    result = func(*args, **kwargs)
                    cache[key] = result
                    return result
            
            def get_stats():
                return stats.copy()
            
            def clear_cache():
                nonlocal cache, stats
                cache.clear()
                stats = {'hits': 0, 'misses': 0}
            
            # 添加额外方法
            wrapper.get_stats = get_stats
            wrapper.clear_cache = clear_cache
            wrapper.__name__ = func.__name__
            
            return wrapper
        
        return cache_decorator
    
    # 使用缓存装饰器
    cache = create_cache_decorator()
    
    @cache
    def fibonacci(n):
        """计算斐波那契数列"""
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    @cache
    def factorial(n):
        """计算阶乘"""
        if n <= 1:
            return 1
        return n * factorial(n-1)
    
    # 测试缓存装饰器
    print("斐波那契数列测试:")
    print(f"fibonacci(5) = {fibonacci(5)}")
    print(f"fibonacci(5) = {fibonacci(5)}")
    print(f"fibonacci统计: {fibonacci.get_stats()}")
    
    print("\n阶乘测试:")
    print(f"factorial(5) = {factorial(5)}")
    print(f"factorial(4) = {factorial(4)}")
    print(f"factorial统计: {factorial.get_stats()}")

def exercise_8_state_machine():
    """
    练习8：状态机实现
    
    任务：使用闭包实现简单的状态机
    """
    print("\n=== 练习8：状态机实现 ===")
    
    def create_traffic_light():
        """
        TODO: 创建交通灯状态机
        
        状态：红灯 -> 绿灯 -> 黄灯 -> 红灯
        """
        states = ['红灯', '绿灯', '黄灯']
        current_state = 0
        transition_count = 0
        
        def next_state():
            nonlocal current_state, transition_count
            current_state = (current_state + 1) % len(states)
            transition_count += 1
            return states[current_state]
        
        def get_current_state():
            return states[current_state]
        
        def get_stats():
            return {
                'current': states[current_state],
                'transitions': transition_count
            }
        
        def reset():
            nonlocal current_state, transition_count
            current_state = 0
            transition_count = 0
        
        # 返回控制接口
        return {
            'next': next_state,
            'current': get_current_state,
            'stats': get_stats,
            'reset': reset
        }
    
    def create_counter_machine(max_count=10):
        """
        TODO: 创建计数器状态机
        
        状态：计数中、已满、已重置
        """
        count = 0
        state = '计数中'
        
        def increment():
            nonlocal count, state
            if state == '已满':
                return f"无法增加，当前状态：{state}"
            
            count += 1
            if count >= max_count:
                state = '已满'
            
            return f"计数：{count}，状态：{state}"
        
        def reset():
            nonlocal count, state
            count = 0
            state = '已重置'
            return f"已重置，状态：{state}"
        
        def resume():
            nonlocal state
            if state == '已重置':
                state = '计数中'
            return f"状态：{state}"
        
        def get_info():
            return {
                'count': count,
                'max_count': max_count,
                'state': state
            }
        
        return {
            'increment': increment,
            'reset': reset,
            'resume': resume,
            'info': get_info
        }
    
    # 测试交通灯
    traffic_light = create_traffic_light()
    
    print("交通灯测试:")
    print(f"初始状态: {traffic_light['current']()}")
    
    for i in range(5):
        next_light = traffic_light['next']()
        print(f"切换{i+1}: {next_light}")
    
    print(f"统计信息: {traffic_light['stats']()}")
    
    # 测试计数器
    counter = create_counter_machine(3)
    
    print("\n计数器测试:")
    print(f"初始信息: {counter['info']()}")
    
    for i in range(5):
        result = counter['increment']()
        print(f"增加{i+1}: {result}")
    
    print(f"重置: {counter['reset']()}")
    print(f"恢复: {counter['resume']()}")
    print(f"增加: {counter['increment']()}")

# ==================== 调试练习 ====================

def exercise_9_debug_scope_issues():
    """
    练习9：调试作用域问题
    
    任务：找出并修复作用域相关的错误
    """
    print("\n=== 练习9：调试作用域问题 ===")
    
    # 问题1：UnboundLocalError
    def buggy_function_1():
        """这个函数有作用域错误，请修复"""
        count = 0
        
        def increment():
            # TODO: 修复这个错误
            # count = count + 1  # UnboundLocalError
            nonlocal count
            count = count + 1
            return count
        
        return increment
    
    # 问题2：意外的全局变量修改
    debug_global = "原始值"
    
    def buggy_function_2():
        """这个函数意外修改了全局变量"""
        debug_global = "局部值"  # 本意是创建局部变量
        
        def inner():
            global debug_global  # 错误：这会修改全局变量
            debug_global = "被修改的值"
        
        def inner_fixed():
            nonlocal debug_global  # 正确：修改外层局部变量
            debug_global = "正确修改的值"
        
        print(f"修改前 - 局部: {debug_global}, 全局: {globals().get('debug_global', '未定义')}")
        
        inner()  # 错误的修改
        print(f"错误修改后 - 局部: {debug_global}, 全局: {globals()['debug_global']}")
        
        inner_fixed()  # 正确的修改
        print(f"正确修改后 - 局部: {debug_global}, 全局: {globals()['debug_global']}")
    
    # 问题3：闭包变量捕获问题
    def buggy_function_3():
        """闭包变量捕获问题"""
        functions = []
        
        # 错误的方式
        for i in range(3):
            functions.append(lambda: f"错误捕获: {i}")
        
        # 正确的方式
        functions_fixed = []
        for i in range(3):
            functions_fixed.append(lambda x=i: f"正确捕获: {x}")
        
        print("闭包捕获问题演示:")
        for j, func in enumerate(functions):
            print(f"  错误函数{j}: {func()}")
        
        for j, func in enumerate(functions_fixed):
            print(f"  正确函数{j}: {func()}")
    
    # 测试修复后的函数
    print("测试修复后的函数:")
    
    inc = buggy_function_1()
    print(f"计数器测试: {inc()}, {inc()}, {inc()}")
    
    print("\n全局变量修改测试:")
    buggy_function_2()
    
    print("\n闭包捕获测试:")
    buggy_function_3()

# ==================== 高级练习 ====================

def exercise_10_advanced_applications():
    """
    练习10：高级应用
    
    任务：实现复杂的作用域应用
    """
    print("\n=== 练习10：高级应用 ===")
    
    def create_namespace():
        """
        TODO: 创建一个命名空间系统
        
        要求：
        1. 支持嵌套命名空间
        2. 支持变量查找和设置
        3. 支持作用域链查找
        """
        def namespace_factory(parent=None):
            variables = {}
            children = {}
            
            def get_variable(name):
                # 在当前命名空间查找
                if name in variables:
                    return variables[name]
                # 在父命名空间查找
                elif parent is not None:
                    return parent['get'](name)
                else:
                    raise NameError(f"变量 '{name}' 未定义")
            
            def set_variable(name, value):
                variables[name] = value
            
            def create_child(child_name):
                if child_name not in children:
                    child_ns = namespace_factory({
                        'get': get_variable,
                        'set': set_variable,
                        'child': lambda n: children[n] if n in children else None
                    })
                    children[child_name] = child_ns
                return children[child_name]
            
            def list_variables():
                return variables.copy()
            
            def get_child(child_name):
                return children.get(child_name)
            
            return {
                'get': get_variable,
                'set': set_variable,
                'child': create_child,
                'get_child': get_child,
                'list': list_variables
            }
        
        return namespace_factory()
    
    def create_function_registry():
        """
        TODO: 创建函数注册系统
        
        要求：
        1. 支持函数注册和调用
        2. 支持中间件
        3. 支持作用域隔离
        """
        functions = {}
        middlewares = []
        
        def register(name):
            def decorator(func):
                def wrapper(*args, **kwargs):
                    # 执行前置中间件
                    context = {'name': name, 'args': args, 'kwargs': kwargs}
                    
                    for middleware in middlewares:
                        if hasattr(middleware, 'before'):
                            middleware.before(context)
                    
                    # 执行函数
                    try:
                        result = func(*args, **kwargs)
                        context['result'] = result
                        
                        # 执行后置中间件
                        for middleware in reversed(middlewares):
                            if hasattr(middleware, 'after'):
                                middleware.after(context)
                        
                        return result
                    
                    except Exception as e:
                        context['error'] = e
                        
                        # 执行错误中间件
                        for middleware in reversed(middlewares):
                            if hasattr(middleware, 'error'):
                                middleware.error(context)
                        
                        raise
                
                functions[name] = wrapper
                wrapper.__name__ = name
                return wrapper
            
            return decorator
        
        def add_middleware(middleware):
            middlewares.append(middleware)
        
        def call_function(name, *args, **kwargs):
            if name in functions:
                return functions[name](*args, **kwargs)
            else:
                raise NameError(f"函数 '{name}' 未注册")
        
        def list_functions():
            return list(functions.keys())
        
        return {
            'register': register,
            'call': call_function,
            'middleware': add_middleware,
            'list': list_functions
        }
    
    # 测试命名空间系统
    print("命名空间系统测试:")
    
    root_ns = create_namespace()
    root_ns['set']('global_var', '全局变量')
    
    app_ns = root_ns['child']('app')
    app_ns['set']('app_var', '应用变量')
    
    module_ns = app_ns['child']('module')
    module_ns['set']('module_var', '模块变量')
    
    print(f"模块中访问全局变量: {module_ns['get']('global_var')}")
    print(f"模块中访问应用变量: {module_ns['get']('app_var')}")
    print(f"模块中访问模块变量: {module_ns['get']('module_var')}")
    
    # 测试函数注册系统
    print("\n函数注册系统测试:")
    
    registry = create_function_registry()
    
    # 创建日志中间件
    class LogMiddleware:
        def before(self, context):
            print(f"  调用函数: {context['name']}{context['args']}")
        
        def after(self, context):
            print(f"  函数返回: {context.get('result')}")
        
        def error(self, context):
            print(f"  函数错误: {context.get('error')}")
    
    registry['middleware'](LogMiddleware())
    
    # 注册函数
    @registry['register']('add')
    def add_numbers(a, b):
        return a + b
    
    @registry['register']('divide')
    def divide_numbers(a, b):
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b
    
    # 测试函数调用
    print(f"注册的函数: {registry['list']()}")
    
    result1 = registry['call']('add', 5, 3)
    print(f"add(5, 3) = {result1}")
    
    try:
        result2 = registry['call']('divide', 10, 0)
    except ValueError as e:
        print(f"divide(10, 0) 出错: {e}")

# ==================== 主程序 ====================

def run_all_exercises():
    """运行所有练习"""
    print("Python函数作用域综合练习")
    print("=" * 60)
    
    exercises = [
        exercise_1_basic_scope,
        exercise_2_variable_lookup,
        exercise_3_legb_challenge,
        exercise_4_scope_modification,
        exercise_5_closure_practice,
        exercise_6_closure_loops,
        exercise_7_decorator_scopes,
        exercise_8_state_machine,
        exercise_9_debug_scope_issues,
        exercise_10_advanced_applications
    ]
    
    for i, exercise in enumerate(exercises, 1):
        try:
            exercise()
            print(f"\n{'='*20} 练习{i}完成 {'='*20}")
        except Exception as e:
            print(f"\n练习{i}执行出错: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n=== 练习总结 ===")
    print("1. 掌握了基础的作用域概念和LEGB规则")
    print("2. 学会了使用global和nonlocal关键字")
    print("3. 理解了闭包的工作原理和应用场景")
    print("4. 学会了调试作用域相关的问题")
    print("5. 实践了作用域在实际项目中的应用")
    print("6. 掌握了高级的作用域应用技巧")
    
    print("\n=== 学习建议 ===")
    print("1. 多练习不同层次的嵌套函数")
    print("2. 理解闭包的内存模型")
    print("3. 在实际项目中应用这些概念")
    print("4. 学习其他语言的作用域机制进行对比")
    print("5. 深入理解Python的内存管理")

if __name__ == "__main__":
    run_all_exercises()