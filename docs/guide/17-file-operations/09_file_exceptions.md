# 文件异常处理

## 学习目标

通过本节学习，你将掌握：
- 常见文件操作异常的类型和处理方法
- try-except-finally 异常处理结构
- 自定义异常类的设计和使用
- 防御性编程的最佳实践
- 错误恢复和数据保护策略
- 日志记录和错误监控技术
- 异常处理的性能考虑

## 核心概念

### 异常处理的重要性

文件操作是程序中最容易出错的部分之一，因为它涉及：
- **外部资源**：文件系统状态可能随时变化
- **权限控制**：用户可能没有足够的访问权限
- **硬件限制**：磁盘空间、网络连接等物理限制
- **并发访问**：多个程序可能同时访问同一文件

### 异常处理原则

1. **具体性**：捕获具体的异常类型而非通用异常
2. **完整性**：确保资源得到正确释放
3. **信息性**：提供有用的错误信息
4. **恢复性**：在可能的情况下提供错误恢复机制

## 代码示例

### 1. 常见文件异常类型

```python
import os
from pathlib import Path

def demonstrate_common_exceptions():
    """演示常见的文件异常"""
    print("=== 常见文件异常演示 ===")
    
    # 1. FileNotFoundError - 文件不存在
    print("\n1. FileNotFoundError - 文件不存在：")
    try:
        with open('nonexistent_file.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError as e:
        print(f"捕获异常：{type(e).__name__}")
        print(f"错误信息：{e}")
        print(f"错误代码：{e.errno}")
        print(f"文件名：{e.filename}")
    
    # 2. PermissionError - 权限不足
    print("\n2. PermissionError - 权限不足：")
    test_file = Path('permission_test.txt')
    try:
        # 创建文件
        test_file.write_text('test content')
        
        # 在Unix系统上尝试修改权限
        if os.name != 'nt':  # 非Windows系统
            os.chmod(test_file, 0o000)  # 移除所有权限
            
            try:
                with open(test_file, 'r') as f:
                    content = f.read()
            except PermissionError as e:
                print(f"捕获异常：{type(e).__name__}")
                print(f"错误信息：{e}")
            finally:
                # 恢复权限以便删除
                os.chmod(test_file, 0o644)
        else:
            print("Windows系统，跳过权限测试")
    except Exception as e:
        print(f"权限测试出错：{e}")
    finally:
        # 清理测试文件
        if test_file.exists():
            test_file.unlink()
    
    # 3. IsADirectoryError - 尝试以文件方式打开目录
    print("\n3. IsADirectoryError - 尝试以文件方式打开目录：")
    try:
        with open('.', 'r') as f:
            content = f.read()
    except IsADirectoryError as e:
        print(f"捕获异常：{type(e).__name__}")
        print(f"错误信息：{e}")
    
    # 4. UnicodeDecodeError - 编码错误
    print("\n4. UnicodeDecodeError - 编码错误：")
    binary_file = Path('binary_test.txt')
    try:
        # 写入一些二进制数据
        binary_file.write_bytes(b'\xff\xfe\x00\x48\x00\x65\x00\x6c\x00\x6c\x00\x6f')
        
        # 尝试以UTF-8读取
        try:
            content = binary_file.read_text(encoding='utf-8')
        except UnicodeDecodeError as e:
            print(f"捕获异常：{type(e).__name__}")
            print(f"错误信息：{e}")
            print(f"编码：{e.encoding}")
            print(f"错误位置：{e.start}-{e.end}")
            print(f"原因：{e.reason}")
    finally:
        if binary_file.exists():
            binary_file.unlink()
```

### 2. 异常处理模式

```python
from typing import Optional
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def safe_file_read(filename: str) -> Optional[str]:
    """安全地读取文件"""
    file_handle = None
    try:
        print(f"尝试打开文件：{filename}")
        file_handle = open(filename, 'r', encoding='utf-8')
        content = file_handle.read()
        print(f"成功读取文件，内容长度：{len(content)}")
        return content
    except FileNotFoundError:
        print(f"文件不存在：{filename}")
        return None
    except PermissionError:
        print(f"没有权限访问文件：{filename}")
        return None
    except UnicodeDecodeError as e:
        print(f"文件编码错误：{e}")
        return None
    except Exception as e:
        print(f"读取文件时发生未知错误：{e}")
        return None
    finally:
        if file_handle and not file_handle.closed:
            file_handle.close()
            print("文件已关闭")

# 多重异常处理
def robust_file_operation(filename: str, operation: str = 'read'):
    """健壮的文件操作"""
    try:
        if operation == 'read':
            with open(filename, 'r', encoding='utf-8') as f:
                return f.read()
        elif operation == 'write':
            with open(filename, 'w', encoding='utf-8') as f:
                f.write('Test content')
                return True
    except (FileNotFoundError, IsADirectoryError) as e:
        logger.error(f"文件路径错误：{e}")
        raise FileOperationError(f"文件路径错误", filename, e)
    except (PermissionError, OSError) as e:
        logger.error(f"文件访问错误：{e}")
        raise FileAccessError(f"无法访问文件", filename, e)
    except UnicodeError as e:
        logger.error(f"文件编码错误：{e}")
        raise FileOperationError(f"文件编码错误", filename, e)
    except Exception as e:
        logger.error(f"未知错误：{e}")
        raise FileOperationError(f"未知错误", filename, e)
```

