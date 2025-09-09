# 内置作用域（Built-in Scope）

内置作用域是Python作用域系统中的最外层，包含了Python解释器预定义的所有内置函数、常量和异常。理解内置作用域对于掌握Python的变量查找机制和避免命名冲突至关重要。

## 什么是内置作用域

内置作用域（Built-in Scope）是Python中最外层的作用域，包含了Python解释器启动时自动加载的所有内置对象。这些对象在任何地方都可以直接使用，无需导入。

## 内置作用域的特点

1. **全局可访问**：在任何地方都可以访问
2. **最低优先级**：在LEGB查找顺序中优先级最低
3. **预定义内容**：包含Python的核心功能
4. **可以被遮蔽**：可以被其他作用域的同名变量遮蔽

## 代码示例

### 内置作用域基础

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
内置作用域演示

本文件演示Python中内置作用域的概念、内容和使用方法。
内置作用域包含了Python解释器预定义的所有内置函数、常量和异常。
"""

import builtins
import sys

def demonstrate_builtin_scope_basics():
    """
    演示内置作用域的基本概念
    """
    print("=== 内置作用域基础 ===")
    
    # 直接使用内置函数，无需导入
    print("常用内置函数演示:")
    
    # 类型转换函数
    print(f"int('123'): {int('123')}")
    print(f"float('3.14'): {float('3.14')}")
    print(f"str(42): {str(42)}")
    print(f"bool(1): {bool(1)}")
    
    # 容器函数
    print(f"list((1, 2, 3)): {list((1, 2, 3))}")
    print(f"tuple([1, 2, 3]): {tuple([1, 2, 3])}")
    print(f"set([1, 2, 2, 3]): {set([1, 2, 2, 3])}")
    print(f"dict([('a', 1), ('b', 2)]): {dict([('a', 1), ('b', 2)])}")
    
    # 数学函数
    print(f"abs(-5): {abs(-5)}")
    print(f"max(1, 5, 3): {max(1, 5, 3)}")
    print(f"min(1, 5, 3): {min(1, 5, 3)}")
    print(f"sum([1, 2, 3, 4]): {sum([1, 2, 3, 4])}")
    
    # 序列函数
    print(f"len('hello'): {len('hello')}")
    print(f"sorted([3, 1, 4, 1, 5]): {sorted([3, 1, 4, 1, 5])}")
    print(f"reversed([1, 2, 3]): {list(reversed([1, 2, 3]))}")
    
    # 输入输出
    print("print函数正在被使用")
    # input函数在脚本中不演示，避免阻塞

def demonstrate_builtin_constants():
    """
    演示内置常量
    """
    print("\n=== 内置常量 ===")
    
    # 布尔常量
    print(f"True: {True} (类型: {type(True)})")
    print(f"False: {False} (类型: {type(False)})")
    
    # 空值常量
    print(f"None: {None} (类型: {type(None)})")
    
    # 省略号常量
    print(f"Ellipsis (...): {Ellipsis} (类型: {type(Ellipsis)})")
    
    # 未实现常量
    print(f"NotImplemented: {NotImplemented} (类型: {type(NotImplemented)})")
    
    # 演示省略号的使用
    def incomplete_function():
        """一个未完成的函数"""
        ...  # 等价于 pass，但更明确表示"待实现"
    
    print("省略号可以用作占位符")
    incomplete_function()

def demonstrate_builtin_exceptions():
    """
    演示内置异常
    """
    print("\n=== 内置异常 ===")
    
    # 常见异常演示
    exceptions_demo = [
        ("ValueError", lambda: int("not_a_number")),
        ("TypeError", lambda: "string" + 123),
        ("IndexError", lambda: [1, 2, 3][10]),
        ("KeyError", lambda: {"a": 1}["b"]),
        ("AttributeError", lambda: "string".nonexistent_method()),
        ("ZeroDivisionError", lambda: 1 / 0),
        ("FileNotFoundError", lambda: open("nonexistent_file.txt")),
    ]
    
    for exception_name, func in exceptions_demo:
        try:
            func()
        except Exception as e:
            print(f"{exception_name}: {e}")
    
    # 异常层次结构演示
    print("\n异常层次结构示例:")
    try:
        raise ValueError("这是一个值错误")
    except Exception as e:
        print(f"捕获到异常: {type(e).__name__}: {e}")
        print(f"异常的基类: {type(e).__bases__}")

def demonstrate_builtin_functions_categories():
    """
    演示内置函数的分类
    """
    print("\n=== 内置函数分类 ===")
    
    # 1. 类型检查和转换
    print("1. 类型检查和转换:")
    value = 42
    print(f"  type({value}): {type(value)}")
    print(f"  isinstance({value}, int): {isinstance(value, int)}")
    print(f"  issubclass(bool, int): {issubclass(bool, int)}")
    
    # 2. 数学运算
    print("\n2. 数学运算:")
    numbers = [1, -2, 3, -4, 5]
    print(f"  abs(-42): {abs(-42)}")
    print(f"  divmod(17, 5): {divmod(17, 5)}")
    print(f"  pow(2, 3): {pow(2, 3)}")
    print(f"  round(3.14159, 2): {round(3.14159, 2)}")
    
    # 3. 序列操作
    print("\n3. 序列操作:")
    data = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"  len(data): {len(data)}")
    print(f"  max(data): {max(data)}")
    print(f"  min(data): {min(data)}")
    print(f"  sum(data): {sum(data)}")
    print(f"  sorted(data): {sorted(data)}")
    
    # 4. 迭代器和生成器
    print("\n4. 迭代器和生成器:")
    print(f"  range(5): {list(range(5))}")
    print(f"  enumerate(['a', 'b', 'c']): {list(enumerate(['a', 'b', 'c']))}")
    print(f"  zip([1, 2, 3], ['a', 'b', 'c']): {list(zip([1, 2, 3], ['a', 'b', 'c']))}")
    
    # 5. 函数式编程
    print("\n5. 函数式编程:")
    numbers = [1, 2, 3, 4, 5]
    print(f"  map(lambda x: x**2, numbers): {list(map(lambda x: x**2, numbers))}")
    print(f"  filter(lambda x: x % 2 == 0, numbers): {list(filter(lambda x: x % 2 == 0, numbers))}")
    
    # 6. 对象操作
    print("\n6. 对象操作:")
    obj = {"name": "Alice", "age": 30}
    print(f"  hasattr(obj, '__len__'): {hasattr(obj, '__len__')}")
    print(f"  getattr(obj, 'name', 'Unknown'): {getattr(obj, 'name', 'Unknown')}")
    print(f"  id(obj): {id(obj)}")
    
    # 7. 编译和执行
    print("\n7. 编译和执行:")
    code = "result = 2 + 3"
    compiled_code = compile(code, "<string>", "exec")
    local_vars = {}
    exec(compiled_code, {}, local_vars)
    print(f"  exec('{code}'): result = {local_vars['result']}")
    
    expression = "2 * 3 + 1"
    result = eval(expression)
    print(f"  eval('{expression}'): {result}")

def demonstrate_builtin_scope_access():
    """
    演示如何访问内置作用域
    """
    print("\n=== 访问内置作用域 ===")
    
    # 使用builtins模块访问内置作用域
    print("通过builtins模块访问:")
    print(f"  builtins.len: {builtins.len}")
    print(f"  builtins.print: {builtins.print}")
    print(f"  builtins.int: {builtins.int}")
    
    # 列出所有内置名称
    builtin_names = [name for name in dir(builtins) if not name.startswith('_')]
    print(f"\n内置名称总数: {len(builtin_names)}")
    print(f"前10个内置名称: {builtin_names[:10]}")
    
    # 按类型分类内置对象
    builtin_types = {}
    for name in builtin_names:
        obj = getattr(builtins, name)
        obj_type = type(obj).__name__
        if obj_type not in builtin_types:
            builtin_types[obj_type] = []
        builtin_types[obj_type].append(name)
    
    print("\n内置对象按类型分类:")
    for obj_type, names in sorted(builtin_types.items()):
        print(f"  {obj_type}: {len(names)}个 - {names[:5]}{'...' if len(names) > 5 else ''}")

def demonstrate_scope_shadowing():
    """
    演示内置作用域的遮蔽现象
    """
    print("\n=== 内置作用域遮蔽 ===")
    
    # 演示遮蔽内置函数
    print("遮蔽内置函数演示:")
    
    # 保存原始的内置函数
    original_len = len
    original_max = max
    
    print(f"原始len函数: {original_len}")
    print(f"使用原始len: len('hello') = {original_len('hello')}")
    
    # 在全局作用域中遮蔽len
    def shadow_builtin_globally():
        global len  # 声明要修改全局的len
        len = lambda x: f"被遮蔽的len函数，参数是: {x}"
        print(f"\n遮蔽后的len: {len}")
        print(f"使用遮蔽的len: len('hello') = {len('hello')}")
    
    # 在局部作用域中遮蔽
    def shadow_builtin_locally():
        print("\n在局部作用域中遮蔽:")
        
        # 局部遮蔽max函数
        max = "这不是max函数，而是一个字符串"
        print(f"局部作用域中的max: {max}")
        
        # 尝试使用被遮蔽的max
        try:
            result = max([1, 2, 3])  # 这会出错
        except TypeError as e:
            print(f"错误: {e}")
        
        # 通过builtins访问原始max
        result = builtins.max([1, 2, 3])
        print(f"通过builtins.max访问: {result}")
    
    # 演示遮蔽的危险性
    def demonstrate_shadowing_dangers():
        print("\n遮蔽的危险性演示:")
        
        # 意外遮蔽内置函数
        def process_data():
            # 意外地创建了一个名为list的变量
            list = [1, 2, 3, 4, 5]  # 这遮蔽了内置的list函数
            print(f"数据: {list}")
            
            # 后面想使用list函数时会出错
            try:
                new_list = list((6, 7, 8))  # 这会出错
            except TypeError as e:
                print(f"错误: {e}")
                print("原因: list变量遮蔽了内置的list函数")
            
            # 正确的做法：使用不同的变量名
            data_list = [1, 2, 3, 4, 5]
            new_list = list((6, 7, 8))  # 这样就正常了
            print(f"正确做法 - 数据: {data_list}")
            print(f"正确做法 - 新列表: {new_list}")
        
        process_data()
    
    # 执行演示
    shadow_builtin_globally()
    
    # 恢复原始函数
    len = original_len
    print(f"\n恢复后的len: len('world') = {len('world')}")
    
    shadow_builtin_locally()
    demonstrate_shadowing_dangers()

def demonstrate_builtin_scope_extension():
    """
    演示如何扩展内置作用域
    """
    print("\n=== 扩展内置作用域 ===")
    
    # 添加自定义函数到内置作用域
    def add_to_builtins():
        print("添加自定义函数到内置作用域:")
        
        # 定义一些有用的函数
        def is_even(n):
            """检查数字是否为偶数"""
            return n % 2 == 0
        
        def is_odd(n):
            """检查数字是否为奇数"""
            return n % 2 == 1
        
        def clamp(value, min_val, max_val):
            """将值限制在指定范围内"""
            return max(min_val, min(value, max_val))
        
        # 添加到内置作用域
        builtins.is_even = is_even
        builtins.is_odd = is_odd
        builtins.clamp = clamp
        
        print("已添加函数: is_even, is_odd, clamp")
        
        # 测试新添加的函数
        print(f"is_even(4): {is_even(4)}")
        print(f"is_odd(4): {is_odd(4)}")
        print(f"clamp(15, 0, 10): {clamp(15, 0, 10)}")
    
    def demonstrate_custom_builtins():
        print("\n在其他函数中使用自定义内置函数:")
        
        def test_function():
            # 这些函数现在可以像内置函数一样使用
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            even_numbers = [n for n in numbers if is_even(n)]
            odd_numbers = [n for n in numbers if is_odd(n)]
            
            print(f"偶数: {even_numbers}")
            print(f"奇数: {odd_numbers}")
            
            # 使用clamp函数
            values = [-5, 0, 5, 10, 15, 20]
            clamped = [clamp(v, 0, 10) for v in values]
            print(f"原始值: {values}")
            print(f"限制在[0,10]: {clamped}")
        
        test_function()
    
    def cleanup_builtins():
        print("\n清理自定义内置函数:")
        
        # 删除添加的函数
        if hasattr(builtins, 'is_even'):
            delattr(builtins, 'is_even')
        if hasattr(builtins, 'is_odd'):
            delattr(builtins, 'is_odd')
        if hasattr(builtins, 'clamp'):
            delattr(builtins, 'clamp')
        
        print("已清理自定义内置函数")
        
        # 验证清理结果
        try:
            is_even(4)
        except NameError:
            print("确认: is_even函数已被移除")
    
    # 执行演示
    add_to_builtins()
    demonstrate_custom_builtins()
    cleanup_builtins()

def demonstrate_practical_applications():
    """
    演示内置作用域的实际应用
    """
    print("\n=== 实际应用示例 ===")
    
    # 1. 创建安全的eval环境
    def safe_eval_demo():
        print("1. 安全的eval环境:")
        
        # 创建受限的内置环境
        safe_builtins = {
            'abs': abs,
            'max': max,
            'min': min,
            'sum': sum,
            'len': len,
            'int': int,
            'float': float,
            'str': str,
            'bool': bool,
        }
        
        # 安全的表达式
        safe_expressions = [
            "abs(-5)",
            "max(1, 2, 3)",
            "sum([1, 2, 3, 4])",
            "int('42') + float('3.14')",
        ]
        
        for expr in safe_expressions:
            try:
                result = eval(expr, {"__builtins__": safe_builtins}, {})
                print(f"  {expr} = {result}")
            except Exception as e:
                print(f"  {expr} -> 错误: {e}")
        
        # 危险的表达式（会被阻止）
        dangerous_expressions = [
            "__import__('os').system('ls')",  # 尝试导入模块
            "open('/etc/passwd')",  # 尝试打开文件
            "exec('print(\"危险代码\")')",  # 尝试执行代码
        ]
        
        print("\n  测试危险表达式（应该被阻止）:")
        for expr in dangerous_expressions:
            try:
                result = eval(expr, {"__builtins__": safe_builtins}, {})
                print(f"  {expr} = {result} (警告: 应该被阻止!)")
            except Exception as e:
                print(f"  {expr} -> 已阻止: {type(e).__name__}")
    
    # 2. 动态函数创建
    def dynamic_function_demo():
        print("\n2. 动态函数创建:")
        
        def create_math_function(operation):
            """根据操作名创建数学函数"""
            
            # 获取对应的内置函数
            builtin_func = getattr(builtins, operation, None)
            
            if builtin_func and callable(builtin_func):
                def wrapper(*args):
                    try:
                        return builtin_func(*args)
                    except Exception as e:
                        return f"错误: {e}"
                
                wrapper.__name__ = f"safe_{operation}"
                wrapper.__doc__ = f"安全的{operation}函数"
                return wrapper
            else:
                return lambda *args: f"不支持的操作: {operation}"
        
        # 创建动态函数
        operations = ['abs', 'max', 'min', 'sum', 'len', 'nonexistent']
        
        for op in operations:
            func = create_math_function(op)
            print(f"  {func.__name__}: {func.__doc__}")
            
            # 测试函数
            if op == 'abs':
                print(f"    测试: {func(-42)}")
            elif op == 'max':
                print(f"    测试: {func([1, 5, 3])}")
            elif op == 'len':
                print(f"    测试: {func('hello')}")
            elif op == 'nonexistent':
                print(f"    测试: {func(1, 2, 3)}")
    
    # 3. 内置函数的性能比较
    def performance_comparison():
        print("\n3. 内置函数性能比较:")
        
        import time
        
        # 比较不同求和方法的性能
        data = list(range(100000))
        
        # 方法1: 使用内置sum函数
        start_time = time.time()
        result1 = sum(data)
        time1 = time.time() - start_time
        
        # 方法2: 使用循环
        start_time = time.time()
        result2 = 0
        for x in data:
            result2 += x
        time2 = time.time() - start_time
        
        # 方法3: 使用reduce
        from functools import reduce
        import operator
        start_time = time.time()
        result3 = reduce(operator.add, data, 0)
        time3 = time.time() - start_time
        
        print(f"  数据大小: {len(data)}")
        print(f"  内置sum: {time1:.6f}秒, 结果: {result1}")
        print(f"  for循环: {time2:.6f}秒, 结果: {result2}")
        print(f"  reduce: {time3:.6f}秒, 结果: {result3}")
        print(f"  内置sum比for循环快: {time2/time1:.2f}倍")
    
    # 执行所有演示
    safe_eval_demo()
    dynamic_function_demo()
    performance_comparison()

def demonstrate_best_practices():
    """
    演示内置作用域的最佳实践
    """
    print("\n=== 最佳实践 ===")
    
    print("1. 避免遮蔽内置名称:")
    
    # 不好的做法
    def bad_practice():
        print("  不好的做法:")
        # 这些变量名会遮蔽内置函数
        list = [1, 2, 3]  # 遮蔽了list()
        dict = {'a': 1}   # 遮蔽了dict()
        str = "hello"     # 遮蔽了str()
        print(f"    定义了变量: list={list}, dict={dict}, str={str}")
        print("    但是现在无法使用内置的list(), dict(), str()函数了")
    
    # 好的做法
    def good_practice():
        print("  好的做法:")
        # 使用描述性的变量名
        data_list = [1, 2, 3]
        config_dict = {'a': 1}
        message_str = "hello"
        print(f"    使用描述性名称: data_list={data_list}")
        print(f"    config_dict={config_dict}, message_str={message_str}")
        print("    内置函数仍然可用")
        
        # 演示内置函数仍然可用
        new_list = list((4, 5, 6))
        new_dict = dict([('b', 2), ('c', 3)])
        new_str = str(123)
        print(f"    内置函数: list((4,5,6))={new_list}")
        print(f"    dict([('b',2),('c',3)])={new_dict}")
        print(f"    str(123)={new_str}")
    
    bad_practice()
    good_practice()
    
    print("\n2. 检查名称冲突:")
    
    def check_name_conflicts():
        """检查变量名是否与内置名称冲突"""
        
        def is_builtin_name(name):
            return hasattr(builtins, name)
        
        # 测试一些变量名
        test_names = ['data', 'list', 'dict', 'str', 'len', 'max', 'sum', 'count']
        
        for name in test_names:
            if is_builtin_name(name):
                print(f"  警告: '{name}' 是内置名称，建议使用其他名称")
            else:
                print(f"  安全: '{name}' 不是内置名称")
    
    check_name_conflicts()
    
    print("\n3. 安全地扩展内置作用域:")
    
    def safe_builtin_extension():
        """安全地扩展内置作用域"""
        
        # 检查是否已存在
        def add_safe_builtin(name, func):
            if hasattr(builtins, name):
                print(f"  警告: '{name}' 已存在于内置作用域中")
                return False
            else:
                setattr(builtins, name, func)
                print(f"  成功添加 '{name}' 到内置作用域")
                return True
        
        # 安全地添加函数
        def my_custom_function(x):
            return x * 2
        
        success = add_safe_builtin('my_custom_function', my_custom_function)
        
        if success:
            # 测试新函数
            result = my_custom_function(21)
            print(f"  测试新函数: my_custom_function(21) = {result}")
            
            # 清理
            delattr(builtins, 'my_custom_function')
            print(f"  已清理 'my_custom_function'")
    
    safe_builtin_extension()

def main():
    """
    主函数：演示所有内置作用域概念
    """
    print("Python 内置作用域详解")
    print("=" * 50)
    
    # 演示各种内置作用域概念
    demonstrate_builtin_scope_basics()
    demonstrate_builtin_constants()
    demonstrate_builtin_exceptions()
    demonstrate_builtin_functions_categories()
    demonstrate_builtin_scope_access()
    demonstrate_scope_shadowing()
    demonstrate_builtin_scope_extension()
    demonstrate_practical_applications()
    demonstrate_best_practices()
    
    print("\n=== 总结 ===")
    print("1. 内置作用域包含Python的核心功能")
    print("2. 内置对象在任何地方都可以直接使用")
    print("3. 内置名称可以被遮蔽，但应该避免")
    print("4. 可以通过builtins模块访问和扩展内置作用域")
    print("5. 内置函数通常比自定义实现更高效")
    print("6. 遵循最佳实践可以避免常见问题")

if __name__ == "__main__":
    main()
```

## 学习要点

### 核心概念
1. **最外层作用域**：LEGB规则中的B（Built-in）
2. **预定义内容**：Python解释器自动加载的对象
3. **全局可访问**：无需导入即可使用
4. **最低优先级**：在变量查找中优先级最低

### 主要内容
1. **内置函数**：len()、max()、min()、sum()等
2. **内置常量**：True、False、None、Ellipsis等
3. **内置异常**：ValueError、TypeError、IndexError等
4. **内置类型**：int、str、list、dict等

### 重要特性
1. **可遮蔽性**：可以被其他作用域的同名变量遮蔽
2. **可扩展性**：可以通过builtins模块添加新的内置对象
3. **高性能**：内置函数通常经过优化，性能较好
4. **稳定性**：内置对象在Python版本间保持稳定

### 实际应用
1. **日常编程**：使用内置函数提高开发效率
2. **安全编程**：创建受限的执行环境
3. **性能优化**：优先使用内置函数
4. **工具开发**：扩展内置作用域添加常用工具

## 运行示例

在15-function-scope目录下运行：

```bash
python3 06_built_in_scope.py
```

## 注意事项

1. **避免遮蔽**：不要使用内置名称作为变量名
2. **性能考虑**：内置函数通常比自定义实现更快
3. **版本兼容**：某些内置对象可能在不同Python版本中有差异
4. **安全风险**：修改内置作用域可能影响整个程序

## 常见错误

1. **名称遮蔽**：意外使用内置名称作为变量名
2. **类型错误**：将内置函数当作变量使用
3. **导入混淆**：不清楚哪些是内置的，哪些需要导入
4. **版本差异**：在不同Python版本间移植代码时的兼容性问题

## 最佳实践

1. **避免遮蔽**：使用描述性的变量名，避免与内置名称冲突
2. **优先使用内置**：优先使用内置函数而不是自定义实现
3. **检查冲突**：在定义变量前检查是否与内置名称冲突
4. **谨慎扩展**：谨慎地扩展内置作用域，并及时清理

## 调试技巧

1. **使用dir(builtins)**：查看所有内置名称
2. **使用hasattr(builtins, name)**：检查名称是否为内置
3. **使用type()和isinstance()**：检查对象类型
4. **使用help()**：查看内置对象的帮助信息

## 性能提示

1. **内置函数优先**：内置函数通常比等价的Python代码更快
2. **避免重复查找**：将频繁使用的内置函数赋值给局部变量
3. **合理使用**：了解内置函数的时间复杂度
4. **基准测试**：对性能敏感的代码进行基准测试

## 下一步学习

掌握内置作用域后，建议继续学习：
- [作用域解析规则](08_scope_resolution.md)
- [综合练习](09_exercises.md)
- 函数式编程相关内容