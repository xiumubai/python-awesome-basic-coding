#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字典方法 - 字典内置方法详解

学习目标：
1. 掌握字典的所有内置方法
2. 了解每个方法的用途和返回值
3. 学会在实际场景中应用这些方法
4. 理解字典视图对象的特性

作者：Python学习教程
日期：2024年
"""

print("=" * 50)
print("字典方法 - 字典内置方法详解")
print("=" * 50)

# 创建示例字典
original_dict = {
    "name": "张三",
    "age": 25,
    "city": "北京",
    "job": "工程师",
    "salary": 15000
}

print(f"原始字典: {original_dict}")

# 1. keys() - 获取所有键
print("\n1. keys() - 获取所有键")
print("-" * 30)

keys = original_dict.keys()
print(f"所有键: {keys}")
print(f"键的类型: {type(keys)}")
print(f"转换为列表: {list(keys)}")

# 键视图的动态特性
test_dict = original_dict.copy()
keys_view = test_dict.keys()
print(f"添加前的键: {list(keys_view)}")
test_dict["email"] = "zhangsan@example.com"
print(f"添加后的键: {list(keys_view)}")

# 2. values() - 获取所有值
print("\n2. values() - 获取所有值")
print("-" * 30)

values = original_dict.values()
print(f"所有值: {values}")
print(f"值的类型: {type(values)}")
print(f"转换为列表: {list(values)}")

# 值的统计操作
print(f"值的数量: {len(values)}")
print(f"是否包含'北京': {'北京' in values}")

# 3. items() - 获取所有键值对
print("\n3. items() - 获取所有键值对")
print("-" * 30)

items = original_dict.items()
print(f"所有键值对: {items}")
print(f"键值对类型: {type(items)}")
print(f"转换为列表: {list(items)}")

# 键值对的遍历
print("遍历键值对:")
for key, value in original_dict.items():
    print(f"  {key}: {value}")

# 4. get() - 安全获取值
print("\n4. get() - 安全获取值")
print("-" * 30)

print(f"获取姓名: {original_dict.get('name')}")
print(f"获取不存在的键: {original_dict.get('phone')}")
print(f"获取不存在的键（带默认值）: {original_dict.get('phone', '未提供')}")

# get()与直接访问的对比
try:
    value = original_dict['phone']
except KeyError:
    print("直接访问不存在的键会抛出KeyError")

# 5. pop() - 删除并返回值
print("\n5. pop() - 删除并返回值")
print("-" * 30)

test_dict = original_dict.copy()
print(f"删除前: {test_dict}")

# 删除存在的键
removed_salary = test_dict.pop('salary')
print(f"删除的薪资: {removed_salary}")
print(f"删除后: {test_dict}")

# 删除不存在的键（带默认值）
removed_phone = test_dict.pop('phone', '无电话')
print(f"删除不存在的电话: {removed_phone}")

# 删除不存在的键（不带默认值）会抛出异常
try:
    test_dict.pop('nonexistent')
except KeyError:
    print("删除不存在的键（无默认值）会抛出KeyError")

# 6. popitem() - 删除并返回最后一个键值对
print("\n6. popitem() - 删除并返回最后一个键值对")
print("-" * 30)

test_dict = original_dict.copy()
print(f"删除前: {test_dict}")

# Python 3.7+保证字典有序，popitem()删除最后插入的项
last_item = test_dict.popitem()
print(f"删除的最后一项: {last_item}")
print(f"删除后: {test_dict}")

# 空字典调用popitem()会抛出异常
empty_dict = {}
try:
    empty_dict.popitem()
except KeyError:
    print("空字典调用popitem()会抛出KeyError")

# 7. update() - 更新字典
print("\n7. update() - 更新字典")
print("-" * 30)

test_dict = original_dict.copy()
print(f"更新前: {test_dict}")

# 使用字典更新
update_data = {'age': 26, 'department': 'IT', 'experience': 3}
test_dict.update(update_data)
print(f"字典更新后: {test_dict}")

# 使用关键字参数更新
test_dict.update(city='上海', salary=18000)
print(f"关键字更新后: {test_dict}")

# 使用键值对序列更新
test_dict.update([('hobby', '编程'), ('language', 'Python')])
print(f"序列更新后: {test_dict}")

# 8. setdefault() - 获取值或设置默认值
print("\n8. setdefault() - 获取值或设置默认值")
print("-" * 30)

test_dict = original_dict.copy()
print(f"原字典: {test_dict}")

# 获取已存在的键
existing_value = test_dict.setdefault('name', '默认姓名')
print(f"已存在的键'name': {existing_value}")
print(f"字典未改变: {test_dict}")

# 设置不存在的键
new_value = test_dict.setdefault('phone', '138****1234')
print(f"新设置的'phone': {new_value}")
print(f"字典已更新: {test_dict}")

# setdefault()的实际应用：分组
data = ['apple', 'banana', 'apricot', 'blueberry', 'cherry']
groups = {}
for item in data:
    first_letter = item[0]
    groups.setdefault(first_letter, []).append(item)
print(f"按首字母分组: {groups}")

# 9. clear() - 清空字典
print("\n9. clear() - 清空字典")
print("-" * 30)

test_dict = original_dict.copy()
print(f"清空前: {test_dict}")
test_dict.clear()
print(f"清空后: {test_dict}")
print(f"字典对象仍存在: {type(test_dict)}")

# 10. copy() - 浅拷贝字典
print("\n10. copy() - 浅拷贝字典")
print("-" * 30)

# 创建包含可变对象的字典
complex_dict = {
    'name': '张三',
    'scores': [85, 90, 78],
    'info': {'age': 25, 'city': '北京'}
}

print(f"原字典: {complex_dict}")

# 浅拷贝
shallow_copy = complex_dict.copy()
print(f"浅拷贝: {shallow_copy}")

# 修改拷贝的简单值
shallow_copy['name'] = '李四'
print(f"修改拷贝的name后:")
print(f"  原字典: {complex_dict['name']}")
print(f"  拷贝字典: {shallow_copy['name']}")

# 修改拷贝的可变对象
shallow_copy['scores'].append(95)
print(f"修改拷贝的scores后:")
print(f"  原字典: {complex_dict['scores']}")
print(f"  拷贝字典: {shallow_copy['scores']}")

# 深拷贝对比
import copy
deep_copy = copy.deepcopy(complex_dict)
deep_copy['scores'].append(100)
print(f"深拷贝修改后:")
print(f"  原字典: {complex_dict['scores']}")
print(f"  深拷贝: {deep_copy['scores']}")

# 11. fromkeys() - 类方法创建字典
print("\n11. fromkeys() - 类方法创建字典")
print("-" * 30)

# 使用序列创建字典
keys = ['name', 'age', 'city', 'job']
default_dict = dict.fromkeys(keys)
print(f"默认值字典: {default_dict}")

# 指定默认值
default_dict2 = dict.fromkeys(keys, '未设置')
print(f"指定默认值: {default_dict2}")

# 注意：可变对象作为默认值的陷阱
default_dict3 = dict.fromkeys(['a', 'b', 'c'], [])
print(f"可变默认值: {default_dict3}")
default_dict3['a'].append(1)
print(f"修改一个列表后: {default_dict3}")
print("注意：所有键共享同一个列表对象！")

# 12. 字典视图对象的高级操作
print("\n12. 字典视图对象的高级操作")
print("-" * 30)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 3, 'd': 4}

keys1 = dict1.keys()
keys2 = dict2.keys()

# 集合操作
print(f"字典1的键: {keys1}")
print(f"字典2的键: {keys2}")
print(f"键的交集: {keys1 & keys2}")
print(f"键的并集: {keys1 | keys2}")
print(f"键的差集: {keys1 - keys2}")
print(f"键的对称差集: {keys1 ^ keys2}")

# 项目视图的集合操作
items1 = dict1.items()
items2 = dict2.items()
print(f"\n项目交集: {items1 & items2}")
print(f"项目并集: {items1 | items2}")

# 13. 实际应用示例
print("\n13. 实际应用示例")
print("-" * 30)

# 统计字符频率
text = "hello world python programming"
char_count = {}
for char in text:
    if char.isalpha():  # 只统计字母
        char_count[char] = char_count.get(char, 0) + 1

print(f"字符频率统计: {char_count}")

# 使用setdefault()实现相同功能
char_count2 = {}
for char in text:
    if char.isalpha():
        char_count2.setdefault(char, 0)
        char_count2[char] += 1

print(f"使用setdefault统计: {char_count2}")

# 字典合并的不同策略
def merge_dicts_sum_values(*dicts):
    """合并字典，相同键的值相加"""
    result = {}
    for d in dicts:
        for key, value in d.items():
            result[key] = result.get(key, 0) + value
    return result

sales_q1 = {'apple': 100, 'banana': 150, 'orange': 80}
sales_q2 = {'apple': 120, 'banana': 130, 'grape': 90}
total_sales = merge_dicts_sum_values(sales_q1, sales_q2)
print(f"\n季度销售合计: {total_sales}")

# 14. 性能比较
print("\n14. 性能比较")
print("-" * 30)

import time

# 创建大字典
large_dict = {f"key_{i}": i for i in range(10000)}

# 测试不同访问方法的性能
start = time.time()
for i in range(1000):
    value = large_dict.get(f"key_{i}", None)
get_time = time.time() - start

start = time.time()
for i in range(1000):
    try:
        value = large_dict[f"key_{i}"]
    except KeyError:
        value = None
direct_time = time.time() - start

print(f"get()方法耗时: {get_time:.6f}秒")
print(f"直接访问耗时: {direct_time:.6f}秒")
print(f"性能比较: get()方法约为直接访问的{get_time/direct_time:.2f}倍")

print("\n" + "=" * 50)
print("字典方法总结：")
print("1. keys(), values(), items() - 获取视图对象")
print("2. get(key, default) - 安全获取值")
print("3. pop(key, default) - 删除并返回值")
print("4. popitem() - 删除最后一项")
print("5. update() - 批量更新")
print("6. setdefault() - 获取或设置默认值")
print("7. clear() - 清空字典")
print("8. copy() - 浅拷贝")
print("9. fromkeys() - 类方法创建字典")
print("=" * 50)

if __name__ == "__main__":
    print("\n程序执行完成！")
    print("请尝试修改代码，深入理解各种字典方法的用法。")