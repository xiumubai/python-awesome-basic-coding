#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
函数参数综合练习 (Function Parameters Exercises)

本文件包含了关于函数参数的各种练习题，涵盖了从基础到高级的所有概念。
通过这些练习，你将能够熟练掌握Python函数参数的各种用法。

练习内容：
1. 基础参数练习
2. 默认参数练习
3. 可变参数练习
4. 关键字参数练习
5. 参数组合练习
6. 参数解包练习
7. 参数验证练习
8. 实际应用练习
9. 高级挑战练习
"""

import functools
import inspect
from typing import Any, Dict, List, Optional, Union, Callable
from datetime import datetime, date
import json

# ============================================================================
# 练习1: 基础参数练习
# ============================================================================

def exercise_1_basic_parameters():
    """
    练习1: 基础参数使用
    
    任务：创建以下函数
    1. calculate_rectangle_area(length, width) - 计算矩形面积
    2. greet_person(first_name, last_name) - 问候某人
    3. convert_temperature(temp, from_unit, to_unit) - 温度转换
    """
    print("\n" + "=" * 50)
    print("练习1: 基础参数练习")
    print("=" * 50)
    
    # 解答1: 计算矩形面积
    def calculate_rectangle_area(length, width):
        """
        计算矩形面积
        
        参数:
            length (float): 长度
            width (float): 宽度
        
        返回:
            float: 面积
        """
        area = length * width
        print(f"矩形面积: {length} × {width} = {area}")
        return area
    
    # 解答2: 问候某人
    def greet_person(first_name, last_name):
        """
        问候某人
        
        参数:
            first_name (str): 名
            last_name (str): 姓
        
        返回:
            str: 问候语
        """
        greeting = f"你好，{last_name}{first_name}！"
        print(greeting)
        return greeting
    
    # 解答3: 温度转换
    def convert_temperature(temp, from_unit, to_unit):
        """
        温度转换
        
        参数:
            temp (float): 温度值
            from_unit (str): 源单位 ('C', 'F', 'K')
            to_unit (str): 目标单位 ('C', 'F', 'K')
        
        返回:
            float: 转换后的温度
        """
        # 先转换为摄氏度
        if from_unit == 'F':
            celsius = (temp - 32) * 5/9
        elif from_unit == 'K':
            celsius = temp - 273.15
        else:  # 'C'
            celsius = temp
        
        # 再转换为目标单位
        if to_unit == 'F':
            result = celsius * 9/5 + 32
        elif to_unit == 'K':
            result = celsius + 273.15
        else:  # 'C'
            result = celsius
        
        print(f"温度转换: {temp}°{from_unit} = {result:.2f}°{to_unit}")
        return result
    
    # 测试函数
    calculate_rectangle_area(5, 3)
    calculate_rectangle_area(10.5, 7.2)
    
    greet_person("三", "张")
    greet_person("明", "李")
    
    convert_temperature(100, 'C', 'F')
    convert_temperature(32, 'F', 'C')
    convert_temperature(273.15, 'K', 'C')

# ============================================================================
# 练习2: 默认参数练习
# ============================================================================

def exercise_2_default_parameters():
    """
    练习2: 默认参数使用
    
    任务：创建以下函数
    1. create_user_profile(name, age=18, city="北京", active=True) - 创建用户档案
    2. format_currency(amount, currency="CNY", symbol="¥") - 格式化货币
    3. send_email(to, subject, body, cc=None, bcc=None, priority="normal") - 发送邮件
    """
    print("\n" + "=" * 50)
    print("练习2: 默认参数练习")
    print("=" * 50)
    
    # 解答1: 创建用户档案
    def create_user_profile(name, age=18, city="北京", active=True):
        """
        创建用户档案
        
        参数:
            name (str): 用户名
            age (int): 年龄，默认18
            city (str): 城市，默认"北京"
            active (bool): 是否激活，默认True
        
        返回:
            dict: 用户档案
        """
        profile = {
            'name': name,
            'age': age,
            'city': city,
            'active': active,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        print(f"用户档案: {profile}")
        return profile
    
    # 解答2: 格式化货币
    def format_currency(amount, currency="CNY", symbol="¥"):
        """
        格式化货币
        
        参数:
            amount (float): 金额
            currency (str): 货币代码，默认"CNY"
            symbol (str): 货币符号，默认"¥"
        
        返回:
            str: 格式化后的货币字符串
        """
        formatted = f"{symbol}{amount:,.2f} {currency}"
        print(f"格式化货币: {formatted}")
        return formatted
    
    # 解答3: 发送邮件
    def send_email(to, subject, body, cc=None, bcc=None, priority="normal"):
        """
        发送邮件
        
        参数:
            to (str): 收件人
            subject (str): 主题
            body (str): 正文
            cc (list): 抄送，默认None
            bcc (list): 密送，默认None
            priority (str): 优先级，默认"normal"
        
        返回:
            dict: 邮件信息
        """
        email = {
            'to': to,
            'subject': subject,
            'body': body,
            'cc': cc or [],
            'bcc': bcc or [],
            'priority': priority,
            'sent_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        print(f"邮件发送: {email}")
        return email
    
    # 测试函数
    create_user_profile("张三")
    create_user_profile("李四", 25)
    create_user_profile("王五", 30, "上海")
    create_user_profile("赵六", 28, "广州", False)
    
    format_currency(1234.56)
    format_currency(9999.99, "USD", "$")
    format_currency(5000, "EUR", "€")
    
    send_email("user@example.com", "测试邮件", "这是一封测试邮件")
    send_email("user@example.com", "重要通知", "紧急事项", 
              cc=["manager@example.com"], priority="high")

# ============================================================================
# 练习3: 可变参数练习
# ============================================================================

def exercise_3_variable_args():
    """
    练习3: 可变参数使用
    
    任务：创建以下函数
    1. calculate_statistics(*numbers) - 计算统计信息
    2. build_path(*parts) - 构建文件路径
    3. log_message(level, *messages) - 记录日志消息
    """
    print("\n" + "=" * 50)
    print("练习3: 可变参数练习")
    print("=" * 50)
    
    # 解答1: 计算统计信息
    def calculate_statistics(*numbers):
        """
        计算统计信息
        
        参数:
            *numbers: 可变数量的数字
        
        返回:
            dict: 统计信息
        """
        if not numbers:
            return {'error': '没有提供数字'}
        
        stats = {
            'count': len(numbers),
            'sum': sum(numbers),
            'average': sum(numbers) / len(numbers),
            'min': min(numbers),
            'max': max(numbers),
            'range': max(numbers) - min(numbers)
        }
        
        print(f"统计信息: {stats}")
        return stats
    
    # 解答2: 构建文件路径
    def build_path(*parts):
        """
        构建文件路径
        
        参数:
            *parts: 路径组件
        
        返回:
            str: 完整路径
        """
        import os
        path = os.path.join(*parts)
        print(f"构建路径: {path}")
        return path
    
    # 解答3: 记录日志消息
    def log_message(level, *messages):
        """
        记录日志消息
        
        参数:
            level (str): 日志级别
            *messages: 可变数量的消息
        
        返回:
            str: 格式化的日志
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        combined_message = ' '.join(str(msg) for msg in messages)
        log_entry = f"[{timestamp}] {level.upper()}: {combined_message}"
        print(log_entry)
        return log_entry
    
    # 测试函数
    calculate_statistics(1, 2, 3, 4, 5)
    calculate_statistics(10, 20, 30, 40, 50, 60)
    calculate_statistics()
    
    build_path("home", "user", "documents", "file.txt")
    build_path("var", "log", "app.log")
    build_path("C:", "Program Files", "Python", "python.exe")
    
    log_message("info", "应用程序启动")
    log_message("warning", "内存使用率较高:", 85, "%")
    log_message("error", "数据库连接失败", "重试中...")

