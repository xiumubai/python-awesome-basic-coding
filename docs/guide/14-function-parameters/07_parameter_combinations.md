# 参数组合使用

在Python函数设计中，我们可以将不同类型的参数组合使用，创建既灵活又强大的函数接口。理解参数的正确顺序和组合方式是编写高质量Python代码的关键技能。

## 参数顺序规则

### 标准参数顺序
Python函数参数必须按照以下顺序定义：

1. **位置参数**（positional arguments）
2. **默认参数**（default arguments）
3. **可变位置参数**（*args）
4. **仅关键字参数**（keyword-only arguments）
5. **可变关键字参数**（**kwargs）

```python
def complete_function_signature(
    pos_arg,                    # 1. 位置参数
    default_arg="default",      # 2. 默认参数
    *args,                      # 3. 可变位置参数
    kw_only_arg,               # 4. 仅关键字参数
    kw_only_default="kw_def",  # 4. 带默认值的仅关键字参数
    **kwargs                   # 5. 可变关键字参数
):
    """
    完整的函数参数签名示例
    
    Args:
        pos_arg: 必需的位置参数
        default_arg: 带默认值的参数
        *args: 可变位置参数
        kw_only_arg: 仅关键字参数（必需）
        kw_only_default: 带默认值的仅关键字参数
        **kwargs: 可变关键字参数
    """
    print(f"位置参数: {pos_arg}")
    print(f"默认参数: {default_arg}")
    print(f"可变位置参数: {args}")
    print(f"仅关键字参数: {kw_only_arg}")
    print(f"仅关键字默认参数: {kw_only_default}")
    print(f"可变关键字参数: {kwargs}")
    print("-" * 50)

# 正确的调用方式
complete_function_signature(
    "必需位置参数",              # pos_arg
    "自定义默认值",              # default_arg
    "额外", "位置", "参数",      # *args
    kw_only_arg="仅关键字值",    # 必需的仅关键字参数
    kw_only_default="自定义kw",  # 可选的仅关键字参数
    extra1="额外1",             # **kwargs
    extra2="额外2"              # **kwargs
)
```

## 常见参数组合

### 1. 位置参数 + 默认参数

```python
def create_user(username, email, age=18, active=True):
    """
    创建用户 - 基本组合
    
    Args:
        username: 用户名（必需）
        email: 邮箱（必需）
        age: 年龄（默认18）
        active: 是否激活（默认True）
    """
    user = {
        "username": username,
        "email": email,
        "age": age,
        "active": active,
        "created_at": "2024-01-01 12:00:00"
    }
    
    print(f"创建用户: {username}")
    print(f"用户信息: {user}")
    print("-" * 40)
    
    return user

def format_message(message, prefix="INFO", timestamp=True, uppercase=False):
    """
    格式化消息 - 多个默认参数
    
    Args:
        message: 消息内容（必需）
        prefix: 消息前缀（默认"INFO"）
        timestamp: 是否包含时间戳（默认True）
        uppercase: 是否转换为大写（默认False）
    """
    formatted = message
    
    if uppercase:
        formatted = formatted.upper()
    
    if timestamp:
        formatted = f"[2024-01-01 12:00:00] {formatted}"
    
    if prefix:
        formatted = f"[{prefix}] {formatted}"
    
    print(f"原始消息: {message}")
    print(f"格式化后: {formatted}")
    print("-" * 40)
    
    return formatted

# 基本组合示例
create_user("alice", "alice@example.com")
create_user("bob", "bob@example.com", 25)
create_user("charlie", "charlie@example.com", 30, False)

format_message("系统启动成功")
format_message("错误信息", "ERROR", False)
format_message("警告信息", "WARN", True, True)
```

### 2. 位置参数 + *args + 默认参数

