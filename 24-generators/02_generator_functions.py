#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成器函数的定义和使用

本模块介绍：
1. 生成器函数的定义规则
2. 多种生成器函数模式
3. 生成器函数的参数传递
4. 生成器函数的返回值处理
5. 生成器函数的嵌套使用
"""

import time
import random

# 1. 生成器函数的定义规则
print("=== 1. 生成器函数的定义规则 ===")
print("只要函数中包含yield关键字，就是生成器函数")
print()

def is_generator_function():
    """包含yield的函数就是生成器函数"""
    print("这是一个生成器函数")
    yield "Hello"
    return "这个return值会被忽略"  # return在生成器中会抛出StopIteration异常

def not_generator_function():
    """不包含yield的普通函数"""
    print("这是一个普通函数")
    return "Hello"

print("生成器函数调用:")
gen_func = is_generator_function()
print(f"类型: {type(gen_func)}")
print(f"值: {next(gen_func)}")

print("\n普通函数调用:")
normal_result = not_generator_function()
print(f"类型: {type(normal_result)}")
print(f"值: {normal_result}")
print()

# 2. 带参数的生成器函数
print("=== 2. 带参数的生成器函数 ===")

def countdown(start, step=1):
    """倒计时生成器"""
    print(f"开始倒计时，从{start}开始，步长{step}")
    current = start
    while current > 0:
        yield current
        current -= step
    print("倒计时结束！")

print("倒计时示例:")
for num in countdown(5, 1):
    print(f"倒计时: {num}")
print()

print("自定义步长倒计时:")
for num in countdown(10, 2):
    print(f"倒计时: {num}")
print()

# 3. 无限生成器函数
print("=== 3. 无限生成器函数 ===")

def infinite_sequence():
    """无限序列生成器"""
    num = 0
    while True:
        yield num
        num += 1

def even_numbers():
    """无限偶数生成器"""
    num = 0
    while True:
        yield num
        num += 2

print("无限序列（前10个）:")
inf_gen = infinite_sequence()
for i in range(10):
    print(f"序列值: {next(inf_gen)}")
print()

print("无限偶数序列（前5个）:")
even_gen = even_numbers()
for i in range(5):
    print(f"偶数: {next(even_gen)}")
print()

# 4. 条件生成器函数
print("=== 4. 条件生成器函数 ===")

def filter_generator(iterable, condition):
    """条件过滤生成器"""
    for item in iterable:
        if condition(item):
            yield item

def prime_generator(max_num):
    """质数生成器"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for num in range(2, max_num + 1):
        if is_prime(num):
            yield num

