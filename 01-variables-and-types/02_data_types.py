#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第二课：数据类型详解

学习目标：
1. 了解Python的基本数据类型
2. 掌握整数(int)类型的特点和用法
3. 掌握浮点数(float)类型的特点和用法
4. 掌握字符串(str)类型的特点和用法
5. 掌握布尔值(bool)类型的特点和用法
6. 学会使用type()函数查看数据类型

作者：Python基础教程
日期：2024年
"""

print("=" * 50)
print("第二课：数据类型详解")
print("=" * 50)

# 1. Python的基本数据类型概述
print("\n1. Python的基本数据类型概述")
print("-" * 30)
print("Python有四种基本数据类型：")
print("• int（整数）")
print("• float（浮点数）")
print("• str（字符串）")
print("• bool（布尔值）")

# 2. 整数类型 (int)
print("\n2. 整数类型 (int)")
print("-" * 30)
print("整数是没有小数部分的数字")

# 正整数
positive_num = 42
print(f"正整数：{positive_num}，类型：{type(positive_num)}")

# 负整数
negative_num = -17
print(f"负整数：{negative_num}，类型：{type(negative_num)}")

# 零
zero = 0
print(f"零：{zero}，类型：{type(zero)}")

# 大整数（Python可以处理任意大的整数）
big_num = 123456789012345678901234567890
print(f"大整数：{big_num}")
print(f"大整数类型：{type(big_num)}")

# 不同进制的整数
print("\n不同进制的整数表示：")
binary_num = 0b1010  # 二进制
octal_num = 0o12     # 八进制
hex_num = 0xa        # 十六进制
print(f"二进制 0b1010 = {binary_num}")
print(f"八进制 0o12 = {octal_num}")
print(f"十六进制 0xa = {hex_num}")

# 3. 浮点数类型 (float)
print("\n3. 浮点数类型 (float)")
print("-" * 30)
print("浮点数是带有小数部分的数字")

# 普通浮点数
float_num1 = 3.14
print(f"浮点数：{float_num1}，类型：{type(float_num1)}")

# 负浮点数
float_num2 = -2.5
print(f"负浮点数：{float_num2}，类型：{type(float_num2)}")

# 科学计数法
scientific_num1 = 1.5e3  # 1.5 × 10^3 = 1500
scientific_num2 = 2.5e-2  # 2.5 × 10^-2 = 0.025
print(f"科学计数法 1.5e3 = {scientific_num1}")
print(f"科学计数法 2.5e-2 = {scientific_num2}")

# 特殊浮点数值
print("\n特殊浮点数值：")
infinity = float('inf')  # 无穷大
neg_infinity = float('-inf')  # 负无穷大
not_a_number = float('nan')  # 非数字
print(f"正无穷：{infinity}")
print(f"负无穷：{neg_infinity}")
print(f"非数字：{not_a_number}")

# 4. 字符串类型 (str)
print("\n4. 字符串类型 (str)")
print("-" * 30)
print("字符串是用引号包围的文本")

# 单引号字符串
single_quote_str = 'Hello World'
print(f"单引号字符串：{single_quote_str}，类型：{type(single_quote_str)}")

# 双引号字符串
double_quote_str = "Python编程"
print(f"双引号字符串：{double_quote_str}，类型：{type(double_quote_str)}")

# 三引号字符串（多行字符串）
multi_line_str = """这是一个
多行字符串
可以包含换行符"""
print(f"多行字符串：{multi_line_str}")

# 空字符串
empty_str = ""
print(f"空字符串：'{empty_str}'，长度：{len(empty_str)}")

# 字符串中包含引号
quote_in_str1 = "他说：'你好！'"
quote_in_str2 = '她回答："很高兴见到你！"'
print(f"字符串中包含单引号：{quote_in_str1}")
print(f"字符串中包含双引号：{quote_in_str2}")

# 转义字符
escape_str = "第一行\n第二行\t制表符\\反斜杠"
print(f"转义字符示例：{escape_str}")

# 原始字符串（r字符串）
raw_str = r"C:\Users\name\Documents"
print(f"原始字符串：{raw_str}")

# 5. 布尔值类型 (bool)
print("\n5. 布尔值类型 (bool)")
print("-" * 30)
print("布尔值只有两个值：True 和 False")

# 布尔值
bool_true = True
bool_false = False
print(f"True：{bool_true}，类型：{type(bool_true)}")
print(f"False：{bool_false}，类型：{type(bool_false)}")

# 布尔值的数值表示
print(f"True 的数值：{int(bool_true)}")
print(f"False 的数值：{int(bool_false)}")

# 比较运算产生布尔值
comparison1 = 5 > 3
comparison2 = 10 == 5
comparison3 = "hello" == "world"
print(f"5 > 3 的结果：{comparison1}")
print(f"10 == 5 的结果：{comparison2}")
print(f"'hello' == 'world' 的结果：{comparison3}")

# 6. 使用type()函数查看数据类型
print("\n6. 使用type()函数查看数据类型")
print("-" * 30)

# 创建不同类型的变量
num_int = 100
num_float = 3.14
text = "Hello"
is_valid = True

print("使用type()函数查看变量类型：")
print(f"type({num_int}) = {type(num_int)}")
print(f"type({num_float}) = {type(num_float)}")
print(f"type('{text}') = {type(text)}")
print(f"type({is_valid}) = {type(is_valid)}")

# 7. 数据类型的特点总结
print("\n7. 数据类型的特点总结")
print("-" * 30)
print("int（整数）：")
print("  • 没有小数部分")
print("  • 可以是正数、负数或零")
print("  • 支持任意大的整数")
print("  • 支持不同进制表示")

print("\nfloat（浮点数）：")
print("  • 有小数部分")
print("  • 支持科学计数法")
print("  • 有精度限制")
print("  • 支持特殊值（inf, -inf, nan）")

print("\nstr（字符串）：")
print("  • 用引号包围的文本")
print("  • 支持单引号、双引号、三引号")
print("  • 支持转义字符")
print("  • 不可变类型")

print("\nbool（布尔值）：")
print("  • 只有True和False两个值")
print("  • 用于逻辑判断")
print("  • 可以转换为数字（True=1, False=0）")

# 8. 实践练习
print("\n8. 实践练习")
print("-" * 30)
print("请尝试创建以下变量并查看它们的类型：")
print("1. 一个表示年龄的整数")
print("2. 一个表示身高的浮点数")
print("3. 一个表示姓名的字符串")
print("4. 一个表示是否成年的布尔值")

# 练习示例
age = 25
height = 175.5
name = "张三"
is_adult = True

print("\n练习答案示例：")
print(f"年龄：{age}，类型：{type(age)}")
print(f"身高：{height}，类型：{type(height)}")
print(f"姓名：{name}，类型：{type(name)}")
print(f"是否成年：{is_adult}，类型：{type(is_adult)}")

# 9. 思考题
print("\n9. 思考题")
print("-" * 30)
print("1. 为什么 3.0 是 float 类型而不是 int 类型？")
print("2. 字符串 '123' 和 整数 123 有什么区别？")
print("3. True + True 的结果是什么？为什么？")
print("4. 如何判断一个变量是否为字符串类型？")

# 思考题答案
print("\n思考题答案：")
print("1. 因为有小数点，Python将其识别为浮点数")
print("2. '123'是字符串，不能进行数学运算；123是整数，可以进行数学运算")
print(f"3. True + True = {True + True}，因为True在数学运算中被当作1")
print("4. 使用 type(变量) == str 或 isinstance(变量, str)")

# 10. 常见错误和注意事项
print("\n10. 常见错误和注意事项")
print("-" * 30)
print("常见错误：")
print("1. 混淆字符串和数字：'123' + 456 会报错")
print("2. 浮点数精度问题：0.1 + 0.2 可能不等于 0.3")
print("3. 大小写敏感：true 和 True 是不同的")

# 演示浮点数精度问题
result = 0.1 + 0.2
print(f"\n浮点数精度演示：0.1 + 0.2 = {result}")
print(f"是否等于0.3：{result == 0.3}")
print(f"正确的比较方法：{abs(result - 0.3) < 1e-10}")

print("\n=" * 50)
print("第二课学习完成！")
print("下一课将学习Python的动态类型特性")
print("=" * 50)

# 运行这个文件的方法：
# 在终端中输入：python 02_data_types.py
# 或者在IDE中直接运行