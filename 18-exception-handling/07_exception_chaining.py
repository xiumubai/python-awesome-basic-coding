#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
异常链和上下文管理

本文件详细演示Python中异常链的概念和使用方法，包括异常的因果关系、
上下文保留、异常链的创建和分析等高级异常处理技术。

学习目标：
1. 理解异常链的概念和重要性
2. 掌握raise...from语句的使用
3. 学会分析和处理异常链
4. 了解异常上下文的保留和抑制
5. 掌握在实际项目中使用异常链
"""

import sys
import traceback
from typing import Any, List, Dict, Optional, Union, Type
from datetime import datetime
import json
import logging
import functools
from contextlib import contextmanager


def print_section(title: str) -> None:
    """打印章节标题"""
    print("\n" + "=" * 60)
    print(f"{title}")
    print("=" * 60)


def demonstrate_basic_exception_chaining():
    """演示基本的异常链"""
    print_section("1. 异常链基础概念")
    
    print("异常链的作用：")
    print("- 保留原始异常信息")
    print("- 提供完整的错误上下文")
    print("- 便于问题的根因分析")
    print("- 支持异常的层次化处理")
    
    print("\nPython异常链的三种形式：")
    print("1. 隐式链接 (__context__)：异常处理过程中发生新异常")
    print("2. 显式链接 (__cause__)：使用 raise...from 语句")
    print("3. 抑制链接：使用 raise...from None")
    
    def demonstrate_implicit_chaining():
        """演示隐式异常链"""
        print("\n--- 隐式异常链 (__context__) ---")
        print("当在异常处理过程中发生新异常时，Python会自动创建隐式链接")
        
        def problematic_function():
            """有问题的函数，会产生隐式异常链"""
            try:
                # 第一个异常：除零错误
                result = 10 / 0
            except ZeroDivisionError:
                # 在处理异常时又发生新异常：类型错误
                invalid_operation = "string" + 42
        
        try:
            problematic_function()
        except Exception as e:
            print(f"✓ 捕获异常: {type(e).__name__}: {e}")
            print(f"  当前异常: {e}")
            print(f"  上下文异常: {e.__context__}")
            print(f"  原因异常: {e.__cause__}")
            
            # 打印完整的异常链
            print("\n  完整异常链:")
            current = e
            level = 0
            while current:
                indent = "  " * (level + 1)
                print(f"{indent}[{level}] {type(current).__name__}: {current}")
                current = current.__context__ or current.__cause__
                level += 1
    
    def demonstrate_explicit_chaining():
        """演示显式异常链"""
        print("\n--- 显式异常链 (__cause__) ---")
        print("使用 'raise...from' 语句明确指定异常的原因")
        
        class DatabaseError(Exception):
            """数据库异常"""
            pass
        
        class UserServiceError(Exception):
            """用户服务异常"""
            pass
        
        def connect_to_database():
            """模拟数据库连接"""
            raise ConnectionError("无法连接到数据库服务器")
        
        def get_user_data(user_id: str):
            """获取用户数据"""
            try:
                connect_to_database()
                # 模拟数据库查询
                return {"id": user_id, "name": "Alice"}
            except ConnectionError as e:
                # 显式链接：将底层异常作为原因
                raise DatabaseError(f"数据库操作失败，用户ID: {user_id}") from e
        
        def process_user_request(user_id: str):
            """处理用户请求"""
            try:
                user_data = get_user_data(user_id)
                return f"处理用户: {user_data['name']}"
            except DatabaseError as e:
                # 再次显式链接
                raise UserServiceError(f"用户服务不可用，请稍后重试") from e
        
        try:
            result = process_user_request("user_123")
            print(f"结果: {result}")
        except UserServiceError as e:
            print(f"✓ 捕获异常: {type(e).__name__}: {e}")
            print(f"  当前异常: {e}")
            print(f"  原因异常: {e.__cause__}")
            print(f"  原因的原因: {e.__cause__.__cause__ if e.__cause__ else None}")
            
            # 分析异常链
            print("\n  异常链分析:")
            current = e
            level = 0
            while current:
                indent = "  " * (level + 1)
                print(f"{indent}[{level}] {type(current).__name__}: {current}")
                if hasattr(current, '__cause__') and current.__cause__:
                    current = current.__cause__
                elif hasattr(current, '__context__') and current.__context__:
                    current = current.__context__
                else:
                    break
                level += 1
    
    def demonstrate_suppressed_chaining():
        """演示抑制异常链"""
        print("\n--- 抑制异常链 (raise...from None) ---")
        print("使用 'raise...from None' 抑制异常链，隐藏底层异常")
        
        class UserFriendlyError(Exception):
            """用户友好异常"""
            pass
        
        def sensitive_operation():
            """敏感操作，可能暴露系统信息"""
            raise FileNotFoundError("/etc/secret/database.conf not found")
        
        def public_api_call():
            """公共API调用，需要隐藏内部错误"""
            try:
                sensitive_operation()
            except FileNotFoundError:
                # 抑制异常链，不暴露敏感信息
                raise UserFriendlyError("服务暂时不可用，请稍后重试") from None
        
        try:
            public_api_call()
        except UserFriendlyError as e:
            print(f"✓ 捕获异常: {type(e).__name__}: {e}")
            print(f"  当前异常: {e}")
            print(f"  原因异常: {e.__cause__}")
            print(f"  上下文异常: {e.__context__}")
            print("  注意: 原因异常和上下文异常都为None，异常链被抑制")
    
    demonstrate_implicit_chaining()
    demonstrate_explicit_chaining()
    demonstrate_suppressed_chaining()


def demonstrate_exception_chain_analysis():
    """演示异常链的分析和处理"""
    print_section("2. 异常链分析和处理")
    
    print("异常链分析的重要性：")
    print("- 快速定位问题根源")
    print("- 理解错误传播路径")
    print("- 提供完整的调试信息")
    print("- 支持智能错误恢复")
    
    class ExceptionChainAnalyzer:
        """异常链分析器"""
        
        @staticmethod
        def get_exception_chain(exception: Exception) -> List[Dict[str, Any]]:
            """获取完整的异常链信息"""
            chain = []
            current = exception
            
            while current:
                chain.append({
                    'type': type(current).__name__,
                    'message': str(current),
                    'module': getattr(type(current), '__module__', 'builtins'),
                    'args': current.args,
                    'has_cause': current.__cause__ is not None,
                    'has_context': current.__context__ is not None,
                    'traceback_summary': ExceptionChainAnalyzer._get_traceback_summary(current)
                })
                
                # 移动到下一个异常
                if current.__cause__:
                    current = current.__cause__
                elif current.__context__:
                    current = current.__context__
                else:
                    break
            
            return chain
        
        @staticmethod
        def _get_traceback_summary(exception: Exception) -> List[Dict[str, Any]]:
            """获取异常的回溯摘要"""
            if not hasattr(exception, '__traceback__') or not exception.__traceback__:
                return []
            
            summary = []
            tb = exception.__traceback__
            
            while tb:
                frame = tb.tb_frame
                summary.append({
                    'filename': frame.f_code.co_filename,
                    'function': frame.f_code.co_name,
                    'lineno': tb.tb_lineno,
                    'locals': {k: str(v)[:100] for k, v in frame.f_locals.items() 
                              if not k.startswith('__')}
                })
                tb = tb.tb_next
            
            return summary
        
        @staticmethod
        def print_chain_analysis(exception: Exception) -> None:
            """打印异常链分析"""
            chain = ExceptionChainAnalyzer.get_exception_chain(exception)
            
            print(f"\n异常链分析 (共 {len(chain)} 层):")
            print("-" * 50)
            
            for i, link in enumerate(chain):
                print(f"\n[{i}] {link['type']}: {link['message']}")
                print(f"    模块: {link['module']}")
                print(f"    参数: {link['args']}")
                print(f"    有原因: {link['has_cause']}")
                print(f"    有上下文: {link['has_context']}")
                
                if link['traceback_summary']:
                    print("    调用栈:")
                    for tb_info in link['traceback_summary'][-3:]:  # 只显示最后3层
                        filename = tb_info['filename'].split('/')[-1]
                        print(f"      {filename}:{tb_info['lineno']} in {tb_info['function']}()")
        
        @staticmethod
        def find_root_cause(exception: Exception) -> Exception:
            """查找根本原因异常"""
            current = exception
            
            while current.__cause__ or current.__context__:
                if current.__cause__:
                    current = current.__cause__
                elif current.__context__:
                    current = current.__context__
                else:
                    break
            
            return current
        
        @staticmethod
        def get_exception_types(exception: Exception) -> List[str]:
            """获取异常链中的所有异常类型"""
            types = []
            current = exception
            
            while current:
                types.append(type(current).__name__)
                
                if current.__cause__:
                    current = current.__cause__
                elif current.__context__:
                    current = current.__context__
                else:
                    break
            
            return types
    
    def test_chain_analysis():
        """测试异常链分析"""
        print("\n测试异常链分析：")
        
        # 创建复杂的异常链
        class NetworkError(Exception):
            pass
        
        class DatabaseError(Exception):
            pass
        
        class ServiceError(Exception):
            pass
        
        class APIError(Exception):
            pass
        
        def network_call():
            """网络调用"""
            raise ConnectionError("网络连接超时")
        
        def database_operation():
            """数据库操作"""
            try:
                network_call()
            except ConnectionError as e:
                raise DatabaseError("数据库连接失败") from e
        
        def business_service():
            """业务服务"""
            try:
                database_operation()
            except DatabaseError as e:
                raise ServiceError("业务服务不可用") from e
        
        def api_endpoint():
            """API端点"""
            try:
                business_service()
            except ServiceError as e:
                raise APIError("API调用失败") from e
        
        try:
            api_endpoint()
        except APIError as e:
            print(f"✓ 捕获顶层异常: {e}")
            
            # 分析异常链
            ExceptionChainAnalyzer.print_chain_analysis(e)
            
            # 查找根本原因
            root_cause = ExceptionChainAnalyzer.find_root_cause(e)
            print(f"\n根本原因: {type(root_cause).__name__}: {root_cause}")
            
            # 获取异常类型列表
            exception_types = ExceptionChainAnalyzer.get_exception_types(e)
            print(f"异常类型链: {' -> '.join(exception_types)}")
    
    test_chain_analysis()


def demonstrate_context_managers_and_chaining():
    """演示上下文管理器与异常链"""
    print_section("3. 上下文管理器与异常链")
    
    print("上下文管理器中的异常处理：")
    print("- __enter__ 方法中的异常")
    print("- __exit__ 方法中的异常")
    print("- with语句块中的异常")
    print("- 异常的传播和抑制")
    
    class ResourceManager:
        """资源管理器示例"""
        
        def __init__(self, name: str, fail_on_enter: bool = False, 
                     fail_on_exit: bool = False, suppress_exception: bool = False):
            self.name = name
            self.fail_on_enter = fail_on_enter
            self.fail_on_exit = fail_on_exit
            self.suppress_exception = suppress_exception
            self.resource = None
        
        def __enter__(self):
            print(f"  进入上下文: {self.name}")
            
            if self.fail_on_enter:
                raise RuntimeError(f"进入 {self.name} 时发生错误")
            
            self.resource = f"Resource-{self.name}"
            return self.resource
        
        def __exit__(self, exc_type, exc_value, traceback):
            print(f"  退出上下文: {self.name}")
            print(f"    异常类型: {exc_type}")
            print(f"    异常值: {exc_value}")
            print(f"    有回溯: {traceback is not None}")
            
            if self.fail_on_exit:
                # 在退出时发生异常
                raise RuntimeError(f"退出 {self.name} 时发生错误")
            
            # 返回True抑制异常，返回False或None传播异常
            return self.suppress_exception
    
    def test_context_manager_exceptions():
        """测试上下文管理器中的异常"""
        print("\n测试上下文管理器异常：")
        
        # 测试1：正常情况
        print("\n1. 正常情况:")
        try:
            with ResourceManager("Normal") as resource:
                print(f"    使用资源: {resource}")
                print("    操作成功")
        except Exception as e:
            print(f"✗ 异常: {e}")
        else:
            print("✓ 正常完成")
        
        # 测试2：进入时异常
        print("\n2. 进入时异常:")
        try:
            with ResourceManager("FailOnEnter", fail_on_enter=True) as resource:
                print(f"    使用资源: {resource}")
        except Exception as e:
            print(f"✗ 异常: {type(e).__name__}: {e}")
        
        # 测试3：with块中异常
        print("\n3. with块中异常:")
        try:
            with ResourceManager("Normal") as resource:
                print(f"    使用资源: {resource}")
                raise ValueError("with块中发生错误")
        except Exception as e:
            print(f"✗ 异常: {type(e).__name__}: {e}")
        
        # 测试4：退出时异常
        print("\n4. 退出时异常:")
        try:
            with ResourceManager("FailOnExit", fail_on_exit=True) as resource:
                print(f"    使用资源: {resource}")
                print("    操作完成")
        except Exception as e:
            print(f"✗ 异常: {type(e).__name__}: {e}")
        
        # 测试5：with块和退出都有异常
        print("\n5. with块和退出都有异常:")
        try:
            with ResourceManager("FailOnExit", fail_on_exit=True) as resource:
                print(f"    使用资源: {resource}")
                raise ValueError("with块中的错误")
        except Exception as e:
            print(f"✗ 异常: {type(e).__name__}: {e}")
            print(f"  原因异常: {e.__cause__}")
            print(f"  上下文异常: {e.__context__}")
        
        # 测试6：抑制异常
        print("\n6. 抑制异常:")
        try:
            with ResourceManager("Suppress", suppress_exception=True) as resource:
                print(f"    使用资源: {resource}")
                raise ValueError("这个异常会被抑制")
            print("✓ 异常被抑制，正常继续")
        except Exception as e:
            print(f"✗ 异常: {type(e).__name__}: {e}")
    
    @contextmanager
    def chaining_context_manager(name: str):
        """演示异常链的上下文管理器"""
        print(f"  设置 {name}")
        try:
            yield name
        except Exception as e:
            print(f"  {name} 中发生异常: {e}")
            # 重新抛出时添加上下文
            raise RuntimeError(f"{name} 操作失败") from e
        finally:
            print(f"  清理 {name}")
    
    def test_chaining_context_manager():
        """测试异常链上下文管理器"""
        print("\n测试异常链上下文管理器：")
        
        try:
            with chaining_context_manager("外层操作"):
                with chaining_context_manager("内层操作"):
                    print("    执行核心逻辑")
                    raise ValueError("核心逻辑错误")
        except Exception as e:
            print(f"\n✗ 最终异常: {type(e).__name__}: {e}")
            
            # 分析异常链
            print("\n异常链:")
            current = e
            level = 0
            while current:
                indent = "  " * level
                print(f"{indent}[{level}] {type(current).__name__}: {current}")
                current = current.__cause__ or current.__context__
                level += 1
    
    test_context_manager_exceptions()
    test_chaining_context_manager()


def demonstrate_practical_exception_chaining():
    """演示实际项目中的异常链应用"""
    print_section("4. 实际项目中的异常链应用")
    
    print("实际应用场景：")
    print("- 微服务架构中的错误传播")
    print("- 数据处理管道的错误跟踪")
    print("- API网关的错误聚合")
    print("- 批处理任务的错误报告")
    
    # 微服务异常链示例
    class MicroserviceError(Exception):
        """微服务异常基类"""
        def __init__(self, service: str, operation: str, message: str, 
                     error_code: str = None, context: Dict[str, Any] = None):
            self.service = service
            self.operation = operation
            self.message = message
            self.error_code = error_code or "SERVICE_ERROR"
            self.context = context or {}
            self.timestamp = datetime.now()
            
            full_message = f"[{self.service}:{self.operation}] {self.message}"
            super().__init__(full_message)
        
        def to_dict(self) -> Dict[str, Any]:
            """转换为字典格式"""
            return {
                'service': self.service,
                'operation': self.operation,
                'message': self.message,
                'error_code': self.error_code,
                'context': self.context,
                'timestamp': self.timestamp.isoformat()
            }
    
    class DatabaseService:
        """数据库服务"""
        
        @staticmethod
        def get_user(user_id: str) -> Dict[str, Any]:
            """获取用户信息"""
            try:
                # 模拟数据库连接错误
                if user_id == "error_user":
                    raise ConnectionError("数据库连接超时")
                
                # 模拟用户不存在
                if user_id == "not_found":
                    raise KeyError(f"用户 {user_id} 不存在")
                
                return {"id": user_id, "name": f"User-{user_id}", "email": f"{user_id}@example.com"}
                
            except ConnectionError as e:
                raise MicroserviceError(
                    service="database",
                    operation="get_user",
                    message="数据库连接失败",
                    error_code="DB_CONNECTION_ERROR",
                    context={"user_id": user_id, "timeout": 30}
                ) from e
            
            except KeyError as e:
                raise MicroserviceError(
                    service="database",
                    operation="get_user",
                    message="用户不存在",
                    error_code="USER_NOT_FOUND",
                    context={"user_id": user_id}
                ) from e
    
    class AuthService:
        """认证服务"""
        
        @staticmethod
        def validate_token(token: str) -> str:
            """验证令牌"""
            try:
                # 模拟令牌验证
                if token == "invalid_token":
                    raise ValueError("令牌格式无效")
                
                if token == "expired_token":
                    raise TimeoutError("令牌已过期")
                
                # 从令牌中提取用户ID
                user_id = token.replace("token_", "")
                return user_id
                
            except ValueError as e:
                raise MicroserviceError(
                    service="auth",
                    operation="validate_token",
                    message="令牌验证失败",
                    error_code="INVALID_TOKEN",
                    context={"token_length": len(token)}
                ) from e
            
            except TimeoutError as e:
                raise MicroserviceError(
                    service="auth",
                    operation="validate_token",
                    message="令牌已过期",
                    error_code="TOKEN_EXPIRED",
                    context={"token_prefix": token[:10]}
                ) from e
    
    class UserService:
        """用户服务"""
        
        def __init__(self):
            self.db_service = DatabaseService()
            self.auth_service = AuthService()
        
        def get_user_profile(self, token: str) -> Dict[str, Any]:
            """获取用户档案"""
            try:
                # 验证令牌
                user_id = self.auth_service.validate_token(token)
                
                # 获取用户信息
                user_data = self.db_service.get_user(user_id)
                
                return {
                    "profile": user_data,
                    "authenticated": True,
                    "timestamp": datetime.now().isoformat()
                }
                
            except MicroserviceError as e:
                # 重新包装异常，添加用户服务的上下文
                raise MicroserviceError(
                    service="user",
                    operation="get_user_profile",
                    message="获取用户档案失败",
                    error_code="PROFILE_ACCESS_ERROR",
                    context={"original_service": e.service, "original_operation": e.operation}
                ) from e
    
    class APIGateway:
        """API网关"""
        
        def __init__(self):
            self.user_service = UserService()
        
        def handle_request(self, endpoint: str, token: str) -> Dict[str, Any]:
            """处理API请求"""
            try:
                if endpoint == "/api/user/profile":
                    return self.user_service.get_user_profile(token)
                else:
                    raise ValueError(f"未知的端点: {endpoint}")
                    
            except MicroserviceError as e:
                # API网关层的异常处理
                raise MicroserviceError(
                    service="api_gateway",
                    operation="handle_request",
                    message="API请求处理失败",
                    error_code="API_REQUEST_ERROR",
                    context={
                        "endpoint": endpoint,
                        "original_error_code": e.error_code,
                        "service_chain": self._extract_service_chain(e)
                    }
                ) from e
            
            except Exception as e:
                raise MicroserviceError(
                    service="api_gateway",
                    operation="handle_request",
                    message="未知错误",
                    error_code="UNKNOWN_ERROR",
                    context={"endpoint": endpoint, "error_type": type(e).__name__}
                ) from e
        
        def _extract_service_chain(self, exception: MicroserviceError) -> List[str]:
            """提取服务调用链"""
            chain = []
            current = exception
            
            while current and isinstance(current, MicroserviceError):
                chain.append(f"{current.service}:{current.operation}")
                current = current.__cause__
            
            return chain
    
    def test_microservice_exception_chain():
        """测试微服务异常链"""
        print("\n测试微服务异常链：")
        
        gateway = APIGateway()
        
        # 测试场景
        test_cases = [
            {"name": "正常请求", "token": "token_user123"},
            {"name": "无效令牌", "token": "invalid_token"},
            {"name": "过期令牌", "token": "expired_token"},
            {"name": "用户不存在", "token": "token_not_found"},
            {"name": "数据库错误", "token": "token_error_user"}
        ]
        
        for case in test_cases:
            print(f"\n--- {case['name']} ---")
            
            try:
                result = gateway.handle_request("/api/user/profile", case['token'])
                print(f"✓ 成功: {json.dumps(result, ensure_ascii=False, indent=2)}")
                
            except MicroserviceError as e:
                print(f"✗ 异常: {e}")
                print(f"  服务: {e.service}")
                print(f"  操作: {e.operation}")
                print(f"  错误代码: {e.error_code}")
                print(f"  上下文: {json.dumps(e.context, ensure_ascii=False)}")
                
                # 分析完整的异常链
                print("\n  完整异常链:")
                current = e
                level = 0
                while current:
                    indent = "    " * level
                    if isinstance(current, MicroserviceError):
                        print(f"{indent}[{level}] {current.service}:{current.operation} - {current.error_code}")
                        print(f"{indent}    消息: {current.message}")
                        print(f"{indent}    上下文: {current.context}")
                    else:
                        print(f"{indent}[{level}] {type(current).__name__}: {current}")
                    
                    current = current.__cause__
                    level += 1
    
    test_microservice_exception_chain()


def demonstrate_exception_chain_utilities():
    """演示异常链实用工具"""
    print_section("5. 异常链实用工具")
    
    print("异常链实用工具的作用：")
    print("- 异常链的格式化输出")
    print("- 异常信息的结构化提取")
    print("- 异常链的过滤和搜索")
    print("- 异常恢复策略的实现")
    
    class ExceptionChainUtils:
        """异常链实用工具类"""
        
        @staticmethod
        def format_exception_chain(exception: Exception, include_traceback: bool = False) -> str:
            """格式化异常链为可读字符串"""
            lines = []
            current = exception
            level = 0
            
            while current:
                indent = "  " * level
                
                # 异常基本信息
                lines.append(f"{indent}[{level}] {type(current).__name__}: {current}")
                
                # 添加异常属性
                if hasattr(current, 'error_code'):
                    lines.append(f"{indent}    错误代码: {current.error_code}")
                
                if hasattr(current, 'context') and current.context:
                    lines.append(f"{indent}    上下文: {current.context}")
                
                if hasattr(current, 'timestamp'):
                    lines.append(f"{indent}    时间: {current.timestamp}")
                
                # 添加回溯信息
                if include_traceback and hasattr(current, '__traceback__') and current.__traceback__:
                    lines.append(f"{indent}    回溯:")
                    tb_lines = traceback.format_tb(current.__traceback__)
                    for tb_line in tb_lines[-2:]:  # 只显示最后2层
                        lines.append(f"{indent}      {tb_line.strip()}")
                
                # 移动到下一个异常
                if current.__cause__:
                    lines.append(f"{indent}    ↓ 原因:")
                    current = current.__cause__
                elif current.__context__:
                    lines.append(f"{indent}    ↓ 上下文:")
                    current = current.__context__
                else:
                    break
                
                level += 1
            
            return "\n".join(lines)
        
        @staticmethod
        def extract_error_codes(exception: Exception) -> List[str]:
            """提取异常链中的所有错误代码"""
            codes = []
            current = exception
            
            while current:
                if hasattr(current, 'error_code'):
                    codes.append(current.error_code)
                
                current = current.__cause__ or current.__context__
            
            return codes
        
        @staticmethod
        def find_exception_by_type(exception: Exception, target_type: Type[Exception]) -> Optional[Exception]:
            """在异常链中查找特定类型的异常"""
            current = exception
            
            while current:
                if isinstance(current, target_type):
                    return current
                
                current = current.__cause__ or current.__context__
            
            return None
        
        @staticmethod
        def is_recoverable_error(exception: Exception) -> bool:
            """判断异常是否可恢复"""
            # 定义可恢复的异常类型
            recoverable_types = (
                ConnectionError,
                TimeoutError,
                OSError
            )
            
            # 定义不可恢复的错误代码
            non_recoverable_codes = {
                'INVALID_TOKEN',
                'USER_NOT_FOUND',
                'PERMISSION_DENIED',
                'CONFIG_ERROR'
            }
            
            current = exception
            
            while current:
                # 检查异常类型
                if isinstance(current, recoverable_types):
                    return True
                
                # 检查错误代码
                if hasattr(current, 'error_code'):
                    if current.error_code in non_recoverable_codes:
                        return False
                
                current = current.__cause__ or current.__context__
            
            return False
        
        @staticmethod
        def get_user_friendly_message(exception: Exception) -> str:
            """获取用户友好的错误消息"""
            # 错误代码到用户消息的映射
            user_messages = {
                'DB_CONNECTION_ERROR': '系统暂时不可用，请稍后重试',
                'USER_NOT_FOUND': '用户信息不存在',
                'INVALID_TOKEN': '登录已过期，请重新登录',
                'TOKEN_EXPIRED': '登录已过期，请重新登录',
                'PERMISSION_DENIED': '您没有权限执行此操作',
                'RATE_LIMIT_EXCEEDED': '请求过于频繁，请稍后重试'
            }
            
            # 查找最合适的用户消息
            current = exception
            
            while current:
                if hasattr(current, 'error_code') and current.error_code in user_messages:
                    return user_messages[current.error_code]
                
                if hasattr(current, 'user_message'):
                    return current.user_message
                
                current = current.__cause__ or current.__context__
            
            return "操作失败，请稍后重试"
    
    def test_exception_chain_utils():
        """测试异常链实用工具"""
        print("\n测试异常链实用工具：")
        
        # 创建复杂的异常链用于测试
        class CustomError(Exception):
            def __init__(self, message: str, error_code: str, user_message: str = None):
                self.error_code = error_code
                self.user_message = user_message
                self.timestamp = datetime.now()
                super().__init__(message)
        
        try:
            try:
                try:
                    raise ConnectionError("网络连接失败")
                except ConnectionError as e:
                    raise CustomError(
                        "数据库连接失败",
                        "DB_CONNECTION_ERROR",
                        "系统暂时不可用，请稍后重试"
                    ) from e
            except CustomError as e:
                raise CustomError(
                    "用户服务不可用",
                    "SERVICE_UNAVAILABLE",
                    "服务暂时不可用"
                ) from e
        except CustomError as e:
            print("✓ 创建测试异常链")
            
            # 测试格式化输出
            print("\n1. 格式化异常链:")
            formatted = ExceptionChainUtils.format_exception_chain(e)
            print(formatted)
            
            # 测试错误代码提取
            print("\n2. 提取错误代码:")
            error_codes = ExceptionChainUtils.extract_error_codes(e)
            print(f"错误代码: {error_codes}")
            
            # 测试异常类型查找
            print("\n3. 查找特定异常类型:")
            connection_error = ExceptionChainUtils.find_exception_by_type(e, ConnectionError)
            if connection_error:
                print(f"找到ConnectionError: {connection_error}")
            else:
                print("未找到ConnectionError")
            
            # 测试可恢复性判断
            print("\n4. 判断异常可恢复性:")
            is_recoverable = ExceptionChainUtils.is_recoverable_error(e)
            print(f"异常可恢复: {is_recoverable}")
            
            # 测试用户友好消息
            print("\n5. 获取用户友好消息:")
            user_message = ExceptionChainUtils.get_user_friendly_message(e)
            print(f"用户消息: {user_message}")
    
    test_exception_chain_utils()


def main():
    """主函数"""
    print("Python异常处理 - 异常链和上下文管理")
    print("=" * 60)
    
    try:
        # 演示各种异常链的用法
        demonstrate_basic_exception_chaining()
        demonstrate_exception_chain_analysis()
        demonstrate_context_managers_and_chaining()
        demonstrate_practical_exception_chaining()
        demonstrate_exception_chain_utilities()
        
        print_section("学习总结")
        print("""
        异常链和上下文要点：
        
        1. 异常链类型：
           - 隐式链接 (__context__)：异常处理中的新异常
           - 显式链接 (__cause__)：使用 raise...from 语句
           - 抑制链接：使用 raise...from None
        
        2. 异常链分析：
           - 提供完整的错误上下文
           - 便于问题的根因分析
           - 支持智能错误恢复
        
        3. 上下文管理器：
           - __enter__ 和 __exit__ 中的异常处理
           - 异常的传播和抑制
           - 资源清理的保证
        
        4. 实际应用：
           - 微服务架构中的错误传播
           - 分层架构的异常处理
           - 错误信息的结构化管理
        
        5. 实用工具：
           - 异常链的格式化和分析
           - 错误恢复策略的实现
           - 用户友好消息的生成
        
        下一步学习：
        - 08_logging_exceptions.py: 异常日志记录
        - 09_best_practices.py: 异常处理最佳实践
        """)
        
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"程序执行过程中发生错误: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()