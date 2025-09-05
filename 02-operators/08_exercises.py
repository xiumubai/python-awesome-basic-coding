#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
02-operators 模块 - 综合练习题

本文件包含运算符的综合练习题，涵盖所有类型的运算符应用。
通过这些练习，你将能够熟练掌握Python中各种运算符的使用。

练习内容：
1. 基础运算练习
2. 条件判断练习
3. 逻辑运算练习
4. 位运算应用
5. 综合应用题
6. 挑战题
"""

print("=" * 60)
print("Python 运算符 - 综合练习题")
print("=" * 60)

# ============================================================================
# 练习1：基础运算练习
# ============================================================================
print("\n练习1：基础运算练习")
print("-" * 30)

# 题目1：计算器函数
def calculator(a, b, operator):
    """
    实现一个简单的计算器函数
    支持 +, -, *, /, //, %, ** 运算
    """
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b if b != 0 else "除数不能为0"
    elif operator == '//':
        return a // b if b != 0 else "除数不能为0"
    elif operator == '%':
        return a % b if b != 0 else "除数不能为0"
    elif operator == '**':
        return a ** b
    else:
        return "不支持的运算符"

# 测试计算器函数
print("计算器测试：")
test_cases = [
    (10, 3, '+'),
    (10, 3, '-'),
    (10, 3, '*'),
    (10, 3, '/'),
    (10, 3, '//'),
    (10, 3, '%'),
    (2, 3, '**')
]

for a, b, op in test_cases:
    result = calculator(a, b, op)
    print(f"{a} {op} {b} = {result}")

# 题目2：温度转换
def temperature_converter(temp, from_unit, to_unit):
    """
    温度单位转换函数
    支持摄氏度(C)、华氏度(F)、开尔文(K)之间的转换
    """
    # 先转换为摄氏度
    if from_unit == 'F':
        celsius = (temp - 32) * 5 / 9
    elif from_unit == 'K':
        celsius = temp - 273.15
    else:  # from_unit == 'C'
        celsius = temp
    
    # 再从摄氏度转换为目标单位
    if to_unit == 'F':
        return celsius * 9 / 5 + 32
    elif to_unit == 'K':
        return celsius + 273.15
    else:  # to_unit == 'C'
        return celsius

print("\n温度转换测试：")
print(f"100°C = {temperature_converter(100, 'C', 'F'):.1f}°F")
print(f"32°F = {temperature_converter(32, 'F', 'C'):.1f}°C")
print(f"0°C = {temperature_converter(0, 'C', 'K'):.1f}K")

# ============================================================================
# 练习2：条件判断练习
# ============================================================================
print("\n\n练习2：条件判断练习")
print("-" * 30)

# 题目3：成绩等级判定
def grade_classifier(score):
    """
    根据分数判定成绩等级
    90-100: A
    80-89: B
    70-79: C
    60-69: D
    0-59: F
    """
    if not (0 <= score <= 100):
        return "无效分数"
    
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

print("成绩等级判定测试：")
test_scores = [95, 85, 75, 65, 55, 105, -10]
for score in test_scores:
    grade = grade_classifier(score)
    print(f"分数 {score}: 等级 {grade}")

# 题目4：年份判断
def is_leap_year(year):
    """
    判断是否为闰年
    闰年规则：
    1. 能被4整除但不能被100整除
    2. 或者能被400整除
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print("\n闰年判断测试：")
test_years = [2000, 2004, 1900, 2020, 2021, 2024]
for year in test_years:
    is_leap = is_leap_year(year)
    print(f"{year}年: {'是' if is_leap else '不是'}闰年")

# ============================================================================
# 练习3：逻辑运算练习
# ============================================================================
print("\n\n练习3：逻辑运算练习")
print("-" * 30)

