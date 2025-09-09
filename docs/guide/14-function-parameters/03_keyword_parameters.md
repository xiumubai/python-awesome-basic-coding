# 关键字参数 (Keyword Parameters)

关键字参数允许你在调用函数时通过参数名来指定参数值，而不依赖于参数的位置顺序。这种方式大大提高了代码的可读性和灵活性，是Python函数调用的重要特性。

## 核心概念

### 什么是关键字参数？
关键字参数是通过参数名=值的形式传递给函数的参数。调用时可以不按照定义时的顺序，只要指定了正确的参数名即可。

### 特点
- **顺序无关**：可以任意调整参数顺序
- **提高可读性**：明确显示每个值对应的参数
- **减少错误**：避免因位置错误导致的参数混淆
- **灵活性强**：可以只传递部分参数（配合默认参数）

## 基础用法

### 基本关键字参数

```python
def introduce_person(name, age, city):
    """
    介绍一个人的基本信息
    
    Args:
        name: 姓名
        age: 年龄
        city: 城市
    """
    print(f"大家好，我是{name}，今年{age}岁，来自{city}。")

# 使用关键字参数调用（顺序可以改变）
introduce_person(name="小明", age=25, city="北京")
introduce_person(city="上海", name="小红", age=23)
introduce_person(age=30, city="广州", name="小李")

# 输出:
# 大家好，我是小明，今年25岁，来自北京。
# 大家好，我是小红，今年23岁，来自上海。
# 大家好，我是小李，今年30岁，来自广州。
```

### 混合使用位置参数和关键字参数

```python
def create_profile(name, age, email=None, phone=None):
    """
    创建用户档案
    
    Args:
        name: 姓名（必需）
        age: 年龄（必需）
        email: 邮箱（可选）
        phone: 电话（可选）
    """
    profile = f"姓名: {name}, 年龄: {age}"
    if email:
        profile += f", 邮箱: {email}"
    if phone:
        profile += f", 电话: {phone}"
    
    print(profile)
    return profile

# 混合使用位置参数和关键字参数
create_profile("张三", 28)  # 只使用位置参数
create_profile("李四", 32, email="lisi@example.com")  # 位置参数 + 关键字参数
create_profile("王五", 25, phone="13800138000", email="wangwu@example.com")  # 位置参数 + 多个关键字参数

# 输出:
# 姓名: 张三, 年龄: 28
# 姓名: 李四, 年龄: 32, 邮箱: lisi@example.com
# 姓名: 王五, 年龄: 25, 邮箱: wangwu@example.com, 电话: 13800138000
```

## 实际应用示例

### 复杂配置函数

```python
def setup_database_connection(host, port, database, username, password, 
                             timeout=30, ssl=False, charset='utf8'):
    """
    设置数据库连接
    
    Args:
        host: 数据库主机地址
        port: 端口号
        database: 数据库名
        username: 用户名
        password: 密码
        timeout: 连接超时时间（秒）
        ssl: 是否使用SSL连接
        charset: 字符编码
    """
    config = {
        'host': host,
        'port': port,
        'database': database,
        'username': username,
        'password': password,
        'timeout': timeout,
        'ssl': ssl,
        'charset': charset
    }
    
    print("数据库连接配置:")
    for key, value in config.items():
        if key == 'password':
            print(f"  {key}: {'*' * len(str(value))}")
        else:
            print(f"  {key}: {value}")
    
    return config

# 使用关键字参数，提高可读性
db_config = setup_database_connection(
    host="localhost",
    port=3306,
    database="myapp",
    username="admin",
    password="secret123",
    timeout=60,
    ssl=True
)

# 输出:
# 数据库连接配置:
#   host: localhost
#   port: 3306
#   database: myapp
#   username: admin
#   password: *********
#   timeout: 60
#   ssl: True
#   charset: utf8
```

### API调用函数

