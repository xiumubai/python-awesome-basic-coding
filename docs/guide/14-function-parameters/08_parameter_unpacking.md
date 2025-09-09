# 参数解包

参数解包是Python中一个强大的特性，它允许我们将序列（如列表、元组）和字典中的元素作为独立的参数传递给函数。这个特性与函数定义中的*args和**kwargs相对应，提供了灵活的参数传递方式。

## 核心概念

### 什么是参数解包？
参数解包是指在函数调用时，使用特殊的语法将容器类型的数据（列表、元组、字典等）"解包"成独立的参数。Python提供了两种解包操作符：

- **单星号（*）**：用于解包序列类型（列表、元组等）
- **双星号（**）**：用于解包字典类型

### 基本语法

```python
def demonstrate_unpacking():
    """
    演示参数解包的基本概念
    """
    print("🎯 参数解包基本概念演示")
    print("-" * 40)
    
    # 定义一个简单的函数
    def greet(name, age, city):
        return f"你好，我是{name}，{age}岁，来自{city}"
    
    # 传统的参数传递方式
    result1 = greet("Alice", 25, "北京")
    print(f"传统方式: {result1}")
    
    # 使用序列解包
    person_info = ["Bob", 30, "上海"]
    result2 = greet(*person_info)  # 解包列表
    print(f"序列解包: {result2}")
    
    # 使用字典解包
    person_dict = {"name": "Charlie", "age": 28, "city": "广州"}
    result3 = greet(**person_dict)  # 解包字典
    print(f"字典解包: {result3}")
    
    print("-" * 40)

# 运行基本演示
demonstrate_unpacking()
```

## 序列解包（*操作符）

### 基本序列解包

```python
def basic_sequence_unpacking():
    """
    演示基本的序列解包
    """
    print("📦 基本序列解包演示")
    print("-" * 40)
    
    def calculate_area(length, width, height=1):
        """计算面积或体积"""
        if height == 1:
            result = length * width
            print(f"面积计算: {length} × {width} = {result}")
        else:
            result = length * width * height
            print(f"体积计算: {length} × {width} × {height} = {result}")
        return result
    
    # 使用列表解包
    dimensions_2d = [10, 5]
    area = calculate_area(*dimensions_2d)
    
    # 使用元组解包
    dimensions_3d = (8, 6, 4)
    volume = calculate_area(*dimensions_3d)
    
    # 使用字符串解包（字符串也是序列）
    coords = "35"
    try:
        result = calculate_area(*coords)  # 解包为 '3', '5'
        print(f"字符串解包结果: {result}")
    except TypeError as e:
        print(f"字符串解包错误: {e}")
    
    # 使用range解包
    range_values = range(2, 5)  # 生成 2, 3, 4
    result = calculate_area(*range_values)
    
    print("-" * 40)

def advanced_sequence_unpacking():
    """
    高级序列解包技巧
    """
    print("🚀 高级序列解包技巧")
    print("-" * 40)
    
    def process_scores(*scores):
        """处理分数"""
        if not scores:
            return "没有分数"
        
        total = sum(scores)
        average = total / len(scores)
        max_score = max(scores)
        min_score = min(scores)
        
        print(f"分数: {scores}")
        print(f"总分: {total}, 平均分: {average:.2f}")
        print(f"最高分: {max_score}, 最低分: {min_score}")
        
        return {
            "total": total,
            "average": average,
            "max": max_score,
            "min": min_score
        }
    
    # 解包不同类型的序列
    list_scores = [85, 92, 78, 96, 88]
    result1 = process_scores(*list_scores)
    
    tuple_scores = (90, 87, 93, 89)
    result2 = process_scores(*tuple_scores)
    
    # 组合多个序列
    math_scores = [95, 88]
    english_scores = [92, 85, 90]
    science_scores = (89, 94)
    
    # 将多个序列组合解包
    all_scores = [*math_scores, *english_scores, *science_scores]
    print(f"组合后的分数: {all_scores}")
    result3 = process_scores(*all_scores)
    
    print("-" * 40)

# 运行序列解包示例
basic_sequence_unpacking()
advanced_sequence_unpacking()
```

### 部分解包和剩余参数

