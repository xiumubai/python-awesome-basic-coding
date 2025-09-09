# 参数验证

参数验证是编写健壮Python函数的重要技能。通过适当的参数验证，我们可以确保函数接收到正确类型和格式的数据，提前发现错误，并提供清晰的错误信息。这不仅提高了代码的可靠性，还改善了调试体验。

## 为什么需要参数验证？

### 参数验证的重要性

```python
def why_parameter_validation():
    """
    演示为什么需要参数验证
    """
    print("🔍 为什么需要参数验证？")
    print("-" * 40)
    
    # 没有参数验证的函数
    def calculate_average_no_validation(numbers):
        """计算平均值（无验证版本）"""
        return sum(numbers) / len(numbers)
    
    # 有参数验证的函数
    def calculate_average_with_validation(numbers):
        """计算平均值（有验证版本）"""
        # 类型验证
        if not isinstance(numbers, (list, tuple)):
            raise TypeError(f"期望列表或元组，但得到 {type(numbers).__name__}")
        
        # 空值验证
        if not numbers:
            raise ValueError("数字列表不能为空")
        
        # 元素类型验证
        for i, num in enumerate(numbers):
            if not isinstance(num, (int, float)):
                raise TypeError(f"索引 {i} 处的元素必须是数字，但得到 {type(num).__name__}: {num}")
        
        return sum(numbers) / len(numbers)
    
    # 测试数据
    test_cases = [
        [1, 2, 3, 4, 5],           # 正常情况
        [],                        # 空列表
        "12345",                   # 错误类型
        [1, 2, "3", 4, 5],         # 包含非数字元素
        None,                      # None值
    ]
    
    for i, test_data in enumerate(test_cases):
        print(f"\n测试用例 {i+1}: {test_data}")
        
        # 测试无验证版本
        print("  无验证版本:")
        try:
            result = calculate_average_no_validation(test_data)
            print(f"    结果: {result}")
        except Exception as e:
            print(f"    错误: {type(e).__name__}: {e}")
        
        # 测试有验证版本
        print("  有验证版本:")
        try:
            result = calculate_average_with_validation(test_data)
            print(f"    结果: {result}")
        except Exception as e:
            print(f"    错误: {type(e).__name__}: {e}")
    
    print("-" * 40)

# 运行演示
why_parameter_validation()
```

## 基本类型检查

### 使用isinstance进行类型检查