```python
def calculate_statistics(*numbers, operation="mean", precision=2):
    """
    计算统计信息 - *args与默认参数组合
    
    Args:
        *numbers: 要计算的数字
        operation: 操作类型（默认"mean"）
        precision: 精度（默认2位小数）
    """
    if not numbers:
        print("没有提供数字")
        return None
    
    print(f"数字: {numbers}")
    print(f"操作: {operation}")
    print(f"精度: {precision}")
    
    if operation == "mean":
        result = sum(numbers) / len(numbers)
    elif operation == "sum":
        result = sum(numbers)
    elif operation == "max":
        result = max(numbers)
    elif operation == "min":
        result = min(numbers)
    elif operation == "product":
        result = 1
        for num in numbers:
            result *= num
    else:
        print(f"不支持的操作: {operation}")
        return None
    
    result = round(result, precision)
    print(f"结果: {result}")
    print("-" * 40)
    
    return result

def build_path(*path_parts, separator="/", absolute=False):
    """
    构建路径 - *args与默认参数
    
    Args:
        *path_parts: 路径组件
        separator: 路径分隔符（默认"/"）
        absolute: 是否为绝对路径（默认False）
    """
    if not path_parts:
        return "/" if absolute else ""
    
    # 清理路径组件
    clean_parts = []
    for part in path_parts:
        if part:  # 忽略空字符串
            clean_parts.append(str(part).strip(separator))
    
    path = separator.join(clean_parts)
    
    if absolute and not path.startswith(separator):
        path = separator + path
    
    print(f"路径组件: {path_parts}")
    print(f"分隔符: '{separator}'")
    print(f"绝对路径: {absolute}")
    print(f"构建的路径: '{path}'")
    print("-" * 40)
    
    return path

# *args与默认参数示例
calculate_statistics(1, 2, 3, 4, 5)
calculate_statistics(10, 20, 30, operation="sum")
calculate_statistics(1.234, 2.567, 3.891, operation="mean", precision=3)

build_path("home", "user", "documents")
build_path("var", "log", "app.log", separator="\\", absolute=True)
build_path("src", "components", "Button.js", absolute=True)
```

### 3. 完整参数组合

```python
def advanced_api_call(
    endpoint,                    # 必需位置参数
    method="GET",               # 默认参数
    *path_segments,             # 可变位置参数
    timeout=30,                 # 仅关键字参数（带默认值）
    headers=None,               # 仅关键字参数（带默认值）
    **params                    # 可变关键字参数
):
    """
    高级API调用函数 - 完整参数组合
    
    Args:
        endpoint: API端点（必需）
        method: HTTP方法（默认GET）
        *path_segments: 路径段
        timeout: 超时时间（仅关键字，默认30秒）
        headers: 请求头（仅关键字，默认None）
        **params: 其他参数
    """
    # 构建完整URL
    url = endpoint
    if path_segments:
        url += "/" + "/".join(str(seg) for seg in path_segments)
    
    # 处理请求头
    if headers is None:
        headers = {}
    
    # 分离不同类型的参数
    query_params = params.pop("query", {})
    body_data = params.pop("data", {})
    config_options = params  # 剩余的参数作为配置选项
    
    print(f"🌐 API调用详情:")
    print(f"   URL: {url}")
    print(f"   方法: {method}")
    print(f"   超时: {timeout}秒")
    print(f"   请求头: {headers}")
    print(f"   查询参数: {query_params}")
    print(f"   请求体: {body_data}")
    print(f"   配置选项: {config_options}")
    
    # 模拟API响应
    response = {
        "status": 200,
        "url": url,
        "method": method,
        "data": f"Response from {url}"
    }
    
    print(f"📥 响应: {response['status']} - {response['data']}")
    print("-" * 50)
    
    return response

def flexible_data_processor(
    data,                       # 必需位置参数
    *transformations,           # 可变位置参数（转换函数）
    validate=True,              # 仅关键字参数
    sort_result=False,          # 仅关键字参数
    **options                   # 可变关键字参数
):
    """
    灵活的数据处理器 - 完整参数组合
    
    Args:
        data: 要处理的数据（必需）
        *transformations: 转换函数列表
        validate: 是否验证数据（仅关键字）
        sort_result: 是否排序结果（仅关键字）
        **options: 处理选项
    """
    print(f"📊 数据处理开始:")
    print(f"   原始数据: {data}")
    print(f"   转换函数数量: {len(transformations)}")
    print(f"   验证数据: {validate}")
    print(f"   排序结果: {sort_result}")
    print(f"   处理选项: {options}")
    
    result = data.copy() if isinstance(data, (list, dict)) else data
    
    # 数据验证
    if validate:
        if isinstance(result, list) and options.get("min_length"):
            if len(result) < options["min_length"]:
                raise ValueError(f"数据长度不足，最少需要 {options['min_length']} 项")
        print(f"   ✅ 数据验证通过")
    
    # 应用转换函数
    for i, transform_func in enumerate(transformations):
        print(f"   🔄 应用转换 {i+1}: {transform_func.__name__}")
        try:
            result = transform_func(result)
            print(f"      转换后: {result}")
        except Exception as e:
            print(f"      ❌ 转换失败: {e}")
            if not options.get("ignore_errors", False):
                raise
    
    # 排序结果
    if sort_result and isinstance(result, list):
        try:
            result.sort(reverse=options.get("reverse_sort", False))
            print(f"   📈 排序完成: {result}")
        except TypeError:
            print(f"   ⚠️  排序失败: 数据类型不一致")
    
    # 应用其他选项
    if options.get("unique_only") and isinstance(result, list):
        result = list(set(result))
        print(f"   🎯 去重完成: {result}")
    
    if options.get("limit") and isinstance(result, list):
        limit = options["limit"]
        result = result[:limit]
        print(f"   ✂️  限制数量到 {limit}: {result}")
    
    print(f"📋 最终结果: {result}")
    print("-" * 50)
    
    return result

# 完整参数组合示例
advanced_api_call(
    "https://api.example.com",
    "POST",
    "users", "123", "profile",
    timeout=60,
    headers={"Authorization": "Bearer token123"},
    query={"include": "details"},
    data={"name": "Alice", "age": 25},
    retry_count=3,
    cache_enabled=True
)

# 定义一些转换函数
def double_numbers(data):
    """将数字翻倍"""
    if isinstance(data, list):
        return [x * 2 if isinstance(x, (int, float)) else x for x in data]
    return data

def add_prefix(data):
    """添加前缀"""
    if isinstance(data, list):
        return [f"item_{x}" if isinstance(x, (int, float)) else x for x in data]
    return data

def filter_positive(data):
    """过滤正数"""
    if isinstance(data, list):
        return [x for x in data if isinstance(x, (int, float)) and x > 0]
    return data

# 数据处理示例
test_data = [1, -2, 3, -4, 5, 0, 6]

flexible_data_processor(
    test_data,
    filter_positive,
    double_numbers,
    add_prefix,
    validate=True,
    sort_result=True,
    min_length=3,
    unique_only=False,
    limit=5,
    reverse_sort=True
)
```