# ============================================================================
# 练习4: 关键字参数练习
# ============================================================================

def exercise_4_keyword_args():
    """
    练习4: 关键字参数使用
    
    任务：创建以下函数
    1. create_database_config(**config) - 创建数据库配置
    2. generate_report(title, **options) - 生成报告
    3. api_request(url, method="GET", **params) - API请求
    """
    print("\n" + "=" * 50)
    print("练习4: 关键字参数练习")
    print("=" * 50)
    
    # 解答1: 创建数据库配置
    def create_database_config(**config):
        """
        创建数据库配置
        
        参数:
            **config: 数据库配置参数
        
        返回:
            dict: 完整的数据库配置
        """
        default_config = {
            'host': 'localhost',
            'port': 3306,
            'database': 'mydb',
            'charset': 'utf8mb4',
            'timeout': 30
        }
        
        # 合并配置
        final_config = {**default_config, **config}
        print(f"数据库配置: {final_config}")
        return final_config
    
    # 解答2: 生成报告
    def generate_report(title, **options):
        """
        生成报告
        
        参数:
            title (str): 报告标题
            **options: 报告选项
        
        返回:
            dict: 报告信息
        """
        report = {
            'title': title,
            'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'format': options.get('format', 'pdf'),
            'include_charts': options.get('include_charts', True),
            'page_size': options.get('page_size', 'A4'),
            'orientation': options.get('orientation', 'portrait'),
            'author': options.get('author', 'System'),
            'additional_options': {k: v for k, v in options.items() 
                                 if k not in ['format', 'include_charts', 
                                            'page_size', 'orientation', 'author']}
        }
        
        print(f"报告生成: {report}")
        return report
    
    # 解答3: API请求
    def api_request(url, method="GET", **params):
        """
        API请求
        
        参数:
            url (str): 请求URL
            method (str): 请求方法
            **params: 请求参数
        
        返回:
            dict: 请求信息
        """
        request_info = {
            'url': url,
            'method': method.upper(),
            'headers': params.get('headers', {}),
            'data': params.get('data'),
            'json': params.get('json'),
            'timeout': params.get('timeout', 30),
            'auth': params.get('auth'),
            'other_params': {k: v for k, v in params.items() 
                           if k not in ['headers', 'data', 'json', 'timeout', 'auth']}
        }
        
        print(f"API请求: {request_info}")
        return request_info
    
    # 测试函数
    create_database_config()
    create_database_config(host="192.168.1.100", port=5432, database="postgres")
    create_database_config(user="admin", password="secret", ssl=True)
    
    generate_report("月度销售报告")
    generate_report("年度财务报告", format="excel", include_charts=False)
    generate_report("用户分析报告", format="html", page_size="A3", 
                   orientation="landscape", author="数据分析师", 
                   theme="dark", language="zh-CN")
    
    api_request("https://api.example.com/users")
    api_request("https://api.example.com/posts", method="POST", 
               json={'title': '新文章', 'content': '内容'})
    api_request("https://api.example.com/data", 
               headers={'Authorization': 'Bearer token'}, 
               timeout=60, retries=3)

