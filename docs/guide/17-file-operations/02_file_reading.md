# 文件读取方法

## 学习目标
- 掌握Python中各种文件读取方法
- 理解不同读取方式的优缺点和适用场景
- 学会根据文件大小选择合适的读取方法
- 了解文件指针在读取过程中的变化

## 核心概念

### 文件读取方法概览
Python提供了多种文件读取方法，每种方法都有其特定的使用场景：

1. **read()** - 读取整个文件或指定字符数
2. **readline()** - 逐行读取文件
3. **readlines()** - 读取所有行到列表
4. **文件迭代器** - 逐行遍历文件（推荐）

## 代码示例

### read()方法详解

`read()`方法可以读取整个文件内容或指定数量的字符。

```python
# 读取整个文件
with open('sample.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"文件内容：{content}")

# 读取指定字符数
with open('sample.txt', 'r', encoding='utf-8') as f:
    partial_content = f.read(50)  # 读取前50个字符
    print(f"前50个字符: {partial_content}")
    
    remaining = f.read(50)  # 继续读取接下来的50个字符
    print(f"接下来50个字符: {remaining}")
```

**read()方法特点：**
- 一次性读取，适合小文件
- 可以指定读取字符数
- 文件指针会移动到读取位置之后
- 大文件可能导致内存不足

### readline()方法详解

`readline()`方法每次读取文件的一行内容。

```python
# 逐行读取文件
with open('sample.txt', 'r', encoding='utf-8') as f:
    line_number = 1
    while True:
        line = f.readline()
        if not line:  # 文件结束
            break
        print(f"第{line_number}行: {line.strip()}")
        line_number += 1

# 读取指定长度的行内容
with open('sample.txt', 'r', encoding='utf-8') as f:
    partial_line = f.readline(15)  # 只读取15个字符
    print(f"部分行内容: {partial_line}")
    
    rest_of_line = f.readline()  # 读取该行剩余内容
    print(f"该行剩余内容: {rest_of_line.strip()}")
```

**readline()方法特点：**
- 逐行读取，内存占用小
- 可以控制读取过程
- 适合需要逐行处理的场景
- 需要手动检查文件结束

### readlines()方法详解

`readlines()`方法读取文件的所有行，返回一个列表。

```python
# 读取所有行到列表
with open('sample.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(f"总共读取了 {len(lines)} 行")
    
    # 处理每一行
    for i, line in enumerate(lines, 1):
        print(f"第{i}行: {line.strip()}")

# 对行列表进行统计分析
with open('sample.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
    total_chars = sum(len(line) for line in lines)
    longest_line = max(lines, key=len)
    shortest_line = min(lines, key=len)
    
    print(f"总字符数: {total_chars}")
    print(f"最长行长度: {len(longest_line)}")
    print(f"最短行长度: {len(shortest_line)}")
```

**readlines()方法特点：**
- 一次性读取所有行
- 返回列表，支持随机访问
- 适合需要多次访问行数据的场景
- 大文件可能占用大量内存

### 文件迭代器（推荐方式）

直接迭代文件对象是最Pythonic和内存高效的方式。

```python
# 使用for循环迭代文件
with open('sample.txt', 'r', encoding='utf-8') as f:
    for line_number, line in enumerate(f, 1):
        print(f"第{line_number}行: {line.strip()}")

# 处理大文件的示例
def process_large_file(filename):
    """处理大文件的高效方法"""
    line_count = 0
    word_count = 0
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line_count += 1
            word_count += len(line.split())
    
    return line_count, word_count

# 条件处理
with open('sample.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('重要'):
            print(f"找到重要信息: {line.strip()}")
        elif line.strip() == '':
            print("发现空行")
```

**文件迭代器特点：**
- 内存效率最高
- 代码简洁易读
- 适合处理任意大小的文件
- 自动处理文件结束
- 最推荐的读取方式

### 结合文件指针的读取操作

文件指针控制读取位置，实现随机访问。

```python
with open('sample.txt', 'r', encoding='utf-8') as f:
    # 读取前20个字符
    content1 = f.read(20)
    print(f"前20个字符: {content1}")
    print(f"当前文件指针位置: {f.tell()}")
    
    # 重置文件指针到开头
    f.seek(0)
    print(f"重置后文件指针位置: {f.tell()}")
    
    # 重新读取
    content2 = f.read(20)
    print(f"重新读取: {content2}")
    
    # 移动到第二行开始
    f.seek(0)
    f.readline()  # 跳过第一行
    second_line_pos = f.tell()
    
    content3 = f.read(30)
    print(f"第二行开始的30个字符: {content3}")
    
    # 移动到文件结尾
    f.seek(0, 2)
    print(f"文件大小: {f.tell()} 字节")
```

### 性能对比示例

```python
import time

def compare_reading_methods(filename):
    """比较不同读取方法的性能"""
    
    # 测试read()方法
    start_time = time.time()
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    read_time = time.time() - start_time
    
    # 测试readlines()方法
    start_time = time.time()
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    readlines_time = time.time() - start_time
    
    # 测试文件迭代器
    start_time = time.time()
    line_count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line_count += 1
    iterator_time = time.time() - start_time
    
    print(f"read()方法耗时: {read_time:.4f}秒")
    print(f"readlines()方法耗时: {readlines_time:.4f}秒")
    print(f"文件迭代器耗时: {iterator_time:.4f}秒")
```

## 重要知识点

### 1. 方法选择指南

| 方法 | 适用场景 | 内存使用 | 性能 |
|------|----------|----------|------|
| read() | 小文件，需要全部内容 | 高 | 快 |
| readline() | 需要控制读取过程 | 低 | 中等 |
| readlines() | 需要随机访问行 | 高 | 快 |
| 文件迭代器 | 大文件，逐行处理 | 低 | 快 |

### 2. 文件指针行为
- 每次读取操作都会移动文件指针
- `tell()`方法获取当前指针位置
- `seek()`方法设置指针位置
- 指针位置以字节为单位

### 3. 内存管理
- `read()`和`readlines()`会将内容加载到内存
- 文件迭代器和`readline()`逐行处理，内存占用小
- 处理大文件时优先选择迭代器

## 最佳实践

### 1. 推荐的读取方式
```python
# 最推荐：使用文件迭代器
with open('file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        process_line(line.strip())
```

### 2. 处理不同大小的文件
```python
# 小文件（< 1MB）
with open('small_file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 大文件（> 1MB）
with open('large_file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        process_line(line)
```

### 3. 错误处理
```python
try:
    with open('file.txt', 'r', encoding='utf-8') as f:
        for line in f:
            process_line(line)
except FileNotFoundError:
    print("文件不存在")
except UnicodeDecodeError:
    print("文件编码错误")
```

## 注意事项

1. **编码问题**: 始终指定正确的编码格式
2. **内存使用**: 大文件避免使用`read()`和`readlines()`
3. **文件指针**: 注意指针位置对后续读取的影响
4. **行结束符**: `readline()`保留行结束符，需要使用`strip()`
5. **性能考虑**: 文件迭代器通常是最佳选择

## 练习建议

1. 创建不同大小的测试文件，比较各种读取方法的性能
2. 练习使用文件指针进行随机访问
3. 实现一个文件内容统计工具（行数、字数、字符数）
4. 处理包含中文的文件，注意编码问题
5. 编写处理大文件的程序，观察内存使用情况

## 下一步学习

学习完文件读取方法后，建议继续学习：
- [文件写入方法](./03_file_writing.md)
- [文件打开模式](./04_file_modes.md)
- [with语句使用](./05_with_statement.md)