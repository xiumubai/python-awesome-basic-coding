#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
iter()和next()函数使用

本模块详细介绍Python内置的iter()和next()函数的各种用法。
这两个函数是迭代器协议的核心，掌握它们的用法对理解迭代器至关重要。

学习目标：
1. 掌握iter()函数的多种用法
2. 理解next()函数的参数和返回值
3. 学会使用iter()创建自定义迭代器
4. 了解iter()和next()的高级应用
"""

# 1. iter()函数基础用法
print("=== 1. iter()函数基础用法 ===")

# iter()从可迭代对象创建迭代器
my_list = [1, 2, 3, 4, 5]
list_iter = iter(my_list)
print(f"原列表: {my_list}")
print(f"迭代器类型: {type(list_iter)}")

# 使用next()获取元素
print("使用next()获取元素:")
print(f"第1个元素: {next(list_iter)}")
print(f"第2个元素: {next(list_iter)}")
print(f"第3个元素: {next(list_iter)}")

# 2. next()函数的默认值参数
print("\n=== 2. next()函数的默认值参数 ===")

# next()的第二个参数是默认值，当迭代器耗尽时返回
my_list = [1, 2, 3]
iterator = iter(my_list)

print("使用默认值参数:")
for i in range(5):
    value = next(iterator, "没有更多元素")
    print(f"第{i+1}次调用next(): {value}")

# 3. iter()函数的双参数形式
print("\n=== 3. iter()函数的双参数形式 ===")

# iter(callable, sentinel) - 调用callable直到返回sentinel值
import random

# 模拟掷骰子，直到掷出6
print("掷骰子直到出现6:")
dice_iter = iter(lambda: random.randint(1, 6), 6)
rolls = []
for roll in dice_iter:
    rolls.append(roll)
    if len(rolls) > 10:  # 防止无限循环
        break
print(f"掷骰子结果: {rolls}")

# 4. 从文件读取示例
print("\n=== 4. 从文件读取示例 ===")

# 创建测试文件
test_content = """line1
line2
line3
END
line4
line5"""

with open('test_input.txt', 'w') as f:
    f.write(test_content)

# 使用iter()读取文件直到遇到"END"
print("读取文件直到遇到'END':")
with open('test_input.txt', 'r') as f:
    line_iter = iter(f.readline, 'END\n')
    for line_num, line in enumerate(line_iter, 1):
        print(f"第{line_num}行: {line.strip()}")

# 清理文件
import os
if os.path.exists('test_input.txt'):
    os.remove('test_input.txt')

# 5. 计数器示例
print("\n=== 5. 计数器示例 ===")

class Counter:
    """简单计数器"""
    def __init__(self, start=0):
        self.value = start
    
    def __call__(self):
        self.value += 1
        return self.value

# 使用计数器创建迭代器
counter = Counter()
print("计数器迭代器（停止在5）:")
counter_iter = iter(counter, 5)
for count in counter_iter:
    print(f"计数: {count}")

# 6. 用户输入示例
print("\n=== 6. 用户输入示例（模拟） ===")

# 模拟用户输入，直到输入"quit"
input_data = ["hello", "world", "python", "quit", "ignored"]
input_iter = iter(input_data)

# 创建一个模拟input函数
def mock_input(prompt=""):
    try:
        return next(input_iter)
    except StopIteration:
        return "quit"

print("模拟用户输入（直到输入'quit'）:")
user_iter = iter(lambda: mock_input("请输入: "), "quit")
for user_input in user_iter:
    print(f"用户输入: {user_input}")

# 7. 高级iter()用法
print("\n=== 7. 高级iter()用法 ===")

# 从字符串创建迭代器
string = "Python"
string_iter = iter(string)
print(f"字符串 '{string}' 的字符:")
for char in string_iter:
    print(f"字符: {char}")

# 从字典创建迭代器
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(f"\n字典 {my_dict} 的迭代:")

# 迭代键
key_iter = iter(my_dict)
print("键迭代:")
for key in key_iter:
    print(f"键: {key}")

# 迭代值
value_iter = iter(my_dict.values())
print("值迭代:")
for value in value_iter:
    print(f"值: {value}")

# 迭代键值对
item_iter = iter(my_dict.items())
print("键值对迭代:")
for key, value in item_iter:
    print(f"键值对: {key} -> {value}")

# 8. next()的错误处理
print("\n=== 8. next()的错误处理 ===")

my_list = [1, 2, 3]
iterator = iter(my_list)

print("正常获取元素:")
for i in range(3):
    print(f"元素: {next(iterator)}")

print("\n尝试获取更多元素:")
# 方法1: 使用默认值
value = next(iterator, "迭代器已耗尽")
print(f"使用默认值: {value}")

# 方法2: 捕获异常
try:
    value = next(iterator)
except StopIteration:
    print("捕获StopIteration异常")

# 9. 迭代器链
print("\n=== 9. 迭代器链 ===")

# 创建多个迭代器并链接
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# 手动链接迭代器
class ChainIterator:
    """链接多个迭代器"""
    def __init__(self, *iterables):
        self.iterators = [iter(iterable) for iterable in iterables]
        self.current_index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current_index < len(self.iterators):
            try:
                return next(self.iterators[self.current_index])
            except StopIteration:
                self.current_index += 1
        raise StopIteration

print("链接多个迭代器:")
chain_iter = ChainIterator(list1, list2, list3)
for value in chain_iter:
    print(f"链接值: {value}")

# 10. 迭代器的性能测试
print("\n=== 10. 迭代器的性能测试 ===")

import time

# 比较不同遍历方式的性能
data = list(range(100000))

# 方法1: 直接遍历列表
start_time = time.time()
count1 = 0
for item in data:
    count1 += 1
time1 = time.time() - start_time

# 方法2: 使用迭代器
start_time = time.time()
count2 = 0
iterator = iter(data)
while True:
    try:
        next(iterator)
        count2 += 1
    except StopIteration:
        break
time2 = time.time() - start_time

print(f"直接遍历列表: {count1} 个元素，耗时 {time1:.6f} 秒")
print(f"使用迭代器: {count2} 个元素，耗时 {time2:.6f} 秒")
print(f"性能比较: 迭代器相对耗时 {time2/time1:.2f} 倍")

# 11. 实用工具函数
print("\n=== 11. 实用工具函数 ===")

def peek_iterator(iterator, n=1):
    """窥视迭代器的前n个元素，不消耗迭代器"""
    import itertools
    iterator, peek_iter = itertools.tee(iterator)
    peeked = []
    for _ in range(n):
        try:
            peeked.append(next(peek_iter))
        except StopIteration:
            break
    return peeked, iterator

def consume_iterator(iterator, n=None):
    """消耗迭代器的n个元素"""
    if n is None:
        # 消耗所有元素
        for _ in iterator:
            pass
    else:
        # 消耗n个元素
        for _ in range(n):
            try:
                next(iterator)
            except StopIteration:
                break

# 测试工具函数
test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_iter = iter(test_data)

# 窥视前3个元素
peeked, remaining_iter = peek_iterator(test_iter, 3)
print(f"窥视的元素: {peeked}")

# 消耗2个元素
consume_iterator(remaining_iter, 2)
print(f"消耗2个元素后，下一个元素: {next(remaining_iter)}")

if __name__ == "__main__":
    print("\n=== 总结 ===")
    print("1. iter()函数可以从可迭代对象创建迭代器")
    print("2. iter(callable, sentinel)可以创建调用迭代器")
    print("3. next()函数可以指定默认值避免StopIteration异常")
    print("4. 迭代器提供了统一的遍历接口")
    print("5. 合理使用iter()和next()可以实现复杂的迭代逻辑")