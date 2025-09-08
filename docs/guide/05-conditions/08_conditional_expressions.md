# 条件表达式（三元运算符）

## 概述

条件表达式，也称为三元运算符，是Python中一种简洁的条件判断语法。它允许我们在一行代码中完成简单的条件判断和值选择，使代码更加简洁和易读。

### 基本语法

```python
# 条件表达式的基本语法
# 值1 if 条件 else 值2

# 如果条件为True，返回值1；如果条件为False，返回值2
result = value_if_true if condition else value_if_false
```

### 执行顺序

条件表达式的执行顺序是：
1. 首先计算中间的条件表达式
2. 如果条件为True，返回if前面的值
3. 如果条件为False，返回else后面的值

## 基本示例

```python
# 基本的条件表达式示例
print("=== 基本条件表达式 ===")

# 1. 简单的数值判断
age = 18
status = "成年人" if age >= 18 else "未成年人"
print(f"年龄 {age}，状态：{status}")

# 2. 比较传统if-else写法
# 传统写法
if age >= 18:
    status_traditional = "成年人"
else:
    status_traditional = "未成年人"

# 条件表达式写法（更简洁）
status_ternary = "成年人" if age >= 18 else "未成年人"

print(f"传统写法结果：{status_traditional}")
print(f"条件表达式结果：{status_ternary}")

# 3. 数值处理
number = -5
absolute_value = number if number >= 0 else -number
print(f"数字 {number} 的绝对值：{absolute_value}")

# 4. 字符串处理
name = ""
display_name = name if name else "匿名用户"
print(f"显示名称：{display_name}")

name = "Alice"
display_name = name if name else "匿名用户"
print(f"显示名称：{display_name}")
```

## 嵌套条件表达式

```python
# 嵌套条件表达式
print("\n=== 嵌套条件表达式 ===")

# 1. 多级条件判断
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"
print(f"分数 {score}，等级：{grade}")

# 2. 更复杂的嵌套
temperature = 25
weather = "炎热" if temperature > 30 else "温暖" if temperature > 20 else "凉爽" if temperature > 10 else "寒冷"
print(f"温度 {temperature}°C，天气：{weather}")

# 3. 嵌套的可读性考虑
# 不推荐：过于复杂的嵌套
complex_result = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"

# 推荐：使用函数提高可读性
def get_grade(score):
    """根据分数获取等级"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(f"分数 {score}，等级：{get_grade(score)}")
```

## 在函数中的应用

### 1. 函数返回值

```python
# 在函数中使用条件表达式
print("\n=== 函数中的条件表达式 ===")

# 1. 简化函数返回值
def is_even(number):
    """判断数字是否为偶数"""
    return True if number % 2 == 0 else False
    # 更简洁的写法：return number % 2 == 0

def get_max(a, b):
    """获取两个数中的最大值"""
    return a if a > b else b

def safe_divide(a, b):
    """安全除法，避免除零错误"""
    return a / b if b != 0 else 0

# 测试函数
print(f"5 是偶数：{is_even(5)}")
print(f"6 是偶数：{is_even(6)}")
print(f"max(10, 7) = {get_max(10, 7)}")
print(f"safe_divide(10, 2) = {safe_divide(10, 2)}")
print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")
```

### 2. 参数默认值和验证

```python
# 2. 参数处理和验证
def greet(name, title=None):
    """问候函数，支持可选的称谓"""
    full_name = f"{title} {name}" if title else name
    return f"你好，{full_name}！"

def calculate_discount(price, is_member, age):
    """计算折扣价格"""
    # 会员或老年人享受折扣
    discount_rate = 0.1 if is_member or age >= 65 else 0
    final_price = price * (1 - discount_rate)
    return final_price

def validate_email(email):
    """简单的邮箱验证"""
    return "有效邮箱" if "@" in email and "." in email else "无效邮箱"

# 测试参数处理
print(f"\n{greet('张三')}")
print(f"{greet('李四', '先生')}")
print(f"普通用户价格：{calculate_discount(100, False, 30)}")
print(f"会员价格：{calculate_discount(100, True, 30)}")
print(f"老年人价格：{calculate_discount(100, False, 70)}")
print(f"邮箱验证：{validate_email('user@example.com')}")
print(f"邮箱验证：{validate_email('invalid-email')}")
```

## 在列表推导式中的应用

