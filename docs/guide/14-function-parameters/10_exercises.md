# 综合练习

这个练习模块包含了9个综合练习，涵盖了函数参数的各个方面。通过这些练习，你将能够熟练掌握位置参数、关键字参数、默认参数、可变参数、参数组合、参数解包、参数验证等核心概念。

## 练习概述

### 练习列表

1. **基础参数练习** - 掌握位置参数和关键字参数的基本用法
2. **默认参数练习** - 理解默认参数的设计和使用
3. **可变参数练习** - 熟练使用*args处理不定数量的参数
4. **关键字参数练习** - 掌握**kwargs的灵活应用
5. **参数组合练习** - 学会合理组合不同类型的参数
6. **参数解包练习** - 掌握参数解包的技巧和应用场景
7. **参数验证练习** - 实现健壮的参数验证机制
8. **实际应用练习** - 将参数技巧应用到实际项目中
9. **高级挑战练习** - 挑战复杂的参数处理场景

## 练习1：基础参数练习

### 任务描述
创建一个个人信息管理系统，要求使用位置参数和关键字参数。

```python
def exercise_1_basic_parameters():
    """
    练习1：基础参数练习
    创建个人信息管理函数
    """
    print("📝 练习1：基础参数练习")
    print("-" * 50)
    
    def create_person_profile(name, age, city, occupation, email=None, phone=None):
        """
        创建个人档案
        
        位置参数：name, age, city, occupation
        关键字参数：email, phone
        """
        profile = {
            "name": name,
            "age": age,
            "city": city,
            "occupation": occupation,
            "contact": {}
        }
        
        if email:
            profile["contact"]["email"] = email
        if phone:
            profile["contact"]["phone"] = phone
        
        return profile
    
    def display_profile(profile, show_contact=True, format_style="detailed"):
        """
        显示个人档案
        
        位置参数：profile
        关键字参数：show_contact, format_style
        """
        if format_style == "simple":
            return f"{profile['name']} ({profile['age']}岁) - {profile['occupation']}"
        
        elif format_style == "detailed":
            result = f"姓名: {profile['name']}\n"
            result += f"年龄: {profile['age']}岁\n"
            result += f"城市: {profile['city']}\n"
            result += f"职业: {profile['occupation']}\n"
            
            if show_contact and profile['contact']:
                result += "联系方式:\n"
                for key, value in profile['contact'].items():
                    result += f"  {key}: {value}\n"
            
            return result.strip()
        
        else:
            return str(profile)
    
    # 测试用例
    print("创建个人档案:")
    
    # 使用位置参数
    profile1 = create_person_profile("张三", 28, "北京", "软件工程师")
    print(f"档案1: {profile1}")
    
    # 使用位置参数 + 关键字参数
    profile2 = create_person_profile("李四", 32, "上海", "产品经理", 
                                   email="lisi@example.com", phone="13812345678")
    print(f"档案2: {profile2}")
    
    # 使用关键字参数调用
    profile3 = create_person_profile(name="王五", age=25, city="深圳", 
                                   occupation="UI设计师", email="wangwu@example.com")
    print(f"档案3: {profile3}")
    
    print("\n显示档案:")
    print("简单格式:")
    print(display_profile(profile2, format_style="simple"))
    
    print("\n详细格式:")
    print(display_profile(profile2))
    
    print("\n详细格式（不显示联系方式）:")
    print(display_profile(profile2, show_contact=False))
    
    print("-" * 50)

# 运行练习1
exercise_1_basic_parameters()
```

## 练习2：默认参数练习

### 任务描述
创建一个配置管理系统，合理使用默认参数。

