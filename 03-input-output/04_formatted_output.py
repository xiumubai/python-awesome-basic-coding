#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
格式化输出 - f-string, format(), %格式化

学习目标：
1. 掌握f-string格式化字符串的使用
2. 学会使用.format()方法进行格式化
3. 了解%格式化的基本用法
4. 掌握各种格式化选项和技巧

作者：Python基础教程
日期：2024年
"""

import datetime
import math

# ============================================================================
# 1. f-string格式化（推荐方式）
# ============================================================================

print("=" * 50)
print("1. f-string格式化（Python 3.6+）")
print("=" * 50)

# f-string是最现代、最推荐的字符串格式化方式
name = "张三"
age = 25
score = 85.67

print("\n--- f-string基础用法 ---")
print(f"姓名：{name}")
print(f"年龄：{age}岁")
print(f"分数：{score}分")
print(f"完整信息：{name}今年{age}岁，考试得了{score}分")

# 在f-string中使用表达式
print("\n--- f-string中的表达式 ---")
print(f"明年年龄：{age + 1}岁")
print(f"分数是否及格：{score >= 60}")
print(f"姓名长度：{len(name)}个字符")
print(f"分数的平方根：{math.sqrt(score):.2f}")

# 调用函数和方法
print("\n--- f-string中调用函数 ---")
print(f"姓名大写：{name.upper()}")
print(f"当前时间：{datetime.datetime.now()}")
print(f"圆周率：{math.pi:.4f}")

# ============================================================================
# 2. f-string格式化选项
# ============================================================================

print("\n=" * 50)
print("2. f-string格式化选项")
print("=" * 50)

# 数字格式化
num = 1234.5678
print("\n--- 数字格式化 ---")
print(f"原始数字：{num}")
print(f"保留2位小数：{num:.2f}")
print(f"保留0位小数：{num:.0f}")
print(f"科学计数法：{num:.2e}")
print(f"百分比：{num/100:.1%}")

# 整数格式化
int_num = 42
print("\n--- 整数格式化 ---")
print(f"十进制：{int_num:d}")
print(f"二进制：{int_num:b}")
print(f"八进制：{int_num:o}")
print(f"十六进制：{int_num:x}")
print(f"十六进制（大写）：{int_num:X}")

# 字符串对齐和填充
text = "Python"
print("\n--- 字符串对齐和填充 ---")
print(f"左对齐（宽度10）：'{text:<10}'")
print(f"右对齐（宽度10）：'{text:>10}'")
print(f"居中对齐（宽度10）：'{text:^10}'")
print(f"用*填充居中：'{text:*^10}'")
print(f"用0填充右对齐：'{text:0>10}'")

# 数字填充
print("\n--- 数字填充 ---")
print(f"补零（宽度5）：{int_num:05d}")
print(f"带符号：{int_num:+d}")
print(f"负数带符号：{-int_num:+d}")
print(f"空格占位：{int_num: d}")

# ============================================================================
# 3. .format()方法
# ============================================================================

print("\n=" * 50)
print("3. .format()方法")
print("=" * 50)

# .format()方法是Python 2.7+和3.x都支持的格式化方式
print("\n--- .format()基础用法 ---")
print("姓名：{}，年龄：{}岁".format(name, age))
print("分数：{:.2f}分".format(score))

# 位置参数
print("\n--- 位置参数 ---")
print("学生{0}今年{1}岁，{0}的分数是{2:.1f}".format(name, age, score))
print("{2:.1f}分是{0}的成绩，{0}今年{1}岁".format(name, age, score))

# 关键字参数
print("\n--- 关键字参数 ---")
print("姓名：{name}，年龄：{age}岁，分数：{score:.2f}分".format(
    name=name, age=age, score=score
))

# 混合使用
print("\n--- 混合使用 ---")
print("{0}的信息：年龄{age}岁，分数{1:.1f}分".format(
    name, score, age=age
))

# 格式化选项
print("\n--- .format()格式化选项 ---")
print("数字：{:>10.2f}".format(num))
print("文本：{:*^15}".format(text))
print("整数：{:05d}".format(int_num))

# ============================================================================
# 4. %格式化（传统方式）
# ============================================================================

print("\n=" * 50)
print("4. %格式化（传统方式）")
print("=" * 50)

# %格式化是最古老的格式化方式，类似C语言的printf
print("\n--- %格式化基础用法 ---")
print("姓名：%s，年龄：%d岁" % (name, age))
print("分数：%.2f分" % score)
print("完整信息：%s今年%d岁，分数%.1f分" % (name, age, score))

# 常用格式符
print("\n--- 常用格式符 ---")
print("字符串：%s" % "Hello")
print("整数：%d" % 42)
print("浮点数：%f" % 3.14159)
print("保留2位小数：%.2f" % 3.14159)
print("科学计数法：%e" % 1234.5)
print("百分比：%.1%% " % 0.85)  # 注意%%表示%字符

# 宽度和对齐
print("\n--- 宽度和对齐 ---")
print("右对齐：'%10s'" % text)
print("左对齐：'%-10s'" % text)
print("补零：'%05d'" % int_num)
print("带符号：'%+d'" % int_num)

# 使用字典
print("\n--- 使用字典 ---")
student = {'name': '李四', 'age': 22, 'score': 92.5}
print("学生：%(name)s，年龄：%(age)d岁，分数：%(score).1f分" % student)

# ============================================================================
# 5. 三种方式的比较
# ============================================================================

print("\n=" * 50)
print("5. 三种格式化方式比较")
print("=" * 50)

# 相同的输出，不同的实现方式
product = "苹果"
price = 5.99
quantity = 3
total = price * quantity

print("\n--- 相同输出的不同实现 ---")

# f-string方式（推荐）
print("f-string:", f"购买{quantity}个{product}，单价{price:.2f}元，总计{total:.2f}元")

# .format()方式
print(".format():", "购买{}个{}，单价{:.2f}元，总计{:.2f}元".format(
    quantity, product, price, total
))

# %格式化方式
print("%格式化:", "购买%d个%s，单价%.2f元，总计%.2f元" % (
    quantity, product, price, total
))

# ============================================================================
# 6. 高级格式化技巧
# ============================================================================

print("\n=" * 50)
print("6. 高级格式化技巧")
print("=" * 50)

# 动态宽度
width = 15
print("\n--- 动态宽度 ---")
print(f"动态宽度：'{text:{width}}'")
print(f"动态居中：'{text:^{width}}'")

# 嵌套格式化
print("\n--- 嵌套格式化 ---")
precision = 3
print(f"动态精度：{math.pi:.{precision}f}")

# 条件格式化
print("\n--- 条件格式化 ---")
status = "通过" if score >= 60 else "不通过"
print(f"考试结果：{status}")
print(f"分数评级：{'优秀' if score >= 90 else '良好' if score >= 80 else '及格' if score >= 60 else '不及格'}")

# 格式化日期时间
print("\n--- 日期时间格式化 ---")
now = datetime.datetime.now()
print(f"当前时间：{now}")
print(f"格式化时间：{now:%Y-%m-%d %H:%M:%S}")
print(f"日期：{now:%Y年%m月%d日}")
print(f"时间：{now:%H时%M分%S秒}")

# ============================================================================
# 7. 实际应用示例
# ============================================================================

print("\n=" * 50)
print("7. 实际应用示例")
print("=" * 50)

def format_currency(amount):
    """
    格式化货币显示
    """
    return f"¥{amount:,.2f}"

def format_percentage(value):
    """
    格式化百分比显示
    """
    return f"{value:.1%}"

def format_file_size(bytes_size):
    """
    格式化文件大小显示
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024:
            return f"{bytes_size:.1f} {unit}"
        bytes_size /= 1024
    return f"{bytes_size:.1f} TB"

