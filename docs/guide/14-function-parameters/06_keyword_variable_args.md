# 关键字可变参数 (**kwargs)

关键字可变参数（**kwargs）是Python函数中另一个强大的特性，它允许函数接受任意数量的关键字参数。与*args处理位置参数不同，**kwargs专门处理命名参数，为函数设计提供了更高的灵活性和可读性。

## 核心概念

### 什么是**kwargs？
**kwargs是一个特殊的参数语法，它可以接收任意数量的关键字参数，并将它们打包成一个字典（dict）。"kwargs"是"keyword arguments"的缩写，你可以使用任何名称，关键是前面的双星号（**）。

### 特点
- **字典形式**：参数被打包成字典
- **命名参数**：每个参数都有名称和值
- **无序性**：字典中的键值对没有固定顺序（Python 3.7+保持插入顺序）
- **类型灵活**：值可以是任何类型

## 基础用法

### 简单的**kwargs使用

```python
def print_all_kwargs(**kwargs):
    """
    打印所有传入的关键字参数
    
    Args:
        **kwargs: 任意数量的关键字参数
    """
    print(f"参数类型: {type(kwargs)}")
    print(f"参数数量: {len(kwargs)}")
    print(f"参数内容: {kwargs}")
    
    if kwargs:
        print("详细参数:")
        for key, value in kwargs.items():
            print(f"  {key}: {value} (类型: {type(value).__name__})")
    else:
        print("没有关键字参数")
    
    print("-" * 40)

# 不同的调用方式
print_all_kwargs()
print_all_kwargs(name="Alice")
print_all_kwargs(name="Bob", age=25, city="Beijing")
print_all_kwargs(x=1, y=2.5, active=True, items=[1, 2, 3])
```

### 与普通参数组合使用

```python
def create_user_profile(username, email, **additional_info):
    """
    创建用户档案
    
    Args:
        username: 用户名（必需）
        email: 邮箱（必需）
        **additional_info: 额外的用户信息
    """
    profile = {
        "username": username,
        "email": email
    }
    
    # 添加额外信息
    profile.update(additional_info)
    
    print(f"创建用户档案: {username}")
    print(f"基本信息:")
    print(f"  用户名: {username}")
    print(f"  邮箱: {email}")
    
    if additional_info:
        print(f"额外信息:")
        for key, value in additional_info.items():
            print(f"  {key}: {value}")
    
    print(f"完整档案: {profile}")
    print("-" * 40)
    
    return profile

# 不同的调用方式
create_user_profile("john_doe", "john@example.com")
create_user_profile("alice", "alice@example.com", age=28, city="Shanghai")
create_user_profile(
    "bob", "bob@example.com", 
    age=32, city="Guangzhou", 
    department="Engineering", 
    level="Senior",
    skills=["Python", "JavaScript", "SQL"]
)
```

## 实际应用示例

### 配置选项处理

```python
def configure_database(host, port, **options):
    """
    配置数据库连接
    
    Args:
        host: 数据库主机
        port: 端口号
        **options: 其他配置选项
    """
    config = {
        "host": host,
        "port": port,
        "timeout": options.get("timeout", 30),
        "max_connections": options.get("max_connections", 10),
        "ssl_enabled": options.get("ssl_enabled", False),
        "charset": options.get("charset", "utf8"),
        "autocommit": options.get("autocommit", True)
    }
    
    # 添加其他自定义选项
    for key, value in options.items():
        if key not in config:
            config[key] = value
    
    print(f"数据库配置:")
    print(f"  主机: {host}:{port}")
    print(f"  基本配置:")
    for key, value in config.items():
        if key not in ["host", "port"]:
            print(f"    {key}: {value}")
    
    print("-" * 40)
    return config

def setup_web_server(name, **settings):
    """
    设置Web服务器
    
    Args:
        name: 服务器名称
        **settings: 服务器设置
    """
    default_settings = {
        "debug": False,
        "host": "localhost",
        "port": 8000,
        "workers": 4,
        "log_level": "INFO",
        "static_folder": "static",
        "template_folder": "templates"
    }
    
    # 合并默认设置和用户设置
    final_settings = {**default_settings, **settings}
    
    print(f"Web服务器配置: {name}")
    print(f"设置项:")
    for key, value in final_settings.items():
        print(f"  {key}: {value}")
    
    print("-" * 40)
    return final_settings

# 配置示例
configure_database("localhost", 5432)
configure_database(
    "prod-db.example.com", 5432,
    timeout=60, max_connections=50, ssl_enabled=True,
    backup_enabled=True, monitoring=True
)

setup_web_server("MyApp")
setup_web_server(
    "ProductionApp",
    debug=False, host="0.0.0.0", port=80,
    workers=8, log_level="WARNING",
    cors_enabled=True, rate_limiting=True
)
```

