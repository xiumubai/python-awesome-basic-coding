#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
itertools模块使用

本模块详细介绍Python标准库中的itertools模块，这是一个提供高效迭代器工具的模块。
itertools模块包含了许多用于创建和操作迭代器的函数，是处理迭代器的强大工具箱。

学习目标：
1. 掌握itertools模块的主要函数
2. 学会使用无限迭代器
3. 理解组合迭代器的用法
4. 掌握迭代器的高级操作技巧
"""

import itertools
import operator
from itertools import *

# 1. 无限迭代器
print("=== 1. 无限迭代器 ===")

# count() - 无限计数器
print("count() - 无限计数器:")
counter = itertools.count(10, 2)  # 从10开始，步长为2
for i, value in enumerate(counter):
    print(f"第{i+1}个值: {value}")
    if i >= 4:  # 只显示前5个
        break

# cycle() - 无限循环
print("\ncycle() - 无限循环:")
colors = ['红', '绿', '蓝']
color_cycle = itertools.cycle(colors)
for i, color in enumerate(color_cycle):
    print(f"第{i+1}个颜色: {color}")
    if i >= 7:  # 只显示前8个
        break

# repeat() - 重复值
print("\nrepeat() - 重复值:")
# 无限重复
repeater = itertools.repeat('Hello', 5)  # 重复5次
for value in repeater:
    print(f"重复值: {value}")

# 2. 终止迭代器
print("\n=== 2. 终止迭代器 ===")

# accumulate() - 累积操作
print("accumulate() - 累积操作:")
numbers = [1, 2, 3, 4, 5]
print(f"原数据: {numbers}")

# 累积求和（默认）
sum_acc = list(itertools.accumulate(numbers))
print(f"累积求和: {sum_acc}")

# 累积乘积
product_acc = list(itertools.accumulate(numbers, operator.mul))
print(f"累积乘积: {product_acc}")

# 累积最大值
max_acc = list(itertools.accumulate(numbers, max))
print(f"累积最大值: {max_acc}")

# chain() - 链接迭代器
print("\nchain() - 链接迭代器:")
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [10, 20]
chained = itertools.chain(list1, list2, list3)
print(f"链接结果: {list(chained)}")

# chain.from_iterable() - 从可迭代对象链接
print("\nchain.from_iterable() - 从可迭代对象链接:")
nested_lists = [[1, 2], [3, 4], [5, 6]]
flattened = itertools.chain.from_iterable(nested_lists)
print(f"扁平化结果: {list(flattened)}")

# compress() - 根据选择器过滤
print("\ncompress() - 根据选择器过滤:")
data = ['a', 'b', 'c', 'd', 'e']
selectors = [1, 0, 1, 0, 1]  # 1表示选择，0表示跳过
compressed = itertools.compress(data, selectors)
print(f"原数据: {data}")
print(f"选择器: {selectors}")
print(f"过滤结果: {list(compressed)}")

# dropwhile() 和 takewhile()
print("\ndropwhile() 和 takewhile():")
data = [1, 3, 5, 24, 7, 11, 9, 2]
print(f"原数据: {data}")

# dropwhile - 跳过满足条件的元素
dropped = itertools.dropwhile(lambda x: x < 10, data)
print(f"跳过小于10的元素: {list(dropped)}")

# takewhile - 取满足条件的元素
taken = itertools.takewhile(lambda x: x < 10, data)
print(f"取小于10的元素: {list(taken)}")

# filterfalse() - 过滤假值
print("\nfilterfalse() - 过滤假值:")
data = [0, 1, 2, 0, 3, 4, 0, 5]
filtered = itertools.filterfalse(lambda x: x == 0, data)
print(f"原数据: {data}")
print(f"过滤掉0: {list(filtered)}")

# islice() - 切片迭代器
print("\nislice() - 切片迭代器:")
data = range(20)
print(f"原数据: {list(data)}")

# 取前5个
first_5 = itertools.islice(data, 5)
print(f"前5个: {list(first_5)}")

# 取索引5到10
middle = itertools.islice(range(20), 5, 10)
print(f"索引5到10: {list(middle)}")

# 每隔2个取一个
every_2nd = itertools.islice(range(20), 0, None, 2)
print(f"每隔2个: {list(every_2nd)}")

# 3. 组合迭代器
print("\n=== 3. 组合迭代器 ===")

# product() - 笛卡尔积
print("product() - 笛卡尔积:")
colors = ['红', '蓝']
sizes = ['S', 'M', 'L']
products = itertools.product(colors, sizes)
print("颜色和尺寸的组合:")
for color, size in products:
    print(f"  {color}-{size}")

# 自己与自己的笛卡尔积
print("\n数字的平方组合:")
numbers = [1, 2, 3]
square_products = itertools.product(numbers, repeat=2)
for x, y in square_products:
    print(f"  ({x}, {y})")

# permutations() - 排列
print("\npermutations() - 排列:")
letters = ['A', 'B', 'C']
perms = itertools.permutations(letters, 2)  # 2个元素的排列
print("2个字母的排列:")
for perm in perms:
    print(f"  {''.join(perm)}")

# 全排列
full_perms = itertools.permutations(letters)
print("\n全排列:")
for perm in full_perms:
    print(f"  {''.join(perm)}")

# combinations() - 组合
print("\ncombinations() - 组合:")
numbers = [1, 2, 3, 4]
combos = itertools.combinations(numbers, 2)  # 2个元素的组合
print("2个数字的组合:")
for combo in combos:
    print(f"  {combo}")

# combinations_with_replacement() - 可重复组合
print("\ncombinations_with_replacement() - 可重复组合:")
numbers = [1, 2, 3]
replace_combos = itertools.combinations_with_replacement(numbers, 2)
print("可重复的2个数字组合:")
for combo in replace_combos:
    print(f"  {combo}")

# 4. 分组迭代器
print("\n=== 4. 分组迭代器 ===")

# groupby() - 分组
print("groupby() - 分组:")
data = [('张三', '男'), ('李四', '男'), ('王五', '女'), ('赵六', '女'), ('钱七', '男')]
print(f"原数据: {data}")

# 按性别分组（需要先排序）
sorted_data = sorted(data, key=lambda x: x[1])
print("\n按性别分组:")
for gender, group in itertools.groupby(sorted_data, key=lambda x: x[1]):
    names = [person[0] for person in group]
    print(f"  {gender}: {names}")

# 按字符串长度分组
words = ['a', 'bb', 'ccc', 'dd', 'eeee', 'f']
sorted_words = sorted(words, key=len)
print(f"\n单词: {words}")
print("按长度分组:")
for length, group in itertools.groupby(sorted_words, key=len):
    word_list = list(group)
    print(f"  长度{length}: {word_list}")

# 5. 实用工具函数
print("\n=== 5. 实用工具函数 ===")

# tee() - 复制迭代器
print("tee() - 复制迭代器:")
original = iter([1, 2, 3, 4, 5])
iter1, iter2, iter3 = itertools.tee(original, 3)  # 复制成3个

print(f"迭代器1: {list(iter1)}")
print(f"迭代器2: {list(iter2)}")
print(f"迭代器3: {list(iter3)}")

# zip_longest() - 最长拉链
print("\nzip_longest() - 最长拉链:")
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']
zipped = itertools.zip_longest(list1, list2, fillvalue='X')
print(f"列表1: {list1}")
print(f"列表2: {list2}")
print(f"最长拉链: {list(zipped)}")

# 6. 高级应用示例
print("\n=== 6. 高级应用示例 ===")

# 示例1: 批处理数据
def batch_data(iterable, batch_size):
    """将数据分批处理"""
    iterator = iter(iterable)
    while True:
        batch = list(itertools.islice(iterator, batch_size))
        if not batch:
            break
        yield batch

data = range(13)
print(f"原数据: {list(data)}")
print("分批处理（每批3个）:")
for i, batch in enumerate(batch_data(data, 3), 1):
    print(f"  批次{i}: {batch}")

# 示例2: 滑动窗口
def sliding_window(iterable, window_size):
    """创建滑动窗口"""
    iterators = itertools.tee(iterable, window_size)
    for i, it in enumerate(iterators):
        # 跳过前i个元素
        for _ in range(i):
            next(it, None)
    return zip(*iterators)

data = [1, 2, 3, 4, 5, 6, 7]
print(f"\n原数据: {data}")
print("滑动窗口（窗口大小3）:")
for window in sliding_window(data, 3):
    print(f"  窗口: {window}")

# 示例3: 扁平化嵌套结构
def flatten(nested_iterable):
    """扁平化嵌套结构"""
    for item in nested_iterable:
        if hasattr(item, '__iter__') and not isinstance(item, (str, bytes)):
            yield from flatten(item)
        else:
            yield item

nested_data = [1, [2, 3], [4, [5, 6]], 7]
print(f"\n嵌套数据: {nested_data}")
flattened = list(flatten(nested_data))
print(f"扁平化结果: {flattened}")

# 示例4: 数据管道
print("\n示例4: 数据管道")
def create_data_pipeline(data):
    """创建数据处理管道"""
    # 步骤1: 过滤正数
    positive = filter(lambda x: x > 0, data)
    
    # 步骤2: 平方
    squared = map(lambda x: x**2, positive)
    
    # 步骤3: 累积求和
    accumulated = itertools.accumulate(squared)
    
    # 步骤4: 取前5个
    limited = itertools.islice(accumulated, 5)
    
    return limited

input_data = [-2, 1, -1, 2, 3, -3, 4, 5, 6, 7]
print(f"输入数据: {input_data}")
pipeline_result = list(create_data_pipeline(input_data))
print(f"管道结果: {pipeline_result}")

# 7. 性能优化技巧
print("\n=== 7. 性能优化技巧 ===")

import time

def performance_comparison():
    """性能对比"""
    data = range(100000)
    
    # 方法1: 使用列表推导式
    start_time = time.time()
    result1 = [x**2 for x in data if x % 2 == 0][:1000]
    time1 = time.time() - start_time
    
    # 方法2: 使用itertools
    start_time = time.time()
    filtered = filter(lambda x: x % 2 == 0, data)
    squared = map(lambda x: x**2, filtered)
    result2 = list(itertools.islice(squared, 1000))
    time2 = time.time() - start_time
    
    print(f"列表推导式: {time1:.6f} 秒")
    print(f"itertools: {time2:.6f} 秒")
    print(f"结果相同: {result1 == result2}")
    
    if time1 > time2:
        print(f"itertools 快 {time1/time2:.2f} 倍")
    else:
        print(f"列表推导式 快 {time2/time1:.2f} 倍")

performance_comparison()

# 8. 实际应用场景
print("\n=== 8. 实际应用场景 ===")

# 场景1: 生成测试数据
print("场景1: 生成测试数据")
def generate_test_users(count):
    """生成测试用户数据"""
    names = itertools.cycle(['张三', '李四', '王五', '赵六'])
    ages = itertools.cycle(range(20, 60))
    genders = itertools.cycle(['男', '女'])
    
    for i, (name, age, gender) in enumerate(zip(names, ages, genders)):
        if i >= count:
            break
        yield f"用户{i+1}: {name}, {age}岁, {gender}"

test_users = list(generate_test_users(8))
for user in test_users:
    print(f"  {user}")

# 场景2: 配置组合测试
print("\n场景2: 配置组合测试")
browsers = ['Chrome', 'Firefox', 'Safari']
operating_systems = ['Windows', 'macOS', 'Linux']
versions = ['v1.0', 'v2.0']

print("测试配置组合:")
test_configs = itertools.product(browsers, operating_systems, versions)
for i, (browser, os, version) in enumerate(test_configs, 1):
    print(f"  配置{i}: {browser} on {os} {version}")

# 场景3: 数据分析
print("\n场景3: 数据分析")
sales_data = [
    ('2023-01', 1000), ('2023-01', 1500), ('2023-01', 800),
    ('2023-02', 1200), ('2023-02', 1800), ('2023-02', 900),
    ('2023-03', 1100), ('2023-03', 1600), ('2023-03', 1000)
]

print("月度销售汇总:")
sorted_sales = sorted(sales_data, key=lambda x: x[0])
for month, sales_group in itertools.groupby(sorted_sales, key=lambda x: x[0]):
    monthly_sales = [sale[1] for sale in sales_group]
    total = sum(monthly_sales)
    avg = total / len(monthly_sales)
    print(f"  {month}: 总计={total}, 平均={avg:.1f}, 次数={len(monthly_sales)}")

if __name__ == "__main__":
    print("\n=== 总结 ===")
    print("1. itertools提供了丰富的迭代器工具")
    print("2. 无限迭代器适合生成序列数据")
    print("3. 组合迭代器用于排列组合计算")
    print("4. 分组和过滤功能强大且高效")
    print("5. 合理使用itertools可以提高代码效率")
    print("6. itertools特别适合数据处理管道")