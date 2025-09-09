#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
参数组合使用 (Parameter Combinations)

在Python中，可以将不同类型的参数组合使用，但必须遵循特定的顺序：
1. 位置参数 (positional arguments)
2. 默认参数 (default arguments)
3. 可变位置参数 (*args)
4. 关键字参数 (keyword-only arguments)
5. 可变关键字参数 (**kwargs)

学习目标：
1. 理解参数组合的顺序规则
2. 掌握各种参数组合的使用方法
3. 学会设计灵活且清晰的函数接口
4. 了解参数组合的最佳实践
"""

# 1. 基本参数组合：位置参数 + 默认参数
def basic_combination(name, age, city="未知", country="中国"):
    """
    基本参数组合示例
    
    参数:
        name (str): 姓名（位置参数）
        age (int): 年龄（位置参数）
        city (str): 城市（默认参数）
        country (str): 国家（默认参数）
    
    返回:
        dict: 个人信息
    """
    info = {
        'name': name,
        'age': age,
        'city': city,
        'country': country
    }
    
    print(f"个人信息: {info}")
    return info

# 2. 位置参数 + *args + 默认参数
def calculate_stats(operation, *numbers, precision=2, show_details=False):
    """
    计算统计信息，演示位置参数、*args和默认参数的组合
    
    参数:
        operation (str): 操作类型（位置参数）
        *numbers: 数字列表（可变位置参数）
        precision (int): 精度（默认参数）
        show_details (bool): 是否显示详情（默认参数）
    
    返回:
        float: 计算结果
    """
    if not numbers:
        print("错误: 没有提供数字")
        return None
    
    if show_details:
        print(f"操作: {operation}")
        print(f"数字: {numbers}")
        print(f"精度: {precision}")
    
    result = None
    
    if operation == "sum":
        result = sum(numbers)
    elif operation == "avg":
        result = sum(numbers) / len(numbers)
    elif operation == "max":
        result = max(numbers)
    elif operation == "min":
        result = min(numbers)
    else:
        print(f"不支持的操作: {operation}")
        return None
    
    result = round(result, precision)
    
    if show_details:
        print(f"结果: {result}")
    
    return result

# 3. 完整参数组合：位置参数 + 默认参数 + *args + **kwargs
def full_combination(required_param, default_param="默认值", *args, **kwargs):
    """
    完整参数组合示例
    
    参数:
        required_param: 必需的位置参数
        default_param: 默认参数
        *args: 可变位置参数
        **kwargs: 可变关键字参数
    """
    print(f"必需参数: {required_param}")
    print(f"默认参数: {default_param}")
    print(f"位置参数 (*args): {args}")
    print(f"关键字参数 (**kwargs): {kwargs}")
    
    # 处理所有参数
    result = {
        'required': required_param,
        'default': default_param,
        'args': args,
        'kwargs': kwargs
    }
    
    print(f"组合结果: {result}")
    print("-" * 40)
    return result

# 4. 仅关键字参数 (keyword-only arguments)
def keyword_only_example(name, age, *, email, phone=None, address=None):
    """
    仅关键字参数示例
    
    参数:
        name (str): 姓名（位置参数）
        age (int): 年龄（位置参数）
        *: 分隔符，之后的参数只能通过关键字传递
        email (str): 邮箱（仅关键字参数，必需）
        phone (str): 电话（仅关键字参数，可选）
        address (str): 地址（仅关键字参数，可选）
    
    返回:
        dict: 联系信息
    """
    contact = {
        'name': name,
        'age': age,
        'email': email
    }
    
    if phone:
        contact['phone'] = phone
    if address:
        contact['address'] = address
    
    print(f"联系信息: {contact}")
    return contact

# 5. 复杂参数组合：包含仅关键字参数
def complex_combination(base, multiplier=1, *extras, 
                       operation="add", **options):
    """
    复杂参数组合，包含所有类型的参数
    
    参数:
        base: 基础值（位置参数）
        multiplier: 乘数（默认参数）
        *extras: 额外值（可变位置参数）
        operation: 操作类型（仅关键字参数）
        **options: 选项（可变关键字参数）
    
    返回:
        计算结果
    """
    print(f"基础值: {base}")
    print(f"乘数: {multiplier}")
    print(f"额外值: {extras}")
    print(f"操作: {operation}")
    print(f"选项: {options}")
    
    # 计算基础结果
    result = base * multiplier
    
    # 处理额外值
    if extras:
        if operation == "add":
            result += sum(extras)
        elif operation == "multiply":
            for extra in extras:
                result *= extra
        elif operation == "subtract":
            result -= sum(extras)
    
    # 应用选项
    if options.get('round_to'):
        result = round(result, options['round_to'])
    
    if options.get('absolute'):
        result = abs(result)
    
    if options.get('format_as_string'):
        result = f"{result:,.2f}"
    
    print(f"计算结果: {result}")
    print("-" * 40)
    return result

# 6. 实际应用：API端点函数
def api_endpoint(endpoint, method="GET", *middleware, 
                timeout=30, retries=3, **headers):
    """
    API端点配置函数，演示实际应用中的参数组合
    
    参数:
        endpoint (str): API端点（位置参数）
        method (str): HTTP方法（默认参数）
        *middleware: 中间件列表（可变位置参数）
        timeout (int): 超时时间（仅关键字参数）
        retries (int): 重试次数（仅关键字参数）
        **headers: HTTP头部（可变关键字参数）
    
    返回:
        dict: API配置
    """
    config = {
        'endpoint': endpoint,
        'method': method.upper(),
        'middleware': list(middleware),
        'timeout': timeout,
        'retries': retries,
        'headers': headers
    }
    
    print(f"API配置:")
    for key, value in config.items():
        print(f"  {key}: {value}")
    
    # 验证配置
    if not endpoint.startswith('/'):
        print("警告: 端点应该以 '/' 开头")
    
    if timeout <= 0:
        print("警告: 超时时间应该大于0")
    
    if retries < 0:
        print("警告: 重试次数不能为负数")
    
    print("-" * 40)
    return config

# 7. 数据处理函数
def process_data(data, processor_type="default", *transforms, 
                validate=True, sort_key=None, **filters):
    """
    数据处理函数，展示参数组合在数据处理中的应用
    
    参数:
        data (list): 要处理的数据（位置参数）
        processor_type (str): 处理器类型（默认参数）
        *transforms: 变换函数列表（可变位置参数）
        validate (bool): 是否验证数据（仅关键字参数）
        sort_key: 排序键（仅关键字参数）
        **filters: 过滤条件（可变关键字参数）
    
    返回:
        list: 处理后的数据
    """
    print(f"原始数据: {data}")
    print(f"处理器类型: {processor_type}")
    print(f"变换函数: {transforms}")
    print(f"验证数据: {validate}")
    print(f"排序键: {sort_key}")
    print(f"过滤条件: {filters}")
    
    if not isinstance(data, list):
        print("错误: 数据必须是列表")
        return []
    
    result = data.copy()
    
    # 数据验证
    if validate:
        result = [item for item in result if item is not None]
        print(f"验证后数据: {result}")
    
    # 应用过滤条件
    if filters:
        for filter_key, filter_value in filters.items():
            if filter_key == "min_value":
                result = [item for item in result 
                         if isinstance(item, (int, float)) and item >= filter_value]
            elif filter_key == "max_value":
                result = [item for item in result 
                         if isinstance(item, (int, float)) and item <= filter_value]
            elif filter_key == "type_filter":
                result = [item for item in result if isinstance(item, filter_value)]
        
        print(f"过滤后数据: {result}")
    
    # 应用变换
    for transform in transforms:
        if callable(transform):
            try:
                result = [transform(item) for item in result]
                print(f"应用变换 {transform.__name__} 后: {result}")
            except Exception as e:
                print(f"变换 {transform.__name__} 失败: {e}")
    
    # 排序
    if sort_key:
        try:
            if callable(sort_key):
                result.sort(key=sort_key)
            else:
                result.sort()
            print(f"排序后数据: {result}")
        except Exception as e:
            print(f"排序失败: {e}")
    
    print(f"最终结果: {result}")
    print("-" * 40)
    return result

# 8. 配置构建器
class ConfigBuilder:
    """
    配置构建器类，演示在类方法中使用参数组合
    """
    
    def __init__(self, name, version="1.0", *components, 
                 debug=False, **settings):
        """
        初始化配置构建器
        
        参数:
            name (str): 配置名称（位置参数）
            version (str): 版本（默认参数）
            *components: 组件列表（可变位置参数）
            debug (bool): 调试模式（仅关键字参数）
            **settings: 其他设置（可变关键字参数）
        """
        self.config = {
            'name': name,
            'version': version,
            'components': list(components),
            'debug': debug,
            'settings': settings
        }
        
        print(f"创建配置: {name} v{version}")
        print(f"组件: {components}")
        print(f"调试模式: {debug}")
        print(f"设置: {settings}")
    
    def add_component(self, component, *dependencies, 
                     required=True, **component_config):
        """
        添加组件
        
        参数:
            component (str): 组件名称（位置参数）
            *dependencies: 依赖列表（可变位置参数）
            required (bool): 是否必需（仅关键字参数）
            **component_config: 组件配置（可变关键字参数）
        """
        component_info = {
            'name': component,
            'dependencies': list(dependencies),
            'required': required,
            'config': component_config
        }
        
        if 'components_detail' not in self.config:
            self.config['components_detail'] = []
        
        self.config['components_detail'].append(component_info)
        
        print(f"添加组件: {component}")
        print(f"依赖: {dependencies}")
        print(f"必需: {required}")
        print(f"配置: {component_config}")
        print("-" * 30)
    
    def build(self, output_format="dict", *validators, 
             validate_dependencies=True, **build_options):
        """
        构建最终配置
        
        参数:
            output_format (str): 输出格式（默认参数）
            *validators: 验证器列表（可变位置参数）
            validate_dependencies (bool): 是否验证依赖（仅关键字参数）
            **build_options: 构建选项（可变关键字参数）
        
        返回:
            构建后的配置
        """
        print(f"构建配置，格式: {output_format}")
        print(f"验证器: {validators}")
        print(f"验证依赖: {validate_dependencies}")
        print(f"构建选项: {build_options}")
        
        # 应用验证器
        for validator in validators:
            if callable(validator):
                try:
                    validator(self.config)
                    print(f"验证器 {validator.__name__} 通过")
                except Exception as e:
                    print(f"验证器 {validator.__name__} 失败: {e}")
        
        # 依赖验证
        if validate_dependencies and 'components_detail' in self.config:
            print("验证组件依赖...")
            # 这里可以添加依赖验证逻辑
        
        # 应用构建选项
        final_config = self.config.copy()
        if build_options.get('include_metadata'):
            final_config['build_time'] = "2024-01-15 10:30:00"
            final_config['build_options'] = build_options
        
        print(f"最终配置: {final_config}")
        print("-" * 40)
        return final_config

# 9. 参数组合的错误示例和正确示例
def demonstrate_parameter_order():
    """
    演示参数顺序的重要性
    """
    print("参数顺序演示：")
    
    # 正确的参数顺序
    def correct_order(pos1, pos2, default1="def1", default2="def2", 
                     *args, kw_only1, kw_only2="kw_def", **kwargs):
        return {
            'pos': [pos1, pos2],
            'defaults': [default1, default2],
            'args': args,
            'kw_only': [kw_only1, kw_only2],
            'kwargs': kwargs
        }
    
    # 演示正确调用
    result = correct_order("p1", "p2", "d1", 1, 2, 3, 
                          kw_only1="kw1", extra="extra")
    print(f"正确调用结果: {result}")
    
    # 错误的参数顺序示例（注释掉，因为会导致语法错误）
    # def wrong_order(pos1, *args, default1="def1"):  # 错误：默认参数不能在*args之后
    #     pass
    
    # def wrong_order2(**kwargs, pos1):  # 错误：位置参数不能在**kwargs之后
    #     pass
    
    print("参数顺序规则:")
    print("1. 位置参数")
    print("2. 默认参数")
    print("3. *args")
    print("4. 仅关键字参数")
    print("5. **kwargs")
    print("-" * 40)

def main():
    """
    主函数：演示各种参数组合的使用
    """
    print("=" * 50)
    print("参数组合使用演示")
    print("=" * 50)
    
    # 1. 基本参数组合
    print("\n1. 基本参数组合：")
    basic_combination("张三", 25)
    basic_combination("李四", 30, "上海")
    basic_combination("王五", 28, "北京", "中国")
    print()
    
    # 2. 统计计算
    print("\n2. 统计计算（位置参数 + *args + 默认参数）：")
    calculate_stats("sum", 1, 2, 3, 4, 5)
    calculate_stats("avg", 10, 20, 30, precision=1, show_details=True)
    calculate_stats("max", 5, 15, 8, 12, 3, show_details=True)
    print()
    
    # 3. 完整参数组合
    print("\n3. 完整参数组合：")
    full_combination("必需值")
    full_combination("必需值", "自定义默认值")
    full_combination("必需值", "自定义默认值", 1, 2, 3)
    full_combination("必需值", "自定义默认值", 1, 2, 3, 
                    extra1="额外1", extra2="额外2")
    
    # 4. 仅关键字参数
    print("\n4. 仅关键字参数：")
    keyword_only_example("张三", 25, email="zhang@example.com")
    keyword_only_example("李四", 30, email="li@example.com", 
                        phone="13800138000", address="北京市")
    print()
    
    # 5. 复杂参数组合
    print("\n5. 复杂参数组合：")
    complex_combination(100)
    complex_combination(100, 2, 10, 20, operation="add")
    complex_combination(50, 3, 5, 10, operation="multiply", 
                       round_to=2, absolute=True)
    complex_combination(100, 0.8, 25, operation="subtract", 
                       format_as_string=True)
    
    # 6. API端点配置
    print("\n6. API端点配置：")
    api_endpoint("/users")
    api_endpoint("/api/data", "POST", "auth", "logging", 
                timeout=60, retries=5)
    api_endpoint("/secure/endpoint", "GET", "auth", "rate_limit", 
                timeout=30, retries=3,
                Authorization="Bearer token", 
                Content_Type="application/json")
    
    # 7. 数据处理
    print("\n7. 数据处理：")
    
    # 定义一些变换函数
    def square(x):
        return x ** 2 if isinstance(x, (int, float)) else x
    
    def add_ten(x):
        return x + 10 if isinstance(x, (int, float)) else x
    
    # 处理数据
    data1 = [1, 2, 3, 4, 5, None, 6]
    process_data(data1, validate=True)
    
    data2 = [10, 5, 8, 3, 12, 1]
    process_data(data2, "numeric", square, add_ten, 
                sort_key=True, min_value=5, max_value=15)
    
    data3 = [1, 2, "hello", 3.14, 5, "world"]
    process_data(data3, "mixed", validate=True, 
                type_filter=int, sort_key=True)
    
    # 8. 配置构建器
    print("\n8. 配置构建器：")
    
    # 创建配置
    builder = ConfigBuilder("MyApp", "2.0", "database", "cache", 
                           debug=True, log_level="INFO", 
                           max_connections=100)
    
    # 添加组件
    builder.add_component("redis", "network", required=True, 
                         host="localhost", port=6379)
    builder.add_component("postgres", "network", "auth", 
                         required=True, host="db.example.com", 
                         port=5432, ssl=True)
    
    # 定义验证器
    def validate_config(config):
        if not config.get('name'):
            raise ValueError("配置名称不能为空")
        return True
    
    def validate_version(config):
        version = config.get('version', '')
        if not version or version == '0.0':
            raise ValueError("版本号无效")
        return True
    
    # 构建配置
    final_config = builder.build("dict", validate_config, validate_version,
                               validate_dependencies=True, 
                               include_metadata=True, 
                               optimize=True)
    
    # 9. 参数顺序演示
    print("\n9. 参数顺序演示：")
    demonstrate_parameter_order()
    
    print("\n=" * 50)
    print("参数组合最佳实践：")
    print("1. 遵循正确的参数顺序")
    print("2. 合理使用默认参数减少函数调用复杂度")
    print("3. 使用*args处理不定数量的位置参数")
    print("4. 使用**kwargs处理不定数量的关键字参数")
    print("5. 使用仅关键字参数提高代码可读性")
    print("6. 避免过度复杂的参数组合")
    print("7. 为复杂函数提供清晰的文档说明")
    print("8. 考虑使用类或配置对象替代过多参数")
    print("=" * 50)

if __name__ == "__main__":
    main()