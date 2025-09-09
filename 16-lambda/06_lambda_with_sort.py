#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lambda表达式与排序函数

本文件介绍Lambda表达式与排序函数的结合使用，
学习如何使用Lambda表达式自定义排序规则。

学习目标：
1. 掌握sorted()函数和list.sort()方法的使用
2. 学会使用Lambda表达式作为排序的key函数
3. 理解多级排序和复杂排序规则
4. 掌握排序的最佳实践
"""

import operator
from datetime import datetime
import random

# 1. 排序函数基础
print("=== 1. 排序函数基础 ===")
print("Python中的两种排序方式：")
print("1. sorted() - 返回新的排序列表，不修改原列表")
print("2. list.sort() - 就地排序，修改原列表")
print()

# 基本排序示例
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"原始列表: {numbers}")

# 使用sorted()函数
sorted_numbers = sorted(numbers)
print(f"sorted()结果: {sorted_numbers}")
print(f"原列表未变: {numbers}")

# 使用list.sort()方法
numbers_copy = numbers.copy()
numbers_copy.sort()
print(f"sort()后列表: {numbers_copy}")

# 降序排序
desc_numbers = sorted(numbers, reverse=True)
print(f"降序排序: {desc_numbers}")
print()

# 2. 使用Lambda作为key函数
print("=== 2. 使用Lambda作为key函数 ===")

# 按绝对值排序
numbers_with_negative = [-5, 3, -1, 8, -9, 2, -4, 7]
print(f"包含负数的列表: {numbers_with_negative}")

# 按绝对值排序
abs_sorted = sorted(numbers_with_negative, key=lambda x: abs(x))
print(f"按绝对值排序: {abs_sorted}")

# 按数字的平方排序
square_sorted = sorted(numbers_with_negative, key=lambda x: x**2)
print(f"按平方值排序: {square_sorted}")

# 按数字除以3的余数排序
mod_sorted = sorted(numbers, key=lambda x: x % 3)
print(f"按除3余数排序: {mod_sorted}")
print("余数分组: 0余数={}, 1余数={}, 2余数={}".format(
    [x for x in numbers if x % 3 == 0],
    [x for x in numbers if x % 3 == 1],
    [x for x in numbers if x % 3 == 2]
))
print()

# 3. 字符串排序
print("=== 3. 字符串排序 ===")

words = ['apple', 'Banana', 'cherry', 'Date', 'elderberry']
print(f"单词列表: {words}")

# 默认排序（按ASCII值）
default_sorted = sorted(words)
print(f"默认排序: {default_sorted}")

# 忽略大小写排序
case_insensitive = sorted(words, key=lambda x: x.lower())
print(f"忽略大小写: {case_insensitive}")

# 按长度排序
length_sorted = sorted(words, key=lambda x: len(x))
print(f"按长度排序: {length_sorted}")

# 按长度排序，长度相同时按字母顺序
length_alpha_sorted = sorted(words, key=lambda x: (len(x), x.lower()))
print(f"长度+字母排序: {length_alpha_sorted}")

# 按最后一个字符排序
last_char_sorted = sorted(words, key=lambda x: x[-1].lower())
print(f"按最后字符排序: {last_char_sorted}")

# 按元音字母数量排序
vowels = 'aeiouAEIOU'
vowel_count_sorted = sorted(words, key=lambda x: sum(1 for char in x if char in vowels))
print(f"按元音数量排序: {vowel_count_sorted}")
for word in words:
    vowel_count = sum(1 for char in word if char in vowels)
    print(f"  {word}: {vowel_count}个元音")
print()

# 4. 复杂数据结构排序
print("=== 4. 复杂数据结构排序 ===")

# 学生信息排序
students = [
    {'name': '张三', 'age': 20, 'score': 85, 'grade': 'A'},
    {'name': '李四', 'age': 19, 'score': 92, 'grade': 'A'},
    {'name': '王五', 'age': 21, 'score': 78, 'grade': 'B'},
    {'name': '赵六', 'age': 20, 'score': 88, 'grade': 'A'},
    {'name': '钱七', 'age': 22, 'score': 76, 'grade': 'B'}
]

print("学生信息排序示例：")

# 按分数排序
score_sorted = sorted(students, key=lambda x: x['score'], reverse=True)
print("按分数降序排序：")
for student in score_sorted:
    print(f"  {student['name']}: {student['score']}分")

# 按年龄排序
age_sorted = sorted(students, key=lambda x: x['age'])
print("\n按年龄升序排序：")
for student in age_sorted:
    print(f"  {student['name']}: {student['age']}岁")

# 按等级和分数排序（多级排序）
grade_score_sorted = sorted(students, key=lambda x: (x['grade'], -x['score']))
print("\n按等级升序，分数降序排序：")
for student in grade_score_sorted:
    print(f"  {student['name']}: {student['grade']}等级, {student['score']}分")

# 按姓名长度和字母顺序排序
name_sorted = sorted(students, key=lambda x: (len(x['name']), x['name']))
print("\n按姓名长度和字母顺序排序：")
for student in name_sorted:
    print(f"  {student['name']}: 长度{len(student['name'])}")
print()

# 5. 元组和列表排序
print("=== 5. 元组和列表排序 ===")

# 坐标点排序
points = [(3, 4), (1, 2), (5, 1), (2, 3), (4, 2)]
print(f"坐标点: {points}")

# 按x坐标排序
x_sorted = sorted(points, key=lambda point: point[0])
print(f"按x坐标排序: {x_sorted}")

# 按y坐标排序
y_sorted = sorted(points, key=lambda point: point[1])
print(f"按y坐标排序: {y_sorted}")

# 按距离原点的距离排序
distance_sorted = sorted(points, key=lambda point: (point[0]**2 + point[1]**2)**0.5)
print(f"按距离原点排序: {distance_sorted}")
for point in points:
    distance = (point[0]**2 + point[1]**2)**0.5
    print(f"  {point}: 距离 = {distance:.2f}")

# 按象限排序
def get_quadrant(point):
    x, y = point
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4

points_with_negative = [(3, 4), (-1, 2), (-5, -1), (2, -3), (4, 2)]
quadrant_sorted = sorted(points_with_negative, key=lambda point: get_quadrant(point))
print(f"\n包含负坐标: {points_with_negative}")
print(f"按象限排序: {quadrant_sorted}")
for point in points_with_negative:
    print(f"  {point}: 第{get_quadrant(point)}象限")
print()

# 6. 日期和时间排序
print("=== 6. 日期和时间排序 ===")

# 日期字符串排序
date_strings = ['2023-12-25', '2023-01-15', '2023-06-30', '2023-03-10', '2023-09-05']
print(f"日期字符串: {date_strings}")

# 直接排序（字符串比较）
string_sorted = sorted(date_strings)
print(f"字符串排序: {string_sorted}")

# 转换为日期对象排序
date_obj_sorted = sorted(date_strings, key=lambda x: datetime.strptime(x, '%Y-%m-%d'))
print(f"日期对象排序: {date_obj_sorted}")

# 复杂日期格式
complex_dates = ['Dec 25, 2023', 'Jan 15, 2023', 'Jun 30, 2023', 'Mar 10, 2023']
complex_sorted = sorted(complex_dates, key=lambda x: datetime.strptime(x, '%b %d, %Y'))
print(f"\n复杂日期格式: {complex_dates}")
print(f"排序结果: {complex_sorted}")

# 按月份排序
month_sorted = sorted(date_strings, key=lambda x: datetime.strptime(x, '%Y-%m-%d').month)
print(f"按月份排序: {month_sorted}")

# 按星期几排序
weekday_sorted = sorted(date_strings, key=lambda x: datetime.strptime(x, '%Y-%m-%d').weekday())
print(f"按星期几排序: {weekday_sorted}")
for date_str in date_strings:
    weekday = datetime.strptime(date_str, '%Y-%m-%d').strftime('%A')
    print(f"  {date_str}: {weekday}")
print()

# 7. 自定义排序规则
print("=== 7. 自定义排序规则 ===")

# 扑克牌排序
cards = ['A♠', 'K♥', '2♣', 'J♦', '10♠', 'Q♥', '3♣', 'A♥', '5♦', 'K♠']
print(f"扑克牌: {cards}")

# 定义牌面值和花色的优先级
def card_value(card):
    # 提取牌面和花色
    if card.startswith('10'):
        face = '10'
        suit = card[2:]
    else:
        face = card[0]
        suit = card[1:]
    
    # 牌面值映射
    face_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
                   '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    
    # 花色优先级
    suit_values = {'♠': 1, '♥': 2, '♦': 3, '♣': 4}
    
    return (face_values[face], suit_values[suit])

cards_sorted = sorted(cards, key=card_value)
print(f"排序后扑克牌: {cards_sorted}")

# 中文姓名排序（按拼音）
names = ['张三', '李四', '王五', '赵六', '钱七', '孙八', '周九', '吴十']
print(f"\n中文姓名: {names}")

# 简单的拼音映射（实际应用中可使用pypinyin库）
pinyin_map = {
    '张': 'zhang', '李': 'li', '王': 'wang', '赵': 'zhao',
    '钱': 'qian', '孙': 'sun', '周': 'zhou', '吴': 'wu'
}

names_sorted = sorted(names, key=lambda x: pinyin_map.get(x[0], x[0]))
print(f"按拼音排序: {names_sorted}")

# 版本号排序
versions = ['1.10.2', '1.2.1', '1.10.10', '1.2.10', '2.1.0', '1.10.1']
print(f"\n版本号: {versions}")

# 按版本号规则排序
def version_key(version):
    return tuple(map(int, version.split('.')))

versions_sorted = sorted(versions, key=version_key)
print(f"正确的版本排序: {versions_sorted}")

# 错误的字符串排序对比
wrong_sorted = sorted(versions)
print(f"错误的字符串排序: {wrong_sorted}")
print()

# 8. 稳定排序和多级排序
print("=== 8. 稳定排序和多级排序 ===")

# 员工信息
employees = [
    {'name': '张三', 'department': 'IT', 'salary': 8000, 'age': 25},
    {'name': '李四', 'department': 'HR', 'salary': 7000, 'age': 30},
    {'name': '王五', 'department': 'IT', 'salary': 9000, 'age': 28},
    {'name': '赵六', 'department': 'Finance', 'salary': 8500, 'age': 32},
    {'name': '钱七', 'department': 'IT', 'salary': 8000, 'age': 26},
    {'name': '孙八', 'department': 'HR', 'salary': 7500, 'age': 29}
]

print("员工多级排序示例：")

# 按部门和薪资排序
dept_salary_sorted = sorted(employees, key=lambda x: (x['department'], -x['salary']))
print("按部门升序，薪资降序：")
for emp in dept_salary_sorted:
    print(f"  {emp['name']}: {emp['department']}, ¥{emp['salary']}")

# 按薪资范围和年龄排序
def salary_range(salary):
    if salary < 7500:
        return 'Low'
    elif salary < 8500:
        return 'Medium'
    else:
        return 'High'

salary_age_sorted = sorted(employees, key=lambda x: (salary_range(x['salary']), x['age']))
print("\n按薪资范围和年龄排序：")
for emp in salary_age_sorted:
    print(f"  {emp['name']}: {salary_range(emp['salary'])}, {emp['age']}岁")

# 稳定排序演示
print("\n稳定排序演示（相同薪资保持原顺序）：")
same_salary = [emp for emp in employees if emp['salary'] == 8000]
print(f"薪资8000的员工原顺序: {[emp['name'] for emp in same_salary]}")

salary_sorted = sorted(employees, key=lambda x: x['salary'])
same_salary_after = [emp for emp in salary_sorted if emp['salary'] == 8000]
print(f"排序后相同薪资顺序: {[emp['name'] for emp in same_salary_after]}")
print("Python的排序是稳定的，相同值保持原有顺序")
print()

# 9. 排序性能和优化
print("=== 9. 排序性能和优化 ===")

# 生成测试数据
import time

def generate_test_data(size):
    return [random.randint(1, 1000) for _ in range(size)]

# 性能测试
def performance_test(data_size=10000):
    data = generate_test_data(data_size)
    
    # 测试不同排序方法的性能
    methods = [
        ('内置排序', lambda x: sorted(x)),
        ('Lambda key', lambda x: sorted(x, key=lambda item: item)),
        ('operator.itemgetter', lambda x: sorted(x, key=operator.itemgetter(0)) if isinstance(x[0], (list, tuple)) else sorted(x)),
        ('list.sort()', lambda x: x.sort() or x)  # sort()返回None，用or返回列表
    ]
    
    results = []
    for name, method in methods[:2]:  # 只测试前两个，避免修改原数据
        test_data = data.copy()
        start_time = time.time()
        try:
            result = method(test_data)
            end_time = time.time()
            results.append((name, end_time - start_time))
        except:
            results.append((name, float('inf')))
    
    return results

print(f"排序性能测试（数据量：10000）：")
perf_results = performance_test()
for name, duration in perf_results:
    print(f"{name}: {duration:.6f} 秒")

# 排序优化建议
print("\n排序优化建议：")
print("1. 对于简单数据类型，直接使用sorted()")
print("2. 对于复杂key计算，考虑预计算")
print("3. 使用operator模块的函数替代lambda")
print("4. 就地排序使用list.sort()节省内存")
print("5. 多级排序使用元组key")
print()

# 10. operator模块的使用
print("=== 10. operator模块的使用 ===")

# 使用operator替代lambda
students_simple = [('张三', 85), ('李四', 92), ('王五', 78), ('赵六', 88)]
print(f"学生成绩: {students_simple}")

# 使用lambda
lambda_sorted = sorted(students_simple, key=lambda x: x[1], reverse=True)
print(f"Lambda排序: {lambda_sorted}")

# 使用operator.itemgetter
operator_sorted = sorted(students_simple, key=operator.itemgetter(1), reverse=True)
print(f"operator排序: {operator_sorted}")

# 多级排序比较
students_multi = [('张三', 'A', 85), ('李四', 'B', 92), ('王五', 'A', 78), ('赵六', 'A', 88)]
print(f"\n多级数据: {students_multi}")

# Lambda多级排序
lambda_multi = sorted(students_multi, key=lambda x: (x[1], -x[2]))
print(f"Lambda多级: {lambda_multi}")

# operator多级排序
operator_multi = sorted(students_multi, key=operator.itemgetter(1, 2))
print(f"operator多级: {operator_multi}")

# 属性排序
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __repr__(self):
        return f"Student('{self.name}', {self.score})"

student_objects = [
    Student('张三', 85),
    Student('李四', 92),
    Student('王五', 78),
    Student('赵六', 88)
]

# 使用lambda访问属性
lambda_attr = sorted(student_objects, key=lambda x: x.score, reverse=True)
print(f"\nLambda属性排序: {lambda_attr}")

# 使用operator.attrgetter
operator_attr = sorted(student_objects, key=operator.attrgetter('score'), reverse=True)
print(f"operator属性排序: {operator_attr}")
print()

# 11. 实际应用案例
print("=== 11. 实际应用案例 ===")

# 案例1：文件排序
files = [
    {'name': 'document.pdf', 'size': 1024000, 'modified': '2023-12-01'},
    {'name': 'image.jpg', 'size': 2048000, 'modified': '2023-12-03'},
    {'name': 'script.py', 'size': 5120, 'modified': '2023-12-02'},
    {'name': 'data.csv', 'size': 512000, 'modified': '2023-11-30'}
]

print("文件排序案例：")

# 按文件大小排序
size_sorted = sorted(files, key=lambda x: x['size'], reverse=True)
print("按大小排序：")
for file in size_sorted:
    size_mb = file['size'] / 1024 / 1024
    print(f"  {file['name']}: {size_mb:.2f} MB")

# 按修改时间排序
time_sorted = sorted(files, key=lambda x: datetime.strptime(x['modified'], '%Y-%m-%d'))
print("\n按修改时间排序：")
for file in time_sorted:
    print(f"  {file['name']}: {file['modified']}")

# 按文件类型和大小排序
type_size_sorted = sorted(files, key=lambda x: (x['name'].split('.')[-1], -x['size']))
print("\n按类型和大小排序：")
for file in type_size_sorted:
    file_type = file['name'].split('.')[-1]
    print(f"  {file['name']}: {file_type}类型, {file['size']}字节")

# 案例2：成绩排名
class_scores = [
    {'student': '张三', 'math': 85, 'english': 92, 'science': 78},
    {'student': '李四', 'math': 92, 'english': 88, 'science': 95},
    {'student': '王五', 'math': 78, 'english': 85, 'science': 82},
    {'student': '赵六', 'math': 88, 'english': 90, 'science': 87}
]

print("\n成绩排名案例：")

# 按总分排序
total_sorted = sorted(class_scores, 
                     key=lambda x: x['math'] + x['english'] + x['science'], 
                     reverse=True)
print("按总分排名：")
for i, student in enumerate(total_sorted, 1):
    total = student['math'] + student['english'] + student['science']
    print(f"  {i}. {student['student']}: 总分{total}")

# 按平均分排序
avg_sorted = sorted(class_scores,
                   key=lambda x: (x['math'] + x['english'] + x['science']) / 3,
                   reverse=True)
print("\n按平均分排名：")
for i, student in enumerate(avg_sorted, 1):
    avg = (student['math'] + student['english'] + student['science']) / 3
    print(f"  {i}. {student['student']}: 平均分{avg:.1f}")

# 按单科最高分排序
max_subject_sorted = sorted(class_scores,
                           key=lambda x: max(x['math'], x['english'], x['science']),
                           reverse=True)
print("\n按单科最高分排名：")
for i, student in enumerate(max_subject_sorted, 1):
    max_score = max(student['math'], student['english'], student['science'])
    print(f"  {i}. {student['student']}: 最高分{max_score}")
print()

# 12. 最佳实践和注意事项
print("=== 12. 最佳实践和注意事项 ===")
print("Lambda排序的优点：")
print("✓ 语法简洁，适合简单的key函数")
print("✓ 可以直接在排序调用中定义")
print("✓ 适合一次性使用的排序规则")
print("✓ 支持复杂的排序逻辑")
print()
print("使用注意事项：")
print("⚠ 复杂逻辑考虑使用普通函数")
print("⚠ 性能敏感场景考虑operator模块")
print("⚠ 多级排序使用元组key")
print("⚠ 注意排序的稳定性")
print()
print("选择建议：")
print("• 简单排序：直接使用sorted()")
print("• 单一条件：使用lambda key")
print("• 多级排序：使用元组key")
print("• 复杂逻辑：定义专门的key函数")
print("• 性能优先：使用operator模块")
print("• 就地排序：使用list.sort()")
print()
print("常见排序模式：")
print("• 数值排序：key=lambda x: x")
print("• 长度排序：key=lambda x: len(x)")
print("• 属性排序：key=lambda x: x.attr")
print("• 索引排序：key=lambda x: x[index]")
print("• 绝对值排序：key=lambda x: abs(x)")
print("• 多级排序：key=lambda x: (x.a, x.b)")
print("• 反向排序：reverse=True")

if __name__ == "__main__":
    print("\n=== Lambda表达式与排序函数学习完成 ===")
    print("排序是数据处理中的重要操作")
    print("Lambda表达式让自定义排序规则变得简单")
    print("下一步：学习Lambda表达式的高级用法")