print("过滤偶数:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_filter = filter_generator(numbers, lambda x: x % 2 == 0)
for even in even_filter:
    print(f"偶数: {even}")
print()

print("20以内的质数:")
primes = prime_generator(20)
for prime in primes:
    print(f"质数: {prime}")
print()

# 5. 生成器函数的组合使用
print("=== 5. 生成器函数的组合使用 ===")

def number_generator(start, end):
    """数字生成器"""
    for i in range(start, end + 1):
        yield i

def square_generator(numbers):
    """平方生成器"""
    for num in numbers:
        yield num ** 2

def sum_generator(numbers, batch_size):
    """批量求和生成器"""
    batch = []
    for num in numbers:
        batch.append(num)
        if len(batch) == batch_size:
            yield sum(batch)
            batch = []
    if batch:  # 处理剩余的数字
        yield sum(batch)

print("生成器链式组合:")
nums = number_generator(1, 10)
squares = square_generator(nums)
batch_sums = sum_generator(squares, 3)

for batch_sum in batch_sums:
    print(f"批量和: {batch_sum}")
print()

# 6. 带状态的生成器函数
print("=== 6. 带状态的生成器函数 ===")

def stateful_generator():
    """带状态的生成器"""
    state = {'count': 0, 'total': 0}
    
    while True:
        value = yield state.copy()  # 返回状态副本
        if value is not None:
            state['count'] += 1
            state['total'] += value
            print(f"接收到值: {value}, 当前状态: {state}")

print("带状态的生成器示例:")
stateful_gen = stateful_generator()
print(f"初始状态: {next(stateful_gen)}")

# 发送数据并获取状态
state = stateful_gen.send(10)
print(f"发送10后的状态: {state}")

state = stateful_gen.send(20)
print(f"发送20后的状态: {state}")

state = stateful_gen.send(30)
print(f"发送30后的状态: {state}")
print()

# 7. 递归生成器函数
print("=== 7. 递归生成器函数 ===")

def fibonacci_recursive(n, a=0, b=1):
    """递归斐波那契生成器"""
    if n <= 0:
        return
    yield a
    yield from fibonacci_recursive(n - 1, b, a + b)

def tree_traversal(node):
    """树遍历生成器"""
    yield node['value']
    for child in node.get('children', []):
        yield from tree_traversal(child)

print("递归斐波那契数列（前8项）:")
for fib in fibonacci_recursive(8):
    print(f"斐波那契: {fib}")
print()

print("树遍历示例:")
tree = {
    'value': 'A',
    'children': [
        {
            'value': 'B',
            'children': [
                {'value': 'D'},
                {'value': 'E'}
            ]
        },
        {
            'value': 'C',
            'children': [
                {'value': 'F'}
            ]
        }
    ]
}

for node_value in tree_traversal(tree):
    print(f"遍历节点: {node_value}")
print()

# 8. 异步模拟生成器
print("=== 8. 异步模拟生成器 ===")

def async_data_generator(delay=0.1):
    """模拟异步数据生成器"""
    data_sources = ['数据源A', '数据源B', '数据源C', '数据源D']
    
    for i, source in enumerate(data_sources):
        print(f"正在从{source}获取数据...")
        time.sleep(delay)  # 模拟网络延迟
        
        # 模拟随机数据
        data = {
            'source': source,
            'timestamp': time.time(),
            'value': random.randint(1, 100)
        }
        yield data

print("异步数据获取模拟:")
for data in async_data_generator(0.05):  # 减少延迟以便演示
    print(f"获取数据: {data}")
print()

# 9. 生成器函数的错误处理
print("=== 9. 生成器函数的错误处理 ===")

def safe_division_generator(numbers, divisor):
    """安全除法生成器"""
    for num in numbers:
        try:
            if divisor == 0:
                raise ValueError("除数不能为零")
            result = num / divisor
            yield result
        except ValueError as e:
            print(f"错误: {e}")
            yield None
        except Exception as e:
            print(f"未知错误: {e}")
            yield None

print("安全除法生成器:")
numbers = [10, 20, 30, 40]
for result in safe_division_generator(numbers, 2):
    if result is not None:
        print(f"除法结果: {result}")
    else:
        print("计算失败")
print()

print("除零错误处理:")
for result in safe_division_generator(numbers, 0):
    if result is not None:
        print(f"除法结果: {result}")
    else:
        print("计算失败")
print()

# 10. 生成器函数的性能优势
print("=== 10. 生成器函数的性能优势 ===")

def list_approach(n):
    """列表方式处理大量数据"""
    return [x ** 2 for x in range(n)]

def generator_approach(n):
    """生成器方式处理大量数据"""
    for x in range(n):
        yield x ** 2

print("性能比较（处理大量数据）:")
n = 100000

# 测试列表方式
start_time = time.time()
list_result = list_approach(n)
list_time = time.time() - start_time
print(f"列表方式耗时: {list_time:.4f}秒")
print(f"列表占用内存（元素数量）: {len(list_result)}")

# 测试生成器方式
start_time = time.time()
gen_result = generator_approach(n)
gen_time = time.time() - start_time
print(f"生成器创建耗时: {gen_time:.6f}秒")
print(f"生成器对象: {gen_result}")

# 只获取前10个值进行比较
print("\n获取前10个值:")
for i, value in enumerate(gen_result):
    if i >= 10:
        break
    print(f"值: {value}")
print()

print("=== 生成器函数学习完成 ===")
print("关键要点:")
print("1. 包含yield的函数就是生成器函数")
print("2. 生成器函数支持参数传递")
print("3. 可以创建无限序列生成器")
print("4. 生成器函数可以组合使用")
print("5. 生成器函数具有内存和性能优势")
print("6. yield from可以委托给其他生成器")
print("7. 生成器函数支持错误处理")

if __name__ == "__main__":
    print("\n=== 运行完成 ===")
    print("本模块演示了生成器函数的各种定义和使用方式")