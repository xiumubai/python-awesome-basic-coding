# 文件模式详解

## 学习目标

通过本节学习，你将掌握：
- Python中各种文件打开模式的使用
- 文本模式和二进制模式的区别
- 读写模式的组合使用
- 根据实际需求选择合适的文件模式
- 文件模式对文件指针的影响

## 核心概念

### 文件模式分类

1. **基本文本模式**
   - `'r'`：只读模式（默认）
   - `'w'`：写入模式（覆盖）
   - `'a'`：追加模式
   - `'x'`：独占创建模式

2. **二进制模式**
   - `'rb'`：二进制读取
   - `'wb'`：二进制写入
   - `'ab'`：二进制追加

3. **读写模式**
   - `'r+'`：读写模式（文件必须存在）
   - `'w+'`：读写模式（清空文件）
   - `'a+'`：追加读写模式

## 代码示例

### 1. 基本文本模式

```python
# 'r' 模式 - 只读模式
with open('demo.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"读取内容：{content}")
    # f.write("test")  # 会报错，只读模式不支持写入

# 'w' 模式 - 写入模式（覆盖）
with open('demo.txt', 'w', encoding='utf-8') as f:
    f.write("新内容：覆盖原有内容\n")
    f.write("新内容：第二行\n")
    # content = f.read()  # 会报错，写入模式不支持读取

# 'a' 模式 - 追加模式
with open('demo.txt', 'a', encoding='utf-8') as f:
    f.write("追加内容：第三行\n")
    f.write("追加内容：第四行\n")

# 'x' 模式 - 独占创建模式
try:
    with open('new_file.txt', 'x', encoding='utf-8') as f:
        f.write("独占创建的文件内容\n")
    print("成功创建新文件")
except FileExistsError:
    print("文件已存在，创建失败")
```

### 2. 二进制模式

```python
# 'wb' 模式 - 二进制写入
binary_data = b"\x48\x65\x6c\x6c\x6f"  # "Hello"
numbers = bytes([1, 2, 3, 4, 5, 255])

with open('binary_demo.bin', 'wb') as f:
    f.write(binary_data)
    f.write(b"\n")
    f.write(numbers)

# 'rb' 模式 - 二进制读取
with open('binary_demo.bin', 'rb') as f:
    all_data = f.read()
    print(f"二进制数据：{all_data}")
    
    # 分段读取
    f.seek(0)
    text_part = f.read(5)  # "Hello"
    print(f"文本部分：{text_part.decode('utf-8')}")

# 'ab' 模式 - 二进制追加
with open('binary_demo.bin', 'ab') as f:
    f.write(b"\nAppended data")
```

### 3. 读写模式

```python
# 'r+' 模式 - 读写模式（文件必须存在）
with open('demo.txt', 'r+', encoding='utf-8') as f:
    # 先读取
    content = f.read()
    print(f"原内容：{content}")
    
    # 在末尾写入
    f.write("r+模式追加的内容\n")
    
    # 移动到开头并覆盖
    f.seek(0)
    f.write("修改")

# 'w+' 模式 - 读写模式（清空文件）
with open('demo.txt', 'w+', encoding='utf-8') as f:
    # 写入新内容
    f.write("w+模式的新内容\n第二行\n")
    
    # 移动到开头读取
    f.seek(0)
    content = f.read()
    print(f"新内容：{content}")

# 'a+' 模式 - 追加读写模式
with open('demo.txt', 'a+', encoding='utf-8') as f:
    # 写入内容（总是在末尾）
    f.write("a+模式追加的内容\n")
    
    # 移动到开头读取
    f.seek(0)
    content = f.read()
    print(f"完整内容：{content}")
```

### 4. 模式组合和参数

```python
# 明确指定文本模式
with open('demo.txt', 'wt', encoding='utf-8') as f:
    f.write("明确的文本模式\n")

# 缓冲区参数
with open('demo.bin', 'wb', buffering=0) as f:  # 无缓冲
    f.write(b"Unbuffered write")

with open('demo.txt', 'w', buffering=1, encoding='utf-8') as f:  # 行缓冲
    f.write("Line buffered write\n")

# 编码参数
with open('utf8_demo.txt', 'w', encoding='utf-8') as f:
    f.write("UTF-8编码：你好世界！\n")

with open('gbk_demo.txt', 'w', encoding='gbk') as f:
    f.write("GBK编码：你好世界！\n")
```

### 5. 实际应用场景