```python
def exercise_2_default_parameters():
    """
    练习2：默认参数练习
    创建配置管理系统
    """
    print("⚙️  练习2：默认参数练习")
    print("-" * 50)
    
    def create_server_config(host="localhost", port=8000, debug=False, 
                           max_connections=100, timeout=30, ssl_enabled=False,
                           log_level="INFO", database_url=None):
        """
        创建服务器配置
        使用默认参数提供合理的默认值
        """
        config = {
            "server": {
                "host": host,
                "port": port,
                "debug": debug,
                "max_connections": max_connections,
                "timeout": timeout,
                "ssl_enabled": ssl_enabled
            },
            "logging": {
                "level": log_level
            }
        }
        
        if database_url:
            config["database"] = {"url": database_url}
        
        return config
    
    def create_email_config(smtp_server, smtp_port=587, use_tls=True, 
                          username=None, password=None, from_email=None,
                          retry_count=3, timeout=10):
        """
        创建邮件配置
        smtp_server是必需参数，其他都有默认值
        """
        config = {
            "smtp": {
                "server": smtp_server,
                "port": smtp_port,
                "use_tls": use_tls,
                "timeout": timeout
            },
            "auth": {},
            "settings": {
                "retry_count": retry_count
            }
        }
        
        if username and password:
            config["auth"] = {
                "username": username,
                "password": "*" * len(password)  # 隐藏密码
            }
        
        if from_email:
            config["settings"]["from_email"] = from_email
        
        return config
    
    def merge_configs(*configs, override_duplicates=True):
        """
        合并多个配置
        使用默认参数控制合并行为
        """
        if not configs:
            return {}
        
        merged = configs[0].copy()
        
        for config in configs[1:]:
            for key, value in config.items():
                if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
                    # 递归合并字典
                    merged[key] = {**merged[key], **value} if override_duplicates else merged[key]
                elif key not in merged or override_duplicates:
                    merged[key] = value
        
        return merged
    
    # 测试用例
    print("创建服务器配置:")
    
    # 使用所有默认值
    config1 = create_server_config()
    print(f"默认配置: {config1}")
    
    # 部分自定义
    config2 = create_server_config(host="0.0.0.0", port=3000, debug=True)
    print(f"开发配置: {config2}")
    
    # 生产环境配置
    config3 = create_server_config(
        host="prod.example.com",
        port=443,
        ssl_enabled=True,
        max_connections=1000,
        log_level="WARNING",
        database_url="postgresql://user:pass@db.example.com/prod"
    )
    print(f"生产配置: {config3}")
    
    print("\n创建邮件配置:")
    
    # 最简配置
    email_config1 = create_email_config("smtp.gmail.com")
    print(f"基础邮件配置: {email_config1}")
    
    # 完整配置
    email_config2 = create_email_config(
        smtp_server="smtp.company.com",
        smtp_port=465,
        use_tls=False,
        username="admin",
        password="secret123",
        from_email="noreply@company.com",
        retry_count=5
    )
    print(f"完整邮件配置: {email_config2}")
    
    print("\n合并配置:")
    
    base_config = {"app": {"name": "MyApp", "version": "1.0"}}
    dev_config = {"app": {"debug": True}, "database": {"host": "localhost"}}
    
    merged = merge_configs(base_config, dev_config)
    print(f"合并后的配置: {merged}")
    
    # 测试不覆盖重复项
    merged_no_override = merge_configs(base_config, dev_config, override_duplicates=False)
    print(f"不覆盖重复项: {merged_no_override}")
    
    print("-" * 50)

# 运行练习2
exercise_2_default_parameters()
```

## 练习3：可变参数练习

### 任务描述
创建一个数据分析工具，使用*args处理不定数量的数据集。