### 与*args组合使用

```python
def flexible_function(required_param, *args, **kwargs):
    """
    同时使用*args和**kwargs的灵活函数
    
    Args:
        required_param: 必需参数
        *args: 可变位置参数
        **kwargs: 可变关键字参数
    """
    print(f"必需参数: {required_param}")
    print(f"位置参数数量: {len(args)}")
    print(f"位置参数: {args}")
    print(f"关键字参数数量: {len(kwargs)}")
    print(f"关键字参数: {kwargs}")
    
    # 处理所有参数
    all_values = [required_param] + list(args) + list(kwargs.values())
    print(f"所有参数值: {all_values}")
    print("-" * 40)
    
    return {
        "required": required_param,
        "args": args,
        "kwargs": kwargs,
        "all_values": all_values
    }

def calculate_with_options(operation, *numbers, **options):
    """
    带选项的计算函数
    
    Args:
        operation: 操作类型
        *numbers: 要计算的数字
        **options: 计算选项
    """
    print(f"操作: {operation}")
    print(f"数字: {numbers}")
    print(f"选项: {options}")
    
    if not numbers:
        print("没有提供数字")
        return None
    
    # 根据操作类型计算
    if operation == "sum":
        result = sum(numbers)
    elif operation == "product":
        result = 1
        for num in numbers:
            result *= num
    elif operation == "average":
        result = sum(numbers) / len(numbers)
    elif operation == "max":
        result = max(numbers)
    elif operation == "min":
        result = min(numbers)
    else:
        print(f"不支持的操作: {operation}")
        return None
    
    # 应用选项
    if options.get("round_result"):
        digits = options.get("decimal_places", 2)
        result = round(result, digits)
    
    if options.get("absolute"):
        result = abs(result)
    
    if options.get("format_as_string"):
        result = f"{result:,.2f}"
    
    print(f"计算结果: {result}")
    print("-" * 40)
    
    return result

# 灵活函数示例
flexible_function("必需值", 1, 2, 3, name="Alice", age=25)

# 计算函数示例
calculate_with_options("sum", 1, 2, 3, 4, 5)
calculate_with_options(
    "average", 10, 20, 30, 40,
    round_result=True, decimal_places=1
)
calculate_with_options(
    "product", 2, 3, 4,
    format_as_string=True
)
```

### API包装函数

