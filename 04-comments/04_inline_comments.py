#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
行内注释的使用

本文件演示Python中行内注释的使用方法、最佳实践和注意事项。
行内注释是指在代码行末尾添加的注释，用于解释该行代码的具体功能。

作者: Python学习教程
日期: 2024
"""

import random
import time

# ============================================================
# 1. 基本的行内注释使用
# ============================================================

print("=== 基本行内注释示例 ===")

# 变量声明时的行内注释
name = "张三"          # 用户姓名
age = 25              # 用户年龄
salary = 8000.50      # 月薪（元）
is_married = False    # 婚姻状态

print(f"姓名: {name}, 年龄: {age}, 月薪: {salary}, 已婚: {is_married}")

# 计算时的行内注释
total_seconds = 3661                    # 总秒数
hours = total_seconds // 3600           # 计算小时数
minutes = (total_seconds % 3600) // 60  # 计算分钟数
seconds = total_seconds % 60            # 计算剩余秒数

print(f"{total_seconds}秒 = {hours}小时{minutes}分{seconds}秒")

# ============================================================
# 2. 数学计算中的行内注释
# ============================================================

print("\n=== 数学计算行内注释 ===")

# 几何计算
radius = 5                              # 圆的半径
pi = 3.14159                           # 圆周率
area = pi * radius ** 2                # 圆的面积公式: π × r²
circumference = 2 * pi * radius        # 圆的周长公式: 2 × π × r

print(f"半径: {radius}")
print(f"面积: {area:.2f}")
print(f"周长: {circumference:.2f}")

# 物理计算
mass = 10           # 质量（kg）
velocity = 20       # 速度（m/s）
kinetic_energy = 0.5 * mass * velocity ** 2  # 动能公式: ½mv²

print(f"动能: {kinetic_energy} 焦耳")

# ============================================================
# 3. 条件判断中的行内注释
# ============================================================

print("\n=== 条件判断行内注释 ===")

score = 85

# 成绩等级判断
if score >= 90:      # 优秀等级
    grade = "A"
elif score >= 80:    # 良好等级
    grade = "B"
elif score >= 70:    # 中等等级
    grade = "C"
elif score >= 60:    # 及格等级
    grade = "D"
else:                # 不及格
    grade = "F"

print(f"成绩: {score}, 等级: {grade}")

# 年龄分组
user_age = 25

if user_age < 18:           # 未成年人
    category = "青少年"
elif user_age < 35:         # 青年
    category = "青年"
elif user_age < 60:         # 中年
    category = "中年"
else:                       # 老年
    category = "老年"

print(f"年龄: {user_age}, 分类: {category}")

# ============================================================
# 4. 循环中的行内注释
# ============================================================

print("\n=== 循环中的行内注释 ===")

# for循环示例
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:     # 遍历数字列表
    total += num        # 累加到总和
    print(f"当前数字: {num}, 累计总和: {total}")

print(f"最终总和: {total}")

# while循环示例
count = 0
while count < 3:        # 循环3次
    print(f"第 {count + 1} 次循环")
    count += 1          # 计数器递增

# ============================================================
# 5. 函数调用中的行内注释
# ============================================================

print("\n=== 函数调用行内注释 ===")

# 字符串操作
text = "  Hello World  "
clean_text = text.strip()           # 去除首尾空格
upper_text = clean_text.upper()     # 转换为大写
lower_text = clean_text.lower()     # 转换为小写

print(f"原文本: '{text}'")
print(f"清理后: '{clean_text}'")
print(f"大写: '{upper_text}'")
print(f"小写: '{lower_text}'")

# 列表操作
data = [3, 1, 4, 1, 5, 9, 2, 6]
data.sort()                         # 原地排序
max_value = max(data)               # 获取最大值
min_value = min(data)               # 获取最小值
length = len(data)                  # 获取列表长度

print(f"排序后: {data}")
print(f"最大值: {max_value}, 最小值: {min_value}, 长度: {length}")

# ============================================================
# 6. 复杂表达式的行内注释
# ============================================================

print("\n=== 复杂表达式行内注释 ===")

# 复合条件判断
x, y, z = 10, 20, 30

result = (x > 5 and y < 25) or z == 30  # 复合逻辑: (x>5且y<25) 或 z=30
print(f"复合条件结果: {result}")

# 复杂的数学表达式
a, b, c = 2, 3, 4
discriminant = b**2 - 4*a*c             # 二次方程判别式: b²-4ac
print(f"判别式: {discriminant}")

# 列表推导式
squares = [x**2 for x in range(1, 6)]   # 生成1-5的平方数列表
print(f"平方数列表: {squares}")

# ============================================================
# 7. 行内注释的注意事项和最佳实践
# ============================================================

print("\n=== 行内注释注意事项 ===")

# 好的行内注释示例
temperature = 25        # 摄氏度
fahrenheit = temperature * 9/5 + 32     # 转换为华氏度

# 避免显而易见的注释
# 不好的例子：
# x = 5                 # 将5赋值给x
# 好的例子：
max_attempts = 5        # 最大重试次数

# 注释应该解释"为什么"而不是"是什么"
retry_delay = 2         # 重试间隔，避免频繁请求被限制
time.sleep(0.1)         # 短暂延迟，模拟处理时间

# 保持注释与代码的一致性
user_input = "test"     # 用户输入的测试数据
if user_input:          # 检查输入是否为空
    print(f"处理输入: {user_input}")

# ============================================================
# 8. 特殊情况下的行内注释
# ============================================================

print("\n=== 特殊情况行内注释 ===")

# 魔法数字的解释
VAT_RATE = 0.13         # 增值税率 13%
DISCOUNT_RATE = 0.1     # 折扣率 10%
MAX_RETRY = 3           # 最大重试次数

price = 100
tax = price * VAT_RATE          # 计算税费
discount = price * DISCOUNT_RATE # 计算折扣
final_price = price + tax - discount  # 最终价格

print(f"原价: {price}, 税费: {tax}, 折扣: {discount}, 最终价格: {final_price}")

# 临时调试代码
debug_mode = True
if debug_mode:          # TODO: 发布前移除调试代码
    print("调试信息: 程序运行正常")

# 平台特定代码
import sys
if sys.platform == "win32":    # Windows系统特定处理
    path_separator = "\\"
else:                           # Unix/Linux系统
    path_separator = "/"

print(f"路径分隔符: {path_separator}")

# ============================================================
# 9. 行内注释的格式规范
# ============================================================

print("\n=== 格式规范示例 ===")

# 推荐格式：代码后至少两个空格，然后是#和一个空格
width = 10              # 矩形宽度
height = 5              # 矩形高度
area_rect = width * height  # 计算矩形面积

# 对齐注释（可选，适用于相关的代码块）
student_name = "李明"    # 学生姓名
student_id = "2024001"  # 学号
student_grade = 85      # 成绩

print(f"学生信息: {student_name} ({student_id}) - {student_grade}分")

print("\n=== 行内注释演示完成 ===")
print("行内注释应该简洁明了，解释代码的目的而不是重复代码")
print("合理使用行内注释可以让代码更容易理解和维护")
print("记住：好的代码本身就是最好的文档")

# 运行这个文件来查看行内注释的效果
# 在终端中执行: python 04_inline_comments.py