```python
def exercise_3_variable_args():
    """
    练习3：可变参数练习
    创建数据分析工具
    """
    print("📊 练习3：可变参数练习")
    print("-" * 50)
    
    def calculate_statistics(*datasets, operation="all"):
        """
        计算多个数据集的统计信息
        
        *datasets: 可变数量的数据集
        operation: 要执行的操作类型
        """
        if not datasets:
            return {"error": "至少需要一个数据集"}
        
        results = {}
        
        for i, dataset in enumerate(datasets):
            dataset_name = f"dataset_{i+1}"
            
            if not dataset:
                results[dataset_name] = {"error": "数据集为空"}
                continue
            
            stats = {}
            
            if operation in ["all", "basic"]:
                stats.update({
                    "count": len(dataset),
                    "sum": sum(dataset),
                    "mean": sum(dataset) / len(dataset),
                    "min": min(dataset),
                    "max": max(dataset)
                })
            
            if operation in ["all", "advanced"]:
                sorted_data = sorted(dataset)
                n = len(sorted_data)
                
                # 中位数
                if n % 2 == 0:
                    median = (sorted_data[n//2-1] + sorted_data[n//2]) / 2
                else:
                    median = sorted_data[n//2]
                
                # 方差和标准差
                mean = sum(dataset) / len(dataset)
                variance = sum((x - mean) ** 2 for x in dataset) / len(dataset)
                std_dev = variance ** 0.5
                
                stats.update({
                    "median": median,
                    "variance": variance,
                    "std_dev": std_dev,
                    "range": max(dataset) - min(dataset)
                })
            
            results[dataset_name] = stats
        
        return results
    
    def merge_datasets(*datasets, remove_duplicates=False):
        """
        合并多个数据集
        
        *datasets: 要合并的数据集
        remove_duplicates: 是否移除重复值
        """
        merged = []
        
        for dataset in datasets:
            merged.extend(dataset)
        
        if remove_duplicates:
            merged = list(set(merged))
            merged.sort()
        
        return merged
    
    def find_common_elements(*datasets):
        """
        找出所有数据集的共同元素
        
        *datasets: 要比较的数据集
        """
        if not datasets:
            return []
        
        # 将第一个数据集转换为集合
        common = set(datasets[0])
        
        # 与其他数据集求交集
        for dataset in datasets[1:]:
            common = common.intersection(set(dataset))
        
        return sorted(list(common))
    
    def apply_operations(*datasets, operations):
        """
        对多个数据集应用操作序列
        
        *datasets: 数据集
        operations: 操作函数列表
        """
        results = []
        
        for dataset in datasets:
            current_data = dataset.copy()
            
            for operation in operations:
                try:
                    current_data = operation(current_data)
                except Exception as e:
                    current_data = f"操作失败: {e}"
                    break
            
            results.append(current_data)
        
        return results
    
    # 测试用例
    print("计算统计信息:")
    
    # 测试数据
    data1 = [1, 2, 3, 4, 5]
    data2 = [10, 20, 30, 40, 50, 60]
    data3 = [2, 4, 6, 8, 10, 12, 14]
    data4 = []  # 空数据集
    
    # 基础统计
    basic_stats = calculate_statistics(data1, data2, operation="basic")
    print(f"基础统计: {basic_stats}")
    
    # 完整统计
    full_stats = calculate_statistics(data1, data2, data3, data4)
    print(f"完整统计: {full_stats}")
    
    print("\n合并数据集:")
    
    # 普通合并
    merged = merge_datasets(data1, data2, data3)
    print(f"合并结果: {merged}")
    
    # 去重合并
    data_with_duplicates = [1, 2, 3, 2, 4, 3, 5]
    merged_unique = merge_datasets(data1, data_with_duplicates, remove_duplicates=True)
    print(f"去重合并: {merged_unique}")
    
    print("\n查找共同元素:")
    
    set1 = [1, 2, 3, 4, 5]
    set2 = [3, 4, 5, 6, 7]
    set3 = [4, 5, 6, 7, 8]
    
    common = find_common_elements(set1, set2, set3)
    print(f"共同元素: {common}")
    
    print("\n应用操作序列:")
    
    # 定义操作函数
    def double_values(data):
        return [x * 2 for x in data]
    
    def filter_even(data):
        return [x for x in data if x % 2 == 0]
    
    def sort_desc(data):
        return sorted(data, reverse=True)
    
    operations = [double_values, filter_even, sort_desc]
    
    results = apply_operations(data1, data2, operations=operations)
    print(f"操作结果: {results}")
    
    print("-" * 50)

# 运行练习3
exercise_3_variable_args()
```

## 练习4：关键字参数练习

### 任务描述
创建一个API客户端，使用**kwargs处理灵活的配置选项。

