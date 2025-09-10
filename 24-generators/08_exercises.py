#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成器综合练习

本模块包含生成器相关的综合练习题和实战项目，
帮助巩固和深化对生成器概念的理解和应用。

学习目标:
1. 综合运用生成器的各种特性
2. 解决实际编程问题
3. 提高代码的性能和可读性
4. 掌握生成器的高级应用技巧
5. 培养使用生成器思考问题的习惯
"""

import time
import random
import itertools
from typing import Iterator, Generator, List, Tuple, Any
from collections import defaultdict


# 练习1: 基础生成器练习
print("=== 练习1: 基础生成器练习 ===")

def exercise_1_fibonacci(n: int) -> Generator[int, None, None]:
    """练习1: 生成前n个斐波那契数"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def exercise_1_prime_numbers(limit: int) -> Generator[int, None, None]:
    """练习1: 生成指定范围内的质数"""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

def exercise_1_factorial_sequence(n: int) -> Generator[int, None, None]:
    """练习1: 生成前n个数的阶乘序列"""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        yield factorial

print("练习1 - 基础生成器:")

# 斐波那契数列
print("\n1.1 前10个斐波那契数:")
fib_gen = exercise_1_fibonacci(10)
fib_list = list(fib_gen)
print(f"结果: {fib_list}")

# 质数生成
print("\n1.2 50以内的质数:")
prime_gen = exercise_1_prime_numbers(50)
prime_list = list(prime_gen)
print(f"结果: {prime_list}")

# 阶乘序列
print("\n1.3 前6个数的阶乘:")
fact_gen = exercise_1_factorial_sequence(6)
fact_list = list(fact_gen)
print(f"结果: {fact_list}")


# 练习2: 生成器表达式练习
print("\n=== 练习2: 生成器表达式练习 ===")

def exercise_2_data_processing():
    """练习2: 使用生成器表达式处理数据"""
    # 原始数据
    sales_data = [
        {"product": "笔记本", "price": 5000, "quantity": 10, "category": "电子产品"},
        {"product": "鼠标", "price": 50, "quantity": 100, "category": "电子产品"},
        {"product": "书籍", "price": 30, "quantity": 200, "category": "图书"},
        {"product": "键盘", "price": 200, "quantity": 50, "category": "电子产品"},
        {"product": "杂志", "price": 15, "quantity": 300, "category": "图书"},
    ]
    
    # 2.1 计算每个产品的总销售额
    total_sales = (item["price"] * item["quantity"] for item in sales_data)
    print("2.1 各产品总销售额:")
    for i, (item, total) in enumerate(zip(sales_data, total_sales)):
        print(f"  {item['product']}: {total}元")
    
    # 2.2 筛选电子产品并计算平均价格
    electronics = (item for item in sales_data if item["category"] == "电子产品")
    electronics_list = list(electronics)
    avg_price = sum(item["price"] for item in electronics_list) / len(electronics_list)
    print(f"\n2.2 电子产品平均价格: {avg_price:.2f}元")
    
    # 2.3 找出高价值产品(总销售额>10000)
    high_value = (
        (item["product"], item["price"] * item["quantity"])
        for item in sales_data
        if item["price"] * item["quantity"] > 10000
    )
    print("\n2.3 高价值产品(总销售额>10000):")
    for product, total in high_value:
        print(f"  {product}: {total}元")

exercise_2_data_processing()


# 练习3: 生成器方法练习
print("\n=== 练习3: 生成器方法练习 ===")

def exercise_3_interactive_calculator():
    """练习3: 交互式计算器生成器"""
    result = 0
    print(f"计算器启动，初始值: {result}")
    
    try:
        while True:
            # 接收操作指令
            operation = yield result
            
            if operation is None:
                continue
            
            if isinstance(operation, tuple) and len(operation) == 2:
                op, value = operation
                
                if op == "add":
                    result += value
                    print(f"执行加法: {result - value} + {value} = {result}")
                elif op == "sub":
                    result -= value
                    print(f"执行减法: {result + value} - {value} = {result}")
                elif op == "mul":
                    old_result = result
                    result *= value
                    print(f"执行乘法: {old_result} * {value} = {result}")
                elif op == "div":
                    if value != 0:
                        old_result = result
                        result /= value
                        print(f"执行除法: {old_result} / {value} = {result}")
                    else:
                        print("错误: 除数不能为0")
                elif op == "reset":
                    result = 0
                    print("计算器已重置")
                else:
                    print(f"未知操作: {op}")
            elif operation == "quit":
                print("计算器退出")
                break
            else:
                print(f"无效操作格式: {operation}")
    
    except GeneratorExit:
        print("计算器被强制关闭")

