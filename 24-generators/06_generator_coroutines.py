#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成器的协程应用

本模块介绍：
1. 协程的基本概念
2. 使用生成器实现协程
3. 协程的调度和通信
4. 异步任务处理
5. 协程在并发编程中的应用
"""

import time
import random
from collections import deque
from typing import Generator, Any, Callable

# 1. 协程的基本概念
print("=== 1. 协程的基本概念 ===")
print("协程是一种用户态的轻量级线程，可以在执行过程中暂停和恢复")
print("生成器是Python中实现协程的基础机制")
print()

def simple_coroutine():
    """简单的协程示例"""
    print("协程启动")
    
    while True:
        # 暂停执行，等待外部发送数据
        data = yield
        if data is None:
            break
        print(f"协程处理数据: {data}")
        
        # 模拟处理时间
        time.sleep(0.1)
        print(f"数据 {data} 处理完成")
    
    print("协程结束")

print("简单协程演示:")
coro = simple_coroutine()
next(coro)  # 启动协程

# 向协程发送数据
for i in range(5):
    coro.send(f"task_{i}")
    print("---")

# 结束协程
try:
    coro.send(None)
except StopIteration:
    pass  # 协程正常结束
print()

# 2. 协程装饰器
print("=== 2. 协程装饰器 ===")

def coroutine(func):
    """协程装饰器，自动启动协程"""
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)  # 自动启动
        return gen
    return wrapper

@coroutine
def auto_started_coroutine():
    """自动启动的协程"""
    print("自动启动协程已就绪")
    
    while True:
        data = yield
        if data == 'quit':
            break
        print(f"自动协程处理: {data}")
    
    print("自动协程结束")

print("使用装饰器的协程:")
auto_coro = auto_started_coroutine()

# 直接发送数据，无需手动启动
for item in ['apple', 'banana', 'cherry']:
    auto_coro.send(item)

try:
    auto_coro.send('quit')
except StopIteration:
    pass  # 协程正常结束
print()

# 3. 协程管道
print("=== 3. 协程管道 ===")

@coroutine
def data_processor():
    """数据处理协程"""
    print("处理器启动")
    
    try:
        while True:
            data = yield
            processed = data.upper()
            print(f"处理结果: {processed}")
    except GeneratorExit:
        print("处理器关闭")

@coroutine
def data_filter(pattern, target):
    """数据过滤协程"""
    print(f"过滤器启动，模式: {pattern}")
    
    try:
        while True:
            data = yield
            if pattern in data:
                print(f"数据通过过滤: {data}")
                target.send(data)
            else:
                print(f"数据被过滤: {data}")
    except GeneratorExit:
        try:
            target.close()
        except:
            pass
        print("过滤器关闭")

print("协程管道演示:")
# 构建处理管道
processor = data_processor()
filter_coro = data_filter("5", processor)  # 只处理包含"5"的数据

# 手动发送数据到管道
for i in range(10):
    data = f"data_{i}"
    print(f"生成数据: {data}")
    filter_coro.send(data)
    time.sleep(0.05)

# 关闭管道
try:
    filter_coro.close()
except:
    pass
print()

# 4. 协程调度器
print("=== 4. 协程调度器 ===")

class SimpleScheduler:
    """简单的协程调度器"""
    
    def __init__(self):
        self.ready = deque()  # 就绪队列
        self.sequence = 0
    
    def new_task(self, coro):
        """添加新任务"""
        self.sequence += 1
        task_id = self.sequence
        self.ready.append((task_id, coro))
        print(f"添加任务 {task_id}")
        return task_id
    
    def run(self):
        """运行调度器"""
        print("调度器启动")
        
        rounds = 0
        while self.ready and rounds < 20:  # 限制轮数避免无限循环
            rounds += 1
            current_tasks = list(self.ready)
            self.ready.clear()
            
            for task_id, task in current_tasks:
                try:
                    next(task)
                    # 任务还没结束，重新加入队列
                    self.ready.append((task_id, task))
                except StopIteration:
                    print(f"任务 {task_id} 完成")
            
            # 避免忙等待
            time.sleep(0.1)
        
        print("调度器结束")

def worker_task(name, work_time):
    """工作任务协程"""
    print(f"任务 {name} 开始工作")
    
    for i in range(3):
        print(f"任务 {name} 执行步骤 {i+1}")
        
        # 模拟工作时间
        time.sleep(work_time)
        yield
    
    print(f"任务 {name} 完成所有工作")

print("协程调度演示:")
scheduler = SimpleScheduler()

# 创建多个任务
task1 = worker_task("A", 0.1)
task2 = worker_task("B", 0.15)
task3 = worker_task("C", 0.05)

# 添加到调度器
scheduler.new_task(task1)
scheduler.new_task(task2)
scheduler.new_task(task3)

# 运行调度器
start_time = time.time()
scheduler.run()
end_time = time.time()
print(f"总执行时间: {end_time - start_time:.2f} 秒")
print()

# 5. 生产者-消费者模式
print("=== 5. 生产者-消费者模式 ===")

@coroutine
def simple_producer(name, count):
    """简单生产者协程"""
    print(f"生产者 {name} 启动")
    
    items = []
    for i in range(count):
        item = f"{name}_item_{i}"
        items.append(item)
        print(f"生产者 {name} 生产: {item}")
        
        # 模拟生产时间
        time.sleep(0.1)
        yield item
    
    print(f"生产者 {name} 完成，共生产 {len(items)} 个项目")
    return items

@coroutine
def simple_consumer(name):
    """简单消费者协程"""
    print(f"消费者 {name} 启动")
    
    consumed_items = []
    try:
        while True:
            item = yield
            if item is None:
                break
            consumed_items.append(item)
            print(f"消费者 {name} 消费: {item}")
            
            # 模拟消费时间
            time.sleep(0.05)
    except GeneratorExit:
        pass
    
    print(f"消费者 {name} 完成，共消费 {len(consumed_items)} 个项目")
    return consumed_items

print("生产者-消费者演示:")
# 创建消费者
consumer1 = simple_consumer("C1")
consumer2 = simple_consumer("C2")

# 创建生产者并分发给消费者
producer1 = simple_producer("P1", 5)
producer2 = simple_producer("P2", 3)

# 模拟生产和消费过程
producers = [producer1, producer2]
consumers = [consumer1, consumer2]
consumer_index = 0

for producer in producers:
    try:
        while True:
            item = next(producer)
            if item:
                # 轮流分发给消费者
                consumers[consumer_index].send(item)
                consumer_index = (consumer_index + 1) % len(consumers)
    except StopIteration:
        pass

# 结束消费者
for consumer in consumers:
    try:
        consumer.send(None)
    except StopIteration:
        pass

print()

# 6. 异步任务处理
print("=== 6. 异步任务处理 ===")

def async_download(url, size):
    """模拟异步下载"""
    print(f"开始下载: {url}")
    
    downloaded = 0
    chunk_size = max(1, size // 5)  # 减少步骤数
    
    while downloaded < size:
        # 模拟网络延迟
        time.sleep(0.05)
        
        # 下载一块数据
        chunk = min(chunk_size, size - downloaded)
        downloaded += chunk
        
        progress = (downloaded / size) * 100
        print(f"{url} 下载进度: {progress:.1f}%")
        yield progress
    
    print(f"下载完成: {url}")
    return f"文件 {url} 下载成功，大小: {size}MB"

def async_process_data(data_id, steps):
    """模拟异步数据处理"""
    print(f"开始处理数据: {data_id}")
    
    for step in range(steps):
        time.sleep(0.05)
        progress = ((step + 1) / steps) * 100
        print(f"{data_id} 处理进度: {progress:.1f}%")
        yield progress
    
    print(f"数据处理完成: {data_id}")
    return f"数据 {data_id} 处理结果"

print("异步任务管理演示:")

# 创建多个异步任务
tasks = [
    async_download("file1.zip", 20),
    async_download("file2.zip", 15),
    async_process_data("dataset_A", 4),
    async_process_data("dataset_B", 3)
]

# 简单的轮询执行
active_tasks = list(tasks)
while active_tasks:
    for task in active_tasks[:]:
        try:
            next(task)
        except StopIteration as e:
            result = getattr(e, 'value', None)
            if result:
                print(f"任务完成: {result}")
            active_tasks.remove(task)
    
    time.sleep(0.1)  # 调度间隔

print("所有异步任务完成")
print()

# 7. 协程通信和同步
print("=== 7. 协程通信和同步 ===")

@coroutine
def synchronized_worker(name, work_steps):
    """同步工作协程"""
    print(f"工作者 {name} 开始准备")
    
    # 等待启动信号
    signal = yield
    if signal == "start":
        print(f"工作者 {name} 收到启动信号，开始工作")
        
        # 执行工作
        for step in range(work_steps):
            print(f"工作者 {name} 执行步骤 {step + 1}")
            time.sleep(0.1)
            yield f"步骤 {step + 1} 完成"
        
        print(f"工作者 {name} 完成工作")
    else:
        print(f"工作者 {name} 收到无效信号: {signal}")

print("协程同步演示:")

# 创建多个工作协程
workers = [
    synchronized_worker("Alpha", 3),
    synchronized_worker("Beta", 4),
    synchronized_worker("Gamma", 2)
]

print("所有工作者已就绪，等待启动信号...")
time.sleep(0.2)

# 发送启动信号
print("发送启动信号")
for worker in workers:
    worker.send("start")

# 继续执行工作者
active_workers = list(workers)
while active_workers:
    for worker in active_workers[:]:
        try:
            result = next(worker)
            if result:
                print(f"收到结果: {result}")
        except StopIteration:
            active_workers.remove(worker)
    time.sleep(0.1)

print()

print("=== 生成器协程应用学习完成 ===")
print("关键要点:")
print("1. 协程是用户态的轻量级线程")
print("2. 生成器是Python实现协程的基础")
print("3. 协程可以实现异步编程和并发处理")
print("4. 协程调度器管理多个协程的执行")
print("5. 协程间可以通过队列和事件进行通信")
print("6. 协程适合I/O密集型任务")
print("7. 现代Python使用async/await语法")

if __name__ == "__main__":
    print("\n=== 运行完成 ===")
    print("本模块演示了使用生成器实现协程的各种应用场景")
    print("注意：现代Python推荐使用async/await语法进行异步编程")