```python
def exercise_4_keyword_args():
    """
    练习4：关键字参数练习
    创建API客户端
    """
    print("🌐 练习4：关键字参数练习")
    print("-" * 50)
    
    def make_api_request(url, method="GET", **kwargs):
        """
        发起API请求
        
        url: 请求URL
        method: HTTP方法
        **kwargs: 其他请求参数
        """
        # 提取常用参数
        headers = kwargs.get("headers", {})
        params = kwargs.get("params", {})
        data = kwargs.get("data", None)
        json_data = kwargs.get("json", None)
        timeout = kwargs.get("timeout", 30)
        auth = kwargs.get("auth", None)
        
        # 构建请求信息
        request_info = {
            "url": url,
            "method": method.upper(),
            "headers": headers,
            "timeout": timeout
        }
        
        if params:
            request_info["params"] = params
        
        if data:
            request_info["data"] = data
        
        if json_data:
            request_info["json"] = json_data
        
        if auth:
            request_info["auth"] = "***"  # 隐藏认证信息
        
        # 处理其他自定义选项
        custom_options = {k: v for k, v in kwargs.items() 
                         if k not in ['headers', 'params', 'data', 'json', 'timeout', 'auth']}
        
        if custom_options:
            request_info["custom_options"] = custom_options
        
        # 模拟请求结果
        response = {
            "status_code": 200,
            "request_info": request_info,
            "response_data": f"模拟响应数据 for {method} {url}"
        }
        
        return response
    
    def create_database_query(table, **conditions):
        """
        创建数据库查询
        
        table: 表名
        **conditions: 查询条件
        """
        # 分离不同类型的条件
        where_conditions = []
        order_by = conditions.pop("order_by", None)
        limit = conditions.pop("limit", None)
        offset = conditions.pop("offset", None)
        select_fields = conditions.pop("select", "*")
        
        # 构建WHERE子句
        for field, value in conditions.items():
            if isinstance(value, dict):
                # 处理复杂条件，如 {"age": {"gt": 18, "lt": 65}}
                for operator, op_value in value.items():
                    if operator == "gt":
                        where_conditions.append(f"{field} > {op_value}")
                    elif operator == "lt":
                        where_conditions.append(f"{field} < {op_value}")
                    elif operator == "gte":
                        where_conditions.append(f"{field} >= {op_value}")
                    elif operator == "lte":
                        where_conditions.append(f"{field} <= {op_value}")
                    elif operator == "in":
                        where_conditions.append(f"{field} IN ({', '.join(map(str, op_value))})")
                    elif operator == "like":
                        where_conditions.append(f"{field} LIKE '{op_value}'")
            else:
                # 简单等值条件
                if isinstance(value, str):
                    where_conditions.append(f"{field} = '{value}'")
                else:
                    where_conditions.append(f"{field} = {value}")
        
        # 构建完整查询
        query = f"SELECT {select_fields} FROM {table}"
        
        if where_conditions:
            query += f" WHERE {' AND '.join(where_conditions)}"
        
        if order_by:
            if isinstance(order_by, str):
                query += f" ORDER BY {order_by}"
            elif isinstance(order_by, dict):
                order_clauses = []
                for field, direction in order_by.items():
                    order_clauses.append(f"{field} {direction.upper()}")
                query += f" ORDER BY {', '.join(order_clauses)}"
        
        if limit:
            query += f" LIMIT {limit}"
        
        if offset:
            query += f" OFFSET {offset}"
        
        return query
    
    def configure_logger(name, **config):
        """
        配置日志记录器
        
        name: 记录器名称
        **config: 配置选项
        """
        # 默认配置
        logger_config = {
            "level": "INFO",
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "handlers": ["console"]
        }
        
        # 更新配置
        logger_config.update(config)
        
        # 处理特殊配置
        if "file" in config:
            file_config = config["file"]
            if isinstance(file_config, str):
                logger_config["file_path"] = file_config
            elif isinstance(file_config, dict):
                logger_config.update({f"file_{k}": v for k, v in file_config.items()})
        
        if "email" in config:
            email_config = config["email"]
            logger_config["email_notifications"] = email_config
        
        # 验证配置
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if logger_config["level"] not in valid_levels:
            logger_config["level"] = "INFO"
        
        return {
            "name": name,
            "config": logger_config,
            "status": "configured"
        }
    
    # 测试用例
    print("API请求测试:")
    
    # 简单GET请求
    response1 = make_api_request("https://api.example.com/users")
    print(f"GET请求: {response1}")
    
    # 带参数的GET请求
    response2 = make_api_request(
        "https://api.example.com/users",
        params={"page": 1, "limit": 10},
        headers={"Authorization": "Bearer token123"},
        timeout=60
    )
    print(f"\n带参数的GET请求: {response2}")
    
    # POST请求
    response3 = make_api_request(
        "https://api.example.com/users",
        method="POST",
        json={"name": "张三", "email": "zhangsan@example.com"},
        headers={"Content-Type": "application/json"},
        auth=("username", "password"),
        retry_count=3,
        cache_enabled=True
    )
    print(f"\nPOST请求: {response3}")
    
    print("\n数据库查询测试:")
    
    # 简单查询
    query1 = create_database_query("users", name="张三", age=25)
    print(f"简单查询: {query1}")
    
    # 复杂查询
    query2 = create_database_query(
        "products",
        category="electronics",
        price={"gte": 100, "lte": 1000},
        status="active",
        select="id, name, price",
        order_by={"price": "desc", "name": "asc"},
        limit=20,
        offset=0
    )
    print(f"复杂查询: {query2}")
    
    # 带IN条件的查询
    query3 = create_database_query(
        "orders",
        status={"in": ["pending", "processing", "shipped"]},
        customer_name={"like": "%张%"},
        order_by="created_at desc",
        limit=50
    )
    print(f"IN条件查询: {query3}")
    
    print("\n日志配置测试:")
    
    # 基础配置
    logger1 = configure_logger("app", level="DEBUG")
    print(f"基础日志配置: {logger1}")
    
    # 文件日志配置
    logger2 = configure_logger(
        "database",
        level="WARNING",
        file="/var/log/database.log",
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=["console", "file"]
    )
    print(f"\n文件日志配置: {logger2}")
    
    # 完整配置
    logger3 = configure_logger(
        "api",
        level="INFO",
        file={
            "path": "/var/log/api.log",
            "max_size": "10MB",
            "backup_count": 5
        },
        email={
            "smtp_server": "smtp.company.com",
            "recipients": ["admin@company.com"],
            "level": "ERROR"
        },
        format="%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s",
        handlers=["console", "file", "email"]
    )
    print(f"\n完整日志配置: {logger3}")
    
    print("-" * 50)

# 运行练习4
exercise_4_keyword_args()
```

