# 高级输入输出技巧

## 概述

本节介绍Python中的高级输入输出技巧，包括命令行参数处理、环境变量使用、标准流重定向、缓冲区控制、大文件处理、多线程IO等高级主题。这些技巧在实际开发中非常有用，特别是在处理系统级编程和数据处理任务时。

## 学习目标

- 掌握命令行参数处理（sys.argv和argparse）
- 学会环境变量的读取和使用
- 了解标准输入输出重定向技巧
- 掌握缓冲区控制和实时输出
- 学会处理大文件和流式数据
- 了解多线程IO和内存映射文件
- 掌握压缩文件和序列化操作

## 完整代码

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
高级输入输出技巧

学习目标：
1. 掌握命令行参数处理
2. 学会环境变量的读取和使用
3. 了解标准输入输出重定向
4. 掌握缓冲区控制
5. 学会处理大文件和流式数据
6. 了解异步IO基础

作者：Python基础教程
日期：2024年
"""

import sys
import os
import argparse
import io
import time
import threading
import queue
from pathlib import Path
import tempfile
import gzip
import pickle
from contextlib import contextmanager

# ============================================================================
# 1. 命令行参数处理
# ============================================================================

print("=" * 50)
print("1. 命令行参数处理")
print("=" * 50)

# sys.argv - 基本命令行参数
print("\n--- sys.argv 基础 ---")
print(f"脚本名称：{sys.argv[0]}")
print(f"参数数量：{len(sys.argv)}")
print(f"所有参数：{sys.argv}")

if len(sys.argv) > 1:
    print("传入的参数：")
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"  参数{i}: {arg}")
else:
    print("没有传入额外参数")
    print("提示：可以这样运行脚本：python 07_advanced_io.py arg1 arg2 arg3")

# argparse - 高级参数解析
print("\n--- argparse 高级解析 ---")

def demo_argparse():
    """
    演示argparse的使用
    """
    # 创建解析器
    parser = argparse.ArgumentParser(
        description='高级IO演示程序',
        epilog='示例：python script.py -f input.txt -o output.txt --verbose'
    )
    
    # 添加参数
    parser.add_argument('input_file', nargs='?', default='demo.txt',
                       help='输入文件名（可选）')
    parser.add_argument('-f', '--file', dest='filename',
                       help='指定处理的文件')
    parser.add_argument('-o', '--output', dest='output',
                       help='输出文件名')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='详细输出模式')
    parser.add_argument('-c', '--count', type=int, default=10,
                       help='处理数量（默认：10）')
    parser.add_argument('--format', choices=['txt', 'json', 'csv'],
                       default='txt', help='输出格式')
    
    # 解析参数（使用默认值演示）
    # 在实际使用中，这会解析sys.argv
    demo_args = ['demo_input.txt', '-f', 'test.txt', '-v', '-c', '5', '--format', 'json']
    args = parser.parse_args(demo_args)
    
    print("解析结果：")
    print(f"  输入文件：{args.input_file}")
    print(f"  指定文件：{args.filename}")
    print(f"  输出文件：{args.output}")
    print(f"  详细模式：{args.verbose}")
    print(f"  处理数量：{args.count}")
    print(f"  输出格式：{args.format}")
    
    return args

# 演示argparse
try:
    args = demo_argparse()
except SystemExit:
    print("argparse演示完成")

# ============================================================================
# 2. 环境变量处理
# ============================================================================

print("\n" + "=" * 50)
print("2. 环境变量处理")
print("=" * 50)

# 读取环境变量
print("\n--- 环境变量读取 ---")

# 常用环境变量
common_vars = ['PATH', 'HOME', 'USER', 'SHELL', 'LANG']
for var in common_vars:
    value = os.environ.get(var, '未设置')
    if len(str(value)) > 50:
        value = str(value)[:50] + '...'
    print(f"{var}: {value}")

# 设置和使用自定义环境变量
print("\n--- 自定义环境变量 ---")

# 设置环境变量
os.environ['DEMO_APP_NAME'] = 'Python高级IO演示'
os.environ['DEMO_VERSION'] = '1.0.0'
os.environ['DEMO_DEBUG'] = 'true'

# 读取自定义环境变量
app_name = os.environ.get('DEMO_APP_NAME', '默认应用')
version = os.environ.get('DEMO_VERSION', '1.0')
debug_mode = os.environ.get('DEMO_DEBUG', 'false').lower() == 'true'

print(f"应用名称：{app_name}")
print(f"版本号：{version}")
print(f"调试模式：{debug_mode}")

# 环境变量配置类
class Config:
    """
    基于环境变量的配置类
    """
    def __init__(self):
        self.app_name = os.environ.get('APP_NAME', 'DefaultApp')
        self.debug = os.environ.get('DEBUG', 'false').lower() == 'true'
        self.log_level = os.environ.get('LOG_LEVEL', 'INFO')
        self.max_connections = int(os.environ.get('MAX_CONNECTIONS', '100'))
        self.timeout = float(os.environ.get('TIMEOUT', '30.0'))
    
    def __str__(self):
        return f"Config(app_name='{self.app_name}', debug={self.debug}, log_level='{self.log_level}')"

# 演示配置类
config = Config()
print(f"\n配置信息：{config}")

# ============================================================================
# 3. 标准输入输出重定向
# ============================================================================

print("\n" + "=" * 50)
print("3. 标准输入输出重定向")
print("=" * 50)

# 标准流信息
print("\n--- 标准流信息 ---")
print(f"标准输入：{sys.stdin}")
print(f"标准输出：{sys.stdout}")
print(f"标准错误：{sys.stderr}")

# 输出重定向到字符串
print("\n--- 输出重定向演示 ---")

# 保存原始stdout
original_stdout = sys.stdout

# 重定向到StringIO
string_buffer = io.StringIO()
sys.stdout = string_buffer

# 这些输出会被重定向
print("这行文本被重定向到缓冲区")
print("第二行重定向的文本")
print(f"当前时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")

# 恢复原始stdout
sys.stdout = original_stdout

# 获取重定向的内容
captured_output = string_buffer.getvalue()
print("捕获的输出内容：")
print(captured_output)

# 上下文管理器方式重定向
@contextmanager
def capture_output():
    """
    上下文管理器：捕获标准输出
    """
    old_stdout = sys.stdout
    buffer = io.StringIO()
    try:
        sys.stdout = buffer
        yield buffer
    finally:
        sys.stdout = old_stdout

print("\n--- 使用上下文管理器重定向 ---")
with capture_output() as output:
    print("这是在上下文管理器中的输出")
    print("多行输出测试")
    for i in range(3):
        print(f"循环输出 {i+1}")

print("捕获的内容：")
print(output.getvalue())

# 错误输出重定向
print("\n--- 错误输出处理 ---")

def demo_error_output():
    """
    演示错误输出的处理
    """
    # 正常输出
    print("这是正常输出", file=sys.stdout)
    
    # 错误输出
    print("这是错误信息", file=sys.stderr)
    
    # 同时输出到stdout和stderr
    message = "重要信息"
    print(f"INFO: {message}", file=sys.stdout)
    print(f"ERROR: {message}", file=sys.stderr)

demo_error_output()

# ============================================================================
# 4. 缓冲区控制
# ============================================================================

print("\n" + "=" * 50)
print("4. 缓冲区控制")
print("=" * 50)

# 创建临时目录用于演示
temp_dir = tempfile.mkdtemp(prefix='advanced_io_')
print(f"临时目录：{temp_dir}")

# 缓冲区模式演示
print("\n--- 缓冲区模式 ---")

def demo_buffering():
    """
    演示不同的缓冲区模式
    """
    test_file = os.path.join(temp_dir, 'buffer_test.txt')
    
    # 无缓冲写入（文本模式不支持buffering=0）
    print("行缓冲写入：")
    with open(test_file, 'w', buffering=1, encoding='utf-8') as f:
        for i in range(5):
            f.write(f"行缓冲数据 {i+1}\n")
            print(f"写入第 {i+1} 行")
            time.sleep(0.1)  # 模拟处理时间
    
    # 全缓冲写入
    print("\n全缓冲写入：")
    with open(test_file, 'w', buffering=8192, encoding='utf-8') as f:
        for i in range(5):
            f.write(f"全缓冲数据 {i+1}\n")
            print(f"写入第 {i+1} 行（可能还在缓冲区）")
            time.sleep(0.1)
        # 手动刷新缓冲区
        f.flush()
        print("手动刷新缓冲区")
    
    # 读取验证
    with open(test_file, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"\n文件内容：\n{content}")

demo_buffering()

# 实时输出演示
print("\n--- 实时输出演示 ---")

def progress_bar_demo():
    """
    演示实时进度条
    """
    print("进度条演示：")
    total = 20
    for i in range(total + 1):
        percent = (i / total) * 100
        bar_length = 20
        filled_length = int(bar_length * i // total)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        
        # 使用\r回到行首，实现覆盖效果
        print(f'\r进度: |{bar}| {percent:.1f}% 完成', end='', flush=True)
        time.sleep(0.1)
    
    print()  # 换行

progress_bar_demo()

# ============================================================================
# 5. 大文件处理
# ============================================================================

print("\n" + "=" * 50)
print("5. 大文件处理")
print("=" * 50)

# 创建测试大文件
print("\n--- 创建测试文件 ---")
large_file = os.path.join(temp_dir, 'large_file.txt')

def create_large_file(filename, lines=10000):
    """
    创建大文件用于测试
    """
    print(f"创建包含 {lines} 行的测试文件...")
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(lines):
            f.write(f"这是第 {i+1:06d} 行数据，包含一些测试内容和数字：{i*2}\n")
    
    size = os.path.getsize(filename)
    print(f"文件创建完成，大小：{size:,} 字节")
    return size

# 创建测试文件（较小的版本用于演示）
file_size = create_large_file(large_file, 1000)

# 逐行读取大文件
print("\n--- 逐行读取大文件 ---")

def process_large_file_by_lines(filename):
    """
    逐行处理大文件
    """
    line_count = 0
    word_count = 0
    
    start_time = time.time()
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line_count += 1
            word_count += len(line.split())
            
            # 每处理100行显示一次进度
            if line_count % 100 == 0:
                print(f"已处理 {line_count} 行")
    
    end_time = time.time()
    
    print(f"处理完成：")
    print(f"  总行数：{line_count:,}")
    print(f"  总词数：{word_count:,}")
    print(f"  处理时间：{end_time - start_time:.2f} 秒")

process_large_file_by_lines(large_file)

# 分块读取大文件
print("\n--- 分块读取大文件 ---")

def process_large_file_by_chunks(filename, chunk_size=8192):
    """
    分块处理大文件
    """
    total_size = 0
    chunk_count = 0
    
    start_time = time.time()
    
    with open(filename, 'r', encoding='utf-8') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            
            chunk_count += 1
            total_size += len(chunk)
            
            # 每处理10个块显示一次进度
            if chunk_count % 10 == 0:
                print(f"已处理 {chunk_count} 个块，{total_size:,} 字符")
    
    end_time = time.time()
    
    print(f"分块处理完成：")
    print(f"  总块数：{chunk_count}")
    print(f"  总字符数：{total_size:,}")
    print(f"  处理时间：{end_time - start_time:.2f} 秒")

process_large_file_by_chunks(large_file)

# ============================================================================
# 6. 压缩文件处理
# ============================================================================

print("\n" + "=" * 50)
print("6. 压缩文件处理")
print("=" * 50)

# 创建压缩文件
print("\n--- 创建和读取压缩文件 ---")

compressed_file = os.path.join(temp_dir, 'compressed_data.gz')

# 写入压缩文件
with gzip.open(compressed_file, 'wt', encoding='utf-8') as f:
    f.write("这是压缩文件的内容\n")
    f.write("支持中文内容\n")
    for i in range(100):
        f.write(f"压缩数据行 {i+1:03d}\n")

print(f"压缩文件创建完成")

# 比较文件大小
original_size = os.path.getsize(large_file)
compressed_size = os.path.getsize(compressed_file)
compression_ratio = (1 - compressed_size / original_size) * 100

print(f"原始文件大小：{original_size:,} 字节")
print(f"压缩文件大小：{compressed_size:,} 字节")
print(f"压缩率：{compression_ratio:.1f}%")

# 读取压缩文件
print("\n--- 读取压缩文件内容 ---")
with gzip.open(compressed_file, 'rt', encoding='utf-8') as f:
    lines = f.readlines()
    print(f"压缩文件包含 {len(lines)} 行")
    print("前5行内容：")
    for i, line in enumerate(lines[:5]):
        print(f"  {i+1}: {line.strip()}")

# ============================================================================
# 7. 序列化和反序列化
# ============================================================================

print("\n" + "=" * 50)
print("7. 序列化和反序列化")
print("=" * 50)

# 准备测试数据
test_data = {
    'name': '张三',
    'age': 25,
    'scores': [85, 92, 78, 90],
    'info': {
        'city': '北京',
        'email': 'zhangsan@example.com'
    },
    'timestamp': time.time()
}

print("\n--- Pickle序列化 ---")

# 序列化到文件
pickle_file = os.path.join(temp_dir, 'data.pickle')
with open(pickle_file, 'wb') as f:
    pickle.dump(test_data, f)

print(f"数据已序列化到：{pickle_file}")
print(f"序列化文件大小：{os.path.getsize(pickle_file)} 字节")

# 从文件反序列化
with open(pickle_file, 'rb') as f:
    loaded_data = pickle.load(f)

print("反序列化成功：")
print(f"  姓名：{loaded_data['name']}")
print(f"  年龄：{loaded_data['age']}")
print(f"  成绩：{loaded_data['scores']}")
print(f"  时间戳：{loaded_data['timestamp']}")

# 序列化到字节串
print("\n--- 序列化到内存 ---")
serialized_bytes = pickle.dumps(test_data)
print(f"序列化字节长度：{len(serialized_bytes)}")

# 从字节串反序列化
deserialized_data = pickle.loads(serialized_bytes)
print(f"内存反序列化成功：{deserialized_data['name']}")

# ============================================================================
# 8. 多线程IO
# ============================================================================

print("\n" + "=" * 50)
print("8. 多线程IO演示")
print("=" * 50)

def worker_thread(thread_id, input_queue, output_queue):
    """
    工作线程：处理IO任务
    """
    while True:
        try:
            task = input_queue.get(timeout=1)
            if task is None:  # 结束信号
                break
            
            # 模拟IO操作
            filename, content = task
            filepath = os.path.join(temp_dir, f'thread_{thread_id}_{filename}')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            result = f"线程 {thread_id} 完成文件：{filename}"
            output_queue.put(result)
            
            input_queue.task_done()
            
        except queue.Empty:
            break
        except Exception as e:
            output_queue.put(f"线程 {thread_id} 错误：{e}")
            input_queue.task_done()

print("\n--- 多线程文件写入 ---")

# 创建队列
input_queue = queue.Queue()
output_queue = queue.Queue()

# 准备任务
tasks = [
    (f'file_{i:03d}.txt', f'这是文件 {i} 的内容\n包含多行数据\n任务编号：{i}\n')
    for i in range(20)
]

# 添加任务到队列
for task in tasks:
    input_queue.put(task)

# 创建工作线程
num_threads = 3
threads = []

start_time = time.time()

for i in range(num_threads):
    t = threading.Thread(target=worker_thread, args=(i+1, input_queue, output_queue))
    t.start()
    threads.append(t)

print(f"启动 {num_threads} 个工作线程")

# 等待所有任务完成
input_queue.join()

# 发送结束信号
for _ in range(num_threads):
    input_queue.put(None)

# 等待所有线程结束
for t in threads:
    t.join()

end_time = time.time()

# 收集结果
results = []
while not output_queue.empty():
    results.append(output_queue.get())

print(f"\n多线程处理完成：")
print(f"  处理时间：{end_time - start_time:.2f} 秒")
print(f"  完成任务：{len(results)} 个")
print("前5个结果：")
for result in results[:5]:
    print(f"  {result}")

# ============================================================================
# 9. 内存映射文件
# ============================================================================

print("\n" + "=" * 50)
print("9. 内存映射文件")
print("=" * 50)

import mmap

# 创建用于内存映射的文件
mmap_file = os.path.join(temp_dir, 'mmap_test.txt')
with open(mmap_file, 'w', encoding='utf-8') as f:
    for i in range(1000):
        f.write(f"内存映射测试行 {i+1:04d}\n")

print(f"创建内存映射测试文件：{mmap_file}")
print(f"文件大小：{os.path.getsize(mmap_file):,} 字节")

# 使用内存映射读取文件
print("\n--- 内存映射读取 ---")
with open(mmap_file, 'r+b') as f:
    # 创建内存映射
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
        print(f"内存映射大小：{len(mm):,} 字节")
        
        # 读取前100个字节
        mm.seek(0)
        first_100_bytes = mm.read(100)
        print(f"前100字节：{first_100_bytes.decode('utf-8', errors='ignore')}")
        
        # 查找特定内容
        mm.seek(0)
        search_text = b'0050'
        pos = mm.find(search_text)
        if pos != -1:
            print(f"找到 '{search_text.decode()}' 在位置：{pos}")
            mm.seek(pos)
            line = mm.readline()
            print(f"该行内容：{line.decode('utf-8').strip()}")

# ============================================================================
# 10. 实际应用示例
# ============================================================================

print("\n" + "=" * 50)
print("10. 实际应用示例")
print("=" * 50)

class LogProcessor:
    """
    日志处理器：演示高级IO技巧的综合应用
    """
    
    def __init__(self, log_dir):
        self.log_dir = log_dir
        self.stats = {
            'total_lines': 0,
            'error_count': 0,
            'warning_count': 0,
            'info_count': 0
        }
    
    def process_log_file(self, filename):
        """
        处理单个日志文件
        """
        filepath = os.path.join(self.log_dir, filename)
        
        if not os.path.exists(filepath):
            print(f"文件不存在：{filepath}")
            return
        
        print(f"处理日志文件：{filename}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                self.stats['total_lines'] += 1
                
                # 分析日志级别
                line_lower = line.lower()
                if 'error' in line_lower:
                    self.stats['error_count'] += 1
                elif 'warning' in line_lower or 'warn' in line_lower:
                    self.stats['warning_count'] += 1
                elif 'info' in line_lower:
                    self.stats['info_count'] += 1
    
    def generate_report(self, output_file):
        """
        生成处理报告
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("日志处理报告\n")
            f.write("=" * 30 + "\n")
            f.write(f"生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("统计信息：\n")
            f.write(f"  总行数：{self.stats['total_lines']:,}\n")
            f.write(f"  错误数：{self.stats['error_count']:,}\n")
            f.write(f"  警告数：{self.stats['warning_count']:,}\n")
            f.write(f"  信息数：{self.stats['info_count']:,}\n")
            
            if self.stats['total_lines'] > 0:
                error_rate = (self.stats['error_count'] / self.stats['total_lines']) * 100
                f.write(f"\n错误率：{error_rate:.2f}%\n")
        
        print(f"报告已生成：{output_file}")

print("\n--- 日志处理器演示 ---")

# 创建示例日志文件
log_file = os.path.join(temp_dir, 'application.log')
with open(log_file, 'w', encoding='utf-8') as f:
    log_entries = [
        "2024-01-01 10:00:00 INFO 应用程序启动",
        "2024-01-01 10:00:01 INFO 加载配置文件",
        "2024-01-01 10:00:02 WARNING 配置项缺失，使用默认值",
        "2024-01-01 10:00:03 INFO 连接数据库",
        "2024-01-01 10:00:04 ERROR 数据库连接失败",
        "2024-01-01 10:00:05 INFO 重试连接数据库",
        "2024-01-01 10:00:06 INFO 数据库连接成功",
        "2024-01-01 10:00:07 WARNING 内存使用率较高",
        "2024-01-01 10:00:08 ERROR 处理请求时发生异常",
        "2024-01-01 10:00:09 INFO 应用程序正常运行"
    ]
    
    for entry in log_entries:
        f.write(entry + "\n")

# 使用日志处理器
processor = LogProcessor(temp_dir)
processor.process_log_file('application.log')

# 生成报告
report_file = os.path.join(temp_dir, 'log_report.txt')
processor.generate_report(report_file)

# 显示报告内容
with open(report_file, 'r', encoding='utf-8') as f:
    print("\n生成的报告：")
    print(f.read())

# ============================================================================
# 11. 练习题
# ============================================================================

print("\n" + "=" * 50)
print("11. 练习题")
print("=" * 50)

print("""
练习题：

1. 基础练习：
   - 编写命令行工具，支持多种参数选项
   - 创建配置文件读取器，支持环境变量覆盖
   - 实现简单的进度条显示功能

2. 进阶练习：
   - 编写大文件分割和合并工具
   - 创建多线程文件处理程序
   - 实现日志文件轮转功能

3. 思考题：
   - 什么时候使用内存映射文件？
   - 如何选择合适的缓冲区大小？
   - 多线程IO的优势和注意事项？

4. 挑战练习：
   - 实现一个通用的数据处理管道
   - 创建支持插件的文件处理框架
   - 编写高性能的日志分析工具
""")

# ============================================================================
# 12. 清理临时文件
# ============================================================================

print("\n" + "=" * 50)
print("12. 临时文件清理")
print("=" * 50)

# 列出创建的文件
if os.path.exists(temp_dir):
    files = os.listdir(temp_dir)
    print(f"\n临时目录中的文件数量：{len(files)}")
    total_size = 0
    
    print("文件列表：")
    for file in sorted(files):
        file_path = os.path.join(temp_dir, file)
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            total_size += size
            print(f"  {file} ({size:,} 字节)")
    
    print(f"\n总大小：{total_size:,} 字节")
    print(f"临时目录：{temp_dir}")
    print("提示：程序结束后可以手动删除临时目录")

# ============================================================================
# 13. 知识点总结
# ============================================================================

print("\n" + "=" * 50)
print("13. 知识点总结")
print("=" * 50)

print("""
知识点总结：

1. 命令行参数：
   - sys.argv：基本参数获取
   - argparse：高级参数解析
   - 参数验证和类型转换

2. 环境变量：
   - os.environ：读取和设置
   - 配置管理最佳实践
   - 默认值处理

3. 标准流重定向：
   - sys.stdout/stderr重定向
   - StringIO缓冲区
   - 上下文管理器

4. 缓冲区控制：
   - 不同缓冲模式
   - flush()强制刷新
   - 实时输出技巧

5. 大文件处理：
   - 逐行读取
   - 分块处理
   - 内存映射文件

6. 高级技巧：
   - 压缩文件处理
   - 序列化/反序列化
   - 多线程IO
   - 原子性操作

7. 性能优化：
   - 选择合适的读取方式
   - 缓冲区大小调优
   - 并发处理策略

8. 最佳实践：
   - 异常处理
   - 资源管理
   - 跨平台兼容性
   - 安全性考虑
""")

print("\n程序运行完成！")
print(f"临时文件保存在：{temp_dir}")
print("建议：查看临时目录中的文件，了解各种IO操作的效果。")
```

## 代码详解

### 1. 命令行参数处理

**sys.argv基础**：
- `sys.argv[0]`：脚本名称
- `sys.argv[1:]`：命令行参数列表
- 适用于简单的参数处理

**argparse高级解析**：
- 创建ArgumentParser对象
- 添加各种类型的参数（位置参数、可选参数、标志参数）
- 支持参数验证、类型转换、帮助信息
- 提供更好的用户体验

### 2. 环境变量处理

**读取环境变量**：
- `os.environ.get()`：安全读取，支持默认值
- `os.environ[]`：直接访问，不存在时抛出异常

**配置管理**：
- 使用环境变量进行配置
- 支持类型转换（字符串转布尔、整数等）
- 提供默认值和验证

### 3. 标准流重定向

**输出重定向**：
- 使用StringIO捕获输出
- 上下文管理器确保资源正确释放
- 区分标准输出和错误输出

**应用场景**：
- 测试输出内容
- 日志捕获
- 输出格式化

### 4. 缓冲区控制

**缓冲模式**：
- 行缓冲：每行自动刷新
- 全缓冲：达到缓冲区大小才刷新
- 无缓冲：立即写入（二进制模式）

**实时输出**：
- 使用`flush=True`强制刷新
- `\r`回车符实现覆盖效果
- 进度条和实时状态显示

### 5. 大文件处理

**逐行读取**：
- 内存占用小
- 适合文本文件处理
- 支持迭代器模式

**分块读取**：
- 控制内存使用
- 适合二进制文件
- 可调节块大小

**内存映射**：
- 虚拟内存技术
- 适合大文件随机访问
- 系统级优化

### 6. 压缩文件处理

**gzip模块**：
- 透明的压缩/解压缩
- 支持文本和二进制模式
- 节省存储空间

### 7. 序列化操作

**pickle模块**：
- Python对象序列化
- 支持复杂数据结构
- 二进制格式，高效存储

### 8. 多线程IO

**并发处理**：
- 使用队列进行任务分发
- 工作线程模式
- 提高IO密集型任务性能

**注意事项**：
- GIL限制CPU密集型任务
- 适合IO密集型操作
- 需要考虑线程安全

## 学习要点

### 性能优化技巧

1. **选择合适的读取方式**：
   - 小文件：一次性读取
   - 大文件：逐行或分块读取
   - 随机访问：内存映射

2. **缓冲区优化**：
   - 根据文件大小调整缓冲区
   - 考虑系统内存限制
   - 平衡内存使用和性能

3. **并发策略**：
   - IO密集型：多线程
   - CPU密集型：多进程
   - 异步IO：适合网络操作

### 最佳实践

1. **资源管理**：
   - 使用with语句确保文件关闭
   - 及时释放大对象
   - 避免内存泄漏

2. **异常处理**：
   - 处理文件不存在、权限不足等异常
   - 提供有意义的错误信息
   - 优雅降级

3. **跨平台兼容**：
   - 使用os.path或pathlib处理路径
   - 注意文件编码问题
   - 考虑不同操作系统的差异

## 实践练习

### 基础练习

1. **命令行工具**：
```python
# 创建一个文件处理工具
# 支持 -i 输入文件, -o 输出文件, -f 格式选项
```

2. **配置读取器**：
```python
# 从配置文件和环境变量读取配置
# 环境变量优先级更高
```

3. **进度条实现**：
```python
# 实现可复用的进度条类
# 支持百分比、时间估算等
```

### 进阶练习

1. **文件分割工具**：
```python
# 将大文件分割成多个小文件
# 支持按大小或行数分割
```

2. **多线程处理**：
```python
# 使用线程池处理多个文件
# 实现任务队列和结果收集
```

3. **日志轮转**：
```python
# 实现日志文件自动轮转
# 支持按大小、时间轮转
```

## 运行示例

```bash
# 基本运行
python 07_advanced_io.py

# 带参数运行
python 07_advanced_io.py input.txt -v --format json

# 设置环境变量
export DEBUG=true
export LOG_LEVEL=DEBUG
python 07_advanced_io.py
```

## 扩展思考

1. **什么时候使用内存映射文件？**
   - 大文件随机访问
   - 多进程共享数据
   - 系统级性能优化需求

2. **如何选择缓冲区大小？**
   - 考虑可用内存
   - 文件大小和访问模式
   - 系统IO特性

3. **多线程IO的优势和限制？**
   - 优势：提高IO并发度
   - 限制：GIL、线程开销
   - 适用场景：IO密集型任务

## 模块导航

- [上一节：文件输出操作](./file-output.md)
- [下一节：综合练习](./exercises.md)
- [返回目录](./index.md)