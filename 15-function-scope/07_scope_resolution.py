#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
作用域解析LEGB规则 (Scope Resolution LEGB Rule)

LEGB是Python变量查找的顺序规则：
L - Local（局部作用域）
E - Enclosing（嵌套作用域）
G - Global（全局作用域）
B - Built-in（内置作用域）

学习目标：
1. 深入理解LEGB规则的工作原理
2. 掌握不同作用域的查找顺序
3. 了解作用域解析的实际应用
4. 学会调试作用域相关的问题
"""

# 全局变量
global_var = "全局变量"
shared_name = "全局的shared_name"

# 1. LEGB规则基础演示
def legb_basic_demo():
    """演示LEGB规则的基本工作原理"""
    print("=== LEGB规则基础演示 ===")
    
    # 局部变量
    local_var = "局部变量"
    shared_name = "局部的shared_name"  # 遮蔽全局变量
    
    def enclosing_function():
        # 嵌套作用域变量
        enclosing_var = "嵌套作用域变量"
        shared_name = "嵌套的shared_name"  # 遮蔽外层变量
        
        def inner_function():
            # 内层函数中的变量查找
            inner_var = "内层变量"
            
            print("=== 变量查找顺序演示 ===")
            
            # L - Local: 查找局部变量
            print(f"L - 局部变量 inner_var: {inner_var}")
            
            # E - Enclosing: 查找嵌套作用域变量
            print(f"E - 嵌套变量 enclosing_var: {enclosing_var}")
            
            # G - Global: 查找全局变量
            print(f"G - 全局变量 global_var: {global_var}")
            
            # B - Built-in: 查找内置变量
            print(f"B - 内置函数 len: {len}")
            
            # 变量遮蔽演示
            print(f"\n变量遮蔽演示 - shared_name: {shared_name}")
            print("(这里访问的是嵌套作用域的shared_name)")
        
        inner_function()
        print(f"\n嵌套函数中的shared_name: {shared_name}")
    
    enclosing_function()
    print(f"外层函数中的shared_name: {shared_name}")
    print(f"全局的shared_name: {globals()['shared_name']}")

# 2. 详细的LEGB查找演示
def detailed_legb_lookup():
    """详细演示LEGB查找过程"""
    print("\n=== 详细LEGB查找演示 ===")
    
    # 创建一个在不同作用域都存在的变量名
    variable_name = "外层函数的variable_name"
    
    def middle_function():
        variable_name = "中层函数的variable_name"
        
        def inner_function():
            # 演示从中层函数查找variable_name
            
            def innermost_function():
                # 在这里查找variable_name（从中层函数）
                print(f"最内层函数找到的variable_name: {variable_name}")
                print("查找路径: 最内层(无) -> 内层(无) -> 中层(找到!)")
                
                # 演示查找内置函数
                print(f"查找内置函数abs: {abs}")
                print("查找路径: 最内层(无) -> 内层(无) -> 中层(无) -> 外层(无) -> 全局(无) -> 内置(找到!)")
            
            innermost_function()
        
        inner_function()
        
        # 演示内层函数定义变量后的情况
        def inner_function_with_local():
            # 在内层函数中定义variable_name
            variable_name = "内层函数的variable_name"
            
            def another_innermost():
                print(f"\n另一个最内层函数找到的variable_name: {variable_name}")
                print("查找路径: 最内层(无) -> 内层(找到!)")
            
            another_innermost()
        
        inner_function_with_local()
    
    middle_function()

# 3. 作用域修改演示
def scope_modification_demo():
    """演示如何在不同作用域中修改变量"""
    print("\n=== 作用域修改演示 ===")
    
    # 全局变量
    global global_counter
    global_counter = 0
    
    # 外层函数变量
    enclosing_counter = 0
    
    def modify_scopes():
        # 局部变量
        local_counter = 0
        
        def inner_function():
            # 修改不同作用域的变量
            nonlocal enclosing_counter  # 修改嵌套作用域
            global global_counter       # 修改全局作用域
            
            # 修改局部变量（自动创建）
            local_counter = 10
            
            # 修改嵌套作用域变量
            enclosing_counter = 20
            
            # 修改全局变量
            global_counter = 30
            
            print(f"内层函数中:")
            print(f"  local_counter: {local_counter}")
            print(f"  enclosing_counter: {enclosing_counter}")
            print(f"  global_counter: {global_counter}")
        
        print(f"调用内层函数前:")
        print(f"  local_counter: {local_counter}")
        print(f"  enclosing_counter: {enclosing_counter}")
        print(f"  global_counter: {global_counter}")
        
        inner_function()
        
        print(f"调用内层函数后:")
        print(f"  local_counter: {local_counter}")
        print(f"  enclosing_counter: {enclosing_counter}")
        print(f"  global_counter: {global_counter}")
    
    modify_scopes()

# 4. 复杂的作用域嵌套
def complex_scope_nesting():
    """演示复杂的作用域嵌套情况"""
    print("\n=== 复杂作用域嵌套 ===")
    
    x = "level1_x"
    
    def level2():
        x = "level2_x"
        y = "level2_y"
        
        def level3():
            x = "level3_x"
            z = "level3_z"
            
            def level4():
                # level4不定义任何变量，全部从外层查找
                
                def level5():
                    x = "level5_x"  # 只定义x
                    
                    def level6():
                        # level6查找所有变量
                        print(f"Level6中的变量查找:")
                        print(f"  x: {x} (来自level5)")
                        print(f"  y: {y} (来自level2)")
                        print(f"  z: {z} (来自level3)")
                        
                        # 演示查找路径
                        print(f"\n查找路径分析:")
                        print(f"  x: L6(无) -> L5(找到) = {x}")
                        print(f"  y: L6(无) -> L5(无) -> L4(无) -> L3(无) -> L2(找到) = {y}")
                        print(f"  z: L6(无) -> L5(无) -> L4(无) -> L3(找到) = {z}")
                    
                    level6()
                
                level5()
            
            level4()
        
        level3()
    
    level2()

# 5. 作用域与闭包
def scope_and_closures():
    """演示作用域在闭包中的作用"""
    print("\n=== 作用域与闭包 ===")
    
    def create_multiplier(factor):
        """创建乘法器闭包"""
        
        def multiplier(value):
            # 访问外层的factor参数
            return value * factor
        
        # 显示闭包信息
        print(f"创建乘法器，factor={factor}")
        print(f"闭包变量: {multiplier.__closure__}")
        if multiplier.__closure__:
            print(f"闭包内容: {[cell.cell_contents for cell in multiplier.__closure__]}")
        
        return multiplier
    
    # 创建不同的乘法器
    multiply_by_2 = create_multiplier(2)
    multiply_by_5 = create_multiplier(5)
    
    # 测试闭包
    print(f"\n测试闭包:")
    print(f"multiply_by_2(10): {multiply_by_2(10)}")
    print(f"multiply_by_5(10): {multiply_by_5(10)}")
    
    # 演示闭包中的作用域查找
    def create_complex_closure():
        outer_var = "外层变量"
        
        def middle_function(middle_param):
            middle_var = "中层变量"
            
            def inner_function(inner_param):
                inner_var = "内层变量"
                
                # 这个函数可以访问所有外层变量
                result = f"{outer_var} + {middle_var} + {inner_var} + {middle_param} + {inner_param}"
                return result
            
            return inner_function
        
        return middle_function
    
    complex_closure = create_complex_closure()
    final_function = complex_closure("中层参数")
    result = final_function("内层参数")
    print(f"\n复杂闭包结果: {result}")

# 6. 作用域调试技巧
def scope_debugging_techniques():
    """演示作用域调试技巧"""
    print("\n=== 作用域调试技巧 ===")
    
    def debug_scopes():
        local_var = "局部变量"
        
        def inner_function():
            inner_var = "内层变量"
            
            # 调试技巧1: 使用locals()查看当前作用域
            print("当前局部作用域:")
            for name, value in locals().items():
                print(f"  {name}: {value}")
            
            # 调试技巧2: 使用globals()查看全局作用域
            print("\n全局作用域中的自定义变量:")
            for name, value in globals().items():
                if not name.startswith('__') and not callable(value):
                    print(f"  {name}: {value}")
            
            # 调试技巧3: 检查变量是否在不同作用域中存在
            test_vars = ['inner_var', 'local_var', 'global_var', 'nonexistent']
            
            print("\n变量存在性检查:")
            for var_name in test_vars:
                in_local = var_name in locals()
                in_global = var_name in globals()
                
                print(f"  {var_name}:")
                print(f"    在局部作用域: {in_local}")
                print(f"    在全局作用域: {in_global}")
                
                # 尝试访问变量
                try:
                    value = eval(var_name)
                    print(f"    可以访问，值为: {value}")
                except NameError:
                    print(f"    无法访问: NameError")
        
        inner_function()
    
    debug_scopes()

# 7. 作用域陷阱和常见错误
def scope_pitfalls():
    """演示作用域相关的常见陷阱"""
    print("\n=== 作用域陷阱和常见错误 ===")
    
    # 陷阱1: 循环变量的闭包问题
    print("陷阱1: 循环变量闭包问题")
    
    # 错误的方式
    functions = []
    for i in range(3):
        functions.append(lambda: i)  # 所有lambda都引用同一个i
    
    print("错误的闭包创建:")
    for j, func in enumerate(functions):
        print(f"  函数{j}返回: {func()}")
    
    # 正确的方式
    functions_correct = []
    for i in range(3):
        functions_correct.append(lambda x=i: x)  # 使用默认参数捕获i的值
    
    print("正确的闭包创建:")
    for j, func in enumerate(functions_correct):
        print(f"  函数{j}返回: {func()}")
    
    # 陷阱2: 意外的变量遮蔽
    print("\n陷阱2: 意外的变量遮蔽")
    
    def outer_function():
        data = [1, 2, 3, 4, 5]
        
        def process_data():
            # 意外创建了局部变量data，遮蔽了外层的data
            result = []
            for item in data:  # 这里会出错，因为下面定义了data
                result.append(item * 2)
            data = result  # 这行代码使得上面的data变成局部变量
            return data
        
        try:
            return process_data()
        except UnboundLocalError as e:
            print(f"  错误: {e}")
            print("  原因: 在函数中赋值给data使其成为局部变量，但在赋值前就使用了")
    
    outer_function()
    
    # 陷阱3: global和nonlocal的混淆
    print("\n陷阱3: global和nonlocal的混淆")
    
    global_var = "原始全局变量"
    
    def confusion_demo():
        global_var = "外层局部变量"
        
        def inner_wrong():
            global global_var  # 错误：这会修改真正的全局变量
            global_var = "错误修改"
        
        def inner_correct():
            nonlocal global_var  # 正确：这会修改外层的局部变量
            global_var = "正确修改"
        
        print(f"  修改前 - 外层: {global_var}, 全局: {globals()['global_var']}")
        
        inner_wrong()
        print(f"  错误修改后 - 外层: {global_var}, 全局: {globals()['global_var']}")
        
        inner_correct()
        print(f"  正确修改后 - 外层: {global_var}, 全局: {globals()['global_var']}")
    
    confusion_demo()

# 8. 作用域性能优化
def scope_performance_optimization():
    """演示作用域相关的性能优化"""
    print("\n=== 作用域性能优化 ===")
    
    import time
    
    # 优化1: 局部化全局变量访问
    def global_access_test():
        """测试全局变量访问性能"""
        start_time = time.time()
        
        # 直接访问全局变量（较慢）
        result = 0
        for i in range(100000):
            result += len([1, 2, 3])  # len是内置函数，需要查找
        
        end_time = time.time()
        return end_time - start_time, result
    
    def local_access_test():
        """测试局部变量访问性能"""
        start_time = time.time()
        
        # 局部化内置函数（较快）
        local_len = len
        result = 0
        for i in range(100000):
            result += local_len([1, 2, 3])
        
        end_time = time.time()
        return end_time - start_time, result
    
    global_time, global_result = global_access_test()
    local_time, local_result = local_access_test()
    
    print(f"全局访问时间: {global_time:.4f}秒, 结果: {global_result}")
    print(f"局部访问时间: {local_time:.4f}秒, 结果: {local_result}")
    print(f"性能提升: {global_time / local_time:.2f}倍")
    
    # 优化2: 避免深层嵌套查找
    def deep_nesting_slow():
        """深层嵌套的慢速版本"""
        def level1():
            var1 = "level1"
            def level2():
                var2 = "level2"
                def level3():
                    var3 = "level3"
                    def level4():
                        # 需要查找多层才能找到var1
                        return f"{var1}-{var2}-{var3}"
                    return level4
                return level3
            return level2
        
        func = level1()()()
        
        start_time = time.time()
        for _ in range(10000):
            result = func()
        end_time = time.time()
        
        return end_time - start_time, result
    
    def deep_nesting_fast():
        """优化后的版本"""
        def create_processor(var1, var2, var3):
            # 将需要的变量作为参数传递，避免深层查找
            def processor():
                return f"{var1}-{var2}-{var3}"
            return processor
        
        func = create_processor("level1", "level2", "level3")
        
        start_time = time.time()
        for _ in range(10000):
            result = func()
        end_time = time.time()
        
        return end_time - start_time, result
    
    slow_time, slow_result = deep_nesting_slow()
    fast_time, fast_result = deep_nesting_fast()
    
    print(f"\n深层嵌套查找时间: {slow_time:.4f}秒")
    print(f"优化后查找时间: {fast_time:.4f}秒")
    print(f"性能提升: {slow_time / fast_time:.2f}倍")

# 9. 实际应用案例
def practical_applications():
    """演示LEGB规则的实际应用案例"""
    print("\n=== 实际应用案例 ===")
    
    # 案例1: 配置管理系统
    class ConfigManager:
        """配置管理系统"""
        
        def __init__(self):
            self.global_config = {
                'debug': False,
                'timeout': 30,
                'retries': 3
            }
        
        def create_service(self, service_name, service_config=None):
            """创建服务，演示作用域的层次化配置"""
            if service_config is None:
                service_config = {}
            
            # 合并配置（全局 < 服务 < 方法）
            def get_config_value(key, method_config=None):
                if method_config is None:
                    method_config = {}
                
                # LEGB式的配置查找
                if key in method_config:  # L - 方法级配置
                    return method_config[key]
                elif key in service_config:  # E - 服务级配置
                    return service_config[key]
                elif key in self.global_config:  # G - 全局配置
                    return self.global_config[key]
                else:  # B - 默认值
                    defaults = {'debug': False, 'timeout': 10, 'retries': 1}
                    return defaults.get(key, None)
            
            def service_method(method_config=None):
                debug = get_config_value('debug', method_config)
                timeout = get_config_value('timeout', method_config)
                retries = get_config_value('retries', method_config)
                
                return {
                    'service': service_name,
                    'debug': debug,
                    'timeout': timeout,
                    'retries': retries
                }
            
            return service_method
    
    # 测试配置管理
    config_manager = ConfigManager()
    
    # 创建不同配置的服务
    web_service = config_manager.create_service('web', {'timeout': 60})
    db_service = config_manager.create_service('database', {'debug': True, 'retries': 5})
    
    print("配置管理系统演示:")
    print(f"Web服务默认配置: {web_service()}")
    print(f"Web服务方法配置: {web_service({'debug': True})}")
    print(f"数据库服务配置: {db_service()}")
    print(f"数据库服务方法配置: {db_service({'timeout': 120})}")
    
    # 案例2: 模板引擎
    def create_template_engine():
        """创建简单的模板引擎"""
        global_context = {'app_name': 'MyApp', 'version': '1.0'}
        
        def render_template(template, page_context=None):
            if page_context is None:
                page_context = {}
            
            def process_variable(var_name, local_context=None):
                if local_context is None:
                    local_context = {}
                
                # LEGB式的变量查找
                if var_name in local_context:  # L - 局部上下文
                    return local_context[var_name]
                elif var_name in page_context:  # E - 页面上下文
                    return page_context[var_name]
                elif var_name in global_context:  # G - 全局上下文
                    return global_context[var_name]
                else:  # B - 默认值
                    return f'{{未定义变量: {var_name}}}'
            
            # 简单的模板处理
            import re
            
            def replace_var(match):
                var_name = match.group(1)
                return str(process_variable(var_name))
            
            result = re.sub(r'\{\{(\w+)\}\}', replace_var, template)
            return result
        
        return render_template
    
    # 测试模板引擎
    template_engine = create_template_engine()
    
    template = "欢迎使用{{app_name}} v{{version}}！当前用户：{{username}}，页面：{{page_title}}"
    
    result1 = template_engine(template, {'username': 'Alice', 'page_title': '首页'})
    result2 = template_engine(template, {'username': 'Bob', 'page_title': '设置', 'app_name': '自定义应用'})
    
    print("\n模板引擎演示:")
    print(f"模板1: {result1}")
    print(f"模板2: {result2}")

# 主程序
if __name__ == "__main__":
    print("Python函数作用域学习 - LEGB作用域解析规则")
    print("=" * 60)
    
    # 1. LEGB基础演示
    legb_basic_demo()
    
    # 2. 详细查找演示
    detailed_legb_lookup()
    
    # 3. 作用域修改
    scope_modification_demo()
    
    # 4. 复杂嵌套
    complex_scope_nesting()
    
    # 5. 闭包应用
    scope_and_closures()
    
    # 6. 调试技巧
    scope_debugging_techniques()
    
    # 7. 常见陷阱
    scope_pitfalls()
    
    # 8. 性能优化
    scope_performance_optimization()
    
    # 9. 实际应用
    practical_applications()
    
    print("\n=== 学习总结 ===")
    print("1. LEGB规则定义了Python变量查找的顺序")
    print("2. L(Local) -> E(Enclosing) -> G(Global) -> B(Built-in)")
    print("3. 理解LEGB有助于避免变量遮蔽和作用域错误")
    print("4. 合理利用作用域层次可以实现优雅的设计模式")
    print("5. 局部化全局变量访问可以提高性能")
    print("6. 闭包是LEGB规则的重要应用场景")
    print("7. 调试作用域问题时要善用locals()和globals()")
    print("8. 避免过深的嵌套以保持代码可读性和性能")