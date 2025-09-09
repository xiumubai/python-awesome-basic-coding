# 06. 自定义异常

## 学习目标

- 掌握自定义异常类的创建方法
- 理解异常继承层次的设计原则
- 学会为异常添加自定义属性和方法
- 掌握异常类的最佳实践和设计模式
- 学会构建业务相关的异常体系

## 基本自定义异常

### 1. 简单自定义异常

```python
def demonstrate_basic_custom_exceptions():
    """演示基本的自定义异常"""
    
    # 最简单的自定义异常
    class CustomError(Exception):
        """自定义异常基类"""
        pass
    
    class ValidationError(CustomError):
        """验证错误"""
        pass
    
    class BusinessLogicError(CustomError):
        """业务逻辑错误"""
        pass
    
    class DataProcessingError(CustomError):
        """数据处理错误"""
        pass
    
    def validate_user_input(user_input):
        """验证用户输入"""
        if not user_input:
            raise ValidationError("用户输入不能为空")
        
        if not isinstance(user_input, str):
            raise ValidationError(f"用户输入必须是字符串，得到了 {type(user_input).__name__}")
        
        if len(user_input) < 3:
            raise ValidationError(f"用户输入长度至少3个字符，当前长度: {len(user_input)}")
        
        return user_input.strip()
    
    def process_business_logic(data):
        """处理业务逻辑"""
        if data.lower() == 'forbidden':
            raise BusinessLogicError("输入包含禁止的内容")
        
        if data.startswith('admin_'):
            raise BusinessLogicError("普通用户不能使用管理员前缀")
        
        return f"处理结果: {data}"
    
    def process_data(raw_input):
        """数据处理流程"""
        try:
            # 验证输入
            validated_input = validate_user_input(raw_input)
            
            # 业务逻辑处理
            result = process_business_logic(validated_input)
            
            # 模拟数据处理错误
            if validated_input == 'error_trigger':
                raise DataProcessingError("数据处理过程中发生错误")
            
            return result
            
        except ValidationError as e:
            print(f"验证失败: {e}")
            return None
        except BusinessLogicError as e:
            print(f"业务逻辑错误: {e}")
            return None
        except DataProcessingError as e:
            print(f"数据处理错误: {e}")
            return None
        except CustomError as e:
            print(f"自定义错误: {e}")
            return None
    
    # 测试用例
    test_inputs = [
        "valid_input",      # 正常输入
        "",                 # 空输入
        123,                # 类型错误
        "ab",               # 长度不足
        "forbidden",        # 业务逻辑错误
        "admin_user",       # 权限错误
        "error_trigger",    # 数据处理错误
    ]
    
    print("=== 基本自定义异常演示 ===")
    for test_input in test_inputs:
        print(f"\n处理输入: {test_input} ({type(test_input).__name__})")
        result = process_data(test_input)
        print(f"处理结果: {result}")

demonstrate_basic_custom_exceptions()
```

### 2. 带有自定义属性的异常

