# 文件写入方法

## 学习目标
- 掌握Python中各种文件写入方法
- 理解不同写入模式的区别和应用场景
- 学会处理写入缓冲区和性能优化
- 掌握格式化写入的技巧

## 核心概念

### 文件写入方法概览
Python提供了两种主要的文件写入方法：

1. **write()** - 写入单个字符串
2. **writelines()** - 写入字符串列表

### 写入模式
- **'w'** - 写入模式（覆盖）
- **'a'** - 追加模式
- **'x'** - 独占创建模式

## 代码示例

### write()方法详解

`write()`方法用于写入字符串到文件，返回写入的字符数。

```python
# 基本写入操作
with open('demo.txt', 'w', encoding='utf-8') as f:
    chars_written = f.write("Hello, Python文件操作！\n")
    print(f"写入了 {chars_written} 个字符")
    
    # 继续写入
    f.write("这是第二行内容\n")
    f.write("这是第三行内容")

# 追加写入
with open('demo.txt', 'a', encoding='utf-8') as f:
    f.write("\n这是追加的第四行")
    f.write("\n这是追加的第五行")

# 读取验证
with open('demo.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"文件内容：\n{content}")
```

**write()方法特点：**
- 写入单个字符串
- 返回实际写入的字符数
- 不会自动添加换行符
- 适合逐步构建文件内容

### writelines()方法详解

`writelines()`方法用于写入字符串列表或可迭代对象。

```python
# 写入字符串列表
lines = [
    "第一行：Python文件写入\n",
    "第二行：writelines()方法\n",
    "第三行：处理多行数据\n",
    "第四行：非常方便\n"
]

with open('demo.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
    print(f"写入了 {len(lines)} 行数据")

# 注意：writelines()不会自动添加换行符
lines_no_newline = ["行1", "行2", "行3", "行4"]

with open('demo.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines_no_newline)  # 结果："行1行2行3行4"

# 正确的方式：手动添加换行符
with open('demo.txt', 'w', encoding='utf-8') as f:
    f.writelines([line + '\n' for line in lines_no_newline])
```

**writelines()方法特点：**
- 接受字符串列表或可迭代对象
- 不会自动添加换行符
- 适合批量写入多行数据
- 性能比多次调用write()更好

### 不同写入模式详解

```python
# 创建初始文件
with open('modes_demo.txt', 'w', encoding='utf-8') as f:
    f.write("初始内容：第一行\n初始内容：第二行\n")

# 'w' 模式：覆盖写入
with open('modes_demo.txt', 'w', encoding='utf-8') as f:
    f.write("覆盖后的新内容\n")  # 原内容被完全覆盖

# 'a' 模式：追加写入
with open('modes_demo.txt', 'a', encoding='utf-8') as f:
    f.write("追加的内容\n")  # 在文件末尾追加

# 'x' 模式：独占创建（文件不存在时创建）
try:
    with open('new_file.txt', 'x', encoding='utf-8') as f:
        f.write("独占创建的文件内容\n")
    print("成功创建新文件")
except FileExistsError:
    print("文件已存在，'x'模式创建失败")
```

**写入模式对比：**

| 模式 | 行为 | 文件不存在 | 文件存在 |
|------|------|------------|----------|
| 'w' | 写入（覆盖） | 创建新文件 | 覆盖原内容 |
| 'a' | 追加写入 | 创建新文件 | 在末尾追加 |
| 'x' | 独占创建 | 创建新文件 | 抛出异常 |

### 格式化写入

```python
from datetime import datetime

# 学生信息数据
data = {
    'name': '张三',
    'age': 25,
    'score': 95.5,
    'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
}

with open('formatted_demo.txt', 'w', encoding='utf-8') as f:
    # 使用format()方法
    f.write("学生信息报告\n")
    f.write("=" * 20 + "\n")
    f.write("姓名：{}\n".format(data['name']))
    f.write("年龄：{}岁\n".format(data['age']))
    f.write("成绩：{:.1f}分\n".format(data['score']))
    
    # 使用f-string（推荐）
    f.write("\n--- 使用f-string格式化 ---\n")
    f.write(f"学生{data['name']}今年{data['age']}岁，")
    f.write(f"考试成绩为{data['score']:.1f}分\n")

# 写入表格数据
students = [
    {'name': '张三', 'math': 95, 'english': 87, 'science': 92},
    {'name': '李四', 'math': 88, 'english': 94, 'science': 89},
    {'name': '王五', 'math': 92, 'english': 91, 'science': 95}
]

with open('table_demo.txt', 'w', encoding='utf-8') as f:
    # 写入表头
    f.write(f"{'姓名':<8} {'数学':<6} {'英语':<6} {'科学':<6} {'平均分':<8}\n")
    f.write("-" * 40 + "\n")
    
    # 写入数据行
    for student in students:
        avg = (student['math'] + student['english'] + student['science']) / 3
        f.write(f"{student['name']:<8} {student['math']:<6} "
                f"{student['english']:<6} {student['science']:<6} {avg:<8.1f}\n")
```