```python
def partial_unpacking_examples():
    """
    演示部分解包和剩余参数处理
    """
    print("🎪 部分解包和剩余参数")
    print("-" * 40)
    
    def analyze_data(first, second, *rest):
        """分析数据，处理前两个和剩余的"""
        print(f"第一个数据: {first}")
        print(f"第二个数据: {second}")
        print(f"剩余数据: {rest}")
        print(f"剩余数据数量: {len(rest)}")
        
        if rest:
            print(f"剩余数据总和: {sum(rest) if all(isinstance(x, (int, float)) for x in rest) else '无法计算'}")
        
        return {"first": first, "second": second, "rest": rest}
    
    # 解包时的部分使用
    data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 全部解包
    result1 = analyze_data(*data_list)
    
    # 部分解包 - 只取前几个
    result2 = analyze_data(*data_list[:5])
    
    # 使用切片和解包
    first_part = data_list[:2]
    remaining_part = data_list[2:]
    print(f"\n分割数据:")
    print(f"前两个: {first_part}")
    print(f"剩余的: {remaining_part}")
    
    # 分别解包
    result3 = analyze_data(*first_part, *remaining_part)
    
    print("-" * 40)

def nested_unpacking_examples():
    """
    演示嵌套结构的解包
    """
    print("🏗️  嵌套结构解包")
    print("-" * 40)
    
    def create_matrix(rows, cols, *values):
        """创建矩阵"""
        print(f"创建 {rows}×{cols} 矩阵")
        print(f"提供的值: {values}")
        
        if len(values) != rows * cols:
            print(f"警告: 需要 {rows * cols} 个值，但提供了 {len(values)} 个")
            # 填充不足的值
            values = list(values) + [0] * (rows * cols - len(values))
        
        matrix = []
        for i in range(rows):
            row = list(values[i * cols:(i + 1) * cols])
            matrix.append(row)
        
        print(f"生成的矩阵:")
        for row in matrix:
            print(f"  {row}")
        
        return matrix
    
    # 嵌套列表解包
    nested_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # 展平嵌套列表
    flattened = []
    for sublist in nested_data:
        flattened.extend(sublist)
    
    print(f"原始嵌套数据: {nested_data}")
    print(f"展平后的数据: {flattened}")
    
    # 解包展平的数据
    matrix = create_matrix(3, 3, *flattened)
    
    # 使用列表推导式展平并解包
    flattened_comprehension = [item for sublist in nested_data for item in sublist]
    print(f"\n使用列表推导式展平: {flattened_comprehension}")
    
    matrix2 = create_matrix(2, 4, *flattened_comprehension[:8])
    
    print("-" * 40)

# 运行部分解包示例
partial_unpacking_examples()
nested_unpacking_examples()
```

## 字典解包（**操作符）

### 基本字典解包

```python
def basic_dictionary_unpacking():
    """
    演示基本的字典解包
    """
    print("📚 基本字典解包演示")
    print("-" * 40)
    
    def create_user_profile(username, email, age=18, active=True, **extra_info):
        """创建用户档案"""
        profile = {
            "username": username,
            "email": email,
            "age": age,
            "active": active,
            "created_at": "2024-01-01 12:00:00"
        }
        
        # 添加额外信息
        profile.update(extra_info)
        
        print(f"创建用户档案:")
        for key, value in profile.items():
            print(f"  {key}: {value}")
        
        return profile
    
    # 使用字典解包
    user_data = {
        "username": "alice",
        "email": "alice@example.com",
        "age": 25,
        "city": "北京",
        "department": "Engineering"
    }
    
    profile1 = create_user_profile(**user_data)
    
    # 部分字典解包
    basic_info = {"username": "bob", "email": "bob@example.com"}
    additional_info = {"age": 30, "city": "上海", "skills": ["Python", "JavaScript"]}
    
    # 组合多个字典
    profile2 = create_user_profile(**basic_info, **additional_info)
    
    # 混合使用位置参数和字典解包
    profile3 = create_user_profile(
        "charlie", 
        "charlie@example.com",
        **{"age": 28, "city": "广州", "active": False}
    )
    
    print("-" * 40)

def advanced_dictionary_unpacking():
    """
    高级字典解包技巧
    """
    print("🎯 高级字典解包技巧")
    print("-" * 40)
    
    def configure_database(**config):
        """配置数据库连接"""
        # 默认配置
        default_config = {
            "host": "localhost",
            "port": 5432,
            "database": "myapp",
            "username": "user",
            "password": "password",
            "ssl_mode": "prefer",
            "timeout": 30,
            "pool_size": 10
        }
        
        # 合并配置
        final_config = {**default_config, **config}
        
        print(f"数据库配置:")
        for key, value in final_config.items():
            # 隐藏敏感信息
            if key == "password":
                print(f"  {key}: {'*' * len(str(value))}")
            else:
                print(f"  {key}: {value}")
        
        return final_config
    
    # 不同的配置场景
    dev_config = {
        "host": "dev-db.example.com",
        "database": "myapp_dev",
        "ssl_mode": "disable"
    }
    
    prod_config = {
        "host": "prod-db.example.com",
        "port": 5433,
        "database": "myapp_prod",
        "username": "prod_user",
        "password": "secure_password",
        "ssl_mode": "require",
        "pool_size": 50
    }
    
    print("开发环境配置:")
    dev_db_config = configure_database(**dev_config)
    
    print("\n生产环境配置:")
    prod_db_config = configure_database(**prod_config)
    
    # 动态配置构建
    def build_config(environment, **overrides):
        """根据环境构建配置"""
        base_configs = {
            "development": {
                "debug": True,
                "log_level": "DEBUG",
                "cache_enabled": False
            },
            "production": {
                "debug": False,
                "log_level": "WARNING",
                "cache_enabled": True,
                "ssl_required": True
            },
            "testing": {
                "debug": True,
                "log_level": "INFO",
                "cache_enabled": False,
                "database": ":memory:"
            }
        }
        
        base_config = base_configs.get(environment, {})
        final_config = {**base_config, **overrides}
        
        print(f"\n{environment.upper()} 环境配置:")
        for key, value in final_config.items():
            print(f"  {key}: {value}")
        
        return final_config
    
    # 构建不同环境的配置
    dev_app_config = build_config("development", port=8000, workers=1)
    prod_app_config = build_config("production", port=80, workers=8, ssl_cert="/path/to/cert")
    test_app_config = build_config("testing", port=9000)
    
    print("-" * 40)

# 运行字典解包示例
basic_dictionary_unpacking()
advanced_dictionary_unpacking()
```