```python
def basic_type_checking():
    """
    演示基本的类型检查方法
    """
    print("🏷️  基本类型检查")
    print("-" * 40)
    
    def process_user_data(name, age, email, active=True):
        """
        处理用户数据，包含类型检查
        """
        print(f"处理用户数据: name={name}, age={age}, email={email}, active={active}")
        
        # 字符串类型检查
        if not isinstance(name, str):
            raise TypeError(f"name 必须是字符串，但得到 {type(name).__name__}")
        
        if not isinstance(email, str):
            raise TypeError(f"email 必须是字符串，但得到 {type(email).__name__}")
        
        # 数字类型检查
        if not isinstance(age, int):
            raise TypeError(f"age 必须是整数，但得到 {type(age).__name__}")
        
        # 布尔类型检查
        if not isinstance(active, bool):
            raise TypeError(f"active 必须是布尔值，但得到 {type(active).__name__}")
        
        # 额外的值验证
        if not name.strip():
            raise ValueError("name 不能为空")
        
        if age < 0 or age > 150:
            raise ValueError(f"age 必须在 0-150 之间，但得到 {age}")
        
        if "@" not in email or "." not in email:
            raise ValueError(f"email 格式无效: {email}")
        
        return {
            "name": name.strip(),
            "age": age,
            "email": email.lower(),
            "active": active,
            "processed_at": "2024-01-01 12:00:00"
        }
    
    # 测试不同类型的输入
    test_cases = [
        ("Alice", 25, "alice@example.com", True),      # 正常情况
        ("Bob", "30", "bob@example.com", True),        # age为字符串
        ("", 25, "alice@example.com", True),           # 空name
        ("Charlie", -5, "charlie@example.com", True),  # 负数age
        ("David", 25, "invalid-email", True),          # 无效email
        ("Eve", 25, "eve@example.com", "yes"),         # active为字符串
    ]
    
    for i, (name, age, email, active) in enumerate(test_cases):
        print(f"\n测试用例 {i+1}:")
        try:
            result = process_user_data(name, age, email, active)
            print(f"  成功: {result}")
        except (TypeError, ValueError) as e:
            print(f"  失败: {type(e).__name__}: {e}")
    
    print("-" * 40)

def advanced_type_checking():
    """
    高级类型检查技巧
    """
    print("🎯 高级类型检查技巧")
    print("-" * 40)
    
    def process_data_structure(data, expected_structure):
        """
        处理复杂数据结构，支持嵌套类型检查
        
        Args:
            data: 要验证的数据
            expected_structure: 期望的结构描述
        """
        print(f"验证数据结构: {data}")
        print(f"期望结构: {expected_structure}")
        
        def validate_structure(value, structure, path="root"):
            """递归验证数据结构"""
            if isinstance(structure, type):
                # 简单类型检查
                if not isinstance(value, structure):
                    raise TypeError(f"路径 {path}: 期望 {structure.__name__}，但得到 {type(value).__name__}")
            
            elif isinstance(structure, dict):
                # 字典结构检查
                if not isinstance(value, dict):
                    raise TypeError(f"路径 {path}: 期望字典，但得到 {type(value).__name__}")
                
                for key, expected_type in structure.items():
                    if key not in value:
                        raise ValueError(f"路径 {path}: 缺少必需的键 '{key}'")
                    validate_structure(value[key], expected_type, f"{path}.{key}")
            
            elif isinstance(structure, list) and len(structure) == 1:
                # 列表结构检查
                if not isinstance(value, list):
                    raise TypeError(f"路径 {path}: 期望列表，但得到 {type(value).__name__}")
                
                element_type = structure[0]
                for i, item in enumerate(value):
                    validate_structure(item, element_type, f"{path}[{i}]")
            
            elif isinstance(structure, tuple):
                # 多类型选择
                if not isinstance(value, structure):
                    type_names = [t.__name__ for t in structure]
                    raise TypeError(f"路径 {path}: 期望 {' 或 '.join(type_names)}，但得到 {type(value).__name__}")
        
        try:
            validate_structure(data, expected_structure)
            print(f"  ✅ 验证通过")
            return True
        except (TypeError, ValueError) as e:
            print(f"  ❌ 验证失败: {e}")
            return False
    
    # 测试复杂数据结构
    user_structure = {
        "name": str,
        "age": int,
        "email": str,
        "addresses": [{
            "type": str,
            "street": str,
            "city": str,
            "zipcode": (str, int)  # 可以是字符串或整数
        }],
        "preferences": {
            "theme": str,
            "notifications": bool,
            "language": str
        }
    }
    
    test_data = [
        # 正确的数据
        {
            "name": "Alice",
            "age": 25,
            "email": "alice@example.com",
            "addresses": [
                {
                    "type": "home",
                    "street": "123 Main St",
                    "city": "New York",
                    "zipcode": "10001"
                }
            ],
            "preferences": {
                "theme": "dark",
                "notifications": True,
                "language": "en"
            }
        },
        # 错误的数据 - age为字符串
        {
            "name": "Bob",
            "age": "25",  # 错误类型
            "email": "bob@example.com",
            "addresses": [],
            "preferences": {
                "theme": "light",
                "notifications": False,
                "language": "zh"
            }
        },
        # 错误的数据 - 缺少必需字段
        {
            "name": "Charlie",
            "age": 30,
            "email": "charlie@example.com",
            "addresses": [
                {
                    "type": "work",
                    "street": "456 Oak Ave",
                    "city": "Boston"
                    # 缺少 zipcode
                }
            ],
            "preferences": {
                "theme": "auto",
                "notifications": True,
                "language": "fr"
            }
        }
    ]
    
    for i, data in enumerate(test_data):
        print(f"\n测试数据 {i+1}:")
        process_data_structure(data, user_structure)
    
    print("-" * 40)

# 运行基本和高级类型检查示例
basic_type_checking()
advanced_type_checking()
```

## 使用断言进行验证

### 断言的基本用法

