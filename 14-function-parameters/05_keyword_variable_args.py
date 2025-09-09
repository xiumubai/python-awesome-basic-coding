#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
关键字可变参数 **kwargs (Keyword Variable Arguments)

**kwargs允许函数接受任意数量的关键字参数，这些参数会被收集到一个字典中。
这为函数提供了处理不确定关键字参数的能力，常用于配置选项、API包装等场景。

学习目标：
1. 理解**kwargs的概念和作用
2. 掌握**kwargs的定义和使用方法
3. 学会**kwargs与其他参数类型的组合使用
4. 了解**kwargs的实际应用场景
"""

# 1. 基本的**kwargs使用
def print_info(**kwargs):
    """
    打印任意关键字参数信息
    
    参数:
        **kwargs: 任意数量的关键字参数
    """
    print(f"接收到的关键字参数: {kwargs}")
    print(f"参数类型: {type(kwargs)}")
    print(f"参数数量: {len(kwargs)}")
    
    if not kwargs:
        print("没有提供关键字参数")
    else:
        print("参数详情:")
        for key, value in kwargs.items():
            print(f"  {key}: {value} (类型: {type(value).__name__})")
    
    print("-" * 30)

# 2. **kwargs与普通参数组合
def create_user(username, email, **kwargs):
    """
    创建用户，支持额外的可选属性
    
    参数:
        username (str): 用户名（必需）
        email (str): 邮箱（必需）
        **kwargs: 其他用户属性
    
    返回:
        dict: 用户信息字典
    """
    # 基本用户信息
    user = {
        'username': username,
        'email': email
    }
    
    # 添加额外属性
    user.update(kwargs)
    
    print(f"创建用户: {username}")
    print(f"基本信息: 用户名={username}, 邮箱={email}")
    
    if kwargs:
        print("额外属性:")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")
    
    print(f"完整用户信息: {user}")
    print("-" * 30)
    return user

# 3. **kwargs用于配置选项
def setup_database(host, port, database, **config):
    """
    设置数据库连接，支持额外配置选项
    
    参数:
        host (str): 数据库主机
        port (int): 端口号
        database (str): 数据库名
        **config: 额外配置选项
    
    返回:
        dict: 数据库配置
    """
    # 默认配置
    db_config = {
        'host': host,
        'port': port,
        'database': database,
        'charset': 'utf8',
        'timeout': 30,
        'pool_size': 5,
        'ssl_enabled': False
    }
    
    # 更新自定义配置
    db_config.update(config)
    
    print(f"数据库配置:")
    for key, value in db_config.items():
        print(f"  {key}: {value}")
    
    connection_string = f"{db_config.get('username', 'user')}@{host}:{port}/{database}"
    print(f"连接字符串: {connection_string}")
    print("-" * 40)
    
    return db_config

# 4. **kwargs与*args组合使用
def flexible_function(*args, **kwargs):
    """
    同时接受任意位置参数和关键字参数的函数
    
    参数:
        *args: 任意数量的位置参数
        **kwargs: 任意数量的关键字参数
    """
    print(f"位置参数 (*args): {args}")
    print(f"关键字参数 (**kwargs): {kwargs}")
    
    # 处理位置参数
    if args:
        print(f"位置参数处理:")
        for i, arg in enumerate(args):
            print(f"  参数{i+1}: {arg}")
    
    # 处理关键字参数
    if kwargs:
        print(f"关键字参数处理:")
        for key, value in kwargs.items():
            print(f"  {key} = {value}")
    
    print("-" * 30)

# 5. **kwargs用于API包装
def make_http_request(url, method="GET", **options):
    """
    模拟HTTP请求，支持各种选项
    
    参数:
        url (str): 请求URL
        method (str): HTTP方法
        **options: 请求选项
    
    返回:
        dict: 模拟的响应
    """
    # 默认选项
    default_options = {
        'timeout': 30,
        'verify_ssl': True,
        'follow_redirects': True,
        'max_retries': 3
    }
    
    # 合并选项
    request_options = {**default_options, **options}
    
    print(f"HTTP请求配置:")
    print(f"  URL: {url}")
    print(f"  方法: {method}")
    print(f"  选项:")
    for key, value in request_options.items():
        print(f"    {key}: {value}")
    
    # 模拟响应
    response = {
        'status_code': 200,
        'url': url,
        'method': method,
        'options_used': request_options
    }
    
    print(f"模拟响应: 状态码 {response['status_code']}")
    print("-" * 40)
    return response

# 6. **kwargs用于数据过滤
def filter_data(data, **filters):
    """
    根据关键字参数过滤数据
    
    参数:
        data (list): 要过滤的数据列表
        **filters: 过滤条件
    
    返回:
        list: 过滤后的数据
    """
    print(f"原始数据: {data}")
    print(f"过滤条件: {filters}")
    
    if not filters:
        print("没有过滤条件，返回原始数据")
        return data
    
    filtered_data = []
    
    for item in data:
        match = True
        for key, value in filters.items():
            if isinstance(item, dict):
                if key not in item or item[key] != value:
                    match = False
                    break
            else:
                # 对于非字典项，尝试属性访问
                try:
                    if not hasattr(item, key) or getattr(item, key) != value:
                        match = False
                        break
                except:
                    match = False
                    break
        
        if match:
            filtered_data.append(item)
    
    print(f"过滤结果: {filtered_data}")
    print(f"匹配项数量: {len(filtered_data)}")
    print("-" * 30)
    return filtered_data

# 7. **kwargs用于装饰器
def log_function_calls(func):
    """
    记录函数调用的装饰器
    """
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        print(f"位置参数: {args}")
        print(f"关键字参数: {kwargs}")
        
        try:
            result = func(*args, **kwargs)
            print(f"函数返回: {result}")
            return result
        except Exception as e:
            print(f"函数异常: {e}")
            raise
        finally:
            print(f"函数调用结束")
            print("-" * 30)
    
    return wrapper

@log_function_calls
def calculate_total(base_amount, **adjustments):
    """
    计算总金额，支持各种调整
    """
    total = base_amount
    
    for adjustment_type, amount in adjustments.items():
        if adjustment_type == 'tax':
            total += base_amount * amount
        elif adjustment_type == 'discount':
            total -= base_amount * amount
        elif adjustment_type == 'shipping':
            total += amount
        elif adjustment_type == 'insurance':
            total += amount
        else:
            print(f"未知调整类型: {adjustment_type}")
    
    return round(total, 2)

# 8. **kwargs用于配置类
class ConfigurableClass:
    """
    可配置的类，演示**kwargs在类中的使用
    """
    
    def __init__(self, name, **config):
        """
        初始化可配置类
        
        参数:
            name (str): 实例名称
            **config: 配置选项
        """
        self.name = name
        self.config = {
            'debug': False,
            'timeout': 30,
            'max_retries': 3,
            'log_level': 'INFO'
        }
        
        # 更新配置
        self.config.update(config)
        
        print(f"创建 {self.__class__.__name__} 实例: {name}")
        print(f"配置: {self.config}")
    
    def update_config(self, **new_config):
        """
        更新配置
        
        参数:
            **new_config: 新的配置选项
        """
        old_config = self.config.copy()
        self.config.update(new_config)
        
        print(f"更新 {self.name} 的配置:")
        print(f"  旧配置: {old_config}")
        print(f"  新配置: {self.config}")
        print(f"  变更项: {new_config}")
    
    def get_config(self, *keys):
        """
        获取指定的配置项
        
        参数:
            *keys: 要获取的配置键
        
        返回:
            dict: 指定的配置项
        """
        if not keys:
            return self.config.copy()
        
        result = {}
        for key in keys:
            if key in self.config:
                result[key] = self.config[key]
        
        return result

# 9. **kwargs用于动态函数调用
def dynamic_function_call(func_name, **params):
    """
    动态调用函数，演示**kwargs的传递
    
    参数:
        func_name (str): 函数名
        **params: 传递给函数的参数
    """
    # 模拟函数映射
    functions = {
        'greet': lambda name, greeting="Hello": f"{greeting}, {name}!",
        'add': lambda a, b: a + b,
        'multiply': lambda x, y, factor=1: (x * y) * factor,
        'format_text': lambda text, upper=False, prefix="": 
            f"{prefix}{text.upper() if upper else text}"
    }
    
    print(f"动态调用函数: {func_name}")
    print(f"传递参数: {params}")
    
    if func_name not in functions:
        print(f"错误: 函数 '{func_name}' 不存在")
        return None
    
    try:
        result = functions[func_name](**params)
        print(f"调用结果: {result}")
        print("-" * 30)
        return result
    except Exception as e:
        print(f"调用错误: {e}")
        print("-" * 30)
        return None

def main():
    """
    主函数：演示**kwargs的各种用法
    """
    print("=" * 50)
    print("关键字可变参数 **kwargs 演示")
    print("=" * 50)
    
    # 1. 基本**kwargs使用
    print("\n1. 基本**kwargs使用：")
    print_info()
    print_info(name="张三", age=25, city="北京")
    print_info(product="iPhone", price=8999, color="黑色", storage="256GB")
    
    # 2. **kwargs与普通参数组合
    print("\n2. **kwargs与普通参数组合：")
    create_user("john_doe", "john@example.com")
    create_user("jane_smith", "jane@example.com", 
               age=28, city="上海", department="技术部")
    create_user("admin", "admin@example.com", 
               role="管理员", permissions=["read", "write", "delete"],
               last_login="2024-01-15")
    
    # 3. 数据库配置
    print("\n3. 数据库配置：")
    setup_database("localhost", 3306, "myapp")
    setup_database("192.168.1.100", 5432, "production",
                  username="admin", password="secret",
                  ssl_enabled=True, pool_size=20, timeout=60)
    
    # 4. *args与**kwargs组合
    print("\n4. *args与**kwargs组合：")
    flexible_function()
    flexible_function(1, 2, 3)
    flexible_function(name="测试", version=1.0)
    flexible_function("hello", "world", debug=True, timeout=30)
    
    # 5. HTTP请求包装
    print("\n5. HTTP请求包装：")
    make_http_request("https://api.example.com/users")
    make_http_request("https://api.example.com/data", "POST",
                     headers={"Content-Type": "application/json"},
                     data={"key": "value"},
                     timeout=60, max_retries=5)
    
    # 6. 数据过滤
    print("\n6. 数据过滤：")
    users_data = [
        {"name": "张三", "age": 25, "city": "北京", "department": "技术部"},
        {"name": "李四", "age": 30, "city": "上海", "department": "销售部"},
        {"name": "王五", "age": 25, "city": "北京", "department": "技术部"},
        {"name": "赵六", "age": 28, "city": "广州", "department": "市场部"}
    ]
    
    filter_data(users_data, age=25)
    filter_data(users_data, city="北京", department="技术部")
    filter_data(users_data, department="销售部")
    
    # 7. 装饰器中的**kwargs
    print("\n7. 装饰器中的**kwargs：")
    calculate_total(1000)
    calculate_total(1000, tax=0.1, discount=0.05)
    calculate_total(1000, tax=0.08, shipping=50, insurance=20)
    
    # 8. 可配置类
    print("\n8. 可配置类：")
    obj1 = ConfigurableClass("服务A")
    obj2 = ConfigurableClass("服务B", debug=True, timeout=60, log_level="DEBUG")
    
    print("\n更新配置：")
    obj1.update_config(debug=True, max_retries=5)
    
    print("\n获取配置：")
    config = obj2.get_config("debug", "timeout")
    print(f"部分配置: {config}")
    
    # 9. 动态函数调用
    print("\n9. 动态函数调用：")
    dynamic_function_call("greet", name="世界")
    dynamic_function_call("greet", name="Python", greeting="欢迎")
    dynamic_function_call("add", a=10, b=20)
    dynamic_function_call("multiply", x=5, y=3, factor=2)
    dynamic_function_call("format_text", text="hello world", upper=True, prefix=">>> ")
    dynamic_function_call("unknown_func", param=123)  # 错误示例
    
    # 10. 实际应用：配置管理
    print("\n10. 实际应用 - 配置管理：")
    
    def load_config(config_file, **overrides):
        """
        加载配置文件并应用覆盖选项
        """
        # 模拟从文件加载的默认配置
        default_config = {
            'app_name': 'MyApp',
            'version': '1.0.0',
            'debug': False,
            'database': {
                'host': 'localhost',
                'port': 5432,
                'name': 'myapp_db'
            },
            'cache': {
                'enabled': True,
                'ttl': 3600
            }
        }
        
        print(f"加载配置文件: {config_file}")
        print(f"默认配置: {default_config}")
        print(f"覆盖选项: {overrides}")
        
        # 应用覆盖选项
        final_config = default_config.copy()
        final_config.update(overrides)
        
        print(f"最终配置: {final_config}")
        print("-" * 40)
        return final_config
    
    # 不同环境的配置
    dev_config = load_config("config.json", debug=True)
    prod_config = load_config("config.json", 
                             debug=False,
                             database_host="prod-db.example.com",
                             cache_ttl=7200)
    
    print("\n=" * 50)
    print("**kwargs 要点总结：")
    print("1. **kwargs收集任意数量的关键字参数到字典中")
    print("2. **kwargs必须在所有其他参数之后")
    print("3. **kwargs可以与*args组合使用")
    print("4. 函数内部**kwargs是一个字典，可以进行字典操作")
    print("5. **kwargs常用于配置选项、API包装、装饰器等")
    print("6. 使用**kwargs可以让函数接口更加灵活")
    print("=" * 50)

if __name__ == "__main__":
    main()