### 字典合并和过滤

```python
def dictionary_merging_and_filtering():
    """
    演示字典合并和过滤技巧
    """
    print("🔄 字典合并和过滤技巧")
    print("-" * 40)
    
    def merge_configurations(*config_dicts, **additional_config):
        """合并多个配置字典"""
        print(f"合并 {len(config_dicts)} 个配置字典")
        
        # 显示输入的配置
        for i, config in enumerate(config_dicts):
            print(f"  配置 {i+1}: {config}")
        
        if additional_config:
            print(f"  额外配置: {additional_config}")
        
        # 合并所有配置
        merged = {}
        for config in config_dicts:
            merged.update(config)
        merged.update(additional_config)
        
        print(f"合并结果: {merged}")
        return merged
    
    # 多个配置源
    system_config = {"debug": False, "log_level": "INFO", "timeout": 30}
    user_config = {"log_level": "DEBUG", "theme": "dark", "language": "zh-CN"}
    local_config = {"debug": True, "port": 8080, "host": "localhost"}
    
    # 合并配置
    final_config = merge_configurations(
        system_config,
        user_config,
        local_config,
        version="1.0.0",
        environment="development"
    )
    
    def filter_and_transform_config(config, **filters):
        """过滤和转换配置"""
        print(f"\n过滤配置: {config}")
        print(f"过滤条件: {filters}")
        
        result = {}
        
        # 应用过滤器
        include_keys = filters.get("include_keys", [])
        exclude_keys = filters.get("exclude_keys", [])
        key_prefix = filters.get("key_prefix", "")
        value_transform = filters.get("value_transform")
        
        for key, value in config.items():
            # 包含/排除过滤
            if include_keys and key not in include_keys:
                continue
            if exclude_keys and key in exclude_keys:
                continue
            
            # 键名转换
            new_key = f"{key_prefix}{key}" if key_prefix else key
            
            # 值转换
            new_value = value
            if value_transform and callable(value_transform):
                try:
                    new_value = value_transform(value)
                except Exception as e:
                    print(f"    转换 {key} 失败: {e}")
                    new_value = value
            
            result[new_key] = new_value
        
        print(f"过滤结果: {result}")
        return result
    
    # 应用不同的过滤器
    filtered_config1 = filter_and_transform_config(
        final_config,
        include_keys=["debug", "log_level", "port", "host"]
    )
    
    filtered_config2 = filter_and_transform_config(
        final_config,
        exclude_keys=["timeout", "theme"],
        key_prefix="app_"
    )
    
    filtered_config3 = filter_and_transform_config(
        final_config,
        value_transform=lambda x: str(x).upper() if isinstance(x, str) else x
    )
    
    print("-" * 40)

# 运行字典合并和过滤示例
dictionary_merging_and_filtering()
```

## 混合解包

### 序列和字典混合解包

