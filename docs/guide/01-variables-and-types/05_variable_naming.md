# 变量命名规范

## 学习目标

通过本节学习，你将掌握：

1. 掌握Python变量命名的基本规则
2. 了解Python命名约定（PEP 8）
3. 学会选择有意义的变量名
4. 避免常见的命名错误
5. 掌握不同类型变量的命名风格
6. 了解命名的最佳实践

## Python变量命名的基本规则

### 必须遵守的规则

1. **只能包含字母、数字和下划线**
2. **不能以数字开头**
3. **区分大小写**
4. **不能使用Python关键字**
5. **不能包含空格**

### 有效的变量名示例

```python
# 有效的变量名
name = "张三"
age = 25
user_name = "zhangsan"
firstName = "三"  # 虽然有效，但不推荐
_private = "私有变量"
count1 = 10
MAX_SIZE = 1000
is_valid = True
data_2024 = [1, 2, 3]
__special__ = "特殊变量"

print(f"姓名：{name}")
print(f"年龄：{age}")
print(f"用户名：{user_name}")
```

### 无效的变量名示例

```python
# 以下是无效的变量名（仅作演示，实际不能使用）
# 2name = "张三"        # ❌ 不能以数字开头
# user-name = "张三"    # ❌ 不能包含连字符
# user name = "张三"    # ❌ 不能包含空格
# class = "一班"        # ❌ 是Python关键字
# for = 10             # ❌ 是Python关键字
# user@name = "张三"    # ❌ 不能包含特殊字符
```

## Python关键字

Python有一些保留的关键字，不能用作变量名：

```python
import keyword

# 查看所有Python关键字
print("Python关键字列表：")
keywords = keyword.kwlist
for i, kw in enumerate(keywords, 1):
    print(f"{kw:12}", end="")
    if i % 5 == 0:  # 每5个换行
        print()
print()

# 检查是否为关键字
test_words = ["name", "class", "variable", "def", "my_var"]
for word in test_words:
    is_keyword = keyword.iskeyword(word)
    status = "是关键字" if is_keyword else "不是关键字"
    print(f"'{word}' {status}")
```

## 命名约定（PEP 8风格指南）

Python官方推荐的命名风格：

### 变量和函数名：snake_case（蛇形命名法）

```python
# 推荐的变量命名方式
user_name = "张三"
user_age = 25
is_student = True
total_count = 100
student_score = 85.5

print(f"用户名：{user_name}")
print(f"年龄：{user_age}")
print(f"是否为学生：{is_student}")
print(f"总数：{total_count}")
print(f"学生分数：{student_score}")
```

### 常量：UPPER_CASE（全大写）

```python
# 常量命名
MAX_SIZE = 1000
DEFAULT_TIMEOUT = 30
PI = 3.14159
DATABASE_URL = "localhost:5432"
APP_VERSION = "1.0.0"

print(f"最大尺寸：{MAX_SIZE}")
print(f"默认超时：{DEFAULT_TIMEOUT}")
print(f"圆周率：{PI}")
print(f"数据库URL：{DATABASE_URL}")
print(f"应用版本：{APP_VERSION}")
```

### 类名：PascalCase（帕斯卡命名法）

```python
# 类名示例（仅作演示）
# class User:          # 用户类
# class StudentInfo:   # 学生信息类
# class DatabaseConnection:  # 数据库连接类
# class HttpRequest:   # HTTP请求类

print("类名使用PascalCase：User, StudentInfo, DatabaseConnection")
```

### 私有变量：以下划线开头

```python
# 私有变量命名
_private_var = "这是私有变量"        # 单下划线：内部使用
__very_private = "这是非常私有的变量"  # 双下划线：名称改写

print(f"私有变量：{_private_var}")
print(f"非常私有的变量：{__very_private}")
```

## 有意义的变量名

好的变量名应该：
1. **描述变量的用途**
2. **易于理解和记忆**
3. **避免缩写和简写**
4. **使用完整的单词**

### 命名对比示例

```python
# ❌ 不好的命名
a = 25                    # 不清楚含义
n = "张三"                # 太简短
temp = 36.5              # 模糊不清
data = [1, 2, 3, 4, 5]   # 太泛泛
flag = True              # 不明确用途

print("不好的命名示例：")
print(f"a = {a}")
print(f"n = '{n}'")
print(f"temp = {temp}")
print(f"data = {data}")
print(f"flag = {flag}")

# ✅ 好的命名
student_age = 25                    # 清楚表示学生年龄
student_name = "张三"               # 明确是学生姓名
body_temperature = 36.5             # 明确是体温
test_scores = [1, 2, 3, 4, 5]      # 明确是测试分数
is_login_successful = True          # 明确表示登录是否成功

print("\n好的命名示例：")
print(f"student_age = {student_age}")
print(f"student_name = '{student_name}'")
print(f"body_temperature = {body_temperature}")
print(f"test_scores = {test_scores}")
print(f"is_login_successful = {is_login_successful}")
```

