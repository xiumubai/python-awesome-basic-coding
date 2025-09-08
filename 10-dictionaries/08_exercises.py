#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字典综合练习 - 实战练习题

学习目标：
1. 综合运用字典的各种操作
2. 解决实际问题和编程挑战
3. 提高字典操作的熟练度
4. 掌握复杂数据结构的处理

作者：Python学习教程
日期：2024年
"""

print("=" * 50)
print("字典综合练习 - 实战练习题")
print("=" * 50)

# 练习1：学生成绩管理系统
print("\n练习1：学生成绩管理系统")
print("-" * 30)

# 学生成绩数据
students_scores = {
    "张三": {"数学": 85, "英语": 92, "物理": 78, "化学": 88},
    "李四": {"数学": 92, "英语": 85, "物理": 90, "化学": 87},
    "王五": {"数学": 78, "英语": 88, "物理": 85, "化学": 92},
    "赵六": {"数学": 96, "英语": 89, "物理": 94, "化学": 91},
    "钱七": {"数学": 88, "英语": 94, "物理": 87, "化学": 89}
}

def calculate_average(scores):
    """计算平均分"""
    return sum(scores.values()) / len(scores)

def get_grade(score):
    """根据分数获取等级"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

# 任务1：计算每个学生的平均分
print("任务1：学生平均分")
student_averages = {name: calculate_average(scores) 
                   for name, scores in students_scores.items()}
for name, avg in student_averages.items():
    print(f"  {name}: {avg:.2f}分")

# 任务2：找出每科的最高分学生
print("\n任务2：各科最高分学生")
subjects = ["数学", "英语", "物理", "化学"]
for subject in subjects:
    subject_scores = {name: scores[subject] 
                     for name, scores in students_scores.items()}
    top_student = max(subject_scores, key=subject_scores.get)
    top_score = subject_scores[top_student]
    print(f"  {subject}: {top_student} ({top_score}分)")

# 任务3：统计各等级人数
print("\n任务3：成绩等级分布")
grade_count = {"A": 0, "B": 0, "C": 0, "D": 0}
for name, avg in student_averages.items():
    grade = get_grade(avg)
    grade_count[grade] += 1
for grade, count in grade_count.items():
    print(f"  {grade}等级: {count}人")

# 练习2：商品库存管理系统
print("\n练习2：商品库存管理系统")
print("-" * 30)

# 商品库存数据
inventory = {
    "苹果": {"price": 3.5, "stock": 100, "category": "水果"},
    "香蕉": {"price": 2.0, "stock": 150, "category": "水果"},
    "牛奶": {"price": 12.0, "stock": 50, "category": "乳制品"},
    "面包": {"price": 8.0, "stock": 80, "category": "烘焙"},
    "鸡蛋": {"price": 15.0, "stock": 200, "category": "蛋类"},
    "大米": {"price": 25.0, "stock": 30, "category": "粮食"}
}

# 任务1：计算库存总价值
print("任务1：库存总价值")
total_value = sum(item["price"] * item["stock"] for item in inventory.values())
print(f"  库存总价值: {total_value:.2f}元")

# 任务2：按类别分组商品
print("\n任务2：按类别分组")
category_groups = {}
for name, info in inventory.items():
    category = info["category"]
    if category not in category_groups:
        category_groups[category] = []
    category_groups[category].append(name)

for category, items in category_groups.items():
    print(f"  {category}: {', '.join(items)}")

# 任务3：找出库存不足的商品（库存<50）
print("\n任务3：库存不足商品")
low_stock = {name: info for name, info in inventory.items() 
            if info["stock"] < 50}
for name, info in low_stock.items():
    print(f"  {name}: 库存{info['stock']}件（需要补货）")

# 任务4：价格调整（所有商品打9折）
print("\n任务4：价格调整（9折）")
discounted_inventory = {
    name: {**info, "price": info["price"] * 0.9}
    for name, info in inventory.items()
}
print("调整后价格:")
for name, info in discounted_inventory.items():
    original_price = inventory[name]["price"]
    new_price = info["price"]
    print(f"  {name}: {original_price:.2f}元 → {new_price:.2f}元")

# 练习3：文本分析系统
print("\n练习3：文本分析系统")
print("-" * 30)

