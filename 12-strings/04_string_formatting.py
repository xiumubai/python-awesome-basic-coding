#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字符串格式化

本文件演示Python中字符串格式化的各种方法：
1. 旧式字符串格式化（%格式化）
2. str.format()方法
3. f-string（格式化字符串字面量）
4. 数字格式化
5. 日期时间格式化
6. 高级格式化技巧

作者：Python学习教程
日期：2024年
"""

import datetime
import math

def demonstrate_percent_formatting():
    """演示旧式%格式化"""
    print("=== 旧式%格式化 ===")
    
    # 基本用法
    name = "Alice"
    age = 25
    
    # 字符串和整数
    message1 = "Hello, %s! You are %d years old." % (name, age)
    print(f"基本格式化: {message1}")
    
    # 不同的格式说明符
    print("\n格式说明符示例:")
    number = 42
    float_num = 3.14159
    
    print("%d (整数): %d" % (number, number))
    print("%f (浮点数): %f" % (float_num, float_num))
    print("%.2f (保留2位小数): %.2f" % (float_num, float_num))
    print("%e (科学计数法): %e" % (float_num, float_num))
    print("%x (十六进制): %x" % (number, number))
    print("%o (八进制): %o" % (number, number))
    
    # 字典格式化
    person = {'name': 'Bob', 'age': 30, 'city': 'New York'}
    formatted = "%(name)s is %(age)d years old and lives in %(city)s." % person
    print(f"\n字典格式化: {formatted}")
    
    # 格式化控制
    print("\n格式化控制:")
    print("%10s" % "right")  # 右对齐，宽度10
    print("%-10s" % "left")   # 左对齐，宽度10
    print("%010d" % 42)      # 用0填充，宽度10

def demonstrate_str_format():
    """演示str.format()方法"""
    print("\n=== str.format()方法 ===")
    
    # 基本用法
    name = "Charlie"
    age = 35
    
    # 位置参数
    message1 = "Hello, {}! You are {} years old.".format(name, age)
    print(f"位置参数: {message1}")
    
    # 索引参数
    message2 = "Hello, {0}! You are {1} years old. Nice to meet you, {0}!".format(name, age)
    print(f"索引参数: {message2}")
    
    # 关键字参数
    message3 = "Hello, {name}! You are {age} years old.".format(name=name, age=age)
    print(f"关键字参数: {message3}")
    
    # 混合使用
    message4 = "Hello, {0}! You are {age} years old.".format(name, age=age)
    print(f"混合参数: {message4}")
    
    # 格式化规范
    print("\n格式化规范:")
    number = 1234.5678
    
    print(f"默认: {number}")
    print("保留2位小数: {:.2f}".format(number))
    print("科学计数法: {:.2e}".format(number))
    print("百分比: {:.1%}".format(0.1234))
    print("千位分隔符: {:,}".format(1234567))
    
    # 对齐和填充
    text = "Python"
    print("\n对齐和填充:")
    print("左对齐: '{:<20}'".format(text))
    print("右对齐: '{:>20}'".format(text))
    print("居中: '{:^20}'".format(text))
    print("填充字符: '{:*^20}'".format(text))
    
    # 数字格式化
    print("\n数字格式化:")
    num = 42
    print("二进制: {:b}".format(num))
    print("八进制: {:o}".format(num))
    print("十六进制: {:x}".format(num))
    print("十六进制(大写): {:X}".format(num))

def demonstrate_f_strings():
    """演示f-string格式化"""
    print("\n=== f-string格式化 ===")
    
    # 基本用法
    name = "David"
    age = 28
    
    message = f"Hello, {name}! You are {age} years old."
    print(f"基本f-string: {message}")
    
    # 表达式计算
    x = 10
    y = 20
    print(f"计算结果: {x} + {y} = {x + y}")
    print(f"平方: {x}² = {x**2}")
    
    # 方法调用
    text = "python programming"
    print(f"标题格式: {text.title()}")
    print(f"大写: {text.upper()}")
    
    # 格式化规范
    pi = math.pi
    print(f"\n数字格式化:")
    print(f"π = {pi}")
    print(f"π (2位小数) = {pi:.2f}")
    print(f"π (科学计数法) = {pi:.2e}")
    
    # 对齐和填充
    word = "Hello"
    print(f"\n对齐示例:")
    print(f"左对齐: '{word:<15}'")
    print(f"右对齐: '{word:>15}'")
    print(f"居中: '{word:^15}'")
    print(f"填充: '{word:=^15}'")
    
    # 千位分隔符
    big_number = 1234567890
    print(f"\n大数字: {big_number:,}")
    print(f"货币格式: ${big_number:,.2f}")
    
    # 百分比
    ratio = 0.8567
    print(f"\n百分比: {ratio:.1%}")
    print(f"百分比(2位): {ratio:.2%}")

def demonstrate_number_formatting():
    """演示数字格式化的详细用法"""
    print("\n=== 数字格式化详解 ===")
    
    # 整数格式化
    num = 42
    print("整数格式化:")
    print(f"默认: {num}")
    print(f"宽度10: {num:10}")
    print(f"左对齐: {num:<10}")
    print(f"右对齐: {num:>10}")
    print(f"居中: {num:^10}")
    print(f"零填充: {num:010}")
    print(f"正号显示: {num:+}")
    print(f"空格占位: {num: }")
    
    # 浮点数格式化
    float_num = 123.456789
    print("\n浮点数格式化:")
    print(f"默认: {float_num}")
    print(f"2位小数: {float_num:.2f}")
    print(f"4位小数: {float_num:.4f}")
    print(f"科学计数法: {float_num:.2e}")
    print(f"一般格式: {float_num:.3g}")
    print(f"宽度15,2位小数: {float_num:15.2f}")
    print(f"零填充: {float_num:015.2f}")
    
    # 负数格式化
    negative = -123.45
    print("\n负数格式化:")
    print(f"默认: {negative}")
    print(f"正号显示: {negative:+.2f}")
    print(f"空格占位: {negative: .2f}")
    # 注意：Python不支持括号表示负数的格式化
    # print(f"括号表示负数: {negative:(.2f})")
    print(f"绝对值: {abs(negative):.2f}")
    
    # 进制转换
    number = 255
    print("\n进制转换:")
    print(f"十进制: {number}")
    print(f"二进制: {number:b}")
    print(f"八进制: {number:o}")
    print(f"十六进制: {number:x}")
    print(f"十六进制(大写): {number:X}")
    print(f"带前缀二进制: {number:#b}")
    print(f"带前缀十六进制: {number:#x}")

def demonstrate_datetime_formatting():
    """演示日期时间格式化"""
    print("\n=== 日期时间格式化 ===")
    
    now = datetime.datetime.now()
    date_only = datetime.date.today()
    time_only = datetime.time(14, 30, 45)
    
    print(f"当前时间: {now}")
    
    # 使用f-string格式化日期时间
    print("\nf-string日期格式化:")
    print(f"年-月-日: {now:%Y-%m-%d}")
    print(f"时:分:秒: {now:%H:%M:%S}")
    print(f"完整格式: {now:%Y-%m-%d %H:%M:%S}")
    print(f"中文格式: {now:%Y年%m月%d日 %H时%M分%S秒}")
    print(f"星期几: {now:%A}")
    print(f"月份名: {now:%B}")
    
    # 使用format方法
    print("\nformat方法日期格式化:")
    print("ISO格式: {:%Y-%m-%d}".format(date_only))
    print("美式格式: {:%m/%d/%Y}".format(date_only))
    print("欧式格式: {:%d/%m/%Y}".format(date_only))
    
    # 时间格式化
    print("\n时间格式化:")
    print(f"24小时制: {time_only:%H:%M:%S}")
    print(f"12小时制: {time_only:%I:%M:%S %p}")
    
    # 自定义日期时间格式
    custom_formats = [
        "%Y-%m-%d",           # 2024-01-15
        "%d/%m/%Y",           # 15/01/2024
        "%B %d, %Y",          # January 15, 2024
        "%A, %B %d, %Y",      # Monday, January 15, 2024
        "%Y年%m月%d日",        # 2024年01月15日
        "%H:%M:%S",           # 14:30:45
        "%I:%M %p",           # 02:30 PM
    ]
    
    print("\n各种日期时间格式:")
    for fmt in custom_formats:
        formatted = now.strftime(fmt)
        print(f"{fmt:<20} -> {formatted}")

def demonstrate_advanced_formatting():
    """演示高级格式化技巧"""
    print("\n=== 高级格式化技巧 ===")
    
    # 动态格式化
    width = 15
    precision = 3
    number = 123.456789
    
    # 使用变量控制格式
    print(f"动态宽度和精度: {number:{width}.{precision}f}")
    
    # 嵌套格式化
    data = [1.23, 45.678, 9.0]
    print("\n嵌套格式化:")
    for i, value in enumerate(data):
        print(f"Item {i+1}: {value:8.2f}")
    
    # 条件格式化
    scores = [85, 92, 78, 96, 73]
    print("\n条件格式化:")
    for i, score in enumerate(scores, 1):
        grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
        print(f"Student {i}: {score:3d} ({grade})")
    
    # 表格格式化
    print("\n表格格式化:")
    students = [
        ("Alice", 85, 92, 88),
        ("Bob", 78, 85, 82),
        ("Charlie", 92, 88, 95),
        ("Diana", 88, 94, 91)
    ]
    
    # 表头
    print(f"{'Name':<10} {'Math':>6} {'Science':>8} {'English':>8} {'Average':>8}")
    print("-" * 50)
    
    # 数据行
    for name, math, science, english in students:
        average = (math + science + english) / 3
        print(f"{name:<10} {math:>6} {science:>8} {english:>8} {average:>8.1f}")
    
    # 字典格式化
    person = {
        'name': 'John Doe',
        'age': 30,
        'salary': 50000.50,
        'department': 'Engineering'
    }
    
    print("\n字典格式化:")
    template = "Name: {name}, Age: {age}, Salary: ${salary:,.2f}, Dept: {department}"
    print(template.format(**person))
    
    # 使用f-string和字典
    print(f"f-string字典: {person['name']} earns ${person['salary']:,.2f}")

def demonstrate_string_templates():
    """演示字符串模板的使用"""
    print("\n=== 字符串模板 ===")
    
    from string import Template
    
    # 基本模板使用
    template = Template("Hello, $name! Welcome to $place.")
    result = template.substitute(name="Alice", place="Python World")
    print(f"模板结果: {result}")
    
    # 使用字典
    data = {'name': 'Bob', 'place': 'Programming Land'}
    result2 = template.substitute(data)
    print(f"字典模板: {result2}")
    
    # 安全替换（缺少变量时不报错）
    incomplete_data = {'name': 'Charlie'}
    try:
        result3 = template.substitute(incomplete_data)
    except KeyError as e:
        print(f"缺少变量错误: {e}")
        result3 = template.safe_substitute(incomplete_data)
        print(f"安全替换: {result3}")
    
    # 复杂模板
    email_template = Template("""
