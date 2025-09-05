#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
输入验证和类型转换

学习目标：
1. 掌握输入数据的类型转换
2. 学会验证用户输入的有效性
3. 了解异常处理在输入验证中的应用
4. 掌握常见的输入验证技巧

作者：Python基础教程
日期：2024年
"""

# ============================================================================
# 1. 基本类型转换
# ============================================================================

print("=" * 50)
print("1. 基本类型转换")
print("=" * 50)

# input()返回字符串，需要转换为其他类型
print("\n--- 字符串转整数 ---")
str_num = "123"  # 模拟用户输入
print(f"字符串：'{str_num}' (类型：{type(str_num)})")

# 转换为整数
int_num = int(str_num)
print(f"整数：{int_num} (类型：{type(int_num)})")

# 转换为浮点数
float_num = float(str_num)
print(f"浮点数：{float_num} (类型：{type(float_num)})")

print("\n--- 字符串转浮点数 ---")
str_float = "3.14"  # 模拟用户输入
print(f"字符串：'{str_float}' (类型：{type(str_float)})")

float_val = float(str_float)
print(f"浮点数：{float_val} (类型：{type(float_val)})")

# ============================================================================
# 2. 类型转换异常处理
# ============================================================================

print("\n=" * 50)
print("2. 类型转换异常处理")
print("=" * 50)

# 处理无效输入
print("\n--- 处理无效的数字输入 ---")
invalid_inputs = ["abc", "12.3.4", "", "  ", "12a"]

for invalid_input in invalid_inputs:
    print(f"\n尝试转换：'{invalid_input}'")
    
    # 尝试转换为整数
    try:
        result = int(invalid_input)
        print(f"  转换为整数成功：{result}")
    except ValueError as e:
        print(f"  转换为整数失败：{e}")
    
    # 尝试转换为浮点数
    try:
        result = float(invalid_input)
        print(f"  转换为浮点数成功：{result}")
    except ValueError as e:
        print(f"  转换为浮点数失败：{e}")

# ============================================================================
# 3. 安全的输入转换函数
# ============================================================================

print("\n=" * 50)
print("3. 安全的输入转换函数")
print("=" * 50)

def safe_int_input(prompt, default=None):
    """
    安全地获取整数输入
    
    Args:
        prompt: 提示信息
        default: 默认值（转换失败时返回）
    
    Returns:
        int or None: 转换成功返回整数，失败返回默认值
    """
    user_input = input(prompt) if prompt else "25"  # 模拟输入
    try:
        return int(user_input.strip())
    except ValueError:
        print(f"输入'{user_input}'不是有效的整数")
        return default

def safe_float_input(prompt, default=None):
    """
    安全地获取浮点数输入
    
    Args:
        prompt: 提示信息
        default: 默认值（转换失败时返回）
    
    Returns:
        float or None: 转换成功返回浮点数，失败返回默认值
    """
    user_input = input(prompt) if prompt else "3.14"  # 模拟输入
    try:
        return float(user_input.strip())
    except ValueError:
        print(f"输入'{user_input}'不是有效的数字")
        return default

# 测试安全输入函数
print("\n--- 测试安全输入函数 ---")

# 模拟有效输入
print("模拟输入有效整数：")
age = safe_int_input("请输入年龄：", 0)
print(f"年龄：{age}")

print("\n模拟输入有效浮点数：")
height = safe_float_input("请输入身高(米)：", 0.0)
print(f"身高：{height}米")

# ============================================================================
# 4. 输入范围验证
# ============================================================================

print("\n=" * 50)
print("4. 输入范围验证")
print("=" * 50)

def get_age_input():
    """
    获取有效的年龄输入（0-150岁）
    """
    age_str = "25"  # 模拟用户输入
    print(f"请输入年龄（0-150）：{age_str}")
    
    try:
        age = int(age_str.strip())
        if 0 <= age <= 150:
            return age
        else:
            print(f"年龄{age}超出有效范围（0-150）")
            return None
    except ValueError:
        print(f"'{age_str}'不是有效的年龄")
        return None

def get_score_input():
    """
    获取有效的分数输入（0-100分）
    """
    score_str = "85.5"  # 模拟用户输入
    print(f"请输入分数（0-100）：{score_str}")
    
    try:
        score = float(score_str.strip())
        if 0 <= score <= 100:
            return score
        else:
            print(f"分数{score}超出有效范围（0-100）")
            return None
    except ValueError:
        print(f"'{score_str}'不是有效的分数")
        return None

# 测试范围验证
print("\n--- 测试范围验证 ---")
valid_age = get_age_input()
print(f"有效年龄：{valid_age}")

valid_score = get_score_input()
print(f"有效分数：{valid_score}")

# ============================================================================
# 5. 字符串输入验证
# ============================================================================

print("\n=" * 50)
print("5. 字符串输入验证")
print("=" * 50)

def validate_name(name):
    """
    验证姓名输入
    
    Args:
        name: 输入的姓名
    
    Returns:
        bool: 是否有效
    """
    # 去除首尾空格
    name = name.strip()
    
    # 检查是否为空
    if not name:
        print("姓名不能为空")
        return False
    
    # 检查长度
    if len(name) < 2 or len(name) > 20:
        print("姓名长度应在2-20个字符之间")
        return False
    
    # 检查是否包含数字
    if any(char.isdigit() for char in name):
        print("姓名不应包含数字")
        return False
    
    return True

def validate_email(email):
    """
    简单的邮箱验证
    
    Args:
        email: 输入的邮箱
    
    Returns:
        bool: 是否有效
    """
    email = email.strip()
    
    # 基本格式检查
    if '@' not in email:
        print("邮箱格式错误：缺少@符号")
        return False
    
    if email.count('@') != 1:
        print("邮箱格式错误：@符号数量不正确")
        return False
    
    local, domain = email.split('@')
    
    if not local or not domain:
        print("邮箱格式错误：@前后不能为空")
        return False
    
    if '.' not in domain:
        print("邮箱格式错误：域名格式不正确")
        return False
    
    return True

# 测试字符串验证
print("\n--- 测试姓名验证 ---")
test_names = ["张三", "李四", "", "a", "这是一个非常长的姓名超过了限制", "张3"]

for name in test_names:
    print(f"验证姓名'{name}'：{validate_name(name)}")

print("\n--- 测试邮箱验证 ---")
test_emails = [
    "user@example.com",
    "invalid-email",
    "user@@example.com",
    "@example.com",
    "user@",
    "user@example"
]

for email in test_emails:
    print(f"验证邮箱'{email}'：{validate_email(email)}")

# ============================================================================
# 6. 循环输入直到有效
# ============================================================================

print("\n=" * 50)
print("6. 循环输入直到有效")
print("=" * 50)

def get_valid_integer(prompt, min_val=None, max_val=None, max_attempts=3):
    """
    循环获取有效整数输入
    
    Args:
        prompt: 提示信息
        min_val: 最小值
        max_val: 最大值
        max_attempts: 最大尝试次数
    
    Returns:
        int or None: 有效整数或None（超过最大尝试次数）
    """
    # 模拟用户输入序列
    mock_inputs = ["abc", "200", "25"]  # 第一次无效，第二次超范围，第三次有效
    attempt = 0
    
    for attempt in range(max_attempts):
        try:
            # 模拟用户输入
            user_input = mock_inputs[attempt] if attempt < len(mock_inputs) else "25"
            print(f"\n尝试 {attempt + 1}/{max_attempts}")
            print(f"{prompt}{user_input}")
            
            value = int(user_input.strip())
            
            # 检查范围
            if min_val is not None and value < min_val:
                print(f"输入值{value}小于最小值{min_val}")
                continue
            
            if max_val is not None and value > max_val:
                print(f"输入值{value}大于最大值{max_val}")
                continue
            
            print(f"输入有效：{value}")
            return value
            
        except ValueError:
            print(f"'{user_input}'不是有效的整数")
    
    print(f"\n超过最大尝试次数({max_attempts})，输入失败")
    return None

# 测试循环输入
print("\n--- 测试循环输入验证 ---")
result = get_valid_integer("请输入年龄（18-65）：", 18, 65, 3)
print(f"\n最终结果：{result}")

# ============================================================================
# 7. 综合应用示例
# ============================================================================

print("\n=" * 50)
print("7. 综合应用示例")
print("=" * 50)

def collect_user_info():
    """
    收集用户信息的综合示例
    """
    print("\n=== 用户信息收集系统 ===")
    
    # 模拟用户输入
    user_data = {
        'name': '张三',
        'age': '25',
        'email': 'zhangsan@example.com',
        'score': '85.5'
    }
    
    # 收集姓名
    print(f"\n请输入姓名：{user_data['name']}")
    name = user_data['name']
    if not validate_name(name):
        print("姓名验证失败")
        return None
    
    # 收集年龄
    print(f"请输入年龄：{user_data['age']}")
    try:
        age = int(user_data['age'])
        if not (0 <= age <= 150):
            print("年龄超出有效范围")
            return None
    except ValueError:
        print("年龄格式错误")
        return None
    
    # 收集邮箱
    print(f"请输入邮箱：{user_data['email']}")
    email = user_data['email']
    if not validate_email(email):
        print("邮箱验证失败")
        return None
    
    # 收集分数
    print(f"请输入分数：{user_data['score']}")
    try:
        score = float(user_data['score'])
        if not (0 <= score <= 100):
            print("分数超出有效范围")
            return None
    except ValueError:
        print("分数格式错误")
        return None
    
    # 返回收集的信息
    return {
        'name': name,
        'age': age,
        'email': email,
        'score': score
    }

# 运行综合示例
user_info = collect_user_info()
if user_info:
    print("\n=== 信息收集成功 ===")
    print(f"姓名：{user_info['name']}")
    print(f"年龄：{user_info['age']}岁")
    print(f"邮箱：{user_info['email']}")
    print(f"分数：{user_info['score']}分")
else:
    print("\n信息收集失败")

# ============================================================================
# 8. 练习题
# ============================================================================

print("\n=" * 50)
print("8. 练习题")
print("=" * 50)

print("""
练习题：

