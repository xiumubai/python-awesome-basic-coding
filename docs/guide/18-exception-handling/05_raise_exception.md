# 05. 抛出异常

## 学习目标

- 掌握使用raise语句主动抛出异常
- 理解异常的传播机制和调用栈
- 学会重新抛出捕获的异常
- 掌握异常链接和上下文保持
- 学会设计合理的异常抛出策略

## raise语句的基本用法

### 1. 抛出内置异常

```python
def demonstrate_basic_raise():
    """演示基本的raise语句用法"""
    
    def validate_age(age):
        """验证年龄的有效性"""
        if not isinstance(age, (int, float)):
            raise TypeError(f"年龄必须是数字，得到了 {type(age).__name__}")
        
        if age < 0:
            raise ValueError(f"年龄不能为负数，得到了 {age}")
        
        if age > 150:
            raise ValueError(f"年龄不能超过150岁，得到了 {age}")
        
        return True
    
    def validate_email(email):
        """验证邮箱格式"""
        if not isinstance(email, str):
            raise TypeError("邮箱必须是字符串类型")
        
        if not email:
            raise ValueError("邮箱不能为空")
        
        if '@' not in email:
            raise ValueError(f"邮箱格式无效: {email}")
        
        parts = email.split('@')
        if len(parts) != 2:
            raise ValueError(f"邮箱格式无效: {email}")
        
        username, domain = parts
        if not username or not domain:
            raise ValueError(f"邮箱格式无效: {email}")
        
        return True
    
    def create_user(name, age, email):
        """创建用户，包含多重验证"""
        print(f"正在创建用户: {name}")
        
        # 验证姓名
        if not name or not isinstance(name, str):
            raise ValueError("用户名不能为空且必须是字符串")
        
        # 验证年龄
        validate_age(age)
        
        # 验证邮箱
        validate_email(email)
        
        # 如果所有验证都通过
        user = {
            'name': name,
            'age': age,
            'email': email,
            'created_at': '2024-01-01'
        }
        
        print(f"用户创建成功: {user}")
        return user
    
    # 测试不同的输入
    test_cases = [
        ("Alice", 25, "alice@example.com"),     # 正常情况
        ("Bob", "25", "bob@example.com"),       # 年龄类型错误
        ("Charlie", -5, "charlie@example.com"), # 年龄为负
        ("David", 200, "david@example.com"),    # 年龄过大
        ("Eve", 30, "invalid-email"),           # 邮箱格式错误
        ("", 25, "test@example.com"),           # 姓名为空
    ]
    
    print("=== 基本raise语句演示 ===")
    for name, age, email in test_cases:
        print(f"\n尝试创建用户: name={name}, age={age}, email={email}")
        try:
            user = create_user(name, age, email)
        except (TypeError, ValueError) as e:
            print(f"创建失败: {type(e).__name__} - {e}")

demonstrate_basic_raise()
```

### 2. 抛出异常时不带参数

```python
def demonstrate_raise_without_args():
    """演示不带参数的raise语句"""
    
    def risky_operation(operation_type):
        """可能出现异常的操作"""
        try:
            if operation_type == 'divide_by_zero':
                result = 10 / 0
            elif operation_type == 'index_error':
                my_list = [1, 2, 3]
                result = my_list[10]
            elif operation_type == 'key_error':
                my_dict = {'a': 1, 'b': 2}
                result = my_dict['c']
            else:
                result = f"操作 {operation_type} 完成"
            
            return result
            
        except ZeroDivisionError:
            print("捕获到除零错误，记录日志后重新抛出")
            # 记录错误日志
            print(f"错误日志: 在操作 {operation_type} 中发生除零错误")
            # 重新抛出相同的异常
            raise  # 不带参数的raise，重新抛出当前异常
            
        except (IndexError, KeyError) as e:
            print(f"捕获到访问错误: {type(e).__name__}")
            print("进行错误处理后重新抛出")
            # 可以在这里进行一些清理工作
            print("执行清理操作...")
            # 重新抛出原始异常
            raise
    
    def safe_wrapper(operation_type):
        """安全包装器"""
        try:
            return risky_operation(operation_type)
        except Exception as e:
            print(f"在包装器中捕获异常: {type(e).__name__} - {e}")
            return None
    
    # 测试不同操作
    operations = ['normal', 'divide_by_zero', 'index_error', 'key_error']
    
    print("\n=== 不带参数的raise演示 ===")
    for op in operations:
        print(f"\n执行操作: {op}")
        print("-" * 30)
        result = safe_wrapper(op)
        print(f"最终结果: {result}")

demonstrate_raise_without_args()
```

