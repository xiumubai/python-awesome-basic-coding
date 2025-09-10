#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
StopIteration异常处理

本模块详细介绍StopIteration异常的机制、处理方法和最佳实践。
StopIteration是迭代器协议的核心组成部分，正确理解和处理这个异常
对于编写健壮的迭代器代码至关重要。

学习目标：
1. 理解StopIteration异常的作用和机制
2. 掌握StopIteration异常的处理方法
3. 学会在自定义迭代器中正确使用StopIteration
4. 了解StopIteration的高级用法和注意事项
"""

# 1. StopIteration异常基础
print("=== 1. StopIteration异常基础 ===")

# StopIteration是迭代器耗尽时抛出的异常
my_list = [1, 2, 3]
iterator = iter(my_list)

print("正常迭代:")
try:
    print(f"第1个元素: {next(iterator)}")
    print(f"第2个元素: {next(iterator)}")
    print(f"第3个元素: {next(iterator)}")
    print(f"第4个元素: {next(iterator)}")  # 这里会抛出StopIteration
except StopIteration:
    print("捕获到StopIteration异常 - 迭代器已耗尽")

# 2. StopIteration异常的详细信息
print("\n=== 2. StopIteration异常的详细信息 ===")

class DetailedIterator:
    """展示StopIteration异常详细信息的迭代器"""
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            # 可以在StopIteration中包含返回值
            raise StopIteration(f"迭代完成，共处理了{self.index}个元素")
        value = self.data[self.index]
        self.index += 1
        return value

detailed_iter = DetailedIterator(["a", "b", "c"])

print("使用带详细信息的StopIteration:")
try:
    while True:
        print(f"元素: {next(detailed_iter)}")
except StopIteration as e:
    print(f"异常信息: {e}")
    print(f"异常值: {e.value}")

# 3. 不同的异常处理策略
print("\n=== 3. 不同的异常处理策略 ===")

# 策略1: 使用try-except处理
def iterate_with_exception(iterable):
    """使用异常处理的迭代方式"""
    iterator = iter(iterable)
    result = []
    try:
        while True:
            result.append(next(iterator))
    except StopIteration:
        pass
    return result

# 策略2: 使用默认值
def iterate_with_default(iterable):
    """使用默认值的迭代方式"""
    iterator = iter(iterable)
    result = []
    sentinel = object()  # 创建唯一的哨兵对象
    while True:
        value = next(iterator, sentinel)
        if value is sentinel:
            break
        result.append(value)
    return result

# 策略3: 使用for循环（推荐）
def iterate_with_for(iterable):
    """使用for循环的迭代方式（推荐）"""
    return list(iterable)

test_data = [1, 2, 3, 4, 5]
print(f"原数据: {test_data}")
print(f"异常处理方式: {iterate_with_exception(test_data)}")
print(f"默认值方式: {iterate_with_default(test_data)}")
print(f"for循环方式: {iterate_with_for(test_data)}")

# 4. 自定义迭代器中的StopIteration
print("\n=== 4. 自定义迭代器中的StopIteration ===")

class CountdownIterator:
    """倒计时迭代器"""
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration("倒计时结束")
        self.current -= 1
        return self.current + 1

print("倒计时迭代器:")
countdown = CountdownIterator(5)
for count in countdown:
    print(f"倒计时: {count}")

# 尝试继续迭代已耗尽的迭代器
print("\n尝试继续迭代已耗尽的迭代器:")
try:
    next(countdown)
except StopIteration as e:
    print(f"迭代器已耗尽: {e}")

# 5. 条件停止的迭代器
print("\n=== 5. 条件停止的迭代器 ===")

class ConditionalIterator:
    """条件停止迭代器"""
    def __init__(self, data, condition):
        self.data = data
        self.index = 0
        self.condition = condition
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            if self.condition(value):
                return value
        raise StopIteration("没有更多满足条件的元素")

# 只返回偶数
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_iter = ConditionalIterator(data, lambda x: x % 2 == 0)

print(f"原数据: {data}")
print("只迭代偶数:")
for even in even_iter:
    print(f"偶数: {even}")

# 6. 嵌套迭代器的异常处理
print("\n=== 6. 嵌套迭代器的异常处理 ===")

class NestedIterator:
    """嵌套迭代器 - 迭代嵌套列表"""
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.outer_index = 0
        self.inner_iterator = None
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.outer_index < len(self.nested_list):
            if self.inner_iterator is None:
                self.inner_iterator = iter(self.nested_list[self.outer_index])
            
            try:
                return next(self.inner_iterator)
            except StopIteration:
                # 内层迭代器耗尽，移动到下一个
                self.inner_iterator = None
                self.outer_index += 1
        
        raise StopIteration("所有嵌套列表都已迭代完成")

nested_data = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
nested_iter = NestedIterator(nested_data)

print(f"嵌套数据: {nested_data}")
print("扁平化迭代:")
for item in nested_iter:
    print(f"元素: {item}")

# 7. 异常链和上下文
print("\n=== 7. 异常链和上下文 ===")

class ErrorProneIterator:
    """可能出错的迭代器"""
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration("正常结束")
        
        try:
            # 模拟可能出错的操作
            value = self.data[self.index]
            if value == "error":
                raise ValueError("遇到错误值")
            self.index += 1
            return value
        except ValueError as e:
            # 将其他异常转换为StopIteration
            raise StopIteration(f"因错误提前结束: {e}") from e

error_data = ["a", "b", "error", "c", "d"]
error_iter = ErrorProneIterator(error_data)

print(f"包含错误的数据: {error_data}")
print("迭代直到遇到错误:")
try:
    for item in error_iter:
        print(f"元素: {item}")
except StopIteration as e:
    print(f"迭代停止: {e}")
    if e.__cause__:
        print(f"原因: {e.__cause__}")

# 8. 迭代器状态管理
print("\n=== 8. 迭代器状态管理 ===")

class StatefulIterator:
    """有状态的迭代器"""
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.is_exhausted = False
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.is_exhausted:
            raise StopIteration("迭代器已被标记为耗尽")
        
        if self.index >= len(self.data):
            self.is_exhausted = True
            raise StopIteration(f"迭代完成，共处理{self.index}个元素")
        
        value = self.data[self.index]
        self.index += 1
        return value
    
    def reset(self):
        """重置迭代器"""
        self.index = 0
        self.is_exhausted = False
    
    def is_done(self):
        """检查是否完成"""
        return self.is_exhausted or self.index >= len(self.data)

stateful_data = ["x", "y", "z"]
stateful_iter = StatefulIterator(stateful_data)

print(f"数据: {stateful_data}")
print("第一次迭代:")
for item in stateful_iter:
    print(f"元素: {item}")

print(f"迭代器是否完成: {stateful_iter.is_done()}")

# 重置并再次迭代
stateful_iter.reset()
print("\n重置后再次迭代:")
for item in stateful_iter:
    print(f"元素: {item}")

# 9. 异常处理的性能考虑
print("\n=== 9. 异常处理的性能考虑 ===")

import time

def benchmark_iteration_methods(data, iterations=10000):
    """基准测试不同的迭代方法"""
    
    # 方法1: 使用异常处理
    start_time = time.time()
    for _ in range(iterations):
        iterator = iter(data)
        try:
            while True:
                next(iterator)
        except StopIteration:
            pass
    time1 = time.time() - start_time
    
    # 方法2: 使用默认值
    start_time = time.time()
    for _ in range(iterations):
        iterator = iter(data)
        sentinel = object()
        while next(iterator, sentinel) is not sentinel:
            pass
    time2 = time.time() - start_time
    
    # 方法3: 使用for循环
    start_time = time.time()
    for _ in range(iterations):
        for item in data:
            pass
    time3 = time.time() - start_time
    
    return time1, time2, time3

test_data = list(range(100))
time1, time2, time3 = benchmark_iteration_methods(test_data)

print(f"性能测试结果（{len(test_data)}个元素，10000次迭代）:")
print(f"异常处理方式: {time1:.6f} 秒")
print(f"默认值方式: {time2:.6f} 秒")
print(f"for循环方式: {time3:.6f} 秒")
print(f"for循环相对于异常处理快 {time1/time3:.2f} 倍")

# 10. 最佳实践和建议
print("\n=== 10. 最佳实践和建议 ===")

class BestPracticeIterator:
    """展示最佳实践的迭代器"""
    def __init__(self, data):
        if not hasattr(data, '__iter__'):
            raise TypeError("数据必须是可迭代的")
        self.data = list(data)  # 创建副本避免外部修改
        self.index = 0
    
    def __iter__(self):
        # 返回新的迭代器实例，支持多次迭代
        return BestPracticeIterator(self.data)
    
    def __next__(self):
        if self.index >= len(self.data):
            # 提供清晰的异常信息
            raise StopIteration(
                f"迭代完成: 已处理{self.index}个元素"
            )
        
        value = self.data[self.index]
        self.index += 1
        return value
    
    def __len__(self):
        """支持len()函数"""
        return len(self.data)
    
    def __repr__(self):
        """提供有用的字符串表示"""
        return f"BestPracticeIterator({self.data}, index={self.index})"

# 演示最佳实践
best_iter = BestPracticeIterator(["优", "秀", "实", "践"])
print(f"迭代器: {best_iter}")
print(f"长度: {len(best_iter)}")

print("迭代元素:")
for item in best_iter:
    print(f"元素: {item}")

# 支持多次迭代
print("\n再次迭代:")
for item in best_iter:
    print(f"元素: {item}")

if __name__ == "__main__":
    print("\n=== 总结 ===")
    print("1. StopIteration是迭代器协议的核心异常")
    print("2. 正确处理StopIteration确保程序健壮性")
    print("3. 优先使用for循环而不是手动异常处理")
    print("4. 在自定义迭代器中合理使用StopIteration")
    print("5. 考虑性能影响，选择合适的迭代方式")
    print("6. 提供清晰的异常信息有助于调试")