## 练习5：参数组合练习

### 任务描述
创建一个数据处理管道，合理组合使用各种参数类型。

```python
def exercise_5_parameter_combinations():
    """
    练习5：参数组合练习
    创建数据处理管道
    """
    print("🔄 练习5：参数组合练习")
    print("-" * 50)
    
    def create_data_pipeline(name, *processors, input_format="json", 
                           output_format="json", **options):
        """
        创建数据处理管道
        
        name: 管道名称（位置参数）
        *processors: 处理器函数列表（可变参数）
        input_format: 输入格式（默认参数）
        output_format: 输出格式（默认参数）
        **options: 其他选项（关键字参数）
        """
        pipeline = {
            "name": name,
            "processors": list(processors),
            "input_format": input_format,
            "output_format": output_format,
            "options": options,
            "created_at": "2024-01-01 12:00:00"
        }
        
        # 验证处理器
        for i, processor in enumerate(processors):
            if not callable(processor):
                raise ValueError(f"处理器 {i+1} 必须是可调用对象")
        
        # 处理选项
        if "parallel" in options:
            pipeline["parallel_processing"] = options["parallel"]
        
        if "batch_size" in options:
            pipeline["batch_size"] = max(1, options["batch_size"])
        
        if "error_handling" in options:
            valid_strategies = ["ignore", "stop", "retry"]
            if options["error_handling"] not in valid_strategies:
                pipeline["error_handling"] = "stop"
            else:
                pipeline["error_handling"] = options["error_handling"]
        
        return pipeline
    
    def execute_pipeline(pipeline, data, *additional_data, 
                        validate_input=True, **execution_options):
        """
        执行数据处理管道
        
        pipeline: 管道配置（位置参数）
        data: 主要数据（位置参数）
        *additional_data: 额外数据（可变参数）
        validate_input: 是否验证输入（默认参数）
        **execution_options: 执行选项（关键字参数）
        """
        print(f"执行管道: {pipeline['name']}")
        
        # 合并所有数据
        all_data = [data] + list(additional_data)
        
        # 输入验证
        if validate_input:
            for i, dataset in enumerate(all_data):
                if not isinstance(dataset, (list, tuple)):
                    raise TypeError(f"数据集 {i+1} 必须是列表或元组")
        
        # 执行处理器
        results = []
        
        for dataset in all_data:
            current_data = dataset.copy() if hasattr(dataset, 'copy') else list(dataset)
            
            for j, processor in enumerate(pipeline["processors"]):
                try:
                    print(f"  应用处理器 {j+1}: {processor.__name__}")
                    current_data = processor(current_data)
                except Exception as e:
                    error_handling = pipeline.get("error_handling", "stop")
                    
                    if error_handling == "ignore":
                        print(f"    忽略错误: {e}")
                        continue
                    elif error_handling == "stop":
                        print(f"    停止执行: {e}")
                        return {"error": str(e), "partial_results": results}
                    elif error_handling == "retry":
                        retry_count = execution_options.get("retry_count", 1)
                        for attempt in range(retry_count):
                            try:
                                print(f"    重试 {attempt + 1}/{retry_count}")
                                current_data = processor(current_data)
                                break
                            except Exception as retry_e:
                                if attempt == retry_count - 1:
                                    print(f"    重试失败: {retry_e}")
                                    return {"error": str(retry_e), "partial_results": results}
            
            results.append(current_data)
        
        execution_summary = {
            "pipeline_name": pipeline["name"],
            "processed_datasets": len(all_data),
            "processors_applied": len(pipeline["processors"]),
            "results": results,
            "execution_options": execution_options
        }
        
        return execution_summary
    
    def create_report_generator(title, *sections, format="text", 
                              include_timestamp=True, **formatting_options):
        """
        创建报告生成器
        
        title: 报告标题（位置参数）
        *sections: 报告章节（可变参数）
        format: 输出格式（默认参数）
        include_timestamp: 是否包含时间戳（默认参数）
        **formatting_options: 格式化选项（关键字参数）
        """
        def generate_report(data):
            """生成报告的内部函数"""
            report_lines = []
            
            # 标题
            if format == "text":
                separator = formatting_options.get("separator", "=")
                title_line = f" {title} "
                border = separator * len(title_line)
                report_lines.extend([border, title_line, border, ""])
            elif format == "markdown":
                report_lines.extend([f"# {title}", ""])
            
            # 时间戳
            if include_timestamp:
                timestamp = "2024-01-01 12:00:00"  # 模拟时间戳
                if format == "text":
                    report_lines.extend([f"生成时间: {timestamp}", ""])
                elif format == "markdown":
                    report_lines.extend([f"*生成时间: {timestamp}*", ""])
            
            # 章节内容
            for i, section in enumerate(sections):
                if callable(section):
                    # 如果章节是函数，调用它生成内容
                    section_content = section(data)
                else:
                    # 如果章节是字符串，直接使用
                    section_content = str(section)
                
                if format == "text":
                    report_lines.extend([f"第{i+1}节:", section_content, ""])
                elif format == "markdown":
                    report_lines.extend([f"## 第{i+1}节", section_content, ""])
            
            return "\n".join(report_lines)
        
        return generate_report
    
    # 定义一些处理器函数
    def double_values(data):
        """将所有值翻倍"""
        return [x * 2 for x in data]
    
    def filter_positive(data):
        """过滤正数"""
        return [x for x in data if x > 0]
    
    def sort_data(data):
        """排序数据"""
        return sorted(data)
    
    def calculate_sum(data):
        """计算总和"""
        return [sum(data)]
    
    def add_noise(data):
        """添加噪声（可能出错的处理器）"""
        if len(data) > 10:
            raise ValueError("数据太多，无法处理")
        return [x + 0.1 for x in data]
    
    # 定义报告章节函数
    def summary_section(data):
        """摘要章节"""
        if isinstance(data, dict) and "results" in data:
            results = data["results"]
            return f"处理了 {len(results)} 个数据集，共 {sum(len(r) for r in results)} 个数据点"
        return "数据摘要不可用"
    
    def details_section(data):
        """详细信息章节"""
        if isinstance(data, dict) and "results" in data:
            details = []
            for i, result in enumerate(data["results"]):
                details.append(f"数据集 {i+1}: {result}")
            return "\n".join(details)
        return "详细信息不可用"
    
    # 测试用例
    print("创建数据处理管道:")
    
    # 基础管道
    pipeline1 = create_data_pipeline(
        "基础处理管道",
        double_values,
        filter_positive,
        sort_data
    )
    print(f"基础管道: {pipeline1}")
    
    # 高级管道
    pipeline2 = create_data_pipeline(
        "高级处理管道",
        double_values,
        filter_positive,
        add_noise,
        calculate_sum,
        input_format="csv",
        output_format="json",
        parallel=True,
        batch_size=100,
        error_handling="retry"
    )
    print(f"\n高级管道: {pipeline2}")
    
    print("\n执行管道:")
    
    # 测试数据
    test_data1 = [1, -2, 3, -4, 5]
    test_data2 = [10, 20, 30]
    test_data3 = [100, -200, 300, -400, 500, 600, 700, 800, 900, 1000, 1100]  # 会触发错误
    
    # 执行基础管道
    result1 = execute_pipeline(pipeline1, test_data1, test_data2)
    print(f"基础管道结果: {result1}")
    
    # 执行高级管道（会出错）
    result2 = execute_pipeline(
        pipeline2, 
        test_data3,
        validate_input=True,
        retry_count=2,
        debug_mode=True
    )
    print(f"\n高级管道结果: {result2}")
    
    print("\n生成报告:")
    
    # 创建报告生成器
    report_generator = create_report_generator(
        "数据处理报告",
        summary_section,
        details_section,
        "结论: 数据处理完成",
        format="text",
        separator="-",
        include_metadata=True
    )
    
    # 生成报告
    report = report_generator(result1)
    print(report)
    
    # Markdown格式报告
    md_report_generator = create_report_generator(
        "数据处理报告 (Markdown)",
        summary_section,
        details_section,
        format="markdown",
        include_timestamp=True
    )
    
    md_report = md_report_generator(result1)
    print(f"\nMarkdown报告:\n{md_report}")
    
    print("-" * 50)

# 运行练习5
exercise_5_parameter_combinations()
```

