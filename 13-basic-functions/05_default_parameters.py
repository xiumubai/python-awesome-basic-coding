#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
函数默认参数详解

本文件演示Python函数的默认参数，包括：
1. 默认参数的基本用法
2. 默认参数的位置规则
3. 可变对象作为默认参数的陷阱
4. 默认参数的最佳实践
5. 实际应用示例

作者：Python学习教程
日期：2024年
"""

print("=" * 50)
print("Python 函数默认参数详解")
print("=" * 50)

# 1. 默认参数的基本用法
print("\n1. 默认参数的基本用法")
print("-" * 30)

def greet(name, greeting="你好"):
    """带默认参数的问候函数"""
    return f"{greeting}，{name}！"

def power(base, exponent=2):
    """计算幂，默认计算平方"""
    return base ** exponent

def create_user(username, email, age=18, active=True):
    """创建用户，带多个默认参数"""
    user = {
        "username": username,
        "email": email,
        "age": age,
        "active": active
    }
    return user

print("基本默认参数演示：")
print(greet("张三"))  # 使用默认greeting
print(greet("李四", "早上好"))  # 提供自定义greeting

print(f"\n2的平方：{power(2)}")
print(f"2的3次方：{power(2, 3)}")
print(f"5的平方：{power(5)}")

print("\n创建用户示例：")
user1 = create_user("alice", "alice@example.com")
print(f"用户1：{user1}")

user2 = create_user("bob", "bob@example.com", 25, False)
print(f"用户2：{user2}")

user3 = create_user("charlie", "charlie@example.com", age=30)
print(f"用户3：{user3}")
print()

# 2. 默认参数的位置规则
print("\n2. 默认参数的位置规则")
print("-" * 30)

# 正确：默认参数在非默认参数之后
def correct_function(required_param, optional_param="default"):
    return f"必需：{required_param}，可选：{optional_param}"

# 错误示例（注释掉，因为会导致语法错误）
# def wrong_function(optional_param="default", required_param):
#     return f"这会导致语法错误"

def mixed_parameters(a, b, c=3, d=4, e=5):
    """混合参数示例"""
    return f"a={a}, b={b}, c={c}, d={d}, e={e}"

print("参数位置规则演示：")
print(correct_function("必需值"))
print(correct_function("必需值", "自定义值"))

print("\n混合参数调用：")
print(mixed_parameters(1, 2))  # 使用所有默认值
print(mixed_parameters(1, 2, 10))  # 覆盖c的默认值
print(mixed_parameters(1, 2, d=20))  # 使用关键字参数覆盖d
print(mixed_parameters(1, 2, 10, 20, 30))  # 覆盖所有默认值
print()

# 3. 可变对象作为默认参数的陷阱
print("\n3. 可变对象作为默认参数的陷阱")
print("-" * 30)

# 错误的方式：使用可变对象作为默认参数
def bad_append(item, target_list=[]):
    """危险：使用可变对象作为默认参数"""
    target_list.append(item)
    return target_list

# 正确的方式：使用None作为默认值
def good_append(item, target_list=None):
    """安全：使用None作为默认值"""
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list

# 另一种正确方式：使用copy
def safe_append(item, target_list=None):
    """安全：创建新列表的副本"""
    if target_list is None:
        target_list = []
    else:
        target_list = target_list.copy()  # 创建副本
    target_list.append(item)
    return target_list

print("可变对象陷阱演示：")
print("错误的方式（共享默认列表）：")
result1 = bad_append("第一项")
print(f"第一次调用：{result1}")
result2 = bad_append("第二项")
print(f"第二次调用：{result2}")  # 注意：包含了第一次的项目！
result3 = bad_append("第三项")
print(f"第三次调用：{result3}")  # 包含了前面所有的项目！

print("\n正确的方式（每次创建新列表）：")
result4 = good_append("第一项")
print(f"第一次调用：{result4}")
result5 = good_append("第二项")
print(f"第二次调用：{result5}")  # 只包含当前项目
result6 = good_append("第三项")
print(f"第三次调用：{result6}")  # 只包含当前项目
print()

# 4. 默认参数的计算时机
print("\n4. 默认参数的计算时机")
print("-" * 30)

import time
from datetime import datetime

# 错误：默认参数在函数定义时计算
def bad_timestamp(message, timestamp=datetime.now()):
    """错误：时间戳在函数定义时就固定了"""
    return f"{timestamp}: {message}"

# 正确：在函数调用时计算
def good_timestamp(message, timestamp=None):
    """正确：每次调用时获取当前时间"""
    if timestamp is None:
        timestamp = datetime.now()
    return f"{timestamp}: {message}"

print("默认参数计算时机演示：")
print("错误方式（时间戳固定）：")
print(bad_timestamp("消息1"))
time.sleep(1)
print(bad_timestamp("消息2"))  # 时间戳相同！

print("\n正确方式（时间戳动态）：")
print(good_timestamp("消息1"))
time.sleep(1)
print(good_timestamp("消息2"))  # 时间戳不同
print()

# 5. 复杂默认参数示例
print("\n5. 复杂默认参数示例")
print("-" * 30)

def create_database_connection(host="localhost", port=5432, 
                             database="mydb", username="user",
                             password=None, timeout=30, 
                             ssl_enabled=False, options=None):
    """创建数据库连接（模拟）"""
    if password is None:
        password = "default_password"
    
    if options is None:
        options = {"autocommit": True, "charset": "utf8"}
    
    connection_info = {
        "host": host,
        "port": port,
        "database": database,
        "username": username,
        "password": "*" * len(password),  # 隐藏密码
        "timeout": timeout,
        "ssl_enabled": ssl_enabled,
        "options": options
    }
    
    return connection_info

def format_text(text, width=80, align="left", fill_char=" ", 
               uppercase=False, add_border=False):
    """格式化文本"""
    if uppercase:
        text = text.upper()
    
    if align == "center":
        formatted = text.center(width, fill_char)
    elif align == "right":
        formatted = text.rjust(width, fill_char)
    else:  # left
        formatted = text.ljust(width, fill_char)
    
    if add_border:
        border = "*" * width
        formatted = f"{border}\n{formatted}\n{border}"
    
    return formatted

print("复杂默认参数演示：")
print("数据库连接（使用默认值）：")
conn1 = create_database_connection()
for key, value in conn1.items():
    print(f"  {key}: {value}")

print("\n数据库连接（自定义部分参数）：")
conn2 = create_database_connection(host="192.168.1.100", 
                                 database="production",
                                 ssl_enabled=True)
for key, value in conn2.items():
    print(f"  {key}: {value}")

print("\n文本格式化演示：")
text = "Hello, World!"
print("默认格式：")
print(f"'{format_text(text)}'")

print("\n居中对齐，添加边框：")
print(format_text(text, width=30, align="center", add_border=True))

print("\n右对齐，大写，用-填充：")
print(f"'{format_text(text, width=25, align='right', fill_char='-', uppercase=True)}'")
print()

# 6. 实际应用示例
print("\n6. 实际应用示例")
print("-" * 30)

def send_email(to, subject, body, from_email="noreply@example.com",
              cc=None, bcc=None, priority="normal", 
              content_type="text/plain", attachments=None):
    """发送邮件（模拟）"""
    if cc is None:
        cc = []
    if bcc is None:
        bcc = []
    if attachments is None:
        attachments = []
    
    email_info = {
        "to": to,
        "from": from_email,
        "subject": subject,
        "body": body,
        "cc": cc,
        "bcc": bcc,
        "priority": priority,
        "content_type": content_type,
        "attachments": attachments
    }
    
    print(f"邮件已发送到：{to}")
    print(f"主题：{subject}")
    print(f"发件人：{from_email}")
    if cc:
        print(f"抄送：{', '.join(cc)}")
    if attachments:
        print(f"附件：{', '.join(attachments)}")
    
    return email_info

def create_api_request(url, method="GET", headers=None, params=None,
                      data=None, timeout=30, verify_ssl=True,
                      retry_count=3):
    """创建API请求（模拟）"""
    if headers is None:
        headers = {"User-Agent": "Python-App/1.0"}
    if params is None:
        params = {}
    
    request_info = {
        "url": url,
        "method": method,
        "headers": headers,
        "params": params,
        "data": data,
        "timeout": timeout,
        "verify_ssl": verify_ssl,
        "retry_count": retry_count
    }
    
    print(f"API请求：{method} {url}")
    if params:
        print(f"参数：{params}")
    
    return request_info

print("实际应用示例：")
print("发送简单邮件：")
send_email("user@example.com", "测试邮件", "这是一封测试邮件")

print("\n发送复杂邮件：")
send_email("user@example.com", "重要通知", "请查看附件",
          from_email="admin@company.com",
          cc=["manager@company.com"],
          priority="high",
          attachments=["report.pdf", "data.xlsx"])

print("\nAPI请求示例：")
api_req1 = create_api_request("https://api.example.com/users")
api_req2 = create_api_request("https://api.example.com/posts", 
                             method="POST",
                             data={"title": "新文章", "content": "内容"},
                             headers={"Authorization": "Bearer token123"})
print()

# 7. 最佳实践总结
print("\n7. 默认参数最佳实践")
print("-" * 30)

def best_practice_example(required_param, optional_str="default",
                         optional_num=0, optional_bool=False,
                         optional_list=None, optional_dict=None):
    """默认参数最佳实践示例"""
    # 处理可变对象的默认值
    if optional_list is None:
        optional_list = []
    if optional_dict is None:
        optional_dict = {}
    
    # 创建副本以避免修改原始对象
    safe_list = optional_list.copy()
    safe_dict = optional_dict.copy()
    
    result = {
        "required": required_param,
        "string": optional_str,
        "number": optional_num,
        "boolean": optional_bool,
        "list": safe_list,
        "dict": safe_dict
    }
    
    return result

print("最佳实践演示：")
result = best_practice_example("必需值")
print(f"使用默认值：{result}")

result2 = best_practice_example("必需值", 
                               optional_str="自定义字符串",
                               optional_list=[1, 2, 3],
                               optional_dict={"key": "value"})
print(f"自定义值：{result2}")

print("\n=" * 50)
print("函数默认参数学习完成！")
print("=" * 50)
print("\n总结：")
print("1. 默认参数必须位于非默认参数之后")
print("2. 默认参数在函数定义时计算，不是调用时")
print("3. 避免使用可变对象作为默认参数")
print("4. 使用None作为可变对象的默认值")
print("5. 默认参数可以提高函数的灵活性")
print("6. 合理使用默认参数可以简化函数调用")
print("7. 注意默认参数的陷阱和最佳实践")