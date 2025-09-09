#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
嵌套作用域 (Enclosing Scope)

嵌套作用域是指在函数内部定义的函数可以访问外层函数的变量。
这是Python作用域链中的重要组成部分，也是闭包实现的基础。

学习目标：
1. 理解嵌套作用域的概念
2. 掌握嵌套函数的变量访问规则
3. 了解闭包的形成机制
4. 理解嵌套作用域在实际编程中的应用
"""

# 1. 基本的嵌套作用域
def basic_enclosing_scope():
    """演示基本的嵌套作用域"""
    print("=== 基本嵌套作用域 ===")
    
    # 外层函数的变量
    outer_var = "外层变量"
    outer_number = 100
    
    def inner_function():
        # 内层函数可以直接访问外层变量
        print(f"内层函数访问外层变量: {outer_var}")
        print(f"内层函数访问外层数字: {outer_number}")
        
        # 内层函数的局部变量
        inner_var = "内层变量"
        print(f"内层函数的局部变量: {inner_var}")
    
    print(f"外层函数的变量: {outer_var}")
    inner_function()
    # print(inner_var)  # 错误：外层函数无法访问内层变量

# 2. 多层嵌套作用域
def multilevel_enclosing_scope():
    """演示多层嵌套作用域"""
    print("\n=== 多层嵌套作用域 ===")
    
    level1_var = "第1层变量"
    
    def level2_function():
        level2_var = "第2层变量"
        
        def level3_function():
            level3_var = "第3层变量"
            
            def level4_function():
                # 第4层可以访问所有外层变量
                print(f"第4层访问第1层: {level1_var}")
                print(f"第4层访问第2层: {level2_var}")
                print(f"第4层访问第3层: {level3_var}")
                
                level4_var = "第4层变量"
                print(f"第4层自己的变量: {level4_var}")
            
            print(f"第3层访问第1层: {level1_var}")
            print(f"第3层访问第2层: {level2_var}")
            level4_function()
        
        print(f"第2层访问第1层: {level1_var}")
        level3_function()
    
    level2_function()

# 3. 嵌套作用域中的变量遮蔽
def variable_shadowing():
    """演示嵌套作用域中的变量遮蔽"""
    print("\n=== 变量遮蔽 ===")
    
    name = "外层的name"
    value = 100
    
    def inner_function():
        # 内层定义同名变量，会遮蔽外层变量
        name = "内层的name"
        print(f"内层函数中的name: {name}")  # 访问内层的name
        print(f"内层函数中的value: {value}")  # 访问外层的value
        
        def deeper_function():
            # 更深层的函数
            name = "更深层的name"
            print(f"更深层函数中的name: {name}")
            print(f"更深层函数中的value: {value}")
        
        deeper_function()
        print(f"回到内层函数的name: {name}")
    
    print(f"外层函数的name: {name}")
    inner_function()
    print(f"外层函数的name仍然是: {name}")

# 4. 闭包的形成
def create_closure():
    """演示闭包的形成"""
    print("\n=== 闭包的形成 ===")
    
    def outer_function(x):
        # 外层函数的参数和变量
        outer_var = f"外层变量: {x}"
        
        def inner_function(y):
            # 内层函数访问外层变量，形成闭包
            result = f"{outer_var} + 内层参数: {y}"
            return result
        
        # 返回内层函数（闭包）
        return inner_function
    
    # 创建闭包
    closure1 = outer_function("Hello")
    closure2 = outer_function("World")
    
    # 调用闭包
    print(closure1("Python"))
    print(closure2("Programming"))
    
    # 每个闭包都保持着自己的外层变量
    print("两个闭包是不同的对象:", closure1 is closure2)

# 5. 闭包中的变量绑定
def closure_variable_binding():
    """演示闭包中的变量绑定"""
    print("\n=== 闭包变量绑定 ===")
    
    # 常见的陷阱：循环中创建闭包
    functions = []
    
    # 错误的方式
    print("错误的闭包创建方式:")
    for i in range(3):
        def func():
            return i  # 所有闭包都引用同一个i
        functions.append(func)
    
    # 调用闭包
    for f in functions:
        print(f"函数返回: {f()}")  # 都返回2（循环结束时i的值）
    
    # 正确的方式1：使用默认参数
    print("\n正确方式1 - 使用默认参数:")
    functions_correct1 = []
    for i in range(3):
        def func(x=i):  # 使用默认参数捕获当前的i值
            return x
        functions_correct1.append(func)
    
    for f in functions_correct1:
        print(f"函数返回: {f()}")
    
    # 正确的方式2：使用额外的函数
    print("\n正确方式2 - 使用额外函数:")
    functions_correct2 = []
    for i in range(3):
        def make_func(x):
            def func():
                return x
            return func
        functions_correct2.append(make_func(i))
    
    for f in functions_correct2:
        print(f"函数返回: {f()}")

# 6. 嵌套作用域的实际应用：装饰器
def decorator_with_enclosing_scope():
    """演示装饰器中的嵌套作用域"""
    print("\n=== 装饰器中的嵌套作用域 ===")
    
    def timing_decorator(func):
        import time
        
        def wrapper(*args, **kwargs):
            # wrapper可以访问外层的func参数
            start_time = time.time()
            print(f"开始执行函数: {func.__name__}")
            
            result = func(*args, **kwargs)
            
            end_time = time.time()
            print(f"函数 {func.__name__} 执行时间: {end_time - start_time:.4f}秒")
            return result
        
        return wrapper
    
    @timing_decorator
    def slow_function():
        import time
        time.sleep(0.1)
        return "任务完成"
    
    @timing_decorator
    def calculate(x, y):
        return x * y + x ** y
    
    # 测试装饰器
    result1 = slow_function()
    print(f"结果: {result1}")
    
    result2 = calculate(3, 4)
    print(f"计算结果: {result2}")

# 7. 嵌套作用域与类的结合
def nested_scope_with_class():
    """演示嵌套作用域与类的结合"""
    print("\n=== 嵌套作用域与类 ===")
    
    def create_counter_class(initial_value=0):
        # 外层函数的变量
        default_step = 1
        
        class Counter:
            def __init__(self):
                self.value = initial_value  # 访问外层参数
            
            def increment(self, step=None):
                if step is None:
                    step = default_step  # 访问外层变量
                self.value += step
                return self.value
            
            def get_default_step(self):
                return default_step  # 访问外层变量
        
        return Counter
    
    # 创建不同配置的计数器类
    CounterClass1 = create_counter_class(10)
    CounterClass2 = create_counter_class(100)
    
    # 使用计数器
    counter1 = CounterClass1()
    counter2 = CounterClass2()
    
    print(f"计数器1初始值: {counter1.value}")
    print(f"计数器2初始值: {counter2.value}")
    
    print(f"计数器1递增: {counter1.increment()}")
    print(f"计数器2递增: {counter2.increment()}")
    
    print(f"计数器1默认步长: {counter1.get_default_step()}")
    print(f"计数器2默认步长: {counter2.get_default_step()}")

# 8. 嵌套作用域的性能考虑
def performance_considerations():
    """演示嵌套作用域的性能考虑"""
    print("\n=== 性能考虑 ===")
    
    import time
    
    # 深层嵌套可能影响性能
    def deep_nesting_test():
        var1 = "level1"
        
        def level2():
            var2 = "level2"
            
            def level3():
                var3 = "level3"
                
                def level4():
                    var4 = "level4"
                    
                    def level5():
                        # 访问多层外部变量
                        return f"{var1}-{var2}-{var3}-{var4}-level5"
                    
                    return level5
                
                return level4
            
            return level3
        
        return level2
    
    # 创建深层嵌套函数
    nested_func = deep_nesting_test()()()()()
    
    # 测试性能
    start_time = time.time()
    for _ in range(10000):
        result = nested_func
    end_time = time.time()
    
    print(f"深层嵌套函数结果: {result}")
    print(f"10000次调用耗时: {end_time - start_time:.4f}秒")
    
    # 对比：简单函数
    def simple_function():
        return "simple-result"
    
    start_time = time.time()
    for _ in range(10000):
        result = simple_function()
    end_time = time.time()
    
    print(f"简单函数结果: {result}")
    print(f"10000次调用耗时: {end_time - start_time:.4f}秒")

# 9. 嵌套作用域的调试技巧
def debugging_nested_scope():
    """演示嵌套作用域的调试技巧"""
    print("\n=== 调试技巧 ===")
    
    def outer_function(x):
        outer_var = f"outer: {x}"
        
        def middle_function(y):
            middle_var = f"middle: {y}"
            
            def inner_function(z):
                inner_var = f"inner: {z}"
                
                # 调试技巧1：打印所有可访问的变量
                print("=== 变量访问情况 ===")
                print(f"内层变量: {inner_var}")
                print(f"中层变量: {middle_var}")
                print(f"外层变量: {outer_var}")
                
                # 调试技巧2：使用locals()查看当前作用域
                print(f"当前作用域的局部变量: {locals()}")
                
                # 调试技巧3：检查闭包变量
                if hasattr(inner_function, '__closure__') and inner_function.__closure__:
                    print("闭包变量:")
                    for i, cell in enumerate(inner_function.__closure__):
                        print(f"  闭包变量{i}: {cell.cell_contents}")
                
                return f"结果: {outer_var} + {middle_var} + {inner_var}"
            
            return inner_function
        
        return middle_function
    
    # 创建嵌套函数
    nested_func = outer_function("Hello")("World")
    result = nested_func("Python")
    print(f"\n最终结果: {result}")

# 10. 嵌套作用域的最佳实践
def best_practices():
    """演示嵌套作用域的最佳实践"""
    print("\n=== 最佳实践 ===")
    
    # 1. 避免过深的嵌套
    print("1. 避免过深的嵌套（建议不超过3-4层）")
    
    # 2. 明确变量的作用域
    def clear_scope_example():
        # 明确标注变量的用途
        config_value = "配置值"  # 配置变量
        
        def process_data(data):
            # 处理函数可以访问配置
            return f"处理 {data} 使用配置 {config_value}"
        
        return process_data
    
    processor = clear_scope_example()
    print(f"2. 明确作用域: {processor('数据')}")
    
    # 3. 合理使用闭包
    def create_validator(min_value, max_value):
        """创建数值验证器"""
        def validate(value):
            if min_value <= value <= max_value:
                return True, f"值 {value} 在有效范围内"
            else:
                return False, f"值 {value} 超出范围 [{min_value}, {max_value}]"
        
        return validate
    
    # 使用验证器
    age_validator = create_validator(0, 120)
    score_validator = create_validator(0, 100)
    
    print("3. 合理使用闭包:")
    print(f"   年龄验证: {age_validator(25)}")
    print(f"   分数验证: {score_validator(150)}")
    
    # 4. 文档化嵌套函数
    def documented_nested_function():
        """外层函数：创建数据处理器"""
        processing_count = 0
        
        def process_item(item):
            """内层函数：处理单个数据项"""
            nonlocal processing_count
            processing_count += 1
            return f"处理第{processing_count}个项目: {item}"
        
        def get_count():
            """获取处理计数"""
            return processing_count
        
        # 返回处理函数和计数函数
        return process_item, get_count
    
    process_func, count_func = documented_nested_function()
    print("4. 文档化嵌套函数:")
    print(f"   {process_func('数据1')}")
    print(f"   {process_func('数据2')}")
    print(f"   处理总数: {count_func()}")

# 主程序
if __name__ == "__main__":
    print("Python函数作用域学习 - 嵌套作用域")
    print("=" * 50)
    
    # 1. 基本嵌套作用域
    basic_enclosing_scope()
    
    # 2. 多层嵌套
    multilevel_enclosing_scope()
    
    # 3. 变量遮蔽
    variable_shadowing()
    
    # 4. 闭包形成
    create_closure()
    
    # 5. 变量绑定
    closure_variable_binding()
    
    # 6. 装饰器应用
    decorator_with_enclosing_scope()
    
    # 7. 与类结合
    nested_scope_with_class()
    
    # 8. 性能考虑
    performance_considerations()
    
    # 9. 调试技巧
    debugging_nested_scope()
    
    # 10. 最佳实践
    best_practices()
    
    print("\n=== 学习总结 ===")
    print("1. 嵌套作用域允许内层函数访问外层函数的变量")
    print("2. 变量查找遵循从内到外的顺序")
    print("3. 同名变量会发生遮蔽现象")
    print("4. 嵌套作用域是闭包实现的基础")
    print("5. 合理使用嵌套作用域可以创建优雅的代码结构")
    print("6. 避免过深的嵌套以保持代码可读性和性能")
    print("7. 注意闭包中的变量绑定问题")
    print("8. 适当的文档化有助于理解复杂的嵌套结构")