```python
def mixed_unpacking_examples():
    """
    演示序列和字典的混合解包
    """
    print("🎭 混合解包示例")
    print("-" * 40)
    
    def create_report(title, *sections, author="Unknown", **metadata):
        """创建报告"""
        report = {
            "title": title,
            "author": author,
            "sections": list(sections),
            "metadata": metadata,
            "created_at": "2024-01-01 12:00:00",
            "section_count": len(sections)
        }
        
        print(f"📊 创建报告: {title}")
        print(f"   作者: {author}")
        print(f"   章节数: {len(sections)}")
        print(f"   章节: {list(sections)}")
        print(f"   元数据: {metadata}")
        
        return report
    
    # 混合使用序列和字典解包
    report_sections = ["引言", "方法", "结果", "结论"]
    report_info = {
        "author": "张三",
        "department": "研发部",
        "version": "1.0",
        "confidential": False
    }
    
    # 方式1：分别解包
    report1 = create_report(
        "项目分析报告",
        *report_sections,
        **report_info
    )
    
    # 方式2：部分解包
    additional_sections = ["附录A", "附录B"]
    report2 = create_report(
        "详细技术报告",
        *report_sections,
        *additional_sections,
        author="李四",
        **{"type": "技术文档", "priority": "高"}
    )
    
    # 方式3：动态构建参数
    def build_report_args(base_title, section_list, author_name, **extra):
        """动态构建报告参数"""
        args = [f"{base_title} - {author_name}"]
        kwargs = {"author": author_name, **extra}
        
        return args, section_list, kwargs
    
    title_args, sections, report_kwargs = build_report_args(
        "月度总结",
        ["业绩回顾", "问题分析", "改进计划"],
        "王五",
        department="销售部",
        month="2024-01",
        status="已完成"
    )
    
    report3 = create_report(*title_args, *sections, **report_kwargs)
    
    print("-" * 40)

def complex_mixed_unpacking():
    """
    复杂的混合解包场景
    """
    print("🎪 复杂混合解包场景")
    print("-" * 40)
    
    def process_api_request(endpoint, method="GET", *path_parts, **options):
        """处理API请求"""
        # 构建URL
        url = endpoint
        if path_parts:
            url += "/" + "/".join(str(part) for part in path_parts)
        
        # 提取选项
        headers = options.pop("headers", {})
        params = options.pop("params", {})
        data = options.pop("data", {})
        timeout = options.pop("timeout", 30)
        
        # 剩余选项作为配置
        config = options
        
        request_info = {
            "url": url,
            "method": method,
            "headers": headers,
            "params": params,
            "data": data,
            "timeout": timeout,
            "config": config
        }
        
        print(f"🌐 API请求:")
        print(f"   URL: {url}")
        print(f"   方法: {method}")
        print(f"   超时: {timeout}秒")
        if headers:
            print(f"   请求头: {headers}")
        if params:
            print(f"   查询参数: {params}")
        if data:
            print(f"   请求数据: {data}")
        if config:
            print(f"   配置选项: {config}")
        
        return request_info
    
    # 复杂的API调用场景
    base_url = "https://api.example.com"
    api_path = ["v1", "users", "123", "profile"]
    
    request_headers = {
        "Authorization": "Bearer token123",
        "Content-Type": "application/json"
    }
    
    query_parameters = {
        "include": "details,preferences",
        "format": "json"
    }
    
    request_data = {
        "name": "Updated Name",
        "email": "new@example.com"
    }
    
    # 使用混合解包
    api_response = process_api_request(
        base_url,
        "PUT",
        *api_path,
        headers=request_headers,
        params=query_parameters,
        data=request_data,
        timeout=60,
        retry_count=3,
        verify_ssl=True,
        follow_redirects=False
    )
    
    # 批量API调用
    def batch_api_calls(base_endpoint, *call_configs):
        """批量API调用"""
        print(f"\n📦 批量API调用 ({len(call_configs)} 个请求):")
        
        results = []
        for i, config in enumerate(call_configs):
            print(f"\n请求 {i+1}:")
            
            # 解包配置
            method = config.get("method", "GET")
            path_parts = config.get("path", [])
            options = {k: v for k, v in config.items() 
                      if k not in ["method", "path"]}
            
            result = process_api_request(
                base_endpoint,
                method,
                *path_parts,
                **options
            )
            results.append(result)
        
        return results
    
    # 批量调用配置
    api_calls = [
        {
            "method": "GET",
            "path": ["users"],
            "params": {"page": 1, "limit": 10}
        },
        {
            "method": "POST",
            "path": ["users"],
            "data": {"name": "New User", "email": "user@example.com"},
            "headers": {"Content-Type": "application/json"}
        },
        {
            "method": "DELETE",
            "path": ["users", "456"],
            "timeout": 10
        }
    ]
    
    batch_results = batch_api_calls("https://api.example.com/v2", *api_calls)
    
    print("-" * 40)

# 运行混合解包示例
mixed_unpacking_examples()
complex_mixed_unpacking()
```

## 实际应用场景

### 数学运算应用

```python
def math_applications():
    """
    数学运算中的参数解包应用
    """
    print("🔢 数学运算中的参数解包")
    print("-" * 40)
    
    import math
    
    def calculate_distance(*points):
        """计算多点之间的距离"""
        if len(points) < 2:
            return 0
        
        total_distance = 0
        print(f"计算路径距离，经过 {len(points)} 个点:")
        
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            total_distance += distance
            
            print(f"  点{i+1}({x1}, {y1}) -> 点{i+2}({x2}, {y2}): {distance:.2f}")
        
        print(f"总距离: {total_distance:.2f}")
        return total_distance
    
    # 使用坐标列表
    coordinates = [(0, 0), (3, 4), (6, 8), (10, 0)]
    total_dist = calculate_distance(*coordinates)
    
    def solve_quadratic(a, b, c):
        """解二次方程 ax² + bx + c = 0"""
        print(f"解方程: {a}x² + {b}x + {c} = 0")
        
        discriminant = b**2 - 4*a*c
        
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            print(f"两个实根: x1 = {x1:.2f}, x2 = {x2:.2f}")
            return x1, x2
        elif discriminant == 0:
            x = -b / (2*a)
            print(f"一个重根: x = {x:.2f}")
            return x,
        else:
            real_part = -b / (2*a)
            imag_part = math.sqrt(-discriminant) / (2*a)
            print(f"两个复根: x1 = {real_part:.2f} + {imag_part:.2f}i")
            print(f"          x2 = {real_part:.2f} - {imag_part:.2f}i")
            return complex(real_part, imag_part), complex(real_part, -imag_part)
    
    # 使用系数列表解包
    equations = [
        [1, -5, 6],    # x² - 5x + 6 = 0
        [1, -2, 1],    # x² - 2x + 1 = 0
        [1, 0, 1],     # x² + 1 = 0
        [2, -7, 3]     # 2x² - 7x + 3 = 0
    ]
    
    print(f"\n解多个二次方程:")
    for i, coeffs in enumerate(equations):
        print(f"\n方程 {i+1}:")
        roots = solve_quadratic(*coeffs)
    
    def matrix_multiply(matrix_a, matrix_b):
        """矩阵乘法"""
        rows_a, cols_a = len(matrix_a), len(matrix_a[0])
        rows_b, cols_b = len(matrix_b), len(matrix_b[0])
        
        if cols_a != rows_b:
            raise ValueError(f"矩阵维度不匹配: {rows_a}×{cols_a} 和 {rows_b}×{cols_b}")
        
        print(f"矩阵乘法: {rows_a}×{cols_a} × {rows_b}×{cols_b} = {rows_a}×{cols_b}")
        
        result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
        
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result[i][j] += matrix_a[i][k] * matrix_b[k][j]
        
        print(f"结果矩阵:")
        for row in result:
            print(f"  {row}")
        
        return result
    
    # 使用解包传递矩阵
    matrix_data = [
        [[1, 2], [3, 4]],           # 矩阵A
        [[5, 6], [7, 8]]            # 矩阵B
    ]
    
    result_matrix = matrix_multiply(*matrix_data)
    
    print("-" * 40)

# 运行数学应用示例
math_applications()
```