### 3. 抛出异常实例

```python
def demonstrate_raise_exception_instance():
    """演示抛出异常实例"""
    
    class ValidationError(Exception):
        """自定义验证异常"""
        def __init__(self, message, field_name=None, field_value=None):
            super().__init__(message)
            self.field_name = field_name
            self.field_value = field_value
            self.timestamp = '2024-01-01 12:00:00'
    
    def validate_user_data(user_data):
        """验证用户数据，抛出详细的异常实例"""
        
        # 检查数据类型
        if not isinstance(user_data, dict):
            error = TypeError("用户数据必须是字典类型")
            error.received_type = type(user_data).__name__
            raise error
        
        # 检查必需字段
        required_fields = ['username', 'password', 'email']
        for field in required_fields:
            if field not in user_data:
                error = ValidationError(
                    f"缺少必需字段: {field}",
                    field_name=field,
                    field_value=None
                )
                raise error
        
        # 验证用户名
        username = user_data['username']
        if not isinstance(username, str) or len(username) < 3:
            error = ValidationError(
                "用户名必须是至少3个字符的字符串",
                field_name='username',
                field_value=username
            )
            raise error
        
        # 验证密码强度
        password = user_data['password']
        if len(password) < 8:
            error = ValidationError(
                "密码长度至少8个字符",
                field_name='password',
                field_value='***'  # 不显示实际密码
            )
            raise error
        
        # 验证邮箱
        email = user_data['email']
        if '@' not in email or '.' not in email:
            error = ValidationError(
                "邮箱格式无效",
                field_name='email',
                field_value=email
            )
            raise error
        
        return True
    
    def register_user(user_data):
        """用户注册函数"""
        try:
            print(f"开始注册用户: {user_data.get('username', 'Unknown')}")
            
            # 验证数据
            validate_user_data(user_data)
            
            # 模拟数据库操作
            if user_data['username'] == 'existing_user':
                error = ValueError("用户名已存在")
                error.error_code = 'DUPLICATE_USERNAME'
                error.suggested_usernames = ['existing_user1', 'existing_user2']
                raise error
            
            print("用户注册成功")
            return {'user_id': 12345, 'status': 'registered'}
            
        except ValidationError as e:
            print(f"验证错误: {e}")
            print(f"  字段: {e.field_name}")
            print(f"  值: {e.field_value}")
            print(f"  时间: {e.timestamp}")
            return None
            
        except TypeError as e:
            print(f"类型错误: {e}")
            if hasattr(e, 'received_type'):
                print(f"  接收到的类型: {e.received_type}")
            return None
            
        except ValueError as e:
            print(f"值错误: {e}")
            if hasattr(e, 'error_code'):
                print(f"  错误代码: {e.error_code}")
            if hasattr(e, 'suggested_usernames'):
                print(f"  建议用户名: {e.suggested_usernames}")
            return None
    
    # 测试用例
    test_users = [
        {'username': 'alice', 'password': 'password123', 'email': 'alice@example.com'},  # 正常
        {'username': 'bob', 'password': '123'},  # 密码太短
        {'username': 'ab'},  # 缺少字段
        "not_a_dict",  # 类型错误
        {'username': 'existing_user', 'password': 'password123', 'email': 'test@example.com'},  # 用户名已存在
    ]
    
    print("\n=== 抛出异常实例演示 ===")
    for i, user_data in enumerate(test_users):
        print(f"\n测试用例 {i+1}: {user_data}")
        print("-" * 50)
        result = register_user(user_data)
        print(f"注册结果: {result}")

demonstrate_raise_exception_instance()
```

