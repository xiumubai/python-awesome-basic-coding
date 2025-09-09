#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nonlocal关键字 (Nonlocal Keyword)

nonlocal关键字用于在嵌套函数中声明外层函数的变量，
使得内层函数可以修改外层函数的局部变量。

学习目标：
1. 理解nonlocal关键字的作用
2. 掌握nonlocal关键字的使用方法
3. 了解nonlocal与global的区别
4. 理解闭包中nonlocal的应用
"""

# 1. 基本的nonlocal使用
def basic_nonlocal_usage():
    """演示基本的nonlocal关键字使用"""
    print("=== 基本nonlocal使用 ===")
    
    # 外层函数的局部变量
    outer_var = "外层变量"
    counter = 0
    
    def inner_function():
        # 声明要修改的外层变量
        nonlocal outer_var, counter
        
        print(f"修改前 - outer_var: {outer_var}, counter: {counter}")
        
        # 现在可以修改外层变量
        outer_var = "被内层函数修改"
        counter += 1
        
        print(f"修改后 - outer_var: {outer_var}, counter: {counter}")
    
    print(f"调用内层函数前: {outer_var}, {counter}")
    inner_function()
    print(f"调用内层函数后: {outer_var}, {counter}")

# 2. 不使用nonlocal的后果
def without_nonlocal_demo():
    """演示不使用nonlocal关键字的后果"""
    print("\n=== 不使用nonlocal的后果 ===")
    
    outer_var = "外层变量"
    
    def inner_function():
        # 不使用nonlocal，创建了局部变量
        outer_var = "内层局部变量"
        print(f"内层函数中的outer_var: {outer_var}")
    
    print(f"调用前的outer_var: {outer_var}")
    inner_function()
    print(f"调用后的outer_var: {outer_var}")
    print("注意：外层变量没有被修改")

# 3. nonlocal与global的区别
global_var = "全局变量"

def nonlocal_vs_global():
    """演示nonlocal与global的区别"""
    print("\n=== nonlocal vs global ===")
    
    outer_var = "外层局部变量"
    
    def inner_function():
        # 使用nonlocal修改外层变量
        nonlocal outer_var
        # 使用global修改全局变量
        global global_var
        
        print(f"修改前 - outer_var: {outer_var}")
        print(f"修改前 - global_var: {global_var}")
        
        outer_var = "nonlocal修改的外层变量"
        global_var = "global修改的全局变量"
        
        print(f"修改后 - outer_var: {outer_var}")
        print(f"修改后 - global_var: {global_var}")
    
    print(f"调用前 - outer_var: {outer_var}, global_var: {global_var}")
    inner_function()
    print(f"调用后 - outer_var: {outer_var}, global_var: {global_var}")

# 4. 多层嵌套中的nonlocal
def multilevel_nonlocal():
    """演示多层嵌套中的nonlocal使用"""
    print("\n=== 多层嵌套nonlocal ===")
    
    level1_var = "第1层变量"
    
    def level2_function():
        level2_var = "第2层变量"
        
        def level3_function():
            # 可以修改不同层级的变量
            nonlocal level1_var, level2_var
            
            print(f"第3层修改前 - level1: {level1_var}, level2: {level2_var}")
            
            level1_var = "第3层修改的第1层变量"
            level2_var = "第3层修改的第2层变量"
            
            print(f"第3层修改后 - level1: {level1_var}, level2: {level2_var}")
        
        print(f"第2层调用前 - level1: {level1_var}, level2: {level2_var}")
        level3_function()
        print(f"第2层调用后 - level1: {level1_var}, level2: {level2_var}")
    
    print(f"第1层调用前: {level1_var}")
    level2_function()
    print(f"第1层调用后: {level1_var}")

# 5. nonlocal在闭包中的应用
def create_counter(initial_value=0):
    """创建一个计数器闭包"""
    count = initial_value
    
    def increment(step=1):
        nonlocal count
        count += step
        return count
    
    def decrement(step=1):
        nonlocal count
        count -= step
        return count
    
    def get_count():
        return count
    
    def reset(value=0):
        nonlocal count
        count = value
        return count
    
    # 返回内部函数，形成闭包
    return increment, decrement, get_count, reset

def closure_demo():
    """演示闭包中nonlocal的使用"""
    print("\n=== 闭包中的nonlocal ===")
    
    # 创建两个独立的计数器
    inc1, dec1, get1, reset1 = create_counter(10)
    inc2, dec2, get2, reset2 = create_counter(100)
    
    print(f"计数器1初始值: {get1()}")
    print(f"计数器2初始值: {get2()}")
    
    # 操作计数器1
    print(f"计数器1增加5: {inc1(5)}")
    print(f"计数器1减少3: {dec1(3)}")
    
    # 操作计数器2
    print(f"计数器2增加20: {inc2(20)}")
    print(f"计数器2减少10: {dec2(10)}")
    
    print(f"计数器1当前值: {get1()}")
    print(f"计数器2当前值: {get2()}")
    
    # 重置计数器
    print(f"重置计数器1为0: {reset1()}")
    print(f"重置计数器2为50: {reset2(50)}")

# 6. nonlocal与装饰器
def create_call_counter():
    """创建一个调用计数装饰器"""
    call_count = 0
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            print(f"函数 {func.__name__} 被调用第 {call_count} 次")
            result = func(*args, **kwargs)
            return result
        
        def get_call_count():
            return call_count
        
        # 给wrapper添加获取调用次数的方法
        wrapper.get_call_count = get_call_count
        return wrapper
    
    return decorator

def decorator_demo():
    """演示装饰器中nonlocal的使用"""
    print("\n=== 装饰器中的nonlocal ===")
    
    # 创建装饰器
    call_counter = create_call_counter()
    
    @call_counter
    def greet(name):
        return f"Hello, {name}!"
    
    @call_counter
    def calculate(x, y):
        return x + y
    
    # 调用被装饰的函数
    print(greet("Alice"))
    print(greet("Bob"))
    print(f"greet函数调用次数: {greet.get_call_count()}")
    
    print(calculate(3, 4))
    print(calculate(10, 20))
    print(f"calculate函数调用次数: {calculate.get_call_count()}")

# 7. nonlocal的实际应用：状态机
def create_state_machine():
    """创建一个简单的状态机"""
    state = "stopped"
    
    def start():
        nonlocal state
        if state == "stopped":
            state = "running"
            return f"状态变更: stopped -> running"
        else:
            return f"无法启动，当前状态: {state}"
    
    def pause():
        nonlocal state
        if state == "running":
            state = "paused"
            return f"状态变更: running -> paused"
        else:
            return f"无法暂停，当前状态: {state}"
    
    def resume():
        nonlocal state
        if state == "paused":
            state = "running"
            return f"状态变更: paused -> running"
        else:
            return f"无法恢复，当前状态: {state}"
    
    def stop():
        nonlocal state
        if state in ["running", "paused"]:
            old_state = state
            state = "stopped"
            return f"状态变更: {old_state} -> stopped"
        else:
            return f"无法停止，当前状态: {state}"
    
    def get_state():
        return state
    
    return start, pause, resume, stop, get_state

def state_machine_demo():
    """演示状态机的使用"""
    print("\n=== 状态机中的nonlocal ===")
    
    start, pause, resume, stop, get_state = create_state_machine()
    
    print(f"初始状态: {get_state()}")
    print(start())
    print(f"当前状态: {get_state()}")
    
    print(pause())
    print(f"当前状态: {get_state()}")
    
    print(resume())
    print(f"当前状态: {get_state()}")
    
    print(stop())
    print(f"最终状态: {get_state()}")

# 8. nonlocal的注意事项
def nonlocal_limitations():
    """演示nonlocal的限制和注意事项"""
    print("\n=== nonlocal的注意事项 ===")
    
    # 1. nonlocal只能用于嵌套函数
    def outer():
        var = "外层变量"
        
        def inner():
            nonlocal var  # 正确：在嵌套函数中使用
            var = "修改后的变量"
        
        inner()
        return var
    
    # 2. nonlocal变量必须在外层作用域中存在
    def outer_with_error():
        def inner():
            # nonlocal undefined_var  # 错误：undefined_var不存在
            pass
        inner()
    
    # 3. nonlocal不能用于全局作用域
    def global_scope_error():
        # nonlocal global_var  # 错误：不能在函数顶层使用nonlocal
        pass
    
    print("1. nonlocal只能在嵌套函数中使用")
    print("2. nonlocal变量必须在外层作用域中已定义")
    print("3. nonlocal不能用于全局变量")
    
    result = outer()
    print(f"正确使用nonlocal的结果: {result}")

# 9. nonlocal vs 其他方案的比较
def comparison_demo():
    """比较nonlocal与其他方案"""
    print("\n=== nonlocal vs 其他方案 ===")
    
    # 方案1：使用nonlocal
    def with_nonlocal():
        count = 0
        
        def increment():
            nonlocal count
            count += 1
            return count
        
        return increment
    
    # 方案2：使用可变对象
    def with_mutable_object():
        count = [0]  # 使用列表
        
        def increment():
            count[0] += 1
            return count[0]
        
        return increment
    
    # 方案3：使用类
    class Counter:
        def __init__(self):
            self.count = 0
        
        def increment(self):
            self.count += 1
            return self.count
    
    # 测试三种方案
    print("方案1：使用nonlocal")
    counter1 = with_nonlocal()
    print(f"调用1: {counter1()}")
    print(f"调用2: {counter1()}")
    
    print("\n方案2：使用可变对象")
    counter2 = with_mutable_object()
    print(f"调用1: {counter2()}")
    print(f"调用2: {counter2()}")
    
    print("\n方案3：使用类")
    counter3 = Counter()
    print(f"调用1: {counter3.increment()}")
    print(f"调用2: {counter3.increment()}")

# 主程序
if __name__ == "__main__":
    print("Python函数作用域学习 - nonlocal关键字")
    print("=" * 50)
    
    # 1. 基本使用
    basic_nonlocal_usage()
    
    # 2. 不使用nonlocal的后果
    without_nonlocal_demo()
    
    # 3. nonlocal vs global
    nonlocal_vs_global()
    
    # 4. 多层嵌套
    multilevel_nonlocal()
    
    # 5. 闭包应用
    closure_demo()
    
    # 6. 装饰器应用
    decorator_demo()
    
    # 7. 状态机应用
    state_machine_demo()
    
    # 8. 注意事项
    nonlocal_limitations()
    
    # 9. 方案比较
    comparison_demo()
    
    print("\n=== 学习总结 ===")
    print("1. nonlocal用于在嵌套函数中修改外层函数的变量")
    print("2. nonlocal变量必须在外层作用域中已定义")
    print("3. nonlocal常用于闭包、装饰器和状态管理")
    print("4. nonlocal只能用于嵌套函数，不能用于全局变量")
    print("5. nonlocal是实现闭包状态保持的重要机制")
    print("6. 合理使用nonlocal可以创建优雅的函数式编程解决方案")