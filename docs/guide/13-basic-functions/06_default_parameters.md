# 函数默认参数详解

本节详细介绍Python函数的默认参数，包括基本用法、位置规则、常见陷阱和最佳实践。

## 学习目标

- 掌握默认参数的基本语法和用法
- 理解默认参数的位置规则
- 了解可变对象作为默认参数的陷阱
- 掌握默认参数的计算时机
- 学会默认参数的最佳实践
- 能够在实际项目中合理使用默认参数

## 1. 默认参数的基本用法

默认参数允许函数在调用时省略某些参数，使函数更加灵活易用：

```python
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

# 使用示例
print(greet("张三"))  # 使用默认greeting
print(greet("李四", "早上好"))  # 提供自定义greeting

print(f"2的平方：{power(2)}")  # 使用默认指数2
print(f"2的3次方：{power(2, 3)}")  # 指定指数3

# 创建用户示例
user1 = create_user("alice", "alice@example.com")  # 使用默认age和active
user2 = create_user("bob", "bob@example.com", 25, False)  # 指定所有参数
user3 = create_user("charlie", "charlie@example.com", age=30)  # 使用关键字参数
```

**默认参数的优势：**
- 提高函数的灵活性和易用性
- 减少函数调用时的代码量
- 为常用场景提供合理的默认值
- 保持向后兼容性

## 2. 默认参数的位置规则

默认参数必须位于非默认参数（必需参数）之后：

```python
# 正确：默认参数在非默认参数之后
def correct_function(required_param, optional_param="default"):
    return f"必需：{required_param}，可选：{optional_param}"

# 错误示例（会导致语法错误）
# def wrong_function(optional_param="default", required_param):
#     return f"这会导致语法错误"

def mixed_parameters(a, b, c=3, d=4, e=5):
    """混合参数示例"""
    return f"a={a}, b={b}, c={c}, d={d}, e={e}"

# 调用示例
print(correct_function("必需值"))  # 使用默认值
print(correct_function("必需值", "自定义值"))  # 覆盖默认值

# 混合参数调用方式
print(mixed_parameters(1, 2))  # 使用所有默认值
print(mixed_parameters(1, 2, 10))  # 覆盖c的默认值
print(mixed_parameters(1, 2, d=20))  # 使用关键字参数覆盖d
print(mixed_parameters(1, 2, 10, 20, 30))  # 覆盖所有默认值
```

**位置规则要点：**
- 必需参数必须在默认参数之前
- 一旦开始使用默认参数，后面的参数都必须有默认值
- 可以使用关键字参数跳过某些默认参数

## 3. 可变对象作为默认参数的陷阱

使用可变对象（如列表、字典）作为默认参数是Python中的常见陷阱：

```python
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

# 演示陷阱
print("错误的方式（共享默认列表）：")
result1 = bad_append("第一项")
print(f"第一次调用：{result1}")  # ["第一项"]
result2 = bad_append("第二项")
print(f"第二次调用：{result2}")  # ["第一项", "第二项"] - 包含了第一次的项目！

print("正确的方式（每次创建新列表）：")
result3 = good_append("第一项")
print(f"第一次调用：{result3}")  # ["第一项"]
result4 = good_append("第二项")
print(f"第二次调用：{result4}")  # ["第二项"] - 只包含当前项目
```

**陷阱原因：**
- 默认参数在函数定义时创建，所有调用共享同一个对象
- 对可变对象的修改会影响后续的函数调用
- 这种行为通常不是我们想要的

## 4. 默认参数的计算时机

默认参数的值在函数定义时计算，而不是在每次调用时：

```python
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

# 演示计算时机
print("错误方式（时间戳固定）：")
print(bad_timestamp("消息1"))
time.sleep(1)
print(bad_timestamp("消息2"))  # 时间戳相同！

print("正确方式（时间戳动态）：")
print(good_timestamp("消息1"))
time.sleep(1)
print(good_timestamp("消息2"))  # 时间戳不同
```

**计算时机要点：**
- 默认参数在函数定义时计算一次
- 如果需要动态值，使用None作为默认值
- 在函数内部进行实际的默认值计算

## 5. 复杂默认参数示例

在实际应用中，函数可能有多个默认参数：

```python
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

# 使用示例
conn1 = create_database_connection()  # 使用所有默认值
conn2 = create_database_connection(host="192.168.1.100", 
                                 database="production",
                                 ssl_enabled=True)  # 部分自定义

text = "Hello, World!"
print(format_text(text))  # 默认格式
print(format_text(text, width=30, align="center", add_border=True))  # 自定义格式
```

## 6. 实际应用示例

以下是默认参数在实际项目中的应用：

```python
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
    if cc:
        print(f"抄送：{', '.join(cc)}")
    
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
    
    return request_info

# 使用示例
# 发送简单邮件
send_email("user@example.com", "测试邮件", "这是一封测试邮件")

# 发送复杂邮件
send_email("user@example.com", "重要通知", "请查看附件",
          from_email="admin@company.com",
          cc=["manager@company.com"],
          priority="high",
          attachments=["report.pdf", "data.xlsx"])

# API请求
api_req1 = create_api_request("https://api.example.com/users")
api_req2 = create_api_request("https://api.example.com/posts", 
                             method="POST",
                             data={"title": "新文章", "content": "内容"})
```

## 7. 最佳实践

以下是使用默认参数的最佳实践：

```python
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

# 使用示例
result1 = best_practice_example("必需值")
result2 = best_practice_example("必需值", 
                               optional_str="自定义字符串",
                               optional_list=[1, 2, 3],
                               optional_dict={"key": "value"})
```

## 运行示例

你可以运行以下代码来测试默认参数：

```bash
python3 05_default_parameters.py
```

## 关键知识点总结

1. **基本语法**：`def func(param, default_param=default_value)`
2. **位置规则**：默认参数必须在非默认参数之后
3. **计算时机**：默认参数在函数定义时计算，不是调用时
4. **可变对象陷阱**：避免使用列表、字典等作为默认参数
5. **None模式**：使用None作为可变对象的默认值
6. **关键字参数**：可以跳过某些默认参数
7. **灵活调用**：提供多种调用方式
8. **向后兼容**：添加默认参数不会破坏现有代码

## 最佳实践建议

1. **合理的默认值**：选择最常用的值作为默认值
2. **避免可变对象**：使用None代替列表、字典等可变对象
3. **文档说明**：在文档中说明默认参数的含义和行为
4. **参数顺序**：将最重要的参数放在前面
5. **类型一致性**：确保默认值与参数类型一致
6. **避免副作用**：默认参数不应该有副作用
7. **测试覆盖**：测试有无默认参数的各种调用情况

## 练习建议

1. 编写一个配置函数，使用多个默认参数
2. 实现一个日志函数，合理使用默认参数
3. 创建一个数据处理函数，避免可变对象陷阱
4. 设计一个API客户端，使用默认参数简化调用
5. 分析现有代码中默认参数的使用是否合理

默认参数是Python函数的重要特性，正确使用可以大大提高代码的灵活性和易用性，但需要注意避免常见的陷阱。