#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
运算符优先级和结合性学习教程

本文件演示Python中运算符的优先级和结合性
帮助理解复杂表达式的计算顺序

学习目标：
1. 掌握Python运算符的优先级顺序
2. 理解运算符的结合性（左结合、右结合）
3. 学会使用括号改变运算顺序
4. 避免因优先级导致的常见错误
"""

def main():
    print("="*50)
    print("Python 运算符优先级和结合性学习教程")
    print("="*50)
    
    # 1. 运算符优先级表（从高到低）
    print("\n1. Python运算符优先级表（从高到低）")
    print("-" * 40)
    
    precedence_table = [
        ("1", "()", "括号", "最高优先级"),
        ("2", "**", "幂运算", "右结合"),
        ("3", "+x, -x, ~x", "一元运算符", "正号、负号、按位取反"),
        ("4", "*, /, //, %", "乘除运算", "乘法、除法、整除、取模"),
        ("5", "+, -", "加减运算", "加法、减法"),
        ("6", "<<, >>", "位移运算", "左移、右移"),
        ("7", "&", "按位与", "位运算"),
        ("8", "^", "按位异或", "位运算"),
        ("9", "|", "按位或", "位运算"),
        ("10", "==, !=, <, >, <=, >=, is, is not, in, not in", "比较运算", "比较和成员运算"),
        ("11", "not", "逻辑非", "布尔运算"),
        ("12", "and", "逻辑与", "布尔运算"),
        ("13", "or", "逻辑或", "布尔运算"),
        ("14", "=, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, <<=, >>=", "赋值运算", "最低优先级")
    ]
    
    for level, operators, name, description in precedence_table:
        print(f"{level:2s}. {name:12s} {operators:50s} {description}")
    
    # 2. 基本优先级示例
    print("\n2. 基本优先级示例")
    print("-" * 30)
    
    # 算术运算优先级
    print("算术运算优先级：")
    expr1 = "2 + 3 * 4"
    result1 = 2 + 3 * 4
    print(f"{expr1} = {result1} (先乘后加)")
    
    expr2 = "(2 + 3) * 4"
    result2 = (2 + 3) * 4
    print(f"{expr2} = {result2} (括号改变优先级)")
    
    expr3 = "10 - 6 / 2"
    result3 = 10 - 6 / 2
    print(f"{expr3} = {result3} (先除后减)")
    
    expr4 = "(10 - 6) / 2"
    result4 = (10 - 6) / 2
    print(f"{expr4} = {result4} (括号改变优先级)")
    
    # 幂运算的右结合性
    print("\n幂运算的右结合性：")
    expr5 = "2 ** 3 ** 2"
    result5 = 2 ** 3 ** 2
    print(f"{expr5} = {result5} (等价于 2 ** (3 ** 2) = 2 ** 9)")
    
    expr6 = "(2 ** 3) ** 2"
    result6 = (2 ** 3) ** 2
    print(f"{expr6} = {result6} (括号改变结合性)")
    
    # 3. 比较运算符的链式使用
    print("\n3. 比较运算符的链式使用")
    print("-" * 30)
    
    x = 5
    print(f"x = {x}")
    
    # 链式比较
    result = 1 < x < 10
    print(f"1 < x < 10: {result} (等价于 (1 < x) and (x < 10))")
    
    result = 10 > x > 0
    print(f"10 > x > 0: {result} (等价于 (10 > x) and (x > 0))")
    
    result = x == 5 == 5
    print(f"x == 5 == 5: {result} (等价于 (x == 5) and (5 == 5))")
    
    # 注意：链式比较可能产生意外结果
    result = False == False in [False, True]
    print(f"False == False in [False, True]: {result}")
    print("解释: 等价于 (False == False) and (False in [False, True])")
    print(f"      = {False == False} and {False in [False, True]} = {result}")
    
    # 4. 逻辑运算符优先级
    print("\n4. 逻辑运算符优先级")
    print("-" * 30)
    
    # not > and > or
    print("逻辑运算符优先级 (not > and > or)：")
    
    expr = "not True and False or True"
    result = not True and False or True
    print(f"{expr} = {result}")
    print("计算过程: (not True) and False or True")
    print(f"        = {not True} and {False} or {True}")
    print(f"        = {not True and False} or {True}")
    print(f"        = {result}")
    
    expr = "True or False and False"
    result = True or False and False
    print(f"\n{expr} = {result}")
    print("计算过程: True or (False and False)")
    print(f"        = {True} or {False and False}")
    print(f"        = {result}")
    
    # 5. 位运算符优先级
    print("\n5. 位运算符优先级")
    print("-" * 30)
    
    # & > ^ > |
    print("位运算符优先级 (& > ^ > |)：")
    
    a, b, c = 12, 10, 6  # 1100, 1010, 0110
    print(f"a = {a} ({bin(a)[2:].zfill(4)})")
    print(f"b = {b} ({bin(b)[2:].zfill(4)})")
    print(f"c = {c} ({bin(c)[2:].zfill(4)})")
    
    expr = "a | b & c"
    result = a | b & c
    print(f"\n{expr} = {result}")
    print(f"计算过程: a | (b & c)")
    print(f"        = {a} | ({b} & {c})")
    print(f"        = {a} | {b & c}")
    print(f"        = {result}")
    
    expr = "a ^ b & c"
    result = a ^ b & c
    print(f"\n{expr} = {result}")
    print(f"计算过程: a ^ (b & c)")
    print(f"        = {a} ^ ({b} & {c})")
    print(f"        = {a} ^ {b & c}")
    print(f"        = {result}")
    
    # 6. 混合运算符优先级
    print("\n6. 混合运算符优先级")
    print("-" * 30)
    
    # 复杂表达式
    print("复杂表达式示例：")
    
    expr = "2 + 3 * 4 > 10 and not False"
    result = 2 + 3 * 4 > 10 and not False
    print(f"{expr} = {result}")
    print("计算过程:")
    print(f"  1. 3 * 4 = {3 * 4} (乘法优先级最高)")
    print(f"  2. 2 + {3 * 4} = {2 + 3 * 4} (加法)")
    print(f"  3. {2 + 3 * 4} > 10 = {2 + 3 * 4 > 10} (比较)")
    print(f"  4. not False = {not False} (逻辑非)")
    print(f"  5. {2 + 3 * 4 > 10} and {not False} = {result} (逻辑与)")
    
    expr = "5 << 1 + 1"
    result = 5 << 1 + 1
    print(f"\n{expr} = {result}")
    print("计算过程:")
    print(f"  1. 1 + 1 = {1 + 1} (加法优先于位移)")
    print(f"  2. 5 << {1 + 1} = {result} (左移)")
    
    # 7. 常见的优先级陷阱
    print("\n7. 常见的优先级陷阱")
    print("-" * 30)
    
    print("陷阱1: 位运算与比较运算")
    x = 5
    # 错误的写法
    # result = x & 1 == 1  # 这会被解释为 x & (1 == 1)
    result_wrong = x & 1 == 1
    result_correct = (x & 1) == 1
    
    print(f"x = {x}")
    print(f"x & 1 == 1: {result_wrong} (错误: 等价于 x & (1 == 1))")
    print(f"(x & 1) == 1: {result_correct} (正确: 先位运算再比较)")
    
    print("\n陷阱2: 逻辑运算与比较运算")
    a, b = 5, 10
    # 错误的理解
    result = a < b and b < 15
    print(f"a = {a}, b = {b}")
    print(f"a < b and b < 15: {result}")
    
    # 可能的误解
    # result_wrong = a < b and < 15  # 语法错误
    print("注意: 'a < b and < 15' 是语法错误")
    print("正确写法: 'a < b and b < 15' 或 'a < b < 15'")
    
    print("\n陷阱3: 赋值运算符的优先级")
    x = 10
    y = 5
    # z = x + y = 15  # 语法错误
    z = x + y
    print(f"x = {x}, y = {y}")
    print(f"z = x + y = {z}")
    print("注意: 'z = x + y = 15' 是语法错误")
    print("正确写法: 先计算表达式，再赋值")
    
    # 8. 使用括号提高可读性
    print("\n8. 使用括号提高可读性")
    print("-" * 30)
    
    print("即使了解优先级，使用括号也能提高代码可读性：")
    
    # 不清晰的表达式
    result1 = 2 + 3 * 4 ** 2 / 8 - 1
    print(f"不清晰: 2 + 3 * 4 ** 2 / 8 - 1 = {result1}")
    
    # 清晰的表达式
    result2 = 2 + ((3 * (4 ** 2)) / 8) - 1
    print(f"清晰:   2 + ((3 * (4 ** 2)) / 8) - 1 = {result2}")
    print(f"结果相同: {result1 == result2}")
    
    # 复杂条件判断
    age = 25
    income = 50000
    has_job = True
    
    # 不清晰
    eligible1 = age >= 18 and age <= 65 and income > 30000 or has_job and age > 21
    
    # 清晰
    eligible2 = ((age >= 18) and (age <= 65) and (income > 30000)) or (has_job and (age > 21))
    
    print(f"\n年龄: {age}, 收入: {income}, 有工作: {has_job}")
    print(f"不清晰条件: {eligible1}")
    print(f"清晰条件:   {eligible2}")
    print(f"结果相同: {eligible1 == eligible2}")
    
    # 9. 实际应用中的优先级
    print("\n9. 实际应用中的优先级")
    print("-" * 30)
    
    # 数学公式
    def quadratic_formula(a, b, c):
        """求解二次方程 ax² + bx + c = 0"""
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return None, None  # 无实数解
        
        sqrt_discriminant = discriminant ** 0.5
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant) / (2 * a)
        return x1, x2
    
    print("二次方程求解示例 (x² - 5x + 6 = 0):")
    x1, x2 = quadratic_formula(1, -5, 6)
    print(f"解: x1 = {x1}, x2 = {x2}")
    
    # 验证
    def verify_solution(a, b, c, x):
        return a * x ** 2 + b * x + c
    
    print(f"验证 x1: 1 * {x1}² + (-5) * {x1} + 6 = {verify_solution(1, -5, 6, x1)}")
    print(f"验证 x2: 1 * {x2}² + (-5) * {x2} + 6 = {verify_solution(1, -5, 6, x2)}")
    
    # 条件表达式
    def calculate_discount(price, is_member, quantity):
        """计算折扣价格"""
        # 会员折扣10%，批量购买(>=10)额外5%
        base_discount = 0.1 if is_member else 0.0
        quantity_discount = 0.05 if quantity >= 10 else 0.0
        total_discount = base_discount + quantity_discount
        
        # 确保折扣不超过20%
        total_discount = min(total_discount, 0.2)
        
        return price * (1 - total_discount)
    
    print("\n折扣计算示例：")
    test_cases = [
        (100, True, 5),   # 会员，少量购买
        (100, True, 15),  # 会员，批量购买
        (100, False, 15), # 非会员，批量购买
        (100, False, 5),  # 非会员，少量购买
    ]
    
    for price, is_member, quantity in test_cases:
        final_price = calculate_discount(price, is_member, quantity)
        member_str = "会员" if is_member else "非会员"
        print(f"原价¥{price}, {member_str}, {quantity}件 -> 最终价格¥{final_price:.2f}")

def practice_exercises():
    """
    练习题部分
    """
    print("\n" + "="*50)
    print("练习题")
    print("="*50)
    
    print("\n请计算以下表达式的结果（不使用Python计算器）：")
    expressions = [
        "2 + 3 * 4 ** 2",
        "10 - 6 / 2 + 1",
        "True or False and False",
        "not False and True or False",
        "5 & 3 | 1",
        "2 ** 3 ** 2",
        "1 < 2 == True",
        "3 + 4 > 5 and 2 * 3 == 6"
    ]
    
    print("表达式列表：")
    for i, expr in enumerate(expressions, 1):
        print(f"{i}. {expr}")
    
    print("\n答案和解析：")
    for i, expr in enumerate(expressions, 1):
        try:
            result = eval(expr)
            print(f"{i}. {expr} = {result}")
            
            # 提供解析
            if expr == "2 + 3 * 4 ** 2":
                print("   解析: 2 + 3 * (4 ** 2) = 2 + 3 * 16 = 2 + 48 = 50")
            elif expr == "10 - 6 / 2 + 1":
                print("   解析: 10 - (6 / 2) + 1 = 10 - 3 + 1 = 8")
            elif expr == "True or False and False":
                print("   解析: True or (False and False) = True or False = True")
            elif expr == "not False and True or False":
                print("   解析: (not False) and True or False = True and True or False = True")
            elif expr == "5 & 3 | 1":
                print("   解析: (5 & 3) | 1 = 1 | 1 = 1")
            elif expr == "2 ** 3 ** 2":
                print("   解析: 2 ** (3 ** 2) = 2 ** 9 = 512 (右结合)")
            elif expr == "1 < 2 == True":
                print("   解析: (1 < 2) and (2 == True) = True and False = False")
            elif expr == "3 + 4 > 5 and 2 * 3 == 6":
                print("   解析: (3 + 4 > 5) and (2 * 3 == 6) = (7 > 5) and (6 == 6) = True and True = True")
        except Exception as e:
            print(f"{i}. {expr} = 错误: {e}")
    
    print("\n编程练习：")
    print("1. 编写一个函数，正确计算复合利息")
    print("2. 实现一个表达式求值器（简化版）")
    print("3. 编写一个函数验证括号匹配")
    
    # 示例解答
    print("\n示例解答：")
    
    # 1. 复合利息计算
    def compound_interest(principal, rate, time, compound_frequency=1):
        """
        计算复合利息
        principal: 本金
        rate: 年利率（小数形式，如0.05表示5%）
        time: 时间（年）
        compound_frequency: 每年复利次数
        """
        # 使用正确的优先级：先除法，再加法，最后幂运算
        amount = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
        interest = amount - principal
        return amount, interest
    
    print("1. 复合利息计算：")
    principal = 10000  # 本金1万元
    rate = 0.05       # 年利率5%
    time = 10         # 10年
    
    # 不同复利频率的比较
    frequencies = [(1, "年"), (4, "季"), (12, "月"), (365, "日")]
    
    for freq, name in frequencies:
        amount, interest = compound_interest(principal, rate, time, freq)
        print(f"   {name}复利: 最终金额¥{amount:.2f}, 利息¥{interest:.2f}")
    
    # 2. 简化的表达式求值器
    def simple_evaluator(expression):
        """
        简化的表达式求值器（仅支持基本算术运算）
        注意：这是教学示例，实际应用中应使用更安全的方法
        """
        # 移除空格
        expr = expression.replace(" ", "")
        
        # 检查是否只包含允许的字符
        allowed_chars = set('0123456789+-*/().')
        if not all(c in allowed_chars for c in expr):
            return "错误: 包含不允许的字符"
        
        # 检查括号匹配
        if not is_balanced_parentheses(expr):
            return "错误: 括号不匹配"
        
        try:
            # 注意：eval在实际应用中有安全风险，这里仅作教学演示
            result = eval(expr)
            return result
        except Exception as e:
            return f"错误: {e}"
    
    def is_balanced_parentheses(expression):
        """检查括号是否匹配"""
        count = 0
        for char in expression:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:  # 右括号多于左括号
                    return False
        return count == 0  # 左右括号数量相等
    
    print("\n2. 表达式求值器：")
    test_expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "10 / (2 + 3)",
        "2 ** 3 + 1",
        "((1 + 2) * 3) / 2",
        "2 + 3 * (4 - 1",  # 括号不匹配
        "2 + abc",         # 包含字母
    ]
    
    for expr in test_expressions:
        result = simple_evaluator(expr)
        print(f"   '{expr}' = {result}")
    
    # 3. 括号匹配验证
    def validate_parentheses_detailed(expression):
        """
        详细的括号匹配验证
        返回是否匹配以及详细信息
        """
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}
        
        for i, char in enumerate(expression):
            if char in pairs:  # 左括号
                stack.append((char, i))
            elif char in pairs.values():  # 右括号
                if not stack:
                    return False, f"位置{i}: 多余的右括号 '{char}'"
                
                left_char, left_pos = stack.pop()
                if pairs[left_char] != char:
                    return False, f"位置{i}: 括号类型不匹配 '{left_char}' 和 '{char}'"
        
        if stack:
            left_char, left_pos = stack[-1]
            return False, f"位置{left_pos}: 未匹配的左括号 '{left_char}'"
        
        return True, "括号匹配正确"
    
    print("\n3. 括号匹配验证：")
    test_brackets = [
        "(1 + 2) * 3",
        "[(1 + 2) * 3]",
        "{[(1 + 2) * 3]}",
        "(1 + 2] * 3",
        "((1 + 2) * 3",
        "(1 + 2)) * 3",
        "",
        "no brackets here"
    ]
    
    for expr in test_brackets:
        is_valid, message = validate_parentheses_detailed(expr)
        status = "✓" if is_valid else "✗"
        print(f"   {status} '{expr}': {message}")

if __name__ == "__main__":
    main()
    practice_exercises()
    
    print("\n" + "="*50)
    print("学习小结")
    print("="*50)
    print("1. 运算符优先级决定了表达式的计算顺序")
    print("2. 括号具有最高优先级，可以改变计算顺序")
    print("3. 幂运算是右结合的，其他大多数运算符是左结合的")
    print("4. 比较运算符可以链式使用")
    print("5. 位运算符优先级低于算术运算符，高于比较运算符")
    print("6. 逻辑运算符优先级：not > and > or")
    print("7. 使用括号可以提高代码可读性，即使不改变优先级")
    print("8. 了解优先级有助于避免常见的编程错误")