```python
def demonstrate_custom_exception_attributes():
    """演示带有自定义属性的异常"""
    
    class DetailedError(Exception):
        """详细错误信息的异常基类"""
        
        def __init__(self, message, error_code=None, timestamp=None):
            super().__init__(message)
            self.error_code = error_code
            self.timestamp = timestamp or '2024-01-01 12:00:00'
            self.severity = 'medium'  # 默认严重程度
    
    class ValidationError(DetailedError):
        """验证错误，包含字段信息"""
        
        def __init__(self, message, field_name=None, field_value=None, 
                     validation_rule=None, error_code=None):
            super().__init__(message, error_code)
            self.field_name = field_name
            self.field_value = field_value
            self.validation_rule = validation_rule
            self.severity = 'low'  # 验证错误通常不太严重
    
    class DatabaseError(DetailedError):
        """数据库错误，包含连接和查询信息"""
        
        def __init__(self, message, query=None, connection_info=None, 
                     error_code=None, retry_count=0):
            super().__init__(message, error_code)
            self.query = query
            self.connection_info = connection_info
            self.retry_count = retry_count
            self.severity = 'high'  # 数据库错误通常比较严重
    
    class APIError(DetailedError):
        """API错误，包含HTTP状态码和响应信息"""
        
        def __init__(self, message, status_code=None, response_data=None, 
                     endpoint=None, method=None, error_code=None):
            super().__init__(message, error_code)
            self.status_code = status_code
            self.response_data = response_data
            self.endpoint = endpoint
            self.method = method
            self.severity = 'medium'
        
        def is_client_error(self):
            """判断是否为客户端错误"""
            return self.status_code and 400 <= self.status_code < 500
        
        def is_server_error(self):
            """判断是否为服务器错误"""
            return self.status_code and 500 <= self.status_code < 600
    
    class ConfigurationError(DetailedError):
        """配置错误，包含配置文件和键信息"""
        
        def __init__(self, message, config_file=None, config_key=None, 
                     expected_type=None, actual_value=None, error_code=None):
            super().__init__(message, error_code)
            self.config_file = config_file
            self.config_key = config_key
            self.expected_type = expected_type
            self.actual_value = actual_value
            self.severity = 'high'  # 配置错误通常很严重
    
    # 使用自定义异常的服务类
    class UserService:
        """用户服务类"""
        
        def __init__(self):
            self.users = {}
            self.config = {
                'max_username_length': 20,
                'min_password_length': 8,
                'allowed_domains': ['example.com', 'test.com']
            }
        
        def validate_username(self, username):
            """验证用户名"""
            if not username:
                raise ValidationError(
                    "用户名不能为空",
                    field_name='username',
                    field_value=username,
                    validation_rule='required',
                    error_code='USERNAME_EMPTY'
                )
            
            if not isinstance(username, str):
                raise ValidationError(
                    f"用户名必须是字符串类型，得到了 {type(username).__name__}",
                    field_name='username',
                    field_value=username,
                    validation_rule='type_check',
                    error_code='USERNAME_TYPE_ERROR'
                )
            
            if len(username) > self.config['max_username_length']:
                raise ValidationError(
                    f"用户名长度不能超过 {self.config['max_username_length']} 个字符",
                    field_name='username',
                    field_value=username,
                    validation_rule='max_length',
                    error_code='USERNAME_TOO_LONG'
                )
        
        def validate_email(self, email):
            """验证邮箱"""
            if not email or '@' not in email:
                raise ValidationError(
                    "邮箱格式无效",
                    field_name='email',
                    field_value=email,
                    validation_rule='format_check',
                    error_code='EMAIL_INVALID_FORMAT'
                )
            
            domain = email.split('@')[1]
            if domain not in self.config['allowed_domains']:
                raise ValidationError(
                    f"邮箱域名不在允许列表中: {self.config['allowed_domains']}",
                    field_name='email',
                    field_value=email,
                    validation_rule='domain_whitelist',
                    error_code='EMAIL_DOMAIN_NOT_ALLOWED'
                )
        
        def save_to_database(self, user_data):
            """保存到数据库"""
            # 模拟数据库操作
            if user_data['username'] == 'db_error_user':
                raise DatabaseError(
                    "数据库连接失败",
                    query=f"INSERT INTO users VALUES ({user_data})",
                    connection_info={'host': 'localhost', 'port': 5432, 'db': 'myapp'},
                    error_code='DB_CONNECTION_FAILED',
                    retry_count=3
                )
            
            if user_data['username'] in self.users:
                raise DatabaseError(
                    "用户名已存在",
                    query=f"SELECT * FROM users WHERE username = '{user_data['username']}'",
                    connection_info={'host': 'localhost', 'port': 5432, 'db': 'myapp'},
                    error_code='DB_DUPLICATE_KEY'
                )
        
        def call_external_api(self, user_data):
            """调用外部API"""
            # 模拟API调用
            if user_data['email'] == 'api_error@example.com':
                raise APIError(
                    "外部API调用失败",
                    status_code=500,
                    response_data={'error': 'Internal Server Error'},
                    endpoint='/api/users/validate',
                    method='POST',
                    error_code='API_EXTERNAL_ERROR'
                )
            
            if user_data['username'] == 'rate_limited_user':
                raise APIError(
                    "API调用频率限制",
                    status_code=429,
                    response_data={'error': 'Too Many Requests', 'retry_after': 60},
                    endpoint='/api/users/create',
                    method='POST',
                    error_code='API_RATE_LIMITED'
                )
        
        def create_user(self, username, email, password):
            """创建用户"""
            user_data = {
                'username': username,
                'email': email,
                'password': password
            }
            
            try:
                # 验证输入
                self.validate_username(username)
                self.validate_email(email)
                
                # 调用外部API
                self.call_external_api(user_data)
                
                # 保存到数据库
                self.save_to_database(user_data)
                
                # 成功创建
                self.users[username] = user_data
                return {'status': 'success', 'user_id': len(self.users)}
                
            except (ValidationError, DatabaseError, APIError) as e:
                # 重新抛出，保持异常信息
                raise
    
    def handle_user_creation(service, username, email, password):
        """处理用户创建请求"""
        try:
            result = service.create_user(username, email, password)
            print(f"用户创建成功: {result}")
            return result
            
        except ValidationError as e:
            print(f"验证错误: {e}")
            print(f"  错误代码: {e.error_code}")
            print(f"  字段名: {e.field_name}")
            print(f"  字段值: {e.field_value}")
            print(f"  验证规则: {e.validation_rule}")
            print(f"  严重程度: {e.severity}")
            print(f"  时间戳: {e.timestamp}")
            
        except DatabaseError as e:
            print(f"数据库错误: {e}")
            print(f"  错误代码: {e.error_code}")
            print(f"  查询语句: {e.query}")
            print(f"  连接信息: {e.connection_info}")
            print(f"  重试次数: {e.retry_count}")
            print(f"  严重程度: {e.severity}")
            
        except APIError as e:
            print(f"API错误: {e}")
            print(f"  错误代码: {e.error_code}")
            print(f"  状态码: {e.status_code}")
            print(f"  响应数据: {e.response_data}")
            print(f"  端点: {e.endpoint}")
            print(f"  方法: {e.method}")
            print(f"  是否客户端错误: {e.is_client_error()}")
            print(f"  是否服务器错误: {e.is_server_error()}")
            print(f"  严重程度: {e.severity}")
        
        return None
    
    # 测试用例
    service = UserService()
    
    test_cases = [
        ('alice', 'alice@example.com', 'password123'),          # 正常情况
        ('', 'bob@example.com', 'password123'),                 # 用户名为空
        ('very_long_username_that_exceeds_limit', 'charlie@example.com', 'password123'),  # 用户名过长
        ('david', 'invalid_email', 'password123'),              # 邮箱格式错误
        ('eve', 'eve@forbidden.com', 'password123'),            # 邮箱域名不允许
        ('db_error_user', 'test@example.com', 'password123'),   # 数据库错误
        ('frank', 'api_error@example.com', 'password123'),      # API错误
        ('rate_limited_user', 'test@example.com', 'password123'),  # API频率限制
    ]
    
    print("\n=== 自定义异常属性演示 ===")
    for username, email, password in test_cases:
        print(f"\n创建用户: {username}, {email}")
        print("=" * 60)
        handle_user_creation(service, username, email, password)

demonstrate_custom_exception_attributes()
```

