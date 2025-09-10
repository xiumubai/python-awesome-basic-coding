#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成器的内存效率和惰性求值

本模块演示生成器在内存使用和性能方面的优势，
包括惰性求值、内存效率对比、大数据处理等应用场景。

学习目标:
1. 理解生成器的内存效率优势
2. 掌握惰性求值的概念和应用
3. 学会使用生成器处理大数据集
4. 了解生成器在性能优化中的作用
5. 掌握内存使用的监控和对比方法
"""

import sys
import time
import gc
from typing import Iterator, List, Generator
from itertools import islice


def get_memory_usage():
    """获取当前进程的内存使用量(简化版本)"""
    # 强制垃圾回收
    gc.collect()
    # 返回一个模拟的内存使用量
    return len(gc.get_objects()) * 0.001  # 简化的内存估算


# 1. 内存效率对比
print("=== 1. 内存效率对比 ===")

def create_large_list(n: int) -> List[int]:
    """创建大列表 - 占用大量内存"""
    return [x * x for x in range(n)]

def create_large_generator(n: int) -> Generator[int, None, None]:
    """创建大生成器 - 惰性求值"""
    for x in range(n):
        yield x * x

print("内存使用对比演示:")
n = 1000000  # 100万个数字

# 测试列表的内存使用
print(f"创建前内存使用: {get_memory_usage():.2f} MB")

start_time = time.time()
large_list = create_large_list(n)
list_time = time.time() - start_time
list_memory = get_memory_usage()

print(f"创建列表后内存使用: {list_memory:.2f} MB")
print(f"列表创建时间: {list_time:.4f} 秒")
print(f"列表大小: {sys.getsizeof(large_list) / 1024 / 1024:.2f} MB")

# 清理列表
del large_list
time.sleep(0.1)  # 等待垃圾回收

# 测试生成器的内存使用
start_memory = get_memory_usage()
print(f"\n清理后内存使用: {start_memory:.2f} MB")

start_time = time.time()
large_generator = create_large_generator(n)
gen_time = time.time() - start_time
gen_memory = get_memory_usage()

print(f"创建生成器后内存使用: {gen_memory:.2f} MB")
print(f"生成器创建时间: {gen_time:.6f} 秒")
print(f"生成器大小: {sys.getsizeof(large_generator)} 字节")

print(f"\n内存节省: {((list_memory - gen_memory) / list_memory * 100):.1f}%")
print(f"创建速度提升: {(list_time / gen_time):.0f}x")


# 2. 惰性求值演示
print("\n=== 2. 惰性求值演示 ===")

def fibonacci_list(n: int) -> List[int]:
    """斐波那契数列 - 列表版本"""
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def fibonacci_generator(n: int) -> Generator[int, None, None]:
    """斐波那契数列 - 生成器版本"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def infinite_fibonacci() -> Generator[int, None, None]:
    """无限斐波那契数列"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("惰性求值特性演示:")

# 列表版本 - 立即计算所有值
print("\n1. 列表版本 - 立即计算:")
start_time = time.time()
fib_list = fibonacci_list(10)
print(f"计算时间: {time.time() - start_time:.6f} 秒")
print(f"前10个斐波那契数: {fib_list}")

# 生成器版本 - 按需计算
print("\n2. 生成器版本 - 按需计算:")
start_time = time.time()
fib_gen = fibonacci_generator(10)
print(f"创建时间: {time.time() - start_time:.6f} 秒")

print("逐个获取值:")
for i, value in enumerate(fib_gen):
    print(f"第{i+1}个值: {value}")
    if i >= 4:  # 只获取前5个值
        break

# 无限生成器 - 只在需要时计算
print("\n3. 无限生成器演示:")
inf_fib = infinite_fibonacci()
print("获取前8个斐波那契数:")
for i, value in enumerate(inf_fib):
    print(f"F({i}) = {value}")
    if i >= 7:
        break


# 3. 大数据处理
print("\n=== 3. 大数据处理 ===")

def process_large_dataset_list(filename: str) -> List[str]:
    """使用列表处理大数据集"""
    result = []
    # 模拟读取大文件
    for i in range(1000000):
        line = f"数据行 {i}: 这是一些示例数据内容\n"
        # 简单的数据处理
        if "示例" in line:
            result.append(line.strip().upper())
    return result

def process_large_dataset_generator(filename: str) -> Generator[str, None, None]:
    """使用生成器处理大数据集"""
    # 模拟读取大文件
    for i in range(1000000):
        line = f"数据行 {i}: 这是一些示例数据内容\n"
        # 简单的数据处理
        if "示例" in line:
            yield line.strip().upper()

print("大数据处理对比:")

# 使用生成器处理 - 内存友好
print("\n使用生成器处理大数据集:")
start_memory = get_memory_usage()
start_time = time.time()

data_gen = process_large_dataset_generator("large_file.txt")
processed_count = 0

# 只处理前1000条记录
for processed_line in islice(data_gen, 1000):
    processed_count += 1
    if processed_count <= 3:  # 显示前3条
        print(f"处理结果 {processed_count}: {processed_line[:50]}...")

gen_time = time.time() - start_time
gen_memory = get_memory_usage()

print(f"生成器处理时间: {gen_time:.4f} 秒")
print(f"内存使用: {gen_memory - start_memory:.2f} MB")
print(f"处理记录数: {processed_count}")


# 4. 数据流水线
print("\n=== 4. 数据流水线 ===")

def read_numbers(count: int) -> Generator[int, None, None]:
    """数据源 - 生成数字"""
    for i in range(count):
        yield i

def filter_even(numbers: Iterator[int]) -> Generator[int, None, None]:
    """过滤器 - 只保留偶数"""
    for num in numbers:
        if num % 2 == 0:
            yield num

def square_numbers(numbers: Iterator[int]) -> Generator[int, None, None]:
    """转换器 - 计算平方"""
    for num in numbers:
        yield num * num

def format_output(numbers: Iterator[int]) -> Generator[str, None, None]:
    """格式化器 - 格式化输出"""
    for num in numbers:
        yield f"结果: {num}"

print("数据流水线演示:")

# 构建数据处理流水线
pipeline = format_output(
    square_numbers(
        filter_even(
            read_numbers(20)
        )
    )
)

print("流水线处理结果:")
for i, result in enumerate(pipeline):
    print(result)
    if i >= 4:  # 只显示前5个结果
        break

print("\n流水线特点:")
print("1. 每个阶段都是生成器")
print("2. 数据按需流动")
print("3. 内存使用恒定")
print("4. 可以处理无限数据流")


# 5. 文件处理优化
print("\n=== 5. 文件处理优化 ===")

def read_file_lines_list(filename: str) -> List[str]:
    """一次性读取所有行到列表"""
    # 模拟文件内容
    lines = []
    for i in range(100000):
        lines.append(f"这是文件的第 {i+1} 行内容\n")
    return lines

def read_file_lines_generator(filename: str) -> Generator[str, None, None]:
    """逐行生成文件内容"""
    # 模拟文件内容
    for i in range(100000):
        yield f"这是文件的第 {i+1} 行内容\n"

def process_log_file(lines: Iterator[str]) -> Generator[dict, None, None]:
    """处理日志文件"""
    for line_num, line in enumerate(lines, 1):
        # 模拟日志解析
        if "错误" in line or "ERROR" in line:
            yield {
                "line_number": line_num,
                "level": "ERROR",
                "content": line.strip()
            }
        elif "警告" in line or "WARNING" in line:
            yield {
                "line_number": line_num,
                "level": "WARNING", 
                "content": line.strip()
            }

print("文件处理优化演示:")

# 使用生成器处理大文件
print("\n使用生成器逐行处理:")
start_memory = get_memory_usage()

file_lines = read_file_lines_generator("large_log.txt")
log_entries = process_log_file(file_lines)

# 只处理前几个匹配的条目
processed = 0
for entry in log_entries:
    if "第 50" in entry["content"] or "第 100" in entry["content"]:
        print(f"发现日志: 行 {entry['line_number']}, 级别 {entry['level']}")
        processed += 1
        if processed >= 3:
            break

end_memory = get_memory_usage()
print(f"内存使用: {end_memory - start_memory:.2f} MB")


# 6. 性能基准测试
print("\n=== 6. 性能基准测试 ===")

def benchmark_list_vs_generator():
    """基准测试：列表 vs 生成器"""
    n = 100000
    
    print(f"处理 {n} 个元素的性能对比:")
    
    # 测试列表性能
    start_time = time.time()
    start_memory = get_memory_usage()
    
    # 创建列表并处理前100个元素
    data_list = [x * 2 for x in range(n)]
    result_list = []
    for i, item in enumerate(data_list):
        if i >= 100:
            break
        result_list.append(item + 1)
    
    list_time = time.time() - start_time
    list_memory = get_memory_usage() - start_memory
    
    del data_list, result_list
    time.sleep(0.1)
    
    # 测试生成器性能
    start_time = time.time()
    start_memory = get_memory_usage()
    
    # 创建生成器并处理前100个元素
    data_gen = (x * 2 for x in range(n))
    result_gen = []
    for i, item in enumerate(data_gen):
        if i >= 100:
            break
        result_gen.append(item + 1)
    
    gen_time = time.time() - start_time
    gen_memory = get_memory_usage() - start_memory
    
    print(f"\n列表方式:")
    print(f"  时间: {list_time:.6f} 秒")
    print(f"  内存: {list_memory:.2f} MB")
    
    print(f"\n生成器方式:")
    print(f"  时间: {gen_time:.6f} 秒")
    print(f"  内存: {gen_memory:.2f} MB")
    
    if list_memory > 0:
        print(f"\n内存节省: {((list_memory - gen_memory) / list_memory * 100):.1f}%")
    if gen_time > 0:
        print(f"速度比较: 生成器是列表的 {(list_time / gen_time):.1f}x")

benchmark_list_vs_generator()


# 7. 实际应用场景
print("\n=== 7. 实际应用场景 ===")

def csv_reader_generator(filename: str) -> Generator[dict, None, None]:
    """CSV文件读取器 - 生成器版本"""
    # 模拟CSV文件
    headers = ["id", "name", "age", "city"]
    
    for i in range(10000):
        row_data = {
            "id": i + 1,
            "name": f"用户{i+1}",
            "age": 20 + (i % 50),
            "city": ["北京", "上海", "广州", "深圳"][i % 4]
        }
        yield row_data

def filter_users_by_age(users: Iterator[dict], min_age: int, max_age: int) -> Generator[dict, None, None]:
    """按年龄过滤用户"""
    for user in users:
        if min_age <= user["age"] <= max_age:
            yield user

def group_users_by_city(users: Iterator[dict]) -> dict:
    """按城市分组用户"""
    city_groups = {}
    for user in users:
        city = user["city"]
        if city not in city_groups:
            city_groups[city] = []
        city_groups[city].append(user)
    return city_groups

print("实际应用场景演示:")

# 数据处理流水线
print("\n1. 用户数据处理流水线:")
all_users = csv_reader_generator("users.csv")
young_users = filter_users_by_age(all_users, 25, 35)

# 只处理前10个符合条件的用户
processed_users = []
for user in young_users:
    processed_users.append(user)
    if len(processed_users) >= 10:
        break

print(f"找到 {len(processed_users)} 个25-35岁的用户:")
for user in processed_users[:3]:
    print(f"  {user['name']}, {user['age']}岁, {user['city']}")

# 数据聚合
print("\n2. 数据聚合示例:")
all_users_again = csv_reader_generator("users.csv")
filtered_users = filter_users_by_age(all_users_again, 30, 40)
city_stats = {}

for user in filtered_users:
    city = user["city"]
    if city not in city_stats:
        city_stats[city] = 0
    city_stats[city] += 1

print("30-40岁用户城市分布:")
for city, count in city_stats.items():
    print(f"  {city}: {count} 人")


# 8. 注意事项和最佳实践
print("\n=== 8. 注意事项和最佳实践 ===")

def demonstrate_generator_exhaustion():
    """演示生成器的一次性特性"""
    def simple_gen():
        for i in range(3):
            yield i
    
    gen = simple_gen()
    
    print("第一次遍历:")
    for value in gen:
        print(f"  值: {value}")
    
    print("\n第二次遍历 (生成器已耗尽):")
    for value in gen:
        print(f"  值: {value}")
    print("  (没有输出，因为生成器已耗尽)")
    
    print("\n重新创建生成器:")
    gen = simple_gen()
    for value in gen:
        print(f"  值: {value}")

print("生成器使用注意事项:")
demonstrate_generator_exhaustion()

print("\n最佳实践:")
print("1. 处理大数据集时优先使用生成器")
print("2. 构建数据处理流水线时使用生成器链")
print("3. 注意生成器的一次性特性")
print("4. 在需要多次遍历时重新创建生成器")
print("5. 使用islice()限制生成器输出")
print("6. 监控内存使用情况")
print("7. 结合itertools模块使用")


print("\n=== 内存效率和惰性求值学习完成 ===")
print("关键要点:")
print("1. 生成器显著减少内存使用")
print("2. 惰性求值按需计算，提高效率")
print("3. 适合处理大数据集和无限序列")
print("4. 可以构建高效的数据处理流水线")
print("5. 在文件处理和数据分析中非常有用")
print("6. 需要注意生成器的一次性特性")
print("7. 是Python性能优化的重要工具")

print("\n=== 运行完成 ===")
print("本模块演示了生成器在内存效率和性能优化方面的强大优势")
print("建议在处理大数据时优先考虑使用生成器")