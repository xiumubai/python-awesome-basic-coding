#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抛出异常的使用

本文件详细演示如何在Python中主动抛出异常，包括raise语句的各种用法、
重新抛出异常、异常传播机制和最佳实践。

学习目标：
1. 掌握raise语句的基本用法
2. 学会抛出不同类型的异常
3. 理解异常的重新抛出机制
4. 掌握异常传播和调用栈
5. 学会在适当的时机抛出异常
"""

import sys
import traceback
from typing import Any, List, Dict, Optional, Union
from datetime import datetime
import json


def print_section(title: str) -> None:
    """打印章节标题"""
    print("\n" + "=" * 60)
    print(f"{title}")
    print("=" * 60)


def demonstrate_basic_raise():
    """演示raise语句的基本用法"""
    print_section("1. raise语句的基本用法")
    
    print("raise语句的几种形式：")
    print("1. raise ExceptionType()          # 抛出异常实例")
    print("2. raise ExceptionType(message)   # 抛出带消息的异常")
    print("3. raise                          # 重新抛出当前异常")
    print("4. raise exception_instance       # 抛出异常实例")
    
    def validate_age(age: Any) -> int:
        """验证年龄的函数，演示基本的raise用法"""
        print(f"\n验证年龄: {age} (类型: {type(age).__name__})")
        
        # 检查类型
        if not isinstance(age, (int, float)):
            # 抛出类型错误
            raise TypeError(f"年龄必须是数字类型，但得到了 {type(age).__name__}")
        
        # 转换为整数
        age = int(age)
        
        # 检查范围
        if age < 0:
            # 抛出值错误
            raise ValueError("年龄不能为负数")
        
        if age > 150:
            # 抛出值错误
            raise ValueError(f"年龄 {age} 超出合理范围 (0-150)")
        
        print(f"年龄验证通过: {age}")
        return age
    
    def validate_email(email: Any) -> str:
        """验证邮箱的函数"""
        print(f"\n验证邮箱: {email}")
        
        if not isinstance(email, str):
            raise TypeError("邮箱必须是字符串类型")
        
        if not email:
            raise ValueError("邮箱不能为空")
        
        if '@' not in email:
            raise ValueError("邮箱格式不正确：缺少@符号")
        
        if email.count('@') != 1:
            raise ValueError("邮箱格式不正确：@符号数量不正确")
        
        local, domain = email.split('@')
        
        if not local:
            raise ValueError("邮箱格式不正确：本地部分为空")
        
        if not domain:
            raise ValueError("邮箱格式不正确：域名部分为空")
        
        if '.' not in domain:
            raise ValueError("邮箱格式不正确：域名缺少点号")
        
        print(f"邮箱验证通过: {email}")
        return email
    
    # 测试年龄验证
    age_test_cases = [25, "30", -5, 200, "abc", None, 45.5]
    
    print("\n测试年龄验证：")
    for test_age in age_test_cases:
        try:
            result = validate_age(test_age)
            print(f"✓ 验证成功: {result}")
        except (TypeError, ValueError) as e:
            print(f"✗ 验证失败: {e}")
        print("-" * 40)
    
    # 测试邮箱验证
    email_test_cases = [
        "user@example.com",
        "invalid-email",
        "@example.com",
        "user@",
        "user@@example.com",
        "",
        None,
        123
    ]
    
    print("\n测试邮箱验证：")
    for test_email in email_test_cases:
        try:
            result = validate_email(test_email)
            print(f"✓ 验证成功: {result}")
        except (TypeError, ValueError) as e:
            print(f"✗ 验证失败: {e}")
        print("-" * 40)


def demonstrate_reraise_exception():
    """演示重新抛出异常"""
    print_section("2. 重新抛出异常")
    
    print("重新抛出异常的场景：")
    print("- 记录异常信息后重新抛出")
    print("- 在异常处理中进行清理后重新抛出")
    print("- 将底层异常转换为更高层的异常")
    
    def process_data_with_logging(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """处理数据并记录异常"""
        print(f"\n开始处理数据，共 {len(data)} 条记录")
        processed_data = []
        
        for i, item in enumerate(data):
            try:
                print(f"处理第 {i+1} 条记录: {item}")
                
                # 验证数据结构
                if not isinstance(item, dict):
                    raise TypeError(f"记录 {i+1} 必须是字典类型")
                
                # 验证必需字段
                required_fields = ['id', 'name', 'value']
                for field in required_fields:
                    if field not in item:
                        raise KeyError(f"记录 {i+1} 缺少必需字段: {field}")
                
                # 验证数据类型
                if not isinstance(item['id'], int):
                    raise ValueError(f"记录 {i+1} 的id必须是整数")
                
                if not isinstance(item['name'], str):
                    raise ValueError(f"记录 {i+1} 的name必须是字符串")
                
                if not isinstance(item['value'], (int, float)):
                    raise ValueError(f"记录 {i+1} 的value必须是数字")
                
                # 处理成功
                processed_item = {
                    'id': item['id'],
                    'name': item['name'].strip().title(),
                    'value': float(item['value']),
                    'processed_at': datetime.now().isoformat()
                }
                
                processed_data.append(processed_item)
                print(f"✓ 记录 {i+1} 处理成功")
                
            except (TypeError, KeyError, ValueError) as e:
                # 记录异常信息
                error_info = {
                    'timestamp': datetime.now().isoformat(),
                    'record_index': i + 1,
                    'record_data': item,
                    'error_type': type(e).__name__,
                    'error_message': str(e)
                }
                
                print(f"✗ 记录异常信息: {json.dumps(error_info, ensure_ascii=False, indent=2)}")
                
                # 重新抛出异常，保持原始异常信息
                print("重新抛出异常以便上层处理")
                raise  # 重新抛出当前异常
            
            except Exception as e:
                # 处理未预期的异常
                print(f"✗ 发生未预期的异常: {type(e).__name__}: {e}")
                print("进行必要的清理工作")
                
                # 清理已处理的数据（示例）
                processed_data.clear()
                
                # 重新抛出异常
                raise RuntimeError(f"数据处理失败，在第 {i+1} 条记录时发生未预期错误") from e
        
        print(f"所有数据处理完成，共处理 {len(processed_data)} 条记录")
        return processed_data
    
    def safe_process_data(data: List[Dict[str, Any]]) -> Optional[List[Dict[str, Any]]]:
        """安全地处理数据，捕获并处理异常"""
        try:
            return process_data_with_logging(data)
        except (TypeError, KeyError, ValueError) as e:
            print(f"数据验证错误: {e}")
            print("返回None表示处理失败")
            return None
        except RuntimeError as e:
            print(f"运行时错误: {e}")
            print("返回None表示处理失败")
            return None
        except Exception as e:
            print(f"未知错误: {e}")
            print("返回None表示处理失败")
            return None
    
    # 测试数据
    test_datasets = [
        # 正常数据
        [
            {'id': 1, 'name': 'alice', 'value': 100},
            {'id': 2, 'name': 'bob', 'value': 200}
        ],
        # 包含错误数据
        [
            {'id': 1, 'name': 'alice', 'value': 100},
            {'id': '2', 'name': 'bob', 'value': 200},  # id类型错误
        ],
        # 缺少字段
        [
            {'id': 1, 'name': 'alice', 'value': 100},
            {'id': 2, 'name': 'bob'},  # 缺少value字段
        ],
        # 非字典类型
        [
            {'id': 1, 'name': 'alice', 'value': 100},
            "invalid_data",  # 非字典类型
        ]
    ]
    
    print("\n测试重新抛出异常：")
    for i, dataset in enumerate(test_datasets, 1):
        print(f"\n{'='*20} 测试数据集 {i} {'='*20}")
        result = safe_process_data(dataset)
        if result:
            print(f"处理成功，结果数量: {len(result)}")
        else:
            print("处理失败")


def demonstrate_exception_chaining():
    """演示异常链（Exception Chaining）"""
    print_section("3. 异常链和上下文")
    
    print("异常链的两种形式：")
    print("1. raise new_exception from original_exception  # 显式链接")
    print("2. 在except块中raise new_exception             # 隐式链接")
    
    def read_config_file(filename: str) -> Dict[str, Any]:
        """读取配置文件，演示异常链"""
        print(f"\n尝试读取配置文件: {filename}")
        
        try:
            # 尝试打开文件
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            print("文件读取成功，尝试解析JSON")
            
            # 尝试解析JSON
            config = json.loads(content)
            
            print("JSON解析成功")
            return config
            
        except FileNotFoundError as e:
            # 显式异常链：使用from关键字
            print(f"文件未找到: {e}")
            raise RuntimeError(f"无法加载配置文件 {filename}") from e
            
        except json.JSONDecodeError as e:
            # 显式异常链：提供更多上下文信息
            print(f"JSON解析错误: {e}")
            raise ValueError(f"配置文件 {filename} 格式不正确") from e
            
        except PermissionError as e:
            # 显式异常链
            print(f"权限错误: {e}")
            raise RuntimeError(f"没有权限读取配置文件 {filename}") from e
            
        except Exception as e:
            # 处理其他异常，隐式异常链
            print(f"读取配置时发生未知错误: {e}")
            # 这里没有使用from，会创建隐式异常链
            raise RuntimeError(f"配置文件 {filename} 处理失败")
    
    def initialize_application(config_file: str) -> Dict[str, Any]:
        """初始化应用程序"""
        print(f"\n初始化应用程序，配置文件: {config_file}")
        
        try:
            # 读取配置
            config = read_config_file(config_file)
            
            # 验证配置
            required_keys = ['app_name', 'version', 'database']
            for key in required_keys:
                if key not in config:
                    raise KeyError(f"配置文件缺少必需的键: {key}")
            
            print("配置验证通过")
            
            # 模拟数据库连接
            db_config = config['database']
            if 'host' not in db_config:
                raise ValueError("数据库配置缺少host信息")
            
            print("应用程序初始化成功")
            return {
                'status': 'success',
                'app_name': config['app_name'],
                'version': config['version']
            }
            
        except (RuntimeError, ValueError, KeyError) as e:
            # 将底层异常包装为应用程序异常
            print(f"应用程序初始化失败: {e}")
            raise RuntimeError(f"应用程序启动失败") from e
    
    def print_exception_chain(e: Exception) -> None:
        """打印完整的异常链"""
        print("\n异常链信息：")
        print("-" * 40)
        
        current = e
        level = 0
        
        while current:
            indent = "  " * level
            print(f"{indent}{type(current).__name__}: {current}")
            
            # 检查是否有原因异常（显式链接）
            if hasattr(current, '__cause__') and current.__cause__:
                print(f"{indent}  ↑ 由以下异常引起 (显式链接):")
                current = current.__cause__
                level += 1
            # 检查是否有上下文异常（隐式链接）
            elif hasattr(current, '__context__') and current.__context__:
                print(f"{indent}  ↑ 在处理以下异常时发生 (隐式链接):")
                current = current.__context__
                level += 1
            else:
                break
        
        print("-" * 40)
    
    # 创建测试配置文件
    test_configs = {
        'valid_config.json': {
            'app_name': 'TestApp',
            'version': '1.0.0',
            'database': {
                'host': 'localhost',
                'port': 5432
            }
        },
        'invalid_json.json': '{"app_name": "TestApp", "version": }',  # 无效JSON
        'incomplete_config.json': {
            'app_name': 'TestApp'
            # 缺少version和database
        }
    }
    
    # 创建测试文件
    for filename, content in test_configs.items():
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                if isinstance(content, dict):
                    json.dump(content, f, ensure_ascii=False, indent=2)
                else:
                    f.write(content)
        except Exception as e:
            print(f"创建测试文件 {filename} 失败: {e}")
    
    # 测试异常链
    test_files = [
        'valid_config.json',
        'invalid_json.json', 
        'incomplete_config.json',
        'nonexistent_config.json'
    ]
    
    print("\n测试异常链：")
    for filename in test_files:
        print(f"\n{'='*30} 测试 {filename} {'='*30}")
        
        try:
            result = initialize_application(filename)
            print(f"初始化成功: {result}")
            
        except Exception as e:
            print(f"初始化失败: {e}")
            print_exception_chain(e)
    
    # 清理测试文件
    import os
    for filename in test_configs.keys():
        try:
            if os.path.exists(filename):
                os.remove(filename)
        except:
            pass


def demonstrate_custom_raise_scenarios():
    """演示自定义抛出异常的场景"""
    print_section("4. 自定义抛出异常的场景")
    
    print("常见的抛出异常场景：")
    print("1. 参数验证失败")
    print("2. 业务逻辑约束违反")
    print("3. 资源不可用")
    print("4. 操作不被允许")
    print("5. 数据状态不一致")
    
    class BankAccount:
        """银行账户类，演示业务逻辑中的异常抛出"""
        
        def __init__(self, account_id: str, initial_balance: float = 0.0):
            if not isinstance(account_id, str) or not account_id.strip():
                raise ValueError("账户ID必须是非空字符串")
            
            if not isinstance(initial_balance, (int, float)):
                raise TypeError("初始余额必须是数字类型")
            
            if initial_balance < 0:
                raise ValueError("初始余额不能为负数")
            
            self.account_id = account_id.strip()
            self.balance = float(initial_balance)
            self.is_frozen = False
            self.transaction_history = []
            
            print(f"账户创建成功: {self.account_id}, 初始余额: {self.balance}")
        
        def deposit(self, amount: float, description: str = "") -> None:
            """存款操作"""
            print(f"\n尝试存款: {amount}")
            
            # 参数验证
            if not isinstance(amount, (int, float)):
                raise TypeError("存款金额必须是数字类型")
            
            if amount <= 0:
                raise ValueError("存款金额必须大于0")
            
            # 业务逻辑验证
            if self.is_frozen:
                raise RuntimeError("账户已冻结，无法进行存款操作")
            
            # 执行存款
            self.balance += amount
            transaction = {
                'type': 'deposit',
                'amount': amount,
                'balance_after': self.balance,
                'description': description,
                'timestamp': datetime.now().isoformat()
            }
            self.transaction_history.append(transaction)
            
            print(f"存款成功，当前余额: {self.balance}")
        
        def withdraw(self, amount: float, description: str = "") -> None:
            """取款操作"""
            print(f"\n尝试取款: {amount}")
            
            # 参数验证
            if not isinstance(amount, (int, float)):
                raise TypeError("取款金额必须是数字类型")
            
            if amount <= 0:
                raise ValueError("取款金额必须大于0")
            
            # 业务逻辑验证
            if self.is_frozen:
                raise RuntimeError("账户已冻结，无法进行取款操作")
            
            if amount > self.balance:
                raise ValueError(f"余额不足，当前余额: {self.balance}, 尝试取款: {amount}")
            
            # 单次取款限额检查
            if amount > 10000:
                raise ValueError(f"单次取款金额不能超过10000，尝试取款: {amount}")
            
            # 执行取款
            self.balance -= amount
            transaction = {
                'type': 'withdraw',
                'amount': amount,
                'balance_after': self.balance,
                'description': description,
                'timestamp': datetime.now().isoformat()
            }
            self.transaction_history.append(transaction)
            
            print(f"取款成功，当前余额: {self.balance}")
        
        def transfer(self, target_account: 'BankAccount', amount: float, description: str = "") -> None:
            """转账操作"""
            print(f"\n尝试转账: {amount} 到账户 {target_account.account_id}")
            
            # 参数验证
            if not isinstance(target_account, BankAccount):
                raise TypeError("目标账户必须是BankAccount实例")
            
            if target_account.account_id == self.account_id:
                raise ValueError("不能向自己的账户转账")
            
            if not isinstance(amount, (int, float)):
                raise TypeError("转账金额必须是数字类型")
            
            if amount <= 0:
                raise ValueError("转账金额必须大于0")
            
            # 业务逻辑验证
            if self.is_frozen:
                raise RuntimeError("源账户已冻结，无法进行转账操作")
            
            if target_account.is_frozen:
                raise RuntimeError("目标账户已冻结，无法接收转账")
            
            if amount > self.balance:
                raise ValueError(f"余额不足，当前余额: {self.balance}, 尝试转账: {amount}")
            
            # 转账限额检查
            if amount > 50000:
                raise ValueError(f"单次转账金额不能超过50000，尝试转账: {amount}")
            
            # 执行转账（原子操作）
            try:
                # 从源账户扣款
                self.balance -= amount
                
                # 向目标账户存款
                target_account.balance += amount
                
                # 记录交易历史
                source_transaction = {
                    'type': 'transfer_out',
                    'amount': amount,
                    'balance_after': self.balance,
                    'target_account': target_account.account_id,
                    'description': description,
                    'timestamp': datetime.now().isoformat()
                }
                
                target_transaction = {
                    'type': 'transfer_in',
                    'amount': amount,
                    'balance_after': target_account.balance,
                    'source_account': self.account_id,
                    'description': description,
                    'timestamp': datetime.now().isoformat()
                }
                
                self.transaction_history.append(source_transaction)
                target_account.transaction_history.append(target_transaction)
                
                print(f"转账成功，源账户余额: {self.balance}, 目标账户余额: {target_account.balance}")
                
            except Exception as e:
                # 如果转账过程中出现异常，需要回滚
                print(f"转账过程中发生错误: {e}")
                raise RuntimeError("转账失败，请稍后重试") from e
        
        def freeze_account(self, reason: str = "") -> None:
            """冻结账户"""
            print(f"\n冻结账户: {self.account_id}, 原因: {reason}")
            self.is_frozen = True
        
        def unfreeze_account(self) -> None:
            """解冻账户"""
            print(f"\n解冻账户: {self.account_id}")
            self.is_frozen = False
        
        def get_balance(self) -> float:
            """获取余额"""
            if self.is_frozen:
                raise RuntimeError("账户已冻结，无法查询余额")
            return self.balance
        
        def __str__(self) -> str:
            status = "冻结" if self.is_frozen else "正常"
            return f"账户[{self.account_id}]: 余额={self.balance}, 状态={status}"
    
    # 测试银行账户操作
    print("\n测试银行账户操作：")
    
    try:
        # 创建账户
        print("\n1. 创建账户测试")
        account1 = BankAccount("ACC001", 1000)
        account2 = BankAccount("ACC002", 500)
        
        # 正常操作
        print("\n2. 正常操作测试")
        account1.deposit(200, "工资")
        account1.withdraw(100, "购物")
        account1.transfer(account2, 300, "转账给朋友")
        
        print(f"\n账户状态:")
        print(f"账户1: {account1}")
        print(f"账户2: {account2}")
        
        # 异常操作测试
        print("\n3. 异常操作测试")
        
        # 测试余额不足
        try:
            account1.withdraw(2000)
        except ValueError as e:
            print(f"✗ 余额不足: {e}")
        
        # 测试取款限额
        try:
            account1.withdraw(15000)
        except ValueError as e:
            print(f"✗ 超出限额: {e}")
        
        # 测试冻结账户
        print("\n4. 冻结账户测试")
        account1.freeze_account("可疑交易")
        
        try:
            account1.deposit(100)
        except RuntimeError as e:
            print(f"✗ 账户冻结: {e}")
        
        try:
            account1.get_balance()
        except RuntimeError as e:
            print(f"✗ 账户冻结: {e}")
        
        # 解冻账户
        account1.unfreeze_account()
        balance = account1.get_balance()
        print(f"✓ 解冻后余额: {balance}")
        
        # 测试无效参数
        print("\n5. 无效参数测试")
        
        try:
            BankAccount("", 1000)  # 空账户ID
        except ValueError as e:
            print(f"✗ 无效账户ID: {e}")
        
        try:
            BankAccount("ACC003", -100)  # 负初始余额
        except ValueError as e:
            print(f"✗ 负初始余额: {e}")
        
        try:
            account1.deposit("100")  # 非数字金额
        except TypeError as e:
            print(f"✗ 无效金额类型: {e}")
        
    except Exception as e:
        print(f"测试过程中发生未预期错误: {e}")
        traceback.print_exc()


def demonstrate_raise_best_practices():
    """演示抛出异常的最佳实践"""
    print_section("5. 抛出异常的最佳实践")
    
    print("抛出异常的最佳实践：")
    print("""
    1. 选择合适的异常类型：
       - ValueError: 值不正确
       - TypeError: 类型不正确
       - KeyError: 键不存在
       - IndexError: 索引超出范围
       - RuntimeError: 运行时错误
    
    2. 提供清晰的错误消息：
       - 说明什么出错了
       - 提供期望的值或格式
       - 包含相关的上下文信息
    
    3. 使用异常链：
       - 使用from关键字保留原始异常信息
       - 提供更高层次的错误描述
    
    4. 在适当的层次抛出异常：
       - 在检测到错误的地方立即抛出
       - 不要过早捕获异常
       - 让调用者决定如何处理
    
    5. 避免过度使用异常：
       - 异常应该用于异常情况
       - 不要用异常来控制正常的程序流程
       - 考虑返回特殊值或使用Optional
    """)
    
    # 最佳实践示例
    def parse_user_input(user_input: str) -> Dict[str, Any]:
        """解析用户输入的最佳实践示例"""
        print(f"\n解析用户输入: '{user_input}'")
        
        # 1. 参数验证 - 使用合适的异常类型和清晰的消息
        if not isinstance(user_input, str):
            raise TypeError(
                f"用户输入必须是字符串类型，但得到了 {type(user_input).__name__}"
            )
        
        if not user_input.strip():
            raise ValueError("用户输入不能为空或只包含空白字符")
        
        # 2. 格式验证
        parts = user_input.strip().split(',')
        if len(parts) != 3:
            raise ValueError(
                f"用户输入格式不正确，期望格式: 'name,age,email'，"
                f"但得到了 {len(parts)} 个部分: {parts}"
            )
        
        name, age_str, email = [part.strip() for part in parts]
        
        # 3. 各字段验证 - 提供具体的错误信息
        if not name:
            raise ValueError("姓名不能为空")
        
        if len(name) > 50:
            raise ValueError(f"姓名长度不能超过50个字符，当前长度: {len(name)}")
        
        # 年龄验证
        try:
            age = int(age_str)
        except ValueError as e:
            # 使用异常链提供更好的错误信息
            raise ValueError(f"年龄必须是整数，但得到了: '{age_str}'") from e
        
        if not (0 <= age <= 150):
            raise ValueError(f"年龄必须在0-150之间，但得到了: {age}")
        
        # 邮箱验证
        if not email:
            raise ValueError("邮箱不能为空")
        
        if '@' not in email or '.' not in email:
            raise ValueError(f"邮箱格式不正确: '{email}'，期望格式: 'user@domain.com'")
        
        # 返回解析结果
        result = {
            'name': name,
            'age': age,
            'email': email
        }
        
        print(f"解析成功: {result}")
        return result
    
    # 对比：不好的异常处理方式
    def bad_parse_user_input(user_input: str) -> Dict[str, Any]:
        """不好的异常处理示例（仅用于对比）"""
        print(f"\n不好的解析方式: '{user_input}'")
        
        try:
            parts = user_input.split(',')
            name = parts[0]
            age = int(parts[1])
            email = parts[2]
            
            return {'name': name, 'age': age, 'email': email}
            
        except:
            # 不好的做法：捕获所有异常并抛出通用错误
            raise Exception("输入错误")  # 错误信息不明确
    
    # 测试最佳实践
    test_inputs = [
        "Alice,25,alice@example.com",  # 正常输入
        "Bob,30",                      # 缺少字段
        "Charlie,abc,charlie@example.com",  # 年龄不是数字
        "David,200,david@example.com",      # 年龄超出范围
        "Eve,25,invalid-email",             # 邮箱格式错误
        "",                                  # 空输入
        "   ",                              # 只有空白字符
        None,                               # 非字符串类型
    ]
    
    print("\n测试最佳实践示例：")
    for i, test_input in enumerate(test_inputs, 1):
        print(f"\n--- 测试 {i} ---")
        
        # 测试最佳实践方法
        try:
            result = parse_user_input(test_input)
            print(f"✓ 最佳实践解析成功: {result}")
        except (TypeError, ValueError) as e:
            print(f"✗ 最佳实践解析失败: {e}")
        except Exception as e:
            print(f"✗ 最佳实践发生未预期错误: {e}")
        
        # 对比不好的方法（跳过None类型，因为会导致AttributeError）
        if test_input is not None:
            try:
                result = bad_parse_user_input(test_input)
                print(f"✓ 不好的方法解析成功: {result}")
            except Exception as e:
                print(f"✗ 不好的方法解析失败: {e}")


def main():
    """主函数"""
    print("Python异常处理 - 抛出异常的使用")
    print("=" * 60)
    
    try:
        # 演示各种抛出异常的用法
        demonstrate_basic_raise()
        demonstrate_reraise_exception()
        demonstrate_exception_chaining()
        demonstrate_custom_raise_scenarios()
        demonstrate_raise_best_practices()
        
        print_section("学习总结")
        print("""
        抛出异常要点：
        
        1. raise语句的用法：
           - raise ExceptionType(message)  # 抛出新异常
           - raise                         # 重新抛出当前异常
           - raise new_exception from old  # 异常链
        
        2. 选择合适的异常类型：
           - ValueError: 值错误
           - TypeError: 类型错误
           - RuntimeError: 运行时错误
           - 自定义异常类
        
        3. 异常链的使用：
           - 使用from保留原始异常信息
           - 提供更高层次的错误描述
           - 帮助调试和问题定位
        
        4. 最佳实践：
           - 提供清晰的错误消息
           - 在适当的层次抛出异常
           - 避免过度使用异常
           - 使用异常链保留上下文
        
        下一步学习：
        - 06_custom_exceptions.py: 自定义异常类
        - 07_exception_chaining.py: 异常链详解
        - 08_logging_exceptions.py: 异常日志记录
        """)
        
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"程序执行过程中发生错误: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()