```python
def make_api_request(endpoint, method="GET", **params):
    """
    模拟API请求
    
    Args:
        endpoint: API端点
        method: HTTP方法
        **params: 请求参数
    """
    print(f"API请求: {method} {endpoint}")
    
    # 分离不同类型的参数
    headers = params.pop("headers", {})
    data = params.pop("data", {})
    query_params = params.pop("params", {})
    
    # 其余参数作为配置选项
    config = params
    
    print(f"请求头: {headers}")
    print(f"请求数据: {data}")
    print(f"查询参数: {query_params}")
    print(f"配置选项: {config}")
    
    # 模拟响应
    response = {
        "status": 200,
        "data": f"Response from {endpoint}",
        "method": method,
        "request_params": {
            "headers": headers,
            "data": data,
            "params": query_params,
            "config": config
        }
    }
    
    print(f"响应: {response['status']} - {response['data']}")
    print("-" * 40)
    
    return response

def send_notification(message, **options):
    """
    发送通知
    
    Args:
        message: 通知消息
        **options: 通知选项
    """
    notification = {
        "message": message,
        "timestamp": "2024-01-01 12:00:00",
        "type": options.get("type", "info"),
        "priority": options.get("priority", "normal"),
        "channels": options.get("channels", ["email"]),
        "recipients": options.get("recipients", []),
        "template": options.get("template", "default"),
        "attachments": options.get("attachments", []),
        "retry_count": options.get("retry_count", 3),
        "delay_seconds": options.get("delay_seconds", 0)
    }
    
    # 添加自定义选项
    for key, value in options.items():
        if key not in notification:
            notification[f"custom_{key}"] = value
    
    print(f"发送通知: {message}")
    print(f"通知配置:")
    for key, value in notification.items():
        if key != "message":
            print(f"  {key}: {value}")
    
    print("-" * 40)
    return notification

# API请求示例
make_api_request("/users")
make_api_request(
    "/users", "POST",
    headers={"Authorization": "Bearer token123"},
    data={"name": "Alice", "email": "alice@example.com"},
    timeout=30, verify_ssl=True
)

# 通知示例
send_notification("系统维护通知")
send_notification(
    "重要安全更新",
    type="warning", priority="high",
    channels=["email", "sms", "push"],
    recipients=["admin@example.com", "security@example.com"],
    template="security_alert",
    retry_count=5,
    urgent=True, department="IT"
)
```

### 数据过滤和处理

```python
def filter_data(data, **filters):
    """
    根据条件过滤数据
    
    Args:
        data: 要过滤的数据列表
        **filters: 过滤条件
    """
    print(f"原始数据数量: {len(data)}")
    print(f"过滤条件: {filters}")
    
    filtered_data = data.copy()
    
    for key, value in filters.items():
        if key == "min_value":
            filtered_data = [item for item in filtered_data 
                           if isinstance(item, (int, float)) and item >= value]
            print(f"  应用最小值过滤 >= {value}: 剩余 {len(filtered_data)} 项")
        
        elif key == "max_value":
            filtered_data = [item for item in filtered_data 
                           if isinstance(item, (int, float)) and item <= value]
            print(f"  应用最大值过滤 <= {value}: 剩余 {len(filtered_data)} 项")
        
        elif key == "contains":
            filtered_data = [item for item in filtered_data 
                           if isinstance(item, str) and value in item]
            print(f"  应用包含过滤 '{value}': 剩余 {len(filtered_data)} 项")
        
        elif key == "type_filter":
            filtered_data = [item for item in filtered_data 
                           if isinstance(item, value)]
            print(f"  应用类型过滤 {value.__name__}: 剩余 {len(filtered_data)} 项")
        
        elif key == "length_min":
            filtered_data = [item for item in filtered_data 
                           if hasattr(item, '__len__') and len(item) >= value]
            print(f"  应用最小长度过滤 >= {value}: 剩余 {len(filtered_data)} 项")
        
        elif key == "custom_filter" and callable(value):
            filtered_data = [item for item in filtered_data if value(item)]
            print(f"  应用自定义过滤: 剩余 {len(filtered_data)} 项")
    
    print(f"最终结果: {filtered_data}")
    print("-" * 40)
    
    return filtered_data

def transform_data(data, **transformations):
    """
    转换数据
    
    Args:
        data: 要转换的数据
        **transformations: 转换选项
    """
    print(f"原始数据: {data}")
    print(f"转换选项: {transformations}")
    
    result = data.copy() if isinstance(data, list) else data
    
    # 应用转换
    if transformations.get("to_uppercase") and isinstance(result, list):
        result = [item.upper() if isinstance(item, str) else item for item in result]
        print(f"  转换为大写: {result}")
    
    if transformations.get("multiply_numbers"):
        factor = transformations["multiply_numbers"]
        if isinstance(result, list):
            result = [item * factor if isinstance(item, (int, float)) else item 
                     for item in result]
        elif isinstance(result, (int, float)):
            result = result * factor
        print(f"  数字乘以 {factor}: {result}")
    
    if transformations.get("add_prefix"):
        prefix = transformations["add_prefix"]
        if isinstance(result, list):
            result = [f"{prefix}{item}" if isinstance(item, str) else item 
                     for item in result]
        elif isinstance(result, str):
            result = f"{prefix}{result}"
        print(f"  添加前缀 '{prefix}': {result}")
    
    if transformations.get("sort_data"):
        if isinstance(result, list):
            try:
                result.sort(reverse=transformations.get("reverse_sort", False))
                print(f"  排序数据: {result}")
            except TypeError:
                print("  排序失败: 数据类型不一致")
    
    if transformations.get("unique_only"):
        if isinstance(result, list):
            result = list(set(result))
            print(f"  去重处理: {result}")
    
    print(f"最终结果: {result}")
    print("-" * 40)
    
    return result

# 数据过滤示例
test_data = [1, 5, "hello", 10, "world", 3.14, "python", 20, [1, 2, 3]]

filter_data(test_data, min_value=5, type_filter=int)
filter_data(test_data, contains="o", length_min=4)
filter_data(test_data, custom_filter=lambda x: isinstance(x, str) and len(x) > 4)

# 数据转换示例
string_data = ["hello", "world", "python"]
number_data = [1, 2, 3, 4, 5]

transform_data(string_data, to_uppercase=True, add_prefix=">>> ")
transform_data(number_data, multiply_numbers=2, sort_data=True, reverse_sort=True)
```

