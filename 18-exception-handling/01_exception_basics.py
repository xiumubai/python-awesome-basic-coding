#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
异常处理基础 - Exception Basics

本模块演示Python异常处理的基本概念：
1. 什么是异常
2. 常见的内置异常类型
3. 异常的层次结构
4. 基本的异常处理语法
5. 异常信息的获取和显示

作者: Python学习教程
日期: 2024
"""

import sys
import traceback


def demonstrate_common_exceptions():
    """
    演示常见的Python内置异常类型
    """
    print("=" * 50)
    print("常见异常类型演示")
    print("=" * 50)
    
    # 1. NameError - 使用未定义的变量
    print("\n1. NameError - 使用未定义的变量:")
    try:
        print(undefined_variable)  # 这会引发NameError
    except NameError as e:
        print(f"捕获到NameError: {e}")
        print(f"异常类型: {type(e).__name__}")
    
    # 2. TypeError - 类型错误
    print("\n2. TypeError - 类型错误:")
    try:
        result = "hello" + 5  # 字符串和数字不能直接相加
    except TypeError as e:
        print(f"捕获到TypeError: {e}")
        print(f"异常类型: {type(e).__name__}")
    
    # 3. ValueError - 值错误
    print("\n3. ValueError - 值错误:")
    try:
        number = int("hello")  # 无法将"hello"转换为整数
    except ValueError as e:
        print(f"捕获到ValueError: {e}")
        print(f"异常类型: {type(e).__name__}")
    
    # 4. IndexError - 索引错误
    print("\n4. IndexError - 索引错误:")
    try:
        my_list = [1, 2, 3]
        print(my_list[10])  # 索引超出范围
    except IndexError as e:
        print(f"捕获到IndexError: {e}")
        print(f"异常类型: {type(e).__name__}")
    
    # 5. KeyError - 键错误
    print("\n5. KeyError - 键错误:")
    try:
        my_dict = {"name": "Alice", "age": 25}
        print(my_dict["height"])  # 键不存在
    except KeyError as e:
        print(f"捕获到KeyError: {e}")
        print(f"异常类型: {type(e).__name__}")
    
    # 6. ZeroDivisionError - 除零错误
    print("\n6. ZeroDivisionError - 除零错误:")
    try:
        result = 10 / 0  # 除以零
    except ZeroDivisionError as e:
        print(f"捕获到ZeroDivisionError: {e}")
        print(f"异常类型: {type(e).__name__}")
    
    # 7. FileNotFoundError - 文件未找到错误
    print("\n7. FileNotFoundError - 文件未找到错误:")
    try:
        with open("nonexistent_file.txt", "r") as f:
            content = f.read()
    except FileNotFoundError as e:
        print(f"捕获到FileNotFoundError: {e}")
        print(f"异常类型: {type(e).__name__}")
    
    # 8. AttributeError - 属性错误
    print("\n8. AttributeError - 属性错误:")
    try:
        my_string = "hello"
        my_string.nonexistent_method()  # 字符串没有这个方法
    except AttributeError as e:
        print(f"捕获到AttributeError: {e}")
        print(f"异常类型: {type(e).__name__}")


def demonstrate_exception_hierarchy():
    """
    演示Python异常的层次结构
    """
    print("\n" + "=" * 50)
    print("Python异常层次结构")
    print("=" * 50)
    
    # 显示一些重要异常类的继承关系
    exceptions_to_check = [
        Exception,
        ArithmeticError,
        ZeroDivisionError,
        LookupError,
        IndexError,
        KeyError,
        ValueError,
        TypeError,
        NameError,
        AttributeError,
        FileNotFoundError,
        IOError,
        OSError
    ]
    
    print("\n异常类的继承关系:")
    for exc_class in exceptions_to_check:
        mro = exc_class.__mro__  # Method Resolution Order
        hierarchy = " -> ".join([cls.__name__ for cls in mro])
        print(f"{exc_class.__name__}: {hierarchy}")
    
    # 演示异常捕获的顺序重要性
    print("\n异常捕获顺序的重要性:")
    try:
        # 这会引发ZeroDivisionError
        result = 10 / 0
    except ArithmeticError as e:
        print(f"被ArithmeticError捕获: {e}")
        print(f"实际异常类型: {type(e).__name__}")
        print("注意: ZeroDivisionError是ArithmeticError的子类")


def demonstrate_basic_exception_handling():
    """
    演示基本的异常处理语法
    """
    print("\n" + "=" * 50)
    print("基本异常处理语法")
    print("=" * 50)
    
    # 1. 基本的try-except
    print("\n1. 基本的try-except:")
    try:
        number = int(input("请输入一个数字 (或直接按回车使用默认值): ") or "42")
        result = 100 / number
        print(f"100 / {number} = {result}")
    except ValueError:
        print("输入的不是有效数字!")
    except ZeroDivisionError:
        print("不能除以零!")
    
    # 2. 捕获异常对象
    print("\n2. 捕获异常对象获取详细信息:")
    try:
        my_list = [1, 2, 3]
        index = int(input("请输入列表索引 (或直接按回车使用默认值): ") or "10")
        print(f"列表元素: {my_list[index]}")
    except (ValueError, IndexError) as e:
        print(f"发生错误: {e}")
        print(f"错误类型: {type(e).__name__}")
        print(f"错误参数: {e.args}")
    
    # 3. 捕获所有异常
    print("\n3. 捕获所有异常 (不推荐在生产代码中使用):")
    try:
        # 模拟一个可能出错的操作
        operation = input("输入一个Python表达式 (或直接按回车): ") or "1/0"
        result = eval(operation)  # 注意: eval在实际项目中要谨慎使用
        print(f"结果: {result}")
    except Exception as e:
        print(f"捕获到异常: {e}")
        print(f"异常类型: {type(e).__name__}")


def demonstrate_exception_information():
    """
    演示如何获取和显示异常信息
    """
    print("\n" + "=" * 50)
    print("异常信息获取和显示")
    print("=" * 50)
    
    try:
        # 创建一个会引发异常的情况
        data = {"users": [{"name": "Alice", "age": 25}]}
        user_id = 5  # 不存在的用户ID
        user_name = data["users"][user_id]["name"]
    except Exception as e:
        print("\n异常信息详解:")
        print(f"1. 异常类型: {type(e).__name__}")
        print(f"2. 异常消息: {str(e)}")
        print(f"3. 异常参数: {e.args}")
        
        # 获取异常的详细信息
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(f"\n4. 系统异常信息:")
        print(f"   异常类型: {exc_type.__name__}")
        print(f"   异常值: {exc_value}")
        
        # 打印完整的traceback
        print("\n5. 完整的异常追踪:")
        traceback.print_exc()
        
        # 格式化traceback为字符串
        print("\n6. 格式化的异常追踪:")
        tb_str = traceback.format_exc()
        print(tb_str)


def safe_division(a, b):
    """
    安全除法函数 - 演示异常处理的实际应用
    
    Args:
        a: 被除数
        b: 除数
    
    Returns:
        除法结果或错误信息
    """
    try:
        # 尝试进行除法运算
        result = a / b
        return {"success": True, "result": result, "message": "计算成功"}
    except ZeroDivisionError:
        return {"success": False, "result": None, "message": "错误: 除数不能为零"}
    except TypeError as e:
        return {"success": False, "result": None, "message": f"错误: 参数类型不正确 - {e}"}
    except Exception as e:
        return {"success": False, "result": None, "message": f"未知错误: {e}"}


def demonstrate_practical_example():
    """
    演示异常处理的实际应用示例
    """
    print("\n" + "=" * 50)
    print("实际应用示例 - 安全除法函数")
    print("=" * 50)
    
    # 测试不同的输入情况
    test_cases = [
        (10, 2),      # 正常情况
        (10, 0),      # 除零错误
        ("10", 2),    # 类型错误
        (10, "abc"),  # 类型错误
        (10, None),   # 类型错误
    ]
    
    for i, (a, b) in enumerate(test_cases, 1):
        print(f"\n测试 {i}: safe_division({a}, {b})")
        result = safe_division(a, b)
        
        if result["success"]:
            print(f"✅ {result['message']}: {result['result']}")
        else:
            print(f"❌ {result['message']}")


def main():
    """
    主函数 - 运行所有演示
    """
    print("Python异常处理基础教程")
    print("=" * 60)
    
    try:
        # 运行各个演示函数
        demonstrate_common_exceptions()
        demonstrate_exception_hierarchy()
        demonstrate_basic_exception_handling()
        demonstrate_exception_information()
        demonstrate_practical_example()
        
        print("\n" + "=" * 60)
        print("🎉 异常处理基础教程完成!")
        print("\n📚 学习要点总结:")
        print("1. 异常是程序运行时发生的错误")
        print("2. Python有丰富的内置异常类型")
        print("3. 异常有层次结构，子类异常会被父类捕获")
        print("4. 使用try-except可以优雅地处理异常")
        print("5. 可以获取异常的详细信息用于调试")
        print("6. 异常处理让程序更加健壮和用户友好")
        
        print("\n➡️  下一步学习: 02_try_except.py - 深入学习try-except语法")
        
    except KeyboardInterrupt:
        print("\n\n程序被用户中断")
    except Exception as e:
        print(f"\n程序执行出错: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()