# 示例文本
text = """
Python是一种高级编程语言，由Guido van Rossum于1989年发明。
Python具有简洁、易读的语法，是初学者学习编程的理想选择。
Python广泛应用于Web开发、数据科学、人工智能等领域。
Python的设计哲学强调代码的可读性和简洁性。
"""

# 任务1：统计单词频率
print("任务1：单词频率统计")
import re

# 清理文本并分割单词
words = re.findall(r'\b[a-zA-Z\u4e00-\u9fff]+\b', text.lower())
word_frequency = {}
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

# 按频率排序显示前10个
sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
print("词频统计（前10个）:")
for word, count in sorted_words[:10]:
    print(f"  {word}: {count}次")

# 任务2：统计字符频率
print("\n任务2：字符频率统计")
char_frequency = {}
for char in text:
    if char.isalnum():  # 只统计字母和数字
        char_frequency[char] = char_frequency.get(char, 0) + 1

# 显示频率最高的字符
top_chars = sorted(char_frequency.items(), key=lambda x: x[1], reverse=True)[:5]
print("字符频率（前5个）:")
for char, count in top_chars:
    print(f"  '{char}': {count}次")

# 任务3：文本统计信息
print("\n任务3：文本统计信息")
text_stats = {
    "总字符数": len(text),
    "总单词数": len(words),
    "不重复单词数": len(set(words)),
    "平均单词长度": sum(len(word) for word in words) / len(words) if words else 0,
    "最长单词": max(words, key=len) if words else "",
    "最短单词": min(words, key=len) if words else ""
}

for stat, value in text_stats.items():
    if isinstance(value, float):
        print(f"  {stat}: {value:.2f}")
    else:
        print(f"  {stat}: {value}")

# 练习4：销售数据分析
print("\n练习4：销售数据分析")
print("-" * 30)

# 销售数据
sales_data = [
    {"date": "2024-01-01", "product": "笔记本电脑", "quantity": 2, "price": 5999, "salesperson": "张三"},
    {"date": "2024-01-01", "product": "鼠标", "quantity": 5, "price": 99, "salesperson": "李四"},
    {"date": "2024-01-02", "product": "键盘", "quantity": 3, "price": 299, "salesperson": "张三"},
    {"date": "2024-01-02", "product": "笔记本电脑", "quantity": 1, "price": 5999, "salesperson": "王五"},
    {"date": "2024-01-03", "product": "显示器", "quantity": 2, "price": 1299, "salesperson": "李四"},
    {"date": "2024-01-03", "product": "鼠标", "quantity": 8, "price": 99, "salesperson": "张三"},
    {"date": "2024-01-04", "product": "键盘", "quantity": 4, "price": 299, "salesperson": "王五"},
]

# 任务1：计算每个销售员的总销售额
print("任务1：销售员业绩")
salesperson_sales = {}
for sale in sales_data:
    person = sale["salesperson"]
    amount = sale["quantity"] * sale["price"]
    salesperson_sales[person] = salesperson_sales.get(person, 0) + amount

for person, total in sorted(salesperson_sales.items(), key=lambda x: x[1], reverse=True):
    print(f"  {person}: {total:,}元")

# 任务2：统计每种产品的销售情况
print("\n任务2：产品销售统计")
product_stats = {}
for sale in sales_data:
    product = sale["product"]
    if product not in product_stats:
        product_stats[product] = {"quantity": 0, "revenue": 0}
    
    product_stats[product]["quantity"] += sale["quantity"]
    product_stats[product]["revenue"] += sale["quantity"] * sale["price"]

for product, stats in product_stats.items():
    print(f"  {product}: 销量{stats['quantity']}件, 收入{stats['revenue']:,}元")

# 任务3：按日期统计销售额
print("\n任务3：日销售额统计")
daily_sales = {}
for sale in sales_data:
    date = sale["date"]
    amount = sale["quantity"] * sale["price"]
    daily_sales[date] = daily_sales.get(date, 0) + amount

for date in sorted(daily_sales.keys()):
    print(f"  {date}: {daily_sales[date]:,}元")

# 练习5：配置文件管理器
print("\n练习5：配置文件管理器")
print("-" * 30)

# 模拟配置数据
config_data = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": "admin",
        "password": "secret123",
        "database_name": "myapp"
    },
    "cache": {
        "enabled": True,
        "ttl": 300,
        "max_size": 1000
    },
    "logging": {
        "level": "INFO",
        "file": "/var/log/app.log",
        "max_file_size": "10MB"
    },
    "features": {
        "user_registration": True,
        "email_notifications": False,
        "premium_features": True
    }
}

