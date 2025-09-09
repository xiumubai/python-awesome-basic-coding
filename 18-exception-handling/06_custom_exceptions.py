#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自定义异常类的创建和使用

本文件详细演示如何在Python中创建和使用自定义异常类，包括异常类的设计原则、
继承关系、异常层次结构和实际应用场景。

学习目标：
1. 理解自定义异常的必要性和优势
2. 掌握异常类的创建方法
3. 学会设计异常类层次结构
4. 了解异常类的最佳实践
5. 掌握在实际项目中使用自定义异常
"""

import sys
import traceback
from typing import Any, List, Dict, Optional, Union
from datetime import datetime
import json
import re


def print_section(title: str) -> None:
    """打印章节标题"""
    print("\n" + "=" * 60)
    print(f"{title}")
    print("=" * 60)


def demonstrate_basic_custom_exception():
    """演示基本的自定义异常"""
    print_section("1. 基本自定义异常")
    
    print("自定义异常的优势：")
    print("- 提供更具体的错误信息")
    print("- 便于异常的分类和处理")
    print("- 增强代码的可读性和可维护性")
    print("- 支持异常的层次化管理")
    
    # 最简单的自定义异常
    class CustomError(Exception):
        """自定义异常基类"""
        pass
    
    # 带有默认消息的自定义异常
    class ValidationError(Exception):
        """数据验证异常"""
        def __init__(self, message="数据验证失败"):
            self.message = message
            super().__init__(self.message)
    
    # 带有额外属性的自定义异常
    class BusinessLogicError(Exception):
        """业务逻辑异常"""
        def __init__(self, message: str, error_code: str = None, details: Dict[str, Any] = None):
            self.message = message
            self.error_code = error_code or "BUSINESS_ERROR"
            self.details = details or {}
            self.timestamp = datetime.now()
            
            # 构建完整的错误消息
            full_message = f"[{self.error_code}] {self.message}"
            if self.details:
                full_message += f" | 详情: {self.details}"
            
            super().__init__(full_message)
        
        def to_dict(self) -> Dict[str, Any]:
            """将异常信息转换为字典"""
            return {
                'error_code': self.error_code,
                'message': self.message,
                'details': self.details,
                'timestamp': self.timestamp.isoformat()
            }
        
        def __str__(self) -> str:
            return f"{self.error_code}: {self.message}"
    
    def test_basic_exceptions():
        """测试基本自定义异常"""
        print("\n测试基本自定义异常：")
        
        # 测试最简单的自定义异常
        try:
            raise CustomError("这是一个自定义错误")
        except CustomError as e:
            print(f"✓ 捕获CustomError: {e}")
            print(f"  异常类型: {type(e).__name__}")
            print(f"  异常消息: {str(e)}")
        
        print("-" * 40)
        
        # 测试带默认消息的异常
        try:
            raise ValidationError()  # 使用默认消息
        except ValidationError as e:
            print(f"✓ 捕获ValidationError (默认消息): {e}")
        
        try:
            raise ValidationError("用户名格式不正确")  # 自定义消息
        except ValidationError as e:
            print(f"✓ 捕获ValidationError (自定义消息): {e}")
        
        print("-" * 40)
        
        # 测试带额外属性的异常
        try:
            raise BusinessLogicError(
                message="库存不足",
                error_code="INSUFFICIENT_STOCK",
                details={
                    'product_id': 'P001',
                    'requested_quantity': 10,
                    'available_quantity': 3
                }
            )
        except BusinessLogicError as e:
            print(f"✓ 捕获BusinessLogicError: {e}")
            print(f"  错误代码: {e.error_code}")
            print(f"  错误消息: {e.message}")
            print(f"  详细信息: {e.details}")
            print(f"  时间戳: {e.timestamp}")
            print(f"  字典格式: {json.dumps(e.to_dict(), ensure_ascii=False, indent=2)}")
    
    test_basic_exceptions()


def demonstrate_exception_hierarchy():
    """演示异常类层次结构"""
    print_section("2. 异常类层次结构")
    
    print("设计异常层次结构的原则：")
    print("- 从通用到具体的层次结构")
    print("- 便于异常的分类捕获")
    print("- 支持异常的继承和扩展")
    print("- 遵循单一职责原则")
    
    # 设计一个完整的异常层次结构
    class ApplicationError(Exception):
        """应用程序异常基类"""
        def __init__(self, message: str, error_code: str = None):
            self.message = message
            self.error_code = error_code or "APP_ERROR"
            self.timestamp = datetime.now()
            super().__init__(f"[{self.error_code}] {self.message}")
    
    # 数据相关异常
    class DataError(ApplicationError):
        """数据相关异常基类"""
        def __init__(self, message: str, error_code: str = None):
            super().__init__(message, error_code or "DATA_ERROR")
    
    class DataValidationError(DataError):
        """数据验证异常"""
        def __init__(self, field: str, value: Any, message: str = None):
            self.field = field
            self.value = value
            default_message = f"字段 '{field}' 的值 '{value}' 验证失败"
            super().__init__(message or default_message, "DATA_VALIDATION_ERROR")
    
    class DataNotFoundError(DataError):
        """数据未找到异常"""
        def __init__(self, resource: str, identifier: Any):
            self.resource = resource
            self.identifier = identifier
            message = f"未找到 {resource}: {identifier}"
            super().__init__(message, "DATA_NOT_FOUND")
    
    class DataConflictError(DataError):
        """数据冲突异常"""
        def __init__(self, resource: str, conflict_reason: str):
            self.resource = resource
            self.conflict_reason = conflict_reason
            message = f"{resource} 数据冲突: {conflict_reason}"
            super().__init__(message, "DATA_CONFLICT")
    
    # 业务逻辑相关异常
    class BusinessError(ApplicationError):
        """业务逻辑异常基类"""
        def __init__(self, message: str, error_code: str = None):
            super().__init__(message, error_code or "BUSINESS_ERROR")
    
    class InsufficientPermissionError(BusinessError):
        """权限不足异常"""
        def __init__(self, user: str, action: str, resource: str = None):
            self.user = user
            self.action = action
            self.resource = resource
            
            if resource:
                message = f"用户 '{user}' 没有权限对 '{resource}' 执行 '{action}' 操作"
            else:
                message = f"用户 '{user}' 没有权限执行 '{action}' 操作"
            
            super().__init__(message, "INSUFFICIENT_PERMISSION")
    
    class BusinessRuleViolationError(BusinessError):
        """业务规则违反异常"""
        def __init__(self, rule: str, details: Dict[str, Any] = None):
            self.rule = rule
            self.details = details or {}
            
            message = f"违反业务规则: {rule}"
            if self.details:
                message += f" | 详情: {self.details}"
            
            super().__init__(message, "BUSINESS_RULE_VIOLATION")
    
    # 系统相关异常
    class SystemError(ApplicationError):
        """系统异常基类"""
        def __init__(self, message: str, error_code: str = None):
            super().__init__(message, error_code or "SYSTEM_ERROR")
    
    class ConfigurationError(SystemError):
        """配置错误异常"""
        def __init__(self, config_key: str, issue: str):
            self.config_key = config_key
            self.issue = issue
            message = f"配置项 '{config_key}' 错误: {issue}"
            super().__init__(message, "CONFIGURATION_ERROR")
    
    class ExternalServiceError(SystemError):
        """外部服务异常"""
        def __init__(self, service: str, operation: str, status_code: int = None):
            self.service = service
            self.operation = operation
            self.status_code = status_code
            
            message = f"外部服务 '{service}' 的 '{operation}' 操作失败"
            if status_code:
                message += f" (状态码: {status_code})"
            
            super().__init__(message, "EXTERNAL_SERVICE_ERROR")
    
    def demonstrate_hierarchy_usage():
        """演示异常层次结构的使用"""
        print("\n演示异常层次结构的使用：")
        
        # 创建各种异常实例
        exceptions_to_test = [
            DataValidationError("email", "invalid-email", "邮箱格式不正确"),
            DataNotFoundError("用户", "user_123"),
            DataConflictError("用户名", "用户名已存在"),
            InsufficientPermissionError("john_doe", "删除", "管理员账户"),
            BusinessRuleViolationError("单日转账限额", {"amount": 100000, "limit": 50000}),
            ConfigurationError("database.host", "配置项为空"),
            ExternalServiceError("支付网关", "创建订单", 503)
        ]
        
        for i, exception in enumerate(exceptions_to_test, 1):
            print(f"\n--- 异常 {i}: {type(exception).__name__} ---")
            
            try:
                raise exception
            except ApplicationError as e:
                print(f"✓ 捕获应用程序异常: {e}")
                print(f"  异常类型: {type(e).__name__}")
                print(f"  错误代码: {e.error_code}")
                print(f"  错误消息: {e.message}")
                print(f"  时间戳: {e.timestamp}")
                
                # 显示异常的继承关系
                mro = type(e).__mro__
                inheritance_chain = " -> ".join([cls.__name__ for cls in mro[:-1]])
                print(f"  继承链: {inheritance_chain}")
    
    def demonstrate_selective_catching():
        """演示选择性异常捕获"""
        print("\n演示选择性异常捕获：")
        
        def process_user_operation(operation_type: str):
            """模拟用户操作处理"""
            print(f"\n处理用户操作: {operation_type}")
            
            if operation_type == "validate_email":
                raise DataValidationError("email", "test@", "邮箱格式不完整")
            elif operation_type == "find_user":
                raise DataNotFoundError("用户", "user_999")
            elif operation_type == "delete_admin":
                raise InsufficientPermissionError("regular_user", "删除", "管理员账户")
            elif operation_type == "large_transfer":
                raise BusinessRuleViolationError("转账限额", {"amount": 100000, "limit": 50000})
            elif operation_type == "payment":
                raise ExternalServiceError("支付服务", "处理支付", 500)
            else:
                print("操作成功完成")
        
        operations = [
            "validate_email",
            "find_user", 
            "delete_admin",
            "large_transfer",
            "payment",
            "normal_operation"
        ]
        
        for operation in operations:
            try:
                process_user_operation(operation)
                
            except DataError as e:
                print(f"✗ 数据错误: {e.error_code} - {e.message}")
                print("  处理方式: 返回用户友好的错误信息")
                
            except BusinessError as e:
                print(f"✗ 业务错误: {e.error_code} - {e.message}")
                print("  处理方式: 记录日志并提示用户")
                
            except SystemError as e:
                print(f"✗ 系统错误: {e.error_code} - {e.message}")
                print("  处理方式: 记录错误日志，通知运维团队")
                
            except ApplicationError as e:
                print(f"✗ 应用程序错误: {e.error_code} - {e.message}")
                print("  处理方式: 通用错误处理")
    
    demonstrate_hierarchy_usage()
    demonstrate_selective_catching()


def demonstrate_advanced_custom_exceptions():
    """演示高级自定义异常特性"""
    print_section("3. 高级自定义异常特性")
    
    print("高级特性包括：")
    print("- 异常的序列化和反序列化")
    print("- 异常的国际化支持")
    print("- 异常的上下文管理")
    print("- 异常的链式调用")
    
    class SerializableError(Exception):
        """可序列化的异常类"""
        def __init__(self, message: str, error_code: str = None, 
                     context: Dict[str, Any] = None, user_message: str = None):
            self.message = message
            self.error_code = error_code or "SERIALIZABLE_ERROR"
            self.context = context or {}
            self.user_message = user_message or message
            self.timestamp = datetime.now()
            self.trace_id = self._generate_trace_id()
            
            super().__init__(self.message)
        
        def _generate_trace_id(self) -> str:
            """生成追踪ID"""
            import uuid
            return str(uuid.uuid4())[:8]
        
        def to_dict(self) -> Dict[str, Any]:
            """序列化为字典"""
            return {
                'error_code': self.error_code,
                'message': self.message,
                'user_message': self.user_message,
                'context': self.context,
                'timestamp': self.timestamp.isoformat(),
                'trace_id': self.trace_id,
                'exception_type': self.__class__.__name__
            }
        
        def to_json(self) -> str:
            """序列化为JSON字符串"""
            return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)
        
        @classmethod
        def from_dict(cls, data: Dict[str, Any]) -> 'SerializableError':
            """从字典反序列化"""
            instance = cls(
                message=data['message'],
                error_code=data['error_code'],
                context=data.get('context', {}),
                user_message=data.get('user_message')
            )
            
            # 恢复时间戳和追踪ID
            if 'timestamp' in data:
                instance.timestamp = datetime.fromisoformat(data['timestamp'])
            if 'trace_id' in data:
                instance.trace_id = data['trace_id']
            
            return instance
        
        @classmethod
        def from_json(cls, json_str: str) -> 'SerializableError':
            """从JSON字符串反序列化"""
            data = json.loads(json_str)
            return cls.from_dict(data)
        
        def __str__(self) -> str:
            return f"[{self.trace_id}] {self.error_code}: {self.message}"
    
    class I18nError(SerializableError):
        """支持国际化的异常类"""
        
        # 错误消息模板
        MESSAGE_TEMPLATES = {
            'zh': {
                'VALIDATION_FAILED': '字段 {field} 验证失败: {reason}',
                'RESOURCE_NOT_FOUND': '未找到资源 {resource}: {identifier}',
                'PERMISSION_DENIED': '用户 {user} 没有权限执行 {action} 操作',
                'RATE_LIMIT_EXCEEDED': '请求频率超限，请 {wait_time} 秒后重试'
            },
            'en': {
                'VALIDATION_FAILED': 'Validation failed for field {field}: {reason}',
                'RESOURCE_NOT_FOUND': 'Resource {resource} not found: {identifier}',
                'PERMISSION_DENIED': 'User {user} has no permission to perform {action}',
                'RATE_LIMIT_EXCEEDED': 'Rate limit exceeded, please retry after {wait_time} seconds'
            }
        }
        
        def __init__(self, error_code: str, template_params: Dict[str, Any] = None, 
                     language: str = 'zh', context: Dict[str, Any] = None):
            self.language = language
            self.template_params = template_params or {}
            
            # 生成本地化消息
            message = self._get_localized_message(error_code, self.template_params, language)
            user_message = self._get_localized_message(error_code, self.template_params, language)
            
            super().__init__(
                message=message,
                error_code=error_code,
                context=context,
                user_message=user_message
            )
        
        def _get_localized_message(self, error_code: str, params: Dict[str, Any], language: str) -> str:
            """获取本地化消息"""
            templates = self.MESSAGE_TEMPLATES.get(language, self.MESSAGE_TEMPLATES['zh'])
            template = templates.get(error_code, f"Unknown error: {error_code}")
            
            try:
                return template.format(**params)
            except KeyError as e:
                return f"Message template error for {error_code}: missing parameter {e}"
        
        def get_message(self, language: str = None) -> str:
            """获取指定语言的消息"""
            lang = language or self.language
            return self._get_localized_message(self.error_code, self.template_params, lang)
    
    class ChainableError(SerializableError):
        """支持链式调用的异常类"""
        def __init__(self, message: str, error_code: str = None, 
                     context: Dict[str, Any] = None, cause: Exception = None):
            super().__init__(message, error_code, context)
            self.cause = cause
            
            # 如果有原因异常，设置异常链
            if cause:
                self.__cause__ = cause
        
        def add_context(self, key: str, value: Any) -> 'ChainableError':
            """添加上下文信息"""
            self.context[key] = value
            return self
        
        def with_user_message(self, user_message: str) -> 'ChainableError':
            """设置用户友好消息"""
            self.user_message = user_message
            return self
        
        def get_full_chain(self) -> List[Dict[str, Any]]:
            """获取完整的异常链信息"""
            chain = []
            current = self
            
            while current:
                if isinstance(current, ChainableError):
                    chain.append(current.to_dict())
                    current = current.cause
                elif isinstance(current, Exception):
                    chain.append({
                        'exception_type': type(current).__name__,
                        'message': str(current),
                        'is_custom': False
                    })
                    current = getattr(current, '__cause__', None)
                else:
                    break
            
            return chain
    
    def test_advanced_exceptions():
        """测试高级异常特性"""
        print("\n测试高级异常特性：")
        
        # 测试可序列化异常
        print("\n1. 测试可序列化异常：")
        try:
            raise SerializableError(
                message="数据库连接失败",
                error_code="DB_CONNECTION_ERROR",
                context={
                    'host': 'localhost',
                    'port': 5432,
                    'database': 'myapp',
                    'retry_count': 3
                },
                user_message="系统暂时不可用，请稍后重试"
            )
        except SerializableError as e:
            print(f"✓ 原始异常: {e}")
            
            # 序列化
            json_str = e.to_json()
            print(f"✓ 序列化为JSON: {json_str}")
            
            # 反序列化
            restored_exception = SerializableError.from_json(json_str)
            print(f"✓ 反序列化异常: {restored_exception}")
            print(f"  追踪ID匹配: {e.trace_id == restored_exception.trace_id}")
        
        print("-" * 50)
        
        # 测试国际化异常
        print("\n2. 测试国际化异常：")
        
        i18n_exceptions = [
            I18nError('VALIDATION_FAILED', {'field': 'email', 'reason': '格式不正确'}, 'zh'),
            I18nError('VALIDATION_FAILED', {'field': 'email', 'reason': 'invalid format'}, 'en'),
            I18nError('RESOURCE_NOT_FOUND', {'resource': '用户', 'identifier': 'user_123'}, 'zh'),
            I18nError('RESOURCE_NOT_FOUND', {'resource': 'User', 'identifier': 'user_123'}, 'en'),
            I18nError('RATE_LIMIT_EXCEEDED', {'wait_time': 60}, 'zh'),
            I18nError('RATE_LIMIT_EXCEEDED', {'wait_time': 60}, 'en')
        ]
        
        for exc in i18n_exceptions:
            print(f"✓ {exc.language.upper()}: {exc}")
            # 获取另一种语言的消息
            other_lang = 'en' if exc.language == 'zh' else 'zh'
            other_message = exc.get_message(other_lang)
            print(f"  {other_lang.upper()}: {other_message}")
            print()
        
        print("-" * 50)
        
        # 测试链式异常
        print("\n3. 测试链式异常：")
        
        try:
            # 模拟嵌套异常场景
            try:
                # 最底层异常
                raise ValueError("无效的配置值")
            except ValueError as e:
                # 中间层异常
                config_error = ChainableError(
                    message="配置加载失败",
                    error_code="CONFIG_LOAD_ERROR",
                    context={'config_file': 'app.conf'},
                    cause=e
                ).add_context('section', 'database').with_user_message("配置文件有误")
                
                try:
                    raise config_error
                except ChainableError as ce:
                    # 最上层异常
                    app_error = ChainableError(
                        message="应用程序启动失败",
                        error_code="APP_STARTUP_ERROR",
                        context={'startup_phase': 'initialization'},
                        cause=ce
                    ).add_context('app_version', '1.0.0').with_user_message("应用启动失败，请联系管理员")
                    
                    raise app_error
        
        except ChainableError as e:
            print(f"✓ 顶层异常: {e}")
            print(f"  用户消息: {e.user_message}")
            print(f"  上下文: {e.context}")
            
            # 显示完整异常链
            print("\n  完整异常链:")
            chain = e.get_full_chain()
            for i, link in enumerate(chain):
                indent = "  " * (i + 1)
                if link.get('is_custom', True):
                    print(f"{indent}[{link['error_code']}] {link['message']}")
                    if link.get('context'):
                        print(f"{indent}  上下文: {link['context']}")
                else:
                    print(f"{indent}{link['exception_type']}: {link['message']}")
    
    test_advanced_exceptions()


def demonstrate_real_world_examples():
    """演示实际项目中的自定义异常应用"""
    print_section("4. 实际项目应用示例")
    
    print("实际项目中的异常设计考虑：")
    print("- 异常的粒度和层次")
    print("- 异常信息的安全性")
    print("- 异常的可观测性")
    print("- 异常的恢复策略")
    
    # 电商系统异常设计示例
    class ECommerceError(Exception):
        """电商系统异常基类"""
        def __init__(self, message: str, error_code: str, 
                     user_message: str = None, sensitive_data: Dict[str, Any] = None):
            self.message = message
            self.error_code = error_code
            self.user_message = user_message or "系统繁忙，请稍后重试"
            self.sensitive_data = sensitive_data or {}  # 敏感数据，不会被序列化
            self.timestamp = datetime.now()
            
            super().__init__(f"[{error_code}] {message}")
        
        def get_safe_dict(self) -> Dict[str, Any]:
            """获取安全的字典表示（不包含敏感数据）"""
            return {
                'error_code': self.error_code,
                'user_message': self.user_message,
                'timestamp': self.timestamp.isoformat()
            }
        
        def get_full_dict(self) -> Dict[str, Any]:
            """获取完整的字典表示（包含敏感数据，仅用于内部日志）"""
            result = self.get_safe_dict()
            result.update({
                'message': self.message,
                'sensitive_data': self.sensitive_data
            })
            return result
    
    # 用户相关异常
    class UserNotFoundError(ECommerceError):
        def __init__(self, user_id: str):
            super().__init__(
                message=f"用户不存在: {user_id}",
                error_code="USER_NOT_FOUND",
                user_message="用户信息不存在",
                sensitive_data={'user_id': user_id}
            )
    
    class InvalidCredentialsError(ECommerceError):
        def __init__(self, username: str, attempt_count: int = 1):
            super().__init__(
                message=f"用户 {username} 登录凭据无效，尝试次数: {attempt_count}",
                error_code="INVALID_CREDENTIALS",
                user_message="用户名或密码错误",
                sensitive_data={'username': username, 'attempt_count': attempt_count}
            )
    
    # 商品相关异常
    class ProductNotFoundError(ECommerceError):
        def __init__(self, product_id: str):
            super().__init__(
                message=f"商品不存在: {product_id}",
                error_code="PRODUCT_NOT_FOUND",
                user_message="商品不存在或已下架",
                sensitive_data={'product_id': product_id}
            )
    
    class InsufficientStockError(ECommerceError):
        def __init__(self, product_id: str, requested: int, available: int):
            super().__init__(
                message=f"商品 {product_id} 库存不足，请求: {requested}, 可用: {available}",
                error_code="INSUFFICIENT_STOCK",
                user_message=f"商品库存不足，仅剩 {available} 件",
                sensitive_data={
                    'product_id': product_id,
                    'requested_quantity': requested,
                    'available_quantity': available
                }
            )
    
    # 订单相关异常
    class OrderProcessingError(ECommerceError):
        def __init__(self, order_id: str, stage: str, reason: str):
            super().__init__(
                message=f"订单 {order_id} 在 {stage} 阶段处理失败: {reason}",
                error_code="ORDER_PROCESSING_ERROR",
                user_message="订单处理失败，请稍后重试",
                sensitive_data={
                    'order_id': order_id,
                    'processing_stage': stage,
                    'failure_reason': reason
                }
            )
    
    # 支付相关异常
    class PaymentError(ECommerceError):
        def __init__(self, transaction_id: str, payment_method: str, 
                     error_details: Dict[str, Any]):
            super().__init__(
                message=f"支付失败，交易ID: {transaction_id}, 支付方式: {payment_method}",
                error_code="PAYMENT_FAILED",
                user_message="支付失败，请检查支付信息或更换支付方式",
                sensitive_data={
                    'transaction_id': transaction_id,
                    'payment_method': payment_method,
                    'error_details': error_details
                }
            )
    
    class ECommerceService:
        """电商服务类，演示异常的使用"""
        
        def __init__(self):
            # 模拟数据
            self.users = {
                'user_001': {'username': 'alice', 'password': 'secret123'},
                'user_002': {'username': 'bob', 'password': 'password456'}
            }
            
            self.products = {
                'prod_001': {'name': 'iPhone 15', 'price': 7999, 'stock': 5},
                'prod_002': {'name': 'MacBook Pro', 'price': 15999, 'stock': 0},
                'prod_003': {'name': 'AirPods', 'price': 1299, 'stock': 10}
            }
            
            self.orders = {}
            self.login_attempts = {}
        
        def authenticate_user(self, username: str, password: str) -> str:
            """用户认证"""
            print(f"\n尝试认证用户: {username}")
            
            # 查找用户
            user_id = None
            for uid, user_data in self.users.items():
                if user_data['username'] == username:
                    user_id = uid
                    break
            
            if not user_id:
                raise UserNotFoundError(username)
            
            # 检查密码
            if self.users[user_id]['password'] != password:
                # 记录登录尝试
                attempt_count = self.login_attempts.get(username, 0) + 1
                self.login_attempts[username] = attempt_count
                
                raise InvalidCredentialsError(username, attempt_count)
            
            # 清除登录尝试记录
            self.login_attempts.pop(username, None)
            
            print(f"✓ 用户认证成功: {username}")
            return user_id
        
        def get_product(self, product_id: str) -> Dict[str, Any]:
            """获取商品信息"""
            print(f"\n获取商品信息: {product_id}")
            
            if product_id not in self.products:
                raise ProductNotFoundError(product_id)
            
            product = self.products[product_id].copy()
            print(f"✓ 商品信息: {product}")
            return product
        
        def create_order(self, user_id: str, items: List[Dict[str, Any]]) -> str:
            """创建订单"""
            print(f"\n为用户 {user_id} 创建订单，商品: {items}")
            
            # 验证用户存在
            if user_id not in self.users:
                raise UserNotFoundError(user_id)
            
            order_id = f"order_{len(self.orders) + 1:03d}"
            
            try:
                # 验证商品和库存
                order_items = []
                total_amount = 0
                
                for item in items:
                    product_id = item['product_id']
                    quantity = item['quantity']
                    
                    # 检查商品存在
                    if product_id not in self.products:
                        raise ProductNotFoundError(product_id)
                    
                    product = self.products[product_id]
                    
                    # 检查库存
                    if product['stock'] < quantity:
                        raise InsufficientStockError(product_id, quantity, product['stock'])
                    
                    # 计算金额
                    item_total = product['price'] * quantity
                    total_amount += item_total
                    
                    order_items.append({
                        'product_id': product_id,
                        'product_name': product['name'],
                        'price': product['price'],
                        'quantity': quantity,
                        'subtotal': item_total
                    })
                
                # 创建订单
                order = {
                    'order_id': order_id,
                    'user_id': user_id,
                    'items': order_items,
                    'total_amount': total_amount,
                    'status': 'created',
                    'created_at': datetime.now()
                }
                
                self.orders[order_id] = order
                
                # 扣减库存
                for item in items:
                    product_id = item['product_id']
                    quantity = item['quantity']
                    self.products[product_id]['stock'] -= quantity
                
                print(f"✓ 订单创建成功: {order_id}, 总金额: {total_amount}")
                return order_id
                
            except (ProductNotFoundError, InsufficientStockError) as e:
                # 重新抛出商品相关异常
                raise
            except Exception as e:
                # 包装其他异常为订单处理异常
                raise OrderProcessingError(order_id, "创建", str(e)) from e
        
        def process_payment(self, order_id: str, payment_method: str, 
                          payment_details: Dict[str, Any]) -> str:
            """处理支付"""
            print(f"\n处理订单 {order_id} 的支付，支付方式: {payment_method}")
            
            # 检查订单存在
            if order_id not in self.orders:
                raise OrderProcessingError(order_id, "支付", "订单不存在")
            
            order = self.orders[order_id]
            transaction_id = f"txn_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            try:
                # 模拟支付处理
                if payment_method == "credit_card":
                    # 模拟信用卡支付失败
                    if payment_details.get('card_number', '').endswith('0000'):
                        raise PaymentError(transaction_id, payment_method, {
                            'error_code': 'INVALID_CARD',
                            'error_message': '无效的信用卡号码'
                        })
                
                elif payment_method == "alipay":
                    # 模拟支付宝余额不足
                    if order['total_amount'] > 10000:
                        raise PaymentError(transaction_id, payment_method, {
                            'error_code': 'INSUFFICIENT_BALANCE',
                            'error_message': '账户余额不足'
                        })
                
                # 支付成功
                order['status'] = 'paid'
                order['transaction_id'] = transaction_id
                order['paid_at'] = datetime.now()
                
                print(f"✓ 支付成功，交易ID: {transaction_id}")
                return transaction_id
                
            except PaymentError:
                # 支付失败，恢复库存
                for item in order['items']:
                    product_id = item['product_id']
                    quantity = item['quantity']
                    self.products[product_id]['stock'] += quantity
                
                # 更新订单状态
                order['status'] = 'payment_failed'
                
                # 重新抛出支付异常
                raise
    
    def test_ecommerce_service():
        """测试电商服务"""
        print("\n测试电商服务异常处理：")
        
        service = ECommerceService()
        
        # 测试场景
        test_scenarios = [
            # 正常流程
            {
                'name': '正常购买流程',
                'username': 'alice',
                'password': 'secret123',
                'items': [{'product_id': 'prod_001', 'quantity': 1}],
                'payment_method': 'alipay',
                'payment_details': {}
            },
            # 用户不存在
            {
                'name': '用户不存在',
                'username': 'nonexistent',
                'password': 'password',
                'items': [],
                'payment_method': 'alipay',
                'payment_details': {}
            },
            # 密码错误
            {
                'name': '密码错误',
                'username': 'alice',
                'password': 'wrong_password',
                'items': [],
                'payment_method': 'alipay',
                'payment_details': {}
            },
            # 商品不存在
            {
                'name': '商品不存在',
                'username': 'alice',
                'password': 'secret123',
                'items': [{'product_id': 'prod_999', 'quantity': 1}],
                'payment_method': 'alipay',
                'payment_details': {}
            },
            # 库存不足
            {
                'name': '库存不足',
                'username': 'alice',
                'password': 'secret123',
                'items': [{'product_id': 'prod_002', 'quantity': 1}],  # 库存为0
                'payment_method': 'alipay',
                'payment_details': {}
            },
            # 支付失败
            {
                'name': '信用卡支付失败',
                'username': 'alice',
                'password': 'secret123',
                'items': [{'product_id': 'prod_003', 'quantity': 1}],
                'payment_method': 'credit_card',
                'payment_details': {'card_number': '1234567890120000'}  # 以0000结尾
            }
        ]
        
        for i, scenario in enumerate(test_scenarios, 1):
            print(f"\n{'='*20} 场景 {i}: {scenario['name']} {'='*20}")
            
            try:
                # 用户认证
                user_id = service.authenticate_user(scenario['username'], scenario['password'])
                
                # 如果有商品，创建订单
                if scenario['items']:
                    order_id = service.create_order(user_id, scenario['items'])
                    
                    # 处理支付
                    transaction_id = service.process_payment(
                        order_id, 
                        scenario['payment_method'], 
                        scenario['payment_details']
                    )
                    
                    print(f"✓ 场景完成，交易ID: {transaction_id}")
                else:
                    print("✓ 认证成功，无需创建订单")
                    
            except ECommerceError as e:
                print(f"✗ 业务异常: {e.error_code}")
                print(f"  内部消息: {e.message}")
                print(f"  用户消息: {e.user_message}")
                
                # 安全日志（不包含敏感数据）
                safe_info = e.get_safe_dict()
                print(f"  安全日志: {json.dumps(safe_info, ensure_ascii=False)}")
                
                # 内部日志（包含敏感数据，仅用于调试）
                # 在实际项目中，这些信息应该记录到安全的内部日志系统
                full_info = e.get_full_dict()
                print(f"  内部日志: {json.dumps(full_info, ensure_ascii=False)}")
                
            except Exception as e:
                print(f"✗ 系统异常: {type(e).__name__}: {e}")
    
    test_ecommerce_service()


def demonstrate_exception_best_practices():
    """演示自定义异常的最佳实践"""
    print_section("5. 自定义异常最佳实践")
    
    print("自定义异常的最佳实践：")
    print("""
    1. 异常命名规范：
       - 使用描述性的名称
       - 以Error或Exception结尾
       - 遵循驼峰命名法
    
    2. 异常层次设计：
       - 建立清晰的继承关系
       - 从通用到具体的层次结构
       - 便于分类捕获和处理
    
    3. 异常信息设计：
       - 提供清晰的错误描述
       - 包含必要的上下文信息
       - 区分内部消息和用户消息
    
    4. 异常安全性：
       - 避免泄露敏感信息
       - 提供安全的序列化方法
       - 记录详细的内部日志
    
    5. 异常可观测性：
       - 包含追踪ID和时间戳
       - 支持异常链和上下文
       - 便于问题定位和调试
    
    6. 异常处理策略：
       - 在适当的层次抛出异常
       - 提供恢复机制
       - 避免异常被忽略
    """)
    
    # 最佳实践示例总结
    class BestPracticeError(Exception):
        """最佳实践异常示例"""
        
        def __init__(self, message: str, error_code: str = None, 
                     context: Dict[str, Any] = None, user_message: str = None,
                     recoverable: bool = False, retry_after: int = None):
            # 基本信息
            self.message = message
            self.error_code = error_code or "BEST_PRACTICE_ERROR"
            self.context = context or {}
            self.user_message = user_message or "操作失败，请稍后重试"
            
            # 恢复信息
            self.recoverable = recoverable
            self.retry_after = retry_after
            
            # 元数据
            self.timestamp = datetime.now()
            self.trace_id = self._generate_trace_id()
            
            super().__init__(f"[{self.trace_id}] {self.error_code}: {self.message}")
        
        def _generate_trace_id(self) -> str:
            """生成追踪ID"""
            import uuid
            return str(uuid.uuid4())[:8]
        
        def is_recoverable(self) -> bool:
            """判断异常是否可恢复"""
            return self.recoverable
        
        def get_retry_after(self) -> Optional[int]:
            """获取重试间隔（秒）"""
            return self.retry_after
        
        def to_response_dict(self) -> Dict[str, Any]:
            """转换为API响应格式"""
            response = {
                'error': {
                    'code': self.error_code,
                    'message': self.user_message,
                    'timestamp': self.timestamp.isoformat(),
                    'trace_id': self.trace_id
                }
            }
            
            if self.recoverable:
                response['error']['recoverable'] = True
                if self.retry_after:
                    response['error']['retry_after'] = self.retry_after
            
            return response
        
        def to_log_dict(self) -> Dict[str, Any]:
            """转换为日志格式"""
            return {
                'level': 'ERROR',
                'error_code': self.error_code,
                'message': self.message,
                'user_message': self.user_message,
                'context': self.context,
                'recoverable': self.recoverable,
                'retry_after': self.retry_after,
                'timestamp': self.timestamp.isoformat(),
                'trace_id': self.trace_id,
                'exception_type': self.__class__.__name__
            }
    
    # 演示最佳实践
    def demonstrate_best_practices():
        """演示最佳实践"""
        print("\n最佳实践演示：")
        
        # 创建不同类型的异常
        exceptions = [
            BestPracticeError(
                message="数据库连接超时",
                error_code="DB_TIMEOUT",
                context={'host': 'db.example.com', 'timeout': 30},
                user_message="系统繁忙，请稍后重试",
                recoverable=True,
                retry_after=60
            ),
            BestPracticeError(
                message="配置文件格式错误",
                error_code="CONFIG_FORMAT_ERROR",
                context={'file': 'app.conf', 'line': 15},
                user_message="系统配置错误，请联系管理员",
                recoverable=False
            ),
            BestPracticeError(
                message="API调用频率超限",
                error_code="RATE_LIMIT_EXCEEDED",
                context={'endpoint': '/api/users', 'limit': 100, 'window': 3600},
                user_message="请求过于频繁，请稍后重试",
                recoverable=True,
                retry_after=300
            )
        ]
        
        for i, exc in enumerate(exceptions, 1):
            print(f"\n--- 异常 {i} ---")
            print(f"异常: {exc}")
            print(f"可恢复: {exc.is_recoverable()}")
            if exc.get_retry_after():
                print(f"重试间隔: {exc.get_retry_after()} 秒")
            
            print("\nAPI响应格式:")
            response = exc.to_response_dict()
            print(json.dumps(response, ensure_ascii=False, indent=2))
            
            print("\n日志格式:")
            log_data = exc.to_log_dict()
            print(json.dumps(log_data, ensure_ascii=False, indent=2))
    
    demonstrate_best_practices()


def main():
    """主函数"""
    print("Python异常处理 - 自定义异常类的创建和使用")
    print("=" * 60)
    
    try:
        # 演示各种自定义异常的用法
        demonstrate_basic_custom_exception()
        demonstrate_exception_hierarchy()
        demonstrate_advanced_custom_exceptions()
        demonstrate_real_world_examples()
        demonstrate_exception_best_practices()
        
        print_section("学习总结")
        print("""
        自定义异常要点：
        
        1. 异常类设计：
           - 继承自Exception或其子类
           - 提供清晰的构造函数
           - 包含必要的属性和方法
        
        2. 异常层次结构：
           - 建立合理的继承关系
           - 支持分类捕获和处理
           - 便于异常的扩展和维护
        
        3. 高级特性：
           - 异常的序列化和反序列化
           - 国际化支持
           - 异常链和上下文管理
        
        4. 实际应用：
           - 区分内部消息和用户消息
           - 保护敏感信息安全
           - 提供恢复策略
        
        5. 最佳实践：
           - 遵循命名规范
           - 提供丰富的上下文信息
           - 支持可观测性
           - 考虑异常的可恢复性
        
        下一步学习：
        - 07_exception_chaining.py: 异常链详解
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