### 装饰器应用

```python
def advanced_decorator(**decorator_options):
    """
    高级装饰器，支持配置选项
    
    Args:
        **decorator_options: 装饰器选项
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 装饰器配置
            log_calls = decorator_options.get("log_calls", False)
            measure_time = decorator_options.get("measure_time", False)
            validate_args = decorator_options.get("validate_args", False)
            cache_result = decorator_options.get("cache_result", False)
            
            if log_calls:
                print(f"📞 调用函数: {func.__name__}")
                print(f"   参数: args={args}, kwargs={kwargs}")
            
            if validate_args:
                required_types = decorator_options.get("arg_types", [])
                if required_types and args:
                    for i, (arg, expected_type) in enumerate(zip(args, required_types)):
                        if not isinstance(arg, expected_type):
                            raise TypeError(
                                f"参数 {i+1} 应该是 {expected_type.__name__}, "
                                f"但得到 {type(arg).__name__}"
                            )
            
            # 执行函数
            if measure_time:
                import time
                start_time = time.time()
            
            result = func(*args, **kwargs)
            
            if measure_time:
                end_time = time.time()
                execution_time = end_time - start_time
                print(f"⏱️  执行时间: {execution_time:.4f} 秒")
            
            if log_calls:
                print(f"✅ 函数 {func.__name__} 执行完成")
                print(f"   返回值: {result}")
            
            print("-" * 40)
            return result
        
        return wrapper
    return decorator

def retry_decorator(**retry_options):
    """
    重试装饰器
    
    Args:
        **retry_options: 重试选项
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            max_retries = retry_options.get("max_retries", 3)
            delay = retry_options.get("delay", 1)
            exceptions = retry_options.get("exceptions", (Exception,))
            
            for attempt in range(max_retries + 1):
                try:
                    if attempt > 0:
                        print(f"🔄 重试第 {attempt} 次: {func.__name__}")
                        import time
                        time.sleep(delay)
                    
                    result = func(*args, **kwargs)
                    
                    if attempt > 0:
                        print(f"✅ 重试成功")
                    
                    return result
                
                except exceptions as e:
                    if attempt == max_retries:
                        print(f"❌ 重试失败，已达到最大重试次数 {max_retries}")
                        raise e
                    else:
                        print(f"⚠️  尝试 {attempt + 1} 失败: {e}")
            
            print("-" * 40)
        
        return wrapper
    return decorator

# 使用装饰器
@advanced_decorator(
    log_calls=True, 
    measure_time=True, 
    validate_args=True,
    arg_types=[int, int]
)
def add_numbers(a, b):
    """加法函数"""
    return a + b

@retry_decorator(max_retries=2, delay=0.1)
def unreliable_function(success_rate=0.7):
    """模拟不稳定的函数"""
    import random
    if random.random() < success_rate:
        return "成功执行"
    else:
        raise Exception("随机失败")

# 装饰器示例
add_numbers(5, 3)

# 重试示例（可能需要多次运行才能看到重试效果）
try:
    unreliable_function(0.3)  # 低成功率，更容易触发重试
except Exception as e:
    print(f"最终失败: {e}")
```