## 异常的传播机制

### 1. 调用栈中的异常传播

```python
def demonstrate_exception_propagation():
    """演示异常在调用栈中的传播"""
    
    def level_4_function():
        """第4层函数 - 最深层，抛出异常"""
        print("    执行第4层函数")
        raise RuntimeError("在第4层函数中发生错误")
    
    def level_3_function(handle_exception=False):
        """第3层函数"""
        print("  执行第3层函数")
        try:
            level_4_function()
        except RuntimeError as e:
            if handle_exception:
                print(f"  第3层捕获并处理异常: {e}")
                return "第3层处理的结果"
            else:
                print(f"  第3层捕获异常但重新抛出: {e}")
                raise  # 重新抛出异常
    
    def level_2_function(handle_at_level_3=False, handle_at_level_2=False):
        """第2层函数"""
        print("执行第2层函数")
        try:
            result = level_3_function(handle_exception=handle_at_level_3)
            return result
        except RuntimeError as e:
            if handle_at_level_2:
                print(f"第2层捕获并处理异常: {e}")
                return "第2层处理的结果"
            else:
                print(f"第2层捕获异常但重新抛出: {e}")
                raise
    
    def level_1_function(handle_at_3=False, handle_at_2=False, handle_at_1=False):
        """第1层函数 - 最外层"""
        print("执行第1层函数")
        try:
            result = level_2_function(handle_at_level_3=handle_at_3, handle_at_level_2=handle_at_2)
            return result
        except RuntimeError as e:
            if handle_at_1:
                print(f"第1层捕获并处理异常: {e}")
                return "第1层处理的结果"
            else:
                print(f"第1层捕获异常但重新抛出: {e}")
                raise
    
    # 测试不同的异常处理策略
    test_scenarios = [
        (False, False, False, "异常传播到最外层"),
        (False, False, True, "在第1层处理异常"),
        (False, True, False, "在第2层处理异常"),
        (True, False, False, "在第3层处理异常"),
    ]
    
    print("\n=== 异常传播机制演示 ===")
    for handle_3, handle_2, handle_1, description in test_scenarios:
        print(f"\n场景: {description}")
        print("=" * 40)
        
        try:
            result = level_1_function(handle_at_3=handle_3, handle_at_2=handle_2, handle_at_1=handle_1)
            print(f"最终结果: {result}")
        except RuntimeError as e:
            print(f"未处理的异常到达顶层: {e}")
            import traceback
            print("完整调用栈:")
            traceback.print_exc()

demonstrate_exception_propagation()
```

### 2. 异常传播的控制

