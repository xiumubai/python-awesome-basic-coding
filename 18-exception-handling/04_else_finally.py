#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
else和finally子句的使用

本文件详细演示try-except语句中else和finally子句的使用方法，
包括它们的执行时机、使用场景和最佳实践。

学习目标：
1. 理解else子句的执行条件和使用场景
2. 掌握finally子句的执行时机和重要性
3. 学会合理组合使用try-except-else-finally
4. 了解资源管理和清理的最佳实践
"""

import os
import time
import json
import tempfile
from typing import Optional, Dict, Any, List
from contextlib import contextmanager


def print_section(title: str) -> None:
    """打印章节标题"""
    print("\n" + "=" * 60)
    print(f"{title}")
    print("=" * 60)


def demonstrate_else_clause():
    """演示else子句的使用"""
    print_section("1. else子句的使用")
    
    print("else子句的特点：")
    print("- 只有在try块中没有异常发生时才会执行")
    print("- 如果try块中发生异常，else块不会执行")
    print("- else块中的代码可以访问try块中定义的变量")
    
    def divide_numbers(a: float, b: float) -> Optional[float]:
        """除法运算示例，演示else子句"""
        print(f"\n尝试计算 {a} ÷ {b}")
        
        try:
            result = a / b
            print(f"计算成功，结果在try块中计算完成")
        except ZeroDivisionError as e:
            print(f"除零错误: {e}")
            return None
        except TypeError as e:
            print(f"类型错误: {e}")
            return None
        else:
            # 只有在没有异常时才执行
            print(f"else块执行：没有发生异常")
            print(f"在else块中进行后续处理")
            # 可以在这里进行一些只有成功时才需要的操作
            formatted_result = round(result, 2)
            print(f"格式化结果: {formatted_result}")
            return formatted_result
        finally:
            print(f"finally块：无论是否有异常都会执行")
    
    # 测试不同情况
    test_cases = [
        (10, 2),      # 正常情况
        (10, 0),      # 除零错误
        ("10", 2),    # 类型错误
        (15, 3),      # 正常情况
    ]
    
    print("\n测试else子句：")
    for a, b in test_cases:
        result = divide_numbers(a, b)
        print(f"最终返回值: {result}")
        print("-" * 40)


def demonstrate_finally_clause():
    """演示finally子句的使用"""
    print_section("2. finally子句的使用")
    
    print("finally子句的特点：")
    print("- 无论是否发生异常都会执行")
    print("- 即使在try或except块中有return语句，finally也会执行")
    print("- 常用于资源清理和释放")
    print("- 如果finally中有return，会覆盖其他return值")
    
    def file_operation_example(filename: str, content: str) -> Dict[str, Any]:
        """文件操作示例，演示finally子句"""
        print(f"\n尝试写入文件: {filename}")
        file_handle = None
        start_time = time.time()
        
        try:
            print("try块：打开文件")
            file_handle = open(filename, 'w', encoding='utf-8')
            
            print("try块：写入内容")
            file_handle.write(content)
            
            print("try块：模拟可能的异常")
            if len(content) > 100:
                raise ValueError("内容过长")
            
            print("try块：操作成功完成")
            return {'status': 'success', 'message': '文件写入成功'}
            
        except FileNotFoundError as e:
            print(f"except块：文件未找到错误: {e}")
            return {'status': 'error', 'message': '文件路径不存在'}
            
        except PermissionError as e:
            print(f"except块：权限错误: {e}")
            return {'status': 'error', 'message': '没有写入权限'}
            
        except ValueError as e:
            print(f"except块：值错误: {e}")
            return {'status': 'error', 'message': str(e)}
            
        except Exception as e:
            print(f"except块：未知错误: {e}")
            return {'status': 'error', 'message': '未知错误'}
            
        else:
            print("else块：没有异常发生，进行额外处理")
            file_size = os.path.getsize(filename)
            print(f"else块：文件大小: {file_size} 字节")
            
        finally:
            print("finally块：开始清理资源")
            
            # 关闭文件句柄
            if file_handle and not file_handle.closed:
                print("finally块：关闭文件句柄")
                file_handle.close()
            else:
                print("finally块：文件句柄已关闭或未打开")
            
            # 记录执行时间
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"finally块：操作耗时 {execution_time:.4f} 秒")
            
            print("finally块：清理完成")
    
    # 测试不同情况
    test_cases = [
        ("test_normal.txt", "这是正常的内容"),
        ("test_long.txt", "这是一个很长的内容" * 20),  # 会触发ValueError
        ("/invalid/path/test.txt", "无效路径测试"),  # 会触发FileNotFoundError
    ]
    
    print("\n测试finally子句：")
    for filename, content in test_cases:
        result = file_operation_example(filename, content)
        print(f"操作结果: {result}")
        
        # 清理测试文件
        try:
            if os.path.exists(filename):
                os.remove(filename)
                print(f"清理测试文件: {filename}")
        except:
            pass
        
        print("-" * 50)


def demonstrate_return_in_finally():
    """演示finally中return语句的影响"""
    print_section("3. finally中return语句的影响")
    
    print("注意：finally中的return会覆盖try/except中的return值")
    
    def function_with_finally_return(value: int) -> str:
        """演示finally中return的影响"""
        print(f"\n处理值: {value}")
        
        try:
            if value < 0:
                raise ValueError("值不能为负数")
            print("try块：准备返回success")
            return "success"
            
        except ValueError as e:
            print(f"except块：捕获异常 {e}")
            print("except块：准备返回error")
            return "error"
            
        finally:
            print("finally块：执行清理操作")
            # 注意：这个return会覆盖try/except中的return
            if value == 999:
                print("finally块：返回特殊值")
                return "finally_override"
            print("finally块：不返回值")
    
    def function_without_finally_return(value: int) -> str:
        """对比：finally中不返回值"""
        print(f"\n处理值: {value}")
        
        try:
            if value < 0:
                raise ValueError("值不能为负数")
            print("try块：准备返回success")
            return "success"
            
        except ValueError as e:
            print(f"except块：捕获异常 {e}")
            print("except块：准备返回error")
            return "error"
            
        finally:
            print("finally块：执行清理操作，不返回值")
    
    print("\n测试finally中有return的情况：")
    test_values = [10, -5, 999]
    for value in test_values:
        result = function_with_finally_return(value)
        print(f"最终结果: {result}")
        print("-" * 30)
    
    print("\n测试finally中没有return的情况：")
    for value in test_values:
        result = function_without_finally_return(value)
        print(f"最终结果: {result}")
        print("-" * 30)


def demonstrate_nested_try_finally():
    """演示嵌套的try-finally结构"""
    print_section("4. 嵌套的try-finally结构")
    
    def complex_operation(data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """复杂操作，演示嵌套的异常处理"""
        print("开始复杂操作")
        temp_files = []
        processed_count = 0
        
        try:
            print("外层try：开始处理数据")
            
            for i, item in enumerate(data):
                temp_filename = f"temp_data_{i}.json"
                temp_files.append(temp_filename)
                
                try:
                    print(f"内层try：处理项目 {i}")
                    
                    # 验证数据
                    if not isinstance(item, dict):
                        raise TypeError(f"项目 {i} 不是字典类型")
                    
                    if 'id' not in item:
                        raise KeyError(f"项目 {i} 缺少id字段")
                    
                    # 写入临时文件
                    with open(temp_filename, 'w', encoding='utf-8') as f:
                        json.dump(item, f, ensure_ascii=False, indent=2)
                    
                    print(f"内层try：项目 {i} 处理成功")
                    processed_count += 1
                    
                except (TypeError, KeyError, ValueError) as e:
                    print(f"内层except：处理项目 {i} 时出错: {e}")
                    # 继续处理下一个项目
                    continue
                    
                except Exception as e:
                    print(f"内层except：项目 {i} 发生未知错误: {e}")
                    # 严重错误，停止处理
                    raise
                    
                finally:
                    print(f"内层finally：完成项目 {i} 的处理")
            
            print(f"外层try：所有项目处理完成，成功处理 {processed_count} 个")
            
            if processed_count == 0:
                raise RuntimeError("没有成功处理任何项目")
            
            return {
                'status': 'success',
                'processed_count': processed_count,
                'total_count': len(data)
            }
            
        except RuntimeError as e:
            print(f"外层except：运行时错误: {e}")
            return {
                'status': 'error',
                'error': str(e),
                'processed_count': processed_count
            }
            
        except Exception as e:
            print(f"外层except：未知错误: {e}")
            return {
                'status': 'system_error',
                'error': str(e),
                'processed_count': processed_count
            }
            
        finally:
            print("外层finally：开始清理临时文件")
            
            # 清理所有临时文件
            cleaned_count = 0
            for temp_file in temp_files:
                try:
                    if os.path.exists(temp_file):
                        os.remove(temp_file)
                        cleaned_count += 1
                        print(f"外层finally：删除临时文件 {temp_file}")
                except Exception as e:
                    print(f"外层finally：删除文件 {temp_file} 失败: {e}")
            
            print(f"外层finally：清理完成，删除了 {cleaned_count} 个临时文件")
    
    # 测试数据
    test_data = [
        {'id': 1, 'name': '项目1', 'value': 100},
        {'id': 2, 'name': '项目2', 'value': 200},
        {'name': '项目3', 'value': 300},  # 缺少id
        "无效数据",  # 不是字典
        {'id': 4, 'name': '项目4', 'value': 400},
    ]
    
    print("\n测试嵌套try-finally：")
    result = complex_operation(test_data)
    print(f"\n最终结果: {result}")


def demonstrate_resource_management():
    """演示资源管理的最佳实践"""
    print_section("5. 资源管理最佳实践")
    
    print("资源管理的几种方式：")
    print("1. 使用try-finally手动管理")
    print("2. 使用with语句（推荐）")
    print("3. 使用自定义上下文管理器")
    
    # 方式1：使用try-finally手动管理
    def manual_resource_management(filename: str) -> Dict[str, Any]:
        """手动资源管理示例"""
        print(f"\n方式1：手动管理资源 - {filename}")
        file_handle = None
        
        try:
            print("打开文件")
            file_handle = open(filename, 'w', encoding='utf-8')
            
            print("写入数据")
            file_handle.write("测试数据\n")
            file_handle.write("更多数据\n")
            
            # 模拟可能的异常
            if "error" in filename:
                raise ValueError("模拟错误")
            
            return {'status': 'success', 'method': 'manual'}
            
        except Exception as e:
            print(f"发生错误: {e}")
            return {'status': 'error', 'error': str(e), 'method': 'manual'}
            
        finally:
            print("finally：清理资源")
            if file_handle and not file_handle.closed:
                file_handle.close()
                print("文件已关闭")
    
    # 方式2：使用with语句（推荐）
    def context_manager_approach(filename: str) -> Dict[str, Any]:
        """使用with语句管理资源"""
        print(f"\n方式2：使用with语句 - {filename}")
        
        try:
            with open(filename, 'w', encoding='utf-8') as file_handle:
                print("文件已打开（自动管理）")
                
                file_handle.write("测试数据\n")
                file_handle.write("更多数据\n")
                
                # 模拟可能的异常
                if "error" in filename:
                    raise ValueError("模拟错误")
                
                print("数据写入完成")
            # 文件会自动关闭
            print("文件已自动关闭")
            
            return {'status': 'success', 'method': 'context_manager'}
            
        except Exception as e:
            print(f"发生错误: {e}")
            return {'status': 'error', 'error': str(e), 'method': 'context_manager'}
    
    # 方式3：自定义上下文管理器
    class DatabaseConnection:
        """模拟数据库连接的上下文管理器"""
        
        def __init__(self, db_name: str):
            self.db_name = db_name
            self.connected = False
        
        def __enter__(self):
            print(f"连接到数据库: {self.db_name}")
            self.connected = True
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            print(f"断开数据库连接: {self.db_name}")
            self.connected = False
            
            if exc_type:
                print(f"处理异常: {exc_type.__name__}: {exc_val}")
                # 返回False表示不抑制异常
                return False
        
        def execute_query(self, query: str) -> str:
            if not self.connected:
                raise RuntimeError("数据库未连接")
            
            print(f"执行查询: {query}")
            
            if "error" in query.lower():
                raise ValueError("查询语法错误")
            
            return f"查询结果: {query}"
    
    def custom_context_manager_example(db_name: str, query: str) -> Dict[str, Any]:
        """使用自定义上下文管理器"""
        print(f"\n方式3：自定义上下文管理器 - {db_name}")
        
        try:
            with DatabaseConnection(db_name) as db:
                result = db.execute_query(query)
                print(f"查询成功: {result}")
                return {'status': 'success', 'result': result, 'method': 'custom_context'}
                
        except Exception as e:
            print(f"操作失败: {e}")
            return {'status': 'error', 'error': str(e), 'method': 'custom_context'}
    
    # 测试不同的资源管理方式
    test_cases = [
        ("test_success.txt", "SELECT * FROM users"),
        ("test_error.txt", "SELECT error FROM table"),
    ]
    
    print("\n测试不同的资源管理方式：")
    for filename, query in test_cases:
        print("\n" + "=" * 50)
        
        # 测试手动管理
        result1 = manual_resource_management(filename)
        print(f"手动管理结果: {result1}")
        
        # 测试with语句
        result2 = context_manager_approach(filename)
        print(f"with语句结果: {result2}")
        
        # 测试自定义上下文管理器
        result3 = custom_context_manager_example("test_db", query)
        print(f"自定义上下文结果: {result3}")
        
        # 清理测试文件
        for test_file in [filename]:
            try:
                if os.path.exists(test_file):
                    os.remove(test_file)
            except:
                pass


def demonstrate_best_practices():
    """演示else和finally的最佳实践"""
    print_section("6. else和finally的最佳实践")
    
    print("最佳实践总结：")
    print("""
    1. else子句的使用：
       - 用于只有在没有异常时才需要执行的代码
       - 避免在try块中放入不必要的代码
       - 提高代码的可读性和逻辑清晰度
    
    2. finally子句的使用：
       - 用于资源清理和释放
       - 确保重要的清理代码总是被执行
       - 避免在finally中使用return语句
    
    3. 资源管理：
       - 优先使用with语句进行资源管理
       - 对于复杂资源，考虑实现自定义上下文管理器
       - 在finally中进行必要的清理工作
    
    4. 代码组织：
       - 保持try块尽可能小
       - 将成功后的处理逻辑放在else块中
       - 在finally块中进行清理工作
    """)
    
    # 最佳实践示例
    def best_practice_example(data: Dict[str, Any]) -> Dict[str, Any]:
        """最佳实践示例"""
        print(f"\n处理数据: {data}")
        
        # 初始化资源
        temp_file = None
        start_time = time.time()
        
        try:
            # try块：只包含可能抛出异常的核心操作
            print("验证数据格式")
            if not isinstance(data, dict):
                raise TypeError("数据必须是字典类型")
            
            if 'id' not in data:
                raise KeyError("缺少必需的id字段")
            
            # 创建临时文件
            temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
            json.dump(data, temp_file, ensure_ascii=False, indent=2)
            temp_file.close()
            
            print(f"数据已写入临时文件: {temp_file.name}")
            
        except (TypeError, KeyError, ValueError) as e:
            print(f"数据验证错误: {e}")
            return {
                'status': 'validation_error',
                'error': str(e),
                'processing_time': time.time() - start_time
            }
            
        except Exception as e:
            print(f"处理过程中发生错误: {e}")
            return {
                'status': 'processing_error',
                'error': str(e),
                'processing_time': time.time() - start_time
            }
            
        else:
            # else块：只有在没有异常时才执行的后续处理
            print("数据处理成功，进行后续操作")
            
            # 读取文件大小
            file_size = os.path.getsize(temp_file.name)
            print(f"临时文件大小: {file_size} 字节")
            
            # 生成处理报告
            report = {
                'status': 'success',
                'data_id': data['id'],
                'temp_file': temp_file.name,
                'file_size': file_size,
                'processing_time': time.time() - start_time
            }
            
            print("生成处理报告完成")
            return report
            
        finally:
            # finally块：无论是否有异常都要执行的清理工作
            print("开始清理资源")
            
            # 清理临时文件
            if temp_file and os.path.exists(temp_file.name):
                try:
                    os.unlink(temp_file.name)
                    print(f"已删除临时文件: {temp_file.name}")
                except Exception as e:
                    print(f"删除临时文件失败: {e}")
            
            # 记录总执行时间
            total_time = time.time() - start_time
            print(f"总执行时间: {total_time:.4f} 秒")
            print("资源清理完成")
    
    # 测试最佳实践
    test_cases = [
        {'id': 1, 'name': '测试数据1', 'value': 100},
        {'name': '缺少ID的数据', 'value': 200},
        "无效的数据类型",
        {'id': 2, 'name': '测试数据2', 'value': 300},
    ]
    
    print("\n测试最佳实践示例：")
    for i, test_data in enumerate(test_cases, 1):
        print(f"\n{'='*20} 测试 {i} {'='*20}")
        result = best_practice_example(test_data)
        print(f"最终结果: {result}")


def main():
    """主函数"""
    print("Python异常处理 - else和finally子句的使用")
    print("=" * 60)
    
    try:
        # 演示各种else和finally的用法
        demonstrate_else_clause()
        demonstrate_finally_clause()
        demonstrate_return_in_finally()
        demonstrate_nested_try_finally()
        demonstrate_resource_management()
        demonstrate_best_practices()
        
        print_section("学习总结")
        print("""
        else和finally子句要点：
        
        1. else子句：
           - 只有在try块没有异常时才执行
           - 用于成功后的后续处理
           - 提高代码逻辑的清晰度
        
        2. finally子句：
           - 无论是否有异常都会执行
           - 主要用于资源清理和释放
           - 避免在finally中使用return
        
        3. 资源管理：
           - 优先使用with语句
           - 实现自定义上下文管理器
           - 在finally中进行必要清理
        
        4. 代码组织：
           - try块保持简洁
           - else块处理成功情况
           - finally块进行清理工作
        
        下一步学习：
        - 05_raise_exception.py: 抛出异常
        - 06_custom_exceptions.py: 自定义异常类
        - 07_exception_chaining.py: 异常链和上下文
        """)
        
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"程序执行过程中发生错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()