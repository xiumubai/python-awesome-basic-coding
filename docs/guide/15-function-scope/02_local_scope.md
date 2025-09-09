# 局部作用域

局部作用域是Python中最基本的作用域类型，理解局部作用域是掌握Python作用域机制的基础。

## 什么是局部作用域

局部作用域（Local Scope）是指在函数内部创建的作用域。在函数内部定义的变量只在该函数内部可见，这些变量被称为局部变量。

## 局部作用域的特点

1. **封闭性**：局部变量只在定义它们的函数内部可见
2. **临时性**：局部变量在函数调用结束后被销毁
3. **独立性**：每次函数调用都会创建新的局部作用域
4. **参数包含**：函数参数也是局部变量的一部分

## 代码示例

### 基本局部变量示例

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
局部作用域演示

本文件演示Python中局部作用域的概念和使用方法。
局部作用域是函数内部的作用域，局部变量只在函数内部可见。
"""

def demonstrate_local_scope():
    """
    演示局部作用域的基本概念
    """
    print("=== 局部作用域基本概念 ===")
    
    # 在函数内部定义的变量是局部变量
    local_var = "我是局部变量"
    number = 42
    
    print(f"函数内部访问局部变量: {local_var}")
    print(f"函数内部访问数字变量: {number}")
    
    # 局部变量只在函数内部可见
    print("局部变量只在当前函数内部可见")

def test_local_variable_isolation():
    """
    演示局部变量的隔离性
    """
    print("\n=== 局部变量隔离性 ===")
    
    # 不同函数中的同名局部变量是独立的
    message = "函数A中的消息"
    print(f"函数A中的message: {message}")
    
    def inner_function():
        # 这是另一个局部变量，与外层函数的message无关
        message = "内部函数中的消息"
        print(f"内部函数中的message: {message}")
    
    inner_function()
    print(f"函数A中的message仍然是: {message}")

def demonstrate_parameter_scope(param1, param2="默认值"):
    """
    演示函数参数也是局部变量
    
    Args:
        param1: 位置参数
        param2: 带默认值的参数
    """
    print("\n=== 函数参数作为局部变量 ===")
    
    print(f"参数param1的值: {param1}")
    print(f"参数param2的值: {param2}")
    
    # 可以修改参数的值（它们是局部变量）
    param1 = "修改后的param1"
    param2 = "修改后的param2"
    
    print(f"修改后param1的值: {param1}")
    print(f"修改后param2的值: {param2}")
    
    # 在函数内部定义更多局部变量
    local_calculation = len(param1) + len(param2)
    print(f"局部计算结果: {local_calculation}")

def demonstrate_variable_lifetime():
    """
    演示局部变量的生命周期
    """
    print("\n=== 局部变量生命周期 ===")
    
    def create_and_destroy():
        # 这些变量在函数调用时创建
        temp_var = "临时变量"
        counter = 0
        
        for i in range(3):
            counter += 1
            print(f"循环 {i+1}: counter = {counter}, temp_var = {temp_var}")
        
        print("函数即将结束，局部变量即将被销毁")
        return counter  # 返回值会被复制出去
    
    # 调用函数
    result = create_and_destroy()
    print(f"函数返回值: {result}")
    
    # 再次调用，会创建新的局部变量
    print("\n再次调用函数:")
    result2 = create_and_destroy()
    print(f"第二次调用返回值: {result2}")

def demonstrate_nested_local_scope():
    """
    演示嵌套函数中的局部作用域
    """
    print("\n=== 嵌套函数中的局部作用域 ===")
    
    outer_var = "外层函数的局部变量"
    
    def inner_function():
        inner_var = "内层函数的局部变量"
        print(f"内层函数可以访问: {inner_var}")
        print(f"内层函数也可以访问外层的: {outer_var}")
    
    print(f"外层函数的变量: {outer_var}")
    inner_function()
    
    # 外层函数无法访问内层函数的局部变量
    # print(inner_var)  # 这会引发NameError

def demonstrate_local_vs_global():
    """
    演示局部变量与全局变量的区别
    """
    print("\n=== 局部变量与全局变量 ===")
    
    # 这是一个局部变量，与全局的global_var无关
    global_var = "这实际上是局部变量"
    
    print(f"函数内部的'global_var': {global_var}")
    print("注意：这个变量虽然名字叫global_var，但它是局部变量")
    
    # 创建其他局部变量
    local_only = "只存在于此函数中"
    print(f"纯局部变量: {local_only}")

def practical_example():
    """
    实际应用示例：计算器函数
    """
    print("\n=== 实际应用示例：简单计算器 ===")
    
    def calculator(operation, a, b):
        """
        简单计算器函数，演示局部作用域的实际应用
        
        Args:
            operation: 操作类型 (+, -, *, /)
            a: 第一个数字
            b: 第二个数字
        
        Returns:
            计算结果
        """
        # 所有这些变量都是局部变量
        result = 0
        error_message = None
        
        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            if b != 0:
                result = a / b
            else:
                error_message = "除数不能为零"
        else:
            error_message = f"不支持的操作: {operation}"
        
        # 局部变量用于构建返回信息
        if error_message:
            return f"错误: {error_message}"
        else:
            return f"{a} {operation} {b} = {result}"
    
    # 测试计算器
    test_cases = [
        ("+", 10, 5),
        ("-", 10, 3),
        ("*", 4, 7),
        ("/", 15, 3),
        ("/", 10, 0),  # 错误情况
        ("%", 10, 3),  # 不支持的操作
    ]
    
    for op, x, y in test_cases:
        result = calculator(op, x, y)
        print(f"计算结果: {result}")

def common_mistakes():
    """
    演示局部作用域的常见错误
    """
    print("\n=== 局部作用域常见错误 ===")
    
    def mistake_example():
        # 错误1：试图在定义前使用局部变量
        try:
            print(f"尝试使用未定义的变量: {undefined_var}")
        except NameError as e:
            print(f"NameError: {e}")
        
        # 正确做法：先定义再使用
        undefined_var = "现在已定义"
        print(f"正确使用: {undefined_var}")
    
    def scope_confusion():
        # 错误2：混淆局部变量和全局变量
        x = 10  # 这是局部变量
        print(f"函数内的x: {x}")
        
        def inner():
            x = 20  # 这也是局部变量（在inner函数中）
            print(f"内层函数的x: {x}")
        
        inner()
        print(f"外层函数的x仍然是: {x}")
    
    mistake_example()
    print()
    scope_confusion()

def best_practices():
    """
    局部作用域的最佳实践
    """
    print("\n=== 局部作用域最佳实践 ===")
    
    def well_structured_function(data_list):
        """
        良好结构的函数示例
        
        Args:
            data_list: 输入数据列表
        
        Returns:
            处理结果字典
        """
        # 1. 使用有意义的变量名
        processed_items = []
        error_count = 0
        success_count = 0
        
        # 2. 将复杂逻辑分解为局部变量
        for item in data_list:
            try:
                # 3. 使用局部变量存储中间结果
                processed_item = item.strip().upper() if isinstance(item, str) else str(item)
                processed_items.append(processed_item)
                success_count += 1
            except Exception as e:
                error_count += 1
                print(f"处理项目 {item} 时出错: {e}")
        
        # 4. 使用局部变量构建返回值
        result = {
            'processed_items': processed_items,
            'success_count': success_count,
            'error_count': error_count,
            'total_count': len(data_list)
        }
        
        return result
    
    # 测试最佳实践
    test_data = ["  hello  ", "WORLD", 123, "  python  ", None]
    result = well_structured_function(test_data)
    
    print("处理结果:")
    for key, value in result.items():
        print(f"  {key}: {value}")

# 全局变量（用于对比）
global_var = "我是全局变量"

def main():
    """
    主函数：演示所有局部作用域概念
    """
    print("Python 局部作用域详解")
    print("=" * 50)
    
    # 演示各种局部作用域概念
    demonstrate_local_scope()
    test_local_variable_isolation()
    demonstrate_parameter_scope("传入的参数")
    demonstrate_variable_lifetime()
    demonstrate_nested_local_scope()
    demonstrate_local_vs_global()
    practical_example()
    common_mistakes()
    best_practices()
    
    print("\n=== 总结 ===")
    print("1. 局部变量只在定义它们的函数内部可见")
    print("2. 函数参数也是局部变量")
    print("3. 局部变量在函数调用结束后被销毁")
    print("4. 每次函数调用都会创建新的局部作用域")
    print("5. 使用有意义的变量名和良好的代码结构")

if __name__ == "__main__":
    main()
```

## 学习要点

### 核心概念
1. **局部变量定义**：在函数内部定义的变量
2. **作用域边界**：函数的花括号定义了局部作用域的边界
3. **变量生命周期**：从定义到函数结束
4. **参数特性**：函数参数也是局部变量

### 重要特性
1. **封闭性**：局部变量不会影响函数外部
2. **独立性**：每次函数调用创建独立的作用域
3. **临时性**：函数结束后变量被销毁
4. **优先性**：局部变量优先于全局变量

### 实际应用
1. **数据处理**：使用局部变量存储中间结果
2. **错误处理**：局部变量控制错误状态
3. **算法实现**：局部变量维护算法状态
4. **代码组织**：通过局部作用域实现代码封装

## 运行示例

在15-function-scope目录下运行：

```bash
python3 01_local_scope.py
```

## 注意事项

1. **变量命名**：使用有意义的局部变量名
2. **作用域混淆**：不要混淆局部变量和全局变量
3. **生命周期**：理解局部变量的生命周期
4. **嵌套函数**：注意嵌套函数中的作用域层次

## 下一步学习

掌握局部作用域后，建议继续学习：
- [全局作用域](03_global_scope.md)
- [global关键字](04_global_keyword.md)
- [作用域解析规则](08_scope_resolution.md)