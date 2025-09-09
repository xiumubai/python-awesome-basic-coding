#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
默认参数 (Default Parameters)

默认参数允许在函数定义时为参数指定默认值，
调用函数时如果不提供该参数的值，就会使用默认值。
这使得函数更加灵活，可以处理不同数量的参数。

学习目标：
1. 理解默认参数的概念和作用
2. 掌握默认参数的定义和使用
3. 了解默认参数的最佳实践
4. 避免默认参数的常见陷阱
"""

# 1. 基本的默认参数
def greet_user(name, greeting="你好"):
    """
    问候用户
    
    参数:
        name (str): 用户名
        greeting (str): 问候语，默认为"你好"
    """
    message = f"{greeting}，{name}！"
    print(message)
    return message

# 2. 多个默认参数
def create_user_account(username, email, role="user", active=True, notifications=True):
    """
    创建用户账户
    
    参数:
        username (str): 用户名（必需）
        email (str): 邮箱（必需）
        role (str): 用户角色，默认为"user"
        active (bool): 账户是否激活，默认为True
        notifications (bool): 是否接收通知，默认为True
    
    返回:
        dict: 用户账户信息
    """
    account = {
        'username': username,
        'email': email,
        'role': role,
        'active': active,
        'notifications': notifications
    }
    
    print(f"创建用户账户：{username}")
    print(f"  邮箱: {email}")
    print(f"  角色: {role}")
    print(f"  状态: {'激活' if active else '未激活'}")
    print(f"  通知: {'开启' if notifications else '关闭'}")
    print("-" * 30)
    
    return account

# 3. 默认参数与数值计算
def calculate_interest(principal, rate=0.05, time=1, compound_frequency=1):
    """
    计算复利
    
    参数:
        principal (float): 本金
        rate (float): 年利率，默认5%
        time (float): 时间（年），默认1年
        compound_frequency (int): 复利频率（每年），默认1次
    
    返回:
        float: 最终金额
    """
    # 复利公式: A = P(1 + r/n)^(nt)
    amount = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
    interest = amount - principal
    
    print(f"复利计算：")
    print(f"  本金: ¥{principal:,.2f}")
    print(f"  年利率: {rate*100:.2f}%")
    print(f"  时间: {time}年")
    print(f"  复利频率: 每年{compound_frequency}次")
    print(f"  最终金额: ¥{amount:,.2f}")
    print(f"  利息收入: ¥{interest:,.2f}")
    print("-" * 30)
    
    return amount

# 4. 默认参数与字符串处理
def format_text(text, width=80, align="left", fill_char=" ", truncate=False):
    """
    格式化文本
    
    参数:
        text (str): 要格式化的文本
        width (int): 文本宽度，默认80
        align (str): 对齐方式，默认"left"
        fill_char (str): 填充字符，默认空格
        truncate (bool): 是否截断过长文本，默认False
    
    返回:
        str: 格式化后的文本
    """
    if truncate and len(text) > width:
        text = text[:width-3] + "..."
    
    if align == "left":
        formatted = text.ljust(width, fill_char)
    elif align == "right":
        formatted = text.rjust(width, fill_char)
    elif align == "center":
        formatted = text.center(width, fill_char)
    else:
        formatted = text
    
    print(f"原文本: '{text}'")
    print(f"格式化: '{formatted}'")
    print(f"设置: 宽度={width}, 对齐={align}, 填充='{fill_char}', 截断={truncate}")
    print("-" * 50)
    
    return formatted

# 5. 默认参数与文件操作
def write_log(message, filename="app.log", timestamp=True, level="INFO"):
    """
    写入日志
    
    参数:
        message (str): 日志消息
        filename (str): 日志文件名，默认"app.log"
        timestamp (bool): 是否添加时间戳，默认True
        level (str): 日志级别，默认"INFO"
    """
    from datetime import datetime
    
    log_entry = f"[{level}] {message}"
    
    if timestamp:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{current_time}] {log_entry}"
    
    print(f"写入日志到 {filename}:")
    print(f"  {log_entry}")
    
    # 实际应用中这里会写入文件
    # with open(filename, 'a', encoding='utf-8') as f:
    #     f.write(log_entry + '\n')
    
    print("-" * 40)

# 6. 默认参数与数据处理
def process_data(data, sort_key=None, reverse=False, filter_func=None, limit=None):
    """
    处理数据列表
    
    参数:
        data (list): 数据列表
        sort_key (function): 排序键函数，默认None
        reverse (bool): 是否逆序，默认False
        filter_func (function): 过滤函数，默认None
        limit (int): 限制结果数量，默认None
    
    返回:
        list: 处理后的数据
    """
    result = data.copy()
    
    print(f"原始数据: {data}")
    
    # 过滤
    if filter_func:
        result = [item for item in result if filter_func(item)]
        print(f"过滤后: {result}")
    
    # 排序
    if sort_key:
        result.sort(key=sort_key, reverse=reverse)
    elif sort_key is None and (reverse or not reverse):  # 简单排序
        result.sort(reverse=reverse)
    
    if sort_key or reverse:
        print(f"排序后: {result}")
    
    # 限制数量
    if limit and limit > 0:
        result = result[:limit]
        print(f"限制{limit}个: {result}")
    
    print("-" * 40)
    return result

# 7. 默认参数的陷阱：可变对象作为默认值
def add_item_wrong(item, items=[]):  # 危险！不要这样做
    """
    错误的默认参数使用方式（演示用）
    
    注意：这是一个反面例子，展示了使用可变对象作为默认参数的问题
    """
    items.append(item)
    print(f"错误方式 - 当前列表: {items}")
    return items

def add_item_correct(item, items=None):  # 正确的方式
    """
    正确的默认参数使用方式
    
    参数:
        item: 要添加的项目
        items (list, optional): 目标列表，默认创建新列表
    
    返回:
        list: 包含新项目的列表
    """
    if items is None:
        items = []
    
    items.append(item)
    print(f"正确方式 - 当前列表: {items}")
    return items

# 8. 默认参数与配置选项
def setup_server(host="localhost", port=8000, debug=False, 
                 max_connections=100, timeout=30, ssl_enabled=False):
    """
    设置服务器配置
    
    参数:
        host (str): 主机地址，默认"localhost"
        port (int): 端口号，默认8000
        debug (bool): 调试模式，默认False
        max_connections (int): 最大连接数，默认100
        timeout (int): 超时时间（秒），默认30
        ssl_enabled (bool): 是否启用SSL，默认False
    
    返回:
        dict: 服务器配置
    """
    config = {
        'host': host,
        'port': port,
        'debug': debug,
        'max_connections': max_connections,
        'timeout': timeout,
        'ssl_enabled': ssl_enabled
    }
    
    print(f"服务器配置：")
    for key, value in config.items():
        print(f"  {key}: {value}")
    
    print(f"服务器地址: {'https' if ssl_enabled else 'http'}://{host}:{port}")
    print("-" * 40)
    
    return config

def main():
    """
    主函数：演示默认参数的各种用法
    """
    print("=" * 50)
    print("默认参数演示")
    print("=" * 50)
    
    # 1. 基本默认参数使用
    print("\n1. 基本默认参数：")
    greet_user("小明")  # 使用默认问候语
    greet_user("小红", "早上好")  # 自定义问候语
    greet_user("小李", greeting="晚上好")  # 使用关键字参数
    
    # 2. 多个默认参数
    print("\n2. 多个默认参数：")
    # 只提供必需参数
    create_user_account("john_doe", "john@example.com")
    
    # 提供部分可选参数
    create_user_account("admin_user", "admin@example.com", role="admin")
    
    # 提供所有参数
    create_user_account("guest_user", "guest@example.com", 
                       role="guest", active=False, notifications=False)
    
    # 3. 数值计算中的默认参数
    print("\n3. 数值计算默认参数：")
    # 使用所有默认值
    calculate_interest(10000)
    
    # 自定义利率
    calculate_interest(10000, rate=0.08)
    
    # 自定义时间和复利频率
    calculate_interest(10000, rate=0.06, time=2, compound_frequency=4)
    
    # 4. 文本格式化
    print("\n4. 文本格式化默认参数：")
    # 使用默认设置
    format_text("Hello World")
    
    # 自定义宽度和对齐
    format_text("Python", width=20, align="center")
    
    # 使用填充字符
    format_text("重要", width=30, align="center", fill_char="*")
    
    # 截断长文本
    long_text = "这是一段很长的文本，用来演示截断功能的效果"
    format_text(long_text, width=20, truncate=True)
    
    # 5. 日志写入
    print("\n5. 日志写入默认参数：")
    write_log("应用程序启动")
    write_log("用户登录成功", level="INFO")
    write_log("数据库连接失败", filename="error.log", level="ERROR")
    write_log("调试信息", timestamp=False, level="DEBUG")
    
    # 6. 数据处理
    print("\n6. 数据处理默认参数：")
    numbers = [64, 34, 25, 12, 22, 11, 90, 5]
    
    # 基本排序
    process_data(numbers)
    
    # 逆序排序
    process_data(numbers, reverse=True)
    
    # 过滤和限制
    process_data(numbers, 
                filter_func=lambda x: x > 20,
                reverse=True,
                limit=3)
    
    # 7. 默认参数陷阱演示
    print("\n7. 默认参数陷阱演示：")
    print("错误方式（可变对象作为默认值）：")
    list1 = add_item_wrong("第一项")
    list2 = add_item_wrong("第二项")  # 注意：这会修改同一个列表！
    print(f"list1 和 list2 是同一个对象: {list1 is list2}")
    
    print("\n正确方式：")
    list3 = add_item_correct("第一项")
    list4 = add_item_correct("第二项")  # 这会创建新的列表
    print(f"list3 和 list4 是不同对象: {list3 is not list4}")
    
    # 8. 服务器配置
    print("\n8. 服务器配置默认参数：")
    # 开发环境配置
    setup_server(debug=True)
    
    # 生产环境配置
    setup_server(host="0.0.0.0", 
                port=443, 
                ssl_enabled=True,
                max_connections=1000,
                timeout=60)
    
    # 测试环境配置
    setup_server(port=3000, debug=True, max_connections=10)
    
    print("\n=" * 50)
    print("默认参数要点总结：")
    print("1. 默认参数必须在非默认参数之后")
    print("2. 默认参数使函数调用更加灵活")
    print("3. 避免使用可变对象（如列表、字典）作为默认值")
    print("4. 使用None作为可变对象的默认值，然后在函数内部创建")
    print("5. 默认参数在函数定义时计算，不是每次调用时")
    print("6. 合理使用默认参数可以简化函数调用")
    print("=" * 50)

if __name__ == "__main__":
    main()