```python
def make_api_request(url, method='GET', headers=None, params=None, 
                    data=None, timeout=10, verify_ssl=True):
    """
    模拟API请求函数
    
    Args:
        url: 请求URL
        method: HTTP方法
        headers: 请求头
        params: URL参数
        data: 请求数据
        timeout: 超时时间
        verify_ssl: 是否验证SSL证书
    """
    print(f"发送 {method} 请求到: {url}")
    
    if headers:
        print(f"请求头: {headers}")
    
    if params:
        print(f"URL参数: {params}")
    
    if data:
        print(f"请求数据: {data}")
    
    print(f"超时时间: {timeout}秒")
    print(f"SSL验证: {'开启' if verify_ssl else '关闭'}")
    print("-" * 40)

# 不同的调用方式
# 简单GET请求
make_api_request(url="https://api.example.com/users")

# POST请求with数据
make_api_request(
    url="https://api.example.com/users",
    method="POST",
    headers={"Content-Type": "application/json"},
    data={"name": "新用户", "email": "user@example.com"}
)

# 带参数的GET请求
make_api_request(
    url="https://api.example.com/search",
    params={"q": "python", "limit": 10},
    timeout=30
)
```

### 文件操作函数

```python
def process_file(filename, operation='read', encoding='utf-8', 
                backup=False, create_if_missing=False):
    """
    处理文件的通用函数
    
    Args:
        filename: 文件名
        operation: 操作类型 ('read', 'write', 'append')
        encoding: 文件编码
        backup: 是否创建备份
        create_if_missing: 如果文件不存在是否创建
    """
    import os
    
    print(f"处理文件: {filename}")
    print(f"操作类型: {operation}")
    print(f"编码格式: {encoding}")
    print(f"创建备份: {'是' if backup else '否'}")
    print(f"自动创建: {'是' if create_if_missing else '否'}")
    
    # 检查文件是否存在
    if not os.path.exists(filename):
        if create_if_missing and operation in ['write', 'append']:
            print(f"文件不存在，将创建新文件: {filename}")
        elif operation == 'read':
            print(f"警告: 文件 {filename} 不存在")
            return None
    
    # 创建备份
    if backup and os.path.exists(filename):
        backup_name = f"{filename}.backup"
        print(f"创建备份文件: {backup_name}")
    
    print(f"文件处理完成")
    print("-" * 40)

# 不同的使用场景
# 简单读取
process_file("data.txt")

# 写入文件，创建备份
process_file(
    filename="config.ini",
    operation="write",
    backup=True,
    create_if_missing=True
)

# 追加内容，指定编码
process_file(
    filename="log.txt",
    operation="append",
    encoding="utf-8",
    create_if_missing=True
)
```

### 数据验证函数

```python
def validate_user_input(data, required_fields=None, field_types=None, 
                        min_lengths=None, max_lengths=None, 
                        custom_validators=None):
    """
    验证用户输入数据
    
    Args:
        data: 要验证的数据字典
        required_fields: 必需字段列表
        field_types: 字段类型要求
        min_lengths: 字段最小长度要求
        max_lengths: 字段最大长度要求
        custom_validators: 自定义验证函数
    """
    errors = []
    
    print(f"验证数据: {data}")
    
    # 检查必需字段
    if required_fields:
        for field in required_fields:
            if field not in data or not data[field]:
                errors.append(f"缺少必需字段: {field}")
    
    # 检查字段类型
    if field_types:
        for field, expected_type in field_types.items():
            if field in data and not isinstance(data[field], expected_type):
                errors.append(f"字段 {field} 类型错误，期望 {expected_type.__name__}")
    
    # 检查最小长度
    if min_lengths:
        for field, min_len in min_lengths.items():
            if field in data and len(str(data[field])) < min_len:
                errors.append(f"字段 {field} 长度不足，最少需要 {min_len} 个字符")
    
    # 检查最大长度
    if max_lengths:
        for field, max_len in max_lengths.items():
            if field in data and len(str(data[field])) > max_len:
                errors.append(f"字段 {field} 长度超限，最多允许 {max_len} 个字符")
    
    # 自定义验证
    if custom_validators:
        for field, validator in custom_validators.items():
            if field in data:
                try:
                    if not validator(data[field]):
                        errors.append(f"字段 {field} 自定义验证失败")
                except Exception as e:
                    errors.append(f"字段 {field} 验证出错: {str(e)}")
    
    if errors:
        print("验证失败:")
        for error in errors:
            print(f"  - {error}")
        return False, errors
    else:
        print("验证通过")
        return True, []
    
    print("-" * 40)

# 使用示例
user_data = {
    "username": "john_doe",
    "email": "john@example.com",
    "age": 25,
    "password": "123456"
}

# 邮箱验证函数
def is_valid_email(email):
    return "@" in email and "." in email

# 密码强度验证
def is_strong_password(password):
    return len(password) >= 8 and any(c.isdigit() for c in password)

# 复杂验证
validate_user_input(
    data=user_data,
    required_fields=["username", "email", "password"],
    field_types={"username": str, "age": int, "email": str},
    min_lengths={"username": 3, "password": 8},
    max_lengths={"username": 20},
    custom_validators={
        "email": is_valid_email,
        "password": is_strong_password
    }
)
```