## 运行所有练习

```python
def main():
    """
    运行所有练习
    """
    print("🎯 函数参数综合练习")
    print("=" * 60)
    
    exercises = [
        exercise_1_basic_parameters,
        exercise_2_default_parameters,
        exercise_3_variable_args,
        exercise_4_keyword_args,
        exercise_5_parameter_combinations
    ]
    
    for i, exercise in enumerate(exercises, 1):
        print(f"\n{'='*20} 练习 {i} {'='*20}")
        try:
            exercise()
        except Exception as e:
            print(f"练习 {i} 执行出错: {e}")
        print("\n" + "="*50)
    
    print("\n🎉 所有练习完成！")
    print("\n学习要点总结:")
    print("1. 位置参数：按顺序传递，必须提供")
    print("2. 关键字参数：按名称传递，提高可读性")
    print("3. 默认参数：提供默认值，增加函数灵活性")
    print("4. *args：处理可变数量的位置参数")
    print("5. **kwargs：处理可变数量的关键字参数")
    print("6. 参数组合：合理组合不同类型的参数")
    print("7. 参数验证：确保函数接收正确的输入")
    print("8. 实际应用：将参数技巧应用到真实项目中")

if __name__ == "__main__":
    main()
```

## 运行练习

要运行这些练习，请使用以下命令：

```bash
python3 09_exercises.py
```

## 学习要点

### 核心概念

1. **参数类型理解**：掌握不同参数类型的特点和使用场景
2. **参数顺序规则**：理解参数定义的正确顺序
3. **灵活性设计**：学会设计灵活且易用的函数接口
4. **错误处理**：实现健壮的参数验证和错误处理

### 实际应用

1. **API设计**：创建清晰、灵活的API接口
2. **配置管理**：使用参数技巧简化配置处理
3. **数据处理**：构建可扩展的数据处理管道
4. **工具函数**：编写通用、可重用的工具函数

### 最佳实践

1. **参数命名**：使用清晰、描述性的参数名
2. **文档编写**：为函数参数提供详细的文档说明
3. **类型提示**：使用类型提示提高代码可读性
4. **测试覆盖**：为不同的参数组合编写测试用例

### 下一步学习

完成这些练习后，建议继续学习：

1. **装饰器**：学习如何使用装饰器增强函数功能
2. **生成器**：掌握生成器函数的使用
3. **异步函数**：了解异步编程中的参数处理
4. **类方法**：学习类中方法的参数处理技巧

通过这些综合练习，你应该能够熟练掌握Python函数参数的各种用法，并能在实际项目中灵活应用这些技巧。