print("练习3 - 交互式计算器:")
calc = exercise_3_interactive_calculator()
next(calc)  # 启动生成器

# 执行一系列计算
operations = [
    ("add", 10),
    ("mul", 3),
    ("sub", 5),
    ("div", 5),
    ("reset", 0),
    ("add", 100),
    "quit"
]

for op in operations:
    try:
        result = calc.send(op)
        if op != "quit":
            print(f"当前结果: {result}")
    except StopIteration:
        break


# 练习4: 数据流处理练习
print("\n=== 练习4: 数据流处理练习 ===")

def exercise_4_log_analyzer():
    """练习4: 日志分析器"""
    
    def generate_log_entries(count: int) -> Generator[str, None, None]:
        """生成模拟日志条目"""
        levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
        actions = ["用户登录", "数据查询", "文件上传", "系统错误", "网络超时"]
        
        for i in range(count):
            timestamp = f"2024-01-{(i % 30) + 1:02d} {(i % 24):02d}:{(i % 60):02d}:{(i % 60):02d}"
            level = random.choice(levels)
            action = random.choice(actions)
            user_id = f"user_{(i % 100) + 1:03d}"
            
            yield f"[{timestamp}] {level}: {action} - 用户ID: {user_id}"
    
    def parse_log_entry(log_line: str) -> dict:
        """解析日志条目"""
        parts = log_line.split("] ")
        timestamp = parts[0][1:]  # 移除开头的 '['
        
        rest = parts[1]
        level_end = rest.find(":")
        level = rest[:level_end]
        
        message = rest[level_end + 2:]  # 跳过 ': '
        
        return {
            "timestamp": timestamp,
            "level": level,
            "message": message
        }
    
    def filter_by_level(logs: Iterator[dict], target_level: str) -> Generator[dict, None, None]:
        """按日志级别过滤"""
        for log in logs:
            if log["level"] == target_level:
                yield log
    
    def count_by_level(logs: Iterator[dict]) -> dict:
        """统计各级别日志数量"""
        counts = defaultdict(int)
        for log in logs:
            counts[log["level"]] += 1
        return dict(counts)
    
    print("练习4 - 日志分析器:")
    
    # 生成日志数据
    log_entries = generate_log_entries(1000)
    
    # 解析日志
    parsed_logs = (parse_log_entry(entry) for entry in log_entries)
    
    # 转换为列表以便多次使用
    parsed_logs_list = list(parsed_logs)
    
    # 统计各级别日志数量
    level_counts = count_by_level(iter(parsed_logs_list))
    print("\n4.1 日志级别统计:")
    for level, count in level_counts.items():
        print(f"  {level}: {count} 条")
    
    # 筛选错误日志
    error_logs = list(filter_by_level(iter(parsed_logs_list), "ERROR"))
    print(f"\n4.2 错误日志 (共{len(error_logs)}条):")
    for i, log in enumerate(error_logs[:3]):  # 只显示前3条
        print(f"  {i+1}. [{log['timestamp']}] {log['message']}")
    
    # 筛选警告日志
    warning_logs = list(filter_by_level(iter(parsed_logs_list), "WARNING"))
    print(f"\n4.3 警告日志 (共{len(warning_logs)}条):")
    for i, log in enumerate(warning_logs[:3]):  # 只显示前3条
        print(f"  {i+1}. [{log['timestamp']}] {log['message']}")

exercise_4_log_analyzer()


# 练习5: 协程应用练习
print("\n=== 练习5: 协程应用练习 ===")

