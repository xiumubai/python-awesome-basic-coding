# with语句和上下文管理器

## 学习目标

通过本节学习，你将掌握：
- with语句的基本用法和工作原理
- 上下文管理器协议的实现
- 多文件同时操作的方法
- 自定义上下文管理器的创建
- with语句中的异常处理机制
- 嵌套with语句的使用技巧

## 核心概念

### 什么是with语句

with语句是Python中用于资源管理的语法结构，它确保资源的正确获取和释放。with语句基于上下文管理器协议，自动调用对象的`__enter__`和`__exit__`方法。

### 上下文管理器协议

上下文管理器必须实现两个特殊方法：
- `__enter__()`：进入with块时调用，返回值赋给as后的变量
- `__exit__(exc_type, exc_value, traceback)`：离开with块时调用，处理清理工作

## 代码示例

### 1. with语句基本用法

```python
# 传统方式（不推荐）
try:
    file = open('example.txt', 'w', encoding='utf-8')
    file.write('传统方式写入文件\n')
    file.write('需要手动关闭文件\n')
finally:
    file.close()  # 必须手动关闭

# with语句方式（推荐）
with open('example.txt', 'w', encoding='utf-8') as file:
    file.write('使用with语句写入文件\n')
    file.write('文件会自动关闭\n')
# 文件自动关闭，无需手动处理

# 验证文件状态
with open('example.txt', 'r', encoding='utf-8') as file:
    print(f"文件是否关闭：{file.closed}")  # False，在with块内是打开的
print(f"离开with块后文件是否关闭：{file.closed}")  # True，自动关闭
```

### 2. 自定义上下文管理器

```python
class FileManager:
    """自定义文件管理器，演示上下文管理器协议"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """进入with块时调用"""
        print(f"__enter__: 打开文件 {self.filename}")
        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        """离开with块时调用"""
        print(f"__exit__: 关闭文件 {self.filename}")
        if self.file:
            self.file.close()
        
        # 处理异常信息
        if exc_type:
            print(f"发生异常: {exc_type.__name__}: {exc_value}")
        return False  # 不抑制异常

# 使用自定义上下文管理器
with FileManager('custom.txt', 'w') as file:
    print("在with块内写入数据")
    file.write('使用自定义上下文管理器\n')
print("离开with块")
```

### 3. 多文件同时操作

```python
# 方式1：嵌套with语句
with open('source.txt', 'r', encoding='utf-8') as source:
    with open('target.txt', 'w', encoding='utf-8') as target:
        content = source.read()
        target.write(content)

# 方式2：单个with语句管理多个文件
with open('source.txt', 'r', encoding='utf-8') as source, \
     open('target.txt', 'w', encoding='utf-8') as target:
    
    for line_num, line in enumerate(source, 1):
        target.write(f"第{line_num}行: {line}")

# 方式3：使用contextlib.ExitStack
from contextlib import ExitStack

filenames = ['file1.txt', 'file2.txt', 'file3.txt']

with ExitStack() as stack:
    files = [stack.enter_context(open(f, 'w', encoding='utf-8')) 
            for f in filenames]
    
    for i, file in enumerate(files):
        file.write(f'这是文件{i+1}的内容\n')
```

### 4. 使用contextlib.contextmanager装饰器

```python
from contextlib import contextmanager
import os

@contextmanager
def file_with_backup(filename, mode='r'):
    """带备份功能的文件上下文管理器"""
    backup_name = f"{filename}.backup"
    
    # 如果是写模式且文件存在，先备份
    if 'w' in mode and os.path.exists(filename):
        print(f"备份原文件: {filename} -> {backup_name}")
        with open(filename, 'r', encoding='utf-8') as original:
            with open(backup_name, 'w', encoding='utf-8') as backup:
                backup.write(original.read())
    
    try:
        print(f"打开文件: {filename}")
        file = open(filename, mode, encoding='utf-8')
        yield file
    except Exception as e:
        print(f"操作失败，恢复备份: {e}")
        if os.path.exists(backup_name):
            os.rename(backup_name, filename)
        raise
    else:
        print(f"操作成功，删除备份")
        if os.path.exists(backup_name):
            os.remove(backup_name)
    finally:
        if 'file' in locals():
            file.close()
            print(f"关闭文件: {filename}")

# 使用带备份功能的上下文管理器
with file_with_backup('important.txt', 'w') as f:
    f.write('修改后的数据\n')
    f.write('新的内容\n')
```

### 5. 异常处理

```python
class SafeFileManager:
    """安全的文件管理器，处理各种异常情况"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        try:
            print(f"尝试打开文件: {self.filename}")
            self.file = open(self.filename, self.mode, encoding='utf-8')
            return self.file
        except FileNotFoundError:
            print(f"文件不存在: {self.filename}")
            raise
        except PermissionError:
            print(f"权限不足: {self.filename}")
            raise
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file and not self.file.closed:
            self.file.close()
            print(f"文件已安全关闭: {self.filename}")
        
        if exc_type:
            print(f"处理异常: {exc_type.__name__}: {exc_value}")
            # 返回True会抑制异常，False会传播异常
            return False

# 使用安全文件管理器
try:
    with SafeFileManager('safe_test.txt', 'w') as f:
        f.write('安全文件操作测试\n')
    print("操作成功完成")
except Exception as e:
    print(f"操作失败: {e}")
```

