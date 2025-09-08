#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
局部和全局作用域详解

本文件演示Python函数中的作用域概念，包括：
1. 全局作用域
2. 局部作用域
3. global关键字
4. nonlocal关键字
5. 作用域查找规则（LEGB规则）
6. 作用域的最佳实践

作者：Python学习教程
日期：2024年
"""

print("=" * 50)
print("Python 局部和全局作用域详解")
print("=" * 50)

# 1. 全局变量和局部变量
print("\n1. 全局变量和局部变量")
print("-" * 30)

# 全局变量
global_var = "我是全局变量"
counter = 0

def demo_scope():
    """演示作用域基本概念"""
    # 局部变量
    local_var = "我是局部变量"
    
    print(f"函数内部访问全局变量：{global_var}")
    print(f"函数内部访问局部变量：{local_var}")
    
    # 可以读取全局变量，但不能直接修改
    print(f"函数内部读取全局counter：{counter}")

print("作用域基本演示：")
demo_scope()
print(f"函数外部访问全局变量：{global_var}")
# print(local_var)  # 错误：局部变量在函数外部不可访问
print()

# 2. 局部变量遮蔽全局变量
print("\n2. 局部变量遮蔽全局变量")
print("-" * 30)

name = "全局的张三"

def show_name():
    """局部变量遮蔽全局变量"""
    name = "局部的李四"  # 局部变量遮蔽全局变量
    print(f"函数内部的name：{name}")

def show_global_name():
    """访问全局变量"""
    print(f"函数内部访问全局name：{name}")

print("变量遮蔽演示：")
print(f"全局name：{name}")
show_name()
show_global_name()
print(f"函数调用后全局name：{name}")
print()

# 3. 使用global关键字
print("\n3. 使用global关键字")
print("-" * 30)

total = 0

def add_to_total(value):
    """使用global关键字修改全局变量"""
    global total
    total += value
    print(f"函数内部：total = {total}")

def reset_total():
    """重置全局变量"""
    global total
    total = 0
    print("total已重置为0")

print("global关键字演示：")
print(f"初始total：{total}")
add_to_total(10)
print(f"函数调用后total：{total}")
add_to_total(20)
print(f"再次调用后total：{total}")
reset_total()
print(f"重置后total：{total}")
print()

# 4. 嵌套函数和nonlocal关键字
print("\n4. 嵌套函数和nonlocal关键字")
print("-" * 30)

def outer_function():
    """外层函数"""
    outer_var = "外层变量"
    
    def inner_function():
        """内层函数"""
        inner_var = "内层变量"
        print(f"内层函数访问外层变量：{outer_var}")
        print(f"内层函数访问内层变量：{inner_var}")
    
    print(f"外层函数的变量：{outer_var}")
    inner_function()
    # print(inner_var)  # 错误：外层函数不能访问内层变量

def counter_function():
    """使用nonlocal的计数器函数"""
    count = 0
    
    def increment():
        nonlocal count  # 声明要修改外层函数的变量
        count += 1
        return count
    
    def decrement():
        nonlocal count
        count -= 1
        return count
    
    def get_count():
        return count
    
    return increment, decrement, get_count

print("嵌套函数演示：")
outer_function()

print("\nnonlocal关键字演示：")
inc, dec, get = counter_function()
print(f"初始计数：{get()}")
print(f"递增后：{inc()}")
print(f"再次递增：{inc()}")
print(f"递减后：{dec()}")
print(f"当前计数：{get()}")
print()

# 5. LEGB规则演示
print("\n5. LEGB规则演示（Local, Enclosing, Global, Built-in）")
print("-" * 30)

# Built-in scope（内置作用域）
# len, print, str等都是内置函数

# Global scope（全局作用域）
x = "全局x"

def legb_demo():
    """演示LEGB查找规则"""
    # Enclosing scope（外层作用域）
    x = "外层x"
    
    def inner():
        # Local scope（局部作用域）
        x = "局部x"
        print(f"内层函数中的x：{x}")  # 找到局部x
        
        # 访问不同作用域的变量
        print(f"使用len函数（内置）：{len('hello')}")
    
    def inner_no_local():
        print(f"内层函数（无局部x）：{x}")  # 找到外层x
    
    print(f"外层函数中的x：{x}")
    inner()
    inner_no_local()

print("LEGB规则演示：")
print(f"全局作用域的x：{x}")
legb_demo()
print()

# 6. 作用域陷阱和注意事项
print("\n6. 作用域陷阱和注意事项")
print("-" * 30)

def scope_trap_demo():
    """演示常见的作用域陷阱"""
    print("演示作用域陷阱：")
    
    # 陷阱1：在赋值前访问全局变量
    global_num = 100
    
    def trap1():
        print(f"访问全局变量：{global_num}")
        # global_num = 200  # 如果取消注释，上面的print会报错
    
    trap1()
    
    # 陷阱2：循环中的闭包
    functions = []
    for i in range(3):
        # 错误的方式：所有函数都会返回2
        # functions.append(lambda: i)
        
        # 正确的方式：使用默认参数捕获当前值
        functions.append(lambda x=i: x)
    
    print("闭包陷阱演示：")
    for j, func in enumerate(functions):
        print(f"函数{j}返回：{func()}")

scope_trap_demo()
print()

# 7. 实际应用示例
print("\n7. 实际应用示例")
print("-" * 30)

# 配置管理示例
config = {
    "debug": False,
    "max_connections": 100,
    "timeout": 30
}

def get_config(key):
    """获取配置值"""
    return config.get(key)

def set_config(key, value):
    """设置配置值"""
    global config
    config[key] = value
    print(f"配置已更新：{key} = {value}")

def create_logger(name):
    """创建日志记录器（闭包示例）"""
    log_level = "INFO"
    
    def log(message, level="INFO"):
        nonlocal log_level
        if level == "DEBUG" and not config.get("debug", False):
            return
        print(f"[{level}] {name}: {message}")
    
    def set_level(level):
        nonlocal log_level
        log_level = level
        print(f"日志级别设置为：{level}")
    
    return log, set_level

print("实际应用示例：")
print(f"当前配置：{config}")
set_config("debug", True)
print(f"更新后配置：{config}")

# 创建日志记录器
log, set_level = create_logger("MyApp")
log("应用程序启动")
log("调试信息", "DEBUG")
set_level("ERROR")
log("这是一个错误", "ERROR")
print()

# 8. 最佳实践
print("\n8. 作用域最佳实践")
print("-" * 30)

# 好的实践：最小化全局变量的使用
class AppState:
    """使用类来管理状态，而不是全局变量"""
    def __init__(self):
        self.user_count = 0
        self.is_running = False
    
    def start(self):
        self.is_running = True
        print("应用程序已启动")
    
    def add_user(self):
        self.user_count += 1
        print(f"用户数量：{self.user_count}")

def create_calculator():
    """使用闭包创建计算器"""
    history = []
    
    def calculate(operation, a, b):
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            result = a / b if b != 0 else "错误：除零"
        else:
            result = "未知操作"
        
        history.append(f"{operation}({a}, {b}) = {result}")
        return result
    
    def get_history():
        return history.copy()
    
    def clear_history():
        history.clear()
        print("历史记录已清空")
    
    return calculate, get_history, clear_history

print("最佳实践示例：")
# 使用类管理状态
app = AppState()
app.start()
app.add_user()
app.add_user()

# 使用闭包创建功能
calc, get_hist, clear_hist = create_calculator()
print(f"计算结果：{calc('add', 5, 3)}")
print(f"计算结果：{calc('multiply', 4, 7)}")
print(f"历史记录：{get_hist()}")
clear_hist()

print("\n=" * 50)
print("局部和全局作用域学习完成！")
print("=" * 50)
print("\n总结：")
print("1. 局部变量只在函数内部可见")
print("2. 全局变量在整个程序中可见")
print("3. 局部变量会遮蔽同名的全局变量")
print("4. 使用global关键字可以在函数内修改全局变量")
print("5. 使用nonlocal关键字可以修改外层函数的变量")
print("6. Python遵循LEGB查找规则")
print("7. 最小化全局变量的使用是好的实践")
print("8. 闭包可以创建有状态的函数")