def exercise_5_task_scheduler():
    """练习5: 任务调度器"""
    
    def coroutine(func):
        """协程装饰器"""
        def wrapper(*args, **kwargs):
            gen = func(*args, **kwargs)
            next(gen)
            return gen
        return wrapper
    
    @coroutine
    def task_worker(worker_id: int, task_queue: list):
        """任务工作者协程"""
        completed_tasks = 0
        
        try:
            while True:
                # 接收任务
                task = yield
                
                if task is None:
                    continue
                
                if task == "STOP":
                    print(f"工作者 {worker_id} 收到停止信号")
                    break
                
                # 处理任务
                task_id, task_data = task
                print(f"工作者 {worker_id} 开始处理任务 {task_id}: {task_data}")
                
                # 模拟任务处理时间
                processing_time = random.uniform(0.1, 0.3)
                time.sleep(processing_time)
                
                completed_tasks += 1
                print(f"工作者 {worker_id} 完成任务 {task_id} (耗时 {processing_time:.2f}s)")
                
                # 返回处理结果
                result = f"任务 {task_id} 处理完成"
                task_queue.append(("RESULT", worker_id, task_id, result))
        
        except GeneratorExit:
            print(f"工作者 {worker_id} 被强制停止")
        
        print(f"工作者 {worker_id} 总共完成 {completed_tasks} 个任务")
    
    class SimpleTaskScheduler:
        """简单任务调度器"""
        
        def __init__(self, num_workers: int = 3):
            self.workers = []
            self.task_queue = []
            self.results = []
            
            # 创建工作者
            for i in range(num_workers):
                worker = task_worker(i + 1, self.results)
                self.workers.append(worker)
        
        def add_task(self, task_id: str, task_data: str):
            """添加任务"""
            self.task_queue.append((task_id, task_data))
        
        def run(self):
            """运行调度器"""
            print(f"启动调度器，{len(self.workers)} 个工作者就绪")
            
            # 分发任务
            worker_index = 0
            for task in self.task_queue:
                worker = self.workers[worker_index]
                worker.send(task)
                worker_index = (worker_index + 1) % len(self.workers)
            
            # 等待任务完成
            time.sleep(1)
            
            # 停止所有工作者
            for worker in self.workers:
                try:
                    worker.send("STOP")
                except StopIteration:
                    pass
            
            print(f"\n调度完成，处理了 {len(self.task_queue)} 个任务")
            print(f"收到 {len(self.results)} 个结果")
    
    print("练习5 - 任务调度器:")
    
    # 创建调度器
    scheduler = SimpleTaskScheduler(num_workers=3)
    
    # 添加任务
    tasks = [
        ("T001", "数据备份"),
        ("T002", "报告生成"),
        ("T003", "邮件发送"),
        ("T004", "文件清理"),
        ("T005", "系统检查"),
        ("T006", "日志分析"),
    ]
    
    for task_id, task_data in tasks:
        scheduler.add_task(task_id, task_data)
    
    # 运行调度器
    scheduler.run()

exercise_5_task_scheduler()


# 练习6: 性能优化练习
print("\n=== 练习6: 性能优化练习 ===")

