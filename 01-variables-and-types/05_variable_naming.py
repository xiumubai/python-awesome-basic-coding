#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第五课：变量命名规范

学习目标：
1. 掌握Python变量命名的基本规则
2. 了解Python命名约定（PEP 8）
3. 学会选择有意义的变量名
4. 避免常见的命名错误
5. 掌握不同类型变量的命名风格
6. 了解命名的最佳实践

作者：Python基础教程
日期：2024年
"""

print("=" * 50)
print("第五课：变量命名规范")
print("=" * 50)

# 1. Python变量命名的基本规则
print("\n1. Python变量命名的基本规则")
print("-" * 30)
print("必须遵守的规则：")
print("1. 只能包含字母、数字和下划线")
print("2. 不能以数字开头")
print("3. 区分大小写")
print("4. 不能使用Python关键字")
print("5. 不能包含空格")

# 演示有效的变量名
print("\n有效的变量名示例：")
valid_names = [
    "name", "age", "user_name", "firstName", "_private", 
    "count1", "MAX_SIZE", "is_valid", "data_2024", "__special__"
]

for name in valid_names:
    print(f"✓ {name} - 有效")

# 演示无效的变量名（注释形式，因为无法实际使用）
print("\n无效的变量名示例：")
invalid_examples = [
    "2name - 不能以数字开头",
    "user-name - 不能包含连字符",
    "user name - 不能包含空格",
    "class - 是Python关键字",
    "for - 是Python关键字",
    "user@name - 不能包含特殊字符"
]

for example in invalid_examples:
    print(f"✗ {example}")

# 2. Python关键字
print("\n2. Python关键字（不能用作变量名）")
print("-" * 30)
import keyword
print("Python关键字列表：")
keywords = keyword.kwlist
for i, kw in enumerate(keywords, 1):
    print(f"{kw:12}", end="")
    if i % 5 == 0:  # 每5个换行
        print()
print()  # 最后换行

# 检查是否为关键字的函数
print("\n检查是否为关键字：")
test_words = ["name", "class", "variable", "def", "my_var"]
for word in test_words:
    is_keyword = keyword.iskeyword(word)
    status = "是关键字" if is_keyword else "不是关键字"
    print(f"'{word}' {status}")

# 3. 命名约定（PEP 8风格指南）
print("\n3. 命名约定（PEP 8风格指南）")
print("-" * 30)
print("Python官方推荐的命名风格：")

# 变量和函数名：小写字母，用下划线分隔
print("\n变量和函数名：snake_case（蛇形命名法）")
user_name = "张三"  # 推荐
user_age = 25      # 推荐
is_student = True  # 推荐
total_count = 100  # 推荐
print(f"user_name = '{user_name}'")
print(f"user_age = {user_age}")
print(f"is_student = {is_student}")
print(f"total_count = {total_count}")

# 常量：全大写字母，用下划线分隔
print("\n常量：UPPER_CASE（全大写）")
MAX_SIZE = 1000
DEFAULT_TIMEOUT = 30
PI = 3.14159
DATABASE_URL = "localhost:5432"
print(f"MAX_SIZE = {MAX_SIZE}")
print(f"DEFAULT_TIMEOUT = {DEFAULT_TIMEOUT}")
print(f"PI = {PI}")
print(f"DATABASE_URL = '{DATABASE_URL}'")

# 类名：首字母大写的驼峰命名法
print("\n类名：PascalCase（帕斯卡命名法）")
print("示例：User, StudentInfo, DatabaseConnection, HttpRequest")

# 私有变量：以下划线开头
print("\n私有变量：以下划线开头")
_private_var = "这是私有变量"  # 单下划线：内部使用
__very_private = "这是非常私有的变量"  # 双下划线：名称改写
print(f"_private_var = '{_private_var}'")
print(f"__very_private = '{__very_private}'")

# 4. 有意义的变量名
print("\n4. 有意义的变量名")
print("-" * 30)
print("好的变量名应该：")
print("1. 描述变量的用途")
print("2. 易于理解和记忆")
print("3. 避免缩写和简写")
print("4. 使用完整的单词")

# 对比示例：不好的命名 vs 好的命名
print("\n命名对比示例：")
print("不好的命名 -> 好的命名")
print("-" * 40)

# 不好的命名示例
print("❌ 不好的命名：")
a = 25                    # 不清楚含义
n = "张三"                # 太简短
temp = 36.5              # 模糊不清
data = [1, 2, 3, 4, 5]   # 太泛泛
flag = True              # 不明确用途

print(f"a = {a}")
print(f"n = '{n}'")
print(f"temp = {temp}")
print(f"data = {data}")
print(f"flag = {flag}")

# 好的命名示例
print("\n✅ 好的命名：")
student_age = 25                    # 清楚表示学生年龄
student_name = "张三"               # 明确是学生姓名
body_temperature = 36.5             # 明确是体温
test_scores = [1, 2, 3, 4, 5]      # 明确是测试分数
is_login_successful = True          # 明确表示登录是否成功

print(f"student_age = {student_age}")
print(f"student_name = '{student_name}'")
print(f"body_temperature = {body_temperature}")
print(f"test_scores = {test_scores}")
print(f"is_login_successful = {is_login_successful}")

# 5. 不同类型变量的命名风格
print("\n5. 不同类型变量的命名风格")
print("-" * 30)

# 布尔变量：使用is_, has_, can_, should_等前缀
print("布尔变量命名：")
is_active = True
has_permission = False
can_edit = True
should_save = False
is_empty = True
has_error = False

boolean_vars = {
    "is_active": is_active,
    "has_permission": has_permission,
    "can_edit": can_edit,
    "should_save": should_save,
    "is_empty": is_empty,
    "has_error": has_error
}

for name, value in boolean_vars.items():
    print(f"  {name} = {value}")

# 计数器变量
print("\n计数器变量命名：")
user_count = 100
total_items = 50
max_attempts = 3
current_index = 0
remaining_time = 30

counter_vars = {
    "user_count": user_count,
    "total_items": total_items,
    "max_attempts": max_attempts,
    "current_index": current_index,
    "remaining_time": remaining_time
}

for name, value in counter_vars.items():
    print(f"  {name} = {value}")

# 集合类型变量：使用复数形式
print("\n集合类型变量命名（使用复数）：")
students = ["张三", "李四", "王五"]
scores = [85, 92, 78]
user_ids = [1001, 1002, 1003]
file_names = ["data.txt", "config.json", "log.csv"]

collection_vars = {
    "students": students,
    "scores": scores,
    "user_ids": user_ids,
    "file_names": file_names
}

for name, value in collection_vars.items():
    print(f"  {name} = {value}")

# 6. 避免的命名方式
print("\n6. 应该避免的命名方式")
print("-" * 30)
print("❌ 应该避免：")
print("1. 单字母变量名（除了循环计数器）")
print("2. 数字结尾的变量名（如data1, data2）")
print("3. 拼音命名")
print("4. 过长的变量名")
print("5. 容易混淆的名称")
print("6. 使用内置函数名")

# 避免使用内置函数名
print("\n避免使用内置函数名作为变量名：")
builtin_names = ["list", "dict", "str", "int", "float", "len", "max", "min", "sum", "type"]
print("常见的内置函数名（不要用作变量名）：")
for name in builtin_names:
    print(f"  {name}", end="")
print()

# 正确的做法
print("\n✅ 正确的做法：")
student_list = ["张三", "李四"]      # 而不是 list = [...]
user_dict = {"name": "张三"}        # 而不是 dict = {...}
name_string = "Hello"               # 而不是 str = "Hello"
age_integer = 25                    # 而不是 int = 25
print(f"student_list = {student_list}")
print(f"user_dict = {user_dict}")
print(f"name_string = '{name_string}'")
print(f"age_integer = {age_integer}")

# 7. 上下文相关的命名
print("\n7. 上下文相关的命名")
print("-" * 30)
print("在不同的上下文中，选择合适的变量名：")

# 文件操作上下文
print("\n文件操作上下文：")
file_path = "/path/to/file.txt"
file_content = "文件内容"
file_size = 1024
file_extension = ".txt"
print(f"file_path = '{file_path}'")
print(f"file_content = '{file_content}'")
print(f"file_size = {file_size}")
print(f"file_extension = '{file_extension}'")

# 网络请求上下文
print("\n网络请求上下文：")
request_url = "https://api.example.com"
response_code = 200
response_data = {"status": "success"}
request_timeout = 30
print(f"request_url = '{request_url}'")
print(f"response_code = {response_code}")
print(f"response_data = {response_data}")
print(f"request_timeout = {request_timeout}")

# 数据库操作上下文
print("\n数据库操作上下文：")
database_connection = "connection_object"
table_name = "users"
query_result = "查询结果"
record_count = 100
print(f"database_connection = '{database_connection}'")
print(f"table_name = '{table_name}'")
print(f"query_result = '{query_result}'")
print(f"record_count = {record_count}")

# 8. 循环变量的命名
print("\n8. 循环变量的命名")
print("-" * 30)
print("循环变量的命名建议：")

# 简单循环：可以使用单字母
print("\n简单数值循环：")
for i in range(3):
    print(f"  循环次数：{i + 1}")

# 遍历有意义的集合：使用描述性名称
print("\n遍历集合时使用描述性名称：")
student_names = ["张三", "李四", "王五"]
for student_name in student_names:
    print(f"  学生：{student_name}")

print("\n遍历字典：")
student_grades = {"张三": 85, "李四": 92, "王五": 78}
for student_name, grade in student_grades.items():
    print(f"  {student_name}的成绩：{grade}")

# 嵌套循环：使用有意义的名称
print("\n嵌套循环使用有意义的名称：")
classes = ["一班", "二班"]
for class_name in classes:
    print(f"  班级：{class_name}")
    for student_name in ["学生A", "学生B"]:
        print(f"    学生：{student_name}")

# 9. 临时变量的命名
print("\n9. 临时变量的命名")
print("-" * 30)
print("即使是临时变量，也应该有清晰的名称：")

# 交换变量
print("\n变量交换：")
first_number = 10
second_number = 20
print(f"交换前：first_number = {first_number}, second_number = {second_number}")

# 使用临时变量交换
temp_value = first_number
first_number = second_number
second_number = temp_value
print(f"交换后：first_number = {first_number}, second_number = {second_number}")

# 计算中间结果
print("\n计算中间结果：")
base_price = 100
tax_rate = 0.1
discount_rate = 0.05

tax_amount = base_price * tax_rate
discount_amount = base_price * discount_rate
final_price = base_price + tax_amount - discount_amount

print(f"基础价格：{base_price}")
print(f"税费：{tax_amount}")
print(f"折扣：{discount_amount}")
print(f"最终价格：{final_price}")

# 10. 命名的最佳实践总结
print("\n10. 命名的最佳实践总结")
print("-" * 30)
print("✅ 好的命名实践：")
print("1. 使用完整的英文单词")
print("2. 名称要能表达变量的用途")
print("3. 保持一致的命名风格")
print("4. 避免使用缩写")
print("5. 使用动词+名词的组合描述动作")
print("6. 布尔变量使用is/has/can等前缀")
print("7. 集合使用复数形式")
print("8. 常量使用全大写")
print("9. 私有变量使用下划线前缀")
print("10. 避免使用内置函数名")

# 实际应用示例
print("\n实际应用示例：")
print("一个学生管理系统的变量命名：")

# 学生信息
student_id = "S001"
student_name = "张三"
student_age = 20
student_grade = "大二"
is_student_active = True
student_courses = ["数学", "英语", "计算机"]
student_scores = {"数学": 85, "英语": 92, "计算机": 88}

# 系统配置
MAX_STUDENTS_PER_CLASS = 30
DEFAULT_COURSE_CREDITS = 3
SYSTEM_VERSION = "1.0.0"

# 操作状态
is_data_loaded = True
has_unsaved_changes = False
can_modify_grades = True
current_user_role = "teacher"

print(f"学生ID：{student_id}")
print(f"学生姓名：{student_name}")
print(f"学生年龄：{student_age}")
print(f"学生年级：{student_grade}")
print(f"学生状态：{'活跃' if is_student_active else '非活跃'}")
print(f"选修课程：{student_courses}")
print(f"课程成绩：{student_scores}")
print(f"\n系统配置：")
print(f"每班最大学生数：{MAX_STUDENTS_PER_CLASS}")
print(f"默认课程学分：{DEFAULT_COURSE_CREDITS}")
print(f"系统版本：{SYSTEM_VERSION}")
print(f"\n操作状态：")
print(f"数据已加载：{is_data_loaded}")
print(f"有未保存更改：{has_unsaved_changes}")
print(f"可以修改成绩：{can_modify_grades}")
print(f"当前用户角色：{current_user_role}")

# 11. 练习题
print("\n11. 练习题")
print("-" * 30)
print("练习1：为以下场景选择合适的变量名")
print("  - 存储用户的电子邮件地址")
print("  - 判断文件是否存在")
print("  - 存储购物车中的商品列表")
print("  - 记录最大重试次数")
print("  - 存储当前页面的URL")

print("\n练习2：指出以下变量名的问题并提供改进建议")
problematic_names = [
    "a = 25",
    "list = [1, 2, 3]",
    "userName = '张三'",
    "data1 = 'info'",
    "flag = True"
]

for name in problematic_names:
    print(f"  {name}")

print("\n练习3：为一个图书管理系统设计变量名")
print("  需要存储：书名、作者、ISBN、价格、是否可借、借阅者列表")

# 练习答案示例
print("\n练习答案示例：")
print("练习1答案：")
user_email = "user@example.com"
is_file_exists = True
shopping_cart_items = ["商品1", "商品2"]
max_retry_attempts = 3
current_page_url = "https://example.com/page"

print(f"  user_email = '{user_email}'")
print(f"  is_file_exists = {is_file_exists}")
print(f"  shopping_cart_items = {shopping_cart_items}")
print(f"  max_retry_attempts = {max_retry_attempts}")
print(f"  current_page_url = '{current_page_url}'")

print("\n练习3答案：")
book_title = "Python编程入门"
book_author = "张作者"
book_isbn = "978-1234567890"
book_price = 59.99
is_book_available = True
borrower_list = ["借阅者1", "借阅者2"]

print(f"  book_title = '{book_title}'")
print(f"  book_author = '{book_author}'")
print(f"  book_isbn = '{book_isbn}'")
print(f"  book_price = {book_price}")
print(f"  is_book_available = {is_book_available}")
print(f"  borrower_list = {borrower_list}")

print("\n=" * 50)
print("第五课学习完成！")
print("良好的命名习惯是编程的基础")
print("下一课将进行综合练习")
print("=" * 50)

# 运行这个文件的方法：
# 在终端中输入：python 05_variable_naming.py
# 或者在IDE中直接运行