### 3. 自定义异常类

```python
class FileOperationError(Exception):
    """自定义文件操作异常"""
    def __init__(self, message: str, file_path: str = None, original_error: Exception = None):
        self.message = message
        self.file_path = file_path
        self.original_error = original_error
        super().__init__(self.message)
    
    def __str__(self):
        error_msg = self.message
        if self.file_path:
            error_msg += f" (文件: {self.file_path})"
        if self.original_error:
            error_msg += f" (原因: {self.original_error})"
        return error_msg

class FileValidationError(FileOperationError):
    """文件验证异常"""
    pass

class FileAccessError(FileOperationError):
    """文件访问异常"""
    pass

# 异常链和上下文
def process_config_file(filename: str):
    """处理配置文件，演示异常链"""
    try:
        with open(filename, 'r') as f:
            content = f.read()
        
        # 模拟解析错误
        if 'invalid' in content:
            raise ValueError("配置文件格式无效")
        
        return content
    except FileNotFoundError as e:
        # 使用 raise ... from e 创建异常链
        raise FileOperationError("无法加载配置文件") from e
    except ValueError as e:
        # 重新抛出时保持原始异常信息
        raise FileOperationError("配置文件解析失败") from e

# 使用示例
try:
    process_config_file('nonexistent_config.txt')
except FileOperationError as e:
    print(f"捕获异常：{e}")
    print(f"原始异常：{e.__cause__}")
    print(f"异常链：{e.__cause__.__class__.__name__}")
```

### 4. 防御性编程

```python
from pathlib import Path
from typing import Union
from contextlib import contextmanager

def validate_file_path(file_path: Union[str, Path]) -> Path:
    """验证文件路径"""
    if not file_path:
        raise FileValidationError("文件路径不能为空")
    
    path = Path(file_path)
    
    # 检查路径长度
    if len(str(path)) > 260:  # Windows路径长度限制
        raise FileValidationError("文件路径过长")
    
    # 检查非法字符
    illegal_chars = '<>:"|?*'
    if any(char in str(path) for char in illegal_chars):
        raise FileValidationError(f"文件路径包含非法字符：{illegal_chars}")
    
    # 检查是否为绝对路径的安全性
    if path.is_absolute():
        # 检查是否尝试访问系统敏感目录
        sensitive_dirs = ['/etc', '/sys', '/proc', 'C:\\Windows', 'C:\\System32']
        path_str = str(path).lower()
        for sensitive in sensitive_dirs:
            if path_str.startswith(sensitive.lower()):
                raise FileValidationError(f"不允许访问系统目录：{sensitive}")
    
    return path

@contextmanager
def safe_file_operation(filename: str, mode: str = 'r', encoding: str = 'utf-8'):
    """安全的文件操作上下文管理器"""
    file_handle = None
    try:
        # 验证参数
        validate_file_path(filename)
        
        # 记录操作
        logger.info(f"开始文件操作：{filename} (模式: {mode})")
        
        # 打开文件
        file_handle = open(filename, mode, encoding=encoding)
        yield file_handle
        
        logger.info(f"文件操作成功完成：{filename}")
        
    except Exception as e:
        logger.error(f"文件操作失败：{filename} - {e}")
        raise
    finally:
        if file_handle and not file_handle.closed:
            file_handle.close()
            logger.info(f"文件已关闭：{filename}")

# 重试机制
def retry_file_operation(func, max_retries: int = 3, delay: float = 0.1):
    """文件操作重试装饰器"""
    import time
    
    def wrapper(*args, **kwargs):
        last_exception = None
        
        for attempt in range(max_retries + 1):
            try:
                return func(*args, **kwargs)
            except (OSError, IOError) as e:
                last_exception = e
                if attempt < max_retries:
                    logger.warning(f"操作失败，第{attempt + 1}次重试：{e}")
                    time.sleep(delay * (2 ** attempt))  # 指数退避
                else:
                    logger.error(f"操作最终失败，已重试{max_retries}次：{e}")
                    raise
        
        raise last_exception
    
    return wrapper

@retry_file_operation
def unreliable_file_write(filename: str, content: str):
    """模拟不可靠的文件写入操作"""
    import random
    
    # 模拟随机失败
    if random.random() < 0.7:  # 70%的失败率
        raise OSError("模拟的网络或磁盘错误")
    
    with open(filename, 'w') as f:
        f.write(content)
    return True
```