## 注意事项和最佳实践

### 1. 参数顺序规则

```python
# 正确：位置参数必须在关键字参数之前
def good_function(pos_arg1, pos_arg2, keyword_arg1=None, keyword_arg2=None):
    pass

# 调用时的规则
good_function("value1", "value2", keyword_arg1="kw1")  # 正确
good_function("value1", "value2", keyword_arg2="kw2", keyword_arg1="kw1")  # 正确

# 错误示例
# good_function("value1", keyword_arg1="kw1", "value2")  # 语法错误！
```

### 2. 避免参数名冲突

```python
def process_data(data, format='json', output='file'):
    """
    处理数据
    
    注意：避免使用Python内置函数名作为参数名
    如：list, dict, str, int, type等
    """
    print(f"处理数据: {data}")
    print(f"格式: {format}")
    print(f"输出: {output}")

# 好的调用方式
process_data([1, 2, 3], format='csv', output='console')
```

### 3. 使用有意义的参数名

```python
# 好的做法：参数名清晰明了
def send_notification(recipient_email, subject, message_body, 
                     priority='normal', send_immediately=True):
    """发送通知 - 参数名清晰易懂"""
    pass

# 不好的做法：参数名模糊
def send_notification_bad(e, s, m, p='normal', si=True):
    """参数名不清晰"""
    pass
```

### 4. 合理使用默认值

```python
def create_connection(host, port, username, password, 
                     timeout=30, retries=3, ssl_enabled=False):
    """
    创建连接 - 合理的默认值设置
    
    常用的参数设置默认值，不常用的参数要求明确指定
    """
    connection_info = {
        'host': host,
        'port': port,
        'username': username,
        'password': '***',  # 不显示密码
        'timeout': timeout,
        'retries': retries,
        'ssl_enabled': ssl_enabled
    }
    
    print("连接配置:")
    for key, value in connection_info.items():
        print(f"  {key}: {value}")
    
    return connection_info

# 使用默认值
create_connection(
    host="localhost",
    port=5432,
    username="admin",
    password="secret"
)

# 覆盖默认值
create_connection(
    host="remote.server.com",
    port=5432,
    username="user",
    password="password",
    timeout=60,
    ssl_enabled=True
)
```

## 运行示例

要运行这些示例，请使用以下命令：

```bash
python3 02_keyword_parameters.py
```

## 学习要点

1. **提高可读性**：关键字参数让代码更容易理解
2. **增加灵活性**：可以任意调整参数顺序
3. **减少错误**：避免位置参数的混淆
4. **遵循顺序规则**：位置参数必须在关键字参数之前
5. **选择有意义的参数名**：让代码自文档化
6. **合理设置默认值**：简化常见用法

## 下一步

掌握了关键字参数后，接下来学习[默认参数](04_default_parameters.md)，了解如何为参数设置默认值，进一步简化函数调用。