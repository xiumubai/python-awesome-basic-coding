#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
迭代器基础和协议

本模块介绍Python中迭代器的基本概念和迭代器协议。
迭代器协议包括两个方法：__iter__() 和 __next__()

学习目标：
1. 理解可迭代对象和迭代器的区别
2. 掌握迭代器协议的实现
3. 了解迭代器的工作原理
4. 学会判断对象是否可迭代
"""

# 1. 可迭代对象 vs 迭代器
print("=== 1. 可迭代对象 vs 迭代器 ===")

# 可迭代对象：实现了__iter__方法的对象
# 迭代器：实现了__iter__和__next__方法的对象

# 列表是可迭代对象，但不是迭代器
my_list = [1, 2, 3, 4, 5]
print(f"列表: {my_list}")
print(f"列表是否有__iter__方法: {hasattr(my_list, '__iter__')}")
print(f"列表是否有__next__方法: {hasattr(my_list, '__next__')}")

# 从可迭代对象获取迭代器
list_iterator = iter(my_list)
print(f"\n迭代器: {list_iterator}")
print(f"迭代器是否有__iter__方法: {hasattr(list_iterator, '__iter__')}")
print(f"迭代器是否有__next__方法: {hasattr(list_iterator, '__next__')}")

# 2. 迭代器协议演示
print("\n=== 2. 迭代器协议演示 ===")

# 使用next()函数逐个获取元素
my_list = [1, 2, 3]
iterator = iter(my_list)

print("使用next()逐个获取元素:")
try:
    print(f"第1个元素: {next(iterator)}")
    print(f"第2个元素: {next(iterator)}")
    print(f"第3个元素: {next(iterator)}")
    print(f"第4个元素: {next(iterator)}")  # 这里会抛出StopIteration异常
except StopIteration:
    print("迭代器已耗尽，抛出StopIteration异常")

# 3. 手动实现迭代器协议
print("\n=== 3. 手动实现迭代器协议 ===")

class NumberIterator:
    """一个简单的数字迭代器，从start到end"""
    
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        """返回迭代器对象本身"""
        return self
    
    def __next__(self):
        """返回下一个值"""
        if self.current < self.end:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

# 使用自定义迭代器
print("使用自定义迭代器:")
number_iter = NumberIterator(1, 5)
for num in number_iter:
    print(f"数字: {num}")

# 4. 迭代器的一次性特性
print("\n=== 4. 迭代器的一次性特性 ===")

# 迭代器只能使用一次
my_list = [1, 2, 3]
iterator = iter(my_list)

print("第一次遍历:")
for item in iterator:
    print(f"元素: {item}")

print("\n第二次遍历:")
for item in iterator:
    print(f"元素: {item}")  # 不会输出任何内容，因为迭代器已耗尽

print("迭代器已耗尽，需要重新创建")

# 5. 检查对象是否可迭代
print("\n=== 5. 检查对象是否可迭代 ===")

def is_iterable(obj):
    """检查对象是否可迭代"""
    try:
        iter(obj)
        return True
    except TypeError:
        return False

# 测试不同类型的对象
test_objects = [
    [1, 2, 3],          # 列表
    (1, 2, 3),          # 元组
    {1, 2, 3},          # 集合
    {'a': 1, 'b': 2},   # 字典
    "hello",            # 字符串
    range(5),           # range对象
    42,                 # 整数
    None                # None
]

for obj in test_objects:
    print(f"{obj} 是否可迭代: {is_iterable(obj)}")

# 6. 内置可迭代对象的迭代器
print("\n=== 6. 内置可迭代对象的迭代器 ===")

# 字符串迭代器
string = "Python"
string_iter = iter(string)
print(f"字符串 '{string}' 的迭代器:")
for char in string_iter:
    print(f"字符: {char}")

# 字典迭代器（默认迭代键）
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(f"\n字典 {my_dict} 的键迭代:")
for key in my_dict:
    print(f"键: {key}")

# 字典值迭代器
print("\n字典值迭代:")
for value in my_dict.values():
    print(f"值: {value}")

# 字典项迭代器
print("\n字典项迭代:")
for key, value in my_dict.items():
    print(f"键值对: {key} -> {value}")

# 7. 迭代器与for循环的关系
print("\n=== 7. 迭代器与for循环的关系 ===")

# for循环的工作原理
print("for循环的工作原理演示:")
my_list = [1, 2, 3]

# 这是for循环内部的工作方式
iterator = iter(my_list)
while True:
    try:
        item = next(iterator)
        print(f"处理元素: {item}")
    except StopIteration:
        print("迭代完成")
        break

if __name__ == "__main__":
    print("\n=== 总结 ===")
    print("1. 可迭代对象实现__iter__方法，迭代器实现__iter__和__next__方法")
    print("2. 迭代器是一次性的，耗尽后需要重新创建")
    print("3. for循环内部使用iter()和next()来遍历对象")
    print("4. 可以使用iter()函数检查对象是否可迭代")
    print("5. Python的许多内置类型都是可迭代的")