# 题目5：用户权限检查
def check_access(user_role, resource_level, is_authenticated):
    """
    检查用户是否有权限访问资源
    """
    # 必须先登录
    if not is_authenticated:
        return False, "用户未登录"
    
    # 管理员可以访问所有资源
    if user_role == 'admin':
        return True, "管理员权限"
    
    # 普通用户只能访问公开资源
    if user_role == 'user' and resource_level == 'public':
        return True, "用户权限"
    
    # VIP用户可以访问公开和VIP资源
    if user_role == 'vip' and resource_level in ['public', 'vip']:
        return True, "VIP权限"
    
    return False, "权限不足"

print("权限检查测试：")
access_tests = [
    ('admin', 'private', True),
    ('user', 'public', True),
    ('user', 'private', True),
    ('vip', 'vip', True),
    ('user', 'public', False),
]

for role, level, auth in access_tests:
    can_access, reason = check_access(role, level, auth)
    status = "允许" if can_access else "拒绝"
    print(f"角色:{role}, 资源:{level}, 登录:{auth} -> {status} ({reason})")

# 题目6：数字范围检查
def number_range_check(num):
    """
    检查数字所在的范围
    """
    conditions = [
        (num > 0 and num <= 10, "正小数 (0-10]"),
        (num > 10 and num <= 100, "中等数 (10-100]"),
        (num > 100, "大数 (>100)"),
        (num == 0, "零"),
        (num < 0, "负数")
    ]
    
    for condition, description in conditions:
        if condition:
            return description
    
    return "未知范围"

print("\n数字范围检查测试：")
test_numbers = [5, 50, 150, 0, -10, 10, 100]
for num in test_numbers:
    range_desc = number_range_check(num)
    print(f"数字 {num}: {range_desc}")

# ============================================================================
# 练习4：位运算应用
# ============================================================================
print("\n\n练习4：位运算应用")
print("-" * 30)

# 题目7：权限系统（使用位运算）
class PermissionSystem:
    """
    使用位运算实现的权限系统
    """
    # 权限常量
    READ = 1      # 0001
    WRITE = 2     # 0010
    EXECUTE = 4   # 0100
    DELETE = 8    # 1000
    
    def __init__(self):
        self.user_permissions = {}
    
    def grant_permission(self, user, permission):
        """授予权限"""
        if user not in self.user_permissions:
            self.user_permissions[user] = 0
        self.user_permissions[user] |= permission
    
    def revoke_permission(self, user, permission):
        """撤销权限"""
        if user in self.user_permissions:
            self.user_permissions[user] &= ~permission
    
    def has_permission(self, user, permission):
        """检查是否有权限"""
        if user not in self.user_permissions:
            return False
        return (self.user_permissions[user] & permission) == permission
    
    def get_permissions(self, user):
        """获取用户所有权限"""
        if user not in self.user_permissions:
            return []
        
        permissions = []
        user_perm = self.user_permissions[user]
        
        if user_perm & self.READ:
            permissions.append('READ')
        if user_perm & self.WRITE:
            permissions.append('WRITE')
        if user_perm & self.EXECUTE:
            permissions.append('EXECUTE')
        if user_perm & self.DELETE:
            permissions.append('DELETE')
        
        return permissions

# 测试权限系统
print("权限系统测试：")
perm_sys = PermissionSystem()

# 授予权限
perm_sys.grant_permission('alice', PermissionSystem.READ)
perm_sys.grant_permission('alice', PermissionSystem.WRITE)
perm_sys.grant_permission('bob', PermissionSystem.READ | PermissionSystem.EXECUTE)

print(f"Alice的权限: {perm_sys.get_permissions('alice')}")
print(f"Bob的权限: {perm_sys.get_permissions('bob')}")

# 检查权限
print(f"Alice有读权限: {perm_sys.has_permission('alice', PermissionSystem.READ)}")
print(f"Alice有删除权限: {perm_sys.has_permission('alice', PermissionSystem.DELETE)}")
print(f"Bob有执行权限: {perm_sys.has_permission('bob', PermissionSystem.EXECUTE)}")

