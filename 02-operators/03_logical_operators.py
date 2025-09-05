#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
逻辑运算符学习教程

本文件演示Python中的逻辑运算符的使用方法和特性
包括：逻辑与(and)、逻辑或(or)、逻辑非(not)

学习目标：
1. 掌握三种逻辑运算符的使用
2. 理解逻辑运算符的短路求值特性
3. 学会逻辑运算符与布尔值的转换
4. 了解逻辑运算符的优先级和组合使用
"""

def main():
    print("="*50)
    print("Python 逻辑运算符学习教程")
    print("="*50)
    
    # 1. 基本逻辑运算符
    print("\n1. 基本逻辑运算符演示")
    print("-" * 30)
    
    # 布尔值的逻辑运算
    print("布尔值的逻辑运算：")
    print(f"True and True = {True and True}")
    print(f"True and False = {True and False}")
    print(f"False and True = {False and True}")
    print(f"False and False = {False and False}")
    
    print(f"\nTrue or True = {True or True}")
    print(f"True or False = {True or False}")
    print(f"False or True = {False or True}")
    print(f"False or False = {False or False}")
    
    print(f"\nnot True = {not True}")
    print(f"not False = {not False}")
    
    # 2. 数值的逻辑运算
    print("\n2. 数值的逻辑运算")
    print("-" * 30)
    
    # Python中的真值测试
    print("Python中的真值测试：")
    print(f"0 被视为: {bool(0)} (False)")
    print(f"非零数被视为: {bool(5)} (True)")
    print(f"空字符串被视为: {bool('')} (False)")
    print(f"非空字符串被视为: {bool('hello')} (True)")
    print(f"空列表被视为: {bool([])} (False)")
    print(f"非空列表被视为: {bool([1, 2, 3])} (True)")
    print(f"None 被视为: {bool(None)} (False)")
    
    # 数值逻辑运算示例
    a = 5
    b = 0
    c = 10
    
    print(f"\n数值逻辑运算示例：")
    print(f"a = {a}, b = {b}, c = {c}")
    print(f"a and b = {a and b} (返回 {b}，因为 b 为假值)")
    print(f"a and c = {a and c} (返回 {c}，因为都为真值)")
    print(f"a or b = {a or b} (返回 {a}，因为 a 为真值)")
    print(f"b or c = {b or c} (返回 {c}，因为 b 为假值)")
    
    # 3. 短路求值
    print("\n3. 短路求值演示")
    print("-" * 30)
    
    def true_func():
        print("  true_func() 被调用")
        return True
    
    def false_func():
        print("  false_func() 被调用")
        return False
    
    print("and 运算的短路求值：")
    print("False and true_func():")
    result1 = False and true_func()  # true_func() 不会被调用
    print(f"结果: {result1}")
    
    print("\nTrue and true_func():")
    result2 = True and true_func()   # true_func() 会被调用
    print(f"结果: {result2}")
    
    print("\nor 运算的短路求值：")
    print("True or false_func():")
    result3 = True or false_func()   # false_func() 不会被调用
    print(f"结果: {result3}")
    
    print("\nFalse or false_func():")
    result4 = False or false_func()  # false_func() 会被调用
    print(f"结果: {result4}")
    
    # 4. 复杂条件判断
    print("\n4. 复杂条件判断")
    print("-" * 30)
    
    age = 25
    has_license = True
    has_car = False
    
    print(f"年龄: {age}, 有驾照: {has_license}, 有车: {has_car}")
    
    # 可以开车的条件
    can_drive = age >= 18 and has_license
    print(f"可以开车: {can_drive}")
    
    # 可以自己开车出行的条件
    can_drive_alone = age >= 18 and has_license and has_car
    print(f"可以自己开车出行: {can_drive_alone}")
    
    # 可以出行的条件（开车或坐公交）
    can_travel = can_drive_alone or age >= 16
    print(f"可以出行: {can_travel}")
    
    # 5. 逻辑运算符的优先级
    print("\n5. 逻辑运算符的优先级")
    print("-" * 30)
    
    # not > and > or
    x = True
    y = False
    z = True
    
    print(f"x = {x}, y = {y}, z = {z}")
    
    # 不使用括号
    result1 = not x or y and z
    print(f"not x or y and z = {result1}")
    print(f"等价于: (not x) or (y and z) = {(not x) or (y and z)}")
    
    # 使用括号改变优先级
    result2 = not (x or y) and z
    print(f"not (x or y) and z = {result2}")
    
    result3 = not x or (y and z)
    print(f"not x or (y and z) = {result3}")
    
    # 6. 实际应用示例
    print("\n6. 实际应用示例")
    print("-" * 30)
    
    # 用户权限检查
    def check_permission(user_role, is_owner, is_admin):
        # 管理员或者是资源拥有者可以访问
        return is_admin or is_owner
    
    # 登录验证
    def validate_login(username, password, is_active):
        # 用户名和密码都正确，且账户激活
        return username and password and is_active
    
    # 年龄分组
    def categorize_age(age):
        if age < 0:
            return "无效年龄"
        elif age < 13:
            return "儿童"
        elif 13 <= age < 20:
            return "青少年"
        elif 20 <= age < 60:
            return "成年人"
        else:
            return "老年人"
    
    # 测试示例
    print("权限检查示例：")
    print(f"普通用户访问自己的资源: {check_permission('user', True, False)}")
    print(f"管理员访问任何资源: {check_permission('admin', False, True)}")
    print(f"普通用户访问他人资源: {check_permission('user', False, False)}")
    
    print("\n登录验证示例：")
    print(f"正确用户名密码，账户激活: {validate_login('admin', 'password123', True)}")
    print(f"正确用户名密码，账户未激活: {validate_login('admin', 'password123', False)}")
    print(f"错误密码: {validate_login('admin', '', True)}")
    
    # 7. 逻辑运算符与条件表达式
    print("\n7. 逻辑运算符与条件表达式")
    print("-" * 30)
    
    # 使用 and 和 or 进行默认值设置
    name = ""
    default_name = name or "匿名用户"
    print(f"用户名: '{name}' -> 显示名: '{default_name}'")
    
    name = "张三"
    default_name = name or "匿名用户"
    print(f"用户名: '{name}' -> 显示名: '{default_name}'")
    
    # 链式条件检查
    def get_discount(is_member, age, purchase_amount):
        # 会员折扣
        member_discount = is_member and 0.1 or 0
        # 老年人折扣
        senior_discount = age >= 65 and 0.05 or 0
        # 大额购买折扣
        bulk_discount = purchase_amount >= 1000 and 0.05 or 0
        
        total_discount = member_discount + senior_discount + bulk_discount
        return min(total_discount, 0.3)  # 最大折扣30%
    
    print("\n折扣计算示例：")
    discount1 = get_discount(True, 70, 1200)
    print(f"会员，70岁，购买1200元: 折扣 {discount1*100}%")
    
    discount2 = get_discount(False, 30, 500)
    print(f"非会员，30岁，购买500元: 折扣 {discount2*100}%")
    
    # 8. 德摩根定律
    print("\n8. 德摩根定律")
    print("-" * 30)
    
    a = True
    b = False
    
    print(f"a = {a}, b = {b}")
    print(f"not (a and b) = {not (a and b)}")
    print(f"(not a) or (not b) = {(not a) or (not b)}")
    print(f"两者相等: {not (a and b) == ((not a) or (not b))}")
    
    print(f"\nnot (a or b) = {not (a or b)}")
    print(f"(not a) and (not b) = {(not a) and (not b)}")
    print(f"两者相等: {not (a or b) == ((not a) and (not b))}")

def practice_exercises():
    """
    练习题部分
    """
    print("\n" + "="*50)
    print("练习题")
    print("="*50)
    
    print("\n请判断以下表达式的结果（True/False）：")
    print("1. True and False or True")
    print("2. not True or False and True")
    print("3. (5 > 3) and (2 < 4)")
    print("4. not (10 == 10)")
    print("5. [] or [1, 2, 3]")
    
    print("\n答案：")
    print(f"1. True and False or True = {True and False or True}")
    print(f"2. not True or False and True = {not True or False and True}")
    print(f"3. (5 > 3) and (2 < 4) = {(5 > 3) and (2 < 4)}")
    print(f"4. not (10 == 10) = {not (10 == 10)}")
    print(f"5. [] or [1, 2, 3] = {[] or [1, 2, 3]}")
    
    print("\n编程练习：")
    print("1. 编写函数判断一个年份是否为闰年")
    print("2. 验证用户输入的有效性")
    print("3. 实现简单的权限控制系统")
    
    # 示例解答
    print("\n示例解答：")
    
    # 1. 闰年判断
    def is_leap_year(year):
        # 能被4整除且不能被100整除，或者能被400整除
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    test_years = [2000, 2004, 1900, 2024]
    print("1. 闰年判断：")
    for year in test_years:
        result = is_leap_year(year)
        print(f"   {year} 年是闰年: {result}")
    
    # 2. 输入验证
    def validate_input(value, min_length=1, max_length=50, required=True):
        # 检查是否为空
        if required and not value:
            return False, "输入不能为空"
        
        # 检查长度
        if value and (len(value) < min_length or len(value) > max_length):
            return False, f"长度必须在 {min_length}-{max_length} 之间"
        
        return True, "输入有效"
    
    test_inputs = ["", "a", "hello", "a" * 60]
    print("\n2. 输入验证：")
    for inp in test_inputs:
        valid, message = validate_input(inp, 2, 20)
        print(f"   输入 '{inp}': {message}")
    
    # 3. 权限控制
    def check_access(user_role, resource_type, is_owner):
        # 管理员可以访问所有资源
        if user_role == "admin":
            return True
        
        # 普通用户只能访问自己的资源
        if user_role == "user" and is_owner:
            return True
        
        # 访客只能访问公共资源
        if user_role == "guest" and resource_type == "public":
            return True
        
        return False
    
    access_tests = [
        ("admin", "private", False),
        ("user", "private", True),
        ("user", "private", False),
        ("guest", "public", False),
        ("guest", "private", False)
    ]
    
    print("\n3. 权限控制：")
    for role, resource, owner in access_tests:
        access = check_access(role, resource, owner)
        print(f"   {role} 访问 {resource} 资源 (是否拥有: {owner}): {access}")

if __name__ == "__main__":
    main()
    practice_exercises()
    
    print("\n" + "="*50)
    print("学习小结")
    print("="*50)
    print("1. 逻辑运算符包括：and、or、not")
    print("2. Python中的短路求值可以提高效率")
    print("3. 任何值都可以进行真值测试")
    print("4. 逻辑运算符优先级：not > and > or")
    print("5. 德摩根定律在逻辑运算中很有用")
    print("6. 逻辑运算符在条件判断中应用广泛")