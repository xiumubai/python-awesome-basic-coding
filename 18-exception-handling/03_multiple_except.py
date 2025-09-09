#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
多个except子句的处理

本文件演示如何使用多个except子句来处理不同类型的异常，
包括异常的优先级、组合处理和最佳实践。

学习目标：
1. 理解多个except子句的执行顺序
2. 掌握异常类型的层次结构
3. 学会合理组织异常处理逻辑
4. 了解异常处理的最佳实践
"""

import sys
import json
from typing import List, Dict, Any


def print_section(title: str) -> None:
    """打印章节标题"""
    print("\n" + "=" * 60)
    print(f"{title}")
    print("=" * 60)


def demonstrate_multiple_except_basic():
    """演示多个except子句的基本用法"""
    print_section("1. 多个except子句的基本用法")
    
    def process_data(data: str) -> float:
        """处理数据的函数，可能抛出多种异常"""
        try:
            # 尝试将字符串转换为浮点数
            number = float(data)
            # 尝试除法运算
            result = 100 / number
            return result
        except ValueError as e:
            print(f"数值转换错误: {e}")
            print(f"输入的数据 '{data}' 不能转换为数字")
            return 0.0
        except ZeroDivisionError as e:
            print(f"除零错误: {e}")
            print("不能除以零")
            return float('inf')
        except Exception as e:
            print(f"其他未预期的错误: {e}")
            return -1.0
    
    # 测试不同的输入
    test_cases = ["50", "0", "abc", "25.5", ""]
    
    print("测试多个except子句：")
    for case in test_cases:
        print(f"\n输入: '{case}'")
        result = process_data(case)
        print(f"结果: {result}")


def demonstrate_exception_hierarchy():
    """演示异常层次结构的重要性"""
    print_section("2. 异常层次结构和处理顺序")
    
    print("Python异常层次结构（部分）：")
    print("""
    BaseException
     +-- SystemExit
     +-- KeyboardInterrupt
     +-- GeneratorExit
     +-- Exception
          +-- StopIteration
          +-- ArithmeticError
          |    +-- FloatingPointError
          |    +-- OverflowError
          |    +-- ZeroDivisionError
          +-- AttributeError
          +-- EOFError
          +-- ImportError
          +-- LookupError
          |    +-- IndexError
          |    +-- KeyError
          +-- NameError
          +-- OSError
          +-- RuntimeError
          +-- TypeError
          +-- ValueError
    """)
    
    def demonstrate_order_matters():
        """演示异常处理顺序的重要性"""
        print("\n2.1 正确的异常处理顺序（从具体到一般）：")
        
        def correct_order_example(data: List[str], index: int) -> str:
            try:
                return data[index].upper()
            except IndexError as e:
                print(f"索引错误: {e}")
                return "INDEX_ERROR"
            except AttributeError as e:
                print(f"属性错误: {e}")
                return "ATTRIBUTE_ERROR"
            except LookupError as e:  # IndexError的父类
                print(f"查找错误: {e}")
                return "LOOKUP_ERROR"
            except Exception as e:
                print(f"其他错误: {e}")
                return "OTHER_ERROR"
        
        # 测试用例
        test_data = ["hello", "world", None]
        test_cases = [
            (test_data, 0),   # 正常情况
            (test_data, 5),   # IndexError
            (test_data, 2),   # AttributeError (None没有upper方法)
        ]
        
        for data, idx in test_cases:
            print(f"\n测试: data[{idx}]")
            result = correct_order_example(data, idx)
            print(f"返回值: {result}")
    
    def demonstrate_wrong_order():
        """演示错误的异常处理顺序"""
        print("\n2.2 错误的异常处理顺序示例：")
        print("如果将Exception放在前面，具体的异常永远不会被捕获")
        
        # 这是一个错误的示例，仅用于演示
        def wrong_order_example(numbers: List[int], index: int) -> float:
            try:
                return 100 / numbers[index]
            except Exception as e:  # 太宽泛，会捕获所有异常
                print(f"捕获到异常: {type(e).__name__}: {e}")
                return -1.0
            except ZeroDivisionError as e:  # 永远不会执行到这里
                print(f"除零错误: {e}")
                return 0.0
            except IndexError as e:  # 永远不会执行到这里
                print(f"索引错误: {e}")
                return -2.0
        
        print("注意：下面的代码中，具体的异常处理器永远不会被执行")
        test_cases = [[1, 2, 0], [1, 2, 3]]
        indices = [2, 5]  # 第一个会导致ZeroDivisionError，第二个会导致IndexError
        
        for data, idx in zip(test_cases, indices):
            print(f"\n测试: 100 / {data}[{idx}]")
            result = wrong_order_example(data, idx)
            print(f"结果: {result}")
    
    demonstrate_order_matters()
    demonstrate_wrong_order()


def demonstrate_multiple_exception_types():
    """演示在一个except子句中处理多种异常类型"""
    print_section("3. 在一个except子句中处理多种异常")
    
    def process_user_input(user_input: str) -> Dict[str, Any]:
        """处理用户输入，可能遇到多种异常"""
        try:
            # 尝试解析JSON
            data = json.loads(user_input)
            
            # 尝试访问特定字段
            name = data['name']
            age = int(data['age'])
            
            # 进行一些计算
            years_to_retirement = 65 - age
            
            return {
                'name': name,
                'age': age,
                'years_to_retirement': years_to_retirement,
                'status': 'success'
            }
            
        except (json.JSONDecodeError, KeyError) as e:
            # 处理JSON解析错误和键错误
            print(f"数据格式错误: {type(e).__name__}: {e}")
            return {'status': 'format_error', 'message': '数据格式不正确'}
            
        except (ValueError, TypeError) as e:
            # 处理值错误和类型错误
            print(f"数据类型错误: {type(e).__name__}: {e}")
            return {'status': 'type_error', 'message': '数据类型不正确'}
            
        except Exception as e:
            # 处理其他未预期的异常
            print(f"未知错误: {type(e).__name__}: {e}")
            return {'status': 'unknown_error', 'message': '处理过程中发生未知错误'}
    
    # 测试用例
    test_inputs = [
        '{"name": "张三", "age": "30"}',  # 正常情况
        '{"name": "李四"}',  # 缺少age字段
        '{"name": "王五", "age": "abc"}',  # age不是数字
        'invalid json',  # 无效的JSON
        '{"name": "赵六", "age": 25}',  # 正常情况
    ]
    
    print("测试多种异常类型的处理：")
    for i, input_data in enumerate(test_inputs, 1):
        print(f"\n测试 {i}: {input_data}")
        result = process_user_input(input_data)
        print(f"结果: {result}")


def demonstrate_nested_exception_handling():
    """演示嵌套的异常处理"""
    print_section("4. 嵌套异常处理")
    
    def read_and_process_file(filename: str) -> Dict[str, Any]:
        """读取并处理文件，使用嵌套异常处理"""
        result = {'filename': filename, 'status': 'unknown'}
        
        try:
            # 外层try：处理文件操作异常
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                result['file_size'] = len(content)
                
                try:
                    # 内层try：处理数据处理异常
                    data = json.loads(content)
                    
                    # 进一步处理数据
                    processed_data = []
                    for item in data:
                        try:
                            # 最内层try：处理单个项目的异常
                            processed_item = {
                                'id': int(item['id']),
                                'value': float(item['value']),
                                'name': str(item['name']).upper()
                            }
                            processed_data.append(processed_item)
                        except (KeyError, ValueError, TypeError) as e:
                            print(f"处理项目时出错: {e}")
                            # 跳过有问题的项目，继续处理其他项目
                            continue
                    
                    result['data'] = processed_data
                    result['processed_count'] = len(processed_data)
                    result['status'] = 'success'
                    
                except json.JSONDecodeError as e:
                    print(f"JSON解析错误: {e}")
                    result['status'] = 'json_error'
                    result['error'] = str(e)
                    
                except Exception as e:
                    print(f"数据处理错误: {e}")
                    result['status'] = 'processing_error'
                    result['error'] = str(e)
                    
        except FileNotFoundError as e:
            print(f"文件未找到: {e}")
            result['status'] = 'file_not_found'
            result['error'] = str(e)
            
        except PermissionError as e:
            print(f"权限错误: {e}")
            result['status'] = 'permission_error'
            result['error'] = str(e)
            
        except Exception as e:
            print(f"文件操作错误: {e}")
            result['status'] = 'file_error'
            result['error'] = str(e)
        
        return result
    
    # 创建测试文件
    test_files = {
        'valid.json': '[{"id": "1", "value": "10.5", "name": "item1"}, {"id": "2", "value": "20.3", "name": "item2"}]',
        'invalid.json': '{invalid json content}',
        'partial.json': '[{"id": "1", "value": "10.5"}, {"id": "abc", "value": "20.3", "name": "item2"}]'
    }
    
    # 创建测试文件
    for filename, content in test_files.items():
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"创建测试文件失败: {e}")
    
    # 测试文件处理
    test_filenames = list(test_files.keys()) + ['nonexistent.json']
    
    print("测试嵌套异常处理：")
    for filename in test_filenames:
        print(f"\n处理文件: {filename}")
        result = read_and_process_file(filename)
        print(f"结果: {result}")
    
    # 清理测试文件
    import os
    for filename in test_files.keys():
        try:
            os.remove(filename)
        except:
            pass


def demonstrate_exception_grouping():
    """演示异常分组和统一处理"""
    print_section("5. 异常分组和统一处理策略")
    
    class DataProcessor:
        """数据处理器，演示异常分组处理"""
        
        def __init__(self):
            self.error_counts = {
                'validation_errors': 0,
                'conversion_errors': 0,
                'system_errors': 0,
                'unknown_errors': 0
            }
        
        def process_batch(self, data_batch: List[Dict[str, Any]]) -> Dict[str, Any]:
            """批量处理数据"""
            successful_items = []
            failed_items = []
            
            for i, item in enumerate(data_batch):
                try:
                    processed_item = self._process_single_item(item)
                    successful_items.append(processed_item)
                    
                except (KeyError, ValueError, TypeError) as e:
                    # 数据验证和转换错误
                    self.error_counts['validation_errors'] += 1
                    failed_items.append({
                        'index': i,
                        'item': item,
                        'error_type': 'validation_error',
                        'error_message': str(e)
                    })
                    print(f"数据验证错误 (项目 {i}): {e}")
                    
                except (OverflowError, ZeroDivisionError) as e:
                    # 数值计算错误
                    self.error_counts['conversion_errors'] += 1
                    failed_items.append({
                        'index': i,
                        'item': item,
                        'error_type': 'calculation_error',
                        'error_message': str(e)
                    })
                    print(f"计算错误 (项目 {i}): {e}")
                    
                except (OSError, MemoryError) as e:
                    # 系统级错误
                    self.error_counts['system_errors'] += 1
                    failed_items.append({
                        'index': i,
                        'item': item,
                        'error_type': 'system_error',
                        'error_message': str(e)
                    })
                    print(f"系统错误 (项目 {i}): {e}")
                    
                except Exception as e:
                    # 未知错误
                    self.error_counts['unknown_errors'] += 1
                    failed_items.append({
                        'index': i,
                        'item': item,
                        'error_type': 'unknown_error',
                        'error_message': str(e)
                    })
                    print(f"未知错误 (项目 {i}): {e}")
            
            return {
                'successful_count': len(successful_items),
                'failed_count': len(failed_items),
                'successful_items': successful_items,
                'failed_items': failed_items,
                'error_summary': self.error_counts.copy()
            }
        
        def _process_single_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
            """处理单个数据项"""
            # 验证必需字段
            if 'id' not in item:
                raise KeyError("缺少必需字段: id")
            if 'value' not in item:
                raise KeyError("缺少必需字段: value")
            
            # 类型转换
            item_id = int(item['id'])
            value = float(item['value'])
            
            # 数值验证
            if value <= 0:
                raise ValueError("value必须大于0")
            
            # 计算处理
            processed_value = 100 / value  # 可能导致ZeroDivisionError
            
            return {
                'id': item_id,
                'original_value': value,
                'processed_value': processed_value,
                'status': 'processed'
            }
    
    # 测试数据
    test_data = [
        {'id': '1', 'value': '10.5'},      # 正常
        {'id': '2', 'value': '0'},         # ZeroDivisionError
        {'id': 'abc', 'value': '20.3'},    # ValueError (id转换)
        {'value': '15.2'},                 # KeyError (缺少id)
        {'id': '4', 'value': 'xyz'},       # ValueError (value转换)
        {'id': '5', 'value': '25.0'},      # 正常
        {'id': '6'},                       # KeyError (缺少value)
    ]
    
    print("测试异常分组处理：")
    processor = DataProcessor()
    result = processor.process_batch(test_data)
    
    print(f"\n处理结果摘要：")
    print(f"成功处理: {result['successful_count']} 项")
    print(f"处理失败: {result['failed_count']} 项")
    print(f"错误统计: {result['error_summary']}")
    
    print(f"\n成功处理的项目：")
    for item in result['successful_items']:
        print(f"  {item}")
    
    print(f"\n失败的项目：")
    for item in result['failed_items']:
        print(f"  索引 {item['index']}: {item['error_type']} - {item['error_message']}")


def demonstrate_best_practices():
    """演示多个except子句的最佳实践"""
    print_section("6. 多个except子句的最佳实践")
    
    print("最佳实践总结：")
    print("""
    1. 异常处理顺序：从具体到一般
       - 先处理具体的异常类型
       - 最后处理通用的Exception
    
    2. 合理分组异常：
       - 将相关的异常类型组合在一起
       - 为不同类型的错误提供不同的处理逻辑
    
    3. 提供有意义的错误信息：
       - 记录异常的详细信息
       - 为用户提供友好的错误提示
    
    4. 避免过度捕获：
       - 不要使用裸露的except子句
       - 只捕获你能够处理的异常
    
    5. 考虑异常的传播：
       - 在适当的层级处理异常
       - 必要时重新抛出异常
    
    6. 使用日志记录：
       - 记录异常信息用于调试
       - 区分不同级别的错误
    """)
    
    # 最佳实践示例
    def best_practice_example(data: Dict[str, Any]) -> Dict[str, Any]:
        """最佳实践示例函数"""
        try:
            # 业务逻辑
            result = {
                'user_id': int(data['user_id']),
                'username': str(data['username']).strip(),
                'email': str(data['email']).lower(),
                'age': int(data['age'])
            }
            
            # 数据验证
            if result['age'] < 0 or result['age'] > 150:
                raise ValueError("年龄必须在0-150之间")
            
            if '@' not in result['email']:
                raise ValueError("邮箱格式不正确")
            
            return {'status': 'success', 'data': result}
            
        except KeyError as e:
            # 处理缺少必需字段的情况
            error_msg = f"缺少必需字段: {e}"
            print(f"数据验证错误: {error_msg}")
            return {
                'status': 'validation_error',
                'error': error_msg,
                'error_type': 'missing_field'
            }
            
        except (ValueError, TypeError) as e:
            # 处理数据类型和值错误
            error_msg = f"数据格式错误: {e}"
            print(f"数据格式错误: {error_msg}")
            return {
                'status': 'format_error',
                'error': error_msg,
                'error_type': 'invalid_format'
            }
            
        except Exception as e:
            # 处理未预期的异常
            error_msg = f"处理过程中发生未知错误: {e}"
            print(f"未知错误: {error_msg}")
            # 在实际应用中，这里应该记录到日志系统
            return {
                'status': 'system_error',
                'error': '系统错误，请稍后重试',
                'error_type': 'system_error'
            }
    
    # 测试最佳实践
    test_cases = [
        {'user_id': '123', 'username': 'john_doe', 'email': 'john@example.com', 'age': '25'},
        {'user_id': '456', 'username': 'jane_doe', 'age': '30'},  # 缺少email
        {'user_id': 'abc', 'username': 'bob', 'email': 'bob@example.com', 'age': '35'},  # user_id不是数字
        {'user_id': '789', 'username': 'alice', 'email': 'invalid-email', 'age': '28'},  # 邮箱格式错误
        {'user_id': '101', 'username': 'charlie', 'email': 'charlie@example.com', 'age': '200'},  # 年龄超出范围
    ]
    
    print("\n测试最佳实践示例：")
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n测试 {i}: {test_case}")
        result = best_practice_example(test_case)
        print(f"结果: {result}")


def main():
    """主函数"""
    print("Python异常处理 - 多个except子句的处理")
    print("=" * 60)
    
    try:
        # 演示各种多个except子句的用法
        demonstrate_multiple_except_basic()
        demonstrate_exception_hierarchy()
        demonstrate_multiple_exception_types()
        demonstrate_nested_exception_handling()
        demonstrate_exception_grouping()
        demonstrate_best_practices()
        
        print_section("学习总结")
        print("""
        多个except子句处理要点：
        
        1. 异常处理顺序很重要：
           - 从具体异常到一般异常
           - 子类异常在父类异常之前
        
        2. 合理使用异常分组：
           - 将相关异常组合处理
           - 为不同错误类型提供不同处理策略
        
        3. 嵌套异常处理：
           - 在不同层级处理不同类型的异常
           - 保持代码的清晰和可维护性
        
        4. 最佳实践：
           - 提供有意义的错误信息
           - 记录异常用于调试
           - 避免过度捕获异常
           - 考虑异常的传播和处理层级
        
        下一步学习：
        - 04_else_finally.py: else和finally子句
        - 05_raise_exception.py: 抛出异常
        - 06_custom_exceptions.py: 自定义异常类
        """)
        
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"程序执行过程中发生错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()