### 配置类和构建器模式

```python
class ConfigBuilder:
    """
    配置构建器类，使用**kwargs构建配置
    """
    
    def __init__(self, **initial_config):
        self.config = initial_config.copy()
        print(f"初始化配置构建器")
        if initial_config:
            print(f"初始配置: {initial_config}")
        print("-" * 40)
    
    def add_database_config(self, **db_config):
        """添加数据库配置"""
        self.config["database"] = db_config
        print(f"添加数据库配置: {db_config}")
        return self
    
    def add_cache_config(self, **cache_config):
        """添加缓存配置"""
        self.config["cache"] = cache_config
        print(f"添加缓存配置: {cache_config}")
        return self
    
    def add_logging_config(self, **log_config):
        """添加日志配置"""
        self.config["logging"] = log_config
        print(f"添加日志配置: {log_config}")
        return self
    
    def add_custom_section(self, section_name, **section_config):
        """添加自定义配置段"""
        self.config[section_name] = section_config
        print(f"添加自定义配置段 '{section_name}': {section_config}")
        return self
    
    def update_config(self, **updates):
        """更新配置"""
        self.config.update(updates)
        print(f"更新配置: {updates}")
        return self
    
    def build(self):
        """构建最终配置"""
        print(f"构建最终配置:")
        for section, config in self.config.items():
            print(f"  {section}: {config}")
        print("-" * 40)
        return self.config.copy()

class DynamicObject:
    """
    动态对象类，可以接受任意属性
    """
    
    def __init__(self, **attributes):
        print(f"创建动态对象")
        print(f"属性: {attributes}")
        
        # 设置属性
        for key, value in attributes.items():
            setattr(self, key, value)
            print(f"  设置属性 {key} = {value}")
        
        print("-" * 40)
    
    def update_attributes(self, **new_attributes):
        """更新属性"""
        print(f"更新属性: {new_attributes}")
        
        for key, value in new_attributes.items():
            old_value = getattr(self, key, "<未设置>")
            setattr(self, key, value)
            print(f"  {key}: {old_value} -> {value}")
        
        print("-" * 40)
        return self
    
    def get_all_attributes(self):
        """获取所有属性"""
        attributes = {key: value for key, value in self.__dict__.items() 
                     if not key.startswith('_')}
        print(f"所有属性: {attributes}")
        print("-" * 40)
        return attributes

# 配置构建器示例
config = (ConfigBuilder(app_name="MyApp", version="1.0")
          .add_database_config(host="localhost", port=5432, name="mydb")
          .add_cache_config(type="redis", host="localhost", port=6379)
          .add_logging_config(level="INFO", file="app.log")
          .add_custom_section("security", encryption=True, auth_required=True)
          .update_config(debug=False, max_workers=4)
          .build())

# 动态对象示例
obj = DynamicObject(
    name="测试对象",
    value=42,
    active=True,
    tags=["test", "demo"]
)

obj.update_attributes(
    value=100,
    description="这是一个测试对象",
    created_at="2024-01-01"
)

obj.get_all_attributes()
```

