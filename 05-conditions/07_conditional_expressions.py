#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
条件表达式（三元运算符）

本文件演示Python中条件表达式的用法，包括：
1. 基本条件表达式语法
2. 条件表达式与if-else的对比
3. 嵌套条件表达式
4. 条件表达式的实际应用场景
5. 条件表达式的最佳实践

学习目标：
- 掌握条件表达式的基本语法
- 理解何时使用条件表达式
- 学会编写简洁的条件判断代码
- 避免过度复杂的条件表达式
"""

# 1. 基本条件表达式语法
print("=== 1. 基本条件表达式语法 ===")

# 语法：value_if_true if condition else value_if_false
age = 20

# 传统if-else写法
if age >= 18:
    status = "成年人"
else:
    status = "未成年人"
print(f"传统写法：{status}")

# 条件表达式写法
status = "成年人" if age >= 18 else "未成年人"
print(f"条件表达式：{status}")

# 数值计算中的应用
score = 85
grade = "及格" if score >= 60 else "不及格"
print(f"分数 {score}：{grade}")

# 布尔值转换
is_weekend = True
day_type = "休息日" if is_weekend else "工作日"
print(f"今天是：{day_type}")

print()

# 2. 条件表达式在函数中的应用
print("=== 2. 条件表达式在函数中的应用 ===")

def get_absolute_value(number):
    """获取绝对值（使用条件表达式）"""
    return number if number >= 0 else -number

def get_max(a, b):
    """获取两个数的最大值"""
    return a if a > b else b

def get_min(a, b):
    """获取两个数的最小值"""
    return a if a < b else b

def is_even_or_odd(number):
    """判断奇偶性"""
    return "偶数" if number % 2 == 0 else "奇数"

# 测试函数
test_numbers = [-5, 10, 0, 7]
for num in test_numbers:
    abs_val = get_absolute_value(num)
    parity = is_even_or_odd(num)
    print(f"{num}: 绝对值={abs_val}, {parity}")

print(f"max(15, 23) = {get_max(15, 23)}")
print(f"min(15, 23) = {get_min(15, 23)}")

print()

# 3. 列表和字符串处理中的条件表达式
print("=== 3. 列表和字符串处理 ===")

# 列表推导式中的条件表达式
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 将奇数变为负数，偶数保持不变
processed_numbers = [num if num % 2 == 0 else -num for num in numbers]
print(f"原列表：{numbers}")
print(f"处理后：{processed_numbers}")

# 字符串处理
names = ["alice", "BOB", "Charlie", "DAVID"]

# 统一格式：首字母大写
formatted_names = [name.capitalize() if name.islower() or name.isupper() else name for name in names]
print(f"原名字：{names}")
print(f"格式化后：{formatted_names}")

# 字符串长度处理
words = ["cat", "elephant", "dog", "hippopotamus"]
short_words = [word if len(word) <= 5 else word[:5] + "..." for word in words]
print(f"原单词：{words}")
print(f"截断后：{short_words}")

print()

# 4. 嵌套条件表达式
print("=== 4. 嵌套条件表达式 ===")

# 简单的嵌套
score = 92

# 三级评分
grade = "优秀" if score >= 90 else ("良好" if score >= 80 else ("及格" if score >= 60 else "不及格"))
print(f"分数 {score}：{grade}")

# 更清晰的写法（推荐）
def get_grade(score):
    """获取成绩等级"""
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

# 年龄分组的嵌套条件表达式
age = 25
age_group = "儿童" if age < 12 else ("青少年" if age < 18 else ("青年" if age < 35 else ("中年" if age < 60 else "老年")))
print(f"年龄 {age}：{age_group}")

# 温度和天气建议
temperature = 22
weather = "sunny"

advice = ("穿短袖" if temperature > 25 else "穿长袖") if weather == "sunny" else ("带雨伞" if weather == "rainy" else "查看天气")
print(f"温度 {temperature}°C，天气 {weather}：{advice}")

print()

# 5. 条件表达式在数据处理中的应用
print("=== 5. 数据处理应用 ===")

# 学生成绩数据处理
students = [
    {"name": "Alice", "score": 95, "attendance": 0.9},
    {"name": "Bob", "score": 78, "attendance": 0.85},
    {"name": "Charlie", "score": 65, "attendance": 0.95},
    {"name": "David", "score": 45, "attendance": 0.7},
]

# 添加状态字段
for student in students:
    # 综合评价
    student["status"] = "优秀" if student["score"] >= 85 and student["attendance"] >= 0.9 else \
                       "良好" if student["score"] >= 70 and student["attendance"] >= 0.8 else \
                       "需要改进"
    
    # 是否需要补考
    student["needs_makeup"] = "是" if student["score"] < 60 else "否"
    
    # 出勤评价
    student["attendance_grade"] = "优秀" if student["attendance"] >= 0.95 else \
                                 "良好" if student["attendance"] >= 0.85 else \
                                 "一般" if student["attendance"] >= 0.75 else "较差"

# 显示结果
for student in students:
    print(f"{student['name']}: 分数={student['score']}, 出勤={student['attendance']:.1%}")
    print(f"  状态: {student['status']}, 补考: {student['needs_makeup']}, 出勤评价: {student['attendance_grade']}")

print()

# 6. 条件表达式在配置和设置中的应用
print("=== 6. 配置和设置应用 ===")

# 环境配置
import os

# 模拟环境变量
os.environ["DEBUG"] = "True"
os.environ["PORT"] = "8080"

# 使用条件表达式设置默认值
debug_mode = True if os.environ.get("DEBUG", "False").lower() == "true" else False
port = int(os.environ.get("PORT")) if os.environ.get("PORT") else 3000
log_level = "DEBUG" if debug_mode else "INFO"
database_url = os.environ.get("DATABASE_URL") if os.environ.get("DATABASE_URL") else "sqlite:///default.db"

print(f"调试模式: {debug_mode}")
print(f"端口: {port}")
print(f"日志级别: {log_level}")
print(f"数据库URL: {database_url}")

# 用户偏好设置
user_preferences = {
    "theme": "dark",
    "language": "zh",
    "notifications": True
}

# 应用设置
theme = user_preferences.get("theme") if user_preferences.get("theme") else "light"
language = user_preferences.get("language") if user_preferences.get("language") else "en"
notifications = user_preferences.get("notifications") if user_preferences.get("notifications") is not None else True

print(f"\n用户设置:")
print(f"主题: {theme}")
print(f"语言: {language}")
print(f"通知: {'开启' if notifications else '关闭'}")

print()

# 7. 条件表达式的性能考虑
print("=== 7. 性能考虑 ===")

import time

def expensive_operation_a():
    """模拟耗时操作A"""
    time.sleep(0.001)  # 模拟1毫秒延迟
    return "结果A"

def expensive_operation_b():
    """模拟耗时操作B"""
    time.sleep(0.001)  # 模拟1毫秒延迟
    return "结果B"

# 条件表达式会执行所有表达式
condition = True
start_time = time.time()
result = expensive_operation_a() if condition else expensive_operation_b()
end_time = time.time()
print(f"条件表达式结果: {result}")
print(f"执行时间: {(end_time - start_time) * 1000:.2f}ms")

# 传统if-else只执行需要的分支
start_time = time.time()
if condition:
    result = expensive_operation_a()
else:
    result = expensive_operation_b()
end_time = time.time()
print(f"传统if-else结果: {result}")
print(f"执行时间: {(end_time - start_time) * 1000:.2f}ms")

print()

# 8. 条件表达式的最佳实践
print("=== 8. 最佳实践 ===")

# ✓ 好的用法：简单、清晰
def get_discount(is_member):
    """获取折扣"""
    return 0.1 if is_member else 0.0

# ✓ 好的用法：处理None值
def safe_divide(a, b):
    """安全除法"""
    return a / b if b != 0 else 0

# ✓ 好的用法：设置默认值
def greet(name):
    """问候函数"""
    display_name = name if name else "访客"
    return f"你好，{display_name}！"

# ✗ 不好的用法：过于复杂
def bad_example(score, attendance, behavior):
    """不推荐的复杂条件表达式"""
    return "优秀" if score >= 90 and attendance >= 0.95 and behavior == "good" else \
           "良好" if score >= 80 and attendance >= 0.85 and behavior in ["good", "fair"] else \
           "一般" if score >= 70 and attendance >= 0.75 else \
           "需要改进"

# ✓ 更好的写法：使用函数
def good_example(score, attendance, behavior):
    """推荐的清晰写法"""
    if score >= 90 and attendance >= 0.95 and behavior == "good":
        return "优秀"
    elif score >= 80 and attendance >= 0.85 and behavior in ["good", "fair"]:
        return "良好"
    elif score >= 70 and attendance >= 0.75:
        return "一般"
    else:
        return "需要改进"

# 测试最佳实践
print(f"会员折扣: {get_discount(True):.1%}")
print(f"非会员折扣: {get_discount(False):.1%}")
print(f"安全除法 10/2: {safe_divide(10, 2)}")
print(f"安全除法 10/0: {safe_divide(10, 0)}")
print(f"问候: {greet('Alice')}")
print(f"问候空名字: {greet('')}")

print()

# 9. 实际项目中的应用示例
print("=== 9. 实际项目应用 ===")

# Web应用中的状态显示
class Order:
    def __init__(self, order_id, status, payment_status, items_count):
        self.order_id = order_id
        self.status = status
        self.payment_status = payment_status
        self.items_count = items_count
    
    def get_display_status(self):
        """获取显示状态"""
        return "已完成" if self.status == "completed" else \
               "处理中" if self.status == "processing" else \
               "已取消" if self.status == "cancelled" else "未知状态"
    
    def get_action_button(self):
        """获取操作按钮文本"""
        return "查看详情" if self.status == "completed" else \
               "取消订单" if self.status in ["pending", "processing"] else \
               "重新下单" if self.status == "cancelled" else "联系客服"
    
    def get_payment_info(self):
        """获取支付信息"""
        return "已支付" if self.payment_status == "paid" else \
               "待支付" if self.payment_status == "pending" else \
               "支付失败" if self.payment_status == "failed" else "未知"

# 创建订单示例
orders = [
    Order("ORD001", "completed", "paid", 3),
    Order("ORD002", "processing", "paid", 1),
    Order("ORD003", "cancelled", "refunded", 2),
    Order("ORD004", "pending", "pending", 5),
]

print("订单状态:")
for order in orders:
    print(f"订单 {order.order_id}:")
    print(f"  状态: {order.get_display_status()}")
    print(f"  支付: {order.get_payment_info()}")
    print(f"  操作: {order.get_action_button()}")
    print(f"  商品数量: {order.items_count}")
    print()

# 10. 条件表达式与lambda函数结合
print("=== 10. 与lambda函数结合 ===")

# 排序中使用条件表达式
students_data = [
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 87},
    {"name": "Charlie", "score": 92},
    {"name": "David", "score": 78},
]

# 按分数排序，相同分数按姓名排序
sorted_students = sorted(students_data, 
                        key=lambda x: (-x["score"], x["name"]))

print("排序后的学生:")
for student in sorted_students:
    grade = "优秀" if student["score"] >= 90 else "良好" if student["score"] >= 80 else "一般"
    print(f"{student['name']}: {student['score']} ({grade})")

# 过滤和映射
high_scores = list(filter(lambda x: x["score"] >= 85, students_data))
grade_labels = list(map(lambda x: f"{x['name']}: {'优秀' if x['score'] >= 90 else '良好'}", high_scores))

print(f"\n高分学生: {grade_labels}")

print()
print("=== 程序结束 ===")

# 练习题
print("\n=== 练习题 ===")
print("1. 使用条件表达式编写函数，返回两个数中的较大值")
print("2. 编写函数使用条件表达式判断年份是否为闰年")
print("3. 使用条件表达式和列表推导式，将列表中的负数转为0，正数保持不变")
print("4. 编写函数使用条件表达式实现简单的税率计算")
print("5. 使用条件表达式编写用户输入验证函数（用户名、邮箱等）")