### 4. 仅关键字参数的使用

```python
def create_connection(host, port, *, ssl=False, timeout=30, pool_size=10):
    """
    创建连接 - 使用仅关键字参数
    
    Args:
        host: 主机地址
        port: 端口号
        ssl: 是否使用SSL（仅关键字）
        timeout: 超时时间（仅关键字）
        pool_size: 连接池大小（仅关键字）
    """
    connection_config = {
        "host": host,
        "port": port,
        "ssl": ssl,
        "timeout": timeout,
        "pool_size": pool_size,
        "connection_string": f"{'https' if ssl else 'http'}://{host}:{port}"
    }
    
    print(f"🔗 创建连接:")
    print(f"   主机: {host}:{port}")
    print(f"   SSL: {ssl}")
    print(f"   超时: {timeout}秒")
    print(f"   连接池大小: {pool_size}")
    print(f"   连接字符串: {connection_config['connection_string']}")
    print("-" * 40)
    
    return connection_config

def process_file(filename, *, encoding="utf-8", mode="r", buffer_size=8192):
    """
    处理文件 - 仅关键字参数确保安全性
    
    Args:
        filename: 文件名
        encoding: 编码格式（仅关键字）
        mode: 打开模式（仅关键字）
        buffer_size: 缓冲区大小（仅关键字）
    """
    print(f"📁 处理文件: {filename}")
    print(f"   编码: {encoding}")
    print(f"   模式: {mode}")
    print(f"   缓冲区: {buffer_size} 字节")
    
    # 模拟文件处理
    file_info = {
        "filename": filename,
        "encoding": encoding,
        "mode": mode,
        "buffer_size": buffer_size,
        "status": "已处理"
    }
    
    print(f"   状态: {file_info['status']}")
    print("-" * 40)
    
    return file_info

# 仅关键字参数示例
create_connection("localhost", 8080)
create_connection("api.example.com", 443, ssl=True, timeout=60)
create_connection("db.example.com", 5432, ssl=True, pool_size=20)

process_file("data.txt")
process_file("config.json", encoding="utf-8", mode="r")
process_file("binary.dat", encoding="latin-1", mode="rb", buffer_size=4096)
```

## 实际应用案例

### 1. 数据处理管道