def exercise_6_performance_optimization():
    """练习6: 性能优化对比"""
    
    def process_data_with_list(data_size: int) -> List[int]:
        """使用列表处理数据"""
        # 生成数据
        data = list(range(data_size))
        
        # 处理数据：过滤偶数，平方，再过滤大于100的
        filtered1 = [x for x in data if x % 2 == 0]
        squared = [x * x for x in filtered1]
        filtered2 = [x for x in squared if x > 100]
        
        return filtered2
    
    def process_data_with_generator(data_size: int) -> Generator[int, None, None]:
        """使用生成器处理数据"""
        # 生成数据
        data = range(data_size)
        
        # 处理数据：过滤偶数，平方，再过滤大于100的
        filtered1 = (x for x in data if x % 2 == 0)
        squared = (x * x for x in filtered1)
        filtered2 = (x for x in squared if x > 100)
        
        return filtered2
    
    def process_data_pipeline(data_size: int) -> Generator[int, None, None]:
        """使用生成器流水线处理数据"""
        for x in range(data_size):
            if x % 2 == 0:  # 过滤偶数
                squared = x * x
                if squared > 100:  # 过滤大于100的
                    yield squared
    
    print("练习6 - 性能优化对比:")
    
    data_size = 100000
    
    # 测试列表方式
    print(f"\n6.1 处理 {data_size} 个数据 - 列表方式:")
    start_time = time.time()
    list_result = process_data_with_list(data_size)
    list_time = time.time() - start_time
    print(f"  处理时间: {list_time:.4f} 秒")
    print(f"  结果数量: {len(list_result)}")
    print(f"  前5个结果: {list_result[:5]}")
    
    # 测试生成器方式
    print(f"\n6.2 处理 {data_size} 个数据 - 生成器方式:")
    start_time = time.time()
    gen_result = process_data_with_generator(data_size)
    gen_creation_time = time.time() - start_time
    
    # 获取结果
    start_time = time.time()
    gen_result_list = list(gen_result)
    gen_execution_time = time.time() - start_time
    
    print(f"  创建时间: {gen_creation_time:.6f} 秒")
    print(f"  执行时间: {gen_execution_time:.4f} 秒")
    print(f"  总时间: {gen_creation_time + gen_execution_time:.4f} 秒")
    print(f"  结果数量: {len(gen_result_list)}")
    print(f"  前5个结果: {gen_result_list[:5]}")
    
    # 测试流水线方式
    print(f"\n6.3 处理 {data_size} 个数据 - 流水线方式:")
    start_time = time.time()
    pipeline_result = list(process_data_pipeline(data_size))
    pipeline_time = time.time() - start_time
    print(f"  处理时间: {pipeline_time:.4f} 秒")
    print(f"  结果数量: {len(pipeline_result)}")
    print(f"  前5个结果: {pipeline_result[:5]}")
    
    # 性能对比
    print(f"\n6.4 性能对比:")
    print(f"  列表方式: {list_time:.4f} 秒")
    print(f"  生成器方式: {gen_creation_time + gen_execution_time:.4f} 秒")
    print(f"  流水线方式: {pipeline_time:.4f} 秒")
    
    if pipeline_time > 0:
        print(f"  流水线相比列表提升: {(list_time / pipeline_time):.1f}x")

exercise_6_performance_optimization()


# 练习7: 实战项目 - 数据分析工具
print("\n=== 练习7: 实战项目 - 数据分析工具 ===")