def print_sales_report():
    """
    打印销售报告
    """
    print("\n=== 销售报告 ===")
    print(f"{'产品':<10} {'数量':>6} {'单价':>10} {'总额':>12}")
    print("-" * 40)
    
    products = [
        ("苹果", 100, 5.99),
        ("香蕉", 80, 3.50),
        ("橙子", 60, 4.20),
        ("葡萄", 40, 8.80)
    ]
    
    total_revenue = 0
    for product, qty, price in products:
        revenue = qty * price
        total_revenue += revenue
        print(f"{product:<10} {qty:>6d} {format_currency(price):>10} {format_currency(revenue):>12}")
    
    print("-" * 40)
    print(f"{'总计':<10} {'':<6} {'':<10} {format_currency(total_revenue):>12}")

def print_student_grades():
    """
    打印学生成绩单
    """
    print("\n=== 学生成绩单 ===")
    students = [
        {"name": "张三", "math": 85, "english": 92, "science": 78},
        {"name": "李四", "math": 92, "english": 88, "science": 95},
        {"name": "王五", "math": 78, "english": 85, "science": 82},
    ]
    
    print(f"{'姓名':<8} {'数学':>6} {'英语':>6} {'科学':>6} {'平均分':>8} {'等级':<4}")
    print("-" * 45)
    
    for student in students:
        avg = (student['math'] + student['english'] + student['science']) / 3
        grade = 'A' if avg >= 90 else 'B' if avg >= 80 else 'C' if avg >= 70 else 'D'
        
        print(f"{student['name']:<8} {student['math']:>6d} {student['english']:>6d} "
              f"{student['science']:>6d} {avg:>8.1f} {grade:<4}")