```python
from datetime import datetime

# 日志文件追加
def write_log(message, level="INFO"):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('application.log', 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {level}: {message}\n")

write_log("应用程序启动")
write_log("用户登录成功", "INFO")
write_log("数据库连接失败", "ERROR")

# 配置文件读写
config = {
    'database_host': 'localhost',
    'database_port': '5432',
    'debug_mode': 'True'
}

# 写入配置
with open('config.txt', 'w', encoding='utf-8') as f:
    for key, value in config.items():
        f.write(f"{key}={value}\n")

# 读取配置
loaded_config = {}
with open('config.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if '=' in line:
            key, value = line.strip().split('=', 1)
            loaded_config[key] = value

# CSV数据处理
with open('data.csv', 'w', encoding='utf-8') as f:
    f.write("姓名,年龄,城市\n")
    f.write("张三,25,北京\n")
    f.write("李四,30,上海\n")

with open('data.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    headers = lines[0].strip().split(',')
    for line in lines[1:]:
        values = line.strip().split(',')
        record = dict(zip(headers, values))
        print(record)
```

## 重要知识点

### 1. 模式选择指南

| 场景 | 推荐模式 | 说明 |
|------|----------|------|
| 读取现有文件 | `'r'` | 文件必须存在，只能读取 |
| 创建新文件或覆盖 | `'w'` | 清空文件内容，只能写入 |
| 向文件末尾添加 | `'a'` | 保留原内容，在末尾追加 |
| 安全创建新文件 | `'x'` | 文件存在时会失败 |
| 读写现有文件 | `'r+'` | 文件必须存在，可读可写 |
| 创建文件并读写 | `'w+'` | 清空文件，可读可写 |
| 追加并读取 | `'a+'` | 保留内容，末尾追加，可读 |
| 处理二进制数据 | `'rb'/'wb'/'ab'` | 添加'b'后缀 |

### 2. 文件指针行为

- **'r'模式**：指针在文件开头
- **'w'模式**：指针在文件开头（文件被清空）
- **'a'模式**：指针在文件末尾
- **'r+'模式**：指针在文件开头
- **'w+'模式**：指针在文件开头（文件被清空）
- **'a+'模式**：写入时指针在末尾，读取需要手动移动

### 3. 模式决策树

```
需要读取吗？
├─ 是 → 需要写入吗？
│        ├─ 是 → 保留原内容吗？
│        │        ├─ 是 → r+ 或 a+
│        │        └─ 否 → w+
│        └─ 否 → r
└─ 否 → 需要保留原内容吗？
         ├─ 是 → a
         ├─ 否 → w
         └─ 安全创建 → x
```

## 最佳实践

1. **优先使用with语句**
   ```python
   # 推荐
   with open('file.txt', 'r') as f:
       content = f.read()
   
   # 不推荐
   f = open('file.txt', 'r')
   content = f.read()
   f.close()
   ```

2. **明确指定编码**
   ```python
   with open('file.txt', 'r', encoding='utf-8') as f:
       content = f.read()
   ```

3. **根据数据类型选择模式**
   ```python
   # 文本数据
   with open('text.txt', 'r', encoding='utf-8') as f:
       pass
   
   # 二进制数据
   with open('image.jpg', 'rb') as f:
       pass
   ```

4. **谨慎使用'w'模式**
   ```python
   # 确认要覆盖文件时才使用
   if os.path.exists('important.txt'):
       backup = input("文件存在，是否备份？(y/n): ")
       if backup.lower() == 'y':
           shutil.copy('important.txt', 'important.txt.bak')
   
   with open('important.txt', 'w') as f:
       f.write(new_content)
   ```

## 注意事项

1. **'w'模式会清空文件**：使用前确认不会丢失重要数据
2. **'a'模式写入总是在末尾**：即使移动文件指针也无效
3. **'x'模式提供安全创建**：避免意外覆盖现有文件
4. **二进制模式不能指定编码**：encoding参数无效
5. **读写模式需要手动移动指针**：读写操作会改变指针位置

## 练习建议

1. **基础练习**
   - 使用不同模式创建和读取文件
   - 观察各种模式对文件指针的影响
   - 练习二进制文件的读写

2. **进阶练习**
   - 实现一个简单的日志系统
   - 创建配置文件读写工具
   - 处理CSV数据文件

3. **实战练习**
   - 实现文件备份功能
   - 创建文件合并工具
   - 开发简单的文本编辑器

## 下一步学习

掌握文件模式后，建议学习：
- [with语句和上下文管理器](05_with_statement.md)
- [文件指针操作](06_file_pointer.md)
- [二进制文件处理](07_binary_files.md)
- [路径操作](08_path_operations.md)