## 异常继承层次设计

### 1. 构建异常层次结构

```python
def demonstrate_exception_hierarchy():
    """演示异常继承层次的设计"""
    
    # 应用程序异常基类
    class ApplicationError(Exception):
        """应用程序异常基类"""
        
        def __init__(self, message, error_code=None, context=None):
            super().__init__(message)
            self.error_code = error_code
            self.context = context or {}
            self.timestamp = '2024-01-01 12:00:00'
        
        def get_error_info(self):
            """获取错误信息字典"""
            return {
                'type': self.__class__.__name__,
                'message': str(self),
                'error_code': self.error_code,
                'context': self.context,
                'timestamp': self.timestamp
            }
    
    # 第一层：按功能模块分类
    class UserError(ApplicationError):
        """用户相关错误"""
        pass
    
    class OrderError(ApplicationError):
        """订单相关错误"""
        pass
    
    class PaymentError(ApplicationError):
        """支付相关错误"""
        pass
    
    class SystemError(ApplicationError):
        """系统相关错误"""
        pass
    
    # 第二层：按错误类型细分
    
    # 用户错误的子类
    class UserValidationError(UserError):
        """用户验证错误"""
        def __init__(self, message, field_name=None, **kwargs):
            super().__init__(message, **kwargs)
            self.field_name = field_name
    
    class UserAuthenticationError(UserError):
        """用户认证错误"""
        def __init__(self, message, auth_method=None, **kwargs):
            super().__init__(message, **kwargs)
            self.auth_method = auth_method
    
    class UserAuthorizationError(UserError):
        """用户授权错误"""
        def __init__(self, message, required_permission=None, **kwargs):
            super().__init__(message, **kwargs)
            self.required_permission = required_permission
    
    class UserNotFoundError(UserError):
        """用户不存在错误"""
        def __init__(self, message, user_id=None, **kwargs):
            super().__init__(message, **kwargs)
            self.user_id = user_id
    
    # 订单错误的子类
    class OrderValidationError(OrderError):
        """订单验证错误"""
        def __init__(self, message, order_id=None, **kwargs):
            super().__init__(message, **kwargs)
            self.order_id = order_id
    
    class OrderStatusError(OrderError):
        """订单状态错误"""
        def __init__(self, message, current_status=None, expected_status=None, **kwargs):
            super().__init__(message, **kwargs)
            self.current_status = current_status
            self.expected_status = expected_status
    
    class OrderNotFoundError(OrderError):
        """订单不存在错误"""
        def __init__(self, message, order_id=None, **kwargs):
            super().__init__(message, **kwargs)
            self.order_id = order_id
    
    # 支付错误的子类
    class PaymentValidationError(PaymentError):
        """支付验证错误"""
        def __init__(self, message, payment_method=None, **kwargs):
            super().__init__(message, **kwargs)
            self.payment_method = payment_method
    
    class PaymentProcessingError(PaymentError):
        """支付处理错误"""
        def __init__(self, message, transaction_id=None, gateway_response=None, **kwargs):
            super().__init__(message, **kwargs)
            self.transaction_id = transaction_id
            self.gateway_response = gateway_response
    
    class InsufficientFundsError(PaymentError):
        """余额不足错误"""
        def __init__(self, message, available_amount=None, required_amount=None, **kwargs):
            super().__init__(message, **kwargs)
            self.available_amount = available_amount
            self.required_amount = required_amount
    
    # 系统错误的子类
    class DatabaseError(SystemError):
        """数据库错误"""
        def __init__(self, message, query=None, **kwargs):
            super().__init__(message, **kwargs)
            self.query = query
    
    class ExternalServiceError(SystemError):
        """外部服务错误"""
        def __init__(self, message, service_name=None, status_code=None, **kwargs):
            super().__init__(message, **kwargs)
            self.service_name = service_name
            self.status_code = status_code
    
    class ConfigurationError(SystemError):
        """配置错误"""
        def __init__(self, message, config_key=None, **kwargs):
            super().__init__(message, **kwargs)
            self.config_key = config_key
    
    # 业务服务类
    class ECommerceService:
        """电商服务类"""
        
        def __init__(self):
            self.users = {
                '1': {'id': '1', 'name': 'Alice', 'balance': 1000, 'role': 'user'},
                '2': {'id': '2', 'name': 'Bob', 'balance': 500, 'role': 'admin'}
            }
            self.orders = {}
            self.next_order_id = 1
        
        def authenticate_user(self, user_id, password):
            """用户认证"""
            if not user_id:
                raise UserValidationError(
                    "用户ID不能为空",
                    field_name='user_id',
                    error_code='USER_ID_REQUIRED'
                )
            
            if user_id not in self.users:
                raise UserNotFoundError(
                    f"用户不存在: {user_id}",
                    user_id=user_id,
                    error_code='USER_NOT_FOUND'
                )
            
            # 模拟密码验证
            if password != 'correct_password':
                raise UserAuthenticationError(
                    "密码错误",
                    auth_method='password',
                    error_code='INVALID_PASSWORD'
                )
            
            return self.users[user_id]
        
        def authorize_user(self, user, required_role):
            """用户授权"""
            if user['role'] != required_role and required_role != 'any':
                raise UserAuthorizationError(
                    f"需要 {required_role} 权限，当前用户权限: {user['role']}",
                    required_permission=required_role,
                    error_code='INSUFFICIENT_PERMISSION'
                )
        
        def create_order(self, user_id, items, total_amount):
            """创建订单"""
            # 验证订单数据
            if not items:
                raise OrderValidationError(
                    "订单项目不能为空",
                    error_code='EMPTY_ORDER_ITEMS'
                )
            
            if total_amount <= 0:
                raise OrderValidationError(
                    f"订单金额必须大于0，当前金额: {total_amount}",
                    error_code='INVALID_ORDER_AMOUNT'
                )
            
            # 创建订单
            order_id = str(self.next_order_id)
            self.next_order_id += 1
            
            order = {
                'id': order_id,
                'user_id': user_id,
                'items': items,
                'total_amount': total_amount,
                'status': 'pending'
            }
            
            self.orders[order_id] = order
            return order
        
        def process_payment(self, order_id, payment_method):
            """处理支付"""
            if order_id not in self.orders:
                raise OrderNotFoundError(
                    f"订单不存在: {order_id}",
                    order_id=order_id,
                    error_code='ORDER_NOT_FOUND'
                )
            
            order = self.orders[order_id]
            
            # 检查订单状态
            if order['status'] != 'pending':
                raise OrderStatusError(
                    f"订单状态不正确，无法支付",
                    current_status=order['status'],
                    expected_status='pending',
                    error_code='INVALID_ORDER_STATUS'
                )
            
            # 验证支付方式
            if payment_method not in ['credit_card', 'balance', 'paypal']:
                raise PaymentValidationError(
                    f"不支持的支付方式: {payment_method}",
                    payment_method=payment_method,
                    error_code='UNSUPPORTED_PAYMENT_METHOD'
                )
            
            user = self.users[order['user_id']]
            
            # 处理余额支付
            if payment_method == 'balance':
                if user['balance'] < order['total_amount']:
                    raise InsufficientFundsError(
                        "余额不足",
                        available_amount=user['balance'],
                        required_amount=order['total_amount'],
                        error_code='INSUFFICIENT_BALANCE'
                    )
                
                user['balance'] -= order['total_amount']
            
            # 模拟外部支付网关错误
            elif payment_method == 'credit_card' and order['total_amount'] > 1000:
                raise PaymentProcessingError(
                    "支付网关处理失败",
                    transaction_id='tx_12345',
                    gateway_response={'error': 'Amount too large'},
                    error_code='GATEWAY_ERROR'
                )
            
            # 更新订单状态
            order['status'] = 'paid'
            order['payment_method'] = payment_method
            
            return {'transaction_id': 'tx_success', 'status': 'completed'}
        
        def complete_order_flow(self, user_id, password, items, total_amount, payment_method):
            """完整的订单流程"""
            try:
                # 用户认证
                user = self.authenticate_user(user_id, password)
                
                # 用户授权（任何已认证用户都可以下单）
                self.authorize_user(user, 'any')
                
                # 创建订单
                order = self.create_order(user_id, items, total_amount)
                
                # 处理支付
                payment_result = self.process_payment(order['id'], payment_method)
                
                return {
                    'success': True,
                    'order': order,
                    'payment': payment_result
                }
                
            except ApplicationError as e:
                return {
                    'success': False,
                    'error': e.get_error_info()
                }
    
    def demonstrate_error_handling(service):
        """演示错误处理"""
        
        test_cases = [
            # (user_id, password, items, total_amount, payment_method, description)
            ('1', 'correct_password', ['item1', 'item2'], 100, 'balance', '正常订单'),
            ('', 'correct_password', ['item1'], 50, 'balance', '用户ID为空'),
            ('999', 'correct_password', ['item1'], 50, 'balance', '用户不存在'),
            ('1', 'wrong_password', ['item1'], 50, 'balance', '密码错误'),
            ('1', 'correct_password', [], 50, 'balance', '订单项目为空'),
            ('1', 'correct_password', ['item1'], -10, 'balance', '订单金额无效'),
            ('1', 'correct_password', ['item1'], 2000, 'balance', '余额不足'),
            ('1', 'correct_password', ['item1'], 50, 'bitcoin', '不支持的支付方式'),
            ('1', 'correct_password', ['item1'], 1500, 'credit_card', '支付网关错误'),
        ]
        
        for user_id, password, items, total_amount, payment_method, description in test_cases:
            print(f"\n测试: {description}")
            print("=" * 50)
            
            result = service.complete_order_flow(user_id, password, items, total_amount, payment_method)
            
            if result['success']:
                print(f"订单成功: {result['order']['id']}")
                print(f"支付结果: {result['payment']}")
            else:
                error = result['error']
                print(f"错误类型: {error['type']}")
                print(f"错误消息: {error['message']}")
                print(f"错误代码: {error['error_code']}")
                print(f"上下文: {error['context']}")
                
                # 根据错误类型提供不同的处理建议
                error_type = error['type']
                if 'Validation' in error_type:
                    print("建议: 检查输入数据的格式和有效性")
                elif 'Authentication' in error_type:
                    print("建议: 检查用户凭据")
                elif 'Authorization' in error_type:
                    print("建议: 检查用户权限")
                elif 'NotFound' in error_type:
                    print("建议: 检查资源是否存在")
                elif 'Payment' in error_type:
                    print("建议: 检查支付信息和余额")
                elif 'System' in error_type:
                    print("建议: 检查系统配置和外部服务")
    
    print("\n=== 异常继承层次演示 ===")
    service = ECommerceService()
    demonstrate_error_handling(service)

demonstrate_exception_hierarchy()
```

