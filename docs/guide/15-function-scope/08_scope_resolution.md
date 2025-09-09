# 作用域解析规则（LEGB Rule）

LEGB规则是Python中变量查找的核心机制，定义了Python解释器在查找变量时的搜索顺序。理解LEGB规则对于掌握Python的作用域系统、避免变量查找错误和编写高质量代码至关重要。

## 什么是LEGB规则

LEGB规则定义了Python中变量查找的顺序：
- **L (Local)**：局部作用域
- **E (Enclosing)**：嵌套作用域
- **G (Global)**：全局作用域
- **B (Built-in)**：内置作用域

Python解释器按照L → E → G → B的顺序查找变量，找到第一个匹配的变量后停止搜索。

## LEGB规则的工作原理

1. **查找顺序**：从内到外，从近到远
2. **停止条件**：找到第一个匹配的变量名
3. **查找失败**：如果所有作用域都没有找到，抛出NameError
4. **赋值规则**：赋值操作默认在当前作用域创建变量

## 代码示例

### LEGB规则基础演示

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LEGB作用域解析规则演示

本文件详细演示Python中LEGB（Local, Enclosing, Global, Built-in）
作用域解析规则的工作原理、查找顺序和实际应用。
"""

import builtins
import dis
import sys

# 全局变量（Global scope）
global_var = "我是全局变量"
shared_name = "全局作用域的shared_name"

def demonstrate_legb_basics():
    """
    演示LEGB规则的基本工作原理
    """
    print("=== LEGB规则基础演示 ===")
    
    # 局部变量（Local scope）
    local_var = "我是局部变量"
    shared_name = "局部作用域的shared_name"  # 遮蔽全局变量
    
    print(f"局部变量: {local_var}")
    print(f"共享名称（局部优先）: {shared_name}")
    print(f"全局变量: {global_var}")
    print(f"内置函数: {len('hello')}")
    
    # 演示查找顺序
    def inner_function():
        # 这里会按LEGB顺序查找变量
        print("\n在内部函数中:")
        print(f"  local_var（来自外层局部）: {local_var}")
        print(f"  shared_name（来自外层局部）: {shared_name}")
        print(f"  global_var（来自全局）: {global_var}")
        print(f"  len（来自内置）: {len}")
        
        # 内部函数的局部变量
        inner_local = "内部函数的局部变量"
        print(f"  inner_local（当前局部）: {inner_local}")
    
    inner_function()

def demonstrate_enclosing_scope():
    """
    演示嵌套作用域（Enclosing scope）
    """
    print("\n=== 嵌套作用域演示 ===")
    
    enclosing_var = "外层函数变量"
    shared_name = "外层函数的shared_name"
    
    def level1_function():
        level1_var = "第一层嵌套变量"
        shared_name = "第一层的shared_name"  # 遮蔽外层
        
        def level2_function():
            level2_var = "第二层嵌套变量"
            
            def level3_function():
                level3_var = "第三层嵌套变量"
                
                print("在第三层函数中的变量查找:")
                print(f"  level3_var（L-当前局部）: {level3_var}")
                print(f"  level2_var（E-第二层）: {level2_var}")
                print(f"  level1_var（E-第一层）: {level1_var}")
                print(f"  enclosing_var（E-外层函数）: {enclosing_var}")
                print(f"  shared_name（E-第一层，遮蔽了外层和全局）: {shared_name}")
                print(f"  global_var（G-全局）: {global_var}")
                print(f"  max（B-内置）: {max}")
                
                # 演示变量遮蔽
                max = "我遮蔽了内置的max函数"
                print(f"  遮蔽后的max: {max}")
                
                # 通过builtins访问原始max
                print(f"  原始max（通过builtins）: {builtins.max([1, 2, 3])}")
            
            level3_function()
        
        level2_function()
    
    level1_function()

def demonstrate_scope_modification():
    """
    演示作用域修改（global和nonlocal）
    """
    print("\n=== 作用域修改演示 ===")
    
    # 全局变量
    global global_counter
    global_counter = 0
    
    enclosing_counter = 0
    
    def modify_scopes():
        nonlocal enclosing_counter
        global global_counter
        
        # 局部变量
        local_counter = 0
        
        def inner_modify():
            nonlocal enclosing_counter, local_counter
            global global_counter
            
            # 修改各个作用域的变量
            local_counter += 1
            enclosing_counter += 1
            global_counter += 1
            
            print(f"修改后 - 局部: {local_counter}, 嵌套: {enclosing_counter}, 全局: {global_counter}")
        
        print(f"修改前 - 局部: {local_counter}, 嵌套: {enclosing_counter}, 全局: {global_counter}")
        inner_modify()
        print(f"外层函数中 - 局部: {local_counter}, 嵌套: {enclosing_counter}, 全局: {global_counter}")
    
    modify_scopes()
    print(f"全局作用域中 - 全局: {global_counter}")

def demonstrate_variable_lookup_process():
    """
    演示变量查找过程的详细步骤
    """
    print("\n=== 变量查找过程演示 ===")
    
    # 在不同作用域定义同名变量
    test_var = "全局的test_var"
    
    def outer_function():
        test_var = "外层函数的test_var"
        
        def middle_function():
            # 注意：这里没有定义test_var
            
            def inner_function():
                test_var = "内层函数的test_var"
                
                print("变量查找演示:")
                print(f"1. 在inner_function中查找test_var: {test_var}")
                print("   -> 找到：内层函数的test_var（Local scope）")
                
                def deepest_function():
                    # 这里没有定义test_var，需要向外查找
                    print(f"2. 在deepest_function中查找test_var: {test_var}")
                    print("   -> L: 当前函数没有")
                    print("   -> E: 在inner_function中找到（Enclosing scope）")
                
                deepest_function()
            
            inner_function()
            
            # 在middle_function中查找
            print(f"3. 在middle_function中查找test_var: {test_var}")
            print("   -> L: 当前函数没有")
            print("   -> E: 在outer_function中找到（Enclosing scope）")
        
        middle_function()
    
    outer_function()
    
    # 演示查找失败的情况
    def demonstrate_lookup_failure():
        print("\n变量查找失败演示:")
        
        def test_function():
            try:
                print(nonexistent_variable)  # 这个变量不存在
            except NameError as e:
                print(f"NameError: {e}")
                print("查找过程:")
                print("  -> L: 当前函数没有nonexistent_variable")
                print("  -> E: 外层函数没有nonexistent_variable")
                print("  -> G: 全局作用域没有nonexistent_variable")
                print("  -> B: 内置作用域没有nonexistent_variable")
                print("  -> 抛出NameError异常")
        
        test_function()
    
    demonstrate_lookup_failure()

def demonstrate_scope_inspection():
    """
    演示如何检查和分析作用域
    """
    print("\n=== 作用域检查演示 ===")
    
    def inspect_scopes():
        local_var = "局部变量"
        
        def inner_function():
            inner_local = "内层局部变量"
            
            print("作用域检查:")
            
            # 检查局部作用域
            print(f"1. 局部作用域 locals(): {list(locals().keys())}")
            
            # 检查全局作用域
            global_keys = [k for k in globals().keys() if not k.startswith('_')]
            print(f"2. 全局作用域 globals()（部分）: {global_keys[:10]}...")
            
            # 检查内置作用域
            builtin_keys = [k for k in dir(builtins) if not k.startswith('_')]
            print(f"3. 内置作用域 dir(builtins)（部分）: {builtin_keys[:10]}...")
            
            # 检查变量是否在不同作用域中
            def check_variable_location(var_name):
                print(f"\n检查变量 '{var_name}' 的位置:")
                
                if var_name in locals():
                    print(f"  ✓ 在局部作用域中: {locals()[var_name]}")
                elif var_name in globals():
                    print(f"  ✓ 在全局作用域中: {globals()[var_name]}")
                elif hasattr(builtins, var_name):
                    print(f"  ✓ 在内置作用域中: {getattr(builtins, var_name)}")
                else:
                    print(f"  ✗ 未找到变量 '{var_name}'")
            
            # 检查不同变量的位置
            check_variable_location('inner_local')
            check_variable_location('local_var')
            check_variable_location('global_var')
            check_variable_location('len')
            check_variable_location('nonexistent')
        
        inner_function()
    
    inspect_scopes()

def demonstrate_bytecode_analysis():
    """
    演示通过字节码分析变量查找
    """
    print("\n=== 字节码分析演示 ===")
    
    global_var_for_bytecode = "全局变量"
    
    def analyze_variable_access():
        local_var_for_bytecode = "局部变量"
        
        def inner_function():
            # 访问不同作用域的变量
            result = local_var_for_bytecode + global_var_for_bytecode + str(len([1, 2, 3]))
            return result
        
        print("字节码分析 - inner_function:")
        dis.dis(inner_function)
        
        print("\n字节码指令说明:")
        print("  LOAD_DEREF: 加载嵌套作用域变量（Enclosing）")
        print("  LOAD_GLOBAL: 加载全局作用域变量（Global）")
        print("  LOAD_FAST: 加载局部作用域变量（Local）")
        print("  LOAD_BUILTIN: 加载内置作用域变量（Built-in）")
        
        return inner_function()
    
    result = analyze_variable_access()
    print(f"\n执行结果: {result}")

def demonstrate_performance_implications():
    """
    演示LEGB规则的性能影响
    """
    print("\n=== 性能影响演示 ===")
    
    import time
    
    # 测试数据
    iterations = 1000000
    
    def test_local_access():
        """测试局部变量访问性能"""
        local_len = len  # 将内置函数赋值给局部变量
        data = [1, 2, 3, 4, 5]
        
        start_time = time.time()
        for _ in range(iterations):
            result = local_len(data)  # 访问局部变量
        end_time = time.time()
        
        return end_time - start_time
    
    def test_builtin_access():
        """测试内置函数访问性能"""
        data = [1, 2, 3, 4, 5]
        
        start_time = time.time()
        for _ in range(iterations):
            result = len(data)  # 直接访问内置函数
        end_time = time.time()
        
        return end_time - start_time
    
    def test_global_access():
        """测试全局变量访问性能"""
        data = [1, 2, 3, 4, 5]
        
        start_time = time.time()
        for _ in range(iterations):
            result = global_var  # 访问全局变量
        end_time = time.time()
        
        return end_time - start_time
    
    # 执行性能测试
    local_time = test_local_access()
    builtin_time = test_builtin_access()
    global_time = test_global_access()
    
    print(f"性能测试结果（{iterations}次迭代）:")
    print(f"  局部变量访问: {local_time:.6f}秒")
    print(f"  内置函数访问: {builtin_time:.6f}秒")
    print(f"  全局变量访问: {global_time:.6f}秒")
    
    print("\n性能优化建议:")
    print("1. 频繁使用的内置函数可以赋值给局部变量")
    print("2. 避免在循环中频繁访问全局变量")
    print("3. 局部变量访问速度最快")

def demonstrate_common_pitfalls():
    """
    演示LEGB规则的常见陷阱
    """
    print("\n=== 常见陷阱演示 ===")
    
    # 陷阱1：意外的变量遮蔽
    def pitfall_variable_shadowing():
        print("1. 变量遮蔽陷阱:")
        
        list = [1, 2, 3, 4, 5]  # 意外遮蔽了内置的list函数
        print(f"  定义了变量list: {list}")
        
        try:
            new_list = list((6, 7, 8))  # 尝试使用list函数
        except TypeError as e:
            print(f"  错误: {e}")
            print("  原因: 变量list遮蔽了内置的list函数")
        
        # 解决方案
        data_list = [1, 2, 3, 4, 5]  # 使用不同的变量名
        new_list = list((6, 7, 8))   # 现在可以正常使用list函数
        print(f"  解决方案: data_list={data_list}, new_list={new_list}")
    
    # 陷阱2：闭包中的变量绑定
    def pitfall_closure_binding():
        print("\n2. 闭包变量绑定陷阱:")
        
        # 错误的做法
        functions = []
        for i in range(3):
            functions.append(lambda: i)  # 所有lambda都引用同一个i
        
        print("  错误的闭包:")
        for j, func in enumerate(functions):
            print(f"    函数{j}(): {func()}")
        
        # 正确的做法
        functions_correct = []
        for i in range(3):
            functions_correct.append(lambda x=i: x)  # 使用默认参数捕获当前值
        
        print("  正确的闭包:")
        for j, func in enumerate(functions_correct):
            print(f"    函数{j}(): {func()}")
    
    # 陷阱3：UnboundLocalError
    def pitfall_unbound_local():
        print("\n3. UnboundLocalError陷阱:")
        
        counter = 0  # 外层变量
        
        def increment_wrong():
            try:
                print(counter)  # 尝试读取
                counter += 1    # 尝试修改，但没有声明nonlocal
            except UnboundLocalError as e:
                print(f"  错误: {e}")
                print("  原因: Python发现counter被赋值，认为它是局部变量")
                print("       但在赋值前尝试读取，导致UnboundLocalError")
        
        def increment_correct():
            nonlocal counter
            print(f"  修改前: {counter}")
            counter += 1
            print(f"  修改后: {counter}")
        
        print("  错误的做法:")
        increment_wrong()
        
        print("  正确的做法:")
        increment_correct()
    
    # 陷阱4：全局变量的意外修改
    def pitfall_global_modification():
        print("\n4. 全局变量意外修改陷阱:")
        
        global shared_name
        original_value = shared_name
        
        def modify_without_global():
            # 这会创建一个新的局部变量，而不是修改全局变量
            shared_name = "局部修改的值"
            print(f"  函数内部: {shared_name}")
        
        def modify_with_global():
            global shared_name
            shared_name = "全局修改的值"
            print(f"  函数内部: {shared_name}")
        
        print(f"  原始全局值: {shared_name}")
        
        modify_without_global()
        print(f"  调用modify_without_global后: {shared_name}")
        
        modify_with_global()
        print(f"  调用modify_with_global后: {shared_name}")
        
        # 恢复原始值
        shared_name = original_value
    
    # 执行所有陷阱演示
    pitfall_variable_shadowing()
    pitfall_closure_binding()
    pitfall_unbound_local()
    pitfall_global_modification()

def demonstrate_debugging_techniques():
    """
    演示LEGB相关的调试技巧
    """
    print("\n=== 调试技巧演示 ===")
    
    def debug_variable_lookup():
        print("1. 变量查找调试:")
        
        test_var = "局部变量"
        
        def debug_function():
            # 调试技巧：检查变量来源
            def trace_variable(var_name):
                print(f"\n  追踪变量 '{var_name}':")
                
                # 检查局部作用域
                if var_name in locals():
                    print(f"    ✓ 局部作用域: {locals()[var_name]}")
                    return
                
                # 检查嵌套作用域（通过frame检查）
                import inspect
                frame = inspect.currentframe()
                try:
                    outer_frame = frame.f_back
                    while outer_frame:
                        if var_name in outer_frame.f_locals:
                            print(f"    ✓ 嵌套作用域: {outer_frame.f_locals[var_name]}")
                            return
                        outer_frame = outer_frame.f_back
                finally:
                    del frame
                
                # 检查全局作用域
                if var_name in globals():
                    print(f"    ✓ 全局作用域: {globals()[var_name]}")
                    return
                
                # 检查内置作用域
                if hasattr(builtins, var_name):
                    print(f"    ✓ 内置作用域: {getattr(builtins, var_name)}")
                    return
                
                print(f"    ✗ 未找到变量 '{var_name}'")
            
            trace_variable('test_var')
            trace_variable('global_var')
            trace_variable('len')
            trace_variable('nonexistent')
        
        debug_function()
    
    def debug_scope_pollution():
        print("\n2. 作用域污染调试:")
        
        # 检查是否意外遮蔽了内置名称
        def check_builtin_shadowing():
            builtin_names = set(dir(builtins))
            local_names = set(locals().keys())
            global_names = set(globals().keys())
            
            local_shadows = local_names & builtin_names
            global_shadows = global_names & builtin_names
            
            if local_shadows:
                print(f"  警告: 局部变量遮蔽内置名称: {local_shadows}")
            
            if global_shadows:
                print(f"  警告: 全局变量遮蔽内置名称: {global_shadows}")
            
            if not local_shadows and not global_shadows:
                print("  ✓ 没有发现内置名称遮蔽")
        
        # 故意创建一些遮蔽
        list = "我遮蔽了list函数"
        dict = "我遮蔽了dict函数"
        
        check_builtin_shadowing()
    
    def debug_variable_lifetime():
        print("\n3. 变量生命周期调试:")
        
        def create_closure():
            captured_var = "被闭包捕获的变量"
            
            def closure():
                return captured_var
            
            return closure
        
        # 创建闭包
        my_closure = create_closure()
        
        # 检查闭包捕获的变量
        if hasattr(my_closure, '__closure__') and my_closure.__closure__:
            print("  闭包捕获的变量:")
            for i, cell in enumerate(my_closure.__closure__):
                print(f"    变量{i}: {cell.cell_contents}")
        
        print(f"  闭包执行结果: {my_closure()}")
    
    # 执行所有调试演示
    debug_variable_lookup()
    debug_scope_pollution()
    debug_variable_lifetime()

def demonstrate_advanced_applications():
    """
    演示LEGB规则的高级应用
    """
    print("\n=== 高级应用演示 ===")
    
    # 1. 动态作用域操作
    def dynamic_scope_demo():
        print("1. 动态作用域操作:")
        
        def create_scoped_function(scope_vars):
            """创建带有特定作用域变量的函数"""
            
            def scoped_function():
                # 动态访问传入的作用域变量
                for name, value in scope_vars.items():
                    locals()[name] = value
                    print(f"  动态设置: {name} = {value}")
                
                # 执行一些操作
                if 'x' in scope_vars and 'y' in scope_vars:
                    result = scope_vars['x'] + scope_vars['y']
                    print(f"  计算结果: x + y = {result}")
            
            return scoped_function
        
        # 创建带有不同作用域的函数
        func1 = create_scoped_function({'x': 10, 'y': 20, 'name': 'Function1'})
        func2 = create_scoped_function({'x': 5, 'y': 15, 'name': 'Function2'})
        
        func1()
        func2()
    
    # 2. 作用域链分析
    def scope_chain_analysis():
        print("\n2. 作用域链分析:")
        
        def analyze_scope_chain():
            import inspect
            
            def get_scope_chain():
                """获取当前的作用域链"""
                scopes = []
                frame = inspect.currentframe()
                
                try:
                    while frame:
                        scope_info = {
                            'function': frame.f_code.co_name,
                            'locals': list(frame.f_locals.keys()),
                            'filename': frame.f_code.co_filename.split('/')[-1],
                            'lineno': frame.f_lineno
                        }
                        scopes.append(scope_info)
                        frame = frame.f_back
                finally:
                    del frame
                
                return scopes
            
            def inner_function():
                local_var = "内层变量"
                
                def deepest_function():
                    deepest_var = "最深层变量"
                    
                    print("  作用域链分析:")
                    chain = get_scope_chain()
                    
                    for i, scope in enumerate(chain[:5]):  # 只显示前5层
                        print(f"    层级{i}: {scope['function']} (行{scope['lineno']})")
                        print(f"      局部变量: {scope['locals'][:5]}{'...' if len(scope['locals']) > 5 else ''}")
                
                deepest_function()
            
            inner_function()
        
        outer_var = "外层变量"
        analyze_scope_chain()
    
    # 3. 作用域装饰器
    def scope_decorator_demo():
        print("\n3. 作用域装饰器:")
        
        def with_local_cache(func):
            """为函数添加局部缓存的装饰器"""
            cache = {}  # 这个变量在装饰器的闭包中
            
            def wrapper(*args, **kwargs):
                # 创建缓存键
                key = str(args) + str(sorted(kwargs.items()))
                
                if key in cache:
                    print(f"  缓存命中: {key[:30]}...")
                    return cache[key]
                
                print(f"  计算结果: {key[:30]}...")
                result = func(*args, **kwargs)
                cache[key] = result
                return result
            
            # 添加缓存管理方法
            wrapper.clear_cache = lambda: cache.clear()
            wrapper.cache_info = lambda: f"缓存大小: {len(cache)}"
            
            return wrapper
        
        @with_local_cache
        def expensive_calculation(n):
            """模拟耗时计算"""
            import time
            time.sleep(0.1)  # 模拟计算时间
            return n * n
        
        # 测试缓存装饰器
        print("  测试缓存装饰器:")
        print(f"    第一次调用: {expensive_calculation(5)}")
        print(f"    第二次调用: {expensive_calculation(5)}")
        print(f"    {expensive_calculation.cache_info()}")
        
        expensive_calculation.clear_cache()
        print(f"    清理后: {expensive_calculation.cache_info()}")
    
    # 执行所有高级应用演示
    dynamic_scope_demo()
    scope_chain_analysis()
    scope_decorator_demo()

def main():
    """
    主函数：演示所有LEGB规则概念
    """
    print("Python LEGB作用域解析规则详解")
    print("=" * 50)
    
    # 演示各种LEGB概念
    demonstrate_legb_basics()
    demonstrate_enclosing_scope()
    demonstrate_scope_modification()
    demonstrate_variable_lookup_process()
    demonstrate_scope_inspection()
    demonstrate_bytecode_analysis()
    demonstrate_performance_implications()
    demonstrate_common_pitfalls()
    demonstrate_debugging_techniques()
    demonstrate_advanced_applications()
    
    print("\n=== 总结 ===")
    print("LEGB规则要点:")
    print("1. L (Local): 当前函数的局部作用域")
    print("2. E (Enclosing): 外层函数的作用域")
    print("3. G (Global): 模块的全局作用域")
    print("4. B (Built-in): Python的内置作用域")
    print("\n查找顺序: L → E → G → B")
    print("\n最佳实践:")
    print("- 避免变量名遮蔽")
    print("- 合理使用global和nonlocal")
    print("- 注意闭包中的变量绑定")
    print("- 利用局部变量提高性能")
    print("- 使用调试技巧排查作用域问题")

if __name__ == "__main__":
    main()
```

## 学习要点

### LEGB规则核心
1. **L (Local)**：当前函数的局部作用域
2. **E (Enclosing)**：外层函数的嵌套作用域
3. **G (Global)**：模块的全局作用域
4. **B (Built-in)**：Python的内置作用域

### 查找机制
1. **查找顺序**：L → E → G → B，找到即停止
2. **查找失败**：所有作用域都没找到时抛出NameError
3. **赋值规则**：赋值默认在当前作用域创建变量
4. **修改规则**：需要global或nonlocal声明才能修改外层变量

### 性能影响
1. **局部变量**：访问速度最快
2. **嵌套变量**：需要通过闭包访问，稍慢
3. **全局变量**：需要字典查找，较慢
4. **内置变量**：查找路径最长，最慢

### 常见陷阱
1. **变量遮蔽**：意外遮蔽内置函数或外层变量
2. **UnboundLocalError**：在赋值前读取局部变量
3. **闭包绑定**：循环中创建闭包的变量绑定问题
4. **作用域污染**：全局变量过多或命名冲突

## 运行示例

在15-function-scope目录下运行：

```bash
python3 07_scope_resolution.py
```

## 注意事项

1. **变量遮蔽**：避免使用与内置函数同名的变量
2. **性能考虑**：频繁访问的全局变量可以赋值给局部变量
3. **调试困难**：复杂的嵌套作用域可能难以调试
4. **内存泄漏**：闭包可能导致变量无法被垃圾回收

## 常见错误

1. **NameError**：变量未定义或拼写错误
2. **UnboundLocalError**：局部变量在赋值前被引用
3. **变量遮蔽**：意外遮蔽了重要的变量或函数
4. **作用域混淆**：不清楚变量来自哪个作用域

## 最佳实践

1. **避免遮蔽**：使用描述性的变量名，避免与内置名称冲突
2. **明确声明**：需要修改外层变量时明确使用global或nonlocal
3. **局部优化**：将频繁使用的全局变量或内置函数赋值给局部变量
4. **作用域最小化**：尽量减小变量的作用域范围

## 调试技巧

1. **使用locals()和globals()**：检查当前作用域的变量
2. **使用dir(builtins)**：查看内置作用域的内容
3. **使用dis模块**：分析字节码了解变量访问方式
4. **使用inspect模块**：检查函数的作用域链

## 性能优化

1. **局部变量缓存**：将频繁使用的全局变量赋值给局部变量
2. **避免深层嵌套**：减少作用域查找的层数
3. **合理使用闭包**：避免不必要的变量捕获
4. **基准测试**：对性能敏感的代码进行测试

## 下一步学习

掌握LEGB规则后，建议继续学习：
- [综合练习](09_exercises.md)
- 装饰器和闭包的高级应用
- 元编程和动态作用域操作