### 配置管理应用

```python
def configuration_management():
    """
    配置管理中的参数解包应用
    """
    print("⚙️  配置管理中的参数解包")
    print("-" * 40)
    
    class ConfigManager:
        """配置管理器"""
        
        def __init__(self, **base_config):
            self.config = base_config.copy()
            print(f"初始化配置管理器")
            if base_config:
                print(f"基础配置: {base_config}")
        
        def load_from_dict(self, config_dict, **overrides):
            """从字典加载配置"""
            print(f"从字典加载配置: {config_dict}")
            if overrides:
                print(f"覆盖配置: {overrides}")
            
            # 合并配置
            merged_config = {**self.config, **config_dict, **overrides}
            self.config = merged_config
            
            print(f"合并后配置: {self.config}")
            return self
        
        def load_from_multiple_sources(self, *config_sources, **final_overrides):
            """从多个配置源加载"""
            print(f"从 {len(config_sources)} 个配置源加载")
            
            for i, source in enumerate(config_sources):
                print(f"  配置源 {i+1}: {source}")
                self.config.update(source)
            
            if final_overrides:
                print(f"最终覆盖: {final_overrides}")
                self.config.update(final_overrides)
            
            print(f"最终配置: {self.config}")
            return self
        
        def get_section_config(self, section_name, **defaults):
            """获取特定段的配置"""
            section_config = {**defaults}
            
            # 提取以section_name开头的配置项
            prefix = f"{section_name}_"
            for key, value in self.config.items():
                if key.startswith(prefix):
                    section_key = key[len(prefix):]
                    section_config[section_key] = value
            
            print(f"{section_name} 段配置: {section_config}")
            return section_config
        
        def apply_environment_config(self, environment, **env_overrides):
            """应用环境特定配置"""
            env_configs = {
                "development": {
                    "debug": True,
                    "log_level": "DEBUG",
                    "db_pool_size": 5,
                    "cache_enabled": False
                },
                "testing": {
                    "debug": True,
                    "log_level": "INFO",
                    "db_pool_size": 2,
                    "cache_enabled": False,
                    "db_name": "test_db"
                },
                "production": {
                    "debug": False,
                    "log_level": "WARNING",
                    "db_pool_size": 20,
                    "cache_enabled": True,
                    "ssl_required": True
                }
            }
            
            env_config = env_configs.get(environment, {})
            print(f"应用 {environment} 环境配置: {env_config}")
            
            if env_overrides:
                print(f"环境覆盖配置: {env_overrides}")
                env_config = {**env_config, **env_overrides}
            
            self.config.update(env_config)
            print(f"应用后配置: {self.config}")
            return self
    
    # 使用配置管理器
    config_manager = ConfigManager(
        app_name="MyApp",
        version="1.0.0",
        port=8000
    )
    
    # 多个配置源
    system_config = {
        "system_timezone": "UTC",
        "system_encoding": "utf-8",
        "max_memory": "1GB"
    }
    
    user_config = {
        "user_theme": "dark",
        "user_language": "zh-CN",
        "user_notifications": True
    }
    
    local_config = {
        "local_storage_path": "/tmp/myapp",
        "local_cache_size": "100MB"
    }
    
    # 加载多个配置源
    config_manager.load_from_multiple_sources(
        system_config,
        user_config,
        local_config,
        runtime_mode="server",
        startup_time="2024-01-01 12:00:00"
    )
    
    # 应用环境配置
    config_manager.apply_environment_config(
        "production",
        db_pool_size=50,
        custom_feature_enabled=True
    )
    
    # 获取特定段配置
    db_config = config_manager.get_section_config(
        "db",
        host="localhost",
        port=5432,
        timeout=30
    )
    
    user_section_config = config_manager.get_section_config(
        "user",
        default_role="guest",
        session_timeout=3600
    )
    
    print("-" * 40)

# 运行配置管理示例
configuration_management()
```