# 运行示例
print("\n--- 格式化函数演示 ---")
print(f"货币格式：{format_currency(1234567.89)}")
print(f"百分比格式：{format_percentage(0.856)}")
print(f"文件大小：{format_file_size(1536000)}")

print_sales_report()
print_student_grades()

# ============================================================================
# 8. 练习题
# ============================================================================

print("\n=" * 50)
print("8. 练习题")
print("=" * 50)

print("""
练习题：

1. 基础练习：
   - 使用f-string格式化个人信息（姓名、年龄、身高、体重）
   - 用三种方式格式化同一个数学计算结果
   - 创建一个格式化的购物清单

2. 进阶练习：
   - 编写函数格式化时间显示（如：2小时30分钟）
   - 创建一个成绩单格式化程序
   - 实现一个简单的表格输出函数

3. 思考题：
   - 什么时候使用f-string，什么时候使用.format()？
   - 如何选择合适的数字精度？
   - 格式化输出对程序可读性有什么影响？

4. 挑战练习：
   - 创建一个支持多种货币的格式化函数
   - 实现一个动态表格生成器
   - 编写一个日志格式化系统
""")

# ============================================================================
# 9. 知识点总结
# ============================================================================

print("\n=" * 50)
print("9. 知识点总结")
print("=" * 50)

print("""
知识点总结：

1. 三种格式化方式：
   - f-string: f"text {variable}" (Python 3.6+，推荐)
   - .format(): "text {}".format(variable) (Python 2.7+)
   - % 格式化: "text %s" % variable (传统方式)

2. f-string优势：
   - 语法简洁直观
   - 性能最好
   - 支持表达式和函数调用
   - 易于阅读和维护

3. 常用格式化选项：
   - 数字精度：{:.2f}
   - 字符串对齐：{:<10}, {:>10}, {:^10}
   - 数字填充：{:05d}
   - 进制转换：{:b}, {:o}, {:x}
   - 百分比：{:.1%}

4. 最佳实践：
   - 优先使用f-string
   - 选择合适的精度和宽度
   - 保持格式一致性
   - 考虑国际化需求

5. 应用场景：
   - 用户界面显示
   - 报告生成
   - 日志记录
   - 数据导出
""")

print("\n程序运行完成！")
print("建议：尝试不同的格式化选项，观察输出效果。")