## 异常类的高级特性

### 1. 异常类的特殊方法

```python
def demonstrate_exception_special_methods():
    """演示异常类的特殊方法"""
    
    class AdvancedError(Exception):
        """高级异常类，包含特殊方法"""
        
        def __init__(self, message, error_code=None, details=None, suggestions=None):
            super().__init__(message)
            self.error_code = error_code
            self.details = details or {}
            self.suggestions = suggestions or []
            self.timestamp = '2024-01-01 12:00:00'
        
        def __str__(self):
            """字符串表示"""
            base_message = super().__str__()
            if self.error_code:
                return f"[{self.error_code}] {base_message}"
            return base_message
        
        def __repr__(self):
            """开发者友好的表示"""
            return (f"{self.__class__.__name__}("
                   f"message={super().__str__()!r}, "
                   f"error_code={self.error_code!r}, "
                   f"details={self.details!r})")
        
        def __eq__(self, other):
            """相等性比较"""
            if not isinstance(other, AdvancedError):
                return False
            return (str(self) == str(other) and 
                   self.error_code == other.error_code and
                   self.details == other.details)
        
        def __hash__(self):
            """哈希值计算"""
            return hash((str(self), self.error_code, tuple(sorted(self.details.items()))))
        
        def __bool__(self):
            """布尔值转换"""
            return True  # 异常总是为真
        
        def to_dict(self):
            """转换为字典"""
            return {
                'type': self.__class__.__name__,
                'message': super().__str__(),
                'error_code': self.error_code,
                'details': self.details,
                'suggestions': self.suggestions,
                'timestamp': self.timestamp
            }
        
        def to_json(self):
            """转换为JSON字符串"""
            import json
            return json.dumps(self.to_dict(), indent=2)
        
        def get_suggestions(self):
            """获取解决建议"""
            if self.suggestions:
                return "\n".join([f"- {suggestion}" for suggestion in self.suggestions])
            return "暂无解决建议"
    
    class ValidationError(AdvancedError):
        """验证错误"""
        
        def __init__(self, message, field_name=None, field_value=None, **kwargs):
            # 自动生成建议
            suggestions = kwargs.get('suggestions', [])
            if field_name and not suggestions:
                suggestions = [
                    f"检查字段 '{field_name}' 的值是否符合要求",
                    "参考API文档了解字段的有效格式",
                    "使用数据验证工具进行预检查"
                ]
            
            super().__init__(message, suggestions=suggestions, **kwargs)
            self.field_name = field_name
            self.field_value = field_value
        
        def __str__(self):
            base_message = super().__str__()
            if self.field_name:
                return f"{base_message} (字段: {self.field_name})"
            return base_message
    
    class NetworkError(AdvancedError):
        """网络错误"""
        
        def __init__(self, message, url=None, status_code=None, retry_count=0, **kwargs):
            # 根据状态码生成建议
            suggestions = kwargs.get('suggestions', [])
            if not suggestions and status_code:
                if status_code >= 500:
                    suggestions = [
                        "服务器错误，请稍后重试",
                        "检查服务器状态和日志",
                        "联系系统管理员"
                    ]
                elif status_code >= 400:
                    suggestions = [
                        "检查请求参数和格式",
                        "验证API密钥和权限",
                        "参考API文档"
                    ]
                else:
                    suggestions = [
                        "检查网络连接",
                        "验证URL地址",
                        "检查防火墙设置"
                    ]
            
            super().__init__(message, suggestions=suggestions, **kwargs)
            self.url = url
            self.status_code = status_code
            self.retry_count = retry_count
        
        def __str__(self):
            base_message = super().__str__()
            parts = [base_message]
            
            if self.url:
                parts.append(f"URL: {self.url}")
            if self.status_code:
                parts.append(f"状态码: {self.status_code}")
            if self.retry_count > 0:
                parts.append(f"重试次数: {self.retry_count}")
            
            return " | ".join(parts)
        
        def is_retryable(self):
            """判断是否可以重试"""
            # 5xx错误和网络超时可以重试
            return (self.status_code is None or 
                   self.status_code >= 500 or 
                   self.status_code == 408 or  # Request Timeout
                   self.status_code == 429)    # Too Many Requests
    
    # 异常工厂类
    class ErrorFactory:
        """异常工厂"""
        
        @staticmethod
        def create_validation_error(field_name, field_value, validation_type):
            """创建验证错误"""
            messages = {
                'required': f"字段 '{field_name}' 是必需的",
                'type': f"字段 '{field_name}' 类型不正确",
                'length': f"字段 '{field_name}' 长度不符合要求",
                'format': f"字段 '{field_name}' 格式不正确",
                'range': f"字段 '{field_name}' 值超出允许范围"
            }
            
            message = messages.get(validation_type, f"字段 '{field_name}' 验证失败")
            
            return ValidationError(
                message,
                field_name=field_name,
                field_value=field_value,
                error_code=f"VALIDATION_{validation_type.upper()}",
                details={'validation_type': validation_type}
            )
        
        @staticmethod
        def create_network_error(url, status_code=None, original_error=None):
            """创建网络错误"""
            if status_code:
                message = f"HTTP请求失败，状态码: {status_code}"
            elif original_error:
                message = f"网络请求失败: {original_error}"
            else:
                message = "网络请求失败"
            
            return NetworkError(
                message,
                url=url,
                status_code=status_code,
                error_code='NETWORK_ERROR',
                details={'original_error': str(original_error) if original_error else None}
            )
    
    # 测试异常的特殊方法
    def test_exception_methods():
        """测试异常的特殊方法"""
        
        print("=== 异常特殊方法测试 ===")
        
        # 创建异常实例
        error1 = ValidationError(
            "用户名长度不符合要求",
            field_name='username',
            field_value='ab',
            error_code='USERNAME_TOO_SHORT',
            details={'min_length': 3, 'actual_length': 2}
        )
        
        error2 = NetworkError(
            "API调用失败",
            url='https://api.example.com/users',
            status_code=500,
            error_code='API_ERROR',
            retry_count=2
        )
        
        # 测试字符串表示
        print(f"\nstr(error1): {str(error1)}")
        print(f"repr(error1): {repr(error1)}")
        print(f"str(error2): {str(error2)}")
        print(f"repr(error2): {repr(error2)}")
        
        # 测试相等性
        error1_copy = ValidationError(
            "用户名长度不符合要求",
            field_name='username',
            field_value='ab',
            error_code='USERNAME_TOO_SHORT',
            details={'min_length': 3, 'actual_length': 2}
        )
        
        print(f"\nerror1 == error1_copy: {error1 == error1_copy}")
        print(f"error1 == error2: {error1 == error2}")
        
        # 测试哈希值
        print(f"\nhash(error1): {hash(error1)}")
        print(f"hash(error1_copy): {hash(error1_copy)}")
        
        # 测试布尔值
        print(f"\nbool(error1): {bool(error1)}")
        
        # 测试转换方法
        print(f"\nerror1.to_dict(): {error1.to_dict()}")
        print(f"\nerror1.to_json():\n{error1.to_json()}")
        
        # 测试建议
        print(f"\nerror1建议:\n{error1.get_suggestions()}")
        print(f"\nerror2建议:\n{error2.get_suggestions()}")
        
        # 测试网络错误的特殊方法
        print(f"\nerror2.is_retryable(): {error2.is_retryable()}")
        
        # 测试异常工厂
        print("\n=== 异常工厂测试 ===")
        
        factory_error1 = ErrorFactory.create_validation_error('email', 'invalid-email', 'format')
        factory_error2 = ErrorFactory.create_network_error('https://api.test.com', 404)
        
        print(f"工厂创建的验证错误: {factory_error1}")
        print(f"工厂创建的网络错误: {factory_error2}")
        
        # 测试异常集合
        print("\n=== 异常集合测试 ===")
        
        error_set = {error1, error1_copy, error2}
        print(f"异常集合大小: {len(error_set)}")
        print("集合中的异常:")
        for i, err in enumerate(error_set):
            print(f"  {i+1}. {err}")
    
    test_exception_methods()

demonstrate_exception_special_methods()
```