### 装饰器应用

```python
def decorator_applications():
    """
    装饰器中的参数解包应用
    """
    print("🎨 装饰器中的参数解包")
    print("-" * 40)
    
    def timing_decorator(**decorator_options):
        """计时装饰器"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                import time
                
                # 装饰器选项
                show_args = decorator_options.get("show_args", False)
                show_result = decorator_options.get("show_result", False)
                unit = decorator_options.get("unit", "seconds")
                precision = decorator_options.get("precision", 4)
                
                print(f"⏱️  开始执行: {func.__name__}")
                
                if show_args:
                    print(f"   参数: args={args}, kwargs={kwargs}")
                
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                
                execution_time = end_time - start_time
                
                if unit == "milliseconds":
                    execution_time *= 1000
                    unit_symbol = "ms"
                elif unit == "microseconds":
                    execution_time *= 1000000
                    unit_symbol = "μs"
                else:
                    unit_symbol = "s"
                
                print(f"   执行时间: {execution_time:.{precision}f} {unit_symbol}")
                
                if show_result:
                    print(f"   返回值: {result}")
                
                return result
            return wrapper
        return decorator
    
    def retry_decorator(*retry_args, **retry_options):
        """重试装饰器，支持位置参数和关键字参数"""
        # 处理不同的调用方式
        if len(retry_args) == 1 and callable(retry_args[0]):
            # 直接装饰，没有参数
            func = retry_args[0]
            max_retries = 3
            delay = 1
            exceptions = (Exception,)
        else:
            # 带参数装饰
            func = None
            max_retries = retry_args[0] if retry_args else retry_options.get("max_retries", 3)
            delay = retry_options.get("delay", 1)
            exceptions = retry_options.get("exceptions", (Exception,))
        
        def decorator(f):
            def wrapper(*args, **kwargs):
                print(f"🔄 重试装饰器: {f.__name__}")
                print(f"   最大重试次数: {max_retries}")
                print(f"   延迟: {delay}秒")
                print(f"   捕获异常: {[e.__name__ for e in exceptions]}")
                
                for attempt in range(max_retries + 1):
                    try:
                        if attempt > 0:
                            print(f"   第 {attempt} 次重试")
                            import time
                            time.sleep(delay)
                        
                        result = f(*args, **kwargs)
                        
                        if attempt > 0:
                            print(f"   重试成功")
                        
                        return result
                    
                    except exceptions as e:
                        if attempt == max_retries:
                            print(f"   重试失败，已达到最大次数")
                            raise e
                        else:
                            print(f"   尝试 {attempt + 1} 失败: {e}")
                
            return wrapper
        
        if func:
            return decorator(func)
        else:
            return decorator
    
    # 使用装饰器
    @timing_decorator(show_args=True, show_result=True, unit="milliseconds")
    def calculate_fibonacci(n):
        """计算斐波那契数列"""
        if n <= 1:
            return n
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
    
    @retry_decorator(3, delay=0.1, exceptions=(ValueError, ZeroDivisionError))
    def unreliable_division(a, b, fail_rate=0.7):
        """不稳定的除法函数"""
        import random
        
        if random.random() < fail_rate:
            if random.choice([True, False]):
                raise ValueError("随机值错误")
            else:
                raise ZeroDivisionError("随机除零错误")
        
        return a / b
    
    # 测试装饰器
    print("测试计时装饰器:")
    fib_result = calculate_fibonacci(10)
    
    print("\n测试重试装饰器:")
    try:
        division_result = unreliable_division(10, 2, fail_rate=0.5)
        print(f"除法结果: {division_result}")
    except Exception as e:
        print(f"最终失败: {e}")
    
    # 动态创建装饰器
    def create_logging_decorator(*log_args, **log_options):
        """动态创建日志装饰器"""
        log_level = log_args[0] if log_args else log_options.get("level", "INFO")
        log_format = log_options.get("format", "[{level}] {func_name}: {message}")
        include_timestamp = log_options.get("timestamp", False)
        
        def decorator(func):
            def wrapper(*args, **kwargs):
                timestamp = ""
                if include_timestamp:
                    import datetime
                    timestamp = f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
                
                log_message = log_format.format(
                    level=log_level,
                    func_name=func.__name__,
                    message=f"调用参数: args={args}, kwargs={kwargs}"
                )
                
                print(f"{timestamp}{log_message}")
                
                result = func(*args, **kwargs)
                
                result_message = log_format.format(
                    level=log_level,
                    func_name=func.__name__,
                    message=f"返回结果: {result}"
                )
                
                print(f"{timestamp}{result_message}")
                
                return result
            return wrapper
        return decorator
    
    # 使用动态装饰器
    custom_logger = create_logging_decorator(
        "DEBUG",
        format="[{level}] {func_name} -> {message}",
        timestamp=True
    )
    
    @custom_logger
    def add_numbers(a, b, c=0):
        """加法函数"""
        return a + b + c
    
    print("\n测试动态日志装饰器:")
    sum_result = add_numbers(1, 2, c=3)
    
    print("-" * 40)

# 运行装饰器应用示例
decorator_applications()
```