### 6. 嵌套with语句

```python
import time

# 创建测试数据
test_data = ["第一行数据", "第二行数据", "第三行数据"]

# 嵌套with处理多个相关操作
with open('data_source.txt', 'w', encoding='utf-8') as source:
    # 写入源数据
    for line in test_data:
        source.write(f"{line}\n")
    
    # 在同一个with块中进行相关操作
    with open('data_processed.txt', 'w', encoding='utf-8') as processed:
        with open('data_log.txt', 'w', encoding='utf-8') as log:
            
            log.write(f"处理开始时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            
            for i, line in enumerate(test_data):
                processed_line = f"处理后-{line.upper()}"
                processed.write(f"{processed_line}\n")
                log.write(f"处理第{i+1}行: {line} -> {processed_line}\n")
            
            log.write(f"处理结束时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            log.write(f"总共处理了{len(test_data)}行数据\n")
```

### 7. 实际应用场景

```python
# 日志记录系统
class LogManager:
    def __init__(self, log_file):
        self.log_file = log_file
        self.file = None
    
    def __enter__(self):
        self.file = open(self.log_file, 'a', encoding='utf-8')
        self.file.write(f"\n=== 日志开始 {time.strftime('%Y-%m-%d %H:%M:%S')} ===\n")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.write(f"=== 日志结束 {time.strftime('%Y-%m-%d %H:%M:%S')} ===\n")
        self.file.close()
    
    def log(self, message, level="INFO"):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.file.write(f"[{timestamp}] {level}: {message}\n")
        self.file.flush()  # 立即写入磁盘

# 使用日志管理器
with LogManager('application.log') as logger:
    logger.log("应用程序启动")
    logger.log("用户登录成功", "INFO")
    logger.log("数据库连接失败", "ERROR")
    logger.log("应用程序关闭")

# 数据库连接管理
class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
    
    def __enter__(self):
        print(f"连接数据库: {self.connection_string}")
        # 这里应该是实际的数据库连接代码
        self.connection = f"Connected to {self.connection_string}"
        return self.connection
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("关闭数据库连接")
        self.connection = None

# 使用数据库连接管理器
with DatabaseConnection("postgresql://localhost:5432/mydb") as conn:
    print(f"使用连接: {conn}")
    # 执行数据库操作
```

## 重要知识点

### 1. 上下文管理器协议

- `__enter__(self)`：进入with块时调用，返回值赋给as后的变量
- `__exit__(self, exc_type, exc_value, traceback)`：离开with块时调用
  - `exc_type`：异常类型
  - `exc_value`：异常值
  - `traceback`：异常追踪信息
  - 返回True抑制异常，返回False传播异常

### 2. with语句的执行流程

1. 调用上下文管理器的`__enter__`方法
2. 将`__enter__`的返回值赋给as后的变量
3. 执行with块中的代码
4. 调用上下文管理器的`__exit__`方法
5. 如果with块中发生异常，异常信息传递给`__exit__`方法

### 3. contextlib模块的工具

- `@contextmanager`：装饰器，简化上下文管理器的创建
- `ExitStack`：管理多个上下文管理器
- `closing()`：确保对象的close()方法被调用
- `suppress()`：抑制指定的异常

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

2. **合理处理异常**
   ```python
   def __exit__(self, exc_type, exc_value, traceback):
       # 清理资源
       self.cleanup()
       
       # 记录异常但不抑制
       if exc_type:
           self.log_error(exc_type, exc_value)
       return False  # 不抑制异常
   ```

3. **使用contextlib简化代码**
   ```python
   from contextlib import contextmanager
   
   @contextmanager
   def managed_resource():
       resource = acquire_resource()
       try:
           yield resource
       finally:
           release_resource(resource)
   ```

4. **多个资源的管理**
   ```python
   # 方式1：多个with语句
   with open('file1.txt') as f1, open('file2.txt') as f2:
       # 处理两个文件
       pass
   
   # 方式2：使用ExitStack
   from contextlib import ExitStack
   
   with ExitStack() as stack:
       files = [stack.enter_context(open(f)) for f in filenames]
       # 处理多个文件
   ```

## 注意事项

1. **`__exit__`方法的返回值**
   - 返回True：抑制异常，异常不会传播
   - 返回False或None：异常正常传播

2. **资源清理的重要性**
   - 即使发生异常，`__exit__`方法也会被调用
   - 确保在`__exit__`中进行必要的清理工作

3. **异常处理**
   - `__exit__`方法接收异常信息
   - 可以在此方法中记录或处理异常
   - 谨慎决定是否抑制异常

4. **嵌套使用**
   - 内层异常会传播到外层
   - 每个上下文管理器都会正确清理

## 练习建议

1. **基础练习**
   - 实现一个简单的上下文管理器
   - 使用with语句进行文件操作
   - 观察异常情况下的资源清理

2. **进阶练习**
   - 创建带备份功能的文件管理器
   - 实现数据库连接管理器
   - 使用contextlib.contextmanager装饰器

3. **实战练习**
   - 开发日志记录系统
   - 创建临时目录管理器
   - 实现网络连接管理器

## 下一步学习

掌握with语句后，建议学习：
- [文件指针操作](06_file_pointer.md)
- [二进制文件处理](07_binary_files.md)
- [路径操作](08_path_operations.md)
- [文件异常处理](09_file_exceptions.md)