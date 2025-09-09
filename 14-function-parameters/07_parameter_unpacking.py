#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
参数解包 (Parameter Unpacking)

参数解包是Python中一个强大的特性，允许我们将序列（如列表、元组）和字典
中的元素作为参数传递给函数。使用*操作符解包序列，使用**操作符解包字典。

学习目标：
1. 理解参数解包的概念和语法
2. 掌握*操作符解包序列的方法
3. 掌握**操作符解包字典的方法
4. 学会在函数调用中灵活使用参数解包
5. 了解参数解包的实际应用场景
"""

# 1. 基本的序列解包（*操作符）
def basic_function(a, b, c):
    """
    接受三个参数的基本函数
    
    参数:
        a: 第一个参数
        b: 第二个参数
        c: 第三个参数
    
    返回:
        tuple: 参数元组
    """
    result = (a, b, c)
    print(f"接收到的参数: a={a}, b={b}, c={c}")
    print(f"参数元组: {result}")
    return result

def demonstrate_sequence_unpacking():
    """
    演示序列解包的各种方式
    """
    print("序列解包演示：")
    
    # 1. 列表解包
    numbers_list = [1, 2, 3]
    print(f"\n列表: {numbers_list}")
    basic_function(*numbers_list)  # 等价于 basic_function(1, 2, 3)
    
    # 2. 元组解包
    numbers_tuple = (4, 5, 6)
    print(f"\n元组: {numbers_tuple}")
    basic_function(*numbers_tuple)
    
    # 3. 字符串解包
    text = "abc"
    print(f"\n字符串: {text}")
    basic_function(*text)  # 等价于 basic_function('a', 'b', 'c')
    
    # 4. 范围解包
    range_obj = range(7, 10)
    print(f"\n范围: {list(range_obj)}")
    basic_function(*range_obj)
    
    print("-" * 40)

# 2. 基本的字典解包（**操作符）
def person_info(name, age, city):
    """
    显示个人信息
    
    参数:
        name (str): 姓名
        age (int): 年龄
        city (str): 城市
    
    返回:
        dict: 个人信息字典
    """
    info = {
        'name': name,
        'age': age,
        'city': city
    }
    
    print(f"个人信息: {info}")
    return info

def demonstrate_dict_unpacking():
    """
    演示字典解包的使用
    """
    print("字典解包演示：")
    
    # 1. 基本字典解包
    person_data = {
        'name': '张三',
        'age': 25,
        'city': '北京'
    }
    print(f"\n字典: {person_data}")
    person_info(**person_data)  # 等价于 person_info(name='张三', age=25, city='北京')
    
    # 2. 部分匹配的字典解包
    extended_data = {
        'name': '李四',
        'age': 30,
        'city': '上海',
        'country': '中国',  # 额外的键会被忽略（如果函数不接受**kwargs）
        'occupation': '工程师'
    }
    print(f"\n扩展字典: {extended_data}")
    try:
        person_info(**extended_data)
    except TypeError as e:
        print(f"错误: {e}")
        # 只传递匹配的键
        filtered_data = {k: v for k, v in extended_data.items() 
                        if k in ['name', 'age', 'city']}
        print(f"过滤后的字典: {filtered_data}")
        person_info(**filtered_data)
    
    print("-" * 40)

# 3. 混合解包：同时使用*和**
def flexible_function(a, b, c=10, *args, **kwargs):
    """
    接受多种参数类型的灵活函数
    
    参数:
        a: 第一个位置参数
        b: 第二个位置参数
        c: 默认参数
        *args: 额外的位置参数
        **kwargs: 关键字参数
    
    返回:
        dict: 所有参数的汇总
    """
    result = {
        'required': [a, b],
        'default': c,
        'extra_args': args,
        'kwargs': kwargs
    }
    
    print(f"参数汇总: {result}")
    return result

def demonstrate_mixed_unpacking():
    """
    演示混合参数解包
    """
    print("混合参数解包演示：")
    
    # 准备数据
    position_args = [1, 2]
    extra_args = [3, 4, 5]
    keyword_args = {'name': '测试', 'debug': True}
    
    print(f"位置参数: {position_args}")
    print(f"额外参数: {extra_args}")
    print(f"关键字参数: {keyword_args}")
    
    # 1. 分别解包
    print("\n分别解包:")
    flexible_function(*position_args, *extra_args, **keyword_args)
    
    # 2. 组合解包
    print("\n组合解包:")
    all_position_args = position_args + extra_args
    flexible_function(*all_position_args, **keyword_args)
    
    # 3. 部分解包
    print("\n部分解包:")
    flexible_function(position_args[0], position_args[1], 
                     *extra_args, **keyword_args)
    
    print("-" * 40)

# 4. 实际应用：数学运算函数
def calculate_sum(*numbers):
    """
    计算任意数量数字的和
    
    参数:
        *numbers: 数字列表
    
    返回:
        float: 数字之和
    """
    total = sum(numbers)
    print(f"计算 {numbers} 的和 = {total}")
    return total

def calculate_product(*numbers):
    """
    计算任意数量数字的乘积
    
    参数:
        *numbers: 数字列表
    
    返回:
        float: 数字之积
    """
    if not numbers:
        return 0
    
    result = 1
    for num in numbers:
        result *= num
    
    print(f"计算 {numbers} 的乘积 = {result}")
    return result

def demonstrate_math_operations():
    """
    演示数学运算中的参数解包
    """
    print("数学运算参数解包演示：")
    
    # 准备数据
    numbers1 = [1, 2, 3, 4, 5]
    numbers2 = (2, 4, 6, 8)
    numbers3 = range(1, 6)
    
    print(f"\n数据集1: {numbers1}")
    calculate_sum(*numbers1)
    calculate_product(*numbers1)
    
    print(f"\n数据集2: {numbers2}")
    calculate_sum(*numbers2)
    calculate_product(*numbers2)
    
    print(f"\n数据集3: {list(numbers3)}")
    calculate_sum(*numbers3)
    calculate_product(*numbers3)
    
    # 组合多个数据集
    print(f"\n组合数据集:")
    calculate_sum(*numbers1, *numbers2)
    calculate_product(*numbers1, *numbers2)
    
    print("-" * 40)

# 5. 实际应用：配置管理
def create_database_connection(**config):
    """
    创建数据库连接
    
    参数:
        **config: 数据库配置参数
    
    返回:
        dict: 连接配置
    """
    # 默认配置
    default_config = {
        'host': 'localhost',
        'port': 5432,
        'database': 'myapp',
        'username': 'user',
        'password': '',
        'ssl': False,
        'timeout': 30
    }
    
    # 合并配置
    final_config = {**default_config, **config}
    
    print(f"数据库连接配置: {final_config}")
    
    # 模拟连接
    connection_string = (f"{final_config['username']}@"
                        f"{final_config['host']}:"
                        f"{final_config['port']}/"
                        f"{final_config['database']}")
    
    print(f"连接字符串: {connection_string}")
    return final_config

def demonstrate_config_unpacking():
    """
    演示配置管理中的参数解包
    """
    print("配置管理参数解包演示：")
    
    # 1. 基本配置
    basic_config = {
        'host': '192.168.1.100',
        'database': 'production',
        'username': 'admin'
    }
    print(f"\n基本配置: {basic_config}")
    create_database_connection(**basic_config)
    
    # 2. 完整配置
    full_config = {
        'host': 'db.example.com',
        'port': 3306,
        'database': 'webapp',
        'username': 'webapp_user',
        'password': 'secret123',
        'ssl': True,
        'timeout': 60
    }
    print(f"\n完整配置: {full_config}")
    create_database_connection(**full_config)
    
    # 3. 配置组合
    base_config = {'host': 'cluster.example.com', 'ssl': True}
    env_config = {'database': 'staging', 'username': 'stage_user'}
    security_config = {'password': 'stage_pass', 'timeout': 45}
    
    print(f"\n组合配置:")
    print(f"  基础: {base_config}")
    print(f"  环境: {env_config}")
    print(f"  安全: {security_config}")
    
    create_database_connection(**base_config, **env_config, **security_config)
    
    print("-" * 40)

# 6. 高级应用：函数装饰器
def timing_decorator(func):
    """
    计时装饰器，演示参数解包在装饰器中的应用
    
    参数:
        func: 要装饰的函数
    
    返回:
        function: 装饰后的函数
    """
    import time
    
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        print(f"位置参数: {args}")
        print(f"关键字参数: {kwargs}")
        
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"执行时间: {execution_time:.4f}秒")
            print(f"返回结果: {result}")
            return result
        except Exception as e:
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"执行时间: {execution_time:.4f}秒")
            print(f"发生异常: {e}")
            raise
        finally:
            print("-" * 30)
    
    return wrapper

@timing_decorator
def complex_calculation(base, *multipliers, **options):
    """
    复杂计算函数，用于演示装饰器中的参数解包
    
    参数:
        base (float): 基数
        *multipliers: 乘数列表
        **options: 计算选项
    
    返回:
        float: 计算结果
    """
    import time
    
    # 模拟复杂计算
    time.sleep(0.1)  # 模拟计算时间
    
    result = base
    
    # 应用乘数
    for multiplier in multipliers:
        result *= multiplier
    
    # 应用选项
    if options.get('square'):
        result = result ** 2
    
    if options.get('add_bonus'):
        result += options['add_bonus']
    
    if options.get('round_to'):
        result = round(result, options['round_to'])
    
    return result

def demonstrate_decorator_unpacking():
    """
    演示装饰器中的参数解包
    """
    print("装饰器参数解包演示：")
    
    # 准备数据
    base_value = 10
    multipliers = [2, 3, 1.5]
    options = {'square': True, 'add_bonus': 100, 'round_to': 2}
    
    print(f"基数: {base_value}")
    print(f"乘数: {multipliers}")
    print(f"选项: {options}")
    
    # 调用函数（参数会被装饰器解包和重新打包）
    result = complex_calculation(base_value, *multipliers, **options)
    print(f"最终结果: {result}")
    
    print("-" * 40)

# 7. 实际应用：API调用包装
def make_api_request(url, method="GET", *middleware, **request_options):
    """
    API请求包装函数
    
    参数:
        url (str): 请求URL
        method (str): HTTP方法
        *middleware: 中间件列表
        **request_options: 请求选项
    
    返回:
        dict: 模拟的API响应
    """
    print(f"API请求: {method} {url}")
    print(f"中间件: {middleware}")
    print(f"选项: {request_options}")
    
    # 构建请求配置
    config = {
        'url': url,
        'method': method.upper(),
        'middleware': list(middleware),
        'options': request_options
    }
    
    # 模拟响应
    response = {
        'status_code': 200,
        'data': {'message': '请求成功'},
        'config': config
    }
    
    print(f"响应: {response}")
    return response

def demonstrate_api_unpacking():
    """
    演示API调用中的参数解包
    """
    print("API调用参数解包演示：")
    
    # 1. 基本API调用
    basic_url = "https://api.example.com/users"
    basic_options = {'timeout': 30, 'headers': {'Authorization': 'Bearer token'}}
    
    print(f"\n基本调用:")
    print(f"URL: {basic_url}")
    print(f"选项: {basic_options}")
    make_api_request(basic_url, **basic_options)
    
    # 2. 复杂API调用
    complex_url = "https://api.example.com/data"
    middleware_list = ['auth', 'logging', 'rate_limit']
    complex_options = {
        'timeout': 60,
        'retries': 3,
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': 'MyApp/1.0'
        },
        'data': {'query': 'search term'},
        'verify_ssl': True
    }
    
    print(f"\n复杂调用:")
    print(f"URL: {complex_url}")
    print(f"中间件: {middleware_list}")
    print(f"选项: {complex_options}")
    make_api_request(complex_url, "POST", *middleware_list, **complex_options)
    
    # 3. 配置组合
    base_config = {'timeout': 30, 'verify_ssl': True}
    auth_config = {'headers': {'Authorization': 'Bearer xyz123'}}
    data_config = {'data': {'user_id': 123, 'action': 'update'}}
    
    print(f"\n配置组合:")
    print(f"基础配置: {base_config}")
    print(f"认证配置: {auth_config}")
    print(f"数据配置: {data_config}")
    
    make_api_request("https://api.example.com/update", "PUT",
                    "auth", "validation",
                    **base_config, **auth_config, **data_config)
    
    print("-" * 40)

# 8. 参数解包的注意事项和最佳实践
def demonstrate_unpacking_pitfalls():
    """
    演示参数解包的注意事项
    """
    print("参数解包注意事项：")
    
    # 1. 参数数量不匹配
    def three_params(a, b, c):
        return a + b + c
    
    print("\n1. 参数数量不匹配:")
    try:
        result = three_params(*[1, 2])  # 缺少一个参数
        print(f"结果: {result}")
    except TypeError as e:
        print(f"错误: {e}")
    
    try:
        result = three_params(*[1, 2, 3, 4])  # 参数过多
        print(f"结果: {result}")
    except TypeError as e:
        print(f"错误: {e}")
    
    # 2. 字典键不匹配
    def named_params(name, age, city):
        return f"{name}, {age}岁, 来自{city}"
    
    print("\n2. 字典键不匹配:")
    try:
        wrong_keys = {'full_name': '张三', 'years': 25, 'location': '北京'}
        result = named_params(**wrong_keys)
        print(f"结果: {result}")
    except TypeError as e:
        print(f"错误: {e}")
        
        # 正确的键
        correct_keys = {'name': '张三', 'age': 25, 'city': '北京'}
        result = named_params(**correct_keys)
        print(f"正确结果: {result}")
    
    # 3. 重复的关键字参数
    print("\n3. 重复的关键字参数:")
    try:
        # 这会导致错误，因为name参数被指定了两次
        duplicate_dict = {'name': '李四', 'age': 30, 'city': '上海'}
        result = named_params('王五', **duplicate_dict)  # name被重复指定
        print(f"结果: {result}")
    except TypeError as e:
        print(f"错误: {e}")
        
        # 正确的方式
        result = named_params(**duplicate_dict)
        print(f"正确结果: {result}")
    
    print("-" * 40)

def main():
    """
    主函数：演示参数解包的各种用法
    """
    print("=" * 50)
    print("参数解包演示")
    print("=" * 50)
    
    # 1. 序列解包
    print("\n1. 序列解包 (*操作符)：")
    demonstrate_sequence_unpacking()
    
    # 2. 字典解包
    print("\n2. 字典解包 (**操作符)：")
    demonstrate_dict_unpacking()
    
    # 3. 混合解包
    print("\n3. 混合参数解包：")
    demonstrate_mixed_unpacking()
    
    # 4. 数学运算应用
    print("\n4. 数学运算应用：")
    demonstrate_math_operations()
    
    # 5. 配置管理应用
    print("\n5. 配置管理应用：")
    demonstrate_config_unpacking()
    
    # 6. 装饰器应用
    print("\n6. 装饰器应用：")
    demonstrate_decorator_unpacking()
    
    # 7. API调用应用
    print("\n7. API调用应用：")
    demonstrate_api_unpacking()
    
    # 8. 注意事项
    print("\n8. 注意事项和常见错误：")
    demonstrate_unpacking_pitfalls()
    
    print("\n=" * 50)
    print("参数解包要点总结：")
    print("1. 使用*解包序列（列表、元组、字符串等）")
    print("2. 使用**解包字典")
    print("3. 可以在同一个函数调用中混合使用*和**")
    print("4. 解包的参数数量和类型必须与函数签名匹配")
    print("5. 字典解包时键名必须与参数名匹配")
    print("6. 避免重复指定同一个参数")
    print("7. 参数解包使函数调用更加灵活和动态")
    print("8. 在装饰器、配置管理、API包装等场景中非常有用")
    print("=" * 50)

if __name__ == "__main__":
    main()