```python
def assertion_validation():
    """
    演示使用断言进行参数验证
    """
    print("✅ 使用断言进行参数验证")
    print("-" * 40)
    
    def calculate_rectangle_area(length, width):
        """
        计算矩形面积，使用断言验证参数
        """
        print(f"计算矩形面积: length={length}, width={width}")
        
        # 使用断言进行参数验证
        assert isinstance(length, (int, float)), f"length 必须是数字，但得到 {type(length).__name__}"
        assert isinstance(width, (int, float)), f"width 必须是数字，但得到 {type(width).__name__}"
        assert length > 0, f"length 必须大于0，但得到 {length}"
        assert width > 0, f"width 必须大于0，但得到 {width}"
        
        area = length * width
        print(f"  面积: {area}")
        return area
    
    def process_student_grades(*grades):
        """
        处理学生成绩，使用断言验证
        """
        print(f"处理学生成绩: {grades}")
        
        # 验证参数数量
        assert len(grades) > 0, "至少需要一个成绩"
        assert len(grades) <= 10, f"成绩数量不能超过10个，但得到 {len(grades)} 个"
        
        # 验证每个成绩
        for i, grade in enumerate(grades):
            assert isinstance(grade, (int, float)), f"成绩 {i+1} 必须是数字，但得到 {type(grade).__name__}"
            assert 0 <= grade <= 100, f"成绩 {i+1} 必须在0-100之间，但得到 {grade}"
        
        # 计算统计信息
        average = sum(grades) / len(grades)
        max_grade = max(grades)
        min_grade = min(grades)
        
        result = {
            "grades": grades,
            "count": len(grades),
            "average": round(average, 2),
            "max": max_grade,
            "min": min_grade,
            "pass_count": sum(1 for g in grades if g >= 60)
        }
        
        print(f"  统计结果: {result}")
        return result
    
    # 测试矩形面积计算
    print("测试矩形面积计算:")
    rectangle_test_cases = [
        (5, 3),        # 正常情况
        (0, 5),        # length为0
        (-2, 3),       # 负数length
        ("5", 3),      # 字符串类型
        (5.5, 2.3),    # 浮点数
    ]
    
    for length, width in rectangle_test_cases:
        try:
            area = calculate_rectangle_area(length, width)
        except AssertionError as e:
            print(f"  断言错误: {e}")
        except Exception as e:
            print(f"  其他错误: {type(e).__name__}: {e}")
    
    print("\n测试学生成绩处理:")
    grades_test_cases = [
        (85, 92, 78, 96, 88),                    # 正常情况
        (),                                      # 空成绩
        (85, 92, 105, 78),                       # 超出范围
        (85, "92", 78),                          # 包含字符串
        tuple(range(95, 106)),                   # 超过10个成绩
        (85.5, 92.3, 78.8),                     # 浮点数成绩
    ]
    
    for grades in grades_test_cases:
        try:
            result = process_student_grades(*grades)
        except AssertionError as e:
            print(f"  断言错误: {e}")
        except Exception as e:
            print(f"  其他错误: {type(e).__name__}: {e}")
    
    print("-" * 40)

def advanced_assertion_techniques():
    """
    高级断言技巧
    """
    print("🚀 高级断言技巧")
    print("-" * 40)
    
    def create_database_connection(host, port, database, username, password, **options):
        """
        创建数据库连接，使用高级断言验证
        """
        print(f"创建数据库连接: {host}:{port}/{database}")
        
        # 复合断言
        assert isinstance(host, str) and host.strip(), "host 必须是非空字符串"
        assert isinstance(port, int) and 1 <= port <= 65535, f"port 必须是1-65535之间的整数，但得到 {port}"
        assert isinstance(database, str) and database.strip(), "database 必须是非空字符串"
        assert isinstance(username, str) and username.strip(), "username 必须是非空字符串"
        assert isinstance(password, str) and len(password) >= 8, f"password 长度必须至少8位，但得到 {len(password)} 位"
        
        # 选项验证
        valid_options = {'timeout', 'ssl_mode', 'charset', 'pool_size', 'retry_count'}
        invalid_options = set(options.keys()) - valid_options
        assert not invalid_options, f"无效的选项: {invalid_options}，有效选项: {valid_options}"
        
        # 特定选项值验证
        if 'timeout' in options:
            timeout = options['timeout']
            assert isinstance(timeout, (int, float)) and timeout > 0, f"timeout 必须是正数，但得到 {timeout}"
        
        if 'ssl_mode' in options:
            ssl_mode = options['ssl_mode']
            valid_ssl_modes = {'disable', 'allow', 'prefer', 'require'}
            assert ssl_mode in valid_ssl_modes, f"ssl_mode 必须是 {valid_ssl_modes} 之一，但得到 '{ssl_mode}'"
        
        if 'pool_size' in options:
            pool_size = options['pool_size']
            assert isinstance(pool_size, int) and 1 <= pool_size <= 100, f"pool_size 必须是1-100之间的整数，但得到 {pool_size}"
        
        # 模拟连接创建
        connection_config = {
            "host": host,
            "port": port,
            "database": database,
            "username": username,
            "password": "*" * len(password),  # 隐藏密码
            "options": options,
            "status": "connected"
        }
        
        print(f"  连接配置: {connection_config}")
        return connection_config
    
    # 测试数据库连接
    connection_test_cases = [
        # 正常情况
        {
            "host": "localhost",
            "port": 5432,
            "database": "myapp",
            "username": "user",
            "password": "password123",
            "timeout": 30,
            "ssl_mode": "prefer"
        },
        # 端口超出范围
        {
            "host": "localhost",
            "port": 70000,
            "database": "myapp",
            "username": "user",
            "password": "password123"
        },
        # 密码太短
        {
            "host": "localhost",
            "port": 5432,
            "database": "myapp",
            "username": "user",
            "password": "123"
        },
        # 无效选项
        {
            "host": "localhost",
            "port": 5432,
            "database": "myapp",
            "username": "user",
            "password": "password123",
            "invalid_option": "value"
        },
        # 无效SSL模式
        {
            "host": "localhost",
            "port": 5432,
            "database": "myapp",
            "username": "user",
            "password": "password123",
            "ssl_mode": "invalid"
        }
    ]
    
    for i, config in enumerate(connection_test_cases):
        print(f"\n连接测试 {i+1}:")
        try:
            connection = create_database_connection(**config)
        except AssertionError as e:
            print(f"  断言错误: {e}")
        except Exception as e:
            print(f"  其他错误: {type(e).__name__}: {e}")
    
    print("-" * 40)

# 运行断言验证示例
assertion_validation()
advanced_assertion_techniques()
```