### 2. 异常装饰器和上下文管理器

```python
def demonstrate_exception_decorators_and_context_managers():
    """演示异常装饰器和上下文管理器"""
    
    import functools
    import contextlib
    from typing import Type, Union, Callable, Any
    
    # 异常处理装饰器
    def handle_exceptions(*exception_types, default_return=None, log_errors=True):
        """异常处理装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except exception_types as e:
                    if log_errors:
                        print(f"捕获异常 {type(e).__name__}: {e}")
                    return default_return
                except Exception as e:
                    if log_errors:
                        print(f"未处理的异常 {type(e).__name__}: {e}")
                    raise
            return wrapper
        return decorator
    
    def retry_on_exception(max_retries=3, delay=1, exceptions=(Exception,)):
        """重试装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                last_exception = None
                
                for attempt in range(max_retries + 1):
                    try:
                        return func(*args, **kwargs)
                    except exceptions as e:
                        last_exception = e
                        if attempt < max_retries:
                            print(f"第 {attempt + 1} 次尝试失败: {e}，{delay}秒后重试...")
                            import time
                            time.sleep(delay)
                        else:
                            print(f"所有重试都失败了，抛出最后一个异常")
                            raise last_exception
                
                return None
            return wrapper
        return decorator
    
    def validate_arguments(**validators):
        """参数验证装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 获取函数参数名
                import inspect
                sig = inspect.signature(func)
                bound_args = sig.bind(*args, **kwargs)
                bound_args.apply_defaults()
                
                # 验证参数
                for param_name, validator in validators.items():
                    if param_name in bound_args.arguments:
                        value = bound_args.arguments[param_name]
                        try:
                            validator(value)
                        except Exception as e:
                            raise ValidationError(
                                f"参数 '{param_name}' 验证失败: {e}",
                                field_name=param_name,
                                field_value=value
                            )
                
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    # 异常上下文管理器
    @contextlib.contextmanager
    def exception_handler(exception_types, default_return=None, reraise=False):
        """异常处理上下文管理器"""
        try:
            yield
        except exception_types as e:
            print(f"上下文管理器捕获异常: {type(e).__name__}: {e}")
            if reraise:
                raise
            return default_return
    
    @contextlib.contextmanager
    def error_context(operation_name, cleanup_func=None):
        """错误上下文管理器，提供清理功能"""
        print(f"开始操作: {operation_name}")
        try:
            yield
            print(f"操作成功完成: {operation_name}")
        except Exception as e:
            print(f"操作失败: {operation_name} - {type(e).__name__}: {e}")
            if cleanup_func:
                print("执行清理操作...")
                try:
                    cleanup_func()
                except Exception as cleanup_error:
                    print(f"清理操作失败: {cleanup_error}")
            raise
    
    class ExceptionCollector:
        """异常收集器上下文管理器"""
        
        def __init__(self, collect_all=False):
            self.collect_all = collect_all
            self.exceptions = []
        
        def __enter__(self):
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is not None:
                self.exceptions.append(exc_val)
                if self.collect_all:
                    return True  # 抑制异常
            return False  # 不抑制异常
        
        def has_exceptions(self):
            return len(self.exceptions) > 0
        
        def get_exceptions(self):
            return self.exceptions.copy()
        
        def print_summary(self):
            if self.exceptions:
                print(f"收集到 {len(self.exceptions)} 个异常:")
                for i, exc in enumerate(self.exceptions, 1):
                    print(f"  {i}. {type(exc).__name__}: {exc}")
            else:
                print("没有收集到异常")
    
    # 自定义异常类
    class ValidationError(Exception):
        def __init__(self, message, field_name=None, field_value=None):
            super().__init__(message)
            self.field_name = field_name
            self.field_value = field_value
    
    class NetworkError(Exception):
        def __init__(self, message, retry_count=0):
            super().__init__(message)
            self.retry_count = retry_count
    
    class DataProcessingError(Exception):
        pass
    
    # 测试函数
    @handle_exceptions(ValidationError, NetworkError, default_return="处理失败")
    def process_data_with_handler(data):
        """使用异常处理装饰器的函数"""
        if data == "invalid":
            raise ValidationError("数据无效")
        elif data == "network_error":
            raise NetworkError("网络连接失败")
        elif data == "unknown_error":
            raise DataProcessingError("未知错误")
        return f"处理成功: {data}"
    
    @retry_on_exception(max_retries=3, delay=0.1, exceptions=(NetworkError,))
    def unreliable_network_call(success_rate):
        """不可靠的网络调用"""
        import random
        if random.random() > success_rate:
            raise NetworkError("网络调用失败")
        return "网络调用成功"
    
    # 参数验证器
    def validate_positive_number(value):
        if not isinstance(value, (int, float)):
            raise TypeError("必须是数字")
        if value <= 0:
            raise ValueError("必须是正数")
    
    def validate_non_empty_string(value):
        if not isinstance(value, str):
            raise TypeError("必须是字符串")
        if not value.strip():
            raise ValueError("不能为空字符串")
    
    @validate_arguments(
        name=validate_non_empty_string,
        age=validate_positive_number
    )
    def create_user(name, age, email=None):
        """创建用户，带参数验证"""
        return {'name': name, 'age': age, 'email': email}
    
    # 测试装饰器
    def test_decorators():
        """测试装饰器"""
        print("=== 异常处理装饰器测试 ===")
        
        test_data = ["valid_data", "invalid", "network_error", "unknown_error"]
        
        for data in test_data:
            print(f"\n处理数据: {data}")
            result = process_data_with_handler(data)
            print(f"结果: {result}")
        
        print("\n=== 重试装饰器测试 ===")
        
        # 测试重试装饰器（设置较高的成功率以减少重试次数）
        print("\n尝试网络调用（成功率70%）:")
        try:
            result = unreliable_network_call(0.7)
            print(f"结果: {result}")
        except NetworkError as e:
            print(f"最终失败: {e}")
        
        print("\n=== 参数验证装饰器测试 ===")
        
        test_users = [
            ("Alice", 25),           # 正常
            ("", 25),               # 姓名为空
            ("Bob", -5),            # 年龄为负
            ("Charlie", "25"),      # 年龄类型错误
        ]
        
        for name, age in test_users:
            print(f"\n创建用户: name={name}, age={age}")
            try:
                user = create_user(name, age)
                print(f"用户创建成功: {user}")
            except ValidationError as e:
                print(f"验证失败: {e}")
    
    # 测试上下文管理器
    def test_context_managers():
        """测试上下文管理器"""
        print("\n=== 异常处理上下文管理器测试 ===")
        
        # 测试异常处理上下文管理器
        with exception_handler((ValidationError, NetworkError), default_return="默认值"):
            print("执行可能出错的操作...")
            raise ValidationError("测试验证错误")
        
        print("\n=== 错误上下文管理器测试 ===")
        
        def cleanup_operation():
            print("执行资源清理")
        
        try:
            with error_context("数据库操作", cleanup_func=cleanup_operation):
                print("执行数据库操作...")
                raise DataProcessingError("数据库连接失败")
        except DataProcessingError:
            print("异常已被重新抛出")
        
        print("\n=== 异常收集器测试 ===")
        
        # 收集异常但不抑制
        collector1 = ExceptionCollector(collect_all=False)
        try:
            with collector1:
                raise ValidationError("收集的验证错误")
        except ValidationError:
            print("异常被重新抛出")
        
        collector1.print_summary()
        
        # 收集异常并抑制
        collector2 = ExceptionCollector(collect_all=True)
        with collector2:
            raise NetworkError("收集的网络错误")
        
        print("异常被抑制，程序继续执行")
        collector2.print_summary()
        
        # 收集多个异常
        collector3 = ExceptionCollector(collect_all=True)
        
        operations = [
            lambda: exec('raise ValidationError("错误1")'),
            lambda: exec('raise NetworkError("错误2")'),
            lambda: print("正常操作")
        ]
        
        for i, operation in enumerate(operations):
            with collector3:
                print(f"执行操作 {i+1}")
                try:
                    operation()
                except:
                    # 在这里重新抛出以便收集器捕获
                    raise
        
        collector3.print_summary()
    
    # 运行测试
    test_decorators()
    test_context_managers()

demonstrate_exception_decorators_and_context_managers()
```