```python
def demonstrate_exception_control():
    """演示异常传播的控制技巧"""
    
    class BusinessLogicError(Exception):
        """业务逻辑异常"""
        pass
    
    class DataAccessError(Exception):
        """数据访问异常"""
        pass
    
    class SystemError(Exception):
        """系统异常"""
        pass
    
    def data_access_layer(operation):
        """数据访问层"""
        print(f"    数据层执行: {operation}")
        
        if operation == 'connection_failed':
            raise ConnectionError("数据库连接失败")
        elif operation == 'permission_denied':
            raise PermissionError("数据库权限不足")
        elif operation == 'data_not_found':
            raise FileNotFoundError("数据不存在")
        else:
            return f"数据层结果: {operation}"
    
    def business_logic_layer(operation):
        """业务逻辑层"""
        print(f"  业务层处理: {operation}")
        
        try:
            result = data_access_layer(operation)
            
            # 业务逻辑验证
            if operation == 'invalid_business_rule':
                raise BusinessLogicError("违反业务规则")
            
            return result
            
        except ConnectionError as e:
            # 连接错误转换为系统错误
            print(f"  业务层捕获连接错误: {e}")
            raise SystemError(f"系统不可用: {e}") from e
            
        except PermissionError as e:
            # 权限错误转换为数据访问错误
            print(f"  业务层捕获权限错误: {e}")
            raise DataAccessError(f"数据访问被拒绝: {e}") from e
            
        except FileNotFoundError as e:
            # 数据不存在，返回默认值而不抛出异常
            print(f"  业务层捕获数据不存在错误: {e}")
            print(f"  返回默认值")
            return "默认数据"
    
    def presentation_layer(operation):
        """表示层"""
        print(f"表示层请求: {operation}")
        
        try:
            result = business_logic_layer(operation)
            return {'status': 'success', 'data': result}
            
        except BusinessLogicError as e:
            # 业务逻辑错误，返回用户友好的错误信息
            print(f"表示层捕获业务逻辑错误: {e}")
            return {'status': 'error', 'message': '业务规则验证失败', 'code': 400}
            
        except DataAccessError as e:
            # 数据访问错误，返回权限错误
            print(f"表示层捕获数据访问错误: {e}")
            return {'status': 'error', 'message': '数据访问权限不足', 'code': 403}
            
        except SystemError as e:
            # 系统错误，返回服务器错误
            print(f"表示层捕获系统错误: {e}")
            return {'status': 'error', 'message': '系统暂时不可用', 'code': 500}
            
        except Exception as e:
            # 未预期的错误
            print(f"表示层捕获未知错误: {e}")
            import traceback
            traceback.print_exc()
            return {'status': 'error', 'message': '服务器内部错误', 'code': 500}
    
    # 测试不同的操作
    test_operations = [
        'normal_operation',
        'connection_failed',
        'permission_denied',
        'data_not_found',
        'invalid_business_rule',
    ]
    
    print("\n=== 异常传播控制演示 ===")
    for operation in test_operations:
        print(f"\n测试操作: {operation}")
        print("=" * 50)
        
        response = presentation_layer(operation)
        print(f"最终响应: {response}")

demonstrate_exception_control()
```

## 异常链接和上下文保持

### 1. 使用from关键字链接异常

```python
def demonstrate_exception_chaining():
    """演示异常链接技术"""
    
    class ConfigurationError(Exception):
        """配置错误"""
        pass
    
    class ServiceInitializationError(Exception):
        """服务初始化错误"""
        pass
    
    def load_config_file(filename):
        """加载配置文件"""
        try:
            with open(filename, 'r') as f:
                import json
                config = json.load(f)
                return config
        except FileNotFoundError as e:
            # 将底层异常链接到高层异常
            raise ConfigurationError(f"配置文件 {filename} 不存在") from e
        except json.JSONDecodeError as e:
            # 保持原始异常的上下文
            raise ConfigurationError(f"配置文件 {filename} 格式错误") from e
        except PermissionError as e:
            # 链接权限异常
            raise ConfigurationError(f"无权限读取配置文件 {filename}") from e
    
    def validate_config(config):
        """验证配置"""
        required_keys = ['database_url', 'api_key', 'port']
        
        for key in required_keys:
            if key not in config:
                # 创建新异常但不链接（因为这不是由其他异常引起的）
                raise ConfigurationError(f"配置缺少必需的键: {key}")
        
        # 验证端口号
        try:
            port = int(config['port'])
            if port < 1 or port > 65535:
                raise ValueError(f"端口号超出有效范围: {port}")
        except (ValueError, TypeError) as e:
            # 链接类型转换异常
            raise ConfigurationError(f"端口配置无效: {config['port']}") from e
    
    def initialize_service(config_file):
        """初始化服务"""
        try:
            # 加载配置
            config = load_config_file(config_file)
            
            # 验证配置
            validate_config(config)
            
            # 模拟服务初始化
            if config.get('database_url') == 'invalid_url':
                raise ConnectionError("无法连接到数据库")
            
            return {'status': 'initialized', 'config': config}
            
        except ConfigurationError as e:
            # 将配置错误包装为服务初始化错误
            raise ServiceInitializationError(f"服务初始化失败: 配置问题") from e
        except ConnectionError as e:
            # 将连接错误包装为服务初始化错误
            raise ServiceInitializationError(f"服务初始化失败: 数据库连接问题") from e
    
    def start_application(config_file):
        """启动应用程序"""
        try:
            service = initialize_service(config_file)
            print(f"应用程序启动成功: {service}")
            return service
        except ServiceInitializationError as e:
            print(f"应用程序启动失败: {e}")
            
            # 打印完整的异常链
            print("\n异常链:")
            current_exception = e
            level = 0
            while current_exception:
                indent = "  " * level
                print(f"{indent}{type(current_exception).__name__}: {current_exception}")
                current_exception = current_exception.__cause__
                level += 1
            
            return None
    
    # 创建测试配置文件
    import json
    
    # 正常配置
    with open('valid_config.json', 'w') as f:
        json.dump({
            'database_url': 'postgresql://localhost:5432/mydb',
            'api_key': 'secret_key_123',
            'port': 8080
        }, f)
    
    # 无效配置
    with open('invalid_config.json', 'w') as f:
        json.dump({
            'database_url': 'invalid_url',
            'api_key': 'secret_key_123',
            'port': 'invalid_port'
        }, f)
    
    # 格式错误的配置
    with open('malformed_config.json', 'w') as f:
        f.write('{ invalid json }')
    
    # 测试不同的配置文件
    test_configs = [
        'valid_config.json',
        'invalid_config.json',
        'malformed_config.json',
        'nonexistent_config.json'
    ]
    
    print("\n=== 异常链接演示 ===")
    for config_file in test_configs:
        print(f"\n测试配置文件: {config_file}")
        print("=" * 60)
        start_application(config_file)

demonstrate_exception_chaining()
```