## 自定义验证函数

### 创建可重用的验证函数

```python
def custom_validation_functions():
    """
    演示自定义验证函数的创建和使用
    """
    print("🛠️  自定义验证函数")
    print("-" * 40)
    
    # 基础验证函数
    def validate_email(email):
        """验证邮箱格式"""
        if not isinstance(email, str):
            raise TypeError(f"邮箱必须是字符串，但得到 {type(email).__name__}")
        
        email = email.strip().lower()
        
        if not email:
            raise ValueError("邮箱不能为空")
        
        if "@" not in email:
            raise ValueError(f"邮箱格式无效：缺少@符号 - {email}")
        
        local, domain = email.rsplit("@", 1)
        
        if not local or not domain:
            raise ValueError(f"邮箱格式无效：@符号前后不能为空 - {email}")
        
        if "." not in domain:
            raise ValueError(f"邮箱格式无效：域名必须包含点号 - {email}")
        
        # 简单的字符验证
        valid_chars = set("abcdefghijklmnopqrstuvwxyz0123456789.-_")
        if not all(c in valid_chars for c in local):
            raise ValueError(f"邮箱本地部分包含无效字符 - {email}")
        
        if not all(c in valid_chars for c in domain):
            raise ValueError(f"邮箱域名部分包含无效字符 - {email}")
        
        return email
    
    def validate_phone_number(phone):
        """验证电话号码"""
        if not isinstance(phone, str):
            raise TypeError(f"电话号码必须是字符串，但得到 {type(phone).__name__}")
        
        # 清理电话号码
        cleaned_phone = "".join(c for c in phone if c.isdigit())
        
        if not cleaned_phone:
            raise ValueError("电话号码不能为空")
        
        # 检查长度
        if len(cleaned_phone) < 10 or len(cleaned_phone) > 15:
            raise ValueError(f"电话号码长度必须在10-15位之间，但得到 {len(cleaned_phone)} 位")
        
        # 中国手机号码格式检查
        if len(cleaned_phone) == 11 and cleaned_phone.startswith('1'):
            valid_prefixes = ['13', '14', '15', '16', '17', '18', '19']
            prefix = cleaned_phone[:2]
            if prefix not in valid_prefixes:
                raise ValueError(f"无效的中国手机号码前缀: {prefix}")
        
        return cleaned_phone
    
    def validate_age(age, min_age=0, max_age=150):
        """验证年龄"""
        if not isinstance(age, int):
            raise TypeError(f"年龄必须是整数，但得到 {type(age).__name__}")
        
        if age < min_age or age > max_age:
            raise ValueError(f"年龄必须在 {min_age}-{max_age} 之间，但得到 {age}")
        
        return age
    
    def validate_password(password, min_length=8, require_uppercase=True, 
                         require_lowercase=True, require_digit=True, require_special=True):
        """验证密码强度"""
        if not isinstance(password, str):
            raise TypeError(f"密码必须是字符串，但得到 {type(password).__name__}")
        
        if len(password) < min_length:
            raise ValueError(f"密码长度必须至少 {min_length} 位，但得到 {len(password)} 位")
        
        errors = []
        
        if require_uppercase and not any(c.isupper() for c in password):
            errors.append("至少包含一个大写字母")
        
        if require_lowercase and not any(c.islower() for c in password):
            errors.append("至少包含一个小写字母")
        
        if require_digit and not any(c.isdigit() for c in password):
            errors.append("至少包含一个数字")
        
        if require_special:
            special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
            if not any(c in special_chars for c in password):
                errors.append("至少包含一个特殊字符")
        
        if errors:
            raise ValueError(f"密码不符合要求: {', '.join(errors)}")
        
        return password
    
    # 使用自定义验证函数的用户注册函数
    def register_user(name, email, phone, age, password):
        """用户注册，使用多个验证函数"""
        print(f"注册用户: {name}")
        
        try:
            # 基本类型检查
            if not isinstance(name, str) or not name.strip():
                raise ValueError("姓名不能为空")
            
            # 使用自定义验证函数
            validated_email = validate_email(email)
            validated_phone = validate_phone_number(phone)
            validated_age = validate_age(age, min_age=16, max_age=100)
            validated_password = validate_password(password)
            
            # 创建用户对象
            user = {
                "name": name.strip(),
                "email": validated_email,
                "phone": validated_phone,
                "age": validated_age,
                "password_hash": "*" * len(validated_password),  # 模拟密码哈希
                "created_at": "2024-01-01 12:00:00",
                "status": "active"
            }
            
            print(f"  ✅ 注册成功: {user}")
            return user
            
        except (TypeError, ValueError) as e:
            print(f"  ❌ 注册失败: {e}")
            return None
    
    # 测试用户注册
    test_users = [
        # 正常用户
        {
            "name": "张三",
            "email": "zhangsan@example.com",
            "phone": "13812345678",
            "age": 25,
            "password": "MyPassword123!"
        },
        # 邮箱格式错误
        {
            "name": "李四",
            "email": "invalid-email",
            "phone": "13987654321",
            "age": 30,
            "password": "MyPassword123!"
        },
        # 电话号码无效
        {
            "name": "王五",
            "email": "wangwu@example.com",
            "phone": "123",
            "age": 28,
            "password": "MyPassword123!"
        },
        # 年龄超出范围
        {
            "name": "赵六",
            "email": "zhaoliu@example.com",
            "phone": "13611111111",
            "age": 15,
            "password": "MyPassword123!"
        },
        # 密码太弱
        {
            "name": "孙七",
            "email": "sunqi@example.com",
            "phone": "13722222222",
            "age": 35,
            "password": "123456"
        }
    ]
    
    for i, user_data in enumerate(test_users):
        print(f"\n测试用户 {i+1}:")
        register_user(**user_data)
    
    print("-" * 40)

# 运行自定义验证函数示例
custom_validation_functions()
```

