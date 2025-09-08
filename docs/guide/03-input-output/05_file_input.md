# 文件输入操作

## 概述

文件输入是Python编程中的重要技能，涉及文件的打开、读取、编码处理和异常处理等多个方面。本节将详细介绍各种文件读取方法和最佳实践。

## 学习目标

- 掌握文件的打开和关闭操作
- 学会读取文件的不同方法
- 了解文件编码和异常处理
- 掌握with语句的使用
- 学会处理不同格式的文件
- 掌握大文件处理技巧

## 完整代码

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件输入操作

学习目标：
1. 掌握文件的打开和关闭操作
2. 学会读取文件的不同方法
3. 了解文件编码和异常处理
4. 掌握with语句的使用
5. 学会处理不同格式的文件

作者：Python基础教程
日期：2024年
"""

import os
import json
import csv
from pathlib import Path

# ============================================================================
# 1. 文件打开和关闭基础
# ============================================================================

print("=" * 50)
print("1. 文件打开和关闭基础")
print("=" * 50)

# 首先创建一个示例文件用于演示
sample_text = """这是第一行文本
这是第二行文本
这是第三行文本
包含数字：123
包含特殊字符：@#$%
"""

# 创建示例文件
with open('sample.txt', 'w', encoding='utf-8') as f:
    f.write(sample_text)

print("已创建示例文件 sample.txt")

# 基本的文件打开方式
print("\n--- 基本文件打开方式 ---")

# 方式1：传统方式（需要手动关闭）
print("\n传统方式（不推荐）：")
file = open('sample.txt', 'r', encoding='utf-8')
content = file.read()
print(f"文件内容：\n{content}")
file.close()  # 必须手动关闭文件
print("文件已关闭")

# 方式2：with语句（推荐方式）
print("\nwith语句（推荐）：")
with open('sample.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(f"文件内容：\n{content}")
# 文件会自动关闭，即使发生异常也会关闭
print("文件自动关闭")

# ============================================================================
# 2. 文件读取的不同方法
# ============================================================================

print("\n" + "=" * 50)
print("2. 文件读取的不同方法")
print("=" * 50)

# read() - 读取整个文件
print("\n--- read() 方法 ---")
with open('sample.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"整个文件内容：\n{repr(content)}")
    print(f"文件长度：{len(content)} 个字符")

# read(size) - 读取指定字符数
print("\n--- read(size) 方法 ---")
with open('sample.txt', 'r', encoding='utf-8') as f:
    first_10_chars = f.read(10)
    print(f"前10个字符：{repr(first_10_chars)}")
    next_10_chars = f.read(10)
    print(f"接下来10个字符：{repr(next_10_chars)}")

# readline() - 读取一行
print("\n--- readline() 方法 ---")
with open('sample.txt', 'r', encoding='utf-8') as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    print(f"第一行：{repr(line1)}")
    print(f"第二行：{repr(line2)}")
    print(f"第三行：{repr(line3)}")

# readlines() - 读取所有行到列表
print("\n--- readlines() 方法 ---")
with open('sample.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(f"所有行（列表）：{lines}")
    print(f"总共 {len(lines)} 行")
    for i, line in enumerate(lines, 1):
        print(f"第{i}行：{line.strip()}")

# 迭代读取（推荐大文件）
print("\n--- 迭代读取（内存友好）---")
with open('sample.txt', 'r', encoding='utf-8') as f:
    print("逐行迭代：")
    for line_num, line in enumerate(f, 1):
        print(f"  行{line_num}：{line.strip()}")

# ============================================================================
# 3. 文件编码处理
# ============================================================================

print("\n" + "=" * 50)
print("3. 文件编码处理")
print("=" * 50)

# 创建不同编码的文件
print("\n--- 创建不同编码的文件 ---")

# UTF-8编码（推荐）
with open('utf8_file.txt', 'w', encoding='utf-8') as f:
    f.write("UTF-8编码：你好世界！Hello World!\n")
    f.write("特殊字符：©®™€£¥\n")
    f.write("表情符号：😀😃😄😁\n")

# GBK编码
with open('gbk_file.txt', 'w', encoding='gbk') as f:
    f.write("GBK编码：你好世界！\n")
    f.write("中文测试文本\n")

print("已创建不同编码的文件")

# 读取不同编码的文件
print("\n--- 读取不同编码的文件 ---")

# 读取UTF-8文件
print("\n读取UTF-8文件：")
with open('utf8_file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

# 读取GBK文件
print("读取GBK文件：")
with open('gbk_file.txt', 'r', encoding='gbk') as f:
    content = f.read()
    print(content)

# 编码错误处理
print("\n--- 编码错误处理 ---")

# 错误处理策略
strategies = ['ignore', 'replace', 'strict']
for strategy in strategies:
    try:
        print(f"\n使用 {strategy} 策略读取GBK文件（用UTF-8）：")
        with open('gbk_file.txt', 'r', encoding='utf-8', errors=strategy) as f:
            content = f.read()
            print(f"结果：{repr(content)}")
    except UnicodeDecodeError as e:
        print(f"编码错误：{e}")

# ============================================================================
# 4. 异常处理
# ============================================================================

print("\n" + "=" * 50)
print("4. 文件操作异常处理")
print("=" * 50)

def safe_read_file(filename, encoding='utf-8'):
    """
    安全读取文件的函数
    """
    try:
        with open(filename, 'r', encoding=encoding) as f:
            return f.read()
    except FileNotFoundError:
        print(f"错误：文件 '{filename}' 不存在")
        return None
    except PermissionError:
        print(f"错误：没有权限读取文件 '{filename}'")
        return None
    except UnicodeDecodeError as e:
        print(f"错误：文件编码问题 - {e}")
        return None
    except Exception as e:
        print(f"未知错误：{e}")
        return None

print("\n--- 异常处理演示 ---")

# 测试正常文件
print("\n读取存在的文件：")
content = safe_read_file('sample.txt')
if content:
    print(f"成功读取，内容长度：{len(content)} 字符")

# 测试不存在的文件
print("\n读取不存在的文件：")
content = safe_read_file('nonexistent.txt')

# 测试编码问题
print("\n用错误编码读取文件：")
content = safe_read_file('gbk_file.txt', encoding='ascii')

# ============================================================================
# 5. 文件信息获取
# ============================================================================

print("\n" + "=" * 50)
print("5. 文件信息获取")
print("=" * 50)

def get_file_info(filename):
    """
    获取文件详细信息
    """
    try:
        # 使用os.path
        if os.path.exists(filename):
            stat = os.stat(filename)
            print(f"\n文件：{filename}")
            print(f"大小：{stat.st_size} 字节")
            print(f"创建时间：{stat.st_ctime}")
            print(f"修改时间：{stat.st_mtime}")
            print(f"是否为文件：{os.path.isfile(filename)}")
            print(f"是否为目录：{os.path.isdir(filename)}")
            
            # 使用pathlib（更现代的方式）
            path = Path(filename)
            print(f"文件名：{path.name}")
            print(f"扩展名：{path.suffix}")
            print(f"父目录：{path.parent}")
            print(f"绝对路径：{path.absolute()}")
        else:
            print(f"文件 {filename} 不存在")
    except Exception as e:
        print(f"获取文件信息时出错：{e}")

print("\n--- 文件信息演示 ---")
get_file_info('sample.txt')
get_file_info('utf8_file.txt')

# ============================================================================
# 6. 读取特殊格式文件
# ============================================================================

print("\n" + "=" * 50)
print("6. 读取特殊格式文件")
print("=" * 50)

# 创建JSON文件
print("\n--- JSON文件处理 ---")
data = {
    "name": "张三",
    "age": 25,
    "scores": [85, 92, 78],
    "info": {
        "city": "北京",
        "email": "zhangsan@example.com"
    }
}

# 写入JSON文件
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("已创建JSON文件")

# 读取JSON文件
with open('data.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)
    print(f"JSON数据：{loaded_data}")
    print(f"姓名：{loaded_data['name']}")
    print(f"年龄：{loaded_data['age']}")
    print(f"分数：{loaded_data['scores']}")

# 创建CSV文件
print("\n--- CSV文件处理 ---")
csv_data = [
    ['姓名', '年龄', '城市', '分数'],
    ['张三', '25', '北京', '85'],
    ['李四', '22', '上海', '92'],
    ['王五', '28', '广州', '78']
]

# 写入CSV文件
with open('students.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)

print("已创建CSV文件")

# 读取CSV文件
print("\n读取CSV文件：")
with open('students.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row_num, row in enumerate(reader):
        if row_num == 0:
            print(f"表头：{row}")
        else:
            print(f"数据行{row_num}：{row}")

# 使用DictReader读取CSV
print("\n使用DictReader读取CSV：")
with open('students.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"学生：{row['姓名']}，年龄：{row['年龄']}，城市：{row['城市']}，分数：{row['分数']}")

# ============================================================================
# 7. 大文件处理技巧
# ============================================================================

print("\n" + "=" * 50)
print("7. 大文件处理技巧")
print("=" * 50)

# 创建一个较大的示例文件
print("\n--- 创建大文件示例 ---")
with open('large_file.txt', 'w', encoding='utf-8') as f:
    for i in range(1000):
        f.write(f"这是第{i+1}行，包含一些测试数据：{i*2}, {i*3}, {i*5}\n")

print("已创建大文件示例（1000行）")

# 逐行处理大文件（内存友好）
print("\n--- 逐行处理大文件 ---")
def process_large_file(filename):
    """
    内存友好的大文件处理
    """
    line_count = 0
    total_chars = 0
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line_count += 1
            total_chars += len(line)
            
            # 只显示前5行和后5行
            if line_count <= 5 or line_count > 995:
                print(f"行{line_count}：{line.strip()}")
            elif line_count == 6:
                print("... (省略中间行) ...")
    
    return line_count, total_chars

lines, chars = process_large_file('large_file.txt')
print(f"\n文件统计：{lines}行，{chars}个字符")

# 分块读取文件
print("\n--- 分块读取文件 ---")
def read_in_chunks(filename, chunk_size=1024):
    """
    分块读取文件
    """
    chunk_count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            chunk_count += 1
            print(f"块{chunk_count}：{len(chunk)}个字符")
            if chunk_count >= 3:  # 只显示前3块
                print("... (省略后续块) ...")
                break
    return chunk_count

chunks = read_in_chunks('large_file.txt', 512)
print(f"总共读取了{chunks}块（实际可能更多）")

# ============================================================================
# 8. 实际应用示例
# ============================================================================

print("\n" + "=" * 50)
print("8. 实际应用示例")
print("=" * 50)

def read_config_file(filename):
    """
    读取配置文件
    """
    config = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if line and not line.startswith('#'):
                    if '=' in line:
                        key, value = line.split('=', 1)
                        config[key.strip()] = value.strip()
                    else:
                        print(f"警告：第{line_num}行格式不正确：{line}")
    except FileNotFoundError:
        print(f"配置文件 {filename} 不存在")
    return config

def read_log_file(filename, level='INFO'):
    """
    读取日志文件并过滤级别
    """
    logs = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if level in line:
                    logs.append(line.strip())
    except FileNotFoundError:
        print(f"日志文件 {filename} 不存在")
    return logs

def count_words_in_file(filename):
    """
    统计文件中的单词数
    """
    word_count = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                words = line.strip().split()
                for word in words:
                    # 简单的单词清理
                    word = word.lower().strip('.,!?;:')
                    if word:
                        word_count[word] = word_count.get(word, 0) + 1
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
    return word_count

# 创建示例配置文件
config_content = """# 应用配置文件
app_name=我的应用
version=1.0.0
debug=true
port=8080
# 数据库配置
db_host=localhost
db_port=3306
"""

with open('config.txt', 'w', encoding='utf-8') as f:
    f.write(config_content)

# 创建示例日志文件
log_content = """2024-01-01 10:00:00 INFO 应用启动
2024-01-01 10:01:00 DEBUG 连接数据库
2024-01-01 10:02:00 INFO 用户登录：张三
2024-01-01 10:03:00 ERROR 数据库连接失败
2024-01-01 10:04:00 INFO 重新连接数据库
2024-01-01 10:05:00 WARNING 内存使用率过高
"""

with open('app.log', 'w', encoding='utf-8') as f:
    f.write(log_content)

print("\n--- 应用示例演示 ---")

# 读取配置文件
print("\n读取配置文件：")
config = read_config_file('config.txt')
for key, value in config.items():
    print(f"{key}: {value}")

# 读取日志文件
print("\n读取INFO级别日志：")
info_logs = read_log_file('app.log', 'INFO')
for log in info_logs:
    print(log)

# 统计单词
print("\n统计sample.txt中的单词：")
words = count_words_in_file('sample.txt')
print("单词统计（前10个）：")
for word, count in sorted(words.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"{word}: {count}次")

# ============================================================================
# 9. 练习题
# ============================================================================

print("\n" + "=" * 50)
print("9. 练习题")
print("=" * 50)

print("""
练习题：

