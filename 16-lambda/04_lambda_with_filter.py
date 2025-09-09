#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lambda表达式与filter函数

本文件介绍Lambda表达式与filter函数的结合使用，
学习如何使用filter函数对序列进行条件筛选。

学习目标：
1. 理解filter函数的工作原理
2. 掌握Lambda表达式与filter函数的结合使用
3. 学会使用filter进行数据筛选
4. 了解filter函数的应用场景
"""

import time
from datetime import datetime, date

# 1. filter函数基础
print("=== 1. filter函数基础 ===")
print("filter函数语法：filter(function, iterable)")
print("作用：根据函数返回值筛选可迭代对象中的元素")
print("返回：满足条件（函数返回True）的元素")
print()

# 基本使用示例
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 筛选偶数
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"原始数字: {numbers}")
print(f"偶数: {even_numbers}")

# 筛选奇数
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(f"奇数: {odd_numbers}")

# 筛选大于5的数
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(f"大于5的数: {greater_than_five}")
print()

# 2. filter与普通函数对比
print("=== 2. filter与普通函数对比 ===")

# 传统方法：使用循环
def filter_with_loop(numbers, condition):
    """使用循环筛选数据"""
    result = []
    for num in numbers:
        if condition(num):
            result.append(num)
    return result

# 使用filter和Lambda
def filter_with_filter(numbers, condition):
    """使用filter筛选数据"""
    return list(filter(condition, numbers))

# 使用列表推导式
def filter_with_comprehension(numbers, condition):
    """使用列表推导式筛选数据"""
    return [x for x in numbers if condition(x)]

# 测试条件函数
is_positive = lambda x: x > 0
test_numbers = [-3, -1, 0, 2, 5, -2, 8]

print(f"测试数据: {test_numbers}")
print(f"循环方法: {filter_with_loop(test_numbers, is_positive)}")
print(f"filter方法: {filter_with_filter(test_numbers, is_positive)}")
print(f"推导式方法: {filter_with_comprehension(test_numbers, is_positive)}")
print()

# 3. 字符串筛选
print("=== 3. 字符串筛选 ===")

words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# 筛选长度大于5的单词
long_words = list(filter(lambda word: len(word) > 5, words))
print(f"所有单词: {words}")
print(f"长度>5的单词: {long_words}")

# 筛选包含特定字母的单词
words_with_a = list(filter(lambda word: 'a' in word, words))
print(f"包含字母'a'的单词: {words_with_a}")

# 筛选以特定字母开头的单词
words_start_with_c = list(filter(lambda word: word.startswith('c'), words))
print(f"以'c'开头的单词: {words_start_with_c}")

# 筛选以特定字母结尾的单词
words_end_with_e = list(filter(lambda word: word.endswith('e'), words))
print(f"以'e'结尾的单词: {words_end_with_e}")
print()

# 4. 数值范围筛选
print("=== 4. 数值范围筛选 ===")

scores = [45, 67, 89, 92, 78, 56, 34, 88, 91, 73, 82, 95]

# 筛选及格分数（>=60）
passing_scores = list(filter(lambda score: score >= 60, scores))
print(f"所有分数: {scores}")
print(f"及格分数: {passing_scores}")

# 筛选优秀分数（>=90）
excellent_scores = list(filter(lambda score: score >= 90, scores))
print(f"优秀分数: {excellent_scores}")

# 筛选特定范围的分数
middle_scores = list(filter(lambda score: 70 <= score < 90, scores))
print(f"中等分数(70-89): {middle_scores}")

# 筛选异常分数（过高或过低）
abnormal_scores = list(filter(lambda score: score < 40 or score > 95, scores))
print(f"异常分数(<40 or >95): {abnormal_scores}")
print()

# 5. 复杂条件筛选
print("=== 5. 复杂条件筛选 ===")

# 学生数据
students = [
    {'name': '张三', 'age': 20, 'score': 85, 'gender': '男'},
    {'name': '李四', 'age': 19, 'score': 92, 'gender': '女'},
    {'name': '王五', 'age': 21, 'score': 78, 'gender': '男'},
    {'name': '赵六', 'age': 20, 'score': 88, 'gender': '女'},
    {'name': '钱七', 'age': 22, 'score': 76, 'gender': '男'},
    {'name': '孙八', 'age': 19, 'score': 94, 'gender': '女'}
]

# 筛选成年学生（age >= 20）
adult_students = list(filter(lambda s: s['age'] >= 20, students))
print("成年学生：")
for student in adult_students:
    print(f"{student['name']} - {student['age']}岁")

# 筛选优秀女学生（gender='女' and score >= 90）
excellent_female = list(filter(lambda s: s['gender'] == '女' and s['score'] >= 90, students))
print("\n优秀女学生：")
for student in excellent_female:
    print(f"{student['name']} - {student['score']}分")

# 筛选年轻且成绩好的学生（age < 21 and score >= 85）
young_excellent = list(filter(lambda s: s['age'] < 21 and s['score'] >= 85, students))
print("\n年轻且成绩好的学生：")
for student in young_excellent:
    print(f"{student['name']} - {student['age']}岁, {student['score']}分")
print()

# 6. 数据清洗应用
print("=== 6. 数据清洗应用 ===")

# 原始数据（包含无效数据）
raw_data = [
    {'name': '张三', 'email': 'zhang@example.com', 'phone': '13800138000'},
    {'name': '', 'email': 'li@example.com', 'phone': '13900139000'},
    {'name': '王五', 'email': 'invalid-email', 'phone': ''},
    {'name': '赵六', 'email': 'zhao@example.com', 'phone': '13700137000'},
    {'name': '钱七', 'email': '', 'phone': '13600136000'},
    {'name': '孙八', 'email': 'sun@example.com', 'phone': '1380013800'}
]

# 筛选有效数据（姓名和邮箱都不为空）
valid_data = list(filter(lambda item: item['name'] and item['email'], raw_data))
print("有效数据（姓名和邮箱都不为空）：")
for item in valid_data:
    print(f"{item['name']} - {item['email']}")

# 筛选有效邮箱（包含@符号）
valid_email_data = list(filter(lambda item: '@' in item['email'], raw_data))
print("\n有效邮箱数据：")
for item in valid_email_data:
    print(f"{item['name']} - {item['email']}")

# 筛选完整数据（所有字段都不为空）
complete_data = list(filter(lambda item: all(item.values()), raw_data))
print("\n完整数据：")
for item in complete_data:
    print(f"{item['name']} - {item['email']} - {item['phone']}")
print()

# 7. 文件和路径筛选
print("=== 7. 文件和路径筛选 ===")

file_list = [
    'document.txt', 'image.jpg', 'script.py', 'data.csv',
    'photo.png', 'readme.md', 'config.json', 'backup.zip',
    'video.mp4', 'audio.mp3', 'presentation.ppt', 'spreadsheet.xlsx'
]

# 筛选图片文件
image_files = list(filter(lambda f: f.endswith(('.jpg', '.png', '.gif', '.bmp')), file_list))
print(f"所有文件: {file_list}")
print(f"图片文件: {image_files}")

# 筛选文档文件
document_files = list(filter(lambda f: f.endswith(('.txt', '.md', '.doc', '.pdf')), file_list))
print(f"文档文件: {document_files}")

# 筛选代码文件
code_files = list(filter(lambda f: f.endswith(('.py', '.js', '.html', '.css')), file_list))
print(f"代码文件: {code_files}")

# 筛选大文件名（长度>8）
long_names = list(filter(lambda f: len(f) > 8, file_list))
print(f"长文件名: {long_names}")
print()

# 8. 日期和时间筛选
print("=== 8. 日期和时间筛选 ===")

# 模拟日期数据
from datetime import datetime, timedelta

base_date = datetime(2024, 1, 1)
dates = [base_date + timedelta(days=i*30) for i in range(12)]  # 每月一个日期

print("所有日期：")
for i, d in enumerate(dates):
    print(f"{i+1}月: {d.strftime('%Y-%m-%d')}")

# 筛选夏季月份（6-8月）
summer_dates = list(filter(lambda d: 6 <= d.month <= 8, dates))
print("\n夏季日期：")
for d in summer_dates:
    print(d.strftime('%Y-%m-%d'))

# 筛选工作日（周一到周五）
weekdays = list(filter(lambda d: d.weekday() < 5, dates))
print("\n工作日：")
for d in weekdays:
    print(f"{d.strftime('%Y-%m-%d')} ({['周一','周二','周三','周四','周五','周六','周日'][d.weekday()]})")
print()

# 9. 性能比较
print("=== 9. 性能比较 ===")

# 准备大量数据
large_numbers = list(range(100000))

def performance_test():
    # 方法1：使用filter和Lambda
    start_time = time.time()
    result1 = list(filter(lambda x: x % 2 == 0, large_numbers))
    filter_time = time.time() - start_time
    
    # 方法2：使用列表推导式
    start_time = time.time()
    result2 = [x for x in large_numbers if x % 2 == 0]
    comprehension_time = time.time() - start_time
    
    # 方法3：使用普通循环
    start_time = time.time()
    result3 = []
    for x in large_numbers:
        if x % 2 == 0:
            result3.append(x)
    loop_time = time.time() - start_time
    
    return filter_time, comprehension_time, loop_time

filter_time, comp_time, loop_time = performance_test()
print(f"filter + Lambda 时间: {filter_time:.4f} 秒")
print(f"列表推导式时间: {comp_time:.4f} 秒")
print(f"普通循环时间: {loop_time:.4f} 秒")
print()

# 10. filter的惰性求值
print("=== 10. filter的惰性求值 ===")

# filter返回迭代器
filter_result = filter(lambda x: x > 5, [1, 3, 6, 8, 2, 9])
print(f"filter对象: {filter_result}")
print(f"filter对象类型: {type(filter_result)}")

# 可以多次迭代，但每次只能使用一次
print(f"转换为列表: {list(filter_result)}")
print(f"再次转换: {list(filter_result)}")
print("注意：迭代器只能使用一次！")
print()

# 11. 实际应用案例
print("=== 11. 实际应用案例 ===")

# 案例1：电商商品筛选
products = [
    {'name': 'iPhone 15', 'price': 5999, 'category': '手机', 'rating': 4.8, 'stock': 50},
    {'name': 'MacBook Pro', 'price': 12999, 'category': '电脑', 'rating': 4.9, 'stock': 20},
    {'name': 'AirPods', 'price': 1299, 'category': '耳机', 'rating': 4.7, 'stock': 0},
    {'name': 'iPad Air', 'price': 4599, 'category': '平板', 'rating': 4.6, 'stock': 30},
    {'name': 'Apple Watch', 'price': 2999, 'category': '手表', 'rating': 4.5, 'stock': 15}
]

# 筛选有库存的商品
in_stock = list(filter(lambda p: p['stock'] > 0, products))
print("有库存的商品：")
for product in in_stock:
    print(f"{product['name']} - 库存: {product['stock']}")

# 筛选高评分商品（rating >= 4.7）
high_rated = list(filter(lambda p: p['rating'] >= 4.7, products))
print("\n高评分商品（>=4.7）：")
for product in high_rated:
    print(f"{product['name']} - 评分: {product['rating']}")

# 筛选价格适中的商品（2000-8000元）
affordable = list(filter(lambda p: 2000 <= p['price'] <= 8000, products))
print("\n价格适中的商品（2000-8000元）：")
for product in affordable:
    print(f"{product['name']} - 价格: ¥{product['price']}")

# 案例2：日志分析
log_entries = [
    {'timestamp': '2024-01-01 10:30:15', 'level': 'INFO', 'message': '系统启动'},
    {'timestamp': '2024-01-01 10:35:22', 'level': 'WARNING', 'message': '内存使用率较高'},
    {'timestamp': '2024-01-01 10:40:33', 'level': 'ERROR', 'message': '数据库连接失败'},
    {'timestamp': '2024-01-01 10:45:44', 'level': 'INFO', 'message': '用户登录'},
    {'timestamp': '2024-01-01 10:50:55', 'level': 'ERROR', 'message': '文件读取错误'}
]

# 筛选错误日志
error_logs = list(filter(lambda log: log['level'] == 'ERROR', log_entries))
print("\n错误日志：")
for log in error_logs:
    print(f"{log['timestamp']} - {log['message']}")

# 筛选特定时间段的日志
morning_logs = list(filter(lambda log: '10:30' <= log['timestamp'].split()[1] <= '10:45', log_entries))
print("\n上午时段日志：")
for log in morning_logs:
    print(f"{log['timestamp']} - {log['level']} - {log['message']}")
print()

# 12. 最佳实践和注意事项
print("=== 12. 最佳实践和注意事项 ===")
print("filter函数的优点：")
print("✓ 代码简洁，函数式编程风格")
print("✓ 惰性求值，内存效率高")
print("✓ 与Lambda表达式结合使用方便")
print("✓ 可读性好，意图明确")
print()
print("使用注意事项：")
print("⚠ filter返回迭代器，需要转换为列表查看结果")
print("⚠ 迭代器只能使用一次")
print("⚠ 复杂条件建议使用列表推导式")
print("⚠ None值会被自动过滤")
print()
print("适用场景：")
print("• 根据条件筛选序列元素")
print("• 数据清洗和验证")
print("• 与其他函数式编程工具结合")
print("• 处理大量数据时利用惰性求值")
print()
print("选择建议：")
print("• 简单条件：使用filter + Lambda")
print("• 复杂条件：使用列表推导式")
print("• 需要转换：使用map + filter组合")
print("• 性能要求高：测试不同方法选择最优")

if __name__ == "__main__":
    print("\n=== Lambda表达式与filter函数学习完成 ===")
    print("filter函数是数据筛选的重要工具")
    print("与Lambda表达式结合可以简洁地过滤数据")
    print("下一步：学习Lambda表达式与reduce函数的结合使用")