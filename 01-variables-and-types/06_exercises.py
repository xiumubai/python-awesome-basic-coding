#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第六课：综合练习题

本文件包含变量和数据类型相关的综合练习题，
涵盖前面五课的所有知识点：
1. 基本变量定义和赋值
2. 数据类型详解
3. 动态类型特性
4. 类型转换
5. 变量命名规范

练习分为三个难度级别：
- 基础练习：适合初学者
- 进阶练习：需要综合运用知识
- 挑战练习：考验深度理解

作者：Python基础教程
日期：2024年
"""

print("=" * 60)
print("变量和数据类型 - 综合练习题")
print("=" * 60)

# ==================== 基础练习 ====================
print("\n" + "=" * 20 + " 基础练习 " + "=" * 20)

# 练习1：变量定义和赋值
print("\n练习1：变量定义和赋值")
print("-" * 40)
print("任务：定义以下变量并赋予合适的值")
print("1. 学生姓名")
print("2. 学生年龄")
print("3. 学生身高（米）")
print("4. 是否在校")
print("5. 选修课程列表")

print("\n解答：")
# 学生信息变量定义
student_name = "张三"           # 字符串类型
student_age = 20               # 整数类型
student_height = 1.75          # 浮点数类型
is_enrolled = True             # 布尔类型
elective_courses = ["数学", "英语", "计算机"]  # 列表类型

print(f"学生姓名：{student_name} (类型：{type(student_name).__name__})")
print(f"学生年龄：{student_age} (类型：{type(student_age).__name__})")
print(f"学生身高：{student_height}米 (类型：{type(student_height).__name__})")
print(f"是否在校：{is_enrolled} (类型：{type(is_enrolled).__name__})")
print(f"选修课程：{elective_courses} (类型：{type(elective_courses).__name__})")

# 练习2：数据类型识别
print("\n练习2：数据类型识别")
print("-" * 40)
print("任务：识别以下变量的数据类型")

variables_to_check = [
    42,
    3.14,
    "Hello World",
    True,
    [1, 2, 3],
    {"name": "张三"},
    None,
    (1, 2, 3)
]

print("\n解答：")
for i, var in enumerate(variables_to_check, 1):
    print(f"{i}. {repr(var)} -> {type(var).__name__}")

# 练习3：变量重新赋值
print("\n练习3：变量重新赋值")
print("-" * 40)
print("任务：观察变量类型的动态变化")

print("\n解答：")
dynamic_var = 100
print(f"初始值：{dynamic_var} (类型：{type(dynamic_var).__name__})")

dynamic_var = 3.14
print(f"重新赋值：{dynamic_var} (类型：{type(dynamic_var).__name__})")

dynamic_var = "Hello"
print(f"再次赋值：{dynamic_var} (类型：{type(dynamic_var).__name__})")

dynamic_var = True
print(f"最后赋值：{dynamic_var} (类型：{type(dynamic_var).__name__})")

# 练习4：基本类型转换
print("\n练习4：基本类型转换")
print("-" * 40)
print("任务：进行以下类型转换")
print("1. 字符串 '123' 转换为整数")
print("2. 整数 456 转换为字符串")
print("3. 字符串 '3.14' 转换为浮点数")
print("4. 整数 0 转换为布尔值")
print("5. 整数 1 转换为布尔值")

print("\n解答：")
# 类型转换练习
str_to_int = int("123")
print(f"'123' -> {str_to_int} (类型：{type(str_to_int).__name__})")

int_to_str = str(456)
print(f"456 -> '{int_to_str}' (类型：{type(int_to_str).__name__})")

str_to_float = float("3.14")
print(f"'3.14' -> {str_to_float} (类型：{type(str_to_float).__name__})")

zero_to_bool = bool(0)
print(f"0 -> {zero_to_bool} (类型：{type(zero_to_bool).__name__})")

one_to_bool = bool(1)
print(f"1 -> {one_to_bool} (类型：{type(one_to_bool).__name__})")

# 练习5：变量命名规范检查
print("\n练习5：变量命名规范检查")
print("-" * 40)
print("任务：判断以下变量名是否符合Python命名规范")

variable_names = [
    "student_name",      # 正确
    "2student",          # 错误：以数字开头
    "student-name",      # 错误：包含连字符
    "_private_var",      # 正确
    "MAX_SIZE",          # 正确
    "class",             # 错误：关键字
    "studentName",       # 可以，但不推荐（应该用snake_case）
    "student name",      # 错误：包含空格
    "is_valid",          # 正确
    "list",              # 错误：内置函数名
]

print("\n解答：")
import keyword
for name in variable_names:
    issues = []
    
    # 检查是否以数字开头
    if name and name[0].isdigit():
        issues.append("以数字开头")
    
    # 检查是否包含非法字符
    if not name.replace('_', '').replace('-', '').replace(' ', '').isalnum():
        if '-' in name:
            issues.append("包含连字符")
        if ' ' in name:
            issues.append("包含空格")
    
    # 检查是否为关键字
    if keyword.iskeyword(name):
        issues.append("是Python关键字")
    
    # 检查是否为内置函数名
    builtin_names = ['list', 'dict', 'str', 'int', 'float', 'len', 'max', 'min', 'sum', 'type']
    if name in builtin_names:
        issues.append("是内置函数名")
    
    # 检查命名风格
    if name.replace('_', '').isalnum() and any(c.isupper() for c in name) and '_' not in name and not name.isupper():
        issues.append("建议使用snake_case而非camelCase")
    
    if issues:
        print(f"❌ '{name}' - {', '.join(issues)}")
    else:
        print(f"✅ '{name}' - 符合规范")

# ==================== 进阶练习 ====================
print("\n" + "=" * 20 + " 进阶练习 " + "=" * 20)

# 练习6：用户信息管理系统
print("\n练习6：用户信息管理系统")
print("-" * 40)
print("任务：创建一个简单的用户信息管理系统")
print("要求：")
print("1. 定义用户的基本信息变量")
print("2. 实现用户信息的显示功能")
print("3. 实现用户信息的更新功能")
print("4. 处理不同类型的输入")

print("\n解答：")

# 用户信息变量定义
user_id = 1001
user_name = "李明"
user_email = "liming@example.com"
user_age = 25
user_salary = 8500.50
is_active = True
user_skills = ["Python", "Java", "SQL"]
user_profile = {
    "department": "技术部",
    "position": "软件工程师",
    "join_date": "2023-01-15"
}

def display_user_info():
    """显示用户信息"""
    print(f"\n用户信息：")
    print(f"ID: {user_id}")
    print(f"姓名: {user_name}")
    print(f"邮箱: {user_email}")
    print(f"年龄: {user_age}")
    print(f"薪资: ¥{user_salary}")
    print(f"状态: {'活跃' if is_active else '非活跃'}")
    print(f"技能: {', '.join(user_skills)}")
    print(f"部门: {user_profile['department']}")
    print(f"职位: {user_profile['position']}")
    print(f"入职日期: {user_profile['join_date']}")

def update_user_age(new_age_str):
    """更新用户年龄（带类型转换和验证）"""
    global user_age
    try:
        new_age = int(new_age_str)
        if 18 <= new_age <= 65:
            user_age = new_age
            print(f"年龄更新成功：{user_age}")
        else:
            print(f"年龄无效：{new_age}（应在18-65之间）")
    except ValueError:
        print(f"年龄格式错误：'{new_age_str}'（应为数字）")

def update_user_salary(new_salary_str):
    """更新用户薪资（带类型转换和验证）"""
    global user_salary
    try:
        new_salary = float(new_salary_str)
        if new_salary >= 0:
            user_salary = new_salary
            print(f"薪资更新成功：¥{user_salary}")
        else:
            print(f"薪资无效：{new_salary}（不能为负数）")
    except ValueError:
        print(f"薪资格式错误：'{new_salary_str}'（应为数字）")

# 演示用户信息管理
display_user_info()

print("\n测试信息更新：")
update_user_age("28")
update_user_age("abc")
update_user_age("100")

update_user_salary("9500.75")
update_user_salary("invalid")
update_user_salary("-1000")

display_user_info()

# 练习7：数据类型转换器
print("\n练习7：智能数据类型转换器")
print("-" * 40)
print("任务：创建一个智能转换器，自动识别并转换数据类型")

print("\n解答：")

def smart_convert(value_str):
    """智能类型转换函数"""
    # 去除首尾空格
    value_str = value_str.strip()
    
    # 检查是否为空
    if not value_str:
        return None, "empty"
    
    # 检查布尔值
    if value_str.lower() in ['true', 'false']:
        return value_str.lower() == 'true', "boolean"
    
    # 检查None
    if value_str.lower() in ['none', 'null']:
        return None, "none"
    
    # 检查整数
    try:
        if '.' not in value_str and 'e' not in value_str.lower():
            return int(value_str), "integer"
    except ValueError:
        pass
    
    # 检查浮点数
    try:
        return float(value_str), "float"
    except ValueError:
        pass
    
    # 默认为字符串
    return value_str, "string"

# 测试智能转换器
test_values = [
    "123",
    "45.67",
    "true",
    "false",
    "hello",
    "none",
    "  89  ",
    "3.14e2",
    "",
    "0",
    "-42"
]

print("智能转换测试：")
for test_val in test_values:
    converted_val, detected_type = smart_convert(test_val)
    print(f"'{test_val}' -> {repr(converted_val)} ({detected_type})")

# 练习8：变量作用域和生命周期
print("\n练习8：变量作用域演示")
print("-" * 40)
print("任务：理解变量的作用域和生命周期")

print("\n解答：")

# 全局变量
global_counter = 0

def demonstrate_scope():
    """演示变量作用域"""
    global global_counter
    
    # 局部变量
    local_var = "我是局部变量"
    
    # 修改全局变量
    global_counter += 1
    
    print(f"函数内部：")
    print(f"  局部变量：{local_var}")
    print(f"  全局计数器：{global_counter}")
    
    # 内部函数
    def inner_function():
        inner_var = "我是内部函数的变量"
        print(f"  内部函数变量：{inner_var}")
        print(f"  可以访问外部局部变量：{local_var}")
        print(f"  可以访问全局变量：{global_counter}")
    
    inner_function()

print(f"调用前全局计数器：{global_counter}")
demonstrate_scope()
print(f"调用后全局计数器：{global_counter}")

# ==================== 挑战练习 ====================
print("\n" + "=" * 20 + " 挑战练习 " + "=" * 20)

# 练习9：复杂数据结构处理
print("\n练习9：学生成绩管理系统")
print("-" * 40)
print("任务：创建一个复杂的学生成绩管理系统")
print("要求：")
print("1. 支持多个学生的多门课程成绩")
print("2. 计算平均分、最高分、最低分")
print("3. 支持成绩的增删改查")
print("4. 处理异常输入")

print("\n解答：")

# 学生成绩数据结构
students_data = {
    "张三": {
        "id": "S001",
        "age": 20,
        "grades": {"数学": 85, "英语": 92, "物理": 78},
        "is_active": True
    },
    "李四": {
        "id": "S002",
        "age": 19,
        "grades": {"数学": 90, "英语": 88, "物理": 95},
        "is_active": True
    },
    "王五": {
        "id": "S003",
        "age": 21,
        "grades": {"数学": 76, "英语": 85, "物理": 82},
        "is_active": False
    }
}

def calculate_student_average(student_name):
    """计算学生平均分"""
    if student_name not in students_data:
        return None
    
    grades = students_data[student_name]["grades"]
    if not grades:
        return 0
    
    total = sum(grades.values())
    count = len(grades)
    return round(total / count, 2)

def get_subject_statistics(subject):
    """获取某科目的统计信息"""
    scores = []
    for student_name, student_info in students_data.items():
        if subject in student_info["grades"]:
            scores.append(student_info["grades"][subject])
    
    if not scores:
        return None
    
    return {
        "average": round(sum(scores) / len(scores), 2),
        "max": max(scores),
        "min": min(scores),
        "count": len(scores)
    }

def add_grade(student_name, subject, score_str):
    """添加成绩（带验证）"""
    try:
        score = float(score_str)
        if not (0 <= score <= 100):
            print(f"成绩无效：{score}（应在0-100之间）")
            return False
        
        if student_name not in students_data:
            print(f"学生不存在：{student_name}")
            return False
        
        students_data[student_name]["grades"][subject] = score
        print(f"成绩添加成功：{student_name} {subject} {score}")
        return True
    
    except ValueError:
        print(f"成绩格式错误：'{score_str}'（应为数字）")
        return False

def display_all_students():
    """显示所有学生信息"""
    print("\n所有学生信息：")
    print("-" * 60)
    
    for student_name, student_info in students_data.items():
        status = "活跃" if student_info["is_active"] else "非活跃"
        average = calculate_student_average(student_name)
        
        print(f"姓名：{student_name} (ID: {student_info['id']}, 年龄: {student_info['age']}, 状态: {status})")
        print(f"  成绩：{student_info['grades']}")
        print(f"  平均分：{average}")
        print()

# 演示成绩管理系统
display_all_students()

print("科目统计信息：")
subjects = ["数学", "英语", "物理"]
for subject in subjects:
    stats = get_subject_statistics(subject)
    if stats:
        print(f"{subject}：平均分 {stats['average']}, 最高分 {stats['max']}, 最低分 {stats['min']}, 人数 {stats['count']}")

print("\n测试添加成绩：")
add_grade("张三", "化学", "88")
add_grade("张三", "化学", "105")  # 无效分数
add_grade("张三", "化学", "abc")  # 无效格式
add_grade("不存在", "数学", "90")  # 不存在的学生

# 练习10：类型安全的配置管理器
print("\n练习10：类型安全的配置管理器")
print("-" * 40)
print("任务：创建一个类型安全的配置管理器")
print("要求：")
print("1. 支持多种数据类型的配置项")
print("2. 提供类型验证和转换")
print("3. 支持默认值")
print("4. 提供配置的保存和加载")

print("\n解答：")

class ConfigManager:
    """类型安全的配置管理器"""
    
    def __init__(self):
        self.config = {}
        self.schema = {}
    
    def define_config(self, key, default_value, value_type, description=""):
        """定义配置项"""
        self.schema[key] = {
            "type": value_type,
            "default": default_value,
            "description": description
        }
        self.config[key] = default_value
    
    def set_config(self, key, value):
        """设置配置项（带类型验证）"""
        if key not in self.schema:
            print(f"未知的配置项：{key}")
            return False
        
        expected_type = self.schema[key]["type"]
        
        # 尝试类型转换
        try:
            if expected_type == bool:
                if isinstance(value, str):
                    converted_value = value.lower() in ['true', '1', 'yes', 'on']
                else:
                    converted_value = bool(value)
            elif expected_type == int:
                converted_value = int(value)
            elif expected_type == float:
                converted_value = float(value)
            elif expected_type == str:
                converted_value = str(value)
            else:
                converted_value = value
            
            self.config[key] = converted_value
            print(f"配置更新：{key} = {converted_value} ({type(converted_value).__name__})")
            return True
        
        except (ValueError, TypeError) as e:
            print(f"配置设置失败：{key} = {value} (期望类型: {expected_type.__name__}, 错误: {e})")
            return False
    
    def get_config(self, key):
        """获取配置项"""
        return self.config.get(key, None)
    
    def display_config(self):
        """显示所有配置"""
        print("\n当前配置：")
        print("-" * 50)
        for key, value in self.config.items():
            schema_info = self.schema[key]
            print(f"{key}: {value} ({type(value).__name__})")
            print(f"  描述: {schema_info['description']}")
            print(f"  默认值: {schema_info['default']}")
            print()

# 创建配置管理器实例
config_manager = ConfigManager()

# 定义配置项
config_manager.define_config("server_port", 8080, int, "服务器端口号")
config_manager.define_config("debug_mode", False, bool, "是否启用调试模式")
config_manager.define_config("app_name", "MyApp", str, "应用程序名称")
config_manager.define_config("timeout", 30.0, float, "超时时间（秒）")
config_manager.define_config("max_connections", 100, int, "最大连接数")

# 显示初始配置
config_manager.display_config()

# 测试配置设置
print("测试配置设置：")
config_manager.set_config("server_port", "9000")      # 字符串转整数
config_manager.set_config("debug_mode", "true")       # 字符串转布尔
config_manager.set_config("timeout", "45.5")          # 字符串转浮点
config_manager.set_config("app_name", 123)            # 数字转字符串
config_manager.set_config("server_port", "abc")       # 无效转换
config_manager.set_config("unknown_key", "value")     # 未知配置项

# 显示最终配置
config_manager.display_config()

# ==================== 总结和评估 ====================
print("\n" + "=" * 20 + " 练习总结 " + "=" * 20)
print("\n恭喜完成所有练习！")
print("\n通过这些练习，你应该掌握了：")
print("✅ 变量的定义和赋值")
print("✅ Python的基本数据类型")
print("✅ 动态类型的特性")
print("✅ 类型转换的方法和注意事项")
print("✅ 变量命名的规范和最佳实践")
print("✅ 复杂数据结构的处理")
print("✅ 异常处理和输入验证")
print("✅ 实际项目中的应用场景")

print("\n下一步学习建议：")
print("1. 继续学习控制结构（if语句、循环）")
print("2. 深入学习函数和模块")
print("3. 学习面向对象编程")
print("4. 实践更多的项目案例")

print("\n" + "=" * 60)
print("变量和数据类型学习完成！")
print("=" * 60)

# 运行这个文件的方法：
# 在终端中输入：python 06_exercises.py
# 或者在IDE中直接运行

# 额外挑战：
# 1. 尝试修改ConfigManager类，添加配置的保存和加载功能
# 2. 为学生成绩管理系统添加更多功能，如成绩排名、及格率统计等
# 3. 创建一个数据验证器，支持更复杂的验证规则