# 题目8：数字操作（位运算技巧）
def bit_operations_demo(num):
    """
    演示常用的位运算技巧
    """
    print(f"\n数字 {num} 的位运算操作：")
    print(f"二进制表示: {bin(num)}")
    
    # 检查是否为偶数
    is_even = (num & 1) == 0
    print(f"是否为偶数: {is_even}")
    
    # 乘以2（左移1位）
    multiply_by_2 = num << 1
    print(f"乘以2: {multiply_by_2}")
    
    # 除以2（右移1位）
    divide_by_2 = num >> 1
    print(f"除以2: {divide_by_2}")
    
    # 获取最低位
    lowest_bit = num & 1
    print(f"最低位: {lowest_bit}")
    
    # 清除最低位的1
    clear_lowest_1 = num & (num - 1)
    print(f"清除最低位的1: {clear_lowest_1}")
    
    # 获取最低位的1
    get_lowest_1 = num & (-num)
    print(f"获取最低位的1: {get_lowest_1}")

# 测试位运算技巧
for test_num in [12, 7, 16]:
    bit_operations_demo(test_num)

# ============================================================================
# 练习5：综合应用题
# ============================================================================
print("\n\n练习5：综合应用题")
print("-" * 30)

# 题目9：购物车计算器
class ShoppingCart:
    """
    购物车类，演示多种运算符的综合应用
    """
    def __init__(self):
        self.items = []  # 商品列表
        self.discount_rate = 0  # 折扣率
        self.tax_rate = 0.1  # 税率10%
    
    def add_item(self, name, price, quantity=1):
        """添加商品"""
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })
    
    def remove_item(self, name):
        """移除商品"""
        self.items = [item for item in self.items if item['name'] != name]
    
    def set_discount(self, rate):
        """设置折扣率"""
        self.discount_rate = rate if 0 <= rate <= 1 else 0
    
    def calculate_subtotal(self):
        """计算小计"""
        return sum(item['price'] * item['quantity'] for item in self.items)
    
    def calculate_discount(self):
        """计算折扣金额"""
        return self.calculate_subtotal() * self.discount_rate
    
    def calculate_tax(self):
        """计算税额"""
        discounted_amount = self.calculate_subtotal() - self.calculate_discount()
        return discounted_amount * self.tax_rate
    
    def calculate_total(self):
        """计算总金额"""
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        tax = self.calculate_tax()
        return subtotal - discount + tax
    
    def get_summary(self):
        """获取购物车摘要"""
        if not self.items:
            return "购物车为空"
        
        summary = "购物车摘要:\n"
        summary += "-" * 40 + "\n"
        
        for item in self.items:
            total_price = item['price'] * item['quantity']
            summary += f"{item['name']}: ${item['price']:.2f} x {item['quantity']} = ${total_price:.2f}\n"
        
        summary += "-" * 40 + "\n"
        summary += f"小计: ${self.calculate_subtotal():.2f}\n"
        
        if self.discount_rate > 0:
            summary += f"折扣 ({self.discount_rate*100:.0f}%): -${self.calculate_discount():.2f}\n"
        
        summary += f"税费 ({self.tax_rate*100:.0f}%): ${self.calculate_tax():.2f}\n"
        summary += f"总计: ${self.calculate_total():.2f}\n"
        
        return summary

# 测试购物车
print("购物车测试：")
cart = ShoppingCart()

# 添加商品
cart.add_item("苹果", 2.50, 3)
cart.add_item("香蕉", 1.20, 5)
cart.add_item("牛奶", 3.80, 2)

# 设置折扣
cart.set_discount(0.1)  # 10%折扣

print(cart.get_summary())