1. 基础练习：
   - 编写函数验证手机号码格式（11位数字）
   - 编写函数获取有效的百分比输入（0-100%）
   - 实现一个安全的除法计算器（处理除零错误）

2. 进阶练习：
   - 编写一个学生成绩管理系统的输入验证模块
   - 实现一个带重试机制的用户注册系统
   - 编写函数验证身份证号码格式

3. 思考题：
   - 为什么需要对用户输入进行验证？
   - 如何平衡用户体验和输入验证的严格性？
   - 在什么情况下应该使用异常处理？

4. 挑战练习：
   - 实现一个通用的输入验证框架
   - 编写一个支持多种数据类型的配置文件读取器
   - 实现一个智能的输入建议系统
""")

# ============================================================================
# 9. 知识点总结
# ============================================================================

print("\n=" * 50)
print("9. 知识点总结")
print("=" * 50)

print("""
知识点总结：

1. 类型转换：
   - int(): 转换为整数
   - float(): 转换为浮点数
   - str(): 转换为字符串
   - 转换可能抛出ValueError异常

2. 异常处理：
   - 使用try-except处理转换错误
   - ValueError: 类型转换失败
   - 提供默认值或重新输入机制

3. 输入验证策略：
   - 类型验证：确保数据类型正确
   - 范围验证：确保数值在有效范围内
   - 格式验证：确保字符串格式正确
   - 逻辑验证：确保数据符合业务逻辑

4. 最佳实践：
   - 提供清晰的错误信息
   - 实现重试机制
   - 设置合理的默认值
   - 考虑用户体验

5. 常用验证模式：
   - 立即验证：输入后立即检查
   - 批量验证：收集所有输入后统一验证
   - 渐进验证：逐步引导用户输入正确数据
""")

print("\n程序运行完成！")
print("建议：尝试修改模拟输入，测试不同的验证场景。")