## 不同类型变量的命名风格

### 布尔变量：使用is_, has_, can_, should_等前缀

```python
# 布尔变量命名
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

print("布尔变量命名示例：")
for name, value in boolean_vars.items():
    print(f"  {name} = {value}")
```

### 计数器变量

```python
# 计数器变量命名
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

print("计数器变量命名示例：")
for name, value in counter_vars.items():
    print(f"  {name} = {value}")
```

### 集合类型变量：使用复数形式

```python
# 集合类型变量命名（使用复数）
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

print("集合类型变量命名示例：")
for name, value in collection_vars.items():
    print(f"  {name} = {value}")
```

## 应该避免的命名方式

### ❌ 应该避免：

1. **单字母变量名**（除了循环计数器）
2. **数字结尾的变量名**（如data1, data2）
3. **拼音命名**
4. **过长的变量名**
5. **容易混淆的名称**
6. **使用内置函数名**

### 避免使用内置函数名

```python
# ❌ 避免使用内置函数名作为变量名
# list = [1, 2, 3]      # 不要这样做
# dict = {"key": "value"}  # 不要这样做
# str = "hello"         # 不要这样做
# int = 25              # 不要这样做

# ✅ 正确的做法
student_list = ["张三", "李四"]      # 而不是 list = [...]
user_dict = {"name": "张三"}        # 而不是 dict = {...}
name_string = "Hello"               # 而不是 str = "Hello"
age_integer = 25                    # 而不是 int = 25

print(f"student_list = {student_list}")
print(f"user_dict = {user_dict}")
print(f"name_string = '{name_string}'")
print(f"age_integer = {age_integer}")
```

## 上下文相关的命名

在不同的上下文中，选择合适的变量名：

### 文件操作上下文

```python
# 文件操作相关变量
file_path = "/path/to/file.txt"
file_content = "文件内容"
file_size = 1024
file_extension = ".txt"
file_name = "document"

print("文件操作上下文：")
print(f"file_path = '{file_path}'")
print(f"file_content = '{file_content}'")
print(f"file_size = {file_size}")
print(f"file_extension = '{file_extension}'")
print(f"file_name = '{file_name}'")
```

### 网络请求上下文

```python
# 网络请求相关变量
request_url = "https://api.example.com"
response_code = 200
response_data = {"status": "success"}
request_timeout = 30
api_key = "your_api_key_here"

print("\n网络请求上下文：")
print(f"request_url = '{request_url}'")
print(f"response_code = {response_code}")
print(f"response_data = {response_data}")
print(f"request_timeout = {request_timeout}")
print(f"api_key = '{api_key}'")
```

### 数据库操作上下文

```python
# 数据库操作相关变量
database_connection = "connection_object"
table_name = "users"
query_result = "查询结果"
record_count = 100
column_names = ["id", "name", "email"]

print("\n数据库操作上下文：")
print(f"database_connection = '{database_connection}'")
print(f"table_name = '{table_name}'")
print(f"query_result = '{query_result}'")
print(f"record_count = {record_count}")
print(f"column_names = {column_names}")
```

## 循环变量的命名

### 简单循环：可以使用单字母

```python
# 简单数值循环
print("简单数值循环：")
for i in range(3):
    print(f"  循环次数：{i + 1}")
```

### 遍历有意义的集合：使用描述性名称

```python
# 遍历集合时使用描述性名称
student_names = ["张三", "李四", "王五"]
print("\n遍历学生名单：")
for student_name in student_names:
    print(f"  学生：{student_name}")

# 遍历字典
student_grades = {"张三": 85, "李四": 92, "王五": 78}
print("\n遍历学生成绩：")
for student_name, grade in student_grades.items():
    print(f"  {student_name}的成绩：{grade}")
```

### 嵌套循环：使用有意义的名称

```python
# 嵌套循环使用有意义的名称
classes = ["一班", "二班"]
print("\n嵌套循环示例：")
for class_name in classes:
    print(f"  班级：{class_name}")
    for student_name in ["学生A", "学生B"]:
        print(f"    学生：{student_name}")
```