### 缓冲区和刷新操作

```python
import time
from datetime import datetime

# 缓冲区写入演示
with open('buffer_demo.txt', 'w', encoding='utf-8') as f:
    f.write("第一行数据\n")
    print("已写入第一行，但可能还在缓冲区中")
    
    # 手动刷新缓冲区
    f.flush()
    print("已刷新缓冲区，数据确保写入磁盘")
    
    f.write("第二行数据\n")
    time.sleep(3)
    
    f.write("第三行数据\n")
    print("文件关闭时会自动刷新")

# 实时写入日志
with open('realtime_log.txt', 'w', encoding='utf-8') as f:
    for i in range(5):
        timestamp = datetime.now().strftime('%H:%M:%S')
        log_entry = f"[{timestamp}] 处理任务 {i+1}\n"
        f.write(log_entry)
        f.flush()  # 立即刷新，确保实时写入
        print(f"写入日志：{log_entry.strip()}")
        time.sleep(1)
```

**缓冲区重要概念：**
- 写入操作通常先存储在内存缓冲区中
- `flush()`方法强制将缓冲区内容写入磁盘
- 文件关闭时会自动刷新缓冲区
- 实时日志需要及时刷新

### 写入性能对比

```python
import time

# 准备测试数据
lines = [f"这是第{i+1}行测试数据\n" for i in range(10000)]

# 方法1：逐行写入
start_time = time.time()
with open('test1.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        f.write(line)
time1 = time.time() - start_time

# 方法2：批量写入（writelines）
start_time = time.time()
with open('test2.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
time2 = time.time() - start_time

# 方法3：拼接后一次写入
start_time = time.time()
content = ''.join(lines)
with open('test3.txt', 'w', encoding='utf-8') as f:
    f.write(content)
time3 = time.time() - start_time

print(f"逐行写入耗时: {time1:.4f}秒")
print(f"批量写入耗时: {time2:.4f}秒")
print(f"拼接写入耗时: {time3:.4f}秒")
```

## 重要知识点

### 1. 方法选择指南

| 场景 | 推荐方法 | 原因 |
|------|----------|------|
| 单行写入 | write() | 简单直接 |
| 多行写入 | writelines() | 性能更好 |
| 大量数据 | 拼接后write() | 最高性能 |
| 实时日志 | write() + flush() | 确保及时写入 |

### 2. 写入模式选择
- **新建文件**：使用'w'模式
- **追加内容**：使用'a'模式
- **安全创建**：使用'x'模式（避免覆盖）

### 3. 性能优化要点
- 批量操作比逐个操作快
- 减少磁盘I/O次数
- 合理使用缓冲区
- 大文件考虑分块处理

## 最佳实践

### 1. 推荐的写入方式
```python
# 单行写入
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write("单行内容\n")

# 多行写入（推荐）
lines = ["第一行\n", "第二行\n", "第三行\n"]
with open('file.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)

# 格式化写入（推荐f-string）
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write(f"用户{name}的分数是{score:.1f}\n")
```

### 2. 错误处理
```python
try:
    with open('file.txt', 'w', encoding='utf-8') as f:
        f.write("内容")
except PermissionError:
    print("没有写入权限")
except OSError as e:
    print(f"写入错误：{e}")
```

### 3. 大文件写入
```python
# 分块写入大量数据
def write_large_data(filename, data_generator):
    with open(filename, 'w', encoding='utf-8') as f:
        buffer = []
        for item in data_generator:
            buffer.append(str(item) + '\n')
            if len(buffer) >= 1000:  # 每1000行写入一次
                f.writelines(buffer)
                buffer = []
        if buffer:  # 写入剩余数据
            f.writelines(buffer)
```

## 注意事项

1. **换行符处理**: `writelines()`不会自动添加换行符
2. **编码问题**: 始终指定正确的编码格式
3. **缓冲区**: 重要数据及时调用`flush()`
4. **文件模式**: 选择正确的模式避免数据丢失
5. **性能考虑**: 大量数据使用批量写入
6. **资源管理**: 使用`with`语句确保文件正确关闭

## 练习建议

1. 实现一个日志记录器，支持不同级别的日志写入
2. 编写程序将CSV数据格式化写入文本文件
3. 创建一个文件备份工具，支持增量写入
4. 比较不同写入方法的性能差异
5. 实现一个配置文件生成器

## 下一步学习

学习完文件写入方法后，建议继续学习：
- [文件打开模式](./04_file_modes.md)
- [with语句使用](./05_with_statement.md)
- [文件指针操作](./06_file_pointer.md)