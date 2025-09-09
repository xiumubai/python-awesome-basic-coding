# nonlocal关键字

nonlocal关键字是Python 3中引入的重要特性，用于在嵌套函数中修改外层函数的局部变量，是实现闭包和高级函数式编程的关键工具。

## 什么是nonlocal关键字

nonlocal关键字用于在嵌套函数中声明一个变量引用外层函数的局部变量，使得内层函数可以修改外层函数的局部变量。这是Python 3中新增的功能，解决了嵌套函数中变量修改的问题。

## nonlocal关键字的作用

1. **修改外层变量**：允许内层函数修改外层函数的局部变量
2. **实现闭包**：是实现闭包的重要工具
3. **状态保持**：在函数调用间保持状态
4. **避免全局变量**：提供了全局变量的替代方案

## 代码示例

### 基本nonlocal关键字使用

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nonlocal关键字演示

本文件演示Python中nonlocal关键字的使用方法和实际应用。
nonlocal关键字用于在嵌套函数中修改外层函数的局部变量。
"""

def demonstrate_basic_nonlocal():
    """
    演示nonlocal关键字的基本使用
    """
    print("=== nonlocal关键字基本使用 ===")
    
    def outer_function():
        # 外层函数的局部变量
        count = 0
        message = "Hello"
        
        def inner_function():
            # 使用nonlocal声明要修改外层变量
            nonlocal count, message
            count += 1
            message += " World"
            print(f"内层函数: count={count}, message={message}")
        
        print(f"调用前: count={count}, message={message}")
        inner_function()
        print(f"调用后: count={count}, message={message}")
        
        return inner_function
    
    # 测试基本用法
    func = outer_function()
    print("再次调用返回的函数:")
    func()

def demonstrate_without_nonlocal():
    """
    演示不使用nonlocal的后果
    """
    print("\n=== 不使用nonlocal的后果 ===")
    
    def outer_function():
        count = 0
        
        def inner_without_nonlocal():
            # 不使用nonlocal，只能读取外层变量
            print(f"只能读取: count={count}")
            # count += 1  # 这会引发UnboundLocalError
        
        def inner_create_local():
            # 这会创建一个新的局部变量
            count = 100
            print(f"创建局部变量: count={count}")
        
        def inner_try_modify():
            try:
                # 尝试修改但没有nonlocal声明
                print(f"尝试读取: {count}")
                # count += 1  # 取消注释会出错
            except UnboundLocalError as e:
                print(f"UnboundLocalError: {e}")
        
        print(f"外层函数: count={count}")
        inner_without_nonlocal()
        inner_create_local()
        print(f"外层函数: count={count} (未被修改)")
        inner_try_modify()
    
    outer_function()

def demonstrate_nonlocal_vs_global():
    """
    演示nonlocal与global的区别
    """
    print("\n=== nonlocal vs global ===")
    
    # 全局变量
    global_var = "全局变量"
    
    def outer_function():
        # 外层局部变量
        local_var = "外层局部变量"
        
        def inner_function():
            # 使用global访问全局变量
            global global_var
            global_var = "修改后的全局变量"
            
            # 使用nonlocal访问外层局部变量
            nonlocal local_var
            local_var = "修改后的外层局部变量"
            
            print(f"内层函数修改后:")
            print(f"  global_var: {global_var}")
            print(f"  local_var: {local_var}")
        
        print(f"修改前:")
        print(f"  global_var: {global_var}")
        print(f"  local_var: {local_var}")
        
        inner_function()
        
        print(f"外层函数中:")
        print(f"  global_var: {global_var}")
        print(f"  local_var: {local_var}")
    
    outer_function()
    print(f"全局作用域中: global_var: {global_var}")

def demonstrate_closure_with_nonlocal():
    """
    演示使用nonlocal实现闭包
    """
    print("\n=== 使用nonlocal实现闭包 ===")
    
    def create_counter(initial=0):
        """创建一个计数器闭包"""
        count = initial
        
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
            old_count = count
            count = value
            return old_count
        
        # 返回操作函数
        return increment, decrement, get_count, reset
    
    # 创建两个独立的计数器
    inc1, dec1, get1, reset1 = create_counter(10)
    inc2, dec2, get2, reset2 = create_counter(100)
    
    print("计数器1操作:")
    print(f"初始值: {get1()}")
    print(f"增加5: {inc1(5)}")
    print(f"减少3: {dec1(3)}")
    print(f"当前值: {get1()}")
    
    print("\n计数器2操作:")
    print(f"初始值: {get2()}")
    print(f"增加20: {inc2(20)}")
    print(f"当前值: {get2()}")
    
    print(f"\n重置计数器1: 旧值={reset1()}, 新值={get1()}")
    print(f"计数器2不受影响: {get2()}")

def demonstrate_multiple_levels():
    """
    演示多层嵌套中的nonlocal
    """
    print("\n=== 多层嵌套中的nonlocal ===")
    
    def level1():
        var1 = "Level 1"
        
        def level2():
            var2 = "Level 2"
            
            def level3():
                var3 = "Level 3"
                
                def level4():
                    # 可以修改任何外层的变量
                    nonlocal var1, var2, var3
                    
                    print(f"Level 4 修改前:")
                    print(f"  var1: {var1}")
                    print(f"  var2: {var2}")
                    print(f"  var3: {var3}")
                    
                    var1 += " (modified by level4)"
                    var2 += " (modified by level4)"
                    var3 += " (modified by level4)"
                    
                    print(f"Level 4 修改后:")
                    print(f"  var1: {var1}")
                    print(f"  var2: {var2}")
                    print(f"  var3: {var3}")
                
                level4()
                print(f"Level 3 中: var3={var3}")
            
            level3()
            print(f"Level 2 中: var2={var2}")
        
        level2()
        print(f"Level 1 中: var1={var1}")
    
    level1()

def practical_example_state_machine():
    """
    实际应用示例：状态机
    """
    print("\n=== 实际应用：状态机 ===")
    
    def create_state_machine(initial_state="idle"):
        """创建一个状态机"""
        current_state = initial_state
        state_history = [initial_state]
        
        def get_state():
            return current_state
        
        def set_state(new_state):
            nonlocal current_state
            if new_state != current_state:
                old_state = current_state
                current_state = new_state
                state_history.append(new_state)
                print(f"状态变化: {old_state} -> {new_state}")
                return True
            return False
        
        def get_history():
            return state_history.copy()
        
        def can_transition(from_state, to_state):
            # 定义状态转换规则
            transitions = {
                "idle": ["running", "error"],
                "running": ["paused", "stopped", "error"],
                "paused": ["running", "stopped"],
                "stopped": ["idle"],
                "error": ["idle"]
            }
            return to_state in transitions.get(from_state, [])
        
        def transition_to(new_state):
            nonlocal current_state
            if can_transition(current_state, new_state):
                return set_state(new_state)
            else:
                print(f"无效转换: {current_state} -> {new_state}")
                return False
        
        def reset():
            nonlocal current_state
            current_state = initial_state
            state_history.clear()
            state_history.append(initial_state)
            print(f"状态机已重置为: {initial_state}")
        
        return get_state, transition_to, get_history, reset
    
    # 创建状态机
    get_state, transition, get_history, reset = create_state_machine()
    
    print(f"初始状态: {get_state()}")
    
    # 测试状态转换
    transition("running")
    transition("paused")
    transition("running")
    transition("stopped")
    transition("idle")
    
    print(f"状态历史: {get_history()}")
    
    # 测试无效转换
    transition("paused")  # 从idle不能直接到paused
    
    reset()
    print(f"重置后状态: {get_state()}")
    print(f"重置后历史: {get_history()}")

def practical_example_decorator_with_state():
    """
    实际应用示例：带状态的装饰器
    """
    print("\n=== 实际应用：带状态的装饰器 ===")
    
    def call_counter(func):
        """计算函数调用次数的装饰器"""
        count = 0
        
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            print(f"函数 {func.__name__} 第 {count} 次调用")
            result = func(*args, **kwargs)
            return result
        
        def get_count():
            return count
        
        def reset_count():
            nonlocal count
            old_count = count
            count = 0
            return old_count
        
        # 将计数器函数附加到wrapper上
        wrapper.get_count = get_count
        wrapper.reset_count = reset_count
        
        return wrapper
    
    def timing_decorator(func):
        """计算函数执行时间的装饰器"""
        import time
        total_time = 0
        call_count = 0
        
        def wrapper(*args, **kwargs):
            nonlocal total_time, call_count
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            
            execution_time = end_time - start_time
            total_time += execution_time
            call_count += 1
            
            print(f"函数 {func.__name__} 执行时间: {execution_time:.4f}秒")
            return result
        
        def get_stats():
            if call_count > 0:
                return {
                    "total_time": total_time,
                    "call_count": call_count,
                    "average_time": total_time / call_count
                }
            return {"total_time": 0, "call_count": 0, "average_time": 0}
        
        wrapper.get_stats = get_stats
        return wrapper
    
    # 使用装饰器
    @call_counter
    def greet(name):
        return f"Hello, {name}!"
    
    @timing_decorator
    def slow_function(n):
        import time
        time.sleep(0.01)  # 模拟耗时操作
        return sum(range(n))
    
    # 测试装饰器
    print(greet("Alice"))
    print(greet("Bob"))
    print(greet("Charlie"))
    print(f"greet函数调用次数: {greet.get_count()}")
    
    print(f"\n重置前调用次数: {greet.reset_count()}")
    print(f"重置后调用次数: {greet.get_count()}")
    
    # 测试计时装饰器
    print(f"\n计算结果: {slow_function(1000)}")
    print(f"计算结果: {slow_function(2000)}")
    stats = slow_function.get_stats()
    print(f"执行统计: {stats}")

def demonstrate_nonlocal_with_classes():
    """
    演示nonlocal与类的结合使用
    """
    print("\n=== nonlocal与类的结合 ===")
    
    def create_class_factory():
        """创建类的工厂函数"""
        class_count = 0
        
        def create_counter_class(name):
            nonlocal class_count
            class_count += 1
            
            class Counter:
                def __init__(self, initial=0):
                    self.value = initial
                    self.class_id = class_count
                    self.class_name = name
                
                def increment(self, step=1):
                    self.value += step
                    return self.value
                
                def __str__(self):
                    return f"{self.class_name}#{self.class_id}(value={self.value})"
            
            return Counter
        
        def get_class_count():
            return class_count
        
        return create_counter_class, get_class_count
    
    # 使用类工厂
    create_class, get_count = create_class_factory()
    
    CounterA = create_class("CounterA")
    CounterB = create_class("CounterB")
    
    print(f"已创建类的数量: {get_count()}")
    
    # 创建实例
    counter1 = CounterA(10)
    counter2 = CounterB(20)
    
    print(f"Counter1: {counter1}")
    print(f"Counter2: {counter2}")
    
    counter1.increment(5)
    counter2.increment(3)
    
    print(f"增加后 Counter1: {counter1}")
    print(f"增加后 Counter2: {counter2}")

def demonstrate_nonlocal_best_practices():
    """
    演示nonlocal的最佳实践
    """
    print("\n=== nonlocal最佳实践 ===")
    
    # 最佳实践1：明确的变量命名
    def good_practice_naming():
        """好的做法：使用明确的变量名"""
        user_count = 0
        error_count = 0
        
        def process_user(user_data):
            nonlocal user_count, error_count
            
            try:
                # 处理用户数据
                if user_data and "name" in user_data:
                    user_count += 1
                    return f"处理用户: {user_data['name']}"
                else:
                    error_count += 1
                    return "用户数据无效"
            except Exception:
                error_count += 1
                return "处理出错"
        
        def get_statistics():
            return {
                "processed_users": user_count,
                "errors": error_count,
                "success_rate": user_count / (user_count + error_count) if (user_count + error_count) > 0 else 0
            }
        
        return process_user, get_statistics
    
    # 最佳实践2：限制nonlocal的范围
    def good_practice_limited_scope():
        """好的做法：限制nonlocal的使用范围"""
        state = {"value": 0, "modified": False}
        
        def safe_modify(new_value):
            # 只修改需要修改的部分
            nonlocal state
            if isinstance(new_value, (int, float)) and new_value >= 0:
                state = {"value": new_value, "modified": True}
                return True
            return False
        
        def get_state():
            return state.copy()  # 返回副本，防止外部修改
        
        return safe_modify, get_state
    
    # 测试最佳实践
    process, get_stats = good_practice_naming()
    
    print("处理用户数据:")
    print(process({"name": "Alice", "age": 25}))
    print(process({"name": "Bob"}))
    print(process({}))  # 无效数据
    print(process({"name": "Charlie", "email": "charlie@example.com"}))
    
    stats = get_stats()
    print(f"处理统计: {stats}")
    
    print("\n安全修改示例:")
    modify, get_state = good_practice_limited_scope()
    print(f"初始状态: {get_state()}")
    print(f"修改为10: {modify(10)}")
    print(f"修改后状态: {get_state()}")
    print(f"修改为-5: {modify(-5)}")
    print(f"最终状态: {get_state()}")

def demonstrate_common_pitfalls():
    """
    演示nonlocal的常见陷阱
    """
    print("\n=== nonlocal常见陷阱 ===")
    
    # 陷阱1：忘记使用nonlocal
    def pitfall_forgot_nonlocal():
        count = 0
        
        def increment():
            # 忘记使用nonlocal，创建了局部变量
            count = 1  # 这不会修改外层的count
            print(f"函数内count: {count}")
        
        print(f"修改前: {count}")
        increment()
        print(f"修改后: {count} (未被修改)")
    
    # 陷阱2：nonlocal声明位置错误
    def pitfall_wrong_position():
        value = 10
        
        def modify():
            try:
                print(f"尝试使用value: {value}")
                # nonlocal value  # 如果放在这里就太晚了
                # value += 1
            except UnboundLocalError as e:
                print(f"错误: {e}")
        
        modify()
    
    # 陷阱3：过度使用nonlocal
    def pitfall_overuse():
        var1, var2, var3, var4, var5 = 1, 2, 3, 4, 5
        
        def bad_function():
            # 修改太多外层变量，难以理解和维护
            nonlocal var1, var2, var3, var4, var5
            var1 += 1
            var2 *= 2
            var3 -= 1
            var4 /= 2
            var5 **= 2
            print("修改了太多变量，难以跟踪")
        
        bad_function()
    
    print("演示各种陷阱:")
    pitfall_forgot_nonlocal()
    pitfall_wrong_position()
    pitfall_overuse()

def main():
    """
    主函数：演示所有nonlocal关键字概念
    """
    print("Python nonlocal关键字详解")
    print("=" * 50)
    
    # 演示各种nonlocal关键字概念
    demonstrate_basic_nonlocal()
    demonstrate_without_nonlocal()
    demonstrate_nonlocal_vs_global()
    demonstrate_closure_with_nonlocal()
    demonstrate_multiple_levels()
    practical_example_state_machine()
    practical_example_decorator_with_state()
    demonstrate_nonlocal_with_classes()
    demonstrate_nonlocal_best_practices()
    demonstrate_common_pitfalls()
    
    print("\n=== 总结 ===")
    print("1. nonlocal用于在嵌套函数中修改外层函数的局部变量")
    print("2. nonlocal是实现闭包的重要工具")
    print("3. nonlocal声明必须在变量使用之前")
    print("4. nonlocal提供了全局变量的替代方案")
    print("5. 合理使用nonlocal可以实现复杂的状态管理")
    print("6. 避免过度使用nonlocal，保持代码的可读性")

if __name__ == "__main__":
    main()
```

## 学习要点

### 核心概念
1. **nonlocal声明**：在嵌套函数中声明外层变量
2. **作用范围**：只能访问外层函数的局部变量
3. **修改权限**：允许内层函数修改外层变量
4. **闭包实现**：是实现闭包的关键工具

### 重要特性
1. **嵌套限制**：只能在嵌套函数中使用
2. **层次访问**：可以访问任意外层的变量
3. **声明位置**：必须在变量使用前声明
4. **Python 3特性**：Python 2中不可用

### 实际应用
1. **闭包实现**：创建带状态的函数
2. **装饰器**：实现带状态的装饰器
3. **状态机**：管理复杂的状态转换
4. **工厂函数**：创建具有私有状态的对象

### 与global的区别
1. **作用域不同**：nonlocal访问外层函数，global访问全局
2. **使用场景**：nonlocal用于嵌套函数，global用于任何函数
3. **状态隔离**：nonlocal提供更好的状态隔离
4. **测试友好**：nonlocal比global更容易测试

## 运行示例

在15-function-scope目录下运行：

```bash
python3 04_nonlocal_keyword.py
```

## 注意事项

1. **Python版本**：只在Python 3中可用
2. **声明位置**：必须在变量使用前声明
3. **嵌套要求**：只能在嵌套函数中使用
4. **过度使用**：避免在一个函数中修改太多外层变量

## 常见错误

1. **SyntaxError**：在Python 2中使用nonlocal
2. **UnboundLocalError**：忘记使用nonlocal声明
3. **声明位置错误**：在使用后才声明nonlocal
4. **作用域混淆**：混淆nonlocal和global的使用场景

## 最佳实践

1. **明确命名**：使用有意义的变量名
2. **限制范围**：避免修改太多外层变量
3. **文档说明**：清楚说明闭包的用途
4. **状态封装**：通过闭包实现状态封装

## 下一步学习

掌握nonlocal关键字后，建议继续学习：
- [嵌套作用域](06_enclosing_scope.md)
- [内置作用域](07_built_in_scope.md)
- [作用域解析规则](08_scope_resolution.md)