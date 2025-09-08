#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
if-else语句

本文件演示Python中if-else语句的用法，包括：
1. if-else语句的基本语法
2. 二选一的逻辑判断
3. 嵌套的if-else结构
4. 实际应用场景

学习目标：
- 掌握if-else语句的语法结构
- 理解二选一逻辑的应用场景
- 学会处理互斥条件
- 能够编写完整的条件分支程序
"""

# 1. 基本的if-else语句
print("=== 1. 基本if-else语句 ===")
age = 16
if age >= 18:
    print("你已经成年了，可以投票！")
else:
    print("你还未成年，不能投票。")
    print(f"还需要等待 {18 - age} 年")

print()

# 2. 数字比较的if-else
print("=== 2. 数字比较 ===")
number = 7
if number % 2 == 0:
    print(f"{number} 是偶数")
else:
    print(f"{number} 是奇数")

# 温度判断
temperature = 15
if temperature > 20:
    print("今天比较温暖")
else:
    print("今天比较凉爽")

print()

# 3. 字符串比较的if-else
print("=== 3. 字符串比较 ===")
username = "guest"
if username == "admin":
    print("管理员登录成功")
    print("拥有所有权限")
else:
    print("普通用户登录")
    print("权限受限")

# 密码验证
password = "wrong_password"
correct_password = "secret123"
if password == correct_password:
    print("密码正确，登录成功！")
else:
    print("密码错误，请重新输入！")

print()

# 4. 布尔值的if-else
print("=== 4. 布尔值判断 ===")
is_weekend = True
if is_weekend:
    print("今天是周末，可以休息！")
    print("享受悠闲时光")
else:
    print("今天是工作日，要上班！")
    print("努力工作")

# 会员状态判断
is_vip = False
if is_vip:
    print("VIP用户，享受特殊优惠！")
else:
    print("普通用户，欢迎升级VIP！")

print()

# 5. 列表和容器的if-else
print("=== 5. 列表和容器判断 ===")
shopping_cart = []
if shopping_cart:
    print(f"购物车中有 {len(shopping_cart)} 件商品")
    print("可以去结账了")
else:
    print("购物车是空的")
    print("请先添加商品")

# 非空列表示例
my_hobbies = ["读书", "游泳", "编程"]
if my_hobbies:
    print(f"我的爱好有：{', '.join(my_hobbies)}")
else:
    print("我还没有发现自己的爱好")

print()

# 6. 嵌套的if-else语句
print("=== 6. 嵌套if-else语句 ===")
score = 85
if score >= 60:
    print("考试及格了！")
    if score >= 90:
        print("成绩优秀！")
    else:
        print("成绩良好，继续努力！")
else:
    print("考试不及格")
    if score >= 40:
        print("接近及格线，再努力一点！")
    else:
        print("需要更加努力学习！")

print()

# 7. 实际应用示例
print("=== 7. 实际应用示例 ===")

# 示例1：银行账户余额检查
account_balance = 1500
withdraw_amount = 2000

if account_balance >= withdraw_amount:
    account_balance -= withdraw_amount
    print(f"取款成功！取款金额：{withdraw_amount}")
    print(f"余额：{account_balance}")
else:
    print("余额不足，无法取款！")
    print(f"当前余额：{account_balance}，需要取款：{withdraw_amount}")
    print(f"还差：{withdraw_amount - account_balance}")

print()

# 示例2：学生成绩评定
student_score = 78
if student_score >= 80:
    grade = "优秀"
    message = "恭喜你取得了优秀的成绩！"
else:
    grade = "良好"
    message = "成绩不错，继续加油！"

print(f"学生成绩：{student_score}")
print(f"评定等级：{grade}")
print(message)

print()

# 示例3：天气穿衣建议
outdoor_temperature = 8
if outdoor_temperature > 15:
    clothing_advice = "穿轻薄的衣服就可以了"
    accessories = "可以不用带外套"
else:
    clothing_advice = "建议穿厚一点的衣服"
    accessories = "记得带外套或围巾"

print(f"今天气温：{outdoor_temperature}°C")
print(f"穿衣建议：{clothing_advice}")
print(f"配饰建议：{accessories}")

print()

# 8. 使用函数的if-else
print("=== 8. 使用函数的if-else ===")

def check_password_strength(password):
    """检查密码强度"""
    if len(password) >= 8:
        return "密码强度：强"
    else:
        return "密码强度：弱"

# 测试密码强度
test_password1 = "123"
test_password2 = "mySecurePassword123"

result1 = check_password_strength(test_password1)
result2 = check_password_strength(test_password2)

print(f"密码 '{test_password1}' - {result1}")
print(f"密码 '{test_password2}' - {result2}")

print()

# 9. 条件表达式中的常见模式
print("=== 9. 常见模式 ===")

# 范围检查
user_age = 25
if 18 <= user_age <= 65:
    print("工作年龄段")
else:
    print("非工作年龄段")

# 多个条件的组合
username = "john"
user_status = "active"

if username and user_status == "active":
    print("用户可以登录")
else:
    print("用户无法登录")

print()
print("=== 程序结束 ===")

# 练习题
print("\n=== 练习题 ===")
print("1. 编写程序判断一个年份是否为闰年")
print("2. 编写程序根据分数判断是否及格（60分及格）")
print("3. 编写程序判断一个数字是正数还是负数（包括零）")
print("4. 编写程序检查用户名长度是否在3-20个字符之间")
print("5. 编写程序根据时间判断是上午还是下午")