### 5. 错误恢复策略

```python
def read_config_with_fallback(primary_file: str, fallback_files: list) -> dict:
    """读取配置文件，支持备用文件"""
    all_files = [primary_file] + fallback_files
    
    for i, config_file in enumerate(all_files):
        try:
            with open(config_file, 'r') as f:
                content = f.read()
            
            # 简单的配置解析
            config = {}
            for line in content.strip().split('\n'):
                if '=' in line:
                    key, value = line.split('=', 1)
                    config[key.strip()] = value.strip()
            
            file_type = "主配置文件" if i == 0 else f"备用配置文件{i}"
            print(f"成功加载{file_type}：{config_file}")
            return config
            
        except FileNotFoundError:
            print(f"配置文件不存在：{config_file}")
            continue
        except Exception as e:
            print(f"加载配置文件失败：{config_file} - {e}")
            continue
    
    # 所有文件都失败，返回默认配置
    print("所有配置文件都无法加载，使用默认配置")
    return {
        'host': 'localhost',
        'port': '8080',
        'debug': 'false'
    }

def safe_data_write(filename: str, data: str, create_backup: bool = True):
    """安全的数据写入，支持备份和恢复"""
    file_path = Path(filename)
    backup_path = file_path.with_suffix(file_path.suffix + '.backup')
    temp_path = file_path.with_suffix(file_path.suffix + '.tmp')
    
    try:
        # 1. 如果原文件存在且需要备份，先创建备份
        if create_backup and file_path.exists():
            file_path.replace(backup_path)
            print(f"创建备份文件：{backup_path}")
        
        # 2. 先写入临时文件
        with open(temp_path, 'w', encoding='utf-8') as f:
            f.write(data)
            f.flush()  # 确保数据写入磁盘
            os.fsync(f.fileno())  # 强制同步到磁盘
        
        print(f"数据已写入临时文件：{temp_path}")
        
        # 3. 原子性地替换原文件
        temp_path.replace(file_path)
        print(f"成功更新文件：{file_path}")
        
    except Exception as e:
        print(f"写入失败：{e}")
        
        # 恢复备份文件
        if backup_path.exists():
            backup_path.replace(file_path)
            print(f"已从备份恢复：{backup_path} -> {file_path}")
        
        # 清理临时文件
        if temp_path.exists():
            temp_path.unlink()
        
        raise FileOperationError(f"数据写入失败", filename, e)
```

### 6. 日志记录和监控

```python
import traceback
import time
import sys
from functools import wraps

def logged_file_operation(filename: str, operation: str, **kwargs):
    """带日志记录的文件操作"""
    operation_id = id(kwargs)  # 简单的操作ID
    
    logger.info(f"[{operation_id}] 开始文件操作 - 文件: {filename}, 操作: {operation}")
    
    try:
        if operation == 'read':
            with open(filename, 'r', encoding=kwargs.get('encoding', 'utf-8')) as f:
                content = f.read()
            logger.info(f"[{operation_id}] 读取成功 - 大小: {len(content)} 字符")
            return content
        
        elif operation == 'write':
            content = kwargs.get('content', '')
            with open(filename, 'w', encoding=kwargs.get('encoding', 'utf-8')) as f:
                f.write(content)
            logger.info(f"[{operation_id}] 写入成功 - 大小: {len(content)} 字符")
            return True
        
        elif operation == 'delete':
            Path(filename).unlink()
            logger.info(f"[{operation_id}] 删除成功")
            return True
        
        else:
            raise ValueError(f"不支持的操作：{operation}")
    
    except Exception as e:
        # 记录详细的错误信息
        logger.error(f"[{operation_id}] 操作失败 - 错误: {type(e).__name__}: {e}")
        logger.error(f"[{operation_id}] 错误详情:\n{traceback.format_exc()}")
        
        # 记录系统状态
        logger.error(f"[{operation_id}] 系统状态 - 当前目录: {os.getcwd()}")
        logger.error(f"[{operation_id}] 系统状态 - 文件存在: {Path(filename).exists()}")
        
        raise

def monitor_performance(func):
    """性能监控装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_memory = sys.getsizeof(args) + sys.getsizeof(kwargs)
        
        try:
            result = func(*args, **kwargs)
            
            end_time = time.time()
            duration = end_time - start_time
            
            logger.info(f"性能监控 - 函数: {func.__name__}")
            logger.info(f"性能监控 - 执行时间: {duration:.4f}秒")
            logger.info(f"性能监控 - 参数大小: {start_memory}字节")
            
            if duration > 1.0:  # 超过1秒的操作
                logger.warning(f"慢操作警告 - {func.__name__} 耗时 {duration:.4f}秒")
            
            return result
            
        except Exception as e:
            end_time = time.time()
            duration = end_time - start_time
            
            logger.error(f"性能监控 - 函数失败: {func.__name__}")
            logger.error(f"性能监控 - 失败前耗时: {duration:.4f}秒")
            
            raise
    
    return wrapper

@monitor_performance
def slow_file_operation(filename: str, size: int):
    """模拟慢速文件操作"""
    with open(filename, 'w') as f:
        for i in range(size):
            f.write(f"Line {i}\n")
            if i % 1000 == 0:
                time.sleep(0.001)  # 模拟慢速写入
```

