#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
嵌套字典 - 嵌套字典操作详解

学习目标：
1. 掌握嵌套字典的创建和结构设计
2. 学会访问和修改嵌套字典中的数据
3. 了解嵌套字典的遍历技巧
4. 掌握复杂数据结构的处理方法

作者：Python学习教程
日期：2024年
"""

print("=" * 50)
print("嵌套字典 - 嵌套字典操作详解")
print("=" * 50)

# 1. 创建嵌套字典
print("\n1. 创建嵌套字典")
print("-" * 30)

# 学校管理系统
school = {
    "name": "北京大学",
    "location": "北京市海淀区",
    "departments": {
        "计算机学院": {
            "dean": "张教授",
            "students_count": 500,
            "courses": {
                "数据结构": {"credits": 4, "teacher": "李老师", "students": 120},
                "算法设计": {"credits": 3, "teacher": "王老师", "students": 100},
                "数据库": {"credits": 3, "teacher": "赵老师", "students": 80}
            },
            "faculty": {
                "李老师": {"title": "副教授", "research": "机器学习", "courses": ["数据结构"]},
                "王老师": {"title": "教授", "research": "算法优化", "courses": ["算法设计"]},
                "赵老师": {"title": "讲师", "research": "数据库系统", "courses": ["数据库"]}
            }
        },
        "数学学院": {
            "dean": "陈教授",
            "students_count": 300,
            "courses": {
                "高等数学": {"credits": 5, "teacher": "孙老师", "students": 200},
                "线性代数": {"credits": 4, "teacher": "周老师", "students": 150}
            },
            "faculty": {
                "孙老师": {"title": "教授", "research": "数学分析", "courses": ["高等数学"]},
                "周老师": {"title": "副教授", "research": "代数几何", "courses": ["线性代数"]}
            }
        }
    }
}

print(f"学校名称: {school['name']}")
print(f"学校位置: {school['location']}")
print(f"院系数量: {len(school['departments'])}")

# 2. 访问嵌套字典数据
print("\n2. 访问嵌套字典数据")
print("-" * 30)

# 多层访问
cs_dean = school["departments"]["计算机学院"]["dean"]
print(f"计算机学院院长: {cs_dean}")

ds_credits = school["departments"]["计算机学院"]["courses"]["数据结构"]["credits"]
print(f"数据结构课程学分: {ds_credits}")

li_teacher_title = school["departments"]["计算机学院"]["faculty"]["李老师"]["title"]
print(f"李老师职称: {li_teacher_title}")

# 安全访问嵌套数据
def safe_get_nested(data, keys, default=None):
    """安全获取嵌套字典的值"""
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

# 使用安全访问
physics_dean = safe_get_nested(school, ["departments", "物理学院", "dean"], "未找到")
print(f"物理学院院长: {physics_dean}")

cs_budget = safe_get_nested(school, ["departments", "计算机学院", "budget"], "未设置")
print(f"计算机学院预算: {cs_budget}")

# 3. 修改嵌套字典
print("\n3. 修改嵌套字典")
print("-" * 30)

# 修改现有值
school["departments"]["计算机学院"]["students_count"] = 520
print(f"更新后的计算机学院学生数: {school['departments']['计算机学院']['students_count']}")

# 添加新的嵌套数据
school["departments"]["计算机学院"]["budget"] = 5000000
school["departments"]["计算机学院"]["courses"]["人工智能"] = {
    "credits": 4,
    "teacher": "刘老师",
    "students": 90
}

print(f"添加预算: {school['departments']['计算机学院']['budget']}")
print(f"新增课程: {list(school['departments']['计算机学院']['courses'].keys())}")

# 添加新教师
school["departments"]["计算机学院"]["faculty"]["刘老师"] = {
    "title": "副教授",
    "research": "人工智能",
    "courses": ["人工智能"]
}

print(f"新增教师: 刘老师 - {school['departments']['计算机学院']['faculty']['刘老师']['title']}")

# 4. 嵌套字典的遍历
print("\n4. 嵌套字典的遍历")
print("-" * 30)

# 遍历所有院系
print("所有院系信息:")
for dept_name, dept_info in school["departments"].items():
    print(f"\n{dept_name}:")
    print(f"  院长: {dept_info['dean']}")
    print(f"  学生数: {dept_info['students_count']}")
    
    # 遍历课程
    print(f"  课程:")
    for course_name, course_info in dept_info["courses"].items():
        print(f"    {course_name}: {course_info['credits']}学分, 教师: {course_info['teacher']}")
    
    # 遍历教师
    print(f"  教师:")
    for teacher_name, teacher_info in dept_info["faculty"].items():
        courses = ', '.join(teacher_info['courses'])
        print(f"    {teacher_name}: {teacher_info['title']}, 研究方向: {teacher_info['research']}, 课程: [{courses}]")

# 5. 深度遍历和搜索
print("\n5. 深度遍历和搜索")
print("-" * 30)

def find_all_teachers(data):
    """递归查找所有教师信息"""
    teachers = []
    
    def recursive_search(obj, path=""):
        if isinstance(obj, dict):
            if "title" in obj and "research" in obj:  # 教师对象的特征
                teachers.append((path, obj))
            else:
                for key, value in obj.items():
                    new_path = f"{path}.{key}" if path else key
                    recursive_search(value, new_path)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                new_path = f"{path}[{i}]"
                recursive_search(item, new_path)
    
    recursive_search(data)
    return teachers

# 查找所有教师
all_teachers = find_all_teachers(school)
print("所有教师信息:")
for path, teacher_info in all_teachers:
    print(f"  路径: {path}")
    print(f"    职称: {teacher_info['title']}, 研究: {teacher_info['research']}")

# 6. 嵌套字典的统计分析
print("\n6. 嵌套字典的统计分析")
print("-" * 30)

# 统计总学生数
total_students = 0
for dept_info in school["departments"].values():
    total_students += dept_info["students_count"]
print(f"全校总学生数: {total_students}")

# 统计总课程数和总学分
total_courses = 0
total_credits = 0
for dept_info in school["departments"].values():
    for course_info in dept_info["courses"].values():
        total_courses += 1
        total_credits += course_info["credits"]

print(f"全校总课程数: {total_courses}")
print(f"全校总学分: {total_credits}")
print(f"平均每门课学分: {total_credits/total_courses:.2f}")

# 按职称统计教师
teacher_by_title = {}
for dept_info in school["departments"].values():
    for teacher_info in dept_info["faculty"].values():
        title = teacher_info["title"]
        teacher_by_title[title] = teacher_by_title.get(title, 0) + 1

print(f"\n教师职称分布: {teacher_by_title}")

# 7. 复杂的嵌套结构操作
print("\n7. 复杂的嵌套结构操作")
print("-" * 30)

# 创建电商系统数据结构
ecommerce = {
    "users": {
        "user_001": {
            "name": "张三",
            "email": "zhangsan@example.com",
            "orders": {
                "order_001": {
                    "date": "2024-01-15",
                    "status": "completed",
                    "items": {
                        "item_001": {"name": "笔记本电脑", "price": 5999, "quantity": 1},
                        "item_002": {"name": "鼠标", "price": 99, "quantity": 2}
                    },
                    "shipping": {"address": "北京市朝阳区", "method": "快递", "cost": 15}
                },
                "order_002": {
                    "date": "2024-02-01",
                    "status": "pending",
                    "items": {
                        "item_003": {"name": "键盘", "price": 299, "quantity": 1}
                    },
                    "shipping": {"address": "北京市朝阳区", "method": "快递", "cost": 15}
                }
            },
            "preferences": {
                "categories": ["电子产品", "数码配件"],
                "notifications": {"email": True, "sms": False}
            }
        },
        "user_002": {
            "name": "李四",
            "email": "lisi@example.com",
            "orders": {
                "order_003": {
                    "date": "2024-01-20",
                    "status": "completed",
                    "items": {
                        "item_004": {"name": "手机", "price": 3999, "quantity": 1}
                    },
                    "shipping": {"address": "上海市浦东区", "method": "快递", "cost": 20}
                }
            },
            "preferences": {
                "categories": ["手机通讯"],
                "notifications": {"email": True, "sms": True}
            }
        }
    }
}

# 计算用户总消费
def calculate_user_spending(user_data):
    """计算用户总消费"""
    total = 0
    for order in user_data["orders"].values():
        for item in order["items"].values():
            total += item["price"] * item["quantity"]
        total += order["shipping"]["cost"]
    return total

print("用户消费统计:")
for user_id, user_data in ecommerce["users"].items():
    spending = calculate_user_spending(user_data)
    order_count = len(user_data["orders"])
    print(f"  {user_data['name']} ({user_id}): 消费{spending}元, 订单{order_count}个")

# 8. 嵌套字典的深拷贝和浅拷贝
print("\n8. 嵌套字典的深拷贝和浅拷贝")
print("-" * 30)

import copy

# 原始数据
original = {
    "level1": {
        "level2": {
            "data": [1, 2, 3],
            "info": "原始数据"
        }
    }
}

print(f"原始数据: {original}")

# 浅拷贝
shallow_copy = original.copy()
shallow_copy["level1"]["level2"]["data"].append(4)
shallow_copy["level1"]["level2"]["info"] = "浅拷贝修改"

print(f"浅拷贝修改后原始数据: {original}")
print("注意：浅拷贝会影响原始数据的嵌套对象！")

# 深拷贝
original2 = {
    "level1": {
        "level2": {
            "data": [1, 2, 3],
            "info": "原始数据2"
        }
    }
}

deep_copy = copy.deepcopy(original2)
deep_copy["level1"]["level2"]["data"].append(4)
deep_copy["level1"]["level2"]["info"] = "深拷贝修改"

print(f"\n深拷贝修改后原始数据: {original2}")
print(f"深拷贝数据: {deep_copy}")
print("深拷贝不会影响原始数据！")

# 9. 嵌套字典的扁平化
print("\n9. 嵌套字典的扁平化")
print("-" * 30)

def flatten_dict(d, parent_key='', sep='.'):
    """将嵌套字典扁平化"""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# 测试扁平化
nested_config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "credentials": {
            "username": "admin",
            "password": "secret"
        }
    },
    "cache": {
        "enabled": True,
        "ttl": 300
    }
}

flat_config = flatten_dict(nested_config)
print(f"原始嵌套配置: {nested_config}")
print(f"\n扁平化配置: {flat_config}")

# 10. 实际应用：JSON数据处理
print("\n10. 实际应用：JSON数据处理")
print("-" * 30)

# 模拟API响应数据
api_response = {
    "status": "success",
    "data": {
        "user": {
            "id": 12345,
            "profile": {
                "name": "王五",
                "age": 28,
                "contact": {
                    "email": "wangwu@example.com",
                    "phone": "138****5678"
                }
            },
            "settings": {
                "theme": "dark",
                "language": "zh-CN",
                "notifications": {
                    "push": True,
                    "email": False
                }
            }
        },
        "permissions": ["read", "write", "admin"]
    },
    "metadata": {
        "timestamp": "2024-01-15T10:30:00Z",
        "version": "1.0"
    }
}

# 提取用户信息的函数
def extract_user_info(response):
    """从API响应中提取用户信息"""
    if response.get("status") != "success":
        return None
    
    user_data = response.get("data", {}).get("user", {})
    profile = user_data.get("profile", {})
    settings = user_data.get("settings", {})
    
    return {
        "id": user_data.get("id"),
        "name": profile.get("name"),
        "email": profile.get("contact", {}).get("email"),
        "theme": settings.get("theme"),
        "language": settings.get("language")
    }

user_info = extract_user_info(api_response)
print(f"提取的用户信息: {user_info}")

# 更新嵌套设置
def update_user_setting(response, setting_path, value):
    """更新用户设置"""
    keys = setting_path.split('.')
    current = response["data"]["user"]["settings"]
    
    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]
    
    current[keys[-1]] = value

# 更新通知设置
update_user_setting(api_response, "notifications.push", False)
update_user_setting(api_response, "notifications.sms", True)
print(f"\n更新后的通知设置: {api_response['data']['user']['settings']['notifications']}")

print("\n" + "=" * 50)
print("嵌套字典操作总结：")
print("1. 多层访问 - dict[key1][key2][key3]")
print("2. 安全访问 - 使用get()和异常处理")
print("3. 递归遍历 - 处理任意深度的嵌套")
print("4. 深拷贝 - copy.deepcopy()避免意外修改")
print("5. 扁平化 - 将嵌套结构转换为平面结构")
print("6. 路径访问 - 使用字符串路径访问嵌套数据")
print("=" * 50)

if __name__ == "__main__":
    print("\n程序执行完成！")
    print("请尝试修改代码，练习复杂嵌套字典的操作技巧。")