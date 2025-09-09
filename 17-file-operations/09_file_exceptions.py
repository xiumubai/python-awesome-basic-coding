#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python文件操作 - 文件异常处理

本模块演示文件操作中的异常处理：
1. 常见文件异常类型
2. try-except-finally结构
3. 异常处理最佳实践
4. 自定义异常
5. 日志记录和错误报告
6. 优雅的错误恢复
7. 防御性编程

作者：Python学习助手
日期：2024年
"""

import os
import sys
import logging
import traceback
from pathlib import Path
from typing import Optional, Union, Any
from contextlib import contextmanager


# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('file_operations.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)


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


def demonstrate_common_exceptions():
    """演示常见的文件异常"""
    print("\n=== 常见文件异常演示 ===")
    
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
    
    # 创建一个测试文件并尝试修改权限
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
    
    # 4. OSError - 操作系统相关错误
    print("\n4. OSError - 操作系统相关错误：")
    try:
        # 尝试创建一个名称包含非法字符的文件（在某些系统上）
        illegal_name = 'file\x00name.txt'  # 包含空字符
        with open(illegal_name, 'w') as f:
            f.write('test')
    except OSError as e:
        print(f"捕获异常：{type(e).__name__}")
        print(f"错误信息：{e}")
        print(f"错误代码：{e.errno}")
    
    # 5. UnicodeDecodeError - 编码错误
    print("\n5. UnicodeDecodeError - 编码错误：")
    
    # 创建一个包含非UTF-8内容的文件
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
    
    # 6. IOError - 输入输出错误
    print("\n6. IOError - 输入输出错误：")
    try:
        # 创建一个文件并在写入时关闭
        f = open('io_test.txt', 'w')
        f.close()
        f.write('This will fail')  # 尝试写入已关闭的文件
    except ValueError as e:  # Python 3中IOError通常表现为ValueError
        print(f"捕获异常：{type(e).__name__}")
        print(f"错误信息：{e}")
    finally:
        # 清理
        test_file = Path('io_test.txt')
        if test_file.exists():
            test_file.unlink()


def demonstrate_exception_handling_patterns():
    """演示异常处理模式"""
    print("\n=== 异常处理模式 ===")
    
    # 1. 基本的try-except-finally
    print("\n1. 基本的try-except-finally：")
    
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
    
    # 测试不同情况
    test_cases = [
        __file__,  # 存在的文件
        'nonexistent.txt',  # 不存在的文件
        '.',  # 目录
    ]
    
    for test_file in test_cases:
        print(f"\n测试文件：{test_file}")
        result = safe_file_read(test_file)
        if result:
            print(f"读取成功，前50个字符：{result[:50]}...")
    
    # 2. 多重异常处理
    print("\n2. 多重异常处理：")
    
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
    
    # 测试多重异常处理
    try:
        robust_file_operation('test_robust.txt', 'write')
        content = robust_file_operation('test_robust.txt', 'read')
        print(f"操作成功，内容：{content}")
    except FileOperationError as e:
        print(f"文件操作失败：{e}")
    finally:
        # 清理
        test_file = Path('test_robust.txt')
        if test_file.exists():
            test_file.unlink()
    
    # 3. 异常链和上下文
    print("\n3. 异常链和上下文：")
    
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
    
    try:
        process_config_file('nonexistent_config.txt')
    except FileOperationError as e:
        print(f"捕获异常：{e}")
        print(f"原始异常：{e.__cause__}")
        print(f"异常链：{e.__cause__.__class__.__name__}")


def demonstrate_defensive_programming():
    """演示防御性编程"""
    print("\n=== 防御性编程 ===")
    
    # 1. 输入验证
    print("\n1. 输入验证：")
    
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
    
    # 测试路径验证
    test_paths = [
        'valid_file.txt',
        '',  # 空路径
        'file<with>illegal:chars.txt',  # 非法字符
        '/etc/passwd',  # 敏感目录
        'a' * 300 + '.txt',  # 过长路径
    ]
    
    for test_path in test_paths:
        try:
            validated_path = validate_file_path(test_path)
            print(f"✓ 路径有效：{test_path}")
        except FileValidationError as e:
            print(f"✗ 路径无效：{test_path} - {e}")
    
    # 2. 资源管理
    print("\n2. 资源管理：")
    
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
    
    # 使用安全的文件操作
    try:
        with safe_file_operation('test_safe.txt', 'w') as f:
            f.write('安全的文件操作测试')
        
        with safe_file_operation('test_safe.txt', 'r') as f:
            content = f.read()
            print(f"读取内容：{content}")
    except Exception as e:
        print(f"操作失败：{e}")
    finally:
        # 清理
        test_file = Path('test_safe.txt')
        if test_file.exists():
            test_file.unlink()
    
    # 3. 重试机制
    print("\n3. 重试机制：")
    
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
    
    # 测试重试机制
    try:
        result = unreliable_file_write('retry_test.txt', '重试测试内容')
        print(f"写入成功：{result}")
    except Exception as e:
        print(f"写入最终失败：{e}")
    finally:
        # 清理
        test_file = Path('retry_test.txt')
        if test_file.exists():
            test_file.unlink()


def demonstrate_error_recovery():
    """演示错误恢复策略"""
    print("\n=== 错误恢复策略 ===")
    
    # 1. 备用文件策略
    print("\n1. 备用文件策略：")
    
    def read_config_with_fallback(primary_file: str, fallback_files: list) -> dict:
        """读取配置文件，支持备用文件"""
        all_files = [primary_file] + fallback_files
        
        for i, config_file in enumerate(all_files):
            try:
                with open(config_file, 'r') as f:
                    content = f.read()
                
                # 简单的配置解析（实际应用中可能使用JSON、YAML等）
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
    
    # 创建测试配置文件
    fallback_config = Path('config_fallback.txt')
    fallback_config.write_text('host=backup.example.com\nport=9090\ndebug=true')
    
    try:
        config = read_config_with_fallback(
            'config_primary.txt',  # 不存在的主配置
            ['config_fallback.txt', 'config_default.txt']  # 备用配置
        )
        print(f"最终配置：{config}")
    finally:
        if fallback_config.exists():
            fallback_config.unlink()
    
    # 2. 数据恢复策略
    print("\n2. 数据恢复策略：")
    
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
            
            # 4. 清理备份文件（可选）
            # if backup_path.exists():
            #     backup_path.unlink()
            
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
    
    # 测试数据恢复
    test_data_file = Path('test_data.txt')
    try:
        # 创建初始文件
        test_data_file.write_text('初始数据')
        
        # 安全写入新数据
        safe_data_write(str(test_data_file), '更新后的数据')
        
        # 验证结果
        final_content = test_data_file.read_text()
        print(f"最终文件内容：{final_content}")
        
        # 检查备份文件
        backup_file = test_data_file.with_suffix('.txt.backup')
        if backup_file.exists():
            backup_content = backup_file.read_text()
            print(f"备份文件内容：{backup_content}")
    
    finally:
        # 清理测试文件
        for test_file in [test_data_file, test_data_file.with_suffix('.txt.backup')]:
            if test_file.exists():
                test_file.unlink()


def demonstrate_logging_and_monitoring():
    """演示日志记录和监控"""
    print("\n=== 日志记录和监控 ===")
    
    # 1. 详细的错误日志
    print("\n1. 详细的错误日志：")
    
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
    
    # 测试日志记录
    try:
        # 成功操作
        logged_file_operation('log_test.txt', 'write', content='测试日志记录')
        content = logged_file_operation('log_test.txt', 'read')
        print(f"读取内容：{content}")
        
        # 失败操作
        logged_file_operation('nonexistent.txt', 'read')
        
    except Exception as e:
        print(f"操作失败（已记录日志）：{e}")
    
    finally:
        # 清理
        test_file = Path('log_test.txt')
        if test_file.exists():
            logged_file_operation(str(test_file), 'delete')
    
    # 2. 性能监控
    print("\n2. 性能监控：")
    
    import time
    from functools import wraps
    
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
    
    # 测试性能监控
    try:
        slow_file_operation('performance_test.txt', 5000)
        print("性能测试完成（查看日志文件获取详细信息）")
    except Exception as e:
        print(f"性能测试失败：{e}")
    finally:
        # 清理
        test_file = Path('performance_test.txt')
        if test_file.exists():
            test_file.unlink()


def main():
    """主函数"""
    print("Python文件操作 - 文件异常处理")
    print("=" * 50)
    
    try:
        # 演示各种异常处理技术
        demonstrate_common_exceptions()
        demonstrate_exception_handling_patterns()
        demonstrate_defensive_programming()
        demonstrate_error_recovery()
        demonstrate_logging_and_monitoring()
        
    except Exception as e:
        print(f"\n演示过程中出现错误：{e}")
        logger.error(f"主程序异常：{e}")
        logger.error(f"异常详情:\n{traceback.format_exc()}")
    
    # 学习总结
    print("\n" + "=" * 50)
    print("=== 学习总结 ===")
    print("""