## 临时变量的命名

即使是临时变量，也应该有清晰的名称：

```python
# 变量交换
first_number = 10
second_number = 20
print(f"交换前：first_number = {first_number}, second_number = {second_number}")

# 使用临时变量交换
temp_value = first_number
first_number = second_number
second_number = temp_value
print(f"交换后：first_number = {first_number}, second_number = {second_number}")

# 计算中间结果
base_price = 100
tax_rate = 0.1
discount_rate = 0.05

tax_amount = base_price * tax_rate
discount_amount = base_price * discount_rate
final_price = base_price + tax_amount - discount_amount

print(f"\n价格计算：")
print(f"基础价格：{base_price}")
print(f"税费：{tax_amount}")
print(f"折扣：{discount_amount}")
print(f"最终价格：{final_price}")
```

## 实际应用示例

一个学生管理系统的变量命名：

```python
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

print("学生管理系统变量示例：")
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
```

## 命名的最佳实践总结

### ✅ 好的命名实践：

1. **使用完整的英文单词**
2. **名称要能表达变量的用途**
3. **保持一致的命名风格**
4. **避免使用缩写**
5. **使用动词+名词的组合描述动作**
6. **布尔变量使用is/has/can等前缀**
7. **集合使用复数形式**
8. **常量使用全大写**
9. **私有变量使用下划线前缀**
10. **避免使用内置函数名**

## 实践练习

### 练习1：为以下场景选择合适的变量名

```python
# 练习1答案示例
user_email = "user@example.com"          # 存储用户的电子邮件地址
is_file_exists = True                    # 判断文件是否存在
shopping_cart_items = ["商品1", "商品2"]  # 存储购物车中的商品列表
max_retry_attempts = 3                   # 记录最大重试次数
current_page_url = "https://example.com/page"  # 存储当前页面的URL

print("练习1答案：")
print(f"user_email = '{user_email}'")
print(f"is_file_exists = {is_file_exists}")
print(f"shopping_cart_items = {shopping_cart_items}")
print(f"max_retry_attempts = {max_retry_attempts}")
print(f"current_page_url = '{current_page_url}'")
```

### 练习2：图书管理系统变量设计

```python
# 练习2答案：图书管理系统
book_title = "Python编程入门"
book_author = "张作者"
book_isbn = "978-1234567890"
book_price = 59.99
is_book_available = True
borrower_list = ["借阅者1", "借阅者2"]
book_category = "计算机科学"
publication_date = "2024-01-01"
total_pages = 300
is_book_reserved = False

print("\n练习2答案：图书管理系统")
print(f"book_title = '{book_title}'")
print(f"book_author = '{book_author}'")
print(f"book_isbn = '{book_isbn}'")
print(f"book_price = {book_price}")
print(f"is_book_available = {is_book_available}")
print(f"borrower_list = {borrower_list}")
print(f"book_category = '{book_category}'")
print(f"publication_date = '{publication_date}'")
print(f"total_pages = {total_pages}")
print(f"is_book_reserved = {is_book_reserved}")
```

## 完整代码示例

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
变量命名规范演示

学习目标：
1. 掌握Python变量命名的基本规则
2. 了解Python命名约定（PEP 8）
3. 学会选择有意义的变量名
4. 避免常见的命名错误
5. 掌握不同类型变量的命名风格
6. 了解命名的最佳实践
"""

print("=" * 50)
print("变量命名规范")
print("=" * 50)

# 基本命名规则演示
user_name = "张三"  # snake_case
user_age = 25
is_active = True
MAX_SIZE = 1000    # 常量

print(f"用户名：{user_name}")
print(f"年龄：{user_age}")
print(f"是否活跃：{is_active}")
print(f"最大尺寸：{MAX_SIZE}")

# 集合类型命名
students = ["张三", "李四", "王五"]
scores = [85, 92, 78]

print(f"学生列表：{students}")
print(f"分数列表：{scores}")
```

## 运行方法

在终端中运行：
```bash
python 05_variable_naming.py
```

或者在IDE中直接运行该文件。

## 小结

良好的变量命名是编程的基础技能。通过遵循Python的命名约定和最佳实践，你的代码将更加清晰、易读和易维护。记住：

- 使用有意义的名称
- 保持一致的命名风格
- 遵循PEP 8规范
- 避免使用内置函数名
- 根据变量类型选择合适的命名方式

下一节我们将进行综合练习，巩固所学的变量和数据类型知识。