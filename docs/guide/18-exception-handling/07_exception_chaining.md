# 07. 异常链和上下文

## 学习目标

- 掌握异常链接的概念和使用方法
- 理解异常上下文的保持和传播机制
- 学会使用raise from语句创建异常链
- 掌握异常抑制和上下文管理
- 学会在复杂系统中追踪异常的完整调用链

## 异常链接基础

### 1. 基本异常链接

```python
def demonstrate_basic_exception_chaining():
    """演示基本的异常链接"""
    
    class DatabaseError(Exception):
        """数据库错误"""
        pass
    
    class UserServiceError(Exception):
        """用户服务错误"""
        pass
    
    class APIError(Exception):
        """API错误"""
        pass
    
    def connect_to_database():
        """连接数据库"""
        # 模拟数据库连接失败
        raise ConnectionError("无法连接到数据库服务器")
    
    def get_user_from_database(user_id):
        """从数据库获取用户"""
        try:
            connect_to_database()
            return {'id': user_id, 'name': 'Alice'}
        except ConnectionError as e:
            # 使用 raise from 创建异常链
            raise DatabaseError(f"获取用户 {user_id} 失败") from e
    
    def get_user_profile(user_id):
        """获取用户档案"""
        try:
            user = get_user_from_database(user_id)
            return {'user': user, 'profile': 'complete'}
        except DatabaseError as e:
            # 继续链接异常
            raise UserServiceError(f"用户服务错误: 无法获取用户 {user_id} 的档案") from e
    
    def api_get_user(user_id):
        """API接口获取用户"""
        try:
            profile = get_user_profile(user_id)
            return {'status': 'success', 'data': profile}
        except UserServiceError as e:
            # 最终的API层异常
            raise APIError(f"API调用失败: 用户 {user_id} 不可用") from e
    
    def demonstrate_exception_chain():
        """演示异常链"""
        try:
            result = api_get_user(123)
            print(f"成功: {result}")
        except APIError as e:
            print("=== 异常链演示 ===")
            print(f"最终异常: {type(e).__name__}: {e}")
            
            # 遍历异常链
            current_exception = e
            level = 0
            
            while current_exception is not None:
                print(f"  级别 {level}: {type(current_exception).__name__}: {current_exception}")
                
                # 获取下一个异常（原因）
                current_exception = current_exception.__cause__
                level += 1
            
            print("\n=== 异常上下文信息 ===")
            print(f"直接原因 (__cause__): {e.__cause__}")
            print(f"上下文 (__context__): {e.__context__}")
            print(f"抑制上下文 (__suppress_context__): {e.__suppress_context__}")
    
    demonstrate_exception_chain()

demonstrate_basic_exception_chaining()
```

### 2. 异常上下文的自动保持

```python
def demonstrate_automatic_exception_context():
    """演示异常上下文的自动保持"""
    
    class ProcessingError(Exception):
        pass
    
    class ValidationError(Exception):
        pass
    
    def process_data(data):
        """处理数据"""
        if not data:
            raise ValueError("数据不能为空")
        
        if not isinstance(data, dict):
            raise TypeError("数据必须是字典类型")
        
        return data.get('result', 'processed')
    
    def validate_and_process(data):
        """验证并处理数据"""
        try:
            # 第一步：处理数据
            result = process_data(data)
            
            # 第二步：验证结果
            if result == 'invalid':
                raise ValidationError("处理结果无效")
            
            return result
            
        except (ValueError, TypeError) as e:
            # 不使用 from，异常上下文会自动保持
            raise ProcessingError(f"数据处理失败: {e}")
    
    def demonstrate_context_preservation():
        """演示上下文保持"""
        test_cases = [
            (None, "空数据"),
            ("invalid_type", "错误类型"),
            ({'result': 'invalid'}, "无效结果"),
            ({'result': 'valid'}, "正常数据")
        ]
        
        for data, description in test_cases:
            print(f"\n测试: {description}")
            print("=" * 40)
            
            try:
                result = validate_and_process(data)
                print(f"处理成功: {result}")
            except ProcessingError as e:
                print(f"处理错误: {e}")
                
                # 检查异常上下文
                if e.__context__:
                    print(f"原始异常: {type(e.__context__).__name__}: {e.__context__}")
                    print(f"上下文类型: {type(e.__context__)}")
                
                # 检查是否有显式的异常链
                if e.__cause__:
                    print(f"显式原因: {e.__cause__}")
                else:
                    print("没有显式的异常链（使用了隐式上下文）")
    
    demonstrate_context_preservation()

demonstrate_automatic_exception_context()
```

