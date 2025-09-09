#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
try-except语法详解 - Try-Except Statement

本模块深入学习try-except语句的各种用法：
1. 基本的try-except语法
2. 捕获特定异常类型
3. 捕获多种异常类型
4. 异常对象的使用
5. 异常处理的执行流程
6. 嵌套异常处理
7. 实际应用场景

作者: Python学习教程
日期: 2024
"""

import json
import requests
import time
from typing import Dict, Any, Optional


def basic_try_except_syntax():
    """
    演示基本的try-except语法
    """
    print("=" * 50)
    print("基本try-except语法")
    print("=" * 50)
    
    # 1. 最简单的try-except
    print("\n1. 最简单的try-except:")
    try:
        result = 10 / 0  # 这会引发ZeroDivisionError
        print(f"结果: {result}")
    except:
        print("发生了异常!")
    
    print("程序继续执行...")
    
    # 2. 捕获特定异常类型
    print("\n2. 捕获特定异常类型:")
    try:
        number = int("abc")  # 这会引发ValueError
        print(f"数字: {number}")
    except ValueError:
        print("无法将字符串转换为数字!")
    
    # 3. 捕获异常对象
    print("\n3. 捕获异常对象:")
    try:
        my_list = [1, 2, 3]
        print(my_list[10])  # 这会引发IndexError
    except IndexError as e:
        print(f"索引错误: {e}")
        print(f"异常类型: {type(e).__name__}")


def multiple_exception_handling():
    """
    演示多种异常处理方式
    """
    print("\n" + "=" * 50)
    print("多种异常处理方式")
    print("=" * 50)
    
    # 1. 多个except子句
    print("\n1. 多个except子句:")
    user_input = input("请输入一个数字 (或直接按回车): ") or "abc"
    
    try:
        number = int(user_input)
        result = 100 / number
        print(f"100 / {number} = {result}")
    except ValueError:
        print("❌ 输入的不是有效数字!")
    except ZeroDivisionError:
        print("❌ 不能除以零!")
    except Exception as e:
        print(f"❌ 发生了未预期的错误: {e}")
    
    # 2. 一个except捕获多种异常
    print("\n2. 一个except捕获多种异常:")
    try:
        data = {"name": "Alice", "scores": [85, 92, 78]}
        key = input("请输入要查询的键 (name/scores/age，或直接按回车): ") or "age"
        index = int(input("如果查询scores，请输入索引 (或直接按回车): ") or "10")
        
        if key == "scores":
            print(f"分数: {data[key][index]}")
        else:
            print(f"值: {data[key]}")
    except (KeyError, IndexError, ValueError) as e:
        print(f"❌ 输入错误: {e}")
        print(f"错误类型: {type(e).__name__}")
    
    # 3. 异常处理的顺序很重要
    print("\n3. 异常处理顺序的重要性:")
    try:
        # 模拟一个可能引发不同异常的操作
        operation = input("输入操作类型 (divide_by_zero/type_error/value_error，或直接按回车): ") or "divide_by_zero"
        
        if operation == "divide_by_zero":
            result = 1 / 0
        elif operation == "type_error":
            result = "hello" + 5
        elif operation == "value_error":
            result = int("abc")
        else:
            result = "正常操作"
        
        print(f"结果: {result}")
    except ArithmeticError as e:  # 父类异常
        print(f"算术错误 (父类): {e}")
    except ZeroDivisionError as e:  # 子类异常 - 这个永远不会被执行!
        print(f"除零错误 (子类): {e}")
    except (TypeError, ValueError) as e:
        print(f"类型或值错误: {e}")
    except Exception as e:
        print(f"其他异常: {e}")


def exception_execution_flow():
    """
    演示异常处理的执行流程
    """
    print("\n" + "=" * 50)
    print("异常处理执行流程")
    print("=" * 50)
    
    def risky_operation(operation_type):
        """
        模拟可能出错的操作
        """
        print(f"  → 开始执行操作: {operation_type}")
        
        if operation_type == "success":
            print("  → 操作成功完成")
            return "成功结果"
        elif operation_type == "value_error":
            print("  → 即将引发ValueError")
            raise ValueError("这是一个值错误")
        elif operation_type == "type_error":
            print("  → 即将引发TypeError")
            raise TypeError("这是一个类型错误")
        else:
            print("  → 即将引发未知异常")
            raise RuntimeError("未知的运行时错误")
    
    # 测试不同的执行流程
    test_cases = ["success", "value_error", "type_error", "unknown_error"]
    
    for i, case in enumerate(test_cases, 1):
        print(f"\n--- 测试 {i}: {case} ---")
        
        try:
            print("1. 进入try块")
            result = risky_operation(case)
            print(f"2. try块执行成功，结果: {result}")
            print("3. 准备退出try块")
        except ValueError as e:
            print(f"4a. 捕获到ValueError: {e}")
            print("5a. ValueError处理完成")
        except TypeError as e:
            print(f"4b. 捕获到TypeError: {e}")
            print("5b. TypeError处理完成")
        except Exception as e:
            print(f"4c. 捕获到其他异常: {e}")
            print(f"5c. 异常类型: {type(e).__name__}")
        
        print("6. 异常处理结束，继续执行后续代码")


def nested_exception_handling():
    """
    演示嵌套异常处理
    """
    print("\n" + "=" * 50)
    print("嵌套异常处理")
    print("=" * 50)
    
    def outer_function():
        """
        外层函数
        """
        print("  → 外层函数开始")
        
        try:
            print("  → 外层try块")
            inner_function()
            print("  → 外层try块完成")
        except ValueError as e:
            print(f"  → 外层捕获ValueError: {e}")
            return "外层处理了ValueError"
        except Exception as e:
            print(f"  → 外层捕获其他异常: {e}")
            return "外层处理了其他异常"
        
        return "外层正常完成"
    
    def inner_function():
        """
        内层函数
        """
        print("    → 内层函数开始")
        
        try:
            print("    → 内层try块")
            # 模拟不同的异常情况
            choice = input("选择异常类型 (1:ValueError, 2:TypeError, 3:正常，或直接按回车): ") or "1"
            
            if choice == "1":
                raise ValueError("内层ValueError")
            elif choice == "2":
                raise TypeError("内层TypeError")
            else:
                print("    → 内层正常执行")
                return "内层成功"
        except TypeError as e:
            print(f"    → 内层捕获TypeError: {e}")
            return "内层处理了TypeError"
        # 注意: ValueError没有在内层处理，会向上传播
        
        print("    → 内层函数结束")
    
    # 测试嵌套异常处理
    print("\n测试嵌套异常处理:")
    result = outer_function()
    print(f"最终结果: {result}")


def practical_file_processing():
    """
    实际应用: 文件处理中的异常处理
    """
    print("\n" + "=" * 50)
    print("实际应用: 文件处理")
    print("=" * 50)
    
    def safe_read_json_file(filename: str) -> Optional[Dict[str, Any]]:
        """
        安全地读取JSON文件
        
        Args:
            filename: 文件名
        
        Returns:
            解析后的JSON数据或None
        """
        try:
            print(f"  → 尝试打开文件: {filename}")
            with open(filename, 'r', encoding='utf-8') as file:
                print("  → 文件打开成功，开始读取")
                content = file.read()
                print(f"  → 读取到 {len(content)} 个字符")
                
                print("  → 开始解析JSON")
                data = json.loads(content)
                print("  → JSON解析成功")
                return data
                
        except FileNotFoundError:
            print(f"  ❌ 文件不存在: {filename}")
            return None
        except PermissionError:
            print(f"  ❌ 没有权限读取文件: {filename}")
            return None
        except json.JSONDecodeError as e:
            print(f"  ❌ JSON格式错误: {e}")
            print(f"     错误位置: 行 {e.lineno}, 列 {e.colno}")
            return None
        except UnicodeDecodeError as e:
            print(f"  ❌ 文件编码错误: {e}")
            return None
        except Exception as e:
            print(f"  ❌ 未知错误: {e}")
            return None
    
    # 创建测试文件
    test_files = {
        "valid.json": '{"name": "Alice", "age": 25, "city": "Beijing"}',
        "invalid.json": '{"name": "Bob", "age": 30,}',  # 无效JSON
        "empty.json": ""
    }
    
    print("\n创建测试文件...")
    for filename, content in test_files.items():
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ 创建文件: {filename}")
        except Exception as e:
            print(f"  ❌ 创建文件失败 {filename}: {e}")
    
    # 测试文件读取
    test_filenames = ["valid.json", "invalid.json", "empty.json", "nonexistent.json"]
    
    print("\n测试文件读取:")
    for filename in test_filenames:
        print(f"\n--- 测试文件: {filename} ---")
        result = safe_read_json_file(filename)
        
        if result is not None:
            print(f"  ✅ 成功读取: {result}")
        else:
            print("  ❌ 读取失败")
    
    # 清理测试文件
    print("\n清理测试文件...")
    import os
    for filename in test_files.keys():
        try:
            os.remove(filename)
            print(f"  ✅ 删除文件: {filename}")
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"  ❌ 删除文件失败 {filename}: {e}")


def practical_network_request():
    """
    实际应用: 网络请求中的异常处理
    """
    print("\n" + "=" * 50)
    print("实际应用: 网络请求")
    print("=" * 50)
    
    def safe_http_request(url: str, timeout: int = 5) -> Optional[Dict[str, Any]]:
        """
        安全地发送HTTP请求
        
        Args:
            url: 请求URL
            timeout: 超时时间
        
        Returns:
            响应数据或None
        """
        try:
            print(f"  → 发送请求到: {url}")
            print(f"  → 超时设置: {timeout}秒")
            
            # 注意: 这里使用了requests库，在实际环境中需要安装
            # 为了演示，我们模拟网络请求
            time.sleep(0.1)  # 模拟网络延迟
            
            # 模拟不同的响应情况
            if "httpbin.org" in url:
                # 模拟成功响应
                return {
                    "status_code": 200,
                    "data": {"message": "请求成功", "url": url}
                }
            elif "timeout" in url:
                # 模拟超时
                time.sleep(timeout + 1)
                return None
            elif "404" in url:
                # 模拟404错误
                raise requests.exceptions.HTTPError("404 Not Found")
            else:
                # 模拟连接错误
                raise requests.exceptions.ConnectionError("连接失败")
                
        except requests.exceptions.Timeout:
            print(f"  ❌ 请求超时: {url}")
            return None
        except requests.exceptions.ConnectionError as e:
            print(f"  ❌ 连接错误: {e}")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"  ❌ HTTP错误: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"  ❌ 请求异常: {e}")
            return None
        except Exception as e:
            print(f"  ❌ 未知错误: {e}")
            return None
    
    # 由于requests可能未安装，我们创建一个模拟的requests模块
    class MockRequests:
        class exceptions:
            class RequestException(Exception): pass
            class Timeout(RequestException): pass
            class ConnectionError(RequestException): pass
            class HTTPError(RequestException): pass
    
    # 使用模拟的requests
    global requests
    requests = MockRequests()
    
    # 测试不同的URL
    test_urls = [
        "https://httpbin.org/get",
        "https://example.com/timeout",
        "https://example.com/404",
        "https://invalid-domain-12345.com"
    ]
    
    print("\n测试网络请求:")
    for url in test_urls:
        print(f"\n--- 测试URL: {url} ---")
        result = safe_http_request(url)
        
        if result:
            print(f"  ✅ 请求成功: {result}")
        else:
            print("  ❌ 请求失败")


def exception_handling_best_practices():
    """
    异常处理最佳实践
    """
    print("\n" + "=" * 50)
    print("异常处理最佳实践")
    print("=" * 50)
    
    print("\n✅ 好的做法:")
    
    # 1. 捕获具体的异常类型
    print("\n1. 捕获具体的异常类型:")
    try:
        value = int("abc")
    except ValueError as e:  # 具体的异常类型
        print(f"  ✅ 捕获具体异常: {e}")
    
    # 2. 提供有意义的错误信息
    print("\n2. 提供有意义的错误信息:")
    def divide_numbers(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            raise ValueError(f"无法计算 {a} / {b}: 除数不能为零")
        except TypeError:
            raise TypeError(f"无法计算 {a} / {b}: 参数必须是数字")
    
    try:
        result = divide_numbers(10, 0)
    except ValueError as e:
        print(f"  ✅ 有意义的错误信息: {e}")
    
    # 3. 记录异常信息
    print("\n3. 记录异常信息:")
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    try:
        risky_operation = 1 / 0
    except Exception as e:
        logger.error(f"操作失败: {e}", exc_info=True)
        print("  ✅ 异常已记录到日志")
    
    print("\n❌ 不好的做法:")
    
    # 1. 捕获所有异常但不处理
    print("\n1. 捕获所有异常但不处理 (反例):")
    try:
        problematic_operation = 1 / 0
    except:
        pass  # 这是不好的做法!
    print("  ❌ 异常被忽略，可能隐藏重要问题")
    
    # 2. 异常信息不明确
    print("\n2. 异常信息不明确 (反例):")
    try:
        unclear_operation = int("abc")
    except Exception:
        print("  ❌ 出错了")  # 信息不明确


def main():
    """
    主函数 - 运行所有演示
    """
    print("try-except语法详解教程")
    print("=" * 60)
    
    try:
        # 运行各个演示函数
        basic_try_except_syntax()
        multiple_exception_handling()
        exception_execution_flow()
        nested_exception_handling()
        practical_file_processing()
        practical_network_request()
        exception_handling_best_practices()
        
        print("\n" + "=" * 60)
        print("🎉 try-except语法教程完成!")
        print("\n📚 学习要点总结:")
        print("1. try-except是Python异常处理的核心语法")
        print("2. 可以捕获特定类型的异常或多种异常")
        print("3. 异常处理有明确的执行流程")
        print("4. 支持嵌套异常处理")
        print("5. 在文件处理和网络请求中广泛应用")
        print("6. 遵循最佳实践让代码更健壮")
        
        print("\n➡️  下一步学习: 03_multiple_except.py - 学习多重异常处理")
        
    except KeyboardInterrupt:
        print("\n\n程序被用户中断")
    except Exception as e:
        print(f"\n程序执行出错: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()