## 注意事项和最佳实践

### 常见陷阱和解决方案

```python
def common_pitfalls_and_solutions():
    """
    参数解包的常见陷阱和解决方案
    """
    print("⚠️  参数解包常见陷阱")
    print("-" * 40)
    
    # 陷阱1：参数数量不匹配
    def function_with_fixed_params(a, b, c):
        return a + b + c
    
    print("陷阱1：参数数量不匹配")
    
    # 正确的用法
    correct_args = [1, 2, 3]
    result = function_with_fixed_params(*correct_args)
    print(f"正确: {correct_args} -> {result}")
    
    # 错误的用法（参数过少）
    try:
        insufficient_args = [1, 2]
        result = function_with_fixed_params(*insufficient_args)
    except TypeError as e:
        print(f"错误（参数过少）: {insufficient_args} -> {e}")
    
    # 错误的用法（参数过多）
    try:
        excessive_args = [1, 2, 3, 4, 5]
        result = function_with_fixed_params(*excessive_args)
    except TypeError as e:
        print(f"错误（参数过多）: {excessive_args} -> {e}")
    
    # 解决方案：使用切片控制参数数量
    safe_args = excessive_args[:3]  # 只取前3个
    result = function_with_fixed_params(*safe_args)
    print(f"解决方案（切片）: {safe_args} -> {result}")
    
    print()
    
    # 陷阱2：字典键名不匹配
    def function_with_named_params(name, age, city="Unknown"):
        return f"{name}, {age}岁, 来自{city}"
    
    print("陷阱2：字典键名不匹配")
    
    # 正确的用法
    correct_dict = {"name": "Alice", "age": 25, "city": "北京"}
    result = function_with_named_params(**correct_dict)
    print(f"正确: {correct_dict} -> {result}")
    
    # 错误的用法（键名不匹配）
    try:
        wrong_keys = {"username": "Bob", "years": 30, "location": "上海"}
        result = function_with_named_params(**wrong_keys)
    except TypeError as e:
        print(f"错误（键名不匹配）: {wrong_keys} -> {e}")
    
    # 解决方案：键名映射
    def safe_dict_unpack(func, param_dict, key_mapping=None):
        """安全的字典解包"""
        if key_mapping:
            mapped_dict = {}
            for old_key, new_key in key_mapping.items():
                if old_key in param_dict:
                    mapped_dict[new_key] = param_dict[old_key]
            return func(**mapped_dict)
        else:
            return func(**param_dict)
    
    key_mapping = {"username": "name", "years": "age", "location": "city"}
    result = safe_dict_unpack(function_with_named_params, wrong_keys, key_mapping)
    print(f"解决方案（键名映射）: {result}")
    
    print()
    
    # 陷阱3：可变对象作为默认参数
    print("陷阱3：可变对象的解包")
    
    def append_to_list(item, target_list=[]):
        """错误的默认参数用法"""
        target_list.append(item)
        return target_list
    
    # 演示问题
    result1 = append_to_list(1)
    result2 = append_to_list(2)
    print(f"问题演示: result1={result1}, result2={result2}")
    
    # 正确的做法
    def append_to_list_correct(item, target_list=None):
        """正确的默认参数用法"""
        if target_list is None:
            target_list = []
        target_list.append(item)
        return target_list
    
    result3 = append_to_list_correct(1)
    result4 = append_to_list_correct(2)
    print(f"正确做法: result3={result3}, result4={result4}")
    
    # 在解包时的应用
    def process_lists(*lists, processor=None):
        """处理多个列表"""
        if processor is None:
            processor = lambda x: x  # 默认处理器
        
        results = []
        for lst in lists:
            processed = [processor(item) for item in lst]
            results.append(processed)
        
        return results
    
    list_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    processed_results = process_lists(*list_data, processor=lambda x: x * 2)
    print(f"列表处理结果: {processed_results}")
    
    print("-" * 40)

def best_practices():
    """
    参数解包的最佳实践
    """
    print("✅ 参数解包最佳实践")
    print("-" * 40)
    
    # 最佳实践1：参数验证
    def validated_function(*args, **kwargs):
        """带参数验证的函数"""
        print(f"接收参数: args={args}, kwargs={kwargs}")
        
        # 验证位置参数
        if len(args) < 2:
            raise ValueError("至少需要2个位置参数")
        
        # 验证关键字参数
        required_keys = {"name", "type"}
        provided_keys = set(kwargs.keys())
        missing_keys = required_keys - provided_keys
        
        if missing_keys:
            raise ValueError(f"缺少必需的关键字参数: {missing_keys}")
        
        # 验证参数类型
        if not isinstance(kwargs["name"], str):
            raise TypeError("name 必须是字符串")
        
        print(f"参数验证通过")
        return {"args": args, "kwargs": kwargs}
    
    # 正确使用
    try:
        result = validated_function(1, 2, 3, name="test", type="demo", extra="value")
        print(f"验证成功: {result}")
    except (ValueError, TypeError) as e:
        print(f"验证失败: {e}")
    
    print()
    
    # 最佳实践2：文档化参数
    def well_documented_function(*data_sources, output_format="json", **processing_options):
        """
        处理多个数据源的函数
        
        Args:
            *data_sources: 数据源列表，每个数据源应该是字典或列表
            output_format: 输出格式，支持 'json', 'csv', 'xml'
            **processing_options: 处理选项
                - validate (bool): 是否验证数据，默认True
                - sort_by (str): 排序字段
                - limit (int): 限制结果数量
                - filter_func (callable): 过滤函数
        
        Returns:
            处理后的数据
        
        Examples:
            >>> process_data([1,2,3], [4,5,6], output_format="json")
            >>> process_data(*data_list, validate=False, limit=10)
        """
        print(f"处理 {len(data_sources)} 个数据源")
        print(f"输出格式: {output_format}")
        print(f"处理选项: {processing_options}")
        
        # 实际处理逻辑...
        result = {
            "sources_count": len(data_sources),
            "format": output_format,
            "options": processing_options,
            "processed_data": list(data_sources)
        }
        
        return result
    
    # 使用示例
    data1 = [1, 2, 3, 4, 5]
    data2 = [6, 7, 8, 9, 10]
    data3 = [11, 12, 13, 14, 15]
    
    result = well_documented_function(
        data1, data2, data3,
        output_format="csv",
        validate=True,
        sort_by="value",
        limit=20,
        custom_option="custom_value"
    )
    
    print(f"处理结果: {result}")
    
    print()
    
    # 最佳实践3：错误处理
    def robust_unpacking_function(*args, **kwargs):
        """健壮的参数解包函数"""
        try:
            # 参数预处理
            processed_args = []
            for arg in args:
                if isinstance(arg, (list, tuple)):
                    processed_args.extend(arg)
                else:
                    processed_args.append(arg)
            
            # 关键字参数预处理
            processed_kwargs = {}
            for key, value in kwargs.items():
                # 清理键名
                clean_key = key.strip().lower().replace(" ", "_")
                processed_kwargs[clean_key] = value
            
            print(f"预处理后参数:")
            print(f"  args: {processed_args}")
            print(f"  kwargs: {processed_kwargs}")
            
            # 模拟处理
            result = {
                "processed_args": processed_args,
                "processed_kwargs": processed_kwargs,
                "status": "success"
            }
            
            return result
            
        except Exception as e:
            print(f"处理出错: {e}")
            return {
                "error": str(e),
                "status": "failed",
                "original_args": args,
                "original_kwargs": kwargs
            }
    
    # 测试健壮性
    test_cases = [
        ([1, 2, [3, 4], (5, 6)], {"Name ": "Test", " Type": "Demo"}),
        (["a", "b"], {"count": 10, "enabled": True}),
        ([], {}),  # 空参数
    ]
    
    for i, (args, kwargs) in enumerate(test_cases):
        print(f"\n测试用例 {i+1}:")
        result = robust_unpacking_function(*args, **kwargs)
        print(f"结果: {result}")
    
    print("-" * 40)

# 运行陷阱和最佳实践示例
common_pitfalls_and_solutions()
best_practices()
```

