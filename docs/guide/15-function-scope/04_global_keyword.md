# global关键字

global关键字是Python中用于在函数内部修改全局变量的重要工具，理解其正确使用方法对于编写高质量的Python代码至关重要。

## 什么是global关键字

global关键字用于在函数内部声明一个变量为全局变量，使得函数可以修改全局作用域中的变量。没有global声明，函数内部只能读取全局变量，不能修改它们。

## global关键字的作用

1. **允许修改**：使函数能够修改全局变量
2. **明确意图**：明确表示要操作全局变量
3. **避免错误**：防止UnboundLocalError错误
4. **代码清晰**：让代码意图更加明确

## 代码示例

### 基本global关键字使用

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
global关键字演示

本文件演示Python中global关键字的使用方法和最佳实践。
global关键字用于在函数内部修改全局变量。
"""

# 全局变量
counter = 0
app_status = "stopped"
user_data = {"name": "未设置", "level": 1}
settings = ["default", "auto"]

def demonstrate_basic_global():
    """
    演示global关键字的基本使用
    """
    print("=== global关键字基本使用 ===")
    
    # 读取全局变量（不需要global）
    print(f"读取全局counter: {counter}")
    
    # 修改全局变量（需要global声明）
    global counter
    counter += 1
    print(f"修改后的counter: {counter}")
    
    # 修改全局字符串
    global app_status
    app_status = "running"
    print(f"修改后的app_status: {app_status}")

def demonstrate_without_global():
    """
    演示不使用global关键字的后果
    """
    print("\n=== 不使用global的后果 ===")
    
    def try_modify_without_global():
        try:
            # 尝试读取然后修改（会出错）
            print(f"尝试读取counter: {counter}")
            # counter += 1  # 这行会引发UnboundLocalError
        except UnboundLocalError as e:
            print(f"UnboundLocalError: {e}")
            print("原因：Python认为counter是局部变量，但在赋值前就被引用了")
    
    def create_local_variable():
        # 这会创建一个局部变量，不会影响全局变量
        counter = 100
        print(f"局部counter: {counter}")
        print(f"全局counter仍然是: {globals()['counter']}")
    
    try_modify_without_global()
    create_local_variable()

def demonstrate_multiple_global():
    """
    演示同时声明多个全局变量
    """
    print("\n=== 同时声明多个全局变量 ===")
    
    # 可以在一行中声明多个全局变量
    global counter, app_status
    
    print(f"修改前: counter={counter}, app_status={app_status}")
    
    counter *= 2
    app_status = "busy"
    
    print(f"修改后: counter={counter}, app_status={app_status}")
    
    # 也可以分别声明
    global user_data
    global settings
    
    user_data["name"] = "Alice"
    user_data["level"] = 5
    settings.append("advanced")
    
    print(f"修改后的user_data: {user_data}")
    print(f"修改后的settings: {settings}")

def demonstrate_global_in_nested_functions():
    """
    演示在嵌套函数中使用global
    """
    print("\n=== 嵌套函数中的global ===")
    
    def outer_function():
        # 外层函数中的局部变量
        local_var = "外层局部变量"
        
        def inner_function():
            # 内层函数可以使用global访问全局变量
            global counter
            counter += 10
            
            # 但不能直接修改外层函数的局部变量
            print(f"内层函数访问全局counter: {counter}")
            print(f"内层函数访问外层局部变量: {local_var}")
        
        print(f"调用内层函数前，counter: {counter}")
        inner_function()
        print(f"调用内层函数后，counter: {counter}")
    
    outer_function()

def demonstrate_global_with_collections():
    """
    演示global与集合类型的使用
    """
    print("\n=== global与集合类型 ===")
    
    # 对于集合类型，修改内容不需要global
    print(f"修改前的user_data: {user_data}")
    user_data["score"] = 100  # 不需要global
    print(f"修改内容后的user_data: {user_data}")
    
    # 但是重新赋值需要global
    global user_data
    user_data = {"name": "Bob", "level": 10, "score": 200}
    print(f"重新赋值后的user_data: {user_data}")
    
    # 列表也是同样的规则
    settings.extend(["expert", "custom"])  # 不需要global
    print(f"扩展后的settings: {settings}")
    
    global settings
    settings = ["new", "config"]  # 需要global
    print(f"重新赋值后的settings: {settings}")

def demonstrate_global_scope_chain():
    """
    演示global在作用域链中的作用
    """
    print("\n=== global在作用域链中的作用 ===")
    
    # 创建一个与全局变量同名的局部变量
    counter = 999
    print(f"函数内局部counter: {counter}")
    
    def inner_with_global():
        global counter  # 指向全局counter，不是外层函数的局部counter
        counter += 5
        print(f"inner_with_global中的counter: {counter}")
    
    def inner_without_global():
        # 这里的counter指向外层函数的局部变量
        print(f"inner_without_global中的counter: {counter}")
    
    print(f"调用前全局counter: {globals()['counter']}")
    inner_with_global()
    print(f"调用后全局counter: {globals()['counter']}")
    
    inner_without_global()
    print(f"函数内局部counter仍然是: {counter}")

def practical_example_counter_system():
    """
    实际应用示例：计数器系统
    """
    print("\n=== 实际应用：计数器系统 ===")
    
    def increment_counter(step=1):
        """增加计数器"""
        global counter
        counter += step
        return counter
    
    def decrement_counter(step=1):
        """减少计数器"""
        global counter
        counter -= step
        return counter
    
    def reset_counter():
        """重置计数器"""
        global counter
        old_value = counter
        counter = 0
        return old_value
    
    def get_counter():
        """获取计数器值（不需要global，只是读取）"""
        return counter
    
    # 测试计数器系统
    print(f"当前计数器: {get_counter()}")
    print(f"增加5: {increment_counter(5)}")
    print(f"增加3: {increment_counter(3)}")
    print(f"减少2: {decrement_counter(2)}")
    print(f"当前值: {get_counter()}")
    old_value = reset_counter()
    print(f"重置前的值: {old_value}, 重置后: {get_counter()}")

def practical_example_state_machine():
    """
    实际应用示例：状态机
    """
    print("\n=== 实际应用：状态机 ===")
    
    def start_app():
        """启动应用"""
        global app_status
        if app_status == "stopped":
            app_status = "starting"
            print("应用正在启动...")
            app_status = "running"
            print("应用已启动")
            return True
        else:
            print(f"应用当前状态是 {app_status}，无法启动")
            return False
    
    def stop_app():
        """停止应用"""
        global app_status
        if app_status == "running":
            app_status = "stopping"
            print("应用正在停止...")
            app_status = "stopped"
            print("应用已停止")
            return True
        else:
            print(f"应用当前状态是 {app_status}，无法停止")
            return False
    
    def get_app_status():
        """获取应用状态"""
        return app_status
    
    def pause_app():
        """暂停应用"""
        global app_status
        if app_status == "running":
            app_status = "paused"
            print("应用已暂停")
            return True
        else:
            print(f"应用当前状态是 {app_status}，无法暂停")
            return False
    
    def resume_app():
        """恢复应用"""
        global app_status
        if app_status == "paused":
            app_status = "running"
            print("应用已恢复")
            return True
        else:
            print(f"应用当前状态是 {app_status}，无法恢复")
            return False
    
    # 测试状态机
    print(f"初始状态: {get_app_status()}")
    start_app()
    print(f"当前状态: {get_app_status()}")
    pause_app()
    print(f"当前状态: {get_app_status()}")
    resume_app()
    print(f"当前状态: {get_app_status()}")
    stop_app()
    print(f"最终状态: {get_app_status()}")

def demonstrate_global_best_practices():
    """
    演示global关键字的最佳实践
    """
    print("\n=== global关键字最佳实践 ===")
    
    # 最佳实践1：最小化global的使用
    def good_practice_minimal_global():
        """好的做法：最小化global使用"""
        global counter
        # 只在真正需要修改时使用global
        counter += 1
        
        # 其他操作使用局部变量
        local_result = counter * 2
        return local_result
    
    # 最佳实践2：使用函数封装全局状态
    def good_practice_encapsulation():
        """好的做法：封装全局状态访问"""
        def _modify_global_safely(new_value):
            global counter
            if isinstance(new_value, int) and new_value >= 0:
                counter = new_value
                return True
            return False
        
        return _modify_global_safely
    
    # 最佳实践3：明确的函数命名
    def update_global_counter(new_value):
        """好的做法：函数名明确表示会修改全局状态"""
        global counter
        old_value = counter
        counter = new_value
        return old_value
    
    # 最佳实践4：返回修改结果
    def increment_and_return():
        """好的做法：返回修改后的值"""
        global counter
        counter += 1
        return counter
    
    # 测试最佳实践
    print(f"当前counter: {counter}")
    result = good_practice_minimal_global()
    print(f"最小化global使用结果: {result}, counter: {counter}")
    
    modifier = good_practice_encapsulation()
    success = modifier(50)
    print(f"封装修改结果: {success}, counter: {counter}")
    
    old_value = update_global_counter(100)
    print(f"明确命名函数: 旧值={old_value}, 新值={counter}")
    
    new_value = increment_and_return()
    print(f"返回修改结果: {new_value}")

def demonstrate_global_pitfalls():
    """
    演示global关键字的常见陷阱
    """
    print("\n=== global关键字常见陷阱 ===")
    
    # 陷阱1：忘记使用global
    def pitfall_forgot_global():
        try:
            # 这会创建局部变量，不会修改全局变量
            counter = 200
            print(f"函数内counter: {counter}")
            print(f"全局counter: {globals()['counter']}")
        except Exception as e:
            print(f"错误: {e}")
    
    # 陷阱2：过度使用global
    def pitfall_overuse_global():
        """不好的做法：过度使用global"""
        global counter, app_status, user_data, settings
        # 修改太多全局变量，使函数难以理解和测试
        counter += 1
        app_status = "modified"
        user_data["modified"] = True
        settings.append("overused")
    
    # 陷阱3：在循环中使用global
    def pitfall_global_in_loop():
        """潜在问题：在循环中使用global"""
        global counter
        for i in range(3):
            counter += i
            print(f"循环 {i}: counter = {counter}")
    
    # 陷阱4：global声明位置错误
    def pitfall_wrong_global_position():
        """错误：global声明位置不当"""
        # 错误：在使用后才声明global
        try:
            print(f"尝试使用counter: {counter}")
            global counter  # 这个位置的global声明无效
            counter += 1
        except UnboundLocalError as e:
            print(f"位置错误导致的错误: {e}")
    
    print("演示各种陷阱:")
    pitfall_forgot_global()
    pitfall_overuse_global()
    pitfall_global_in_loop()
    pitfall_wrong_global_position()

def demonstrate_alternatives_to_global():
    """
    演示global的替代方案
    """
    print("\n=== global的替代方案 ===")
    
    # 替代方案1：使用类
    class Counter:
        def __init__(self):
            self.value = 0
        
        def increment(self, step=1):
            self.value += step
            return self.value
        
        def get_value(self):
            return self.value
    
    # 替代方案2：使用闭包
    def create_counter():
        count = 0
        
        def increment(step=1):
            nonlocal count
            count += step
            return count
        
        def get_count():
            return count
        
        return increment, get_count
    
    # 替代方案3：使用字典或列表
    state = {"counter": 0, "status": "ready"}
    
    def modify_state(key, value):
        state[key] = value
        return state[key]
    
    # 测试替代方案
    print("使用类:")
    counter_obj = Counter()
    print(f"增加5: {counter_obj.increment(5)}")
    print(f"当前值: {counter_obj.get_value()}")
    
    print("\n使用闭包:")
    inc, get = create_counter()
    print(f"增加3: {inc(3)}")
    print(f"当前值: {get()}")
    
    print("\n使用字典:")
    print(f"修改counter: {modify_state('counter', 10)}")
    print(f"修改status: {modify_state('status', 'active')}")
    print(f"当前状态: {state}")

def main():
    """
    主函数：演示所有global关键字概念
    """
    print("Python global关键字详解")
    print("=" * 50)
    
    # 演示各种global关键字概念
    demonstrate_basic_global()
    demonstrate_without_global()
    demonstrate_multiple_global()
    demonstrate_global_in_nested_functions()
    demonstrate_global_with_collections()
    demonstrate_global_scope_chain()
    practical_example_counter_system()
    practical_example_state_machine()
    demonstrate_global_best_practices()
    demonstrate_global_pitfalls()
    demonstrate_alternatives_to_global()
    
    print("\n=== 总结 ===")
    print("1. global关键字用于在函数内部修改全局变量")
    print("2. 只读取全局变量不需要global声明")
    print("3. global声明必须在变量使用之前")
    print("4. 可以同时声明多个全局变量")
    print("5. 合理使用global，考虑使用类、闭包等替代方案")
    
    # 显示最终的全局状态
    print("\n=== 最终全局状态 ===")
    print(f"counter: {counter}")
    print(f"app_status: {app_status}")
    print(f"user_data: {user_data}")
    print(f"settings: {settings}")

if __name__ == "__main__":
    main()
```

## 学习要点

### 核心概念
1. **global声明**：在函数内部声明全局变量
2. **修改权限**：允许函数修改全局变量
3. **声明位置**：必须在变量使用之前声明
4. **作用范围**：只影响当前函数作用域

### 重要规则
1. **读取规则**：读取全局变量不需要global
2. **修改规则**：修改全局变量必须使用global
3. **声明规则**：global声明必须在使用前
4. **集合规则**：修改集合内容不需要global，重新赋值需要

### 使用场景
1. **状态管理**：管理应用程序状态
2. **计数器**：实现全局计数功能
3. **配置修改**：动态修改全局配置
4. **缓存更新**：更新全局缓存数据

### 最佳实践
1. **最小化使用**：尽量减少global的使用
2. **明确命名**：函数名应表明会修改全局状态
3. **封装访问**：通过函数封装全局变量访问
4. **考虑替代**：使用类、闭包等替代方案

## 运行示例

在15-function-scope目录下运行：

```bash
python3 03_global_keyword.py
```

## 注意事项

1. **声明位置**：global必须在变量使用前声明
2. **过度使用**：避免在一个函数中修改太多全局变量
3. **测试困难**：全局状态使单元测试变得复杂
4. **副作用**：修改全局变量可能产生意外副作用

## 常见错误

1. **UnboundLocalError**：忘记使用global声明
2. **声明位置错误**：在使用后才声明global
3. **过度依赖**：过度使用global导致代码难以维护
4. **作用域混淆**：混淆局部变量和全局变量

## 下一步学习

掌握global关键字后，建议继续学习：
- [nonlocal关键字](05_nonlocal_keyword.md)
- [嵌套作用域](06_enclosing_scope.md)
- [作用域解析规则](08_scope_resolution.md)