## 异常抑制和上下文管理

### 1. 抑制异常上下文

```python
def demonstrate_exception_suppression():
    """演示异常上下文的抑制"""
    
    class CustomError(Exception):
        pass
    
    class CleanupError(Exception):
        pass
    
    def risky_operation():
        """有风险的操作"""
        raise ValueError("操作失败")
    
    def cleanup_operation():
        """清理操作"""
        raise CleanupError("清理失败")
    
    def demonstrate_with_context():
        """演示带上下文的异常"""
        print("=== 带上下文的异常 ===")
        try:
            try:
                risky_operation()
            except ValueError as e:
                print(f"捕获到原始异常: {e}")
                # 在处理异常时又发生了新异常
                cleanup_operation()
        except CleanupError as e:
            print(f"最终异常: {e}")
            print(f"异常上下文: {e.__context__}")
            print(f"上下文类型: {type(e.__context__).__name__ if e.__context__ else None}")
    
    def demonstrate_suppressed_context():
        """演示抑制上下文的异常"""
        print("\n=== 抑制上下文的异常 ===")
        try:
            try:
                risky_operation()
            except ValueError as e:
                print(f"捕获到原始异常: {e}")
                # 使用 raise from None 抑制上下文
                raise CustomError("自定义错误，不显示原始异常") from None
        except CustomError as e:
            print(f"最终异常: {e}")
            print(f"异常上下文: {e.__context__}")
            print(f"异常原因: {e.__cause__}")
            print(f"抑制上下文: {e.__suppress_context__}")
    
    def demonstrate_explicit_chaining():
        """演示显式异常链接"""
        print("\n=== 显式异常链接 ===")
        try:
            try:
                risky_operation()
            except ValueError as e:
                print(f"捕获到原始异常: {e}")
                # 使用 raise from 显式链接
                raise CustomError("自定义错误，保持异常链") from e
        except CustomError as e:
            print(f"最终异常: {e}")
            print(f"异常上下文: {e.__context__}")
            print(f"异常原因: {e.__cause__}")
            print(f"抑制上下文: {e.__suppress_context__}")
    
    def demonstrate_context_manager_exceptions():
        """演示上下文管理器中的异常"""
        print("\n=== 上下文管理器异常 ===")
        
        class ResourceManager:
            def __init__(self, name):
                self.name = name
            
            def __enter__(self):
                print(f"获取资源: {self.name}")
                return self
            
            def __exit__(self, exc_type, exc_val, exc_tb):
                print(f"释放资源: {self.name}")
                if exc_type:
                    print(f"处理异常: {exc_type.__name__}: {exc_val}")
                
                # 在清理时发生异常
                if self.name == "problematic_resource":
                    raise CleanupError(f"释放资源 {self.name} 时发生错误")
                
                return False  # 不抑制异常
        
        # 正常的上下文管理器异常
        try:
            with ResourceManager("normal_resource"):
                raise ValueError("业务逻辑错误")
        except ValueError as e:
            print(f"捕获业务异常: {e}")
        
        # 上下文管理器清理时的异常
        try:
            with ResourceManager("problematic_resource"):
                raise ValueError("业务逻辑错误")
        except CleanupError as e:
            print(f"\n捕获清理异常: {e}")
            print(f"原始异常上下文: {e.__context__}")
            if e.__context__:
                print(f"原始异常类型: {type(e.__context__).__name__}")
    
    # 运行所有演示
    demonstrate_with_context()
    demonstrate_suppressed_context()
    demonstrate_explicit_chaining()
    demonstrate_context_manager_exceptions()

demonstrate_exception_suppression()
```

### 2. 复杂的异常链管理