### 验证函数组合器

```python
def validation_combinators():
    """
    演示验证函数的组合和链式调用
    """
    print("🔗 验证函数组合器")
    print("-" * 40)
    
    class ValidationError(Exception):
        """自定义验证异常"""
        def __init__(self, field, message):
            self.field = field
            self.message = message
            super().__init__(f"{field}: {message}")
    
    class Validator:
        """验证器类，支持链式调用"""
        
        def __init__(self, field_name, value):
            self.field_name = field_name
            self.value = value
            self.errors = []
        
        def required(self, message="字段是必需的"):
            """检查字段是否为空"""
            if self.value is None or (isinstance(self.value, str) and not self.value.strip()):
                self.errors.append(message)
            return self
        
        def type_check(self, expected_type, message=None):
            """类型检查"""
            if not isinstance(self.value, expected_type):
                if message is None:
                    type_name = expected_type.__name__ if hasattr(expected_type, '__name__') else str(expected_type)
                    message = f"必须是 {type_name} 类型，但得到 {type(self.value).__name__}"
                self.errors.append(message)
            return self
        
        def min_length(self, min_len, message=None):
            """最小长度检查"""
            if hasattr(self.value, '__len__') and len(self.value) < min_len:
                if message is None:
                    message = f"长度必须至少 {min_len}，但得到 {len(self.value)}"
                self.errors.append(message)
            return self
        
        def max_length(self, max_len, message=None):
            """最大长度检查"""
            if hasattr(self.value, '__len__') and len(self.value) > max_len:
                if message is None:
                    message = f"长度不能超过 {max_len}，但得到 {len(self.value)}"
                self.errors.append(message)
            return self
        
        def range_check(self, min_val=None, max_val=None, message=None):
            """范围检查"""
            if min_val is not None and self.value < min_val:
                if message is None:
                    message = f"值不能小于 {min_val}，但得到 {self.value}"
                self.errors.append(message)
            
            if max_val is not None and self.value > max_val:
                if message is None:
                    message = f"值不能大于 {max_val}，但得到 {self.value}"
                self.errors.append(message)
            
            return self
        
        def pattern_match(self, pattern, message=None):
            """正则表达式匹配"""
            import re
            if isinstance(self.value, str) and not re.match(pattern, self.value):
                if message is None:
                    message = f"格式不匹配模式 {pattern}"
                self.errors.append(message)
            return self
        
        def custom(self, validator_func, message=None):
            """自定义验证函数"""
            try:
                if not validator_func(self.value):
                    if message is None:
                        message = "自定义验证失败"
                    self.errors.append(message)
            except Exception as e:
                self.errors.append(f"验证过程中出错: {e}")
            return self
        
        def validate(self):
            """执行验证并返回结果"""
            if self.errors:
                raise ValidationError(self.field_name, "; ".join(self.errors))
            return self.value
    
    def validate_field(field_name, value):
        """创建验证器的便捷函数"""
        return Validator(field_name, value)
    
    # 使用验证器的产品创建函数
    def create_product(name, price, category, description, stock_quantity):
        """创建产品，使用链式验证"""
        print(f"创建产品: {name}")
        
        try:
            # 链式验证
            validated_name = (validate_field("产品名称", name)
                            .required()
                            .type_check(str)
                            .min_length(2, "产品名称至少2个字符")
                            .max_length(100, "产品名称不能超过100个字符")
                            .validate())
            
            validated_price = (validate_field("价格", price)
                             .required()
                             .type_check((int, float))
                             .range_check(min_val=0.01, message="价格必须大于0")
                             .validate())
            
            validated_category = (validate_field("分类", category)
                                .required()
                                .type_check(str)
                                .custom(lambda x: x.lower() in ['electronics', 'clothing', 'books', 'home'],
                                       "分类必须是: electronics, clothing, books, home 之一")
                                .validate())
            
            validated_description = (validate_field("描述", description)
                                   .type_check(str)
                                   .max_length(500, "描述不能超过500个字符")
                                   .validate())
            
            validated_stock = (validate_field("库存数量", stock_quantity)
                             .required()
                             .type_check(int)
                             .range_check(min_val=0, message="库存数量不能为负数")
                             .validate())
            
            # 创建产品对象
            product = {
                "name": validated_name.strip(),
                "price": round(validated_price, 2),
                "category": validated_category.lower(),
                "description": validated_description.strip() if validated_description else "",
                "stock_quantity": validated_stock,
                "created_at": "2024-01-01 12:00:00",
                "status": "active"
            }
            
            print(f"  ✅ 产品创建成功: {product}")
            return product
            
        except ValidationError as e:
            print(f"  ❌ 验证失败: {e}")
            return None
    
    # 测试产品创建
    test_products = [
        # 正常产品
        {
            "name": "iPhone 15",
            "price": 999.99,
            "category": "electronics",
            "description": "最新款iPhone手机",
            "stock_quantity": 50
        },
        # 名称太短
        {
            "name": "A",
            "price": 29.99,
            "category": "books",
            "description": "一本好书",
            "stock_quantity": 100
        },
        # 价格为负数
        {
            "name": "T恤衫",
            "price": -10.00,
            "category": "clothing",
            "description": "舒适的T恤",
            "stock_quantity": 25
        },
        # 无效分类
        {
            "name": "沙发",
            "price": 599.99,
            "category": "furniture",
            "description": "舒适的沙发",
            "stock_quantity": 5
        },
        # 描述太长
        {
            "name": "笔记本电脑",
            "price": 1299.99,
            "category": "electronics",
            "description": "这是一个" + "非常" * 100 + "长的描述",
            "stock_quantity": 10
        }
    ]
    
    for i, product_data in enumerate(test_products):
        print(f"\n测试产品 {i+1}:")
        create_product(**product_data)
    
    print("-" * 40)

# 运行验证函数组合器示例
validation_combinators()
```