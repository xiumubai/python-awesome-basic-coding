#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字典修改 - 修改字典内容

学习目标：
1. 掌握字典元素的添加方法
2. 学会修改字典中的值
3. 了解字典元素的删除操作
4. 掌握字典的更新和合并技巧

作者：Python学习教程
日期：2024年
"""

print("=" * 50)
print("字典修改 - 修改字典内容")
print("=" * 50)

# 创建初始字典
student = {
    "name": "张三",
    "age": 20,
    "grade": "大二"
}

print(f"初始学生信息: {student}")

# 1. 添加新的键值对
print("\n1. 添加新的键值对")
print("-" * 30)

# 使用方括号添加
student["major"] = "计算机科学"
student["gpa"] = 3.8
print(f"添加专业和GPA后: {student}")

# 添加复杂数据类型
student["courses"] = ["数据结构", "算法", "数据库"]
student["contact"] = {"email": "zhangsan@example.com", "phone": "138****1234"}
print(f"添加课程和联系方式后: {student}")

# 2. 修改已存在的值
print("\n2. 修改已存在的值")
print("-" * 30)

# 修改简单值
student["age"] = 21
student["grade"] = "大三"
print(f"修改年龄和年级后: {student}")

# 修改复杂值
student["courses"].append("操作系统")
student["contact"]["address"] = "北京市海淀区"
print(f"修改课程和联系方式后: {student}")

# 3. 使用update()方法批量更新
print("\n3. 使用update()方法批量更新")
print("-" * 30)

# 使用字典更新
update_info = {
    "gpa": 3.9,
    "scholarship": True,
    "graduation_year": 2025
}
student.update(update_info)
print(f"批量更新后: {student}")

# 使用关键字参数更新
student.update(internship="腾讯", project_count=3)
print(f"使用关键字参数更新后: {student}")

# 使用键值对列表更新
student.update([("hobby", "编程"), ("language", "Python")])
print(f"使用键值对列表更新后: {student}")

# 4. 删除字典元素
print("\n4. 删除字典元素")
print("-" * 30)

# 创建测试字典
test_dict = student.copy()
print(f"测试字典: {list(test_dict.keys())}")

# 使用del删除
del test_dict["hobby"]
print(f"删除hobby后的键: {list(test_dict.keys())}")

# 使用pop()删除并返回值
removed_language = test_dict.pop("language")
print(f"删除的语言: {removed_language}")
print(f"删除language后的键: {list(test_dict.keys())}")

# 使用pop()删除不存在的键（带默认值）
removed_skill = test_dict.pop("skill", "未设置")
print(f"删除不存在的skill: {removed_skill}")

# 使用popitem()删除最后插入的键值对
last_item = test_dict.popitem()
print(f"删除的最后一项: {last_item}")
print(f"删除最后一项后的键: {list(test_dict.keys())}")

# 5. 清空字典
print("\n5. 清空字典")
print("-" * 30)

# 创建测试字典
clear_test = {"a": 1, "b": 2, "c": 3}
print(f"清空前: {clear_test}")

# 使用clear()方法
clear_test.clear()
print(f"清空后: {clear_test}")
print(f"字典类型保持: {type(clear_test)}")

# 6. 条件修改
print("\n6. 条件修改")
print("-" * 30)

# 创建成绩字典
scores = {
    "math": 85,
    "english": 78,
    "physics": 92,
    "chemistry": 88
}

print(f"原始成绩: {scores}")

# 只有当成绩低于80时才更新
for subject, score in scores.items():
    if score < 80:
        scores[subject] = score + 5  # 加5分
        print(f"{subject}成绩提升到: {scores[subject]}")

print(f"调整后成绩: {scores}")

# 使用setdefault()进行条件添加
scores.setdefault("biology", 90)  # 只有当键不存在时才添加
scores.setdefault("math", 100)    # 键已存在，不会修改
print(f"使用setdefault后: {scores}")

# 7. 嵌套字典的修改
print("\n7. 嵌套字典的修改")
print("-" * 30)

# 创建复杂的嵌套字典
company = {
    "name": "科技公司",
    "employees": {
        "IT": {
            "manager": "张经理",
            "staff": ["李开发", "王测试"],
            "budget": 500000
        },
        "HR": {
            "manager": "陈经理",
            "staff": ["刘招聘"],
            "budget": 200000
        }
    }
}

print(f"原始公司结构: {company}")

# 修改嵌套值
company["employees"]["IT"]["budget"] = 600000
company["employees"]["IT"]["staff"].append("赵运维")
print(f"修改IT部门后: {company['employees']['IT']}")

# 添加新部门
company["employees"]["Finance"] = {
    "manager": "孙经理",
    "staff": ["钱会计"],
    "budget": 300000
}
print(f"添加财务部后: {list(company['employees'].keys())}")

# 8. 字典合并的不同方式
print("\n8. 字典合并的不同方式")
print("-" * 30)

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 4, "d": 5, "e": 6}

print(f"字典1: {dict1}")
print(f"字典2: {dict2}")

# 方法1: 使用update()
merged1 = dict1.copy()
merged1.update(dict2)
print(f"使用update()合并: {merged1}")

# 方法2: 使用字典解包（Python 3.5+）
merged2 = {**dict1, **dict2}
print(f"使用解包合并: {merged2}")

# 方法3: 使用|操作符（Python 3.9+）
try:
    merged3 = dict1 | dict2
    print(f"使用|操作符合并: {merged3}")
except TypeError:
    print("当前Python版本不支持|操作符合并字典")

# 9. 批量修改操作
print("\n9. 批量修改操作")
print("-" * 30)

# 创建产品价格字典
prices = {
    "laptop": 5999,
    "mouse": 99,
    "keyboard": 299,
    "monitor": 1299
}

print(f"原始价格: {prices}")

# 所有价格打9折
discounted_prices = {item: price * 0.9 for item, price in prices.items()}
print(f"打折后价格: {discounted_prices}")

# 直接修改原字典
for item in prices:
    if prices[item] > 1000:
        prices[item] = int(prices[item] * 0.8)  # 高价商品打8折
    else:
        prices[item] = int(prices[item] * 0.9)  # 低价商品打9折

print(f"分级打折后: {prices}")

# 10. 实际应用示例
print("\n10. 实际应用示例")
print("-" * 30)

# 用户配置管理系统
class ConfigManager:
    def __init__(self):
        self.config = {
            "user": {
                "name": "用户",
                "theme": "light",
                "language": "zh-CN"
            },
            "app": {
                "version": "1.0.0",
                "debug": False
            }
        }
    
    def set_config(self, path, value):
        """根据路径设置配置值"""
        keys = path.split('.')
        current = self.config
        
        # 导航到目标位置
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        
        # 设置最终值
        current[keys[-1]] = value
    
    def get_config(self, path, default=None):
        """根据路径获取配置值"""
        keys = path.split('.')
        current = self.config
        
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default
        
        return current
    
    def update_config(self, updates):
        """批量更新配置"""
        for path, value in updates.items():
            self.set_config(path, value)

# 使用配置管理器
config_mgr = ConfigManager()
print(f"初始配置: {config_mgr.config}")

# 修改单个配置
config_mgr.set_config("user.theme", "dark")
config_mgr.set_config("app.debug", True)
print(f"修改后配置: {config_mgr.config}")

# 批量更新
updates = {
    "user.name": "张三",
    "user.email": "zhangsan@example.com",
    "app.version": "1.1.0"
}
config_mgr.update_config(updates)
print(f"批量更新后: {config_mgr.config}")

print("\n" + "=" * 50)
print("字典修改方法总结：")
print("1. dict[key] = value - 添加或修改键值对")
print("2. dict.update() - 批量更新字典")
print("3. del dict[key] - 删除指定键")
print("4. dict.pop(key) - 删除并返回值")
print("5. dict.popitem() - 删除最后一项")
print("6. dict.clear() - 清空字典")
print("7. dict.setdefault() - 条件设置默认值")
print("=" * 50)

if __name__ == "__main__":
    print("\n程序执行完成！")
    print("请尝试修改代码，练习不同的字典修改操作。")