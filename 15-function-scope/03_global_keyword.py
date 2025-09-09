#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
global关键字 (Global Keyword)

global关键字用于在函数内部声明全局变量，
使得函数可以修改全局变量的值。

学习目标：
1. 理解global关键字的作用
2. 掌握global关键字的使用方法
3. 了解何时需要使用global
4. 理解global的最佳实践
"""

# 全局变量定义
counter = 0
message = "初始消息"
user_list = []
config = {"debug": False, "version": "1.0"}

# 1. 基本的global使用
def basic_global_usage():
    """演示基本的global关键字使用"""
    print("=== 基本global使用 ===")
    
    # 声明要修改的全局变量
    global counter
    global message
    
    print(f"修改前 - counter: {counter}, message: {message}")
    
    # 现在可以修改全局变量
    counter = counter + 1
    message = "已被函数修改"
    
    print(f"修改后 - counter: {counter}, message: {message}")

# 2. 不使用global的后果
def without_global_demo():
    """演示不使用global关键字的后果"""
    print("\n=== 不使用global的后果 ===")
    
    # 创建局部变量（不是修改全局变量）
    counter = 999
    message = "局部消息"
    
    print(f"函数内 - counter: {counter}, message: {message}")
    print("注意：这些是局部变量，不会影响全局变量")
    print("如果在赋值前尝试读取会导致UnboundLocalError")

# 3. global与局部变量的区别
def global_vs_local():
    """演示global变量与局部变量的区别"""
    print("\n=== global vs 局部变量 ===")
    
    # 声明全局变量
    global counter
    
    # 创建局部变量
    local_counter = 100
    
    print(f"全局counter（可修改）: {counter}")
    print(f"局部local_counter: {local_counter}")
    
    # 修改全局变量
    counter += 10
    # 修改局部变量
    local_counter += 10
    
    print(f"修改后 - 全局counter: {counter}")
    print(f"修改后 - 局部local_counter: {local_counter}")

# 4. 多个全局变量的声明
def multiple_global_variables():
    """演示声明多个全局变量"""
    print("\n=== 多个全局变量声明 ===")
    
    # 可以在一行声明多个全局变量
    global counter, message
    
    print(f"当前值 - counter: {counter}, message: {message}")
    
    # 修改多个全局变量
    counter *= 2
    message = f"计数器翻倍为{counter}"
    
    print(f"修改后 - counter: {counter}, message: {message}")

# 5. 条件性使用global
def conditional_global_usage(should_modify=True):
    """演示条件性使用global"""
    print("\n=== 条件性global使用 ===")
    
    if should_modify:
        global counter
        print(f"条件满足，修改前counter: {counter}")
        counter += 5
        print(f"修改后counter: {counter}")
    else:
        # 只读取，不修改
        print(f"条件不满足，只读取counter: {counter}")

# 6. global与函数参数
def global_with_parameters(increment_value):
    """演示global与函数参数的结合使用"""
    print("\n=== global与函数参数 ===")
    
    global counter
    
    print(f"参数值: {increment_value}")
    print(f"修改前的全局counter: {counter}")
    
    # 使用参数修改全局变量
    counter += increment_value
    
    print(f"修改后的全局counter: {counter}")
    
    return counter

# 7. global与容器操作
def global_container_operations():
    """演示global与容器操作"""
    print("\n=== global与容器操作 ===")
    
    # 对于容器，通常不需要global就能修改内容
    print(f"修改前的user_list: {user_list}")
    user_list.append("新用户")
    print(f"添加元素后的user_list: {user_list}")
    
    # 但如果要重新赋值整个容器，需要global
    global config
    print(f"修改前的config: {config}")
    config = {"debug": True, "version": "2.0", "new_feature": True}
    print(f"重新赋值后的config: {config}")

# 8. 嵌套函数中的global
def outer_with_global():
    """演示嵌套函数中的global使用"""
    print("\n=== 嵌套函数中的global ===")
    
    def inner_function():
        # 内层函数也可以使用global
        global message
        message = "被内层函数修改"
        print(f"内层函数修改message: {message}")
    
    print(f"调用内层函数前: {message}")
    inner_function()
    print(f"调用内层函数后: {message}")

# 9. global的实际应用场景
# 应用状态管理
app_status = "stopped"
user_count = 0
error_count = 0

def start_application():
    """启动应用"""
    global app_status, user_count
    
    print("\n=== 启动应用 ===")
    app_status = "running"
    user_count = 0
    print(f"应用状态: {app_status}")
    print(f"用户数量: {user_count}")

def add_user(username):
    """添加用户"""
    global user_count
    
    if app_status == "running":
        user_count += 1
        print(f"添加用户: {username}, 当前用户数: {user_count}")
        return True
    else:
        print("应用未运行，无法添加用户")
        return False

def report_error():
    """报告错误"""
    global error_count
    
    error_count += 1
    print(f"错误报告，当前错误数: {error_count}")

def stop_application():
    """停止应用"""
    global app_status
    
    print("\n=== 停止应用 ===")
    app_status = "stopped"
    print(f"应用状态: {app_status}")
    print(f"最终用户数: {user_count}")
    print(f"总错误数: {error_count}")

# 10. global的注意事项和最佳实践
def global_best_practices():
    """演示global的最佳实践"""
    print("\n=== global最佳实践 ===")
    
    # 1. 尽量减少global的使用
    print("1. 尽量减少global变量的使用")
    
    # 2. 使用函数返回值代替global
    def increment_counter_better(current_value, increment=1):
        """更好的方式：使用参数和返回值"""
        return current_value + increment
    
    # 3. 使用类来管理状态
    class Counter:
        def __init__(self):
            self.value = 0
        
        def increment(self, amount=1):
            self.value += amount
        
        def get_value(self):
            return self.value
    
    # 演示更好的方式
    print("\n更好的替代方案:")
    
    # 使用返回值
    new_value = increment_counter_better(counter, 3)
    print(f"使用返回值: {counter} + 3 = {new_value}")
    
    # 使用类
    counter_obj = Counter()
    counter_obj.increment(5)
    print(f"使用类管理状态: {counter_obj.get_value()}")

# 11. global的错误使用示例
def common_global_mistakes():
    """演示global的常见错误"""
    print("\n=== global常见错误 ===")
    
    # 错误1：忘记声明global
    def mistake1():
        # counter = counter + 1  # 这会报错：UnboundLocalError
        print("错误1：忘记声明global会导致UnboundLocalError")
    
    # 错误2：不必要的global声明
    def mistake2():
        global user_list  # 对于容器修改，通常不需要global
        user_list.append("用户")
        print("错误2：对容器内容修改不需要global")
    
    # 错误3：过度使用global
    def mistake3():
        global counter, message, user_list, config  # 过多的global声明
        print("错误3：过度使用global使代码难以维护")
    
    mistake1()
    mistake2()
    mistake3()

# 主程序
if __name__ == "__main__":
    print("Python函数作用域学习 - global关键字")
    print("=" * 50)
    
    # 显示初始状态
    print(f"初始状态 - counter: {counter}, message: {message}")
    
    # 1. 基本使用
    basic_global_usage()
    print(f"函数调用后 - counter: {counter}, message: {message}")
    
    # 2. 不使用global的后果
    print(f"\n调用without_global_demo前 - counter: {counter}")
    without_global_demo()
    print(f"调用without_global_demo后 - counter: {counter}")
    
    # 3. global vs 局部
    global_vs_local()
    
    # 4. 多个全局变量
    multiple_global_variables()
    
    # 5. 条件性使用
    conditional_global_usage(True)
    conditional_global_usage(False)
    
    # 6. 与参数结合
    result = global_with_parameters(20)
    print(f"函数返回值: {result}")
    
    # 7. 容器操作
    global_container_operations()
    
    # 8. 嵌套函数
    outer_with_global()
    
    # 9. 实际应用
    start_application()
    add_user("Alice")
    add_user("Bob")
    report_error()
    add_user("Charlie")
    report_error()
    stop_application()
    
    # 10. 最佳实践
    global_best_practices()
    
    # 11. 常见错误
    common_global_mistakes()
    
    print("\n=== 学习总结 ===")
    print("1. global关键字用于在函数内修改全局变量")
    print("2. 不使用global只能读取全局变量，不能修改")
    print("3. 可以在一行声明多个全局变量")
    print("4. 修改容器内容通常不需要global")
    print("5. 重新赋值容器需要使用global")
    print("6. 尽量减少global的使用，考虑其他设计模式")
    print("7. 过度使用global会使代码难以维护和测试")