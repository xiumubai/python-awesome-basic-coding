#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
关键字参数 (Keyword Parameters)

关键字参数允许在函数调用时通过参数名来指定参数值，
这样可以不按照参数定义的顺序传递参数，提高代码的可读性和灵活性。

学习目标：
1. 理解关键字参数的概念和优势
2. 掌握关键字参数的使用方法
3. 学会混合使用位置参数和关键字参数
4. 了解关键字参数的最佳实践
"""

# 1. 基本的关键字参数
def introduce_person(name, age, city, occupation):
    """
    介绍一个人的基本信息
    
    参数:
        name (str): 姓名
        age (int): 年龄
        city (str): 城市
        occupation (str): 职业
    """
    print(f"姓名：{name}")
    print(f"年龄：{age}岁")
    print(f"城市：{city}")
    print(f"职业：{occupation}")
    print("-" * 30)

# 2. 关键字参数与位置参数混合使用
def create_book_info(title, author, pages=None, year=None, genre=None):
    """
    创建书籍信息
    
    参数:
        title (str): 书名（必需）
        author (str): 作者（必需）
        pages (int, optional): 页数
        year (int, optional): 出版年份
        genre (str, optional): 类型
    """
    print(f"书名：{title}")
    print(f"作者：{author}")
    
    if pages is not None:
        print(f"页数：{pages}页")
    if year is not None:
        print(f"出版年份：{year}年")
    if genre is not None:
        print(f"类型：{genre}")
    print("-" * 30)

# 3. 复杂的关键字参数示例
def format_address(street, city, state, country="中国", postal_code=None):
    """
    格式化地址信息
    
    参数:
        street (str): 街道地址
        city (str): 城市
        state (str): 省/州
        country (str): 国家，默认为"中国"
        postal_code (str, optional): 邮政编码
    
    返回:
        str: 格式化的地址字符串
    """
    address_parts = [street, city, state, country]
    
    if postal_code:
        address_parts.append(f"邮编：{postal_code}")
    
    formatted_address = ", ".join(address_parts)
    print(f"完整地址：{formatted_address}")
    return formatted_address

# 4. 关键字参数用于配置选项
def generate_report(data, title="数据报告", include_summary=True, 
                   include_charts=False, format_type="text", 
                   save_to_file=False, filename=None):
    """
    生成数据报告
    
    参数:
        data (list): 数据列表
        title (str): 报告标题
        include_summary (bool): 是否包含摘要
        include_charts (bool): 是否包含图表
        format_type (str): 格式类型 ('text', 'html', 'pdf')
        save_to_file (bool): 是否保存到文件
        filename (str, optional): 文件名
    """
    print(f"正在生成报告：{title}")
    print(f"数据条数：{len(data)}")
    print(f"格式类型：{format_type}")
    
    if include_summary:
        print("✓ 包含数据摘要")
        if data:
            print(f"  - 数据范围：{min(data)} 到 {max(data)}")
            print(f"  - 平均值：{sum(data)/len(data):.2f}")
    
    if include_charts:
        print("✓ 包含数据图表")
    
    if save_to_file:
        file_name = filename or f"report.{format_type}"
        print(f"✓ 保存到文件：{file_name}")
    
    print("-" * 40)

# 5. 关键字参数用于数据库连接
def connect_database(host, port, database, username, password, 
                    timeout=30, ssl_enabled=False, charset="utf8"):
    """
    模拟数据库连接
    
    参数:
        host (str): 主机地址
        port (int): 端口号
        database (str): 数据库名
        username (str): 用户名
        password (str): 密码
        timeout (int): 超时时间（秒）
        ssl_enabled (bool): 是否启用SSL
        charset (str): 字符编码
    
    返回:
        dict: 连接配置信息
    """
    config = {
        'host': host,
        'port': port,
        'database': database,
        'username': username,
        'password': '***',  # 隐藏密码
        'timeout': timeout,
        'ssl_enabled': ssl_enabled,
        'charset': charset
    }
    
    print("数据库连接配置：")
    for key, value in config.items():
        print(f"  {key}: {value}")
    
    print(f"连接字符串：{username}@{host}:{port}/{database}")
    print("-" * 40)
    
    return config

# 6. 关键字参数用于API调用
def make_api_request(url, method="GET", headers=None, params=None, 
                    data=None, timeout=10, verify_ssl=True):
    """
    模拟API请求
    
    参数:
        url (str): 请求URL
        method (str): HTTP方法
        headers (dict, optional): 请求头
        params (dict, optional): URL参数
        data (dict, optional): 请求数据
        timeout (int): 超时时间
        verify_ssl (bool): 是否验证SSL证书
    """
    print(f"API请求配置：")
    print(f"  URL: {url}")
    print(f"  方法: {method}")
    print(f"  超时: {timeout}秒")
    print(f"  SSL验证: {verify_ssl}")
    
    if headers:
        print(f"  请求头: {headers}")
    if params:
        print(f"  URL参数: {params}")
    if data:
        print(f"  请求数据: {data}")
    
    print("-" * 40)

# 7. 关键字参数的验证
def validate_user_input(username, email, age, phone=None, 
                       validate_email=True, min_age=0, max_age=150):
    """
    验证用户输入
    
    参数:
        username (str): 用户名
        email (str): 邮箱
        age (int): 年龄
        phone (str, optional): 电话号码
        validate_email (bool): 是否验证邮箱格式
        min_age (int): 最小年龄
        max_age (int): 最大年龄
    
    返回:
        tuple: (是否有效, 错误信息列表)
    """
    errors = []
    
    # 验证用户名
    if not username or len(username) < 3:
        errors.append("用户名至少需要3个字符")
    
    # 验证邮箱
    if validate_email and email:
        if "@" not in email or "." not in email:
            errors.append("邮箱格式不正确")
    
    # 验证年龄
    if not isinstance(age, int) or age < min_age or age > max_age:
        errors.append(f"年龄必须在{min_age}到{max_age}之间")
    
    # 验证电话（如果提供）
    if phone and len(phone) < 10:
        errors.append("电话号码格式不正确")
    
    is_valid = len(errors) == 0
    
    print(f"用户输入验证结果：")
    print(f"  用户名: {username}")
    print(f"  邮箱: {email}")
    print(f"  年龄: {age}")
    if phone:
        print(f"  电话: {phone}")
    
    if is_valid:
        print("  ✓ 验证通过")
    else:
        print("  ✗ 验证失败：")
        for error in errors:
            print(f"    - {error}")
    
    print("-" * 40)
    return is_valid, errors

def main():
    """
    主函数：演示关键字参数的各种用法
    """
    print("=" * 50)
    print("关键字参数演示")
    print("=" * 50)
    
    # 1. 基本关键字参数使用
    print("\n1. 基本关键字参数（不同顺序）：")
    # 按照定义顺序
    introduce_person("张三", 28, "北京", "工程师")
    
    # 使用关键字参数，改变顺序
    introduce_person(city="上海", name="李四", occupation="设计师", age=25)
    
    # 混合使用位置参数和关键字参数
    introduce_person("王五", age=30, city="广州", occupation="教师")
    
    # 2. 书籍信息示例
    print("\n2. 混合使用位置参数和关键字参数：")
    create_book_info("Python编程", "作者A")
    create_book_info("数据科学", "作者B", pages=350, year=2023)
    create_book_info(title="机器学习", author="作者C", genre="技术", year=2024, pages=500)
    
    # 3. 地址格式化
    print("\n3. 带默认值的关键字参数：")
    format_address("中关村大街1号", "北京", "北京市")
    format_address(street="南京路100号", city="上海", state="上海市", 
                  country="中国", postal_code="200000")
    format_address(city="深圳", street="华强北路200号", state="广东省", 
                  postal_code="518000")
    
    # 4. 报告生成
    print("\n4. 复杂的关键字参数配置：")
    sample_data = [10, 20, 30, 40, 50, 25, 35, 45]
    
    # 基本报告
    generate_report(sample_data)
    
    # 详细报告
    generate_report(data=sample_data, 
                   title="销售数据分析报告",
                   include_summary=True,
                   include_charts=True,
                   format_type="html",
                   save_to_file=True,
                   filename="sales_report.html")
    
    # 5. 数据库连接
    print("\n5. 数据库连接配置：")
    # 基本连接
    connect_database("localhost", 3306, "mydb", "user", "password")
    
    # 完整配置
    connect_database(host="192.168.1.100",
                    port=5432,
                    database="production_db",
                    username="admin",
                    password="secret123",
                    timeout=60,
                    ssl_enabled=True,
                    charset="utf8mb4")
    
    # 6. API请求
    print("\n6. API请求配置：")
    # 简单GET请求
    make_api_request("https://api.example.com/users")
    
    # 复杂POST请求
    make_api_request(url="https://api.example.com/users",
                    method="POST",
                    headers={"Content-Type": "application/json"},
                    data={"name": "新用户", "email": "user@example.com"},
                    timeout=30,
                    verify_ssl=True)
    
    # 7. 用户输入验证
    print("\n7. 用户输入验证：")
    # 有效输入
    validate_user_input(username="john_doe", 
                       email="john@example.com", 
                       age=25,
                       phone="13800138000")
    
    # 无效输入
    validate_user_input(username="jo",  # 用户名太短
                       email="invalid-email",  # 邮箱格式错误
                       age=200,  # 年龄超出范围
                       validate_email=True,
                       min_age=0,
                       max_age=150)
    
    # 8. 关键字参数的常见错误
    print("\n8. 常见错误演示：")
    try:
        # 错误：重复指定参数（这种错误在运行时无法捕获，因为是语法错误）
        # introduce_person("张三", 25, city="北京", city="上海")  # 这会报语法错误
        print("注意：不能为同一个参数重复指定值，这会导致语法错误")
    except TypeError as e:
        print(f"类型错误：{e}")
    
    try:
        # 错误：位置参数在关键字参数之后
        # introduce_person(name="张三", 25, "北京", "工程师")  # 这会报语法错误
        print("注意：位置参数必须在关键字参数之前")
    except Exception as e:
        print(f"错误：{e}")
    
    print("\n=" * 50)
    print("关键字参数要点总结：")
    print("1. 关键字参数通过参数名指定值，顺序可以改变")
    print("2. 关键字参数提高代码可读性和灵活性")
    print("3. 位置参数必须在关键字参数之前")
    print("4. 不能为同一个参数同时指定位置值和关键字值")
    print("5. 关键字参数特别适合有很多可选参数的函数")
    print("6. 使用关键字参数可以让函数调用更加清晰")
    print("=" * 50)

if __name__ == "__main__":
    main()