```python
def demonstrate_complex_exception_chaining():
    """演示复杂的异常链管理"""
    
    import traceback
    import sys
    
    # 定义异常层次
    class ApplicationError(Exception):
        """应用程序异常基类"""
        def __init__(self, message, error_code=None, context=None):
            super().__init__(message)
            self.error_code = error_code
            self.context = context or {}
    
    class NetworkError(ApplicationError):
        """网络错误"""
        pass
    
    class DatabaseError(ApplicationError):
        """数据库错误"""
        pass
    
    class BusinessLogicError(ApplicationError):
        """业务逻辑错误"""
        pass
    
    class ValidationError(ApplicationError):
        """验证错误"""
        pass
    
    # 异常链工具类
    class ExceptionChainAnalyzer:
        """异常链分析器"""
        
        @staticmethod
        def get_exception_chain(exception):
            """获取完整的异常链"""
            chain = []
            current = exception
            
            while current is not None:
                chain.append(current)
                # 优先使用 __cause__（显式链接），然后使用 __context__（隐式上下文）
                current = current.__cause__ or current.__context__
            
            return chain
        
        @staticmethod
        def print_exception_chain(exception, show_traceback=False):
            """打印异常链"""
            chain = ExceptionChainAnalyzer.get_exception_chain(exception)
            
            print(f"异常链长度: {len(chain)}")
            print("=" * 60)
            
            for i, exc in enumerate(chain):
                print(f"级别 {i}: {type(exc).__name__}")
                print(f"  消息: {exc}")
                
                if hasattr(exc, 'error_code') and exc.error_code:
                    print(f"  错误代码: {exc.error_code}")
                
                if hasattr(exc, 'context') and exc.context:
                    print(f"  上下文: {exc.context}")
                
                # 显示链接关系
                if i < len(chain) - 1:
                    next_exc = chain[i + 1]
                    if exc.__cause__ is next_exc:
                        print(f"  ↓ (显式链接 'from')")
                    elif exc.__context__ is next_exc:
                        print(f"  ↓ (隐式上下文)")
                
                if show_traceback and i == 0:  # 只显示最顶层异常的traceback
                    print("  Traceback:")
                    tb_lines = traceback.format_exception(type(exc), exc, exc.__traceback__)
                    for line in tb_lines[-3:]:  # 只显示最后几行
                        print(f"    {line.strip()}")
                
                print()
        
        @staticmethod
        def find_root_cause(exception):
            """找到根本原因"""
            chain = ExceptionChainAnalyzer.get_exception_chain(exception)
            return chain[-1] if chain else None
        
        @staticmethod
        def has_exception_type(exception, exception_type):
            """检查异常链中是否包含特定类型的异常"""
            chain = ExceptionChainAnalyzer.get_exception_chain(exception)
            return any(isinstance(exc, exception_type) for exc in chain)
    
    # 模拟服务层
    class NetworkService:
        """网络服务"""
        
        def __init__(self, failure_rate=0.3):
            self.failure_rate = failure_rate
        
        def make_request(self, url):
            """发起网络请求"""
            import random
            
            if random.random() < self.failure_rate:
                if random.random() < 0.5:
                    raise ConnectionError("连接超时")
                else:
                    raise OSError("网络不可达")
            
            return {'status': 'success', 'data': f'Response from {url}'}
    
    class DatabaseService:
        """数据库服务"""
        
        def __init__(self, failure_rate=0.2):
            self.failure_rate = failure_rate
        
        def execute_query(self, query):
            """执行数据库查询"""
            import random
            
            if random.random() < self.failure_rate:
                if random.random() < 0.5:
                    raise ConnectionError("数据库连接失败")
                else:
                    raise PermissionError("权限不足")
            
            return {'rows': [{'id': 1, 'name': 'test'}]}
    
    class UserService:
        """用户服务"""
        
        def __init__(self):
            self.network_service = NetworkService(failure_rate=0.8)  # 高失败率用于演示
            self.database_service = DatabaseService(failure_rate=0.6)
        
        def validate_user_data(self, user_data):
            """验证用户数据"""
            if not user_data:
                raise ValidationError(
                    "用户数据不能为空",
                    error_code="EMPTY_USER_DATA",
                    context={'input': user_data}
                )
            
            if not isinstance(user_data, dict):
                raise ValidationError(
                    "用户数据必须是字典格式",
                    error_code="INVALID_DATA_FORMAT",
                    context={'input_type': type(user_data).__name__}
                )
            
            required_fields = ['name', 'email']
            missing_fields = [field for field in required_fields if field not in user_data]
            
            if missing_fields:
                raise ValidationError(
                    f"缺少必需字段: {missing_fields}",
                    error_code="MISSING_REQUIRED_FIELDS",
                    context={'missing_fields': missing_fields, 'provided_fields': list(user_data.keys())}
                )
        
        def check_user_exists(self, email):
            """检查用户是否存在"""
            try:
                query = f"SELECT * FROM users WHERE email = '{email}'"
                result = self.database_service.execute_query(query)
                return len(result['rows']) > 0
            except (ConnectionError, PermissionError) as e:
                raise DatabaseError(
                    f"检查用户存在性失败: {e}",
                    error_code="USER_CHECK_FAILED",
                    context={'email': email, 'query': query}
                ) from e
        
        def verify_email_domain(self, email):
            """验证邮箱域名"""
            try:
                domain = email.split('@')[1]
                url = f"https://api.emailverify.com/check/{domain}"
                response = self.network_service.make_request(url)
                return response['data'] == 'valid'
            except (ConnectionError, OSError) as e:
                raise NetworkError(
                    f"邮箱域名验证失败: {e}",
                    error_code="EMAIL_VERIFICATION_FAILED",
                    context={'email': email, 'domain': email.split('@')[1] if '@' in email else None}
                ) from e
        
        def create_user(self, user_data):
            """创建用户"""
            try:
                # 第一步：验证数据
                self.validate_user_data(user_data)
                
                # 第二步：检查用户是否已存在
                if self.check_user_exists(user_data['email']):
                    raise BusinessLogicError(
                        f"用户已存在: {user_data['email']}",
                        error_code="USER_ALREADY_EXISTS",
                        context={'email': user_data['email']}
                    )
                
                # 第三步：验证邮箱域名
                if not self.verify_email_domain(user_data['email']):
                    raise BusinessLogicError(
                        f"邮箱域名无效: {user_data['email']}",
                        error_code="INVALID_EMAIL_DOMAIN",
                        context={'email': user_data['email']}
                    )
                
                # 第四步：创建用户
                query = f"INSERT INTO users (name, email) VALUES ('{user_data['name']}', '{user_data['email']}')"
                result = self.database_service.execute_query(query)
                
                return {'success': True, 'user_id': 123}
                
            except (ValidationError, DatabaseError, NetworkError, BusinessLogicError) as e:
                # 重新抛出，保持异常链
                raise
            except Exception as e:
                # 处理未预期的异常
                raise ApplicationError(
                    f"创建用户时发生未预期的错误: {e}",
                    error_code="UNEXPECTED_ERROR",
                    context={'user_data': user_data}
                ) from e
    
    def demonstrate_exception_chain_analysis():
        """演示异常链分析"""
        user_service = UserService()
        
        test_cases = [
            (None, "空数据"),
            ("invalid_format", "错误格式"),
            ({'name': 'Alice'}, "缺少邮箱"),
            ({'name': 'Bob', 'email': 'bob@example.com'}, "完整数据（可能因网络或数据库失败）")
        ]
        
        for user_data, description in test_cases:
            print(f"\n{'='*80}")
            print(f"测试用例: {description}")
            print(f"输入数据: {user_data}")
            print(f"{'='*80}")
            
            try:
                result = user_service.create_user(user_data)
                print(f"创建成功: {result}")
            except ApplicationError as e:
                print(f"\n捕获异常: {type(e).__name__}: {e}")
                
                # 分析异常链
                print("\n--- 异常链分析 ---")
                ExceptionChainAnalyzer.print_exception_chain(e)
                
                # 查找根本原因
                root_cause = ExceptionChainAnalyzer.find_root_cause(e)
                print(f"根本原因: {type(root_cause).__name__}: {root_cause}")
                
                # 检查特定异常类型
                has_network_error = ExceptionChainAnalyzer.has_exception_type(e, NetworkError)
                has_database_error = ExceptionChainAnalyzer.has_exception_type(e, DatabaseError)
                has_validation_error = ExceptionChainAnalyzer.has_exception_type(e, ValidationError)
                
                print(f"\n异常类型检查:")
                print(f"  包含网络错误: {has_network_error}")
                print(f"  包含数据库错误: {has_database_error}")
                print(f"  包含验证错误: {has_validation_error}")
                
                # 根据异常类型提供处理建议
                print(f"\n处理建议:")
                if has_validation_error:
                    print("  - 检查输入数据的格式和完整性")
                if has_database_error:
                    print("  - 检查数据库连接和权限配置")
                if has_network_error:
                    print("  - 检查网络连接和外部服务状态")
                if isinstance(e, BusinessLogicError):
                    print("  - 检查业务逻辑和数据一致性")
    
    demonstrate_exception_chain_analysis()

demonstrate_complex_exception_chaining()
```