1. 基础练习：
   - 编写函数读取文本文件并统计行数、字符数、单词数
   - 创建函数安全读取JSON文件，处理各种异常
   - 实现一个简单的文件搜索功能

2. 进阶练习：
   - 编写CSV文件分析器，计算数值列的统计信息
   - 实现日志文件分析器，提取特定时间段的日志
   - 创建配置文件读取器，支持多种格式

3. 思考题：
   - 什么时候使用read()，什么时候使用readline()？
   - 如何处理超大文件（GB级别）？
   - 文件编码问题如何预防和解决？

4. 挑战练习：
   - 实现一个通用的文件格式检测器
   - 创建支持多种编码的文本文件转换器
   - 编写一个文件内容比较工具
""")

# ============================================================================
# 10. 清理临时文件
# ============================================================================

print("\n" + "=" * 50)
print("10. 清理临时文件")
print("=" * 50)

# 清理演示中创建的文件
temp_files = [
    'sample.txt', 'utf8_file.txt', 'gbk_file.txt', 
    'data.json', 'students.csv', 'large_file.txt',
    'config.txt', 'app.log'
]

print("\n清理临时文件：")
for filename in temp_files:
    try:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"已删除：{filename}")
    except Exception as e:
        print(f"删除 {filename} 时出错：{e}")

# ============================================================================
# 11. 知识点总结
# ============================================================================

print("\n" + "=" * 50)
print("11. 知识点总结")
print("=" * 50)

print("""
知识点总结：