```python
# 在列表推导式中使用条件表达式
print("\n=== 列表推导式中的条件表达式 ===")

# 1. 基本的列表处理
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 将奇数转换为负数，偶数保持不变
processed_numbers = [num if num % 2 == 0 else -num for num in numbers]
print(f"原始数字：{numbers}")
print(f"处理后：{processed_numbers}")

# 2. 字符串处理
words = ["python", "java", "c++", "javascript", "go"]
capitalized = [word.upper() if len(word) <= 4 else word.title() for word in words]
print(f"\n原始单词：{words}")
print(f"处理后：{capitalized}")

# 3. 复杂的数据处理
students_data = [
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 78},
    {"name": "Charlie", "score": 88},
    {"name": "David", "score": 65}
]

# 为每个学生添加等级
students_with_grade = [
    {
        **student,
        "grade": "A" if student["score"] >= 90 else "B" if student["score"] >= 80 else "C"
    }
    for student in students_data
]

print("\n学生成绩和等级：")
for student in students_with_grade:
    print(f"{student['name']}: {student['score']}分 (等级{student['grade']})")
```

## 在字典推导式中的应用

```python
# 在字典推导式中使用条件表达式
print("\n=== 字典推导式中的条件表达式 ===")

# 1. 基本字典处理
original_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# 根据值的奇偶性进行不同处理
processed_dict = {
    key: value * 2 if value % 2 == 0 else value * 3
    for key, value in original_dict.items()
}

print(f"原始字典：{original_dict}")
print(f"处理后：{processed_dict}")

# 2. 配置处理
config = {
    "debug": "true",
    "port": "8080",
    "host": "localhost",
    "timeout": "30"
}

# 转换配置值的类型
typed_config = {
    key: (
        True if value.lower() == "true" else
        False if value.lower() == "false" else
        int(value) if value.isdigit() else
        value
    )
    for key, value in config.items()
}

print(f"\n原始配置：{config}")
print(f"类型转换后：{typed_config}")
for key, value in typed_config.items():
    print(f"{key}: {value} ({type(value).__name__})")
```

## 字符串处理中的应用

```python
# 字符串处理中的条件表达式
print("\n=== 字符串处理中的条件表达式 ===")

# 1. 字符串格式化
def format_name(first_name, last_name=None):
    """格式化姓名"""
    return f"{first_name} {last_name}" if last_name else first_name

def format_phone(phone):
    """格式化电话号码"""
    # 简单的电话号码格式化
    cleaned = phone.replace("-", "").replace(" ", "")
    return f"{cleaned[:3]}-{cleaned[3:6]}-{cleaned[6:]}" if len(cleaned) == 10 else phone

# 2. 文本处理
def truncate_text(text, max_length=50):
    """截断文本"""
    return text if len(text) <= max_length else text[:max_length-3] + "..."

def format_currency(amount, currency="¥"):
    """格式化货币"""
    return f"{currency}{amount:.2f}" if amount >= 0 else f"-{currency}{abs(amount):.2f}"

# 测试字符串处理
print(f"格式化姓名：{format_name('张', '三')}")
print(f"格式化姓名：{format_name('李四')}")
print(f"格式化电话：{format_phone('1234567890')}")
print(f"格式化电话：{format_phone('123-456-7890')}")

long_text = "这是一段很长的文本，用来测试截断功能是否正常工作。"
print(f"截断文本：{truncate_text(long_text, 20)}")
print(f"格式化货币：{format_currency(123.45)}")
print(f"格式化货币：{format_currency(-67.89)}")
```

## 数据处理中的应用

```python
# 数据处理中的条件表达式
print("\n=== 数据处理中的条件表达式 ===")

# 1. 数据清洗
raw_data = ["  Alice  ", "", "Bob", None, "  Charlie", "David  ", ""]

# 清洗数据：去除空白、处理空值
cleaned_data = [
    item.strip() if item and isinstance(item, str) else "Unknown"
    for item in raw_data
    if item is not None
]

print(f"原始数据：{raw_data}")
print(f"清洗后：{cleaned_data}")

# 2. 数据转换
scores = ["95", "invalid", "78", "", "88", "65"]

# 安全的数据转换
valid_scores = [
    int(score) if score.isdigit() else 0
    for score in scores
    if score
]

print(f"\n原始分数：{scores}")
print(f"有效分数：{valid_scores}")

# 3. 配置处理
user_settings = {
    "theme": "dark",
    "notifications": "true",
    "auto_save": "false",
    "language": "",
    "font_size": "14"
}

# 处理用户设置
processed_settings = {
    "theme": user_settings.get("theme", "light"),
    "notifications": user_settings.get("notifications") == "true",
    "auto_save": user_settings.get("auto_save") == "true",
    "language": user_settings.get("language") if user_settings.get("language") else "zh-CN",
    "font_size": int(user_settings.get("font_size", "12")) if user_settings.get("font_size", "12").isdigit() else 12
}

print(f"\n用户设置：{user_settings}")
print(f"处理后设置：{processed_settings}")
```

## 性能考虑和最佳实践