## 异常链的实际应用

### 1. 微服务架构中的异常传播

```python
def demonstrate_microservice_exception_propagation():
    """演示微服务架构中的异常传播"""
    
    import json
    from typing import Dict, Any, Optional
    
    # 微服务异常基类
    class MicroserviceError(Exception):
        """微服务异常基类"""
        
        def __init__(self, message, service_name=None, error_code=None, 
                     request_id=None, context=None):
            super().__init__(message)
            self.service_name = service_name
            self.error_code = error_code
            self.request_id = request_id
            self.context = context or {}
            self.timestamp = '2024-01-01 12:00:00'
        
        def to_dict(self):
            """转换为字典格式"""
            return {
                'error_type': self.__class__.__name__,
                'message': str(self),
                'service_name': self.service_name,
                'error_code': self.error_code,
                'request_id': self.request_id,
                'context': self.context,
                'timestamp': self.timestamp
            }
        
        def to_json(self):
            """转换为JSON格式"""
            return json.dumps(self.to_dict(), indent=2)
    
    class ServiceUnavailableError(MicroserviceError):
        """服务不可用错误"""
        pass
    
    class ServiceTimeoutError(MicroserviceError):
        """服务超时错误"""
        pass
    
    class ServiceAuthenticationError(MicroserviceError):
        """服务认证错误"""
        pass
    
    class DataValidationError(MicroserviceError):
        """数据验证错误"""
        pass
    
    class BusinessRuleError(MicroserviceError):
        """业务规则错误"""
        pass
    
    # 微服务客户端
    class MicroserviceClient:
        """微服务客户端基类"""
        
        def __init__(self, service_name, base_url, timeout=30):
            self.service_name = service_name
            self.base_url = base_url
            self.timeout = timeout
        
        def make_request(self, endpoint, data=None, request_id=None):
            """发起请求"""
            import random
            
            # 模拟各种失败情况
            failure_type = random.choice(['success', 'timeout', 'unavailable', 'auth_error', 'server_error'])
            
            if failure_type == 'timeout':
                raise TimeoutError(f"请求超时: {self.base_url}{endpoint}")
            elif failure_type == 'unavailable':
                raise ConnectionError(f"服务不可用: {self.service_name}")
            elif failure_type == 'auth_error':
                raise PermissionError(f"认证失败: {self.service_name}")
            elif failure_type == 'server_error':
                raise RuntimeError(f"服务内部错误: {self.service_name}")
            
            # 成功情况
            return {'status': 'success', 'data': f'Response from {self.service_name}'}
        
        def handle_request_exception(self, e, endpoint, request_id=None):
            """处理请求异常"""
            context = {
                'endpoint': endpoint,
                'service_url': f"{self.base_url}{endpoint}",
                'timeout': self.timeout
            }
            
            if isinstance(e, TimeoutError):
                raise ServiceTimeoutError(
                    f"调用 {self.service_name} 服务超时",
                    service_name=self.service_name,
                    error_code='SERVICE_TIMEOUT',
                    request_id=request_id,
                    context=context
                ) from e
            elif isinstance(e, ConnectionError):
                raise ServiceUnavailableError(
                    f"{self.service_name} 服务不可用",
                    service_name=self.service_name,
                    error_code='SERVICE_UNAVAILABLE',
                    request_id=request_id,
                    context=context
                ) from e
            elif isinstance(e, PermissionError):
                raise ServiceAuthenticationError(
                    f"{self.service_name} 服务认证失败",
                    service_name=self.service_name,
                    error_code='SERVICE_AUTH_FAILED',
                    request_id=request_id,
                    context=context
                ) from e
            else:
                raise MicroserviceError(
                    f"调用 {self.service_name} 服务时发生未知错误: {e}",
                    service_name=self.service_name,
                    error_code='SERVICE_UNKNOWN_ERROR',
                    request_id=request_id,
                    context=context
                ) from e
    
    # 具体的微服务客户端
    class UserServiceClient(MicroserviceClient):
        """用户服务客户端"""
        
        def __init__(self):
            super().__init__('user-service', 'http://user-service:8080', timeout=10)
        
        def get_user(self, user_id, request_id=None):
            """获取用户信息"""
            try:
                response = self.make_request(f'/users/{user_id}', request_id=request_id)
                return response['data']
            except Exception as e:
                self.handle_request_exception(e, f'/users/{user_id}', request_id)
        
        def validate_user(self, user_data, request_id=None):
            """验证用户数据"""
            try:
                response = self.make_request('/users/validate', data=user_data, request_id=request_id)
                return response['data']
            except Exception as e:
                self.handle_request_exception(e, '/users/validate', request_id)
    
    class OrderServiceClient(MicroserviceClient):
        """订单服务客户端"""
        
        def __init__(self):
            super().__init__('order-service', 'http://order-service:8080', timeout=15)
        
        def create_order(self, order_data, request_id=None):
            """创建订单"""
            try:
                response = self.make_request('/orders', data=order_data, request_id=request_id)
                return response['data']
            except Exception as e:
                self.handle_request_exception(e, '/orders', request_id)
        
        def get_order(self, order_id, request_id=None):
            """获取订单信息"""
            try:
                response = self.make_request(f'/orders/{order_id}', request_id=request_id)
                return response['data']
            except Exception as e:
                self.handle_request_exception(e, f'/orders/{order_id}', request_id)
    
    class PaymentServiceClient(MicroserviceClient):
        """支付服务客户端"""
        
        def __init__(self):
            super().__init__('payment-service', 'http://payment-service:8080', timeout=20)
        
        def process_payment(self, payment_data, request_id=None):
            """处理支付"""
            try:
                response = self.make_request('/payments', data=payment_data, request_id=request_id)
                return response['data']
            except Exception as e:
                self.handle_request_exception(e, '/payments', request_id)
    
    # 业务编排服务
    class OrderOrchestrationService:
        """订单编排服务"""
        
        def __init__(self):
            self.user_service = UserServiceClient()
            self.order_service = OrderServiceClient()
            self.payment_service = PaymentServiceClient()
        
        def validate_order_data(self, order_data, request_id=None):
            """验证订单数据"""
            required_fields = ['user_id', 'items', 'total_amount']
            missing_fields = [field for field in required_fields if field not in order_data]
            
            if missing_fields:
                raise DataValidationError(
                    f"订单数据缺少必需字段: {missing_fields}",
                    service_name='order-orchestration',
                    error_code='MISSING_ORDER_FIELDS',
                    request_id=request_id,
                    context={
                        'missing_fields': missing_fields,
                        'provided_fields': list(order_data.keys())
                    }
                )
            
            if order_data['total_amount'] <= 0:
                raise DataValidationError(
                    f"订单金额必须大于0，当前金额: {order_data['total_amount']}",
                    service_name='order-orchestration',
                    error_code='INVALID_ORDER_AMOUNT',
                    request_id=request_id,
                    context={'total_amount': order_data['total_amount']}
                )
        
        def check_business_rules(self, user_data, order_data, request_id=None):
            """检查业务规则"""
            # 模拟业务规则检查
            if order_data['total_amount'] > 10000 and user_data.get('vip_level', 0) < 3:
                raise BusinessRuleError(
                    "非VIP用户不能创建超过10000元的订单",
                    service_name='order-orchestration',
                    error_code='ORDER_AMOUNT_LIMIT_EXCEEDED',
                    request_id=request_id,
                    context={
                        'user_vip_level': user_data.get('vip_level', 0),
                        'order_amount': order_data['total_amount'],
                        'limit': 10000
                    }
                )
        
        def create_order_with_payment(self, order_data, payment_data, request_id=None):
            """创建订单并处理支付"""
            try:
                # 第一步：验证订单数据
                self.validate_order_data(order_data, request_id)
                
                # 第二步：获取用户信息
                try:
                    user_data = self.user_service.get_user(order_data['user_id'], request_id)
                except MicroserviceError as e:
                    raise MicroserviceError(
                        f"获取用户信息失败，无法创建订单",
                        service_name='order-orchestration',
                        error_code='USER_INFO_REQUIRED',
                        request_id=request_id,
                        context={'user_id': order_data['user_id']}
                    ) from e
                
                # 第三步：检查业务规则
                self.check_business_rules(user_data, order_data, request_id)
                
                # 第四步：创建订单
                try:
                    order_result = self.order_service.create_order(order_data, request_id)
                except MicroserviceError as e:
                    raise MicroserviceError(
                        f"创建订单失败",
                        service_name='order-orchestration',
                        error_code='ORDER_CREATION_FAILED',
                        request_id=request_id,
                        context={'order_data': order_data}
                    ) from e
                
                # 第五步：处理支付
                try:
                    payment_result = self.payment_service.process_payment({
                        **payment_data,
                        'order_id': order_result['order_id'],
                        'amount': order_data['total_amount']
                    }, request_id)
                except MicroserviceError as e:
                    # 支付失败，需要回滚订单（这里简化处理）
                    raise MicroserviceError(
                        f"支付处理失败，订单已创建但未完成支付",
                        service_name='order-orchestration',
                        error_code='PAYMENT_FAILED_ORDER_CREATED',
                        request_id=request_id,
                        context={
                            'order_id': order_result['order_id'],
                            'payment_data': payment_data
                        }
                    ) from e
                
                return {
                    'success': True,
                    'order': order_result,
                    'payment': payment_result
                }
                
            except (DataValidationError, BusinessRuleError, MicroserviceError) as e:
                # 重新抛出业务异常，保持异常链
                raise
            except Exception as e:
                # 处理未预期的异常
                raise MicroserviceError(
                    f"订单创建过程中发生未预期的错误: {e}",
                    service_name='order-orchestration',
                    error_code='UNEXPECTED_ERROR',
                    request_id=request_id,
                    context={'order_data': order_data, 'payment_data': payment_data}
                ) from e
    
    # 异常链追踪器
    class ExceptionTracker:
        """异常链追踪器"""
        
        @staticmethod
        def trace_microservice_exception(exception, request_id=None):
            """追踪微服务异常链"""
            print(f"\n{'='*80}")
            print(f"异常追踪报告 (Request ID: {request_id or 'N/A'})")
            print(f"{'='*80}")
            
            chain = []
            current = exception
            
            while current is not None:
                chain.append(current)
                current = current.__cause__ or current.__context__
            
            print(f"异常传播路径 ({len(chain)} 层):")
            print()
            
            for i, exc in enumerate(chain):
                indent = "  " * i
                print(f"{indent}[级别 {i}] {type(exc).__name__}")
                print(f"{indent}  消息: {exc}")
                
                if isinstance(exc, MicroserviceError):
                    print(f"{indent}  服务: {exc.service_name or 'N/A'}")
                    print(f"{indent}  错误代码: {exc.error_code or 'N/A'}")
                    print(f"{indent}  请求ID: {exc.request_id or 'N/A'}")
                    if exc.context:
                        print(f"{indent}  上下文: {exc.context}")
                
                if i < len(chain) - 1:
                    print(f"{indent}  ↓")
                
                print()
            
            # 分析异常模式
            service_errors = [exc for exc in chain if isinstance(exc, MicroserviceError)]
            if service_errors:
                services_involved = list(set(exc.service_name for exc in service_errors if exc.service_name))
                print(f"涉及的服务: {', '.join(services_involved)}")
                
                error_codes = list(set(exc.error_code for exc in service_errors if exc.error_code))
                print(f"错误代码: {', '.join(error_codes)}")
            
            # 根本原因分析
            root_cause = chain[-1]
            print(f"\n根本原因: {type(root_cause).__name__}: {root_cause}")
            
            # 恢复建议
            print(f"\n恢复建议:")
            if any(isinstance(exc, ServiceTimeoutError) for exc in chain):
                print("  - 检查网络延迟和服务响应时间")
                print("  - 考虑增加超时时间或实现重试机制")
            
            if any(isinstance(exc, ServiceUnavailableError) for exc in chain):
                print("  - 检查服务健康状态和负载均衡配置")
                print("  - 实现熔断器模式防止级联失败")
            
            if any(isinstance(exc, ServiceAuthenticationError) for exc in chain):
                print("  - 检查服务间认证配置")
                print("  - 验证API密钥和证书有效性")
            
            if any(isinstance(exc, DataValidationError) for exc in chain):
                print("  - 检查输入数据格式和完整性")
                print("  - 加强客户端数据验证")
            
            if any(isinstance(exc, BusinessRuleError) for exc in chain):
                print("  - 检查业务规则配置")
                print("  - 验证用户权限和业务逻辑")
    
    def demonstrate_microservice_scenarios():
        """演示微服务场景"""
        orchestration_service = OrderOrchestrationService()
        
        test_cases = [
            (
                {'user_id': 123, 'items': ['item1', 'item2'], 'total_amount': 500},
                {'payment_method': 'credit_card', 'card_number': '****1234'},
                "正常订单"
            ),
            (
                {'user_id': 456, 'items': ['expensive_item'], 'total_amount': 15000},
                {'payment_method': 'credit_card', 'card_number': '****5678'},
                "超额订单（业务规则限制）"
            ),
            (
                {'user_id': 789, 'items': []},
                {'payment_method': 'debit_card'},
                "无效订单数据"
            ),
            (
                {'user_id': 999, 'items': ['item1'], 'total_amount': 100},
                {'payment_method': 'paypal', 'account': 'user@example.com'},
                "服务调用可能失败的订单"
            )
        ]
        
        for order_data, payment_data, description in test_cases:
            request_id = f"req_{hash(str(order_data)) % 10000:04d}"
            
            print(f"\n{'='*100}")
            print(f"测试场景: {description}")
            print(f"请求ID: {request_id}")
            print(f"订单数据: {order_data}")
            print(f"支付数据: {payment_data}")
            print(f"{'='*100}")
            
            try:
                result = orchestration_service.create_order_with_payment(
                    order_data, payment_data, request_id
                )
                print(f"\n✅ 订单创建成功!")
                print(f"结果: {result}")
                
            except MicroserviceError as e:
                print(f"\n❌ 订单创建失败: {type(e).__name__}: {e}")
                
                # 追踪异常链
                ExceptionTracker.trace_microservice_exception(e, request_id)
    
    demonstrate_microservice_scenarios()

demonstrate_microservice_exception_propagation()
```