文件异常处理核心概念：
1. 异常类型：了解不同异常的含义和触发条件
2. 异常捕获：使用try-except结构处理异常
3. 资源清理：使用finally或with语句确保资源释放
4. 异常传播：合理地重新抛出或转换异常

常见文件异常：
- FileNotFoundError：文件不存在
- PermissionError：权限不足
- IsADirectoryError：路径是目录而非文件
- OSError：操作系统相关错误
- UnicodeDecodeError：编码解码错误
- IOError/ValueError：输入输出错误

异常处理最佳实践：
1. 具体异常优于通用异常
2. 记录详细的错误信息
3. 提供有意义的错误消息
4. 实现适当的错误恢复
5. 使用异常链保持上下文
6. 避免忽略异常

防御性编程：
1. 输入验证：检查参数的有效性
2. 边界检查：防止越界和溢出
3. 资源管理：确保资源正确释放
4. 重试机制：处理临时性错误
5. 降级策略：提供备用方案

错误恢复策略：
1. 备用文件：使用多个配置源
2. 数据备份：防止数据丢失
3. 原子操作：确保操作的完整性
4. 回滚机制：撤销失败的操作
5. 优雅降级：在部分功能失败时继续运行

日志和监控：
1. 结构化日志：便于分析和搜索
2. 错误上下文：记录足够的调试信息
3. 性能监控：识别性能瓶颈
4. 告警机制：及时发现问题
5. 审计跟踪：记录重要操作

实际应用场景：
- 配置文件加载
- 数据文件处理
- 日志文件管理
- 备份和恢复
- 批量文件操作
- 网络文件传输

关键要点：
- 异常处理不是错误隐藏
- 合理的异常粒度
- 性能和可靠性的平衡
- 用户友好的错误信息
- 系统的可观测性
""")


if __name__ == "__main__":
    main()