## 重要知识点

### 1. 异常层次结构

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- ArithmeticError
      +-- LookupError
      +-- OSError
      |    +-- FileNotFoundError
      |    +-- PermissionError
      |    +-- IsADirectoryError
      |    +-- FileExistsError
      +-- ValueError
      +-- UnicodeError
           +-- UnicodeDecodeError
           +-- UnicodeEncodeError
```

### 2. 异常处理最佳实践

| 原则 | 说明 | 示例 |
|------|------|------|
| 具体异常 | 捕获具体异常而非通用异常 | `except FileNotFoundError:` 而非 `except Exception:` |
| 异常链 | 使用 `raise ... from` 保持异常上下文 | `raise CustomError() from e` |
| 资源清理 | 使用 `finally` 或 `with` 确保资源释放 | `with open() as f:` |
| 有意义的消息 | 提供有用的错误信息 | 包含文件名、操作类型等 |
| 日志记录 | 记录异常详情用于调试 | 使用 `logging` 模块 |

### 3. 错误恢复策略

- **重试机制**：对于临时性错误（网络中断、文件锁定）
- **备用方案**：使用备用文件、默认配置等
- **优雅降级**：部分功能失败时继续运行
- **数据保护**：使用备份、原子操作防止数据丢失

## 最佳实践

### 1. 异常处理结构

```python
# 推荐的异常处理结构
try:
    # 可能出错的代码
    result = risky_operation()
except SpecificError as e:
    # 处理特定异常
    logger.error(f"特定错误：{e}")
    handle_specific_error(e)
except (Error1, Error2) as e:
    # 处理多个相关异常
    logger.error(f"相关错误：{e}")
    handle_related_errors(e)
except Exception as e:
    # 处理未预期的异常
    logger.error(f"未知错误：{e}")
    raise  # 重新抛出
else:
    # 没有异常时执行
    logger.info("操作成功")
finally:
    # 无论是否有异常都执行
    cleanup_resources()
```

### 2. 自定义异常设计

```python
class BaseFileError(Exception):
    """文件操作基础异常"""
    def __init__(self, message, file_path=None, **kwargs):
        super().__init__(message)
        self.file_path = file_path
        self.context = kwargs

class FileValidationError(BaseFileError):
    """文件验证错误"""
    pass

class FileAccessError(BaseFileError):
    """文件访问错误"""
    pass
```

### 3. 日志配置

```python
import logging

# 配置日志格式
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
```

## 注意事项

### 1. 性能考虑

- **异常处理有性能开销**：不要用异常控制正常流程
- **避免过度捕获**：只捕获真正需要处理的异常
- **合理的重试次数**：避免无限重试

### 2. 安全考虑

- **不要泄露敏感信息**：错误消息中避免包含密码、密钥等
- **输入验证**：验证文件路径，防止路径遍历攻击
- **权限检查**：确保有足够权限进行操作

### 3. 用户体验

- **友好的错误消息**：向用户提供可理解的错误信息
- **操作指导**：告诉用户如何解决问题
- **进度反馈**：长时间操作提供进度信息

### 4. 调试和维护

- **详细的日志**：记录足够的上下文信息
- **错误分类**：区分用户错误、系统错误、程序错误
- **监控告警**：对关键错误设置告警机制

## 练习建议

1. **基础练习**：
   - 编写处理各种文件异常的函数
   - 实现自定义异常类
   - 创建带重试机制的文件操作

2. **进阶练习**：
   - 实现文件操作的事务机制
   - 编写文件操作的性能监控工具
   - 创建配置文件管理系统

3. **实际应用**：
   - 日志文件轮转和清理
   - 数据备份和恢复系统
   - 文件同步工具

## 下一步学习

学习完文件异常处理后，建议继续学习：
- 文件操作的综合练习和实际应用
- 并发文件操作和线程安全
- 网络文件操作和分布式文件系统
- 文件系统监控和事件处理

通过掌握文件异常处理，你将能够编写更加健壮、可靠的文件处理程序，有效应对各种异常情况。