## 学习要点总结

### 异常链接的核心概念
1. **显式链接**: 使用`raise ... from ...`语句创建明确的异常链
2. **隐式上下文**: Python自动保持异常发生时的上下文
3. **上下文抑制**: 使用`raise ... from None`抑制异常上下文
4. **异常属性**: `__cause__`、`__context__`、`__suppress_context__`

### 异常链的最佳实践
1. **保持信息完整**: 在转换异常时保持原始错误信息
2. **合理的抽象层次**: 在不同层次使用适当的异常类型
3. **上下文信息**: 添加有助于调试的上下文信息
4. **链式分析**: 提供工具分析完整的异常链

### 实际应用场景
1. **分层架构**: 在不同架构层之间传播异常
2. **微服务通信**: 跨服务边界的异常传播
3. **错误恢复**: 基于异常链进行智能错误恢复
4. **监控告警**: 根据异常链模式进行系统监控

### 异常链管理工具
1. **链式遍历**: 遍历完整的异常链
2. **根因分析**: 找到问题的根本原因
3. **类型检查**: 检查链中是否包含特定异常类型
4. **可视化展示**: 清晰展示异常传播路径

## 下一步学习

掌握了异常链和上下文后，接下来将学习：
- [08. 异常日志记录](./08_logging_exceptions.md) - 异常的记录和监控
- [09. 异常处理最佳实践](./09_best_practices.md) - 综合应用和最佳实践

通过掌握异常链接和上下文管理，你可以构建更加健壮的错误处理系统，在复杂的应用架构中有效地追踪和诊断问题。