### 2. 抑制异常上下文

```python
def demonstrate_exception_suppression():
    """演示异常上下文的抑制"""
    
    def convert_data_with_context(data):
        """数据转换 - 保持异常上下文"""
        try:
            # 尝试转换为整数
            return int(data)
        except ValueError as e:
            # 抛出新异常，保持原始异常上下文
            raise TypeError(f"无法将 '{data}' 转换为整数") from e
    
    def convert_data_without_context(data):
        """数据转换 - 抑制异常上下文"""
        try:
            # 尝试转换为整数
            return int(data)
        except ValueError:
            # 抛出新异常，抑制原始异常上下文
            raise TypeError(f"无法将 '{data}' 转换为整数") from None
    
    def convert_data_implicit_context(data):
        """数据转换 - 隐式异常上下文"""
        try:
            # 尝试转换为整数
            return int(data)
        except ValueError:
            # 直接抛出新异常，会自动保持上下文
            raise TypeError(f"无法将 '{data}' 转换为整数")
    
    def test_conversion_method(method_name, convert_func, test_data):
        """测试转换方法"""
        print(f"\n--- {method_name} ---")
        try:
            result = convert_func(test_data)
            print(f"转换成功: {result}")
        except Exception as e:
            print(f"捕获异常: {type(e).__name__}: {e}")
            
            # 检查异常上下文
            if e.__cause__ is not None:
                print(f"显式原因: {type(e.__cause__).__name__}: {e.__cause__}")
            elif e.__context__ is not None:
                print(f"隐式上下文: {type(e.__context__).__name__}: {e.__context__}")
            else:
                print("无异常上下文")
    
    # 测试数据
    test_data = "abc"
    
    print("\n=== 异常上下文抑制演示 ===")
    print(f"测试数据: '{test_data}'")
    
    # 测试三种不同的异常处理方式
    test_conversion_method("保持异常上下文 (from e)", convert_data_with_context, test_data)
    test_conversion_method("抑制异常上下文 (from None)", convert_data_without_context, test_data)
    test_conversion_method("隐式异常上下文", convert_data_implicit_context, test_data)

demonstrate_exception_suppression()
```

## 异常抛出的最佳实践

### 1. 设计合理的异常层次

