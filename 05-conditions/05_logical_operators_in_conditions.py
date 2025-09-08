#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
条件中的逻辑运算符

本文件演示Python中逻辑运算符在条件语句中的用法，包括：
1. and运算符的使用
2. or运算符的使用
3. not运算符的使用
4. 逻辑运算符的组合使用
5. 短路求值的概念

学习目标：
- 掌握and、or、not逻辑运算符的用法
- 理解逻辑运算符的优先级
- 学会组合使用多个逻辑运算符
- 理解短路求值的机制
"""

# 1. and运算符 - 所有条件都必须为True
print("=== 1. and运算符 ===")
age = 25
income = 50000
has_job = True

# 基本and用法
if age >= 18 and income >= 30000:
    print("符合贷款基本条件")
else:
    print("不符合贷款基本条件")

# 多个and条件
if age >= 18 and income >= 30000 and has_job:
    print("符合所有贷款条件")
    print("可以申请贷款")
else:
    print("不符合所有条件")

# 数值范围判断
score = 85
if score >= 80 and score <= 100:
    print(f"分数{score}在优秀范围内")

# 更简洁的范围判断写法
if 80 <= score <= 100:
    print(f"分数{score}在优秀范围内（简洁写法）")

print()

# 2. or运算符 - 任一条件为True即可
print("=== 2. or运算符 ===")
day = "Saturday"
weather = "sunny"
is_holiday = False

# 基本or用法
if day == "Saturday" or day == "Sunday":
    print("今天是周末！")

# 多个or条件
if day == "Saturday" or day == "Sunday" or is_holiday:
    print("今天可以休息！")

# 使用in操作符简化多个or条件
if day in ["Saturday", "Sunday"]:
    print("今天是周末（使用in简化）")

# 复杂or条件
temperature = 25
if weather == "sunny" or (weather == "cloudy" and temperature > 20):
    print("适合外出活动")

print()

# 3. not运算符 - 取反操作
print("=== 3. not运算符 ===")
is_raining = False
is_working_day = True
has_homework = False

# 基本not用法
if not is_raining:
    print("没有下雨，可以出门")

# not与其他运算符组合
if not is_working_day and not has_homework:
    print("既不用工作也没有作业，可以放松")

# not用于列表和字符串
empty_list = []
if not empty_list:
    print("列表为空")

username = ""
if not username:
    print("用户名不能为空")

# not与比较运算符
age = 16
if not (age >= 18):
    print("未成年")

# 等价于
if age < 18:
    print("未成年（等价写法）")

print()

# 4. 逻辑运算符的组合使用
print("=== 4. 逻辑运算符组合使用 ===")
student_age = 20
student_score = 88
attendance_rate = 0.95
is_international = False
has_scholarship = True

# 复杂的逻辑组合
if (student_age >= 18 and student_score >= 85) or (is_international and student_score >= 80):
    print("符合奖学金申请条件")
    
    if attendance_rate >= 0.9 and not has_scholarship:
        print("可以申请新的奖学金")
    elif has_scholarship:
        print("已有奖学金，可以申请额外奖励")
    else:
        print("出勤率不足，需要改善")

print()

# 5. 用户权限验证系统
print("=== 5. 用户权限验证系统 ===")
user_role = "editor"
user_level = 3
is_account_active = True
has_special_permission = False
login_attempts = 1
max_attempts = 3

# 复杂的权限判断
if is_account_active and login_attempts < max_attempts:
    print("账户状态正常，可以尝试登录")
    
    # 管理员权限
    if user_role == "admin" or (user_role == "editor" and user_level >= 5):
        print("拥有管理员权限")
        access_level = "full"
    
    # 编辑权限
    elif user_role == "editor" and (user_level >= 3 or has_special_permission):
        print("拥有编辑权限")
        access_level = "edit"
    
    # 查看权限
    elif user_role in ["viewer", "guest"] and not (user_level < 1):
        print("拥有查看权限")
        access_level = "read"
    
    else:
        print("权限不足")
        access_level = "none"
        
else:
    print("账户被锁定或登录次数过多")
    access_level = "blocked"

print(f"最终访问级别：{access_level}")
print()

# 6. 短路求值演示
print("=== 6. 短路求值演示 ===")

def expensive_function():
    """模拟一个耗时的函数"""
    print("执行了耗时函数")
    return True

def another_function():
    """另一个函数"""
    print("执行了另一个函数")
    return False

# and短路求值：如果第一个条件为False，不会执行后面的条件
print("测试and短路求值：")
if False and expensive_function():
    print("这行不会执行")
print("expensive_function没有被调用")

# or短路求值：如果第一个条件为True，不会执行后面的条件
print("\n测试or短路求值：")
if True or expensive_function():
    print("条件为真")
print("expensive_function没有被调用")

# 当需要执行所有函数时
print("\n当第一个条件不能确定结果时：")
if another_function() and expensive_function():
    print("两个函数都会执行")
else:
    print("第一个函数返回False，第二个函数不会执行")

print()

# 7. 实际应用：表单验证
print("=== 7. 表单验证示例 ===")
username = "john_doe"
password = "mypassword123"
email = "john@example.com"
age = 25
terms_accepted = True

# 用户名验证
username_valid = len(username) >= 3 and len(username) <= 20 and username.isalnum()

# 密码验证
password_valid = (len(password) >= 8 and 
                 any(c.isdigit() for c in password) and 
                 any(c.isalpha() for c in password))

# 邮箱验证（简单版）
email_valid = "@" in email and "." in email and len(email) >= 5

# 年龄验证
age_valid = 13 <= age <= 120

# 综合验证
if username_valid and password_valid and email_valid and age_valid and terms_accepted:
    print("表单验证通过！")
    print("用户注册成功")
else:
    print("表单验证失败：")
    if not username_valid:
        print("- 用户名格式不正确")
    if not password_valid:
        print("- 密码强度不够")
    if not email_valid:
        print("- 邮箱格式不正确")
    if not age_valid:
        print("- 年龄不在有效范围内")
    if not terms_accepted:
        print("- 必须同意服务条款")

print()

# 8. 游戏角色状态判断
print("=== 8. 游戏角色状态判断 ===")
player_level = 15
player_health = 80
player_mana = 50
has_weapon = True
has_armor = True
enemy_level = 12
enemy_count = 3

# 战斗可行性判断
can_fight = (player_health > 30 and 
            (has_weapon or player_level >= 10) and 
            player_level >= enemy_level - 5)

if can_fight:
    print("可以参与战斗")
    
    # 胜利概率判断
    if (player_level > enemy_level and has_weapon and has_armor) or player_level > enemy_level + 5:
        win_probability = "高"
    elif player_level >= enemy_level and (has_weapon or has_armor):
        win_probability = "中等"
    else:
        win_probability = "低"
    
    print(f"胜利概率：{win_probability}")
    
    # 特殊技能可用性
    if player_mana >= 30 and player_level >= 10:
        print("可以使用魔法技能")
    
    if has_weapon and player_level >= 15:
        print("可以使用武器特殊技能")
        
else:
    print("不建议参与战斗")
    if player_health <= 30:
        print("生命值过低，需要恢复")
    if not has_weapon and player_level < 10:
        print("需要武器或提升等级")
    if player_level < enemy_level - 5:
        print("等级差距过大")

print()

# 9. 逻辑运算符优先级演示
print("=== 9. 逻辑运算符优先级 ===")
a, b, c = True, False, True

# not > and > or
result1 = not a or b and c
print(f"not {a} or {b} and {c} = {result1}")
# 等价于：(not a) or (b and c)

result2 = (not a) or (b and c)
print(f"(not {a}) or ({b} and {c}) = {result2}")

# 使用括号改变优先级
result3 = not (a or b) and c
print(f"not ({a} or {b}) and {c} = {result3}")

# 建议：复杂表达式使用括号提高可读性
has_existing_loan = False
complex_condition = ((age >= 18 and income >= 30000) or 
                    (is_international and age >= 16)) and \
                   not has_existing_loan
print(f"\n复杂条件结果：{complex_condition}")

print()
print("=== 程序结束 ===")

# 练习题
print("\n=== 练习题 ===")
print("1. 编写程序判断一个年份是否为闰年（使用逻辑运算符）")
print("2. 编写程序验证用户输入的密码是否符合要求（长度、字符类型等）")
print("3. 编写程序判断学生是否可以毕业（多个条件组合）")
print("4. 编写程序实现简单的访问控制系统（角色、权限、时间等因素）")
print("5. 编写程序判断三角形的类型（等边、等腰、直角等，使用逻辑运算符）")