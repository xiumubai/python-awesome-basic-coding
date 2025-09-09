#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
异常日志记录

本文件详细演示Python中异常日志记录的方法和最佳实践，包括日志配置、
异常信息的记录、日志格式化、日志轮转、结构化日志等高级技术。

学习目标：
1. 掌握Python logging模块的使用
2. 学会记录异常信息和堆栈跟踪
3. 了解不同的日志级别和格式
4. 掌握结构化日志记录
5. 学会在生产环境中配置日志
"""

import sys
import os
import logging
import logging.handlers
import traceback
import json
import time
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Union
from pathlib import Path
import functools
from contextlib import contextmanager
import threading
from dataclasses import dataclass, asdict
from enum import Enum


def print_section(title: str) -> None:
    """打印章节标题"""
    print("\n" + "=" * 60)
    print(f"{title}")
    print("=" * 60)


def demonstrate_basic_logging():
    """演示基本的日志记录"""
    print_section("1. 基本日志记录")
    
    print("Python logging模块的核心概念：")
    print("- Logger: 日志记录器，应用程序的接口")
    print("- Handler: 处理器，决定日志输出位置")
    print("- Formatter: 格式化器，决定日志格式")
    print("- Filter: 过滤器，决定哪些日志被处理")
    
    # 基本日志配置
    def setup_basic_logging():
        """设置基本日志配置"""
        print("\n--- 基本日志配置 ---")
        
        # 创建日志目录
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        # 配置日志格式
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        
        # 基本配置
        logging.basicConfig(
            level=logging.DEBUG,
            format=log_format,
            handlers=[
                logging.FileHandler(log_dir / "basic.log", encoding='utf-8'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        logger = logging.getLogger("basic_example")
        
        # 测试不同级别的日志
        logger.debug("这是调试信息")
        logger.info("这是信息日志")
        logger.warning("这是警告信息")
        logger.error("这是错误信息")
        logger.critical("这是严重错误")
        
        print("✓ 基本日志记录完成")
        return logger
    
    def demonstrate_exception_logging(logger):
        """演示异常日志记录"""
        print("\n--- 异常日志记录 ---")
        
        def risky_function(x: int, y: int) -> float:
            """可能出错的函数"""
            if y == 0:
                raise ZeroDivisionError("除数不能为零")
            if x < 0:
                raise ValueError("x不能为负数")
            return x / y
        
        # 方法1：使用exception()记录异常
        print("方法1: 使用logger.exception()")
        try:
            result = risky_function(10, 0)
        except Exception as e:
            logger.exception("计算过程中发生异常")
            print(f"捕获异常: {e}")
        
        # 方法2：使用error()和exc_info参数
        print("\n方法2: 使用logger.error(exc_info=True)")
        try:
            result = risky_function(-5, 2)
        except Exception as e:
            logger.error("计算失败: %s", e, exc_info=True)
            print(f"捕获异常: {e}")
        
        # 方法3：手动记录异常信息
        print("\n方法3: 手动记录异常信息")
        try:
            result = risky_function(10, 0)
        except Exception as e:
            tb_str = traceback.format_exc()
            logger.error("异常详情:\n%s", tb_str)
            print(f"捕获异常: {e}")
        
        # 方法4：记录异常链
        print("\n方法4: 记录异常链")
        try:
            try:
                result = risky_function(10, 0)
            except ZeroDivisionError as e:
                raise RuntimeError("计算模块错误") from e
        except Exception as e:
            logger.exception("发生异常链")
            
            # 手动分析异常链
            chain_info = []
            current = e
            while current:
                chain_info.append(f"{type(current).__name__}: {current}")
                current = current.__cause__ or current.__context__
            
            logger.info("异常链: %s", " -> ".join(chain_info))
            print(f"捕获异常链: {' -> '.join(chain_info)}")
    
    logger = setup_basic_logging()
    demonstrate_exception_logging(logger)


def demonstrate_advanced_logging_configuration():
    """演示高级日志配置"""
    print_section("2. 高级日志配置")
    
    print("高级日志配置特性：")
    print("- 多个处理器和格式化器")
    print("- 日志轮转和压缩")
    print("- 过滤器和自定义处理")
    print("- 异步日志记录")
    
    class ColoredFormatter(logging.Formatter):
        """彩色日志格式化器"""
        
        # ANSI颜色代码
        COLORS = {
            'DEBUG': '\033[36m',      # 青色
            'INFO': '\033[32m',       # 绿色
            'WARNING': '\033[33m',    # 黄色
            'ERROR': '\033[31m',      # 红色
            'CRITICAL': '\033[35m',   # 紫色
            'RESET': '\033[0m'        # 重置
        }
        
        def format(self, record):
            # 添加颜色
            if record.levelname in self.COLORS:
                record.levelname = (f"{self.COLORS[record.levelname]}"
                                  f"{record.levelname}"
                                  f"{self.COLORS['RESET']}")
            
            return super().format(record)
    
    class ExceptionFilter(logging.Filter):
        """异常过滤器"""
        
        def filter(self, record):
            # 只记录包含异常信息的日志
            return record.exc_info is not None or 'exception' in record.getMessage().lower()
    
    def setup_advanced_logging():
        """设置高级日志配置"""
        print("\n--- 高级日志配置 ---")
        
        # 创建日志目录
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        # 创建logger
        logger = logging.getLogger("advanced_example")
        logger.setLevel(logging.DEBUG)
        
        # 清除现有处理器
        logger.handlers.clear()
        
        # 1. 控制台处理器（彩色输出）
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_formatter = ColoredFormatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
        
        # 2. 文件处理器（详细日志）
        file_handler = logging.FileHandler(
            log_dir / "detailed.log", 
            encoding='utf-8'
        )
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        
        # 3. 轮转文件处理器
        rotating_handler = logging.handlers.RotatingFileHandler(
            log_dir / "rotating.log",
            maxBytes=1024*1024,  # 1MB
            backupCount=5,
            encoding='utf-8'
        )
        rotating_handler.setLevel(logging.WARNING)
        rotating_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        rotating_handler.setFormatter(rotating_formatter)
        logger.addHandler(rotating_handler)
        
        # 4. 时间轮转处理器
        timed_handler = logging.handlers.TimedRotatingFileHandler(
            log_dir / "timed.log",
            when='midnight',
            interval=1,
            backupCount=7,
            encoding='utf-8'
        )
        timed_handler.setLevel(logging.ERROR)
        timed_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        timed_handler.setFormatter(timed_formatter)
        logger.addHandler(timed_handler)
        
        # 5. 异常专用处理器（带过滤器）
        exception_handler = logging.FileHandler(
            log_dir / "exceptions.log",
            encoding='utf-8'
        )
        exception_handler.setLevel(logging.ERROR)
        exception_handler.addFilter(ExceptionFilter())
        exception_formatter = logging.Formatter(
            '%(asctime)s - EXCEPTION - %(name)s - %(message)s\n%(exc_text)s'
        )
        exception_handler.setFormatter(exception_formatter)
        logger.addHandler(exception_handler)
        
        print("✓ 高级日志配置完成")
        return logger
    
    def test_advanced_logging(logger):
        """测试高级日志配置"""
        print("\n--- 测试高级日志配置 ---")
        
        # 测试不同级别的日志
        logger.debug("调试信息 - 只在文件中记录")
        logger.info("信息日志 - 控制台和文件")
        logger.warning("警告信息 - 所有处理器")
        logger.error("错误信息 - 所有处理器")
        
        # 测试异常记录
        try:
            raise ValueError("测试异常")
        except Exception:
            logger.exception("这是一个测试异常")
        
        # 测试大量日志（触发轮转）
        for i in range(10):
            logger.warning(f"批量日志测试 {i+1}/10")
        
        print("✓ 高级日志测试完成")
    
    logger = setup_advanced_logging()
    test_advanced_logging(logger)


def demonstrate_structured_logging():
    """演示结构化日志记录"""
    print_section("3. 结构化日志记录")
    
    print("结构化日志的优势：")
    print("- 便于日志分析和搜索")
    print("- 支持自动化处理")
    print("- 提供丰富的上下文信息")
    print("- 便于集成监控系统")
    
    class LogLevel(Enum):
        """日志级别枚举"""
        DEBUG = "DEBUG"
        INFO = "INFO"
        WARNING = "WARNING"
        ERROR = "ERROR"
        CRITICAL = "CRITICAL"
    
    @dataclass
    class LogContext:
        """日志上下文"""
        user_id: Optional[str] = None
        session_id: Optional[str] = None
        request_id: Optional[str] = None
        operation: Optional[str] = None
        module: Optional[str] = None
        
        def to_dict(self) -> Dict[str, Any]:
            return {k: v for k, v in asdict(self).items() if v is not None}
    
    class StructuredLogger:
        """结构化日志记录器"""
        
        def __init__(self, name: str, log_file: Optional[str] = None):
            self.logger = logging.getLogger(name)
            self.context = LogContext()
            
            if not self.logger.handlers:
                self._setup_handlers(log_file)
        
        def _setup_handlers(self, log_file: Optional[str]):
            """设置处理器"""
            # JSON格式化器
            json_formatter = logging.Formatter(
                '%(message)s'  # 只输出消息，因为我们会格式化为JSON
            )
            
            # 控制台处理器
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(json_formatter)
            self.logger.addHandler(console_handler)
            
            # 文件处理器
            if log_file:
                file_handler = logging.FileHandler(log_file, encoding='utf-8')
                file_handler.setFormatter(json_formatter)
                self.logger.addHandler(file_handler)
            
            self.logger.setLevel(logging.DEBUG)
        
        def set_context(self, **kwargs):
            """设置日志上下文"""
            for key, value in kwargs.items():
                if hasattr(self.context, key):
                    setattr(self.context, key, value)
        
        def _log(self, level: LogLevel, message: str, **extra_data):
            """记录结构化日志"""
            log_entry = {
                'timestamp': datetime.now(timezone.utc).isoformat(),
                'level': level.value,
                'message': message,
                'context': self.context.to_dict(),
                **extra_data
            }
            
            # 添加异常信息
            exc_info = extra_data.get('exc_info')
            if exc_info:
                log_entry['exception'] = {
                    'type': exc_info[0].__name__ if exc_info[0] else None,
                    'message': str(exc_info[1]) if exc_info[1] else None,
                    'traceback': traceback.format_exception(*exc_info) if exc_info[2] else None
                }
            
            # 输出JSON格式的日志
            json_message = json.dumps(log_entry, ensure_ascii=False, default=str)
            
            # 根据级别调用相应的logger方法
            getattr(self.logger, level.value.lower())(json_message)
        
        def debug(self, message: str, **extra_data):
            self._log(LogLevel.DEBUG, message, **extra_data)
        
        def info(self, message: str, **extra_data):
            self._log(LogLevel.INFO, message, **extra_data)
        
        def warning(self, message: str, **extra_data):
            self._log(LogLevel.WARNING, message, **extra_data)
        
        def error(self, message: str, **extra_data):
            self._log(LogLevel.ERROR, message, **extra_data)
        
        def critical(self, message: str, **extra_data):
            self._log(LogLevel.CRITICAL, message, **extra_data)
        
        def exception(self, message: str, **extra_data):
            """记录异常信息"""
            extra_data['exc_info'] = sys.exc_info()
            self._log(LogLevel.ERROR, message, **extra_data)
    
    def test_structured_logging():
        """测试结构化日志记录"""
        print("\n--- 测试结构化日志记录 ---")
        
        # 创建日志目录
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        # 创建结构化日志记录器
        logger = StructuredLogger(
            "structured_example",
            log_dir / "structured.log"
        )
        
        # 设置上下文
        logger.set_context(
            user_id="user_123",
            session_id="session_456",
            request_id="req_789",
            module="user_service"
        )
        
        # 记录不同类型的日志
        logger.info("用户登录", 
                   operation="login",
                   ip_address="192.168.1.100",
                   user_agent="Mozilla/5.0")
        
        logger.warning("登录尝试失败",
                      operation="login",
                      reason="invalid_password",
                      attempts=3)
        
        # 记录业务操作
        logger.info("订单创建",
                   operation="create_order",
                   order_id="order_001",
                   amount=99.99,
                   currency="USD")
        
        # 记录异常
        try:
            # 模拟异常
            result = 10 / 0
        except Exception:
            logger.exception("订单处理失败",
                           operation="process_order",
                           order_id="order_001",
                           error_code="DIVISION_ERROR")
        
        # 记录性能指标
        logger.info("API响应时间",
                   operation="get_user_profile",
                   response_time_ms=150,
                   status_code=200,
                   cache_hit=True)
        
        print("✓ 结构化日志记录完成")
    
    test_structured_logging()


def demonstrate_logging_decorators():
    """演示日志装饰器"""
    print_section("4. 日志装饰器")
    
    print("日志装饰器的用途：")
    print("- 自动记录函数调用")
    print("- 记录函数参数和返回值")
    print("- 记录函数执行时间")
    print("- 自动异常记录")
    
    def log_function_calls(logger_name: str = None, 
                          log_args: bool = True, 
                          log_result: bool = True,
                          log_time: bool = True):
        """函数调用日志装饰器"""
        def decorator(func):
            logger = logging.getLogger(logger_name or func.__module__)
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                func_name = f"{func.__module__}.{func.__name__}"
                
                # 记录函数开始
                start_time = time.time()
                
                log_data = {'function': func_name}
                if log_args:
                    log_data['function_args'] = args
                    log_data['function_kwargs'] = kwargs
                
                logger.info(f"开始执行函数: {func_name}", extra=log_data)
                
                try:
                    result = func(*args, **kwargs)
                    
                    # 记录成功结果
                    end_time = time.time()
                    execution_time = end_time - start_time
                    
                    success_data = {'function': func_name, 'status': 'success'}
                    if log_result:
                        success_data['result'] = result
                    if log_time:
                        success_data['execution_time'] = execution_time
                    
                    logger.info(f"函数执行成功: {func_name}", extra=success_data)
                    return result
                    
                except Exception as e:
                    # 记录异常
                    end_time = time.time()
                    execution_time = end_time - start_time
                    
                    error_data = {
                        'function': func_name,
                        'status': 'error',
                        'error_type': type(e).__name__,
                        'error_message': str(e),
                        'execution_time': execution_time
                    }
                    
                    logger.exception(f"函数执行失败: {func_name}", extra=error_data)
                    raise
            
            return wrapper
        return decorator
    
    def log_exceptions(logger_name: str = None, reraise: bool = True):
        """异常日志装饰器"""
        def decorator(func):
            logger = logging.getLogger(logger_name or func.__module__)
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    func_name = f"{func.__module__}.{func.__name__}"
                    
                    error_data = {
                        'function': func_name,
                        'error_type': type(e).__name__,
                        'error_message': str(e),
                        'function_args': args,
                        'function_kwargs': kwargs
                    }
                    
                    logger.exception(f"函数 {func_name} 发生异常", extra=error_data)
                    
                    if reraise:
                        raise
                    return None
            
            return wrapper
        return decorator
    
    @contextmanager
    def log_context(logger_name: str, operation: str, **context_data):
        """日志上下文管理器"""
        logger = logging.getLogger(logger_name)
        
        start_time = time.time()
        logger.info(f"开始操作: {operation}", extra={'operation': operation, **context_data})
        
        try:
            yield logger
            
            end_time = time.time()
            execution_time = end_time - start_time
            
            logger.info(f"操作完成: {operation}", extra={
                'operation': operation,
                'status': 'success',
                'execution_time': execution_time,
                **context_data
            })
            
        except Exception as e:
            end_time = time.time()
            execution_time = end_time - start_time
            
            logger.exception(f"操作失败: {operation}", extra={
                'operation': operation,
                'status': 'error',
                'error_type': type(e).__name__,
                'error_message': str(e),
                'execution_time': execution_time,
                **context_data
            })
            raise
    
    def test_logging_decorators():
        """测试日志装饰器"""
        print("\n--- 测试日志装饰器 ---")
        
        # 设置日志
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_dir / "decorators.log", encoding='utf-8'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        # 测试函数调用装饰器
        @log_function_calls("test_logger", log_args=True, log_result=True, log_time=True)
        def calculate_factorial(n: int) -> int:
            """计算阶乘"""
            if n < 0:
                raise ValueError("n必须为非负整数")
            if n <= 1:
                return 1
            return n * calculate_factorial(n - 1)
        
        @log_exceptions("test_logger")
        def divide_numbers(a: float, b: float) -> float:
            """除法运算"""
            return a / b
        
        # 测试正常执行
        print("\n1. 测试正常函数执行:")
        result = calculate_factorial(5)
        print(f"5! = {result}")
        
        # 测试异常情况
        print("\n2. 测试异常记录:")
        try:
            calculate_factorial(-1)
        except ValueError as e:
            print(f"捕获异常: {e}")
        
        # 测试除零异常
        print("\n3. 测试除零异常:")
        try:
            divide_numbers(10, 0)
        except ZeroDivisionError as e:
            print(f"捕获异常: {e}")
        
        # 测试上下文管理器
        print("\n4. 测试日志上下文管理器:")
        with log_context("test_logger", "数据处理", batch_id="batch_001", record_count=1000):
            time.sleep(0.1)  # 模拟处理时间
            print("数据处理完成")
        
        # 测试上下文管理器异常
        print("\n5. 测试上下文管理器异常:")
        try:
            with log_context("test_logger", "错误处理", operation_id="op_002"):
                raise RuntimeError("模拟处理错误")
        except RuntimeError as e:
            print(f"捕获异常: {e}")
        
        print("✓ 日志装饰器测试完成")
    
    test_logging_decorators()


def demonstrate_production_logging():
    """演示生产环境日志配置"""
    print_section("5. 生产环境日志配置")
    
    print("生产环境日志要求：")
    print("- 高性能和低延迟")
    print("- 日志轮转和归档")
    print("- 安全性和隐私保护")
    print("- 监控和告警集成")
    
    class ProductionLogConfig:
        """生产环境日志配置"""
        
        def __init__(self, app_name: str, log_dir: str = "logs", 
                     log_level: str = "INFO", max_bytes: int = 100*1024*1024,
                     backup_count: int = 10):
            self.app_name = app_name
            self.log_dir = Path(log_dir)
            self.log_level = getattr(logging, log_level.upper())
            self.max_bytes = max_bytes
            self.backup_count = backup_count
            
            # 创建日志目录
            self.log_dir.mkdir(exist_ok=True)
        
        def setup_logging(self) -> logging.Logger:
            """设置生产环境日志"""
            # 创建根logger
            logger = logging.getLogger(self.app_name)
            logger.setLevel(self.log_level)
            
            # 清除现有处理器
            logger.handlers.clear()
            
            # 1. 应用日志（轮转）
            app_handler = logging.handlers.RotatingFileHandler(
                self.log_dir / f"{self.app_name}.log",
                maxBytes=self.max_bytes,
                backupCount=self.backup_count,
                encoding='utf-8'
            )
            app_handler.setLevel(logging.INFO)
            app_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(process)d - %(thread)d - %(message)s'
            )
            app_handler.setFormatter(app_formatter)
            logger.addHandler(app_handler)
            
            # 2. 错误日志（单独文件）
            error_handler = logging.handlers.RotatingFileHandler(
                self.log_dir / f"{self.app_name}_error.log",
                maxBytes=self.max_bytes // 10,
                backupCount=self.backup_count,
                encoding='utf-8'
            )
            error_handler.setLevel(logging.ERROR)
            error_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s\n%(exc_text)s'
            )
            error_handler.setFormatter(error_formatter)
            logger.addHandler(error_handler)
            
            # 3. 审计日志（时间轮转）
            audit_handler = logging.handlers.TimedRotatingFileHandler(
                self.log_dir / f"{self.app_name}_audit.log",
                when='midnight',
                interval=1,
                backupCount=30,
                encoding='utf-8'
            )
            audit_handler.setLevel(logging.WARNING)
            audit_formatter = logging.Formatter(
                '%(asctime)s - AUDIT - %(message)s'
            )
            audit_handler.setFormatter(audit_formatter)
            
            # 添加审计过滤器
            class AuditFilter(logging.Filter):
                def filter(self, record):
                    return hasattr(record, 'audit') and record.audit
            
            audit_handler.addFilter(AuditFilter())
            logger.addHandler(audit_handler)
            
            # 4. 性能日志
            perf_handler = logging.FileHandler(
                self.log_dir / f"{self.app_name}_performance.log",
                encoding='utf-8'
            )
            perf_handler.setLevel(logging.INFO)
            perf_formatter = logging.Formatter(
                '%(asctime)s - PERF - %(message)s'
            )
            perf_handler.setFormatter(perf_formatter)
            
            # 添加性能过滤器
            class PerformanceFilter(logging.Filter):
                def filter(self, record):
                    return hasattr(record, 'performance') and record.performance
            
            perf_handler.addFilter(PerformanceFilter())
            logger.addHandler(perf_handler)
            
            return logger
    
    class SecureLogger:
        """安全日志记录器"""
        
        def __init__(self, logger: logging.Logger):
            self.logger = logger
            self.sensitive_fields = {
                'password', 'token', 'secret', 'key', 'credential',
                'ssn', 'credit_card', 'phone', 'email'
            }
        
        def _sanitize_data(self, data: Any) -> Any:
            """清理敏感数据"""
            if isinstance(data, dict):
                sanitized = {}
                for key, value in data.items():
                    if any(sensitive in key.lower() for sensitive in self.sensitive_fields):
                        sanitized[key] = "***REDACTED***"
                    else:
                        sanitized[key] = self._sanitize_data(value)
                return sanitized
            elif isinstance(data, (list, tuple)):
                return [self._sanitize_data(item) for item in data]
            elif isinstance(data, str):
                # 简单的敏感信息检测
                if len(data) > 10 and any(char.isdigit() for char in data):
                    # 可能是敏感数据，部分遮蔽
                    return data[:3] + "***" + data[-3:] if len(data) > 6 else "***"
                return data
            else:
                return data
        
        def log_user_action(self, user_id: str, action: str, **context):
            """记录用户操作（审计日志）"""
            sanitized_context = self._sanitize_data(context)
            self.logger.warning(
                f"用户操作: {action}",
                extra={
                    'audit': True,
                    'user_id': user_id,
                    'action': action,
                    'context': sanitized_context,
                    'timestamp': datetime.now(timezone.utc).isoformat()
                }
            )
        
        def log_performance(self, operation: str, duration: float, **metrics):
            """记录性能指标"""
            self.logger.info(
                f"性能指标: {operation}",
                extra={
                    'performance': True,
                    'operation': operation,
                    'duration': duration,
                    'metrics': metrics,
                    'timestamp': datetime.now(timezone.utc).isoformat()
                }
            )
        
        def log_security_event(self, event_type: str, severity: str, **details):
            """记录安全事件"""
            sanitized_details = self._sanitize_data(details)
            self.logger.error(
                f"安全事件: {event_type}",
                extra={
                    'audit': True,
                    'security_event': True,
                    'event_type': event_type,
                    'severity': severity,
                    'details': sanitized_details,
                    'timestamp': datetime.now(timezone.utc).isoformat()
                }
            )
    
    def test_production_logging():
        """测试生产环境日志配置"""
        print("\n--- 测试生产环境日志配置 ---")
        
        # 设置生产环境日志
        config = ProductionLogConfig(
            app_name="myapp",
            log_dir="logs/production",
            log_level="INFO",
            max_bytes=10*1024*1024,  # 10MB
            backup_count=5
        )
        
        logger = config.setup_logging()
        secure_logger = SecureLogger(logger)
        
        # 测试普通日志
        logger.info("应用启动", extra={'version': '1.0.0', 'environment': 'production'})
        
        # 测试用户操作审计
        secure_logger.log_user_action(
            user_id="user_123",
            action="login",
            ip_address="192.168.1.100",
            user_agent="Mozilla/5.0",
            password="secret123",  # 这会被清理
            token="abc123def456"     # 这也会被清理
        )
        
        # 测试性能日志
        secure_logger.log_performance(
            operation="database_query",
            duration=0.15,
            query_type="SELECT",
            rows_returned=100,
            cache_hit=False
        )
        
        # 测试安全事件
        secure_logger.log_security_event(
            event_type="failed_login",
            severity="medium",
            user_id="user_456",
            ip_address="192.168.1.200",
            attempts=5,
            password_attempt="wrongpass123"  # 这会被清理
        )
        
        # 测试异常记录
        try:
            # 模拟业务异常
            raise ValueError("无效的用户输入")
        except Exception:
            logger.exception(
                "业务逻辑异常",
                extra={
                    'operation': 'process_user_data',
                    'user_id': 'user_789',
                    'input_data': {'name': 'Alice', 'password': 'secret456'}  # password会在其他地方被清理
                }
            )
        
        # 测试批量日志（触发轮转）
        for i in range(100):
            logger.info(f"批量处理记录 {i+1}/100", extra={'batch_id': 'batch_001', 'record_id': i+1})
        
        print("✓ 生产环境日志测试完成")
        print(f"日志文件位置: {config.log_dir}")
    
    test_production_logging()


def main():
    """主函数"""
    print("Python异常处理 - 异常日志记录")
    print("=" * 60)
    
    try:
        # 演示各种日志记录技术
        demonstrate_basic_logging()
        demonstrate_advanced_logging_configuration()
        demonstrate_structured_logging()
        demonstrate_logging_decorators()
        demonstrate_production_logging()
        
        print_section("学习总结")
        print("""
        异常日志记录要点：
        
        1. 基本日志记录：
           - 使用logging模块记录异常
           - logger.exception()自动记录堆栈跟踪
           - 不同的日志级别和格式
        
        2. 高级日志配置：
           - 多个处理器和格式化器
           - 日志轮转和压缩
           - 自定义过滤器和格式化器
        
        3. 结构化日志：
           - JSON格式的日志记录
           - 丰富的上下文信息
           - 便于自动化分析
        
        4. 日志装饰器：
           - 自动记录函数调用
           - 异常自动记录
           - 性能监控集成
        
        5. 生产环境配置：
           - 高性能日志配置
           - 安全性和隐私保护
           - 审计和监控集成
        
        最佳实践：
        - 合理设置日志级别
        - 保护敏感信息
        - 定期清理日志文件
        - 集成监控和告警
        
        下一步学习：
        - 09_best_practices.py: 异常处理最佳实践
        """)
        
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"程序执行过程中发生错误: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()