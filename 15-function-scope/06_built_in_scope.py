#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
内置作用域 (Built-in Scope)

内置作用域包含Python解释器启动时自动加载的内置函数、异常和常量。
这是Python作用域链中的最外层，当在其他作用域中找不到变量时，
最终会在内置作用域中查找。

学习目标：
1. 理解内置作用域的概念和作用
2. 了解常用的内置函数和常量
3. 掌握如何查看和使用内置对象
4. 理解内置作用域在LEGB规则中的位置
"""

import builtins

# 1. 查看内置作用域
def explore_builtin_scope():
    """探索内置作用域的内容"""
    print("=== 探索内置作用域 ===")
    
    # 获取所有内置名称
    builtin_names = dir(builtins)
    print(f"内置对象总数: {len(builtin_names)}")
    
    # 分类显示内置对象
    functions = []
    exceptions = []
    constants = []
    types = []
    
    for name in builtin_names:
        obj = getattr(builtins, name)
        if callable(obj):
            if isinstance(obj, type) and issubclass(obj, BaseException):
                exceptions.append(name)
            elif isinstance(obj, type):
                types.append(name)
            else:
                functions.append(name)
        else:
            constants.append(name)
    
    print(f"\n内置函数数量: {len(functions)}")
    print(f"内置类型数量: {len(types)}")
    print(f"内置异常数量: {len(exceptions)}")
    print(f"内置常量数量: {len(constants)}")
    
    # 显示一些常用的内置对象
    print("\n常用内置函数:")
    common_functions = ['print', 'len', 'range', 'enumerate', 'zip', 'map', 'filter']
    for func in common_functions:
        if func in functions:
            print(f"  {func}: {getattr(builtins, func).__doc__.split('.')[0] if getattr(builtins, func).__doc__ else '无文档'}")
    
    print("\n常用内置类型:")
    common_types = ['int', 'str', 'list', 'dict', 'tuple', 'set']
    for typ in common_types:
        if typ in types:
            print(f"  {typ}: {getattr(builtins, typ).__doc__.split('.')[0] if getattr(builtins, typ).__doc__ else '无文档'}")
    
    print("\n内置常量:")
    for const in constants:
        value = getattr(builtins, const)
        print(f"  {const}: {value} ({type(value).__name__})")

# 2. 常用内置函数演示
def builtin_functions_demo():
    """演示常用内置函数的使用"""
    print("\n=== 常用内置函数演示 ===")
    
    # 数据处理函数
    data = [1, 2, 3, 4, 5]
    print(f"原始数据: {data}")
    print(f"len(data): {len(data)}")
    print(f"sum(data): {sum(data)}")
    print(f"max(data): {max(data)}")
    print(f"min(data): {min(data)}")
    print(f"sorted(data, reverse=True): {sorted(data, reverse=True)}")
    
    # 类型转换函数
    print("\n类型转换函数:")
    number = 42
    print(f"int('123'): {int('123')}")
    print(f"str({number}): {str(number)}")
    print(f"float('3.14'): {float('3.14')}")
    print(f"bool(0): {bool(0)}, bool(1): {bool(1)}")
    print(f"list('hello'): {list('hello')}")
    print(f"tuple([1,2,3]): {tuple([1,2,3])}")
    
    # 迭代和序列函数
    print("\n迭代和序列函数:")
    print(f"range(5): {list(range(5))}")
    print(f"enumerate(['a','b','c']): {list(enumerate(['a','b','c']))}")
    print(f"zip([1,2,3], ['a','b','c']): {list(zip([1,2,3], ['a','b','c']))}")
    
    # 高阶函数
    print("\n高阶函数:")
    numbers = [1, 2, 3, 4, 5]
    print(f"map(lambda x: x*2, {numbers}): {list(map(lambda x: x*2, numbers))}")
    print(f"filter(lambda x: x%2==0, {numbers}): {list(filter(lambda x: x%2==0, numbers))}")
    
    # 对象检查函数
    print("\n对象检查函数:")
    print(f"isinstance(42, int): {isinstance(42, int)}")
    print(f"hasattr('hello', 'upper'): {hasattr('hello', 'upper')}")
    print(f"callable(print): {callable(print)}")
    print(f"id('hello'): {id('hello')}")
    print(f"type(42): {type(42)}")

# 3. 内置异常演示
def builtin_exceptions_demo():
    """演示内置异常的使用"""
    print("\n=== 内置异常演示 ===")
    
    # 常见异常类型
    exceptions_demo = [
        ("ValueError", lambda: int("not_a_number")),
        ("TypeError", lambda: "string" + 42),
        ("IndexError", lambda: [1, 2, 3][10]),
        ("KeyError", lambda: {'a': 1}['b']),
        ("AttributeError", lambda: "string".nonexistent_method()),
        ("ZeroDivisionError", lambda: 1 / 0),
    ]
    
    for exception_name, func in exceptions_demo:
        try:
            func()
        except Exception as e:
            print(f"{exception_name}: {type(e).__name__} - {e}")
    
    # 自定义异常处理
    print("\n自定义异常处理:")
    def safe_divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "不能除以零"
        except TypeError:
            return "类型错误：请提供数字"
    
    print(f"safe_divide(10, 2): {safe_divide(10, 2)}")
    print(f"safe_divide(10, 0): {safe_divide(10, 0)}")
    print(f"safe_divide(10, 'a'): {safe_divide(10, 'a')}")

# 4. 内置作用域的访问和修改
def builtin_scope_access():
    """演示如何访问和修改内置作用域"""
    print("\n=== 内置作用域的访问和修改 ===")
    
    # 直接访问内置对象
    print("直接访问内置对象:")
    print(f"直接使用print: {print}")
    print(f"通过builtins访问: {builtins.print}")
    print(f"两者是同一个对象: {print is builtins.print}")
    
    # 查看内置对象的属性
    print("\n查看内置函数的属性:")
    print(f"print.__name__: {print.__name__}")
    print(f"print.__doc__[:50]: {print.__doc__[:50]}...")
    print(f"len.__module__: {len.__module__}")
    
    # 临时修改内置对象（不推荐）
    print("\n临时修改内置对象:")
    original_len = builtins.len
    
    def custom_len(obj):
        result = original_len(obj)
        print(f"计算长度: {obj} -> {result}")
        return result
    
    # 替换内置len函数
    builtins.len = custom_len
    
    # 测试修改后的len函数
    test_list = [1, 2, 3, 4]
    length = len(test_list)
    
    # 恢复原始len函数
    builtins.len = original_len
    print(f"恢复后的len([1,2,3,4]): {len([1,2,3,4])}")

# 5. 作用域查找顺序演示
def scope_lookup_demo():
    """演示LEGB作用域查找顺序"""
    print("\n=== LEGB作用域查找顺序 ===")
    
    # 创建一个与内置函数同名的变量
    def demonstrate_legb():
        # Local scope
        len = "局部变量len"
        
        def inner_function():
            # Enclosing scope
            print = "嵌套作用域print"
            
            def innermost_function():
                # 在这里查找变量的顺序是：L -> E -> G -> B
                # print(f"局部len: {len}")  # 找到外层的len（字符串）
                # print(f"嵌套print: {print}")  # 这会出错，因为print被重新定义了
                
                # 使用builtins明确访问内置函数
                import builtins
                print_func = builtins.print
                len_func = builtins.len
                
                print_func(f"外层len变量: {len}")  # 显示外层的len变量（字符串）
                print_func(f"内置len函数: {len_func}")
                print_func(f"使用内置len计算长度: {len_func([1,2,3,4,5])}")
            
            return innermost_function
        
        return inner_function
    
    # 执行演示
    demo_func = demonstrate_legb()()
    demo_func()
    
    # 全局作用域变量
    global_var = "全局变量"
    
    def access_global():
        # 访问全局变量和内置变量
        print(f"全局变量: {global_var}")
        print(f"内置函数abs: {abs(-5)}")
    
    access_global()

# 6. 内置作用域的实际应用
def builtin_scope_applications():
    """演示内置作用域的实际应用"""
    print("\n=== 内置作用域的实际应用 ===")
    
    # 1. 动态函数调用
    def dynamic_function_call(func_name, *args):
        """动态调用内置函数"""
        if hasattr(builtins, func_name):
            func = getattr(builtins, func_name)
            if callable(func):
                try:
                    return func(*args)
                except Exception as e:
                    return f"调用错误: {e}"
            else:
                return f"{func_name} 不是可调用对象"
        else:
            return f"内置作用域中没有 {func_name}"
    
    print("动态函数调用:")
    print(f"调用len: {dynamic_function_call('len', [1,2,3,4])}")
    print(f"调用max: {dynamic_function_call('max', [1,5,3,2])}")
    print(f"调用sum: {dynamic_function_call('sum', [1,2,3,4])}")
    print(f"调用不存在的函数: {dynamic_function_call('nonexistent', 1, 2)}")
    
    # 2. 安全的eval替代
    def safe_eval(expression, allowed_names=None):
        """安全的表达式求值"""
        if allowed_names is None:
            # 只允许使用安全的内置函数
            allowed_names = {
                'abs', 'max', 'min', 'sum', 'len', 'round',
                'int', 'float', 'str', 'bool', 'list', 'tuple', 'dict', 'set'
            }
        
        # 创建受限的命名空间
        safe_builtins = {}
        for name in allowed_names:
            if hasattr(builtins, name):
                safe_builtins[name] = getattr(builtins, name)
        
        try:
            return eval(expression, {"__builtins__": safe_builtins})
        except Exception as e:
            return f"求值错误: {e}"
    
    print("\n安全的表达式求值:")
    expressions = [
        "max([1, 5, 3, 2])",
        "sum(range(10))",
        "len('hello world')",
        "abs(-42)",
        "round(3.14159, 2)"
    ]
    
    for expr in expressions:
        result = safe_eval(expr)
        print(f"{expr} = {result}")
    
    # 3. 类型检查工具
    def analyze_object(obj):
        """分析对象的类型和属性"""
        info = {
            'value': obj,
            'type': type(obj).__name__,
            'is_callable': callable(obj),
            'is_iterable': hasattr(obj, '__iter__'),
            'has_len': hasattr(obj, '__len__'),
            'id': id(obj),
            'size_in_memory': None
        }
        
        # 尝试获取长度
        if info['has_len']:
            try:
                info['length'] = len(obj)
            except:
                info['length'] = 'N/A'
        
        # 尝试获取内存大小
        try:
            import sys
            info['size_in_memory'] = sys.getsizeof(obj)
        except:
            pass
        
        return info
    
    print("\n对象分析:")
    test_objects = [
        "hello",
        [1, 2, 3, 4],
        {'a': 1, 'b': 2},
        lambda x: x * 2,
        42,
        print
    ]
    
    for obj in test_objects:
        info = analyze_object(obj)
        print(f"对象: {info['value']}")
        print(f"  类型: {info['type']}")
        print(f"  可调用: {info['is_callable']}")
        print(f"  可迭代: {info['is_iterable']}")
        if 'length' in info:
            print(f"  长度: {info['length']}")
        if info['size_in_memory']:
            print(f"  内存大小: {info['size_in_memory']} 字节")
        print()

# 7. 内置作用域的扩展
def extend_builtin_scope():
    """演示如何扩展内置作用域"""
    print("\n=== 扩展内置作用域 ===")
    
    # 添加自定义函数到内置作用域
    def custom_print(*args, **kwargs):
        """增强的print函数"""
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        original_print = builtins.print
        original_print(f"[{timestamp}]", *args, **kwargs)
    
    def flatten(nested_list):
        """展平嵌套列表"""
        result = []
        for item in nested_list:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result
    
    # 临时添加到内置作用域
    original_print = builtins.print
    builtins.tprint = custom_print  # 时间戳print
    builtins.flatten = flatten      # 展平函数
    
    print("添加自定义函数到内置作用域:")
    
    # 测试新添加的函数
    tprint("这是带时间戳的输出")
    
    nested = [1, [2, 3], [4, [5, 6]], 7]
    flattened = flatten(nested)
    print(f"原始嵌套列表: {nested}")
    print(f"展平后的列表: {flattened}")
    
    # 清理：移除添加的函数
    del builtins.tprint
    del builtins.flatten
    
    print("已清理自定义函数")

# 8. 内置作用域的最佳实践
def builtin_scope_best_practices():
    """演示内置作用域的最佳实践"""
    print("\n=== 最佳实践 ===")
    
    # 1. 避免遮蔽内置名称
    print("1. 避免遮蔽内置名称")
    
    # 不好的做法
    def bad_practice():
        list = [1, 2, 3]  # 遮蔽了内置的list类型
        # 现在无法使用list()构造函数了
        return list
    
    # 好的做法
    def good_practice():
        data_list = [1, 2, 3]  # 使用描述性名称
        new_list = list(range(5))  # 仍然可以使用内置list
        return data_list, new_list
    
    result1 = bad_practice()
    result2 = good_practice()
    print(f"不好的做法结果: {result1}")
    print(f"好的做法结果: {result2}")
    
    # 2. 明确使用内置函数
    print("\n2. 明确使用内置函数")
    
    def process_data(data):
        # 明确使用内置函数，提高代码可读性
        length = builtins.len(data)
        maximum = builtins.max(data) if data else None
        minimum = builtins.min(data) if data else None
        total = builtins.sum(data) if all(isinstance(x, (int, float)) for x in data) else None
        
        return {
            'length': length,
            'max': maximum,
            'min': minimum,
            'sum': total
        }
    
    test_data = [1, 5, 3, 9, 2]
    analysis = process_data(test_data)
    print(f"数据分析结果: {analysis}")
    
    # 3. 检查内置对象的可用性
    print("\n3. 检查内置对象的可用性")
    
    def safe_builtin_usage(builtin_name, *args, **kwargs):
        """安全地使用内置函数"""
        if hasattr(builtins, builtin_name):
            func = getattr(builtins, builtin_name)
            if callable(func):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    return f"调用 {builtin_name} 时出错: {e}"
            else:
                return f"{builtin_name} 不是函数"
        else:
            return f"内置作用域中没有 {builtin_name}"
    
    # 测试安全使用
    test_cases = [
        ('len', [1, 2, 3]),
        ('max', [1, 5, 3]),
        ('nonexistent', [1, 2, 3]),
        ('__name__',),  # 这是一个属性，不是函数
    ]
    
    for case in test_cases:
        func_name = case[0]
        args = case[1:] if len(case) > 1 else ()
        result = safe_builtin_usage(func_name, *args)
        print(f"safe_builtin_usage('{func_name}', {args}): {result}")

# 主程序
if __name__ == "__main__":
    print("Python函数作用域学习 - 内置作用域")
    print("=" * 50)
    
    # 1. 探索内置作用域
    explore_builtin_scope()
    
    # 2. 内置函数演示
    builtin_functions_demo()
    
    # 3. 内置异常演示
    builtin_exceptions_demo()
    
    # 4. 内置作用域访问
    builtin_scope_access()
    
    # 5. 作用域查找演示
    scope_lookup_demo()
    
    # 6. 实际应用
    builtin_scope_applications()
    
    # 7. 扩展内置作用域
    extend_builtin_scope()
    
    # 8. 最佳实践
    builtin_scope_best_practices()
    
    print("\n=== 学习总结 ===")
    print("1. 内置作用域包含Python的内置函数、类型、异常和常量")
    print("2. 内置作用域是LEGB查找链的最后一环")
    print("3. 可以通过builtins模块访问内置对象")
    print("4. 避免遮蔽内置名称以防止意外错误")
    print("5. 内置作用域可以被修改，但通常不推荐")
    print("6. 了解内置作用域有助于编写更安全和高效的代码")
    print("7. 合理利用内置函数可以简化代码并提高性能")
    print("8. 在动态编程中，内置作用域提供了丰富的工具集")