## 学习要点总结

### 自定义异常的基本原则
1. **继承合适的基类**: 通常继承Exception或其子类
2. **提供有意义的信息**: 包含足够的上下文信息
3. **遵循命名约定**: 异常类名通常以Error结尾
4. **设计清晰的层次**: 构建合理的异常继承结构

### 异常类设计要点
1. **自定义属性**: 添加业务相关的属性信息
2. **特殊方法**: 实现__str__、__repr__等方法
3. **工厂方法**: 提供便捷的异常创建方式
4. **转换方法**: 支持转换为字典、JSON等格式

### 异常层次设计
1. **按模块分类**: 根据业务模块组织异常
2. **按类型细分**: 在模块内按错误类型细分
3. **保持一致性**: 统一的命名和结构规范
4. **适度抽象**: 避免过度细分或过度抽象

### 高级特性应用
1. **装饰器模式**: 使用装饰器简化异常处理
2. **上下文管理器**: 提供资源管理和异常处理
3. **异常收集**: 批量处理多个异常
4. **重试机制**: 自动重试失败的操作

## 下一步学习

掌握了自定义异常后，接下来将学习：
- [07. 异常链和上下文](./07_exception_chaining.md) - 深入理解异常传播和链接
- [08. 异常日志记录](./08_logging_exceptions.md) - 异常的记录和监控
- [09. 异常处理最佳实践](./09_best_practices.md) - 综合应用和最佳实践

通过掌握自定义异常的设计和实现，你可以构建更加专业和易维护的错误处理系统，提高代码的可读性和调试效率。