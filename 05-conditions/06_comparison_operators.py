#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
比较运算符详解

本文件详细演示Python中各种比较运算符的用法，包括：
1. 基本比较运算符（==, !=, <, >, <=, >=）
2. 身份运算符（is, is not）
3. 成员运算符（in, not in）
4. 不同数据类型的比较
5. 比较运算符的链式使用

学习目标：
- 掌握所有比较运算符的用法
- 理解==与is的区别
- 学会在不同数据类型中使用比较运算符
- 掌握链式比较的写法
"""

# 1. 基本比较运算符
print("=== 1. 基本比较运算符 ===")
a = 10
b = 20
c = 10

# 等于 ==
print(f"{a} == {b}: {a == b}")  # False
print(f"{a} == {c}: {a == c}")  # True

# 不等于 !=
print(f"{a} != {b}: {a != b}")  # True
print(f"{a} != {c}: {a != c}")  # False

# 小于 <
print(f"{a} < {b}: {a < b}")   # True
print(f"{b} < {a}: {b < a}")   # False

# 大于 >
print(f"{a} > {b}: {a > b}")   # False
print(f"{b} > {a}: {b > a}")   # True

# 小于等于 <=
print(f"{a} <= {c}: {a <= c}") # True
print(f"{a} <= {b}: {a <= b}") # True

# 大于等于 >=
print(f"{b} >= {a}: {b >= a}") # True
print(f"{a} >= {c}: {a >= c}") # True

print()

# 2. 字符串比较
print("=== 2. 字符串比较 ===")
str1 = "apple"
str2 = "banana"
str3 = "apple"
str4 = "Apple"

# 字符串相等比较
print(f"'{str1}' == '{str3}': {str1 == str3}")  # True
print(f"'{str1}' == '{str4}': {str1 == str4}")  # False (大小写敏感)

# 字符串大小比较（按字典序）
print(f"'{str1}' < '{str2}': {str1 < str2}")   # True
print(f"'{str2}' > '{str1}': {str2 > str1}")   # True

# 大小写比较
print(f"'{str1}' < '{str4}': {str1 < str4}")   # False (小写字母ASCII值大于大写)
print(f"'{str4}' < '{str1}': {str4 < str1}")   # True

# 字符串长度不影响字典序比较
short_str = "z"
long_str = "apple"
print(f"'{short_str}' > '{long_str}': {short_str > long_str}")  # True

# 忽略大小写的比较
print(f"'{str1}'.lower() == '{str4}'.lower(): {str1.lower() == str4.lower()}")  # True

print()

# 3. 列表和元组比较
print("=== 3. 列表和元组比较 ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]
list4 = [1, 2]

# 列表相等比较
print(f"{list1} == {list2}: {list1 == list2}")  # True
print(f"{list1} == {list3}: {list1 == list3}")  # False

# 列表大小比较（逐元素比较）
print(f"{list1} < {list3}: {list1 < list3}")   # True (第三个元素3 < 4)
print(f"{list1} > {list4}: {list1 > list4}")   # True (长度更长)

# 元组比较
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (1, 3, 2)

print(f"{tuple1} == {tuple2}: {tuple1 == tuple2}")  # True
print(f"{tuple1} < {tuple3}: {tuple1 < tuple3}")   # True (第二个元素2 < 3)

# 不同类型容器比较（Python 3中会报错，这里仅作说明）
# print(f"{list1} == {tuple1}: {list1 == tuple1}")  # False

print()

# 4. 身份运算符 is 和 is not
print("=== 4. 身份运算符 is 和 is not ===")

# == vs is 的区别
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b: {a == b}")  # True (内容相同)
print(f"a is b: {a is b}")  # False (不是同一个对象)
print(f"a is c: {a is c}")  # True (是同一个对象)

print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}")

# 小整数和字符串的特殊情况
x = 100
y = 100
print(f"x is y (小整数): {x is y}")  # True (Python缓存小整数)

x = 1000
y = 1000
print(f"x is y (大整数): {x is y}")  # 可能为False

# None的比较
value = None
print(f"value is None: {value is None}")      # True
print(f"value is not None: {value is not None}")  # False

# 布尔值比较
flag = True
print(f"flag is True: {flag is True}")        # True
print(f"flag is not False: {flag is not False}")  # True

print()

# 5. 成员运算符 in 和 not in
print("=== 5. 成员运算符 in 和 not in ===")

# 列表中的成员检查
fruits = ["apple", "banana", "orange", "grape"]
print(f"'apple' in {fruits}: {'apple' in fruits}")        # True
print(f"'mango' in {fruits}: {'mango' in fruits}")        # False
print(f"'mango' not in {fruits}: {'mango' not in fruits}")  # True

# 字符串中的成员检查
text = "Hello, World!"
print(f"'Hello' in '{text}': {'Hello' in text}")         # True
print(f"'hello' in '{text}': {'hello' in text}")         # False (大小写敏感)
print(f"'xyz' not in '{text}': {'xyz' not in text}")     # True

# 字典中的成员检查（检查键）
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(f"'Alice' in student_grades: {'Alice' in student_grades}")    # True
print(f"'David' in student_grades: {'David' in student_grades}")    # False
print(f"85 in student_grades: {85 in student_grades}")              # False (检查的是键，不是值)

# 检查字典的值
print(f"85 in student_grades.values(): {85 in student_grades.values()}")  # True

# 元组中的成员检查
coordinates = (10, 20, 30)
print(f"20 in {coordinates}: {20 in coordinates}")        # True
print(f"40 not in {coordinates}: {40 not in coordinates}")  # True

# 集合中的成员检查
numbers = {1, 2, 3, 4, 5}
print(f"3 in {numbers}: {3 in numbers}")                 # True
print(f"6 not in {numbers}: {6 not in numbers}")         # True

print()

# 6. 链式比较
print("=== 6. 链式比较 ===")
score = 85

# 传统写法
if score >= 80 and score <= 100:
    print(f"分数{score}在优秀范围内（传统写法）")

# 链式比较写法
if 80 <= score <= 100:
    print(f"分数{score}在优秀范围内（链式比较）")

# 更复杂的链式比较
age = 25
if 18 <= age < 30:
    print(f"年龄{age}在青年范围内")

# 多个链式比较
a, b, c, d = 1, 5, 10, 15
if a < b < c < d:
    print(f"{a} < {b} < {c} < {d} 是递增序列")

# 等价的传统写法
if a < b and b < c and c < d:
    print(f"{a} < {b} < {c} < {d} 是递增序列（传统写法）")

print()

# 7. 浮点数比较的注意事项
print("=== 7. 浮点数比较注意事项 ===")

# 浮点数精度问题
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")
print(f"0.1 + 0.2 == 0.3: {result == 0.3}")  # False!

# 正确的浮点数比较方法
import math

def float_equal(a, b, tolerance=1e-9):
    """安全的浮点数相等比较"""
    return abs(a - b) < tolerance

print(f"float_equal(0.1 + 0.2, 0.3): {float_equal(result, 0.3)}")

# 使用math.isclose()（Python 3.5+）
print(f"math.isclose(0.1 + 0.2, 0.3): {math.isclose(result, 0.3)}")

print()

# 8. 实际应用：成绩评定系统
print("=== 8. 成绩评定系统 ===")

def evaluate_grade(score):
    """根据分数评定等级"""
    if not (0 <= score <= 100):
        return "无效分数"
    elif score >= 90:
        return "A (优秀)"
    elif score >= 80:
        return "B (良好)"
    elif score >= 70:
        return "C (中等)"
    elif score >= 60:
        return "D (及格)"
    else:
        return "F (不及格)"

# 测试不同分数
test_scores = [95, 87, 73, 65, 45, 105, -10]
for score in test_scores:
    grade = evaluate_grade(score)
    print(f"分数 {score}: {grade}")

print()

# 9. 用户权限检查系统
print("=== 9. 用户权限检查系统 ===")

class User:
    def __init__(self, username, role, level, permissions):
        self.username = username
        self.role = role
        self.level = level
        self.permissions = permissions

def check_access(user, required_role=None, min_level=0, required_permissions=None):
    """检查用户访问权限"""
    # 检查角色
    if required_role and user.role != required_role:
        if user.role not in ["admin", "superuser"]:
            return False, "角色权限不足"
    
    # 检查等级
    if user.level < min_level:
        return False, f"等级不足，需要等级 {min_level}"
    
    # 检查特定权限
    if required_permissions:
        for permission in required_permissions:
            if permission not in user.permissions:
                return False, f"缺少权限: {permission}"
    
    return True, "访问允许"

# 创建测试用户
users = [
    User("alice", "admin", 5, ["read", "write", "delete", "manage"]),
    User("bob", "editor", 3, ["read", "write"]),
    User("charlie", "viewer", 1, ["read"]),
]

# 测试不同的访问需求
access_requirements = [
    {"required_role": "editor", "min_level": 2, "required_permissions": ["write"]},
    {"required_role": "admin", "min_level": 4, "required_permissions": ["delete"]},
    {"min_level": 1, "required_permissions": ["read"]},
]

for i, req in enumerate(access_requirements, 1):
    print(f"\n访问需求 {i}: {req}")
    for user in users:
        allowed, message = check_access(user, **req)
        status = "✓" if allowed else "✗"
        print(f"  {status} {user.username} ({user.role}, L{user.level}): {message}")

print()

# 10. 数据验证示例
print("=== 10. 数据验证示例 ===")

def validate_user_data(data):
    """验证用户数据"""
    errors = []
    
    # 检查必需字段
    required_fields = ["username", "email", "age"]
    for field in required_fields:
        if field not in data:
            errors.append(f"缺少必需字段: {field}")
    
    if errors:  # 如果有缺少字段，直接返回
        return False, errors
    
    # 用户名验证
    username = data["username"]
    if not (3 <= len(username) <= 20):
        errors.append("用户名长度必须在3-20个字符之间")
    
    if not username.isalnum():
        errors.append("用户名只能包含字母和数字")
    
    # 邮箱验证（简单版）
    email = data["email"]
    if "@" not in email or "." not in email:
        errors.append("邮箱格式不正确")
    
    # 年龄验证
    age = data["age"]
    if not isinstance(age, int) or not (13 <= age <= 120):
        errors.append("年龄必须是13-120之间的整数")
    
    # 可选字段验证
    if "phone" in data:
        phone = data["phone"]
        if not (phone.isdigit() and len(phone) >= 10):
            errors.append("电话号码格式不正确")
    
    return len(errors) == 0, errors

# 测试数据验证
test_data = [
    {"username": "john123", "email": "john@example.com", "age": 25},
    {"username": "a", "email": "invalid-email", "age": 5},
    {"email": "test@example.com", "age": 30},  # 缺少username
    {"username": "valid_user", "email": "user@test.com", "age": 28, "phone": "1234567890"},
]

for i, data in enumerate(test_data, 1):
    is_valid, errors = validate_user_data(data)
    print(f"\n测试数据 {i}: {data}")
    if is_valid:
        print("✓ 数据验证通过")
    else:
        print("✗ 数据验证失败:")
        for error in errors:
            print(f"  - {error}")

print()
print("=== 程序结束 ===")

# 练习题
print("\n=== 练习题 ===")
print("1. 编写函数比较两个列表是否相等（不使用==运算符）")
print("2. 编写函数判断一个字符串是否为回文（使用比较运算符）")
print("3. 编写程序找出列表中的最大值和最小值（使用比较运算符）")
print("4. 编写函数验证密码强度（长度、字符类型、特殊字符等）")
print("5. 编写程序实现简单的排序算法（如冒泡排序，使用比较运算符）")