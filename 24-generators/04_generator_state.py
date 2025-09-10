#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成器的状态保持

本模块介绍：
1. 生成器的状态保持机制
2. 局部变量的保持
3. 执行位置的记忆
4. 多个生成器实例的独立性
5. 生成器状态的生命周期
"""

import time
import random
from typing import Generator

# 1. 生成器状态保持的基本概念
print("=== 1. 生成器状态保持的基本概念 ===")
print("生成器能够在yield处暂停执行，并保持当前的执行状态")
print("包括局部变量、执行位置等信息")
print()

def simple_counter():
    """简单的计数器生成器"""
    count = 0
    print(f"生成器初始化，count = {count}")
    
    while True:
        print(f"yield前，count = {count}")
        yield count
        count += 1
        print(f"yield后，count = {count}")

print("创建生成器实例:")
counter = simple_counter()
print(f"生成器对象: {counter}")
print()

print("调用生成器:")
for i in range(5):
    value = next(counter)
    print(f"第{i+1}次调用，返回值: {value}")
    print("---")
print()

# 2. 局部变量的状态保持
print("=== 2. 局部变量的状态保持 ===")

def fibonacci_with_state():
    """斐波那契数列生成器，展示状态保持"""
    print("初始化斐波那契生成器")
    a, b = 0, 1
    count = 0
    
    while True:
        print(f"当前状态: a={a}, b={b}, count={count}")
        yield a
        print(f"yield后继续执行，准备计算下一个值")
        a, b = b, a + b
        count += 1
        print(f"更新后状态: a={a}, b={b}, count={count}")
        print("---")

print("斐波那契数列状态演示:")
fib_gen = fibonacci_with_state()
for i in range(6):
    fib_value = next(fib_gen)
    print(f"斐波那契第{i+1}项: {fib_value}")
    print()
print()

# 3. 复杂状态管理
print("=== 3. 复杂状态管理 ===")

def stateful_processor():
    """有状态的数据处理器"""
    # 初始化状态变量
    total = 0
    count = 0
    history = []
    max_value = float('-inf')
    min_value = float('inf')
    
    print("数据处理器初始化完成")
    
    try:
        while True:
            # 接收数据
            data = yield {
                'total': total,
                'count': count,
                'average': total / count if count > 0 else 0,
                'max': max_value if max_value != float('-inf') else None,
                'min': min_value if min_value != float('inf') else None,
                'history': history[-5:]  # 只保留最近5个值
            }
            
            if data is not None:
                # 更新状态
                total += data
                count += 1
                history.append(data)
                max_value = max(max_value, data)
                min_value = min(min_value, data)
                
                print(f"处理数据: {data}, 当前统计: 总和={total}, 数量={count}")
    
    except GeneratorExit:
        print("数据处理器关闭")

print("创建有状态的数据处理器:")
processor = stateful_processor()
next(processor)  # 启动生成器

print("\n发送数据并查看状态:")
test_data = [10, 20, 15, 30, 25]
for data in test_data:
    result = processor.send(data)
    print(f"发送: {data}")
    print(f"当前状态: {result}")
    print("---")
print()

# 4. 多个生成器实例的独立性
print("=== 4. 多个生成器实例的独立性 ===")

def independent_counter(start=0, step=1):
    """独立的计数器生成器"""
    current = start
    print(f"计数器初始化: start={start}, step={step}")
    
    while True:
        yield current
        current += step

print("创建多个独立的计数器:")
counter1 = independent_counter(0, 1)    # 从0开始，步长1
counter2 = independent_counter(100, 5)  # 从100开始，步长5
counter3 = independent_counter(10, -2)  # 从10开始，步长-2

print("\n并行使用多个计数器:")
for i in range(5):
    val1 = next(counter1)
    val2 = next(counter2)
    val3 = next(counter3)
    print(f"轮次{i+1}: counter1={val1}, counter2={val2}, counter3={val3}")
print()

# 5. 生成器状态的持久化演示
print("=== 5. 生成器状态的持久化演示 ===")

def persistent_random_walk():
    """随机游走生成器，保持位置状态"""
    position = 0
    steps = 0
    history = []
    
    print(f"随机游走开始，初始位置: {position}")
    
    while True:
        # 记录当前状态
        state_info = {
            'position': position,
            'steps': steps,
            'history': history.copy()
        }
        
        yield state_info
        
        # 随机移动
        move = random.choice([-1, 1])
        position += move
        steps += 1
        history.append(move)
        
        print(f"步骤{steps}: 移动{move}, 新位置: {position}")

print("随机游走状态演示:")
random.seed(42)  # 设置随机种子以便复现
walk = persistent_random_walk()

for i in range(8):
    state = next(walk)
    print(f"第{i+1}次查询状态:")
    print(f"  位置: {state['position']}")
    print(f"  总步数: {state['steps']}")
    print(f"  最近3步: {state['history'][-3:]}")
    print("---")
print()

# 6. 生成器状态的生命周期管理
print("=== 6. 生成器状态的生命周期管理 ===")

def lifecycle_demo():
    """演示生成器的生命周期"""
    print("生成器创建 - 初始化阶段")
    state = "initialized"
    count = 0
    
    try:
        print("生成器启动 - 运行阶段")
        state = "running"
        
        while True:
            count += 1
            print(f"生成器活跃中 - 第{count}次yield，状态: {state}")
            yield f"value_{count}"
            print(f"yield后恢复执行，状态仍为: {state}")
            
    except GeneratorExit:
        print("生成器关闭 - 清理阶段")
        state = "closed"
        print(f"最终状态: {state}, 总共yield了{count}次")
    
    finally:
        print("生成器生命周期结束")

print("生命周期演示:")
lifecycle_gen = lifecycle_demo()

print("\n获取前3个值:")
for i in range(3):
    value = next(lifecycle_gen)
    print(f"获得值: {value}")

print("\n手动关闭生成器:")
lifecycle_gen.close()
print()

# 7. 状态恢复和异常处理
print("=== 7. 状态恢复和异常处理 ===")

def robust_generator():
    """具有异常处理的健壮生成器"""
    state = {
        'count': 0,
        'errors': 0,
        'last_value': None
    }
    
    print("健壮生成器启动")
    
    while True:
        try:
            # 接收输入
            input_value = yield state.copy()
            
            if input_value is not None:
                # 模拟可能出错的处理
                if input_value < 0:
                    raise ValueError(f"负数输入: {input_value}")
                
                # 正常处理
                state['count'] += 1
                state['last_value'] = input_value * 2
                print(f"处理成功: {input_value} -> {state['last_value']}")
                
        except ValueError as e:
            state['errors'] += 1
            print(f"处理错误: {e}, 错误计数: {state['errors']}")
            # 状态保持，继续运行
        
        except Exception as e:
            state['errors'] += 1
            print(f"未知错误: {e}, 错误计数: {state['errors']}")

print("健壮生成器测试:")
robust_gen = robust_generator()
state = next(robust_gen)  # 启动
print(f"初始状态: {state}")

test_inputs = [5, -3, 10, -1, 8]
for inp in test_inputs:
    state = robust_gen.send(inp)
    print(f"输入: {inp}, 状态: {state}")
    print("---")
print()

# 8. 生成器状态的调试和监控
print("=== 8. 生成器状态的调试和监控 ===")

def monitored_generator():
    """可监控的生成器"""
    # 状态变量
    iteration = 0
    start_time = time.time()
    
    def get_debug_info():
        return {
            'iteration': iteration,
            'runtime': time.time() - start_time,
            'memory_usage': f"{iteration * 8} bytes (模拟)",
            'status': 'active'
        }
    
    print("监控生成器启动")
    
    try:
        while iteration < 10:  # 限制迭代次数
            debug_info = get_debug_info()
            yield {
                'value': f"item_{iteration}",
                'debug': debug_info
            }
            
            iteration += 1
            time.sleep(0.1)  # 模拟处理时间
            
    finally:
        final_debug = get_debug_info()
        final_debug['status'] = 'completed'
        print(f"生成器完成，最终调试信息: {final_debug}")

print("监控生成器演示:")
monitor_gen = monitored_generator()

for result in monitor_gen:
    print(f"值: {result['value']}")
    print(f"调试信息: {result['debug']}")
    print("---")
    
    # 只显示前5个结果
    if result['debug']['iteration'] >= 4:
        break
print()

# 9. 状态共享和通信
print("=== 9. 状态共享和通信 ===")

class SharedState:
    """共享状态类"""
    def __init__(self):
        self.data = {}
        self.subscribers = []
    
    def update(self, key, value):
        self.data[key] = value
        self.notify_subscribers(key, value)
    
    def notify_subscribers(self, key, value):
        for subscriber in self.subscribers:
            try:
                subscriber.send((key, value))
            except StopIteration:
                pass

def state_subscriber(name, shared_state):
    """状态订阅者生成器"""
    print(f"订阅者 {name} 启动")
    local_state = {}
    
    try:
        while True:
            # 接收状态更新
            key, value = yield local_state.copy()
            local_state[key] = value
            print(f"订阅者 {name} 收到更新: {key} = {value}")
            
    except GeneratorExit:
        print(f"订阅者 {name} 关闭")

print("状态共享演示:")
shared = SharedState()

# 创建订阅者
sub1 = state_subscriber("A", shared)
sub2 = state_subscriber("B", shared)

# 启动订阅者
next(sub1)
next(sub2)

# 注册订阅者
shared.subscribers = [sub1, sub2]

# 更新共享状态
print("\n更新共享状态:")
shared.update("temperature", 25)
shared.update("humidity", 60)
shared.update("pressure", 1013)

# 查看订阅者状态
print(f"\n订阅者A状态: {sub1.send((None, None))}")
print(f"订阅者B状态: {sub2.send((None, None))}")
print()

print("=== 生成器状态保持学习完成 ===")
print("关键要点:")
print("1. 生成器在yield处暂停并保持所有局部状态")
print("2. 每个生成器实例都有独立的状态空间")
print("3. 状态包括变量值、执行位置、调用栈等")
print("4. 生成器状态在整个生命周期内持续存在")
print("5. 可以通过send()方法与生成器进行双向通信")
print("6. 异常处理不会破坏生成器的状态保持")
print("7. 生成器关闭时会执行清理代码")

if __name__ == "__main__":
    print("\n=== 运行完成 ===")
    print("本模块演示了生成器状态保持的各种机制和应用")