### 1. 性能优化

```python
# 性能考虑
print("\n=== 性能考虑 ===")

import time

# 1. 避免重复计算
def expensive_calculation():
    """模拟耗时计算"""
    time.sleep(0.001)  # 模拟计算时间
    return 42

# ❌ 不好的做法：可能重复计算
def bad_example(condition):
    return expensive_calculation() if condition else expensive_calculation() * 2

# ✅ 好的做法：避免重复计算
def good_example(condition):
    result = expensive_calculation()
    return result if condition else result * 2

# 2. 短路求值的利用
def safe_get_item(lst, index, default=None):
    """安全获取列表元素"""
    return lst[index] if 0 <= index < len(lst) else default

# 测试性能优化
test_list = [1, 2, 3, 4, 5]
print(f"安全获取: index 2 = {safe_get_item(test_list, 2)}, index 10 = {safe_get_item(test_list, 10, 'N/A')}")
```

### 2. 最佳实践指南

```python
# 最佳实践
print("\n=== 最佳实践 ===")

# 1. 简单条件优先使用条件表达式
def get_status(is_active):
    """获取状态"""
    return "激活" if is_active else "未激活"

# 2. 复杂逻辑使用传统if-else
def complex_logic(user_type, score, is_premium):
    """复杂业务逻辑"""
    if user_type == "admin":
        return "管理员权限"
    elif user_type == "premium" or is_premium:
        if score >= 90:
            return "高级会员 - 优秀"
        elif score >= 70:
            return "高级会员 - 良好"
        else:
            return "高级会员 - 一般"
    else:
        return "普通用户"

# 3. 链式条件表达式要适度
def get_grade_simple(score):
    """简单的等级判断"""
    return "A" if score >= 90 else "B" if score >= 80 else "C"

# 4. 可读性优先
def format_file_size(size_bytes):
    """格式化文件大小显示"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"

# 测试最佳实践
print(f"状态：{get_status(True)}")
print(f"复杂逻辑：{complex_logic('premium', 95, True)}")
print(f"等级：{get_grade_simple(85)}")
print(f"文件大小：{format_file_size(2048576)}")
```

## 与lambda函数结合

```python
# 条件表达式与lambda函数结合
print("\n=== 与lambda函数结合 ===")

# 基本的lambda + 条件表达式
abs_func = lambda x: x if x >= 0 else -x
max_func = lambda a, b: a if a > b else b
min_func = lambda a, b: a if a < b else b

# 测试lambda函数
test_numbers = [5, -3, 0, 8, -7]
print("Lambda函数测试:")
for num in test_numbers:
    print(f"abs({num}) = {abs_func(num)}")

print(f"max(5, 3) = {max_func(5, 3)}")
print(f"min(5, 3) = {min_func(5, 3)}")

# 在高阶函数中使用
data = [1, -2, 3, -4, 5, -6]
abs_values = list(map(lambda x: x if x >= 0 else -x, data))
print(f"\n原始数据: {data}")
print(f"绝对值: {abs_values}")
```

## 练习题

### 基础练习

1. **简单条件判断**：编写一个函数，使用条件表达式判断一个数字是正数、负数还是零。

2. **字符串处理**：使用条件表达式创建一个函数，如果字符串长度超过10个字符，则截断并添加"..."，否则返回原字符串。

3. **列表处理**：使用列表推导式和条件表达式，将列表中的偶数乘以2，奇数乘以3。

### 进阶练习

4. **数据验证**：创建一个用户注册验证函数，使用条件表达式检查用户名、邮箱和密码的有效性。

5. **配置处理**：编写一个配置解析器，使用条件表达式将字符串配置转换为适当的Python数据类型。

6. **成绩统计**：使用条件表达式和字典推导式，为学生列表添加等级和奖学金信息。

### 挑战练习

7. **智能推荐系统**：设计一个简单的商品推荐函数，根据用户的购买历史、年龄和会员等级，使用条件表达式计算推荐权重。

8. **数据清洗管道**：创建一个数据清洗函数，使用条件表达式处理各种数据异常情况（空值、格式错误、超出范围等）。

## 学习要点

1. **语法掌握**：熟练掌握条件表达式的基本语法和执行顺序
2. **适用场景**：了解何时使用条件表达式，何时使用传统if-else
3. **可读性平衡**：在简洁性和可读性之间找到平衡点
4. **性能考虑**：避免在条件表达式中进行重复的昂贵计算
5. **最佳实践**：遵循Python的编码规范和最佳实践
6. **实际应用**：在数据处理、配置管理、用户界面等场景中灵活运用

通过掌握条件表达式，你可以编写更加简洁和优雅的Python代码，提高代码的可读性和维护性。