1. 文件打开方式：
   - 使用with语句自动管理文件关闭
   - 指定正确的编码（通常是utf-8）
   - 选择合适的打开模式（r, w, a等）

2. 读取方法选择：
   - read()：读取整个文件（小文件）
   - readline()：逐行读取（需要行处理）
   - 迭代：内存友好的逐行处理（大文件）

3. 异常处理：
   - FileNotFoundError：文件不存在
   - PermissionError：权限不足
   - UnicodeDecodeError：编码问题

4. 编码处理：
   - 优先使用UTF-8编码
   - 了解常见编码（GBK、ASCII等）
   - 使用errors参数处理编码错误

5. 性能优化：
   - 大文件使用迭代读取
   - 分块处理超大文件
   - 及时关闭文件句柄

6. 最佳实践：
   - 始终使用with语句
   - 处理所有可能的异常
   - 选择合适的读取方法
   - 注意文件编码问题
""")

print("\n程序运行完成！")
print("建议：尝试读取不同类型和大小的文件，体验各种读取方法的差异。")
```

## 代码详解

### 1. 文件打开和关闭

**传统方式 vs with语句**：
- 传统方式需要手动调用`close()`方法
- with语句自动管理文件关闭，即使发生异常也会正确关闭
- 推荐始终使用with语句

### 2. 文件读取方法

**不同读取方法的特点**：
- `read()`：一次性读取整个文件，适合小文件
- `read(size)`：读取指定字符数，可控制内存使用
- `readline()`：逐行读取，适合需要行处理的场景
- `readlines()`：读取所有行到列表，适合中等大小文件
- 迭代读取：最内存友好，适合大文件处理

### 3. 文件编码处理

**编码相关要点**：
- UTF-8是推荐的默认编码
- 不同编码需要正确指定encoding参数
- 使用errors参数处理编码错误（ignore、replace、strict）

### 4. 异常处理

**常见异常类型**：
- `FileNotFoundError`：文件不存在
- `PermissionError`：权限不足
- `UnicodeDecodeError`：编码问题
- 建议创建安全的文件读取函数

### 5. 特殊格式文件

**JSON和CSV处理**：
- JSON：使用json模块的load()和dump()方法
- CSV：使用csv模块的reader和writer类
- DictReader可以将CSV行转换为字典

### 6. 大文件处理

**性能优化技巧**：
- 使用迭代读取避免内存溢出
- 分块读取控制内存使用
- 只处理需要的数据，避免全部加载

## 学习要点

### 核心概念
1. **文件句柄管理**：理解文件打开和关闭的重要性
2. **编码处理**：掌握不同编码的处理方法
3. **异常处理**：学会处理各种文件操作异常
4. **性能优化**：了解不同读取方法的性能特点

### 最佳实践
1. **始终使用with语句**：确保文件正确关闭
2. **指定编码**：避免编码问题
3. **异常处理**：处理所有可能的异常情况
4. **选择合适的读取方法**：根据文件大小和需求选择

### 常见陷阱
1. **忘记关闭文件**：可能导致资源泄露
2. **编码问题**：不同编码混用导致乱码
3. **内存溢出**：大文件使用不当的读取方法
4. **异常未处理**：程序崩溃或行为异常

## 实践练习

### 基础练习
1. 创建一个文件统计函数，统计行数、字符数、单词数
2. 实现安全的JSON文件读取函数
3. 编写简单的文件搜索功能

### 进阶练习
1. 创建CSV文件分析器，计算数值列统计信息
2. 实现日志文件分析器，提取特定时间段日志
3. 编写支持多种格式的配置文件读取器

### 挑战练习
1. 实现通用文件格式检测器
2. 创建多编码文本文件转换器
3. 编写文件内容比较工具

## 运行示例

```bash
# 运行完整示例
python 05_file_input.py

# 预期输出包括：
# - 文件打开和关闭演示
# - 各种读取方法的结果
# - 编码处理示例
# - 异常处理演示
# - 文件信息获取
# - JSON和CSV处理
# - 大文件处理技巧
# - 实际应用示例
```

## 扩展思考

1. **什么时候使用不同的读取方法？**
   - 小文件（<1MB）：可以使用read()
   - 中等文件（1MB-100MB）：使用readline()或readlines()
   - 大文件（>100MB）：必须使用迭代读取

2. **如何处理超大文件？**
   - 使用生成器和迭代器
   - 分块处理
   - 考虑使用专门的大数据处理工具

3. **文件编码问题如何预防？**
   - 统一使用UTF-8编码
   - 在文件头部声明编码
   - 使用编码检测工具

## 模块导航

- [上一节：格式化输出](./formatted-output.md)
- [下一节：文件输出](./file-output.md)
- [返回目录](./index.md)