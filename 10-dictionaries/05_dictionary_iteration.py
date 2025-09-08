#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字典遍历 - 字典遍历和迭代方法

学习目标：
1. 掌握字典的各种遍历方式
2. 了解字典迭代的性能特点
3. 学会在遍历中安全地修改字典
4. 掌握字典的排序和过滤技巧

作者：Python学习教程
日期：2024年
"""

print("=" * 50)
print("字典遍历 - 字典遍历和迭代方法")
print("=" * 50)

# 创建示例字典
students = {
    "张三": {"age": 20, "grade": 85, "major": "计算机"},
    "李四": {"age": 21, "grade": 92, "major": "数学"},
    "王五": {"age": 19, "grade": 78, "major": "物理"},
    "赵六": {"age": 22, "grade": 88, "major": "化学"},
    "孙七": {"age": 20, "grade": 95, "major": "计算机"}
}

print(f"学生信息: {students}")

# 1. 遍历键（默认方式）
print("\n1. 遍历键（默认方式）")
print("-" * 30)

print("方式1 - 直接遍历字典:")
for name in students:
    print(f"  学生: {name}")

print("\n方式2 - 显式遍历键:")
for name in students.keys():
    print(f"  学生: {name}, 年龄: {students[name]['age']}")

# 2. 遍历值
print("\n2. 遍历值")
print("-" * 30)

print("遍历所有学生信息:")
for info in students.values():
    print(f"  年龄: {info['age']}, 成绩: {info['grade']}, 专业: {info['major']}")

# 3. 遍历键值对
print("\n3. 遍历键值对")
print("-" * 30)

print("遍历学生姓名和信息:")
for name, info in students.items():
    print(f"  {name}: 年龄{info['age']}, 成绩{info['grade']}, 专业{info['major']}")

# 4. 带索引的遍历
print("\n4. 带索引的遍历")
print("-" * 30)

print("带序号的学生列表:")
for index, (name, info) in enumerate(students.items(), 1):
    print(f"  {index}. {name} - 成绩: {info['grade']}")

# 5. 条件遍历和过滤
print("\n5. 条件遍历和过滤")
print("-" * 30)

# 找出成绩优秀的学生（>= 90分）
print("成绩优秀的学生（>= 90分）:")
for name, info in students.items():
    if info['grade'] >= 90:
        print(f"  {name}: {info['grade']}分")

# 找出计算机专业的学生
print("\n计算机专业的学生:")
for name, info in students.items():
    if info['major'] == '计算机':
        print(f"  {name}: 年龄{info['age']}, 成绩{info['grade']}")

# 6. 字典推导式遍历
print("\n6. 字典推导式遍历")
print("-" * 30)

# 提取成绩信息
grades_only = {name: info['grade'] for name, info in students.items()}
print(f"成绩字典: {grades_only}")

# 过滤高分学生
high_achievers = {name: info for name, info in students.items() if info['grade'] >= 85}
print(f"高分学生: {high_achievers}")

# 转换数据格式
age_groups = {name: '成年' if info['age'] >= 20 else '未成年' for name, info in students.items()}
print(f"年龄分组: {age_groups}")

# 7. 排序遍历
print("\n7. 排序遍历")
print("-" * 30)

# 按键排序
print("按姓名排序:")
for name in sorted(students.keys()):
    print(f"  {name}: {students[name]['grade']}分")

# 按值排序（按成绩）
print("\n按成绩排序（从高到低）:")
sorted_by_grade = sorted(students.items(), key=lambda x: x[1]['grade'], reverse=True)
for name, info in sorted_by_grade:
    print(f"  {name}: {info['grade']}分")

# 按年龄排序
print("\n按年龄排序（从小到大）:")
sorted_by_age = sorted(students.items(), key=lambda x: x[1]['age'])
for name, info in sorted_by_age:
    print(f"  {name}: {info['age']}岁")

# 8. 嵌套字典遍历
print("\n8. 嵌套字典遍历")
print("-" * 30)

# 创建更复杂的嵌套结构
company = {
    "技术部": {
        "经理": {"姓名": "张经理", "薪资": 25000, "下属": ["李开发", "王测试"]},
        "员工": {
            "李开发": {"薪资": 15000, "技能": ["Python", "Java"]},
            "王测试": {"薪资": 12000, "技能": ["测试", "自动化"]}
        }
    },
    "销售部": {
        "经理": {"姓名": "陈经理", "薪资": 20000, "下属": ["刘销售"]},
        "员工": {
            "刘销售": {"薪资": 10000, "技能": ["销售", "沟通"]}
        }
    }
}

print("公司组织结构遍历:")
for dept_name, dept_info in company.items():
    print(f"\n{dept_name}:")
    print(f"  经理: {dept_info['经理']['姓名']} (薪资: {dept_info['经理']['薪资']})")
    print(f"  员工:")
    for emp_name, emp_info in dept_info['员工'].items():
        skills = ', '.join(emp_info['技能'])
        print(f"    {emp_name}: 薪资{emp_info['薪资']}, 技能[{skills}]")

# 9. 安全的遍历修改
print("\n9. 安全的遍历修改")
print("-" * 30)

# 创建测试字典
scores = {"语文": 85, "数学": 78, "英语": 92, "物理": 88, "化学": 76}
print(f"原始成绩: {scores}")

# 错误的做法：在遍历时直接修改字典
# for subject, score in scores.items():
#     if score < 80:
#         del scores[subject]  # 这会导致RuntimeError

# 正确的做法1：先收集要删除的键
to_remove = []
for subject, score in scores.items():
    if score < 80:
        to_remove.append(subject)

for subject in to_remove:
    del scores[subject]

print(f"删除低分科目后: {scores}")

# 正确的做法2：创建新字典
scores2 = {"语文": 85, "数学": 78, "英语": 92, "物理": 88, "化学": 76}
filtered_scores = {subject: score for subject, score in scores2.items() if score >= 80}
print(f"过滤后的成绩: {filtered_scores}")

# 正确的做法3：使用copy()遍历
scores3 = {"语文": 85, "数学": 78, "英语": 92, "物理": 88, "化学": 76}
for subject, score in scores3.copy().items():
    if score < 80:
        del scores3[subject]
print(f"使用copy()删除后: {scores3}")

# 10. 多字典同时遍历
print("\n10. 多字典同时遍历")
print("-" * 30)

# 创建多个相关字典
names = {1: "张三", 2: "李四", 3: "王五"}
ages = {1: 20, 2: 21, 3: 19}
grades = {1: 85, 2: 92, 3: 78}

print("学生综合信息:")
for student_id in names:
    if student_id in ages and student_id in grades:
        print(f"  ID{student_id}: {names[student_id]}, {ages[student_id]}岁, {grades[student_id]}分")

# 使用zip()同时遍历多个字典的值
print("\n使用zip()遍历:")
for name, age, grade in zip(names.values(), ages.values(), grades.values()):
    print(f"  {name}: {age}岁, {grade}分")

# 11. 字典遍历的性能考虑
print("\n11. 字典遍历的性能考虑")
print("-" * 30)

import time

# 创建大字典
large_dict = {f"key_{i}": f"value_{i}" for i in range(100000)}

# 测试不同遍历方式的性能
start = time.time()
for key in large_dict:
    pass
keys_time = time.time() - start

start = time.time()
for value in large_dict.values():
    pass
values_time = time.time() - start

start = time.time()
for key, value in large_dict.items():
    pass
items_time = time.time() - start

print(f"遍历键耗时: {keys_time:.6f}秒")
print(f"遍历值耗时: {values_time:.6f}秒")
print(f"遍历键值对耗时: {items_time:.6f}秒")

# 12. 实际应用示例
print("\n12. 实际应用示例")
print("-" * 30)

# 数据统计和分析
sales_data = {
    "2023-01": {"revenue": 50000, "orders": 120, "customers": 80},
    "2023-02": {"revenue": 55000, "orders": 135, "customers": 90},
    "2023-03": {"revenue": 48000, "orders": 110, "customers": 75},
    "2023-04": {"revenue": 62000, "orders": 150, "customers": 95}
}

print("销售数据分析:")
total_revenue = 0
total_orders = 0
total_customers = 0

for month, data in sales_data.items():
    total_revenue += data['revenue']
    total_orders += data['orders']
    total_customers += data['customers']
    avg_order_value = data['revenue'] / data['orders']
    print(f"  {month}: 收入{data['revenue']}, 订单{data['orders']}, 平均订单价值{avg_order_value:.2f}")

print(f"\n总计: 收入{total_revenue}, 订单{total_orders}, 客户{total_customers}")
print(f"平均月收入: {total_revenue/len(sales_data):.2f}")

# 找出最佳和最差月份
best_month = max(sales_data.items(), key=lambda x: x[1]['revenue'])
worst_month = min(sales_data.items(), key=lambda x: x[1]['revenue'])
print(f"最佳月份: {best_month[0]} (收入: {best_month[1]['revenue']})")
print(f"最差月份: {worst_month[0]} (收入: {worst_month[1]['revenue']})")

# 13. 字典遍历的高级技巧
print("\n13. 字典遍历的高级技巧")
print("-" * 30)

# 使用itertools进行高级遍历
from itertools import islice, chain

# 只遍历前3个元素
print("前3个学生:")
for name, info in islice(students.items(), 3):
    print(f"  {name}: {info['grade']}分")

# 链式遍历多个字典
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print("\n链式遍历:")
for key, value in chain(dict1.items(), dict2.items()):
    print(f"  {key}: {value}")

# 分组遍历
from itertools import groupby

# 按专业分组学生
students_by_major = {}
for name, info in students.items():
    major = info['major']
    if major not in students_by_major:
        students_by_major[major] = []
    students_by_major[major].append((name, info['grade']))

print("\n按专业分组:")
for major, student_list in students_by_major.items():
    print(f"  {major}专业:")
    for name, grade in student_list:
        print(f"    {name}: {grade}分")

print("\n" + "=" * 50)
print("字典遍历方法总结：")
print("1. for key in dict - 遍历键")
print("2. for value in dict.values() - 遍历值")
print("3. for key, value in dict.items() - 遍历键值对")
print("4. enumerate() - 带索引遍历")
print("5. sorted() - 排序遍历")
print("6. 字典推导式 - 过滤和转换")
print("7. 安全修改 - 使用copy()或收集键")
print("=" * 50)

if __name__ == "__main__":
    print("\n程序执行完成！")
    print("请尝试修改代码，练习不同的字典遍历技巧。")