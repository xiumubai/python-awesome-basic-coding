#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
函数参数详解

本文件演示Python函数参数的各种用法，包括：
1. 位置参数
2. 关键字参数
3. 参数的传递方式
4. 参数的顺序
5. 混合使用参数

作者：Python学习教程
日期：2024年
"""

print("=" * 50)
print("Python 函数参数详解")
print("=" * 50)

# 1. 位置参数（Positional Arguments）
print("\n1. 位置参数")
print("-" * 30)

def introduce_person(name, age, city):
    """使用位置参数的函数"""
    print(f"姓名：{name}，年龄：{age}，城市：{city}")

# 位置参数必须按顺序传递
print("按位置传递参数：")
introduce_person("张三", 25, "北京")
introduce_person("李四", 30, "上海")

# 位置参数的顺序很重要
print("\n注意：位置参数的顺序很重要")
print("正确顺序：introduce_person('王五', 28, '广州')")
introduce_person("王五", 28, "广州")
print("错误顺序：introduce_person(28, '王五', '广州')")
# introduce_person(28, "王五", "广州")  # 这会导致逻辑错误

# 2. 关键字参数（Keyword Arguments）
print("\n2. 关键字参数")
print("-" * 30)

def create_profile(name, age, city, job):
    """创建个人档案"""
    print(f"个人档案：")
    print(f"  姓名：{name}")
    print(f"  年龄：{age}")
    print(f"  城市：{city}")
    print(f"  职业：{job}")

# 使用关键字参数，顺序可以任意
print("使用关键字参数（顺序可以任意）：")
create_profile(name="赵六", age=32, city="深圳", job="工程师")
print()
create_profile(job="设计师", city="杭州", name="孙七", age=27)

# 3. 混合使用位置参数和关键字参数
print("\n3. 混合使用位置参数和关键字参数")
print("-" * 30)

def book_info(title, author, year=2024, publisher="未知出版社"):
    """图书信息函数"""
    print(f"书名：{title}")
    print(f"作者：{author}")
    print(f"出版年份：{year}")
    print(f"出版社：{publisher}")
    print()

# 位置参数必须在关键字参数之前
print("混合使用示例：")
book_info("Python编程", "作者A")  # 使用默认值
book_info("数据结构", "作者B", year=2023)  # 部分使用关键字参数
book_info("算法导论", "作者C", publisher="清华出版社", year=2022)  # 关键字参数顺序任意

# 4. 参数传递的详细示例
print("\n4. 参数传递的详细示例")
print("-" * 30)

def calculate_rectangle(length, width, unit="米"):
    """计算矩形面积和周长"""
    area = length * width
    perimeter = 2 * (length + width)
    print(f"矩形尺寸：{length}{unit} × {width}{unit}")
    print(f"面积：{area} 平方{unit}")
    print(f"周长：{perimeter} {unit}")
    print()

# 不同的调用方式
print("不同的参数传递方式：")
calculate_rectangle(5, 3)  # 全部位置参数
calculate_rectangle(5, 3, "厘米")  # 全部位置参数
calculate_rectangle(length=4, width=6)  # 全部关键字参数
calculate_rectangle(4, width=6, unit="英尺")  # 混合参数

# 5. 参数顺序规则演示
print("\n5. 参数顺序规则演示")
print("-" * 30)

def order_demo(pos1, pos2, key1="default1", key2="default2"):
    """演示参数顺序规则"""
    print(f"位置参数1：{pos1}")
    print(f"位置参数2：{pos2}")
    print(f"关键字参数1：{key1}")
    print(f"关键字参数2：{key2}")
    print()

print("正确的调用方式：")
order_demo("A", "B")  # 只传位置参数
order_demo("A", "B", "C")  # 位置参数 + 一个关键字参数
order_demo("A", "B", key2="D")  # 位置参数 + 指定关键字参数
order_demo("A", "B", key1="C", key2="D")  # 位置参数 + 所有关键字参数

# 错误的调用方式（注释掉避免报错）
# order_demo(pos1="A", "B")  # 错误：关键字参数后不能有位置参数

# 6. 实际应用示例
print("\n6. 实际应用示例")
print("-" * 30)

def send_email(to, subject, body, cc=None, bcc=None, priority="normal"):
    """发送邮件函数"""
    print(f"发送邮件：")
    print(f"  收件人：{to}")
    print(f"  主题：{subject}")
    print(f"  正文：{body}")
    if cc:
        print(f"  抄送：{cc}")
    if bcc:
        print(f"  密送：{bcc}")
    print(f"  优先级：{priority}")
    print()

# 不同的使用场景
print("邮件发送示例：")
send_email("user@example.com", "会议通知", "明天下午2点开会")
send_email("user@example.com", "紧急通知", "系统维护", priority="high")
send_email(
    to="user@example.com",
    subject="项目更新",
    body="项目进度报告",
    cc="manager@example.com",
    priority="normal"
)

# 7. 参数验证示例
print("\n7. 参数验证示例")
print("-" * 30)

def create_user(username, email, age, active=True):
    """创建用户，包含参数验证"""
    # 参数验证
    if not username or len(username) < 3:
        print("错误：用户名至少需要3个字符")
        return
    
    if "@" not in email:
        print("错误：邮箱格式不正确")
        return
    
    if age < 0 or age > 150:
        print("错误：年龄必须在0-150之间")
        return
    
    # 创建用户
    print(f"用户创建成功：")
    print(f"  用户名：{username}")
    print(f"  邮箱：{email}")
    print(f"  年龄：{age}")
    print(f"  状态：{'激活' if active else '未激活'}")
    print()

# 测试用户创建
print("用户创建测试：")
create_user("alice", "alice@example.com", 25)
create_user("bob", "bob@example.com", 30, active=False)
create_user("x", "invalid-email", -5)  # 这会触发验证错误

# 8. 函数参数的最佳实践
print("\n8. 函数参数的最佳实践")
print("-" * 30)

def good_function_example(required_param, optional_param="default", flag=False):
    """良好的函数参数设计示例"""
    result = f"必需参数：{required_param}"
    if optional_param != "default":
        result += f"，可选参数：{optional_param}"
    if flag:
        result += "，标志已启用"
    return result

print("最佳实践示例：")
print(good_function_example("重要数据"))
print(good_function_example("重要数据", "额外信息"))
print(good_function_example("重要数据", flag=True))
print(good_function_example("重要数据", "额外信息", True))

print("\n=" * 50)
print("函数参数学习完成！")
print("=" * 50)
print("\n总结：")
print("1. 位置参数：按顺序传递，顺序很重要")
print("2. 关键字参数：使用参数名传递，顺序不重要")
print("3. 位置参数必须在关键字参数之前")
print("4. 可以混合使用位置参数和关键字参数")
print("5. 合理使用参数可以让函数更灵活")
print("6. 参数验证是良好编程习惯")