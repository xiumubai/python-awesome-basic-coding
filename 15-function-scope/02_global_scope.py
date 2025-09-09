#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全局作用域 (Global Scope)

全局作用域是指在模块级别定义的变量的作用范围。
这些变量可以在整个模块中的任何地方访问，包括函数内部。

学习目标：
1. 理解全局作用域的概念
2. 掌握全局变量的定义和访问
3. 了解全局变量的生命周期
4. 理解全局变量与局部变量的关系
"""

# 1. 全局变量的定义
# 在模块顶层定义的变量都是全局变量
global_message = "我是全局变量"
global_counter = 0
global_list = [1, 2, 3, 4, 5]
global_dict = {"name": "Python", "version": "3.9"}

# 常量（按约定使用大写）
MAX_SIZE = 100
DEFAULT_COLOR = "blue"
PI = 3.14159

def access_global_variables():
    """演示如何在函数中访问全局变量"""
    print("=== 访问全局变量 ===")
    
    # 直接访问全局变量
    print(f"全局消息: {global_message}")
    print(f"全局计数器: {global_counter}")
    print(f"全局列表: {global_list}")
    print(f"全局字典: {global_dict}")
    
    # 访问常量
    print(f"最大尺寸: {MAX_SIZE}")
    print(f"默认颜色: {DEFAULT_COLOR}")
    print(f"圆周率: {PI}")

# 2. 全局变量的只读访问
def read_only_access():
    """演示全局变量的只读访问"""
    print("\n=== 只读访问全局变量 ===")
    
    # 可以读取全局变量
    current_counter = global_counter
    print(f"当前计数器值: {current_counter}")
    
    # 可以使用全局变量进行计算
    doubled_counter = global_counter * 2
    print(f"计数器的两倍: {doubled_counter}")
    
    # 可以访问全局容器的元素
    first_item = global_list[0]
    python_name = global_dict["name"]
    print(f"列表第一个元素: {first_item}")
    print(f"字典中的名称: {python_name}")

# 3. 全局变量与局部变量的名称冲突
def name_conflict_demo():
    """演示全局变量与局部变量的名称冲突"""
    print("\n=== 名称冲突演示 ===")
    
    # 定义同名的局部变量
    global_message = "我是局部变量，会遮蔽全局变量"
    global_counter = 999
    
    print(f"函数内的global_message: {global_message}")
    print(f"函数内的global_counter: {global_counter}")
    
    print("注意：局部变量会遮蔽同名的全局变量")

# 4. 全局变量在不同函数间共享
def function_a():
    """函数A访问全局变量"""
    print(f"函数A访问全局消息: {global_message}")
    return global_counter

def function_b():
    """函数B访问全局变量"""
    print(f"函数B访问全局消息: {global_message}")
    return len(global_list)

def shared_global_access():
    """演示全局变量在不同函数间的共享"""
    print("\n=== 全局变量共享访问 ===")
    
    result_a = function_a()
    result_b = function_b()
    
    print(f"函数A返回的计数器值: {result_a}")
    print(f"函数B返回的列表长度: {result_b}")

# 5. 全局变量的修改限制
def modify_attempt():
    """演示尝试修改全局变量的限制"""
    print("\n=== 修改全局变量的限制 ===")
    
    # 尝试修改全局变量（实际上创建了局部变量）
    # global_counter = global_counter + 1  # 这会报错：UnboundLocalError
    
    # 正确的做法是先声明为全局变量（下一个文件会详细介绍）
    print("不使用global关键字无法修改全局变量")
    print("尝试修改会创建同名的局部变量")

# 6. 全局容器的元素修改
def modify_global_container():
    """演示修改全局容器的元素"""
    print("\n=== 修改全局容器元素 ===")
    
    print(f"修改前的全局列表: {global_list}")
    print(f"修改前的全局字典: {global_dict}")
    
    # 可以修改全局容器的内容（不是重新赋值）
    global_list.append(6)
    global_dict["author"] = "Guido van Rossum"
    
    print(f"修改后的全局列表: {global_list}")
    print(f"修改后的全局字典: {global_dict}")

# 7. 全局变量的实际应用
# 配置信息
APP_NAME = "学生管理系统"
VERSION = "1.0.0"
DEBUG_MODE = True

# 应用状态
user_count = 0
active_sessions = []
config_settings = {
    "max_users": 1000,
    "session_timeout": 3600,
    "log_level": "INFO"
}

def show_app_info():
    """显示应用信息"""
    print(f"\n=== 应用信息 ===")
    print(f"应用名称: {APP_NAME}")
    print(f"版本: {VERSION}")
    print(f"调试模式: {DEBUG_MODE}")
    print(f"当前用户数: {user_count}")
    print(f"活跃会话: {len(active_sessions)}")

def get_config(key):
    """获取配置信息"""
    return config_settings.get(key, "未找到配置")

def add_session(session_id):
    """添加会话（修改全局列表）"""
    active_sessions.append(session_id)
    print(f"添加会话: {session_id}")
    print(f"当前活跃会话数: {len(active_sessions)}")

# 8. 模块级别的计算
# 在模块加载时执行的计算
calculated_value = PI * 2
max_items = MAX_SIZE // 10
default_settings = {
    "color": DEFAULT_COLOR,
    "size": MAX_SIZE,
    "pi_doubled": calculated_value
}

def show_calculated_values():
    """显示计算得出的全局值"""
    print("\n=== 计算得出的全局值 ===")
    print(f"计算值: {calculated_value}")
    print(f"最大项目数: {max_items}")
    print(f"默认设置: {default_settings}")

# 9. 全局变量的最佳实践示例
class GlobalCounter:
    """使用类来管理全局状态的更好方式"""
    def __init__(self):
        self.count = 0
        self.history = []
    
    def increment(self):
        self.count += 1
        self.history.append(f"增加到 {self.count}")
    
    def get_status(self):
        return {
            "current": self.count,
            "history_length": len(self.history)
        }

# 创建全局计数器实例
global_counter_obj = GlobalCounter()

def use_global_counter():
    """使用全局计数器对象"""
    print("\n=== 使用全局计数器对象 ===")
    
    # 使用对象方法修改状态
    global_counter_obj.increment()
    global_counter_obj.increment()
    
    status = global_counter_obj.get_status()
    print(f"计数器状态: {status}")

# 主程序
if __name__ == "__main__":
    print("Python函数作用域学习 - 全局作用域")
    print("=" * 50)
    
    # 1. 访问全局变量
    access_global_variables()
    
    # 2. 只读访问
    read_only_access()
    
    # 3. 名称冲突
    print(f"\n函数外的global_message: {global_message}")
    name_conflict_demo()
    print(f"函数调用后的global_message: {global_message}")
    
    # 4. 共享访问
    shared_global_access()
    
    # 5. 修改限制
    modify_attempt()
    
    # 6. 容器修改
    print(f"\n修改容器前 - 列表: {global_list}")
    modify_global_container()
    print(f"修改容器后 - 列表: {global_list}")
    
    # 7. 实际应用
    show_app_info()
    
    # 添加一些会话
    add_session("session_001")
    add_session("session_002")
    
    # 获取配置
    max_users = get_config("max_users")
    timeout = get_config("session_timeout")
    print(f"\n最大用户数: {max_users}")
    print(f"会话超时: {timeout}秒")
    
    # 8. 计算值
    show_calculated_values()
    
    # 9. 最佳实践
    use_global_counter()
    
    print("\n=== 学习总结 ===")
    print("1. 全局变量在模块顶层定义，整个模块都可访问")
    print("2. 函数可以读取全局变量，但不能直接修改")
    print("3. 局部变量会遮蔽同名的全局变量")
    print("4. 可以修改全局容器的内容（如列表、字典）")
    print("5. 全局变量适合存储配置信息和应用状态")
    print("6. 过度使用全局变量可能导致代码难以维护")