def exercise_7_data_analysis_tool():
    """练习7: 数据分析工具"""
    
    def generate_sales_data(days: int) -> Generator[dict, None, None]:
        """生成销售数据"""
        products = ["笔记本电脑", "手机", "平板", "耳机", "键盘", "鼠标"]
        regions = ["北京", "上海", "广州", "深圳"]
        
        for day in range(1, days + 1):
            # 每天生成多条销售记录
            daily_records = random.randint(5, 15)
            
            for _ in range(daily_records):
                yield {
                    "date": f"2024-01-{day:02d}",
                    "product": random.choice(products),
                    "region": random.choice(regions),
                    "quantity": random.randint(1, 10),
                    "unit_price": random.randint(100, 5000),
                    "sales_person": f"销售员{random.randint(1, 20):02d}"
                }
    
    def calculate_daily_revenue(sales_data: Iterator[dict]) -> Generator[Tuple[str, float], None, None]:
        """计算每日收入"""
        daily_revenue = defaultdict(float)
        
        for record in sales_data:
            date = record["date"]
            revenue = record["quantity"] * record["unit_price"]
            daily_revenue[date] += revenue
        
        for date, revenue in sorted(daily_revenue.items()):
            yield date, revenue
    
    def analyze_product_performance(sales_data: Iterator[dict]) -> Generator[Tuple[str, dict], None, None]:
        """分析产品表现"""
        product_stats = defaultdict(lambda: {"quantity": 0, "revenue": 0, "orders": 0})
        
        for record in sales_data:
            product = record["product"]
            quantity = record["quantity"]
            revenue = quantity * record["unit_price"]
            
            product_stats[product]["quantity"] += quantity
            product_stats[product]["revenue"] += revenue
            product_stats[product]["orders"] += 1
        
        for product, stats in product_stats.items():
            stats["avg_order_value"] = stats["revenue"] / stats["orders"] if stats["orders"] > 0 else 0
            yield product, stats
    
    def find_top_performers(sales_data: Iterator[dict], metric: str = "revenue") -> Generator[Tuple[str, float], None, None]:
        """找出顶级销售员"""
        sales_person_stats = defaultdict(lambda: {"quantity": 0, "revenue": 0, "orders": 0})
        
        for record in sales_data:
            person = record["sales_person"]
            quantity = record["quantity"]
            revenue = quantity * record["unit_price"]
            
            sales_person_stats[person]["quantity"] += quantity
            sales_person_stats[person]["revenue"] += revenue
            sales_person_stats[person]["orders"] += 1
        
        # 按指定指标排序
        sorted_performers = sorted(
            sales_person_stats.items(),
            key=lambda x: x[1][metric],
            reverse=True
        )
        
        for person, stats in sorted_performers:
            yield person, stats[metric]
    
    print("练习7 - 数据分析工具:")
    
    # 生成30天的销售数据
    print("\n7.1 生成销售数据...")
    sales_data = list(generate_sales_data(30))
    print(f"生成了 {len(sales_data)} 条销售记录")
    
    # 分析每日收入
    print("\n7.2 每日收入分析:")
    daily_revenues = list(calculate_daily_revenue(iter(sales_data)))
    total_revenue = sum(revenue for _, revenue in daily_revenues)
    avg_daily_revenue = total_revenue / len(daily_revenues)
    
    print(f"总收入: {total_revenue:,.2f} 元")
    print(f"平均日收入: {avg_daily_revenue:,.2f} 元")
    print("前5天收入:")
    for date, revenue in daily_revenues[:5]:
        print(f"  {date}: {revenue:,.2f} 元")
    
    # 产品表现分析
    print("\n7.3 产品表现分析:")
    product_performance = list(analyze_product_performance(iter(sales_data)))
    
    # 按收入排序
    product_performance.sort(key=lambda x: x[1]["revenue"], reverse=True)
    
    print("产品收入排行:")
    for i, (product, stats) in enumerate(product_performance[:3], 1):
        print(f"  {i}. {product}:")
        print(f"     收入: {stats['revenue']:,.2f} 元")
        print(f"     销量: {stats['quantity']} 件")
        print(f"     订单数: {stats['orders']} 单")
        print(f"     平均订单价值: {stats['avg_order_value']:,.2f} 元")
    
    # 销售员表现分析
    print("\n7.4 销售员表现分析:")
    top_performers = list(find_top_performers(iter(sales_data), "revenue"))
    
    print("收入排行榜 (前5名):")
    for i, (person, revenue) in enumerate(top_performers[:5], 1):
        print(f"  {i}. {person}: {revenue:,.2f} 元")
    
    # 区域分析
    print("\n7.5 区域分析:")
    region_stats = defaultdict(lambda: {"quantity": 0, "revenue": 0, "orders": 0})
    
    for record in sales_data:
        region = record["region"]
        quantity = record["quantity"]
        revenue = quantity * record["unit_price"]
        
        region_stats[region]["quantity"] += quantity
        region_stats[region]["revenue"] += revenue
        region_stats[region]["orders"] += 1
    
    print("各区域表现:")
    for region, stats in sorted(region_stats.items(), key=lambda x: x[1]["revenue"], reverse=True):
        print(f"  {region}:")
        print(f"    收入: {stats['revenue']:,.2f} 元")
        print(f"    销量: {stats['quantity']} 件")
        print(f"    订单数: {stats['orders']} 单")

exercise_7_data_analysis_tool()


print("\n=== 生成器综合练习完成 ===")
print("恭喜！你已经完成了所有生成器练习")
print("\n练习总结:")
print("1. 基础生成器 - 掌握了生成器的基本用法")
print("2. 生成器表达式 - 学会了简洁的数据处理方式")
print("3. 生成器方法 - 理解了send()、throw()、close()的应用")
print("4. 数据流处理 - 掌握了流式数据处理技巧")
print("5. 协程应用 - 学会了使用生成器实现协程")
print("6. 性能优化 - 了解了生成器的性能优势")
print("7. 实战项目 - 应用生成器解决实际问题")

print("\n下一步学习建议:")
print("1. 深入学习async/await异步编程")
print("2. 探索itertools模块的高级功能")
print("3. 学习更多函数式编程概念")
print("4. 在实际项目中应用生成器优化性能")
print("5. 研究生成器在数据科学中的应用")

print("\n=== 运行完成 ===")
print("通过这些练习，你应该已经熟练掌握了生成器的各种应用场景")
print("继续保持学习的热情，在实践中不断提升编程技能！")