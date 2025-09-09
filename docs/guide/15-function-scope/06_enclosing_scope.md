# 嵌套作用域（Enclosing Scope）

嵌套作用域是Python作用域系统中的重要组成部分，它允许内层函数访问外层函数的局部变量，是实现闭包和高级函数式编程的基础。

## 什么是嵌套作用域

嵌套作用域（Enclosing Scope）是指在嵌套函数结构中，内层函数可以访问外层函数的局部变量的作用域。这种作用域关系形成了一个作用域链，内层函数可以"看到"外层函数的变量。

## 嵌套作用域的特点

1. **层次结构**：形成多层嵌套的作用域链
2. **单向访问**：内层可以访问外层，外层不能访问内层
3. **变量遮蔽**：内层变量可以遮蔽外层同名变量
4. **闭包基础**：是实现闭包的基础机制

## 代码示例

### 基本嵌套作用域

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
嵌套作用域演示

本文件演示Python中嵌套作用域的概念和使用方法。
嵌套作用域允许内层函数访问外层函数的局部变量。
"""

def demonstrate_basic_enclosing_scope():
    """
    演示基本的嵌套作用域
    """
    print("=== 基本嵌套作用域 ===")
    
    def outer_function(x):
        # 外层函数的局部变量
        outer_var = "我是外层变量"
        outer_number = 100
        
        def inner_function(y):
            # 内层函数可以访问外层变量
            inner_var = "我是内层变量"
            print(f"内层函数访问:")
            print(f"  参数x: {x}")
            print(f"  参数y: {y}")
            print(f"  外层变量: {outer_var}")
            print(f"  外层数字: {outer_number}")
            print(f"  内层变量: {inner_var}")
            
            # 可以进行计算
            result = x + y + outer_number
            return result
        
        print(f"外层函数: outer_var = {outer_var}")
        return inner_function
    
    # 测试嵌套作用域
    inner_func = outer_function(10)
    result = inner_func(20)
    print(f"计算结果: {result}")

def demonstrate_multiple_levels():
    """
    演示多层嵌套作用域
    """
    print("\n=== 多层嵌套作用域 ===")
    
    def level1(a):
        var1 = "Level 1 变量"
        
        def level2(b):
            var2 = "Level 2 变量"
            
            def level3(c):
                var3 = "Level 3 变量"
                
                def level4(d):
                    var4 = "Level 4 变量"
                    
                    # Level 4 可以访问所有外层变量
                    print(f"Level 4 中访问所有变量:")
                    print(f"  参数: a={a}, b={b}, c={c}, d={d}")
                    print(f"  var1: {var1}")
                    print(f"  var2: {var2}")
                    print(f"  var3: {var3}")
                    print(f"  var4: {var4}")
                    
                    return a + b + c + d
                
                print(f"Level 3 中可以访问: var1={var1}, var2={var2}, var3={var3}")
                return level4
            
            print(f"Level 2 中可以访问: var1={var1}, var2={var2}")
            return level3
        
        print(f"Level 1 中可以访问: var1={var1}")
        return level2
    
    # 逐层调用
    func2 = level1(1)
    func3 = func2(2)
    func4 = func3(3)
    result = func4(4)
    print(f"最终结果: {result}")

def demonstrate_variable_shadowing():
    """
    演示变量遮蔽现象
    """
    print("\n=== 变量遮蔽现象 ===")
    
    def outer_function():
        name = "外层函数的name"
        value = 100
        
        def inner_function():
            # 内层定义同名变量，会遮蔽外层变量
            name = "内层函数的name"
            print(f"内层函数中:")
            print(f"  name: {name} (遮蔽了外层变量)")
            print(f"  value: {value} (来自外层)")
            
            def innermost_function():
                # 最内层也定义同名变量
                name = "最内层函数的name"
                value = 200
                print(f"最内层函数中:")
                print(f"  name: {name} (遮蔽了所有外层的name)")
                print(f"  value: {value} (遮蔽了外层的value)")
            
            innermost_function()
            print(f"回到内层函数: name={name}, value={value}")
        
        print(f"外层函数中: name={name}, value={value}")
        inner_function()
        print(f"外层函数结束: name={name}, value={value}")
    
    outer_function()

def demonstrate_scope_chain_lookup():
    """
    演示作用域链查找过程
    """
    print("\n=== 作用域链查找过程 ===")
    
    # 全局变量
    global_var = "全局变量"
    
    def outer_function():
        outer_var = "外层变量"
        # 注意：这里没有定义middle_var
        
        def middle_function():
            middle_var = "中间变量"
            # 注意：这里没有定义inner_var
            
            def inner_function():
                inner_var = "内层变量"
                
                print("作用域链查找演示:")
                print(f"  inner_var: {inner_var} (在当前作用域找到)")
                print(f"  middle_var: {middle_var} (在上一层作用域找到)")
                print(f"  outer_var: {outer_var} (在上两层作用域找到)")
                print(f"  global_var: {global_var} (在全局作用域找到)")
                
                # 尝试访问不存在的变量会报错
                try:
                    print(f"  nonexistent_var: {nonexistent_var}")
                except NameError as e:
                    print(f"  访问不存在的变量: {e}")
            
            return inner_function
        
        return middle_function
    
    # 执行嵌套函数
    middle_func = outer_function()
    inner_func = middle_func()
    inner_func()

def demonstrate_closure_creation():
    """
    演示闭包的创建过程
    """
    print("\n=== 闭包的创建过程 ===")
    
    def create_multiplier(factor):
        """创建一个乘法器闭包"""
        print(f"创建乘法器，因子为: {factor}")
        
        def multiplier(number):
            # 这个函数"记住"了外层的factor变量
            result = number * factor
            print(f"{number} × {factor} = {result}")
            return result
        
        return multiplier
    
    def create_accumulator(initial=0):
        """创建一个累加器闭包"""
        total = initial
        print(f"创建累加器，初始值为: {initial}")
        
        def accumulate(value):
            nonlocal total
            total += value
            print(f"累加 {value}，当前总和: {total}")
            return total
        
        def get_total():
            return total
        
        def reset(new_initial=0):
            nonlocal total
            old_total = total
            total = new_initial
            print(f"重置累加器: {old_total} -> {new_initial}")
            return old_total
        
        # 返回多个函数
        return accumulate, get_total, reset
    
    # 创建不同的乘法器
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    print("\n使用乘法器:")
    double(5)
    triple(4)
    double(7)
    
    # 创建累加器
    print("\n使用累加器:")
    add, get, reset = create_accumulator(10)
    
    add(5)
    add(3)
    print(f"当前总和: {get()}")
    
    reset(0)
    add(1)
    add(2)
    print(f"重置后总和: {get()}")

def demonstrate_practical_examples():
    """
    演示嵌套作用域的实际应用
    """
    print("\n=== 实际应用示例 ===")
    
    def create_validator(min_length=1, max_length=100):
        """创建字符串验证器"""
        def validate(text):
            if not isinstance(text, str):
                return False, "输入必须是字符串"
            
            length = len(text)
            if length < min_length:
                return False, f"长度不能少于{min_length}个字符"
            
            if length > max_length:
                return False, f"长度不能超过{max_length}个字符"
            
            return True, "验证通过"
        
        def get_rules():
            return {"min_length": min_length, "max_length": max_length}
        
        return validate, get_rules
    
    def create_cache(max_size=100):
        """创建简单的缓存系统"""
        cache = {}
        access_count = {}
        
        def get(key):
            if key in cache:
                access_count[key] = access_count.get(key, 0) + 1
                print(f"缓存命中: {key} (访问次数: {access_count[key]})")
                return cache[key]
            else:
                print(f"缓存未命中: {key}")
                return None
        
        def set(key, value):
            if len(cache) >= max_size:
                # 简单的LRU：删除访问次数最少的项
                least_used = min(access_count.items(), key=lambda x: x[1])[0]
                del cache[least_used]
                del access_count[least_used]
                print(f"缓存已满，删除最少使用的项: {least_used}")
            
            cache[key] = value
            access_count[key] = 0
            print(f"缓存设置: {key} = {value}")
        
        def get_stats():
            return {
                "size": len(cache),
                "max_size": max_size,
                "keys": list(cache.keys()),
                "access_count": access_count.copy()
            }
        
        def clear():
            cache.clear()
            access_count.clear()
            print("缓存已清空")
        
        return get, set, get_stats, clear
    
    # 测试验证器
    print("字符串验证器测试:")
    username_validator, get_username_rules = create_validator(3, 20)
    email_validator, get_email_rules = create_validator(5, 50)
    
    test_strings = ["ab", "alice", "a" * 25, "user@example.com"]
    
    for text in test_strings:
        valid, msg = username_validator(text)
        print(f"用户名 '{text}': {msg}")
    
    print(f"\n用户名规则: {get_username_rules()}")
    print(f"邮箱规则: {get_email_rules()}")
    
    # 测试缓存系统
    print("\n缓存系统测试:")
    get, set, stats, clear = create_cache(3)
    
    # 设置一些值
    set("user1", {"name": "Alice", "age": 25})
    set("user2", {"name": "Bob", "age": 30})
    set("user3", {"name": "Charlie", "age": 35})
    
    # 访问缓存
    print(get("user1"))
    print(get("user2"))
    print(get("user1"))  # 再次访问
    
    # 添加新项，触发LRU删除
    set("user4", {"name": "David", "age": 40})
    
    print(f"\n缓存统计: {stats()}")

def demonstrate_scope_debugging():
    """
    演示作用域调试技巧
    """
    print("\n=== 作用域调试技巧 ===")
    
    def debug_scope_example():
        outer_var = "外层变量"
        
        def inner_function():
            inner_var = "内层变量"
            
            # 使用locals()查看当前作用域的变量
            print("当前作用域的局部变量:")
            for name, value in locals().items():
                print(f"  {name}: {value}")
            
            # 使用globals()查看全局作用域的变量（部分）
            print("\n全局作用域的部分变量:")
            global_vars = {k: v for k, v in globals().items() 
                          if not k.startswith('__') and not callable(v)}
            for name, value in list(global_vars.items())[:5]:  # 只显示前5个
                print(f"  {name}: {value}")
            
            # 检查变量是否在不同作用域中存在
            def check_variable_existence(var_name):
                print(f"\n检查变量 '{var_name}' 的存在性:")
                
                # 检查局部作用域
                if var_name in locals():
                    print(f"  在局部作用域中找到: {locals()[var_name]}")
                
                # 检查全局作用域
                if var_name in globals():
                    print(f"  在全局作用域中找到: {globals()[var_name]}")
                
                # 检查内置作用域
                import builtins
                if hasattr(builtins, var_name):
                    print(f"  在内置作用域中找到: {getattr(builtins, var_name)}")
                
                if (var_name not in locals() and 
                    var_name not in globals() and 
                    not hasattr(builtins, var_name)):
                    print(f"  变量 '{var_name}' 不存在于任何作用域中")
            
            check_variable_existence("inner_var")
            check_variable_existence("outer_var")
            check_variable_existence("print")
            check_variable_existence("nonexistent_var")
        
        inner_function()
    
    debug_scope_example()

def demonstrate_performance_considerations():
    """
    演示嵌套作用域的性能考虑
    """
    print("\n=== 性能考虑 ===")
    
    import time
    
    def performance_test():
        # 测试变量访问性能
        outer_var = "外层变量"
        
        def test_local_access():
            local_var = "局部变量"
            start_time = time.time()
            
            for _ in range(100000):
                _ = local_var  # 访问局部变量
            
            return time.time() - start_time
        
        def test_enclosing_access():
            start_time = time.time()
            
            for _ in range(100000):
                _ = outer_var  # 访问外层变量
            
            return time.time() - start_time
        
        def test_global_access():
            start_time = time.time()
            
            for _ in range(100000):
                _ = global_var  # 访问全局变量
            
            return time.time() - start_time
        
        local_time = test_local_access()
        enclosing_time = test_enclosing_access()
        global_time = test_global_access()
        
        print(f"变量访问性能测试 (100,000次访问):")
        print(f"  局部变量访问: {local_time:.6f}秒")
        print(f"  外层变量访问: {enclosing_time:.6f}秒")
        print(f"  全局变量访问: {global_time:.6f}秒")
        
        print(f"\n性能比较:")
        print(f"  外层/局部比率: {enclosing_time/local_time:.2f}")
        print(f"  全局/局部比率: {global_time/local_time:.2f}")
    
    # 设置全局变量用于测试
    global global_var
    global_var = "全局变量"
    
    performance_test()

def demonstrate_memory_considerations():
    """
    演示内存相关的考虑
    """
    print("\n=== 内存考虑 ===")
    
    def create_closures():
        """创建多个闭包来观察内存使用"""
        closures = []
        
        for i in range(5):
            large_data = list(range(1000))  # 创建大量数据
            
            def closure(x, data=large_data, index=i):
                # 这个闭包会"记住"large_data
                return f"闭包{index}: {x} + 数据长度{len(data)}"
            
            closures.append(closure)
        
        return closures
    
    def demonstrate_memory_leak_risk():
        """演示可能的内存泄漏风险"""
        def parent_function():
            large_object = {f"key_{i}": f"value_{i}" for i in range(1000)}
            
            def child_function():
                # 即使不直接使用large_object，它也会被保持在内存中
                return "子函数执行完毕"
            
            return child_function
        
        # 创建闭包
        func = parent_function()
        
        print("创建了一个闭包，它间接引用了大对象")
        print("即使不直接使用大对象，它也会保持在内存中")
        print(f"闭包执行结果: {func()}")
        
        return func
    
    def demonstrate_proper_cleanup():
        """演示正确的清理方式"""
        def create_efficient_closure(data):
            # 只保留需要的数据
            needed_data = len(data)  # 只保留长度信息
            
            def efficient_closure(x):
                return f"处理 {x}，数据长度: {needed_data}"
            
            return efficient_closure
        
        large_data = list(range(10000))
        closure = create_efficient_closure(large_data)
        
        # large_data可以被垃圾回收，因为闭包只保留了长度信息
        del large_data
        
        return closure
    
    print("内存使用演示:")
    closures = create_closures()
    for i, closure in enumerate(closures):
        print(closure(10))
    
    print("\n内存泄漏风险演示:")
    risky_closure = demonstrate_memory_leak_risk()
    
    print("\n高效闭包演示:")
    efficient_closure = demonstrate_proper_cleanup()
    print(efficient_closure(42))

def main():
    """
    主函数：演示所有嵌套作用域概念
    """
    print("Python 嵌套作用域详解")
    print("=" * 50)
    
    # 演示各种嵌套作用域概念
    demonstrate_basic_enclosing_scope()
    demonstrate_multiple_levels()
    demonstrate_variable_shadowing()
    demonstrate_scope_chain_lookup()
    demonstrate_closure_creation()
    demonstrate_practical_examples()
    demonstrate_scope_debugging()
    demonstrate_performance_considerations()
    demonstrate_memory_considerations()
    
    print("\n=== 总结 ===")
    print("1. 嵌套作用域允许内层函数访问外层函数的变量")
    print("2. 变量查找遵循从内到外的顺序")
    print("3. 内层变量会遮蔽外层同名变量")
    print("4. 嵌套作用域是实现闭包的基础")
    print("5. 需要注意性能和内存使用")
    print("6. 合理使用嵌套作用域可以实现强大的功能")

if __name__ == "__main__":
    main()
```

## 学习要点

### 核心概念
1. **作用域链**：从内层到外层的变量查找链
2. **单向访问**：内层可以访问外层，反之不行
3. **变量遮蔽**：内层同名变量会隐藏外层变量
4. **闭包基础**：嵌套作用域是闭包实现的基础

### 重要特性
1. **层次结构**：可以有多层嵌套
2. **变量查找**：按照LEGB规则查找变量
3. **生命周期**：外层变量的生命周期可能被延长
4. **内存影响**：闭包会保持对外层变量的引用

### 实际应用
1. **闭包实现**：创建带状态的函数
2. **装饰器**：实现复杂的装饰器逻辑
3. **工厂函数**：创建定制化的函数
4. **状态管理**：在函数间保持状态

### 性能考虑
1. **访问速度**：局部变量 > 外层变量 > 全局变量
2. **内存使用**：闭包会保持外层变量的引用
3. **垃圾回收**：可能影响垃圾回收的效率
4. **优化建议**：只保留必要的外层变量引用

## 运行示例

在15-function-scope目录下运行：

```bash
python3 05_enclosing_scope.py
```

## 注意事项

1. **变量遮蔽**：注意内层变量对外层变量的遮蔽
2. **内存泄漏**：闭包可能导致内存泄漏
3. **性能影响**：过深的嵌套可能影响性能
4. **调试困难**：复杂的嵌套结构可能难以调试

## 常见错误

1. **UnboundLocalError**：在赋值前访问外层变量
2. **变量遮蔽混淆**：不理解变量遮蔽的规则
3. **内存泄漏**：闭包保持不必要的大对象引用
4. **作用域混淆**：不清楚变量来自哪个作用域

## 最佳实践

1. **明确变量来源**：使用清晰的变量命名
2. **避免深度嵌套**：保持合理的嵌套层次
3. **内存管理**：注意闭包的内存使用
4. **文档说明**：为复杂的嵌套结构添加注释

## 调试技巧

1. **使用locals()**：查看当前作用域的变量
2. **使用globals()**：查看全局作用域的变量
3. **变量存在性检查**：确认变量在哪个作用域中
4. **作用域可视化**：画出作用域结构图

## 下一步学习

掌握嵌套作用域后，建议继续学习：
- [内置作用域](07_built_in_scope.md)
- [作用域解析规则](08_scope_resolution.md)
- [综合练习](09_exercises.md)