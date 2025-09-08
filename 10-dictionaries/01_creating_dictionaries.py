#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字典创建 - 创建字典的各种方法

学习目标：
1. 掌握字典的基本概念
2. 学会使用不同方法创建字典
3. 理解字典的键值对结构
4. 了解字典的特点和用途

作者：Python学习教程
日期：2024年
"""

print("=" * 50)
print("字典创建 - 创建字典的各种方法")
print("=" * 50)

# 1. 使用花括号创建字典
print("\n1. 使用花括号创建字典")
print("-" * 30)

# 创建空字典
empty_dict = {}
print(f"空字典: {empty_dict}")
print(f"字典类型: {type(empty_dict)}")

# 创建包含数据的字典
student = {
    "name": "张三",
    "age": 20,
    "grade": "大二",
    "major": "计算机科学"
}
print(f"学生信息: {student}")

# 2. 使用dict()函数创建字典
print("\n2. 使用dict()函数创建字典")
print("-" * 30)

# 创建空字典
empty_dict2 = dict()
print(f"空字典: {empty_dict2}")

# 使用关键字参数创建字典
teacher = dict(
    name="李老师",
    age=35,
    subject="数学",
    experience=10
)
print(f"教师信息: {teacher}")

# 使用键值对列表创建字典
key_value_pairs = [('apple', '苹果'), ('banana', '香蕉'), ('orange', '橙子')]
fruits = dict(key_value_pairs)
print(f"水果字典: {fruits}")

# 3. 使用字典推导式创建字典
print("\n3. 使用字典推导式创建字典")
print("-" * 30)

# 创建数字的平方字典
squares = {x: x**2 for x in range(1, 6)}
print(f"平方字典: {squares}")

# 创建字符串长度字典
words = ['hello', 'world', 'python', 'programming']
word_lengths = {word: len(word) for word in words}
print(f"单词长度字典: {word_lengths}")

# 4. 使用zip()函数创建字典
print("\n4. 使用zip()函数创建字典")
print("-" * 30)

# 将两个列表组合成字典
keys = ['name', 'age', 'city', 'job']
values = ['王五', 28, '北京', '工程师']
person = dict(zip(keys, values))
print(f"个人信息: {person}")

# 5. 从其他字典创建新字典
print("\n5. 从其他字典创建新字典")
print("-" * 30)

# 使用copy()方法
original = {'a': 1, 'b': 2, 'c': 3}
copied = original.copy()
print(f"原字典: {original}")
print(f"复制字典: {copied}")

# 使用dict()构造函数
copied2 = dict(original)
print(f"另一种复制: {copied2}")

# 6. 嵌套字典的创建
print("\n6. 嵌套字典的创建")
print("-" * 30)

# 创建包含字典的字典
company = {
    "name": "科技公司",
    "employees": {
        "manager": {"name": "张经理", "salary": 15000},
        "developer": {"name": "李开发", "salary": 12000},
        "designer": {"name": "王设计", "salary": 10000}
    },
    "location": "上海"
}
print(f"公司信息: {company}")

# 7. 字典的特点演示
print("\n7. 字典的特点演示")
print("-" * 30)

# 键必须是不可变类型
valid_keys = {
    "string_key": "字符串键",
    42: "数字键",
    (1, 2): "元组键",
    True: "布尔键"
}
print(f"有效的键类型: {valid_keys}")

# 键是唯一的
duplicate_keys = {'a': 1, 'b': 2, 'a': 3}  # 后面的值会覆盖前面的
print(f"重复键字典: {duplicate_keys}")

# 值可以是任意类型
mixed_values = {
    "number": 42,
    "string": "hello",
    "list": [1, 2, 3],
    "dict": {"nested": "value"},
    "function": len
}
print(f"混合值类型: {mixed_values}")

# 8. 实际应用示例
print("\n8. 实际应用示例")
print("-" * 30)

# 创建配置字典
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp"
    },
    "cache": {
        "enabled": True,
        "timeout": 300
    },
    "debug": False
}
print(f"配置信息: {config}")

# 创建商品库存字典
inventory = dict([
    ("laptop", {"price": 5999, "stock": 10}),
    ("mouse", {"price": 99, "stock": 50}),
    ("keyboard", {"price": 299, "stock": 30})
])
print(f"库存信息: {inventory}")

print("\n" + "=" * 50)
print("字典创建方法总结：")
print("1. 花括号 {} - 最常用的方法")
print("2. dict() 函数 - 灵活的构造方法")
print("3. 字典推导式 - 简洁的生成方法")
print("4. zip() 函数 - 从序列创建")
print("5. copy() 方法 - 复制现有字典")
print("6. 嵌套结构 - 复杂数据组织")
print("=" * 50)

if __name__ == "__main__":
    print("\n程序执行完成！")
    print("请尝试修改代码，创建自己的字典。")