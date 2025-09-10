#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成器基础概念和yield关键字

本模块介绍：
1. 什么是生成器
2. yield关键字的基本用法
3. 生成器与普通函数的区别
4. 生成器的基本特性
"""

# 1. 什么是生成器
print("=== 1. 什么是生成器 ===")
print("生成器是一种特殊的迭代器，它可以暂停执行并保持状态")
print("使用yield关键字可以创建生成器函数")
print()

# 2. 最简单的生成器函数
def simple_generator():
    """最简单的生成器函数"""
    print("生成器开始执行")
    yield 1
    print("生成器继续执行")
    yield 2
    print("生成器即将结束")
    yield 3
    print("生成器执行完毕")

print("=== 2. 简单生成器示例 ===")
# 创建生成器对象
gen = simple_generator()
print(f"生成器对象: {gen}")
print(f"生成器类型: {type(gen)}")
print()

# 使用next()函数获取值
print("使用next()函数逐个获取值:")
try:
    print(f"第一次调用next(): {next(gen)}")
    print(f"第二次调用next(): {next(gen)}")
    print(f"第三次调用next(): {next(gen)}")
    print(f"第四次调用next(): {next(gen)}")  # 这里会抛出StopIteration异常
except StopIteration:
    print("生成器已耗尽，抛出StopIteration异常")
print()

# 3. 生成器与普通函数的区别
def normal_function():
    """普通函数"""
    print("普通函数执行")
    return [1, 2, 3]

def generator_function():
    """生成器函数"""
    print("生成器函数执行")
    yield 1
    yield 2
    yield 3

print("=== 3. 生成器与普通函数的区别 ===")
print("普通函数调用:")
result = normal_function()
print(f"返回值: {result}")
print(f"类型: {type(result)}")
print()

print("生成器函数调用:")
gen_result = generator_function()
print(f"返回值: {gen_result}")
print(f"类型: {type(gen_result)}")
print()

# 4. 使用for循环遍历生成器
print("=== 4. 使用for循环遍历生成器 ===")
gen2 = generator_function()
print("使用for循环遍历:")
for value in gen2:
    print(f"获取到值: {value}")
print()

# 5. 生成器的惰性求值特性
def fibonacci_generator(n):
    """斐波那契数列生成器"""
    print(f"开始生成斐波那契数列，前{n}项")
    a, b = 0, 1
    count = 0
    while count < n:
        print(f"生成第{count + 1}项: {a}")
        yield a
        a, b = b, a + b
        count += 1
    print("斐波那契生成器执行完毕")

print("=== 5. 斐波那契数列生成器 ===")
fib_gen = fibonacci_generator(5)
print("创建生成器对象（此时还未开始执行）")
print()

print("开始遍历生成器:")
for fib_num in fib_gen:
    print(f"斐波那契数: {fib_num}")
print()

# 6. 生成器的状态保持
def counter_generator():
    """计数器生成器，演示状态保持"""
    count = 0
    while True:
        count += 1
        print(f"当前计数: {count}")
        yield count

print("=== 6. 生成器的状态保持 ===")
counter = counter_generator()
print("获取前5个计数值:")
for i in range(5):
    value = next(counter)
    print(f"计数值: {value}")
print()

print("暂停一下，然后继续获取:")
for i in range(3):
    value = next(counter)
    print(f"继续计数: {value}")
print()

# 7. yield的返回值
def echo_generator():
    """回声生成器，演示yield的返回值"""
    while True:
        received = yield
        if received is not None:
            print(f"收到消息: {received}")
            yield f"回声: {received}"

print("=== 7. yield的返回值 ===")
echo = echo_generator()
next(echo)  # 启动生成器

# 发送消息给生成器
response = echo.send("Hello")
print(f"生成器响应: {response}")

response = echo.send("World")
print(f"生成器响应: {response}")
print()

# 8. 生成器的内存优势演示
def memory_efficient_range(n):
    """内存高效的范围生成器"""
    i = 0
    while i < n:
        yield i
        i += 1

print("=== 8. 生成器的内存优势 ===")
print("比较列表和生成器的内存使用:")

# 使用列表（占用更多内存）
large_list = list(range(1000000))
print(f"列表大小: {len(large_list)} 个元素")

# 使用生成器（占用很少内存）
large_gen = memory_efficient_range(1000000)
print(f"生成器对象: {large_gen}")
print("生成器只在需要时才生成值，节省内存")
print()

# 9. 生成器的基本方法
print("=== 9. 生成器的基本方法 ===")
def demo_generator():
    """演示生成器方法的生成器"""
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print("生成器被关闭")
    finally:
        print("生成器清理工作")

gen_demo = demo_generator()
print(f"next(): {next(gen_demo)}")
print(f"next(): {next(gen_demo)}")

# 关闭生成器
gen_demo.close()
print("生成器已关闭")

try:
    next(gen_demo)
except StopIteration:
    print("关闭后的生成器无法继续使用")
print()

print("=== 生成器基础概念学习完成 ===")
print("关键要点:")
print("1. yield关键字创建生成器函数")
print("2. 生成器具有惰性求值特性")
print("3. 生成器可以保持执行状态")
print("4. 生成器比列表更节省内存")
print("5. 生成器是一次性的迭代器")

if __name__ == "__main__":
    print("\n=== 运行完成 ===")
    print("本模块演示了生成器的基础概念和yield关键字的使用")