亲爱的 $name，

感谢您购买我们的产品！
订单号：$order_id
总金额：$$amount
预计送达：$delivery_date

祝好！
$company_name
""")
    
    email_data = {
        'name': '张三',
        'order_id': 'ORD-12345',
        'amount': '299.99',
        'delivery_date': '2024-01-20',
        'company_name': 'Python商城'
    }
    
    email = email_template.substitute(email_data)
    print(f"\n邮件模板:\n{email}")

def main():
    """主函数，演示所有字符串格式化方法"""
    print("Python字符串格式化")
    print("=" * 50)
    
    demonstrate_percent_formatting()
    demonstrate_str_format()
    demonstrate_f_strings()
    demonstrate_number_formatting()
    demonstrate_datetime_formatting()
    demonstrate_advanced_formatting()
    demonstrate_string_templates()
    
    print("\n=== 总结 ===")
    print("1. %格式化：旧式方法，兼容性好")
    print("2. str.format()：功能强大，可读性好")
    print("3. f-string：Python 3.6+，简洁高效")
    print("4. 数字格式化：支持各种数字显示格式")
    print("5. 日期时间格式化：使用strftime格式")
    print("6. 高级技巧：动态格式、条件格式、表格格式")
    print("7. 字符串模板：适合复杂文本生成")

if __name__ == "__main__":
    main()