```python
def create_data_pipeline(
    source,                     # 数据源
    *processors,                # 处理器函数
    output_format="json",       # 输出格式
    validate_steps=True,        # 是否验证每步
    **pipeline_options          # 管道选项
):
    """
    创建数据处理管道
    
    Args:
        source: 数据源
        *processors: 处理器函数列表
        output_format: 输出格式（仅关键字）
        validate_steps: 是否验证每步（仅关键字）
        **pipeline_options: 管道配置选项
    """
    print(f"🏭 创建数据处理管道:")
    print(f"   数据源: {source}")
    print(f"   处理器数量: {len(processors)}")
    print(f"   输出格式: {output_format}")
    print(f"   验证步骤: {validate_steps}")
    print(f"   管道选项: {pipeline_options}")
    
    # 初始化数据
    data = source.copy() if isinstance(source, (list, dict)) else source
    
    # 执行处理管道
    for i, processor in enumerate(processors):
        step_name = processor.__name__
        print(f"\n   📊 步骤 {i+1}: {step_name}")
        print(f"      输入: {data}")
        
        try:
            # 执行处理器
            data = processor(data, **pipeline_options)
            print(f"      输出: {data}")
            
            # 验证步骤
            if validate_steps:
                if data is None:
                    raise ValueError(f"步骤 {step_name} 返回了 None")
                print(f"      ✅ 验证通过")
        
        except Exception as e:
            print(f"      ❌ 处理失败: {e}")
            if not pipeline_options.get("continue_on_error", False):
                raise
            print(f"      ⚠️  跳过错误，继续处理")
    
    # 格式化输出
    if output_format == "json":
        import json
        result = json.dumps(data, ensure_ascii=False, indent=2)
    elif output_format == "string":
        result = str(data)
    elif output_format == "list":
        result = list(data) if not isinstance(data, list) else data
    else:
        result = data
    
    print(f"\n📤 管道输出 ({output_format}):")
    print(f"   {result}")
    print("-" * 50)
    
    return result

# 定义处理器函数
def clean_data(data, **options):
    """清理数据"""
    if isinstance(data, list):
        # 移除空值和重复项
        cleaned = list(set(item for item in data if item is not None and item != ""))
        return cleaned
    return data

def transform_data(data, **options):
    """转换数据"""
    multiplier = options.get("multiplier", 1)
    if isinstance(data, list):
        return [item * multiplier if isinstance(item, (int, float)) else item 
                for item in data]
    return data

def filter_data(data, **options):
    """过滤数据"""
    min_value = options.get("min_value", 0)
    if isinstance(data, list):
        return [item for item in data 
                if not isinstance(item, (int, float)) or item >= min_value]
    return data

# 数据管道示例
raw_data = [1, 2, None, 3, "", 4, 2, 5, -1, 0]

create_data_pipeline(
    raw_data,
    clean_data,
    transform_data,
    filter_data,
    output_format="json",
    validate_steps=True,
    multiplier=2,
    min_value=1,
    continue_on_error=False
)
```

### 2. 配置构建器