# 任务1：扁平化配置
print("任务1：扁平化配置")
def flatten_config(config, prefix=""):
    """将嵌套配置扁平化"""
    flat_config = {}
    for key, value in config.items():
        new_key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            flat_config.update(flatten_config(value, new_key))
        else:
            flat_config[new_key] = value
    return flat_config

flat_config = flatten_config(config_data)
print("扁平化后的配置:")
for key, value in sorted(flat_config.items()):
    print(f"  {key}: {value}")

# 任务2：配置验证
print("\n任务2：配置验证")
required_configs = [
    "database.host",
    "database.port",
    "database.username",
    "logging.level"
]

missing_configs = []
for required in required_configs:
    if required not in flat_config:
        missing_configs.append(required)

if missing_configs:
    print(f"缺少必需配置: {missing_configs}")
else:
    print("所有必需配置都已设置")

# 任务3：配置类型检查
print("\n任务3：配置类型检查")
type_requirements = {
    "database.port": int,
    "cache.enabled": bool,
    "cache.ttl": int,
    "features.user_registration": bool
}

type_errors = []
for config_key, expected_type in type_requirements.items():
    if config_key in flat_config:
        actual_value = flat_config[config_key]
        if not isinstance(actual_value, expected_type):
            type_errors.append(f"{config_key}: 期望{expected_type.__name__}, 实际{type(actual_value).__name__}")

if type_errors:
    print("类型错误:")
    for error in type_errors:
        print(f"  {error}")
else:
    print("所有配置类型正确")

# 练习6：数据去重和合并
print("\n练习6：数据去重和合并")
print("-" * 30)

# 多个数据源
data_source1 = [
    {"id": 1, "name": "张三", "age": 25, "city": "北京"},
    {"id": 2, "name": "李四", "age": 30, "city": "上海"},
    {"id": 3, "name": "王五", "age": 28, "city": "广州"}
]

data_source2 = [
    {"id": 2, "name": "李四", "age": 30, "city": "上海", "email": "lisi@example.com"},
    {"id": 4, "name": "赵六", "age": 35, "city": "深圳"},
    {"id": 5, "name": "钱七", "age": 27, "city": "杭州"}
]

# 任务1：按ID去重合并
print("任务1：数据去重合并")
merged_data = {}

# 处理第一个数据源
for record in data_source1:
    merged_data[record["id"]] = record.copy()

# 处理第二个数据源，合并新字段
for record in data_source2:
    record_id = record["id"]
    if record_id in merged_data:
        # 合并新字段
        merged_data[record_id].update(record)
    else:
        # 新记录
        merged_data[record_id] = record.copy()

print("合并后的数据:")
for record_id, record in sorted(merged_data.items()):
    print(f"  ID {record_id}: {record}")

# 任务2：统计城市分布
print("\n任务2：城市分布统计")
city_distribution = {}
for record in merged_data.values():
    city = record["city"]
    city_distribution[city] = city_distribution.get(city, 0) + 1

for city, count in sorted(city_distribution.items()):
    print(f"  {city}: {count}人")

# 任务3：年龄分组
print("\n任务3：年龄分组")
age_groups = {
    "20-25": [],
    "26-30": [],
    "31-35": [],
    "36+": []
}

for record in merged_data.values():
    age = record["age"]
    name = record["name"]
    
    if 20 <= age <= 25:
        age_groups["20-25"].append(name)
    elif 26 <= age <= 30:
        age_groups["26-30"].append(name)
    elif 31 <= age <= 35:
        age_groups["31-35"].append(name)
    else:
        age_groups["36+"].append(name)

for group, names in age_groups.items():
    if names:
        print(f"  {group}岁: {', '.join(names)}")

print("\n" + "=" * 50)
print("综合练习总结：")
print("1. 学生成绩管理 - 数据统计和分析")
print("2. 商品库存管理 - 分类和筛选")
print("3. 文本分析 - 频率统计和文本处理")
print("4. 销售数据分析 - 多维度数据聚合")
print("5. 配置文件管理 - 嵌套数据处理")
print("6. 数据去重合并 - 复杂数据操作")
print("=" * 50)

if __name__ == "__main__":
    print("\n程序执行完成！")
    print("这些练习涵盖了字典的各种实际应用场景。")
    print("请尝试修改代码，解决更多实际问题。")