# ============================================================================
# 练习5: 参数组合练习
# ============================================================================

def exercise_5_parameter_combinations():
    """
    练习5: 参数组合使用
    
    任务：创建以下函数
    1. process_data(data, *transformations, output_format="json", **options) - 处理数据
    2. create_user(username, email, *roles, active=True, **profile) - 创建用户
    3. execute_query(sql, *params, connection=None, **query_options) - 执行查询
    """
    print("\n" + "=" * 50)
    print("练习5: 参数组合练习")
    print("=" * 50)
    
    # 解答1: 处理数据
    def process_data(data, *transformations, output_format="json", **options):
        """
        处理数据
        
        参数:
            data: 原始数据
            *transformations: 转换操作
            output_format: 输出格式
            **options: 其他选项
        
        返回:
            dict: 处理结果
        """
        result = {
            'original_data': data,
            'transformations_applied': list(transformations),
            'output_format': output_format,
            'processing_options': options,
            'processed_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # 模拟数据处理
        processed_data = data
        for transformation in transformations:
            print(f"应用转换: {transformation}")
            # 这里可以实现实际的转换逻辑
        
        result['processed_data'] = processed_data
        print(f"数据处理完成: {result}")
        return result
    
    # 解答2: 创建用户
    def create_user(username, email, *roles, active=True, **profile):
        """
        创建用户
        
        参数:
            username (str): 用户名
            email (str): 邮箱
            *roles: 用户角色
            active (bool): 是否激活
            **profile: 用户档案信息
        
        返回:
            dict: 用户信息
        """
        user = {
            'username': username,
            'email': email,
            'roles': list(roles) if roles else ['user'],
            'active': active,
            'profile': profile,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        print(f"用户创建: {user}")
        return user
    
    # 解答3: 执行查询
    def execute_query(sql, *params, connection=None, **query_options):
        """
        执行查询
        
        参数:
            sql (str): SQL语句
            *params: 查询参数
            connection: 数据库连接
            **query_options: 查询选项
        
        返回:
            dict: 查询结果
        """
        query_info = {
            'sql': sql,
            'parameters': list(params),
            'connection': connection or 'default',
            'options': query_options,
            'executed_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # 模拟查询执行
        print(f"执行查询: {query_info}")
        
        # 模拟查询结果
        result = {
            'query_info': query_info,
            'rows_affected': query_options.get('expected_rows', 0),
            'execution_time': query_options.get('timeout', 1.0)
        }
        
        return result
    
    # 测试函数
    process_data([1, 2, 3, 4, 5], "normalize", "filter")
    process_data({"a": 1, "b": 2}, "transform", "validate", 
                output_format="xml", encoding="utf-8", pretty=True)
    
    create_user("john_doe", "john@example.com")
    create_user("admin_user", "admin@example.com", "admin", "moderator")
    create_user("jane_smith", "jane@example.com", "user", "editor", 
               active=True, age=28, city="北京", department="IT")
    
    execute_query("SELECT * FROM users")
    execute_query("SELECT * FROM users WHERE age > ?", 18)
    execute_query("UPDATE users SET active = ? WHERE id = ?", True, 123, 
                 connection="primary", timeout=30, retry_count=3)

# ============================================================================
# 练习6: 参数解包练习
# ============================================================================

def exercise_6_parameter_unpacking():
    """
    练习6: 参数解包使用
    
    任务：创建以下函数并演示参数解包
    1. calculate_distance(x1, y1, x2, y2) - 计算两点距离
    2. create_person(name, age, **details) - 创建人员信息
    3. merge_configs(*configs) - 合并配置
    """
    print("\n" + "=" * 50)
    print("练习6: 参数解包练习")
    print("=" * 50)
    
    # 解答1: 计算两点距离
    def calculate_distance(x1, y1, x2, y2):
        """
        计算两点距离
        
        参数:
            x1, y1: 第一个点的坐标
            x2, y2: 第二个点的坐标
        
        返回:
            float: 距离
        """
        import math
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        print(f"距离计算: ({x1}, {y1}) 到 ({x2}, {y2}) = {distance:.2f}")
        return distance
    
    # 解答2: 创建人员信息
    def create_person(name, age, **details):
        """
        创建人员信息
        
        参数:
            name (str): 姓名
            age (int): 年龄
            **details: 其他详细信息
        
        返回:
            dict: 人员信息
        """
        person = {
            'name': name,
            'age': age,
            **details
        }
        print(f"人员信息: {person}")
        return person
    
    # 解答3: 合并配置
    def merge_configs(*configs):
        """
        合并配置
        
        参数:
            *configs: 配置字典
        
        返回:
            dict: 合并后的配置
        """
        merged = {}
        for config in configs:
            if isinstance(config, dict):
                merged.update(config)
        
        print(f"配置合并: {merged}")
        return merged
    
    # 演示参数解包
    print("\n参数解包演示:")
    
    # 1. 列表解包
    point1 = [0, 0]
    point2 = [3, 4]
    calculate_distance(*point1, *point2)
    
    # 2. 元组解包
    coordinates = (1, 1, 5, 5)
    calculate_distance(*coordinates)
    
    # 3. 字典解包
    person_info = {
        'city': '北京',
        'job': '工程师',
        'salary': 10000
    }
    create_person('张三', 25, **person_info)
    
    # 4. 混合解包
    basic_info = {'name': '李四', 'age': 30}
    extra_info = {'department': 'IT', 'level': 'Senior'}
    create_person(**basic_info, **extra_info)
    
    # 5. 多个配置合并
    config1 = {'host': 'localhost', 'port': 8080}
    config2 = {'debug': True, 'timeout': 30}
    config3 = {'ssl': False, 'retries': 3}
    merge_configs(config1, config2, config3)

# ============================================================================
# 练习7: 参数验证练习
# ============================================================================

def exercise_7_parameter_validation():
    """
    练习7: 参数验证练习
    
    任务：创建带有参数验证的函数
    1. safe_divide(a, b) - 安全除法
    2. create_account(username, password, email) - 创建账户
    3. process_age_group(ages) - 处理年龄组
    """
    print("\n" + "=" * 50)
    print("练习7: 参数验证练习")
    print("=" * 50)
    
    # 解答1: 安全除法
    def safe_divide(a, b):
        """
        安全除法，包含参数验证
        
        参数:
            a (float): 被除数
            b (float): 除数
        
        返回:
            float: 除法结果
        
        异常:
            TypeError: 参数类型错误
            ValueError: 除数为零
        """
        # 类型验证
        if not isinstance(a, (int, float)):
            raise TypeError(f"被除数必须是数字，得到 {type(a).__name__}")
        
        if not isinstance(b, (int, float)):
            raise TypeError(f"除数必须是数字，得到 {type(b).__name__}")
        
        # 值验证
        if b == 0:
            raise ValueError("除数不能为零")
        
        result = a / b
        print(f"除法计算: {a} ÷ {b} = {result}")
        return result
    
    # 解答2: 创建账户
    def create_account(username, password, email):
        """
        创建账户，包含参数验证
        
        参数:
            username (str): 用户名
            password (str): 密码
            email (str): 邮箱
        
        返回:
            dict: 账户信息
        
        异常:
            TypeError: 参数类型错误
            ValueError: 参数值错误
        """
        import re
        
        # 类型验证
        if not isinstance(username, str):
            raise TypeError("用户名必须是字符串")
        if not isinstance(password, str):
            raise TypeError("密码必须是字符串")
        if not isinstance(email, str):
            raise TypeError("邮箱必须是字符串")
        
        # 用户名验证
        if len(username) < 3:
            raise ValueError("用户名长度不能少于3个字符")
        if len(username) > 20:
            raise ValueError("用户名长度不能超过20个字符")
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise ValueError("用户名只能包含字母、数字和下划线")
        
        # 密码验证
        if len(password) < 8:
            raise ValueError("密码长度不能少于8个字符")
        if not re.search(r'[A-Z]', password):
            raise ValueError("密码必须包含大写字母")
        if not re.search(r'[a-z]', password):
            raise ValueError("密码必须包含小写字母")
        if not re.search(r'\d', password):
            raise ValueError("密码必须包含数字")
        
        # 邮箱验证
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValueError("邮箱格式不正确")
        
        account = {
            'username': username,
            'email': email,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        print(f"账户创建成功: {account}")
        return account
    
    # 解答3: 处理年龄组
    def process_age_group(ages):
        """
        处理年龄组，包含参数验证
        
        参数:
            ages (list): 年龄列表
        
        返回:
            dict: 年龄组统计
        
        异常:
            TypeError: 参数类型错误
            ValueError: 参数值错误
        """
        # 类型验证
        if not isinstance(ages, list):
            raise TypeError(f"ages必须是列表，得到 {type(ages).__name__}")
        
        if not ages:
            raise ValueError("年龄列表不能为空")
        
        # 验证列表中的每个元素
        for i, age in enumerate(ages):
            if not isinstance(age, int):
                raise TypeError(f"第{i}个年龄必须是整数，得到 {type(age).__name__}")
            if age < 0 or age > 150:
                raise ValueError(f"第{i}个年龄必须在0-150之间，得到 {age}")
        
        # 处理年龄组
        groups = {
            '儿童 (0-12)': 0,
            '青少年 (13-17)': 0,
            '青年 (18-35)': 0,
            '中年 (36-59)': 0,
            '老年 (60+)': 0
        }
        
        for age in ages:
            if age <= 12:
                groups['儿童 (0-12)'] += 1
            elif age <= 17:
                groups['青少年 (13-17)'] += 1
            elif age <= 35:
                groups['青年 (18-35)'] += 1
            elif age <= 59:
                groups['中年 (36-59)'] += 1
            else:
                groups['老年 (60+)'] += 1
        
        result = {
            'total_count': len(ages),
            'age_groups': groups,
            'average_age': sum(ages) / len(ages)
        }
        
        print(f"年龄组统计: {result}")
        return result
    
    # 测试函数
    print("\n正确用法测试:")
    try:
        safe_divide(10, 2)
        safe_divide(7.5, 2.5)
    except (TypeError, ValueError) as e:
        print(f"错误: {e}")
    
    try:
        create_account("john_doe", "MyPassword123", "john@example.com")
    except (TypeError, ValueError) as e:
        print(f"错误: {e}")
    
    try:
        process_age_group([25, 30, 45, 12, 67, 8, 55])
    except (TypeError, ValueError) as e:
        print(f"错误: {e}")
    
    print("\n错误用法测试:")
    # 测试错误情况
    error_tests = [
        (lambda: safe_divide("10", 2), "类型错误测试"),
        (lambda: safe_divide(10, 0), "除零错误测试"),
        (lambda: create_account("ab", "weak", "invalid-email"), "账户验证错误测试"),
        (lambda: process_age_group([25, "30", 45]), "年龄类型错误测试"),
        (lambda: process_age_group([25, 200, 45]), "年龄范围错误测试")
    ]
    
    for test_func, description in error_tests:
        try:
            test_func()
        except (TypeError, ValueError) as e:
            print(f"{description}: {e}")

# ============================================================================
# 练习8: 实际应用练习
# ============================================================================

def exercise_8_practical_applications():
    """
    练习8: 实际应用练习
    
    任务：创建实际应用中的函数
    1. 购物车系统
    2. 文件处理系统
    3. 数据分析系统
    """
    print("\n" + "=" * 50)
    print("练习8: 实际应用练习")
    print("=" * 50)
    
    # 1. 购物车系统
    class ShoppingCart:
        def __init__(self):
            self.items = []
        
        def add_item(self, name, price, quantity=1, **attributes):
            """
            添加商品到购物车
            
            参数:
                name (str): 商品名称
                price (float): 单价
                quantity (int): 数量
                **attributes: 商品属性
            """
            item = {
                'name': name,
                'price': price,
                'quantity': quantity,
                'subtotal': price * quantity,
                'attributes': attributes
            }
            self.items.append(item)
            print(f"添加商品: {item}")
        
        def calculate_total(self, tax_rate=0.0, discount=0.0, **fees):
            """
            计算总价
            
            参数:
                tax_rate (float): 税率
                discount (float): 折扣金额
                **fees: 其他费用
            
            返回:
                dict: 价格明细
            """
            subtotal = sum(item['subtotal'] for item in self.items)
            tax = subtotal * tax_rate
            total_fees = sum(fees.values())
            total = subtotal + tax + total_fees - discount
            
            summary = {
                'subtotal': subtotal,
                'tax': tax,
                'discount': discount,
                'fees': fees,
                'total': total
            }
            
            print(f"价格计算: {summary}")
            return summary
    
    # 2. 文件处理系统
    def process_files(*file_paths, operation="read", **options):
        """
        处理文件
        
        参数:
            *file_paths: 文件路径
            operation (str): 操作类型
            **options: 处理选项
        
        返回:
            list: 处理结果
        """
        results = []
        
        for file_path in file_paths:
            result = {
                'file_path': file_path,
                'operation': operation,
                'options': options,
                'processed_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            # 模拟文件处理
            if operation == "read":
                result['status'] = 'success'
                result['size'] = options.get('expected_size', 1024)
            elif operation == "write":
                result['status'] = 'success'
                result['bytes_written'] = len(options.get('content', ''))
            elif operation == "delete":
                result['status'] = 'success'
                result['deleted'] = True
            
            results.append(result)
            print(f"文件处理: {result}")
        
        return results
    
    # 3. 数据分析系统
    def analyze_data(data, *analysis_types, output_format="dict", **params):
        """
        数据分析
        
        参数:
            data: 数据
            *analysis_types: 分析类型
            output_format (str): 输出格式
            **params: 分析参数
        
        返回:
            分析结果
        """
        if not isinstance(data, list):
            raise TypeError("数据必须是列表")
        
        if not data:
            raise ValueError("数据不能为空")
        
        results = {
            'data_info': {
                'count': len(data),
                'type': type(data[0]).__name__ if data else 'unknown'
            },
            'analysis_results': {}
        }
        
        # 执行分析
        for analysis_type in analysis_types:
            if analysis_type == "basic_stats" and all(isinstance(x, (int, float)) for x in data):
                results['analysis_results']['basic_stats'] = {
                    'sum': sum(data),
                    'average': sum(data) / len(data),
                    'min': min(data),
                    'max': max(data)
                }
            elif analysis_type == "frequency":
                from collections import Counter
                results['analysis_results']['frequency'] = dict(Counter(data))
            elif analysis_type == "unique_count":
                results['analysis_results']['unique_count'] = len(set(data))
        
        # 应用参数
        if params.get('sort_results'):
            # 模拟排序
            results['sorted'] = True
        
        if params.get('limit'):
            results['limited_to'] = params['limit']
        
        print(f"数据分析完成: {results}")
        
        # 根据输出格式返回结果
        if output_format == "json":
            return json.dumps(results, indent=2, ensure_ascii=False)
        else:
            return results
    
    # 测试实际应用
    print("\n1. 购物车系统测试:")
    cart = ShoppingCart()
    cart.add_item("iPhone 15", 8999, 1, color="黑色", storage="256GB")
    cart.add_item("AirPods Pro", 1999, 2, generation="第二代")
    cart.calculate_total(tax_rate=0.13, discount=500, shipping=50, insurance=20)
    
    print("\n2. 文件处理系统测试:")
    process_files("/path/to/file1.txt", "/path/to/file2.txt", 
                 operation="read", encoding="utf-8", buffer_size=4096)
    process_files("/path/to/output.txt", 
                 operation="write", content="Hello World", mode="w")
    
    print("\n3. 数据分析系统测试:")
    sample_data = [1, 2, 3, 4, 5, 3, 2, 1, 4, 5]
    analyze_data(sample_data, "basic_stats", "frequency", "unique_count", 
                sort_results=True, limit=10)
    
    text_data = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    result = analyze_data(text_data, "frequency", "unique_count", 
                         output_format="json")
    print(f"JSON结果: {result}")

# ============================================================================
# 练习9: 高级挑战练习
# ============================================================================

def exercise_9_advanced_challenges():
    """
    练习9: 高级挑战练习
    
    任务：创建高级函数
    1. 函数工厂
    2. 装饰器工厂
    3. 动态函数调用系统
    """
    print("\n" + "=" * 50)
    print("练习9: 高级挑战练习")
    print("=" * 50)
    
    # 1. 函数工厂
    def create_validator(**validation_rules):
        """
        创建验证器函数
        
        参数:
            **validation_rules: 验证规则
        
        返回:
            function: 验证器函数
        """
        def validator(data):
            errors = []
            
            for field, rules in validation_rules.items():
                if field not in data:
                    if rules.get('required', False):
                        errors.append(f"字段 '{field}' 是必需的")
                    continue
                
                value = data[field]
                
                # 类型检查
                if 'type' in rules and not isinstance(value, rules['type']):
                    errors.append(f"字段 '{field}' 类型错误")
                
                # 长度检查
                if 'min_length' in rules and len(str(value)) < rules['min_length']:
                    errors.append(f"字段 '{field}' 长度不足")
                
                if 'max_length' in rules and len(str(value)) > rules['max_length']:
                    errors.append(f"字段 '{field}' 长度超限")
                
                # 范围检查
                if 'min_value' in rules and value < rules['min_value']:
                    errors.append(f"字段 '{field}' 值过小")
                
                if 'max_value' in rules and value > rules['max_value']:
                    errors.append(f"字段 '{field}' 值过大")
            
            return len(errors) == 0, errors
        
        return validator
    
    # 2. 装饰器工厂
    def create_retry_decorator(max_retries=3, delay=1, exceptions=(Exception,)):
        """
        创建重试装饰器
        
        参数:
            max_retries (int): 最大重试次数
            delay (float): 重试延迟
            exceptions (tuple): 需要重试的异常类型
        
        返回:
            function: 装饰器函数
        """
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                last_exception = None
                
                for attempt in range(max_retries + 1):
                    try:
                        result = func(*args, **kwargs)
                        if attempt > 0:
                            print(f"函数 {func.__name__} 在第 {attempt + 1} 次尝试后成功")
                        return result
                    except exceptions as e:
                        last_exception = e
                        if attempt < max_retries:
                            print(f"函数 {func.__name__} 第 {attempt + 1} 次尝试失败: {e}")
                            import time
                            time.sleep(delay)
                        else:
                            print(f"函数 {func.__name__} 在 {max_retries + 1} 次尝试后仍然失败")
                
                raise last_exception
            
            return wrapper
        return decorator
    
    # 3. 动态函数调用系统
    class FunctionRegistry:
        """
        函数注册表
        """
        def __init__(self):
            self.functions = {}
        
        def register(self, name=None, **metadata):
            """
            注册函数装饰器
            
            参数:
                name (str): 函数名称
                **metadata: 函数元数据
            
            返回:
                function: 装饰器函数
            """
            def decorator(func):
                func_name = name or func.__name__
                self.functions[func_name] = {
                    'function': func,
                    'metadata': metadata,
                    'signature': inspect.signature(func)
                }
                return func
            return decorator
        
        def call(self, name, *args, **kwargs):
            """
            调用注册的函数
            
            参数:
                name (str): 函数名称
                *args: 位置参数
                **kwargs: 关键字参数
            
            返回:
                函数执行结果
            """
            if name not in self.functions:
                raise ValueError(f"函数 '{name}' 未注册")
            
            func_info = self.functions[name]
            func = func_info['function']
            
            print(f"调用函数: {name}")
            print(f"元数据: {func_info['metadata']}")
            
            return func(*args, **kwargs)
        
        def list_functions(self):
            """
            列出所有注册的函数
            
            返回:
                dict: 函数信息
            """
            return {name: info['metadata'] for name, info in self.functions.items()}
    
    # 测试高级功能
    print("\n1. 函数工厂测试:")
    
    # 创建用户验证器
    user_validator = create_validator(
        username={'required': True, 'type': str, 'min_length': 3, 'max_length': 20},
        age={'required': True, 'type': int, 'min_value': 0, 'max_value': 150},
        email={'required': True, 'type': str, 'min_length': 5}
    )
    
    # 测试验证器
    test_data = {'username': 'john_doe', 'age': 25, 'email': 'john@example.com'}
    is_valid, errors = user_validator(test_data)
    print(f"验证结果: {is_valid}, 错误: {errors}")
    
    invalid_data = {'username': 'jo', 'age': 200}
    is_valid, errors = user_validator(invalid_data)
    print(f"验证结果: {is_valid}, 错误: {errors}")
    
    print("\n2. 装饰器工厂测试:")
    
    # 创建重试装饰器
    retry_on_error = create_retry_decorator(max_retries=2, delay=0.1, 
                                          exceptions=(ValueError,))
    
    @retry_on_error
    def unreliable_function(success_rate=0.3):
        import random
        if random.random() < success_rate:
            return "成功!"
        else:
            raise ValueError("随机失败")
    
    try:
        result = unreliable_function(0.8)
        print(f"函数结果: {result}")
    except ValueError as e:
        print(f"最终失败: {e}")
    
    print("\n3. 动态函数调用系统测试:")
    
    # 创建函数注册表
    registry = FunctionRegistry()
    
    # 注册函数
    @registry.register("add", description="加法运算", category="math")
    def add_numbers(a, b):
        return a + b
    
    @registry.register("greet", description="问候函数", category="text")
    def greet_user(name, greeting="Hello"):
        return f"{greeting}, {name}!"
    
    @registry.register("analyze", description="数据分析", category="data")
    def analyze_numbers(*numbers, operation="sum"):
        if operation == "sum":
            return sum(numbers)
        elif operation == "avg":
            return sum(numbers) / len(numbers) if numbers else 0
        elif operation == "max":
            return max(numbers) if numbers else None
    
    # 列出注册的函数
    print("注册的函数:")
    for name, metadata in registry.list_functions().items():
        print(f"  {name}: {metadata}")
    
    # 调用函数
    print("\n函数调用测试:")
    print(registry.call("add", 5, 3))
    print(registry.call("greet", "张三"))
    print(registry.call("greet", "李四", greeting="Hi"))
    print(registry.call("analyze", 1, 2, 3, 4, 5, operation="avg"))
    
    print("\n=" * 50)
    print("高级挑战练习完成！")
    print("你已经掌握了：")
    print("1. 函数工厂模式 - 动态创建函数")
    print("2. 装饰器工厂 - 参数化装饰器")
    print("3. 函数注册系统 - 动态函数管理")
    print("4. 元编程技术 - 运行时函数操作")
    print("=" * 50)

def main():
    """
    主函数：运行所有练习
    """
    print("Python函数参数综合练习")
    print("=" * 80)
    
    exercises = [
        exercise_1_basic_parameters,
        exercise_2_default_parameters,
        exercise_3_variable_args,
        exercise_4_keyword_args,
        exercise_5_parameter_combinations,
        exercise_6_parameter_unpacking,
        exercise_7_parameter_validation,
        exercise_8_practical_applications,
        exercise_9_advanced_challenges
    ]
    
    for i, exercise in enumerate(exercises, 1):
        try:
            exercise()
        except Exception as e:
            print(f"\n练习 {i} 执行出错: {e}")
        
        if i < len(exercises):
            input("\n按回车键继续下一个练习...")
    
    print("\n" + "=" * 80)
    print("所有练习完成！")
    print("\n通过这些练习，你应该已经掌握了：")
    print("1. 位置参数和关键字参数的使用")
    print("2. 默认参数的设置和注意事项")
    print("3. 可变长度参数 (*args) 的应用")
    print("4. 关键字可变参数 (**kwargs) 的使用")
    print("5. 各种参数类型的组合使用")
    print("6. 参数解包技术")
    print("7. 参数验证的重要性和实现方法")
    print("8. 实际项目中的参数使用场景")
    print("9. 高级参数处理技术")
    print("\n继续练习，加深理解！")
    print("=" * 80)

if __name__ == "__main__":
    main()