## 注意事项和最佳实践

### 1. 参数顺序规则

```python
# 正确的参数顺序
def correct_parameter_order(pos_arg, *args, kw_only_arg=None, **kwargs):
    """
    正确的参数顺序：
    1. 位置参数
    2. *args
    3. 仅关键字参数
    4. **kwargs
    """
    print(f"位置参数: {pos_arg}")
    print(f"可变位置参数: {args}")
    print(f"仅关键字参数: {kw_only_arg}")
    print(f"可变关键字参数: {kwargs}")
    print("-" * 40)

# 使用示例
correct_parameter_order(
    "必需值", 1, 2, 3,
    kw_only_arg="仅关键字",
    extra1="额外参数1", extra2="额外参数2"
)
```

### 2. 字典解包和合并

```python
def demonstrate_dict_operations(**kwargs):
    """
    演示字典操作技巧
    
    Args:
        **kwargs: 关键字参数
    """
    print(f"接收到的参数: {kwargs}")
    
    # 默认配置
    defaults = {
        "timeout": 30,
        "retries": 3,
        "debug": False
    }
    
    # 方法1: 使用update()
    config1 = defaults.copy()
    config1.update(kwargs)
    print(f"方法1 (update): {config1}")
    
    # 方法2: 使用字典解包
    config2 = {**defaults, **kwargs}
    print(f"方法2 (解包): {config2}")
    
    # 方法3: 使用字典推导式过滤
    filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
    config3 = {**defaults, **filtered_kwargs}
    print(f"方法3 (过滤): {config3}")
    
    print("-" * 40)
    return config3

# 字典操作示例
demonstrate_dict_operations(
    timeout=60, debug=True, 
    custom_option="value", none_value=None
)
```

### 3. 类型提示

```python
from typing import Any, Dict, Optional

def typed_kwargs_function(name: str, **options: Any) -> Dict[str, Any]:
    """
    带类型提示的**kwargs函数
    
    Args:
        name: 名称
        **options: 选项字典
    
    Returns:
        处理结果
    """
    result = {"name": name, "options": options}
    print(f"类型提示函数结果: {result}")
    return result

def specific_typed_kwargs(required: int, **config: str) -> Dict[str, Any]:
    """
    特定类型的**kwargs
    
    Args:
        required: 必需的整数参数
        **config: 字符串配置选项
    
    Returns:
        配置结果
    """
    # 验证所有kwargs都是字符串
    for key, value in config.items():
        if not isinstance(value, str):
            print(f"警告: {key} 的值不是字符串: {value}")
    
    result = {"required": required, "config": config}
    print(f"特定类型函数结果: {result}")
    return result

# 类型提示示例
typed_kwargs_function("test", option1="value1", option2=42)
specific_typed_kwargs(100, host="localhost", port="8080", debug="true")
```

## 运行示例

要运行这些示例，请使用以下命令：

```bash
python3 05_keyword_variable_args.py
```

## 学习要点

1. **字典特性**：**kwargs将参数打包成字典
2. **命名参数**：提供更好的可读性和灵活性
3. **参数顺序**：**kwargs必须在参数列表的最后
4. **字典操作**：熟练使用字典合并和解包技巧
5. **配置模式**：适用于配置选项、API参数等场景
6. **组合使用**：与*args结合使用提供最大灵活性
7. **类型提示**：合理使用类型提示提高代码质量
8. **实际应用**：装饰器、配置管理、API包装等

## 下一步

掌握了**kwargs后，接下来学习[参数组合使用](07_parameter_combinations.md)，了解如何在一个函数中组合使用各种参数类型。