## 运行示例

要运行这个参数解包示例，请使用以下命令：

```bash
python3 07_parameter_unpacking.py
```

## 学习要点

### 核心概念
1. **序列解包（*）**：将列表、元组等序列类型解包为独立参数
2. **字典解包（**）**：将字典解包为关键字参数
3. **混合解包**：同时使用序列和字典解包
4. **参数验证**：确保解包的参数符合函数要求

### 实际应用
1. **数学运算**：坐标计算、矩阵运算、方程求解
2. **配置管理**：多源配置合并、环境配置应用
3. **装饰器**：动态参数传递、功能增强
4. **API调用**：动态构建请求参数

### 注意事项
1. **参数数量匹配**：确保解包的参数数量与函数签名匹配
2. **键名对应**：字典解包时确保键名与参数名对应
3. **类型验证**：对解包的参数进行适当的类型检查
4. **错误处理**：处理解包过程中可能出现的异常

### 最佳实践
1. **文档化**：清楚地文档化函数的参数要求
2. **参数验证**：在函数内部验证解包的参数
3. **错误处理**：提供友好的错误信息
4. **类型提示**：使用类型提示增强代码可读性

## 下一步学习

完成参数解包的学习后，建议继续学习：

1. **参数验证** (`08_parameter_validation.py`) - 学习如何验证函数参数
2. **综合练习** (`09_exercises.py`) - 通过练习巩固所学知识
3. **高级函数特性** - 学习更多Python函数的高级特性

参数解包是Python中非常实用的特性，掌握它能让你的代码更加灵活和优雅！