```python
def demonstrate_exception_design_patterns():
    """演示异常设计模式"""
    
    # 定义异常层次结构
    class APIError(Exception):
        """API基础异常"""
        def __init__(self, message, error_code=None, details=None):
            super().__init__(message)
            self.error_code = error_code
            self.details = details or {}
            self.timestamp = '2024-01-01 12:00:00'
    
    class ValidationError(APIError):
        """验证错误"""
        def __init__(self, message, field_name=None, field_value=None):
            super().__init__(message, error_code='VALIDATION_ERROR')
            self.field_name = field_name
            self.field_value = field_value
    
    class AuthenticationError(APIError):
        """认证错误"""
        def __init__(self, message, auth_method=None):
            super().__init__(message, error_code='AUTH_ERROR')
            self.auth_method = auth_method
    
    class AuthorizationError(APIError):
        """授权错误"""
        def __init__(self, message, required_permission=None):
            super().__init__(message, error_code='AUTHZ_ERROR')
            self.required_permission = required_permission
    
    class ResourceError(APIError):
        """资源错误"""
        def __init__(self, message, resource_type=None, resource_id=None):
            super().__init__(message, error_code='RESOURCE_ERROR')
            self.resource_type = resource_type
            self.resource_id = resource_id
    
    class ExternalServiceError(APIError):
        """外部服务错误"""
        def __init__(self, message, service_name=None, status_code=None):
            super().__init__(message, error_code='EXTERNAL_SERVICE_ERROR')
            self.service_name = service_name
            self.status_code = status_code
    
    # API服务实现
    class UserService:
        """用户服务"""
        
        def __init__(self):
            self.users = {
                '1': {'id': '1', 'name': 'Alice', 'role': 'admin'},
                '2': {'id': '2', 'name': 'Bob', 'role': 'user'}
            }
            self.sessions = {'valid_token': '1'}  # token -> user_id
        
        def authenticate_user(self, token):
            """用户认证"""
            if not token:
                raise AuthenticationError("缺少认证令牌", auth_method='token')
            
            if token not in self.sessions:
                raise AuthenticationError("无效的认证令牌", auth_method='token')
            
            return self.sessions[token]
        
        def authorize_user(self, user_id, required_role):
            """用户授权"""
            user = self.users.get(user_id)
            if not user:
                raise ResourceError("用户不存在", resource_type='user', resource_id=user_id)
            
            if user['role'] != required_role and required_role != 'any':
                raise AuthorizationError(
                    f"需要 {required_role} 权限",
                    required_permission=required_role
                )
            
            return user
        
        def validate_user_data(self, user_data):
            """验证用户数据"""
            if not isinstance(user_data, dict):
                raise ValidationError("用户数据必须是字典格式")
            
            if 'name' not in user_data:
                raise ValidationError("缺少用户名", field_name='name')
            
            name = user_data['name']
            if not isinstance(name, str) or len(name.strip()) < 2:
                raise ValidationError(
                    "用户名必须是至少2个字符的字符串",
                    field_name='name',
                    field_value=name
                )
        
        def create_user(self, token, user_data):
            """创建用户"""
            try:
                # 认证
                user_id = self.authenticate_user(token)
                
                # 授权
                self.authorize_user(user_id, 'admin')
                
                # 验证数据
                self.validate_user_data(user_data)
                
                # 模拟外部服务调用
                self._call_external_service('email_service', user_data.get('email'))
                
                # 创建用户
                new_user_id = str(len(self.users) + 1)
                new_user = {
                    'id': new_user_id,
                    'name': user_data['name'].strip(),
                    'role': user_data.get('role', 'user')
                }
                self.users[new_user_id] = new_user
                
                return new_user
                
            except APIError:
                # 重新抛出API相关异常
                raise
            except Exception as e:
                # 包装未预期的异常
                raise APIError(f"创建用户时发生未知错误: {e}") from e
        
        def _call_external_service(self, service_name, data):
            """调用外部服务"""
            if service_name == 'email_service' and data == 'invalid@email':
                raise ExternalServiceError(
                    "邮件服务验证失败",
                    service_name=service_name,
                    status_code=400
                )
    
    def handle_api_request(service, token, user_data):
        """处理API请求"""
        try:
            result = service.create_user(token, user_data)
            return {
                'success': True,
                'data': result,
                'error': None
            }
        except ValidationError as e:
            return {
                'success': False,
                'data': None,
                'error': {
                    'type': 'validation_error',
                    'message': str(e),
                    'field': e.field_name,
                    'value': e.field_value,
                    'code': e.error_code
                }
            }
        except AuthenticationError as e:
            return {
                'success': False,
                'data': None,
                'error': {
                    'type': 'authentication_error',
                    'message': str(e),
                    'auth_method': e.auth_method,
                    'code': e.error_code
                }
            }
        except AuthorizationError as e:
            return {
                'success': False,
                'data': None,
                'error': {
                    'type': 'authorization_error',
                    'message': str(e),
                    'required_permission': e.required_permission,
                    'code': e.error_code
                }
            }
        except ResourceError as e:
            return {
                'success': False,
                'data': None,
                'error': {
                    'type': 'resource_error',
                    'message': str(e),
                    'resource_type': e.resource_type,
                    'resource_id': e.resource_id,
                    'code': e.error_code
                }
            }
        except ExternalServiceError as e:
            return {
                'success': False,
                'data': None,
                'error': {
                    'type': 'external_service_error',
                    'message': str(e),
                    'service_name': e.service_name,
                    'status_code': e.status_code,
                    'code': e.error_code
                }
            }
        except APIError as e:
            return {
                'success': False,
                'data': None,
                'error': {
                    'type': 'api_error',
                    'message': str(e),
                    'code': e.error_code,
                    'details': e.details
                }
            }
    
    # 测试用例
    service = UserService()
    
    test_cases = [
        ('valid_token', {'name': 'Charlie', 'role': 'user'}),  # 正常情况
        ('invalid_token', {'name': 'David'}),  # 认证失败
        ('valid_token', {'name': 'E'}),  # 验证失败
        ('valid_token', {'name': 'Frank', 'email': 'invalid@email'}),  # 外部服务错误
        (None, {'name': 'Grace'}),  # 缺少token
    ]
    
    print("\n=== 异常设计模式演示 ===")
    for token, user_data in test_cases:
        print(f"\n请求: token={token}, data={user_data}")
        print("-" * 60)
        
        response = handle_api_request(service, token, user_data)
        
        if response['success']:
            print(f"成功: {response['data']}")
        else:
            error = response['error']
            print(f"失败: {error['type']} - {error['message']}")
            print(f"错误代码: {error['code']}")
            
            # 打印特定错误的详细信息
            for key, value in error.items():
                if key not in ['type', 'message', 'code'] and value is not None:
                    print(f"  {key}: {value}")

demonstrate_exception_design_patterns()
```

