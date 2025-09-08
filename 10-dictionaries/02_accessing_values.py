#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字典访问 - 访问字典值和键操作

学习目标：
1. 掌握字典值的访问方法
2. 学会处理不存在的键
3. 了解字典键的操作
4. 掌握安全访问字典的技巧

作者：Python学习教程
日期：2024年
"""

print("=" * 50)
print("字典访问 - 访问字典值和键操作")
print("=" * 50)

# 创建示例字典
student = {
    "name": "张三",
    "age": 20,
    "grade": "大二",
    "major": "计算机科学",
    "scores": {"math": 95, "english": 88, "python": 92}
}

print(f"学生信息字典: {student}")

# 1. 使用方括号访问值
print("\n1. 使用方括号访问值")
print("-" * 30)

print(f"学生姓名: {student['name']}")
print(f"学生年龄: {student['age']}")
print(f"学生专业: {student['major']}")

# 访问嵌套字典
print(f"数学成绩: {student['scores']['math']}")
print(f"英语成绩: {student['scores']['english']}")

# 2. 使用get()方法访问值
print("\n2. 使用get()方法访问值")
print("-" * 30)

print(f"学生姓名: {student.get('name')}")
print(f"学生年龄: {student.get('age')}")

# get()方法的优势：处理不存在的键
print(f"不存在的键: {student.get('phone')}")
print(f"不存在的键（带默认值）: {student.get('phone', '未提供')}")
print(f"邮箱: {student.get('email', 'unknown@example.com')}")

# 3. 键的存在性检查
print("\n3. 键的存在性检查")
print("-" * 30)

# 使用in操作符
print(f"'name' 在字典中: {'name' in student}")
print(f"'phone' 在字典中: {'phone' in student}")
print(f"'age' 不在字典中: {'age' not in student}")

# 安全访问示例
key_to_check = 'phone'
if key_to_check in student:
    print(f"{key_to_check}: {student[key_to_check]}")
else:
    print(f"{key_to_check}: 键不存在")

# 4. 获取所有键、值和键值对
print("\n4. 获取所有键、值和键值对")
print("-" * 30)

# 获取所有键
keys = student.keys()
print(f"所有键: {list(keys)}")
print(f"键的类型: {type(keys)}")

# 获取所有值
values = student.values()
print(f"所有值: {list(values)}")
print(f"值的类型: {type(values)}")

# 获取所有键值对
items = student.items()
print(f"所有键值对: {list(items)}")
print(f"键值对的类型: {type(items)}")

# 5. 遍历字典的不同方式
print("\n5. 遍历字典的不同方式")
print("-" * 30)

# 遍历键
print("遍历键:")
for key in student:
    print(f"  {key}")

# 遍历键（显式）
print("\n遍历键（显式）:")
for key in student.keys():
    print(f"  {key}: {student[key]}")

# 遍历值
print("\n遍历值:")
for value in student.values():
    print(f"  {value}")

# 遍历键值对
print("\n遍历键值对:")
for key, value in student.items():
    print(f"  {key}: {value}")

# 6. 处理异常情况
print("\n6. 处理异常情况")
print("-" * 30)

# KeyError异常处理
try:
    phone = student['phone']  # 这会引发KeyError
except KeyError as e:
    print(f"捕获到KeyError: {e}")
    print("建议使用get()方法或先检查键是否存在")

# 安全访问的最佳实践
def safe_get(dictionary, key, default=None):
    """安全获取字典值的函数"""
    try:
        return dictionary[key]
    except KeyError:
        return default

print(f"安全获取姓名: {safe_get(student, 'name')}")
print(f"安全获取电话: {safe_get(student, 'phone', '未提供')}")

# 7. 复杂数据结构的访问
print("\n7. 复杂数据结构的访问")
print("-" * 30)

# 创建更复杂的字典
company = {
    "name": "科技公司",
    "departments": {
        "IT": {
            "manager": "张经理",
            "employees": ["李开发", "王测试", "赵运维"],
            "budget": 500000
        },
        "HR": {
            "manager": "陈经理",
            "employees": ["刘招聘", "孙培训"],
            "budget": 200000
        }
    }
}

# 访问嵌套数据
print(f"公司名称: {company['name']}")
print(f"IT部门经理: {company['departments']['IT']['manager']}")
print(f"IT部门员工: {company['departments']['IT']['employees']}")
print(f"第一个IT员工: {company['departments']['IT']['employees'][0]}")

# 安全访问嵌套数据
it_budget = company.get('departments', {}).get('IT', {}).get('budget', 0)
print(f"IT部门预算: {it_budget}")

# 不存在的部门
finance_manager = company.get('departments', {}).get('Finance', {}).get('manager', '无')
print(f"财务部经理: {finance_manager}")

# 8. 实用的访问技巧
print("\n8. 实用的访问技巧")
print("-" * 30)

# 使用setdefault()方法
config = {'debug': True, 'port': 8080}
print(f"原配置: {config}")

# 如果键不存在，设置默认值并返回
host = config.setdefault('host', 'localhost')
print(f"主机地址: {host}")
print(f"更新后配置: {config}")

# 再次调用setdefault()，不会覆盖已存在的值
host2 = config.setdefault('host', '127.0.0.1')
print(f"主机地址（再次获取）: {host2}")
print(f"配置保持不变: {config}")

# 9. 字典访问的性能考虑
print("\n9. 字典访问的性能考虑")
print("-" * 30)

# 字典访问是O(1)时间复杂度
import time

# 创建大字典
large_dict = {f"key_{i}": f"value_{i}" for i in range(100000)}

# 测试访问速度
start_time = time.time()
for i in range(1000):
    value = large_dict.get(f"key_{i}")
end_time = time.time()

print(f"访问1000个键耗时: {end_time - start_time:.6f}秒")
print("字典访问具有O(1)平均时间复杂度")

# 10. 实际应用示例
print("\n10. 实际应用示例")
print("-" * 30)

# 用户配置管理
user_settings = {
    "theme": "dark",
    "language": "zh-CN",
    "notifications": {
        "email": True,
        "push": False,
        "sms": True
    }
}

def get_setting(settings, path, default=None):
    """根据路径获取嵌套设置值"""
    keys = path.split('.')
    current = settings
    
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    
    return current

# 使用路径访问设置
print(f"主题设置: {get_setting(user_settings, 'theme')}")
print(f"邮件通知: {get_setting(user_settings, 'notifications.email')}")
print(f"不存在的设置: {get_setting(user_settings, 'advanced.cache', '默认值')}")

print("\n" + "=" * 50)
print("字典访问方法总结：")
print("1. dict[key] - 直接访问，键不存在时抛出异常")
print("2. dict.get(key, default) - 安全访问，可设置默认值")
print("3. key in dict - 检查键是否存在")
print("4. dict.keys(), dict.values(), dict.items() - 获取视图")
print("5. dict.setdefault(key, default) - 获取或设置默认值")
print("=" * 50)

if __name__ == "__main__":
    print("\n程序执行完成！")
    print("请尝试修改代码，练习不同的字典访问方法。")