```python
class ApplicationConfig:
    """
    应用程序配置类 - 使用参数组合
    """
    
    def __init__(self, app_name, version="1.0.0", **base_config):
        """
        初始化配置
        
        Args:
            app_name: 应用名称（必需）
            version: 版本号（默认"1.0.0"）
            **base_config: 基础配置
        """
        self.config = {
            "app_name": app_name,
            "version": version,
            **base_config
        }
        
        print(f"🚀 初始化应用配置: {app_name} v{version}")
        if base_config:
            print(f"   基础配置: {base_config}")
        print("-" * 40)
    
    def add_database_config(
        self, 
        host, 
        port=5432, 
        *additional_hosts,
        ssl_mode="prefer",
        **db_options
    ):
        """
        添加数据库配置
        
        Args:
            host: 主数据库主机
            port: 端口（默认5432）
            *additional_hosts: 额外的主机
            ssl_mode: SSL模式（仅关键字）
            **db_options: 数据库选项
        """
        db_config = {
            "primary_host": host,
            "port": port,
            "ssl_mode": ssl_mode,
            **db_options
        }
        
        if additional_hosts:
            db_config["replica_hosts"] = list(additional_hosts)
        
        self.config["database"] = db_config
        
        print(f"💾 添加数据库配置:")
        print(f"   主机: {host}:{port}")
        if additional_hosts:
            print(f"   副本主机: {additional_hosts}")
        print(f"   SSL模式: {ssl_mode}")
        print(f"   其他选项: {db_options}")
        print("-" * 40)
        
        return self
    
    def add_cache_config(
        self, 
        cache_type="redis", 
        *cache_servers,
        ttl=3600,
        **cache_options
    ):
        """
        添加缓存配置
        
        Args:
            cache_type: 缓存类型（默认"redis"）
            *cache_servers: 缓存服务器列表
            ttl: 生存时间（仅关键字，默认3600秒）
            **cache_options: 缓存选项
        """
        cache_config = {
            "type": cache_type,
            "ttl": ttl,
            **cache_options
        }
        
        if cache_servers:
            cache_config["servers"] = list(cache_servers)
        else:
            cache_config["servers"] = ["localhost:6379"]
        
        self.config["cache"] = cache_config
        
        print(f"🗄️  添加缓存配置:")
        print(f"   类型: {cache_type}")
        print(f"   服务器: {cache_config['servers']}")
        print(f"   TTL: {ttl}秒")
        print(f"   其他选项: {cache_options}")
        print("-" * 40)
        
        return self
    
    def get_config(self):
        """获取完整配置"""
        print(f"📋 完整应用配置:")
        for section, config in self.config.items():
            print(f"   {section}: {config}")
        print("-" * 40)
        
        return self.config.copy()

# 配置构建器示例
app_config = ApplicationConfig(
    "MyWebApp", 
    "2.1.0",
    debug=False,
    log_level="INFO",
    max_workers=4
)

app_config.add_database_config(
    "db-primary.example.com",
    5432,
    "db-replica1.example.com",
    "db-replica2.example.com",
    ssl_mode="require",
    pool_size=20,
    timeout=30,
    charset="utf8mb4"
)

app_config.add_cache_config(
    "redis",
    "cache1.example.com:6379",
    "cache2.example.com:6379",
    ttl=7200,
    max_connections=50,
    cluster_mode=True
)

final_config = app_config.get_config()
```

## 参数顺序错误示例

### 错误的参数顺序

```python
# ❌ 错误：默认参数在位置参数之后
# def wrong_order1(default_arg="default", pos_arg):
#     pass

# ❌ 错误：**kwargs在*args之前
# def wrong_order2(*args, **kwargs, kw_only):
#     pass

# ❌ 错误：位置参数在*args之后
# def wrong_order3(*args, pos_arg):
#     pass

print("❌ 以上注释的函数定义都是错误的参数顺序")
print("Python解释器会报语法错误")
print("-" * 40)
```

### 正确的参数顺序

```python
def correct_order_example(
    required_pos,               # ✅ 位置参数
    optional_pos="default",     # ✅ 默认参数
    *var_pos,                   # ✅ 可变位置参数
    kw_only_required,           # ✅ 仅关键字参数（必需）
    kw_only_optional="kw_def",  # ✅ 仅关键字参数（可选）
    **var_kw                    # ✅ 可变关键字参数
):
    """
    正确的参数顺序示例
    """
    print(f"✅ 正确的参数顺序:")
    print(f"   位置参数: {required_pos}")
    print(f"   默认参数: {optional_pos}")
    print(f"   可变位置参数: {var_pos}")
    print(f"   仅关键字参数（必需）: {kw_only_required}")
    print(f"   仅关键字参数（可选）: {kw_only_optional}")
    print(f"   可变关键字参数: {var_kw}")
    print("-" * 40)

# 正确调用示例
correct_order_example(
    "必需位置参数",
    "自定义默认值",
    "额外1", "额外2", "额外3",
    kw_only_required="必需关键字",
    kw_only_optional="自定义关键字",
    extra1="额外关键字1",
    extra2="额外关键字2"
)
```

## 运行示例

要运行这些示例，请使用以下命令：

```bash
python3 06_parameter_combinations.py
```

## 学习要点

1. **参数顺序**：严格遵循Python的参数顺序规则
2. **灵活性设计**：合理组合不同类型的参数提供灵活的接口
3. **仅关键字参数**：使用*分隔符创建更安全的API
4. **默认值设计**：为可选参数提供合理的默认值
5. **文档说明**：清楚标明每个参数的类型和用途
6. **错误处理**：处理参数验证和错误情况
7. **实际应用**：在配置管理、数据处理等场景中的应用
8. **代码可读性**：保持函数签名的清晰和可理解性

## 下一步

掌握了参数组合使用后，接下来学习[参数解包](08_parameter_unpacking.md)，了解如何在函数调用时解包参数。