## 学习要点总结

### raise语句的用法
1. **raise Exception("message")**: 抛出新的异常实例
2. **raise**: 重新抛出当前捕获的异常
3. **raise Exception from cause**: 链接异常，保持原因
4. **raise Exception from None**: 抑制异常上下文

### 异常传播机制
1. **向上传播**: 异常会沿调用栈向上传播
2. **传播控制**: 可以在任何层级捕获和处理异常
3. **异常转换**: 将底层异常转换为高层异常
4. **上下文保持**: 使用from关键字保持异常链

### 设计原则
1. **层次清晰**: 设计合理的异常继承层次
2. **信息丰富**: 异常应包含足够的调试信息
3. **适当抽象**: 在合适的层级抛出合适的异常
4. **上下文保持**: 保持异常的原始上下文信息

### 最佳实践
- 在合适的抽象层级抛出异常
- 提供详细的错误信息和上下文
- 使用异常链保持原始错误信息
- 设计一致的异常处理策略

## 下一步学习

掌握了异常抛出技巧后，接下来将学习：
- [06. 自定义异常](./06_custom_exceptions.md) - 创建业务相关的异常类
- [07. 异常链和上下文](./07_exception_chaining.md) - 深入理解异常传播
- [08. 异常日志记录](./08_logging_exceptions.md) - 异常的记录和监控

通过掌握异常抛出机制，你可以构建更加清晰和可维护的错误处理系统，有效地传达程序中的问题和状态。