# 题目10：数学表达式求值器
def evaluate_expression(expression):
    """
    简单的数学表达式求值器
    支持 +, -, *, /, (, ) 运算符
    注意：这是一个简化版本，实际应用中应使用更安全的方法
    """
    try:
        # 移除空格
        expression = expression.replace(' ', '')
        
        # 检查表达式是否只包含允许的字符
        allowed_chars = set('0123456789+-*/().')
        if not all(c in allowed_chars for c in expression):
            return "表达式包含非法字符"
        
        # 使用eval计算（注意：在实际应用中应避免使用eval）
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "除零错误"
    except Exception as e:
        return f"表达式错误: {str(e)}"

print("\n表达式求值测试：")
expressions = [
    "2 + 3 * 4",
    "(2 + 3) * 4",
    "10 / 2 + 3",
    "2 ** 3 + 1",
    "10 / 0",
    "2 + 3 * (4 - 1)"
]

for expr in expressions:
    result = evaluate_expression(expr)
    print(f"{expr} = {result}")

# ============================================================================
# 练习6：挑战题
# ============================================================================
print("\n\n练习6：挑战题")
print("-" * 30)

# 题目11：复数运算器
class ComplexCalculator:
    """
    复数运算器，演示运算符重载的概念
    """
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"
    
    def add(self, other):
        """复数加法"""
        return ComplexCalculator(
            self.real + other.real,
            self.imag + other.imag
        )
    
    def subtract(self, other):
        """复数减法"""
        return ComplexCalculator(
            self.real - other.real,
            self.imag - other.imag
        )
    
    def multiply(self, other):
        """复数乘法"""
        # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexCalculator(real_part, imag_part)
    
    def magnitude(self):
        """计算复数的模"""
        return (self.real ** 2 + self.imag ** 2) ** 0.5

print("复数运算测试：")
c1 = ComplexCalculator(3, 4)
c2 = ComplexCalculator(1, -2)

print(f"c1 = {c1}")
print(f"c2 = {c2}")
print(f"c1 + c2 = {c1.add(c2)}")
print(f"c1 - c2 = {c1.subtract(c2)}")
print(f"c1 * c2 = {c1.multiply(c2)}")
print(f"|c1| = {c1.magnitude():.2f}")
print(f"|c2| = {c2.magnitude():.2f}")

# 题目12：位运算实现加法
def add_without_plus(a, b):
    """
    不使用+运算符实现加法（使用位运算）
    """
    while b != 0:
        # 计算进位
        carry = a & b
        
        # 计算不带进位的和
        a = a ^ b
        
        # 进位左移一位
        b = carry << 1
    
    return a

print("\n位运算加法测试：")
test_pairs = [(5, 3), (15, 7), (100, 25), (-5, 3)]
for x, y in test_pairs:
    result = add_without_plus(x, y)
    print(f"{x} + {y} = {result} (验证: {x + y})")

# ============================================================================
# 总结和思考题
# ============================================================================
print("\n\n" + "=" * 60)
print("练习总结")
print("=" * 60)

print("""
通过以上练习，你应该掌握了：

1. 算术运算符的基本使用和应用场景
2. 比较运算符在条件判断中的作用
3. 逻辑运算符的短路求值特性
4. 赋值运算符的便捷性
5. 位运算符在系统编程中的应用
6. 成员运算符和身份运算符的区别
7. 运算符优先级的重要性
8. 各种运算符的综合应用

思考题：
1. 为什么位运算在某些场景下比普通运算更高效？
2. 什么时候应该使用 is 而不是 == ？
3. 如何利用运算符优先级写出更简洁的代码？
4. 在实际项目中，哪些运算符使用频率最高？
5. 如何避免运算符优先级导致的逻辑错误？

挑战练习：
1. 实现一个支持复杂表达式的计算器
2. 使用位运算实现一个简单的加密算法
3. 设计一个权限管理系统，充分利用位运算的优势
4. 编写一个函数，判断两个浮点数是否"相等"（考虑精度问题）
5. 实现一个自定义类，重载所有比较运算符
""")

print("\n恭喜你完成了所有运算符练习！")
print("继续加油，探索Python的更多特性！")