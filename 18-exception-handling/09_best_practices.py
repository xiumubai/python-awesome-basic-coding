#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
异常处理最佳实践

本文件详细演示Python异常处理的最佳实践，包括异常处理原则、
设计模式、性能优化、代码组织、测试策略等综合应用技术。

学习目标：
1. 掌握异常处理的设计原则
2. 学会异常处理的设计模式
3. 了解异常处理的性能考虑
4. 掌握异常处理的测试方法
5. 学会在实际项目中应用最佳实践
"""

import sys
import os
import time
import logging
import traceback
import functools
import threading
import asyncio
from abc import ABC, abstractmethod
from contextlib import contextmanager, suppress
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Union, Callable, Type, TypeVar, Generic
from collections import defaultdict
import json
import unittest
from unittest.mock import Mock, patch
import warnings


def print_section(title: str) -> None:
    """打印章节标题"""
    print("\n" + "=" * 60)
    print(f"{title}")
    print("=" * 60)


def demonstrate_exception_handling_principles():
    """演示异常处理原则"""
    print_section("1. 异常处理原则")
    
    print("异常处理的核心原则：")
    print("1. 具体性原则：捕获具体的异常类型")
    print("2. 就近处理原则：在合适的层级处理异常")
    print("3. 失败快速原则：尽早发现和报告错误")
    print("4. 资源清理原则：确保资源得到正确释放")
    print("5. 信息保留原则：保留足够的错误信息")
    
    # 原则1：具体性原则
    def demonstrate_specificity_principle():
        """演示具体性原则"""
        print("\n--- 具体性原则 ---")
        
        def bad_exception_handling(data: List[str]) -> List[int]:
            """不好的异常处理：捕获过于宽泛"""
            result = []
            for item in data:
                try:
                    result.append(int(item))
                except Exception:  # 太宽泛
                    print(f"转换失败: {item}")
                    continue
            return result
        
        def good_exception_handling(data: List[str]) -> List[int]:
            """好的异常处理：捕获具体异常"""
            result = []
            for item in data:
                try:
                    result.append(int(item))
                except ValueError as e:
                    print(f"数值转换错误 '{item}': {e}")
                    continue
                except OverflowError as e:
                    print(f"数值溢出 '{item}': {e}")
                    continue
            return result
        
        # 测试数据
        test_data = ["123", "abc", "456", "12.34", "789"]
        
        print("不好的处理方式:")
        result1 = bad_exception_handling(test_data)
        print(f"结果: {result1}")
        
        print("\n好的处理方式:")
        result2 = good_exception_handling(test_data)
        print(f"结果: {result2}")
    
    # 原则2：就近处理原则
    def demonstrate_proximity_principle():
        """演示就近处理原则"""
        print("\n--- 就近处理原则 ---")
        
        class DataProcessor:
            """数据处理器"""
            
            def __init__(self):
                self.logger = logging.getLogger(self.__class__.__name__)
            
            def validate_data(self, data: Any) -> bool:
                """验证数据 - 在这里处理验证异常"""
                try:
                    if not isinstance(data, (int, float)):
                        raise TypeError(f"期望数字类型，得到 {type(data).__name__}")
                    if data < 0:
                        raise ValueError("数值不能为负数")
                    return True
                except (TypeError, ValueError) as e:
                    # 在验证层处理验证异常
                    self.logger.warning(f"数据验证失败: {e}")
                    return False
            
            def process_item(self, item: Any) -> Optional[float]:
                """处理单个项目"""
                if not self.validate_data(item):
                    return None
                
                try:
                    # 业务逻辑
                    result = float(item) * 2
                    return result
                except Exception as e:
                    # 在处理层记录异常但不处理
                    self.logger.error(f"处理项目失败 {item}: {e}")
                    raise  # 重新抛出，让上层决定如何处理
            
            def process_batch(self, items: List[Any]) -> List[float]:
                """批量处理 - 在这里处理批量异常"""
                results = []
                failed_count = 0
                
                for i, item in enumerate(items):
                    try:
                        result = self.process_item(item)
                        if result is not None:
                            results.append(result)
                    except Exception as e:
                        # 在批量处理层决定如何处理异常
                        failed_count += 1
                        self.logger.error(f"批量处理第{i+1}项失败: {e}")
                        
                        # 根据失败率决定是否继续
                        failure_rate = failed_count / (i + 1)
                        if failure_rate > 0.5:  # 失败率超过50%
                            raise RuntimeError(f"批量处理失败率过高: {failure_rate:.2%}")
                
                return results
        
        # 测试就近处理原则
        processor = DataProcessor()
        test_items = [10, "abc", 20, -5, 30, "def", 40]
        
        try:
            results = processor.process_batch(test_items)
            print(f"处理结果: {results}")
        except RuntimeError as e:
            print(f"批量处理失败: {e}")
    
    # 原则3：失败快速原则
    def demonstrate_fail_fast_principle():
        """演示失败快速原则"""
        print("\n--- 失败快速原则 ---")
        
        class ConfigurationManager:
            """配置管理器"""
            
            def __init__(self, config_file: str):
                self.config_file = config_file
                self.config = {}
                self._load_config()
                self._validate_config()  # 启动时立即验证
            
            def _load_config(self):
                """加载配置"""
                try:
                    # 模拟配置加载
                    self.config = {
                        "database_url": "postgresql://localhost:5432/mydb",
                        "api_key": "secret_key_123",
                        "max_connections": 100,
                        "timeout": 30
                    }
                except Exception as e:
                    raise RuntimeError(f"无法加载配置文件 {self.config_file}: {e}")
            
            def _validate_config(self):
                """验证配置 - 失败快速"""
                required_keys = ["database_url", "api_key", "max_connections"]
                
                for key in required_keys:
                    if key not in self.config:
                        raise ValueError(f"缺少必需的配置项: {key}")
                
                # 验证数据类型和范围
                if not isinstance(self.config["max_connections"], int):
                    raise TypeError("max_connections必须是整数")
                
                if self.config["max_connections"] <= 0:
                    raise ValueError("max_connections必须大于0")
                
                if len(self.config["api_key"]) < 10:
                    raise ValueError("api_key长度不足")
                
                print("✓ 配置验证通过")
            
            def get(self, key: str, default=None):
                """获取配置值"""
                return self.config.get(key, default)
        
        # 测试失败快速原则
        try:
            config = ConfigurationManager("config.json")
            print(f"数据库URL: {config.get('database_url')}")
            print(f"最大连接数: {config.get('max_connections')}")
        except (ValueError, TypeError, RuntimeError) as e:
            print(f"配置初始化失败: {e}")
    
    # 执行演示
    demonstrate_specificity_principle()
    demonstrate_proximity_principle()
    demonstrate_fail_fast_principle()


def demonstrate_exception_design_patterns():
    """演示异常处理设计模式"""
    print_section("2. 异常处理设计模式")
    
    print("常用的异常处理设计模式：")
    print("1. 异常转换模式")
    print("2. 异常聚合模式")
    print("3. 重试模式")
    print("4. 断路器模式")
    print("5. 异常装饰器模式")
    
    # 模式1：异常转换模式
    def demonstrate_exception_translation_pattern():
        """演示异常转换模式"""
        print("\n--- 异常转换模式 ---")
        
        class DatabaseError(Exception):
            """数据库异常"""
            pass
        
        class UserNotFoundError(DatabaseError):
            """用户未找到异常"""
            pass
        
        class DatabaseRepository:
            """数据库仓储层"""
            
            def find_user_by_id(self, user_id: int) -> Dict[str, Any]:
                """根据ID查找用户"""
                try:
                    # 模拟数据库操作
                    if user_id <= 0:
                        raise ValueError("无效的用户ID")
                    if user_id == 999:
                        raise ConnectionError("数据库连接失败")
                    if user_id == 404:
                        return None  # 用户不存在
                    
                    return {"id": user_id, "name": f"User{user_id}", "email": f"user{user_id}@example.com"}
                    
                except ValueError as e:
                    # 转换为业务异常
                    raise UserNotFoundError(f"用户查找失败: {e}") from e
                except ConnectionError as e:
                    # 转换为数据库异常
                    raise DatabaseError(f"数据库操作失败: {e}") from e
        
        class UserService:
            """用户服务层"""
            
            def __init__(self):
                self.repository = DatabaseRepository()
            
            def get_user_profile(self, user_id: int) -> Dict[str, Any]:
                """获取用户资料"""
                try:
                    user = self.repository.find_user_by_id(user_id)
                    if user is None:
                        raise UserNotFoundError(f"用户 {user_id} 不存在")
                    return user
                except DatabaseError:
                    # 数据库异常直接传播
                    raise
                except Exception as e:
                    # 其他异常转换为服务异常
                    raise RuntimeError(f"用户服务异常: {e}") from e
        
        # 测试异常转换模式
        service = UserService()
        
        test_cases = [123, -1, 999, 404]
        for user_id in test_cases:
            try:
                user = service.get_user_profile(user_id)
                print(f"用户 {user_id}: {user['name']}")
            except UserNotFoundError as e:
                print(f"用户未找到: {e}")
            except DatabaseError as e:
                print(f"数据库错误: {e}")
            except Exception as e:
                print(f"服务错误: {e}")
    
    # 模式2：异常聚合模式
    def demonstrate_exception_aggregation_pattern():
        """演示异常聚合模式"""
        print("\n--- 异常聚合模式 ---")
        
        class ValidationError(Exception):
            """验证异常"""
            
            def __init__(self, errors: List[str]):
                self.errors = errors
                super().__init__(f"验证失败: {len(errors)} 个错误")
            
            def __str__(self):
                return f"验证失败:\n" + "\n".join(f"- {error}" for error in self.errors)
        
        class UserValidator:
            """用户验证器"""
            
            def validate_user_data(self, user_data: Dict[str, Any]) -> None:
                """验证用户数据 - 收集所有错误"""
                errors = []
                
                # 验证姓名
                name = user_data.get("name", "")
                if not name:
                    errors.append("姓名不能为空")
                elif len(name) < 2:
                    errors.append("姓名长度至少2个字符")
                elif len(name) > 50:
                    errors.append("姓名长度不能超过50个字符")
                
                # 验证邮箱
                email = user_data.get("email", "")
                if not email:
                    errors.append("邮箱不能为空")
                elif "@" not in email:
                    errors.append("邮箱格式无效")
                elif len(email) > 100:
                    errors.append("邮箱长度不能超过100个字符")
                
                # 验证年龄
                age = user_data.get("age")
                if age is None:
                    errors.append("年龄不能为空")
                elif not isinstance(age, int):
                    errors.append("年龄必须是整数")
                elif age < 0:
                    errors.append("年龄不能为负数")
                elif age > 150:
                    errors.append("年龄不能超过150")
                
                # 验证密码
                password = user_data.get("password", "")
                if not password:
                    errors.append("密码不能为空")
                elif len(password) < 8:
                    errors.append("密码长度至少8个字符")
                elif not any(c.isdigit() for c in password):
                    errors.append("密码必须包含数字")
                elif not any(c.isupper() for c in password):
                    errors.append("密码必须包含大写字母")
                
                # 如果有错误，抛出聚合异常
                if errors:
                    raise ValidationError(errors)
        
        # 测试异常聚合模式
        validator = UserValidator()
        
        test_users = [
            {"name": "Alice", "email": "alice@example.com", "age": 25, "password": "Password123"},
            {"name": "", "email": "invalid-email", "age": -5, "password": "weak"},
            {"name": "B", "email": "b@example.com", "age": "not_number", "password": "NoDigits"}
        ]
        
        for i, user_data in enumerate(test_users, 1):
            try:
                validator.validate_user_data(user_data)
                print(f"用户 {i}: 验证通过")
            except ValidationError as e:
                print(f"用户 {i}: {e}")
    
    # 模式3：重试模式
    def demonstrate_retry_pattern():
        """演示重试模式"""
        print("\n--- 重试模式 ---")
        
        def retry(max_attempts: int = 3, delay: float = 1.0, 
                 backoff: float = 2.0, exceptions: tuple = (Exception,)):
            """重试装饰器"""
            def decorator(func):
                @functools.wraps(func)
                def wrapper(*args, **kwargs):
                    attempt = 0
                    current_delay = delay
                    
                    while attempt < max_attempts:
                        try:
                            return func(*args, **kwargs)
                        except exceptions as e:
                            attempt += 1
                            if attempt >= max_attempts:
                                print(f"重试 {max_attempts} 次后仍然失败")
                                raise
                            
                            print(f"第 {attempt} 次尝试失败: {e}，{current_delay}秒后重试...")
                            time.sleep(current_delay)
                            current_delay *= backoff
                    
                    return None
                return wrapper
            return decorator
        
        class NetworkService:
            """网络服务"""
            
            def __init__(self):
                self.attempt_count = 0
            
            @retry(max_attempts=3, delay=0.5, exceptions=(ConnectionError, TimeoutError))
            def fetch_data(self, url: str) -> Dict[str, Any]:
                """获取数据 - 可能失败的网络操作"""
                self.attempt_count += 1
                
                # 模拟网络请求
                if self.attempt_count <= 2:
                    if self.attempt_count == 1:
                        raise ConnectionError("网络连接失败")
                    else:
                        raise TimeoutError("请求超时")
                
                # 第三次成功
                return {"data": "成功获取的数据", "timestamp": time.time()}
        
        # 测试重试模式
        service = NetworkService()
        try:
            result = service.fetch_data("https://api.example.com/data")
            print(f"获取数据成功: {result['data']}")
        except Exception as e:
            print(f"最终失败: {e}")
    
    # 模式4：断路器模式
    def demonstrate_circuit_breaker_pattern():
        """演示断路器模式"""
        print("\n--- 断路器模式 ---")
        
        class CircuitBreakerState(Enum):
            CLOSED = "closed"      # 正常状态
            OPEN = "open"          # 断开状态
            HALF_OPEN = "half_open" # 半开状态
        
        class CircuitBreaker:
            """断路器"""
            
            def __init__(self, failure_threshold: int = 5, 
                        recovery_timeout: float = 60.0,
                        expected_exception: Type[Exception] = Exception):
                self.failure_threshold = failure_threshold
                self.recovery_timeout = recovery_timeout
                self.expected_exception = expected_exception
                
                self.failure_count = 0
                self.last_failure_time = None
                self.state = CircuitBreakerState.CLOSED
            
            def __call__(self, func):
                @functools.wraps(func)
                def wrapper(*args, **kwargs):
                    if self.state == CircuitBreakerState.OPEN:
                        if self._should_attempt_reset():
                            self.state = CircuitBreakerState.HALF_OPEN
                            print("断路器进入半开状态")
                        else:
                            raise RuntimeError("断路器开启，服务不可用")
                    
                    try:
                        result = func(*args, **kwargs)
                        self._on_success()
                        return result
                    except self.expected_exception as e:
                        self._on_failure()
                        raise
                
                return wrapper
            
            def _should_attempt_reset(self) -> bool:
                """是否应该尝试重置"""
                return (time.time() - self.last_failure_time) >= self.recovery_timeout
            
            def _on_success(self):
                """成功时的处理"""
                self.failure_count = 0
                if self.state == CircuitBreakerState.HALF_OPEN:
                    self.state = CircuitBreakerState.CLOSED
                    print("断路器重置为关闭状态")
            
            def _on_failure(self):
                """失败时的处理"""
                self.failure_count += 1
                self.last_failure_time = time.time()
                
                if self.failure_count >= self.failure_threshold:
                    self.state = CircuitBreakerState.OPEN
                    print(f"断路器开启（失败次数: {self.failure_count}）")
        
        class ExternalService:
            """外部服务"""
            
            def __init__(self):
                self.call_count = 0
            
            @CircuitBreaker(failure_threshold=3, recovery_timeout=2.0, 
                          expected_exception=ConnectionError)
            def call_external_api(self) -> str:
                """调用外部API"""
                self.call_count += 1
                
                # 模拟前几次调用失败
                if self.call_count <= 5:
                    raise ConnectionError(f"外部服务调用失败 (第{self.call_count}次)")
                
                return f"外部服务响应 (第{self.call_count}次调用)"
        
        # 测试断路器模式
        service = ExternalService()
        
        for i in range(10):
            try:
                result = service.call_external_api()
                print(f"调用 {i+1}: {result}")
            except (ConnectionError, RuntimeError) as e:
                print(f"调用 {i+1}: 失败 - {e}")
            
            time.sleep(0.5)
    
    # 执行演示
    demonstrate_exception_translation_pattern()
    demonstrate_exception_aggregation_pattern()
    demonstrate_retry_pattern()
    demonstrate_circuit_breaker_pattern()


def demonstrate_performance_considerations():
    """演示性能考虑"""
    print_section("3. 性能考虑")
    
    print("异常处理的性能要点：")
    print("1. 异常的性能开销")
    print("2. 避免异常用于控制流")
    print("3. 异常缓存和重用")
    print("4. 异步异常处理")
    
    def demonstrate_exception_performance():
        """演示异常性能"""
        print("\n--- 异常性能测试 ---")
        
        def test_exception_overhead():
            """测试异常开销"""
            iterations = 100000
            
            # 测试正常流程
            start_time = time.time()
            for i in range(iterations):
                try:
                    result = i * 2
                except:
                    pass
            normal_time = time.time() - start_time
            
            # 测试异常流程
            start_time = time.time()
            for i in range(iterations):
                try:
                    if i % 2 == 0:
                        raise ValueError("测试异常")
                except ValueError:
                    pass
            exception_time = time.time() - start_time
            
            print(f"正常流程时间: {normal_time:.4f}秒")
            print(f"异常流程时间: {exception_time:.4f}秒")
            print(f"异常开销: {exception_time/normal_time:.2f}倍")
        
        def demonstrate_control_flow_antipattern():
            """演示控制流反模式"""
            print("\n不好的做法 - 用异常控制流程:")
            
            def bad_find_item(items: List[str], target: str) -> int:
                """不好的查找方法"""
                try:
                    for i, item in enumerate(items):
                        if item == target:
                            raise StopIteration(i)  # 用异常返回结果
                except StopIteration as e:
                    return e.value
                return -1
            
            def good_find_item(items: List[str], target: str) -> int:
                """好的查找方法"""
                for i, item in enumerate(items):
                    if item == target:
                        return i
                return -1
            
            test_items = ["apple", "banana", "cherry"] * 1000
            target = "cherry"
            
            # 测试性能
            start_time = time.time()
            for _ in range(1000):
                bad_find_item(test_items, target)
            bad_time = time.time() - start_time
            
            start_time = time.time()
            for _ in range(1000):
                good_find_item(test_items, target)
            good_time = time.time() - start_time
            
            print(f"异常控制流时间: {bad_time:.4f}秒")
            print(f"正常控制流时间: {good_time:.4f}秒")
            print(f"性能差异: {bad_time/good_time:.2f}倍")
        
        test_exception_overhead()
        demonstrate_control_flow_antipattern()
    
    def demonstrate_exception_caching():
        """演示异常缓存"""
        print("\n--- 异常缓存和重用 ---")
        
        class CachedExceptionFactory:
            """缓存异常工厂"""
            
            def __init__(self):
                self._cache = {}
            
            def get_exception(self, exception_type: Type[Exception], 
                           message: str) -> Exception:
                """获取缓存的异常实例"""
                cache_key = (exception_type, message)
                
                if cache_key not in self._cache:
                    self._cache[cache_key] = exception_type(message)
                
                return self._cache[cache_key]
            
            def clear_cache(self):
                """清除缓存"""
                self._cache.clear()
        
        class ValidationService:
            """验证服务"""
            
            def __init__(self):
                self.exception_factory = CachedExceptionFactory()
            
            def validate_email(self, email: str) -> None:
                """验证邮箱"""
                if not email:
                    raise self.exception_factory.get_exception(
                        ValueError, "邮箱不能为空"
                    )
                
                if "@" not in email:
                    raise self.exception_factory.get_exception(
                        ValueError, "邮箱格式无效"
                    )
            
            def validate_age(self, age: int) -> None:
                """验证年龄"""
                if age < 0:
                    raise self.exception_factory.get_exception(
                        ValueError, "年龄不能为负数"
                    )
                
                if age > 150:
                    raise self.exception_factory.get_exception(
                        ValueError, "年龄不能超过150"
                    )
        
        # 测试异常缓存
        service = ValidationService()
        
        test_cases = [
            ("", "invalid-email", -5),
            ("", "another-invalid", 200),
            ("", "@invalid", -10)
        ]
        
        for emails, invalid_email, invalid_age in test_cases:
            try:
                service.validate_email(emails)
            except ValueError as e:
                print(f"邮箱验证失败: {e} (异常ID: {id(e)})")
            
            try:
                service.validate_age(invalid_age)
            except ValueError as e:
                print(f"年龄验证失败: {e} (异常ID: {id(e)})")
        
        print("注意：相同消息的异常实例ID相同，说明使用了缓存")
    
    def demonstrate_async_exception_handling():
        """演示异步异常处理"""
        print("\n--- 异步异常处理 ---")
        
        async def async_operation(operation_id: int, should_fail: bool = False) -> str:
            """异步操作"""
            await asyncio.sleep(0.1)  # 模拟异步操作
            
            if should_fail:
                raise RuntimeError(f"操作 {operation_id} 失败")
            
            return f"操作 {operation_id} 完成"
        
        async def process_with_exception_handling():
            """带异常处理的异步处理"""
            tasks = []
            
            # 创建多个异步任务
            for i in range(5):
                should_fail = i % 2 == 0  # 偶数任务失败
                task = async_operation(i, should_fail)
                tasks.append(task)
            
            # 并发执行并处理异常
            results = []
            for i, task in enumerate(tasks):
                try:
                    result = await task
                    results.append(result)
                    print(f"✓ {result}")
                except RuntimeError as e:
                    print(f"✗ {e}")
                    results.append(None)
            
            return results
        
        async def process_with_gather():
            """使用gather处理异步异常"""
            tasks = []
            
            for i in range(5):
                should_fail = i == 2  # 只有任务2失败
                task = async_operation(i, should_fail)
                tasks.append(task)
            
            try:
                results = await asyncio.gather(*tasks, return_exceptions=True)
                
                for i, result in enumerate(results):
                    if isinstance(result, Exception):
                        print(f"任务 {i} 失败: {result}")
                    else:
                        print(f"任务 {i} 成功: {result}")
                
                return results
            except Exception as e:
                print(f"批量处理失败: {e}")
                return []
        
        # 运行异步测试
        print("逐个处理异步异常:")
        asyncio.run(process_with_exception_handling())
        
        print("\n使用gather处理异步异常:")
        asyncio.run(process_with_gather())
    
    # 执行演示
    demonstrate_exception_performance()
    demonstrate_exception_caching()
    demonstrate_async_exception_handling()


def demonstrate_testing_exceptions():
    """演示异常测试"""
    print_section("4. 异常测试")
    
    print("异常测试的要点：")
    print("1. 测试异常是否正确抛出")
    print("2. 测试异常消息和类型")
    print("3. 测试异常处理逻辑")
    print("4. 模拟异常场景")
    
    class Calculator:
        """计算器类 - 用于测试"""
        
        def divide(self, a: float, b: float) -> float:
            """除法运算"""
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError("参数必须是数字")
            
            if b == 0:
                raise ZeroDivisionError("除数不能为零")
            
            return a / b
        
        def factorial(self, n: int) -> int:
            """计算阶乘"""
            if not isinstance(n, int):
                raise TypeError("参数必须是整数")
            
            if n < 0:
                raise ValueError("参数不能为负数")
            
            if n > 100:
                raise OverflowError("参数过大")
            
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result
    
    class TestCalculator(unittest.TestCase):
        """计算器测试类"""
        
        def setUp(self):
            """测试设置"""
            self.calculator = Calculator()
        
        def test_divide_normal(self):
            """测试正常除法"""
            result = self.calculator.divide(10, 2)
            self.assertEqual(result, 5.0)
        
        def test_divide_zero_error(self):
            """测试除零异常"""
            with self.assertRaises(ZeroDivisionError) as context:
                self.calculator.divide(10, 0)
            
            self.assertEqual(str(context.exception), "除数不能为零")
        
        def test_divide_type_error(self):
            """测试类型异常"""
            with self.assertRaises(TypeError) as context:
                self.calculator.divide("10", 2)
            
            self.assertIn("参数必须是数字", str(context.exception))
        
        def test_factorial_normal(self):
            """测试正常阶乘"""
            self.assertEqual(self.calculator.factorial(5), 120)
            self.assertEqual(self.calculator.factorial(0), 1)
        
        def test_factorial_type_error(self):
            """测试阶乘类型异常"""
            with self.assertRaises(TypeError):
                self.calculator.factorial(5.5)
        
        def test_factorial_value_error(self):
            """测试阶乘值异常"""
            with self.assertRaises(ValueError):
                self.calculator.factorial(-1)
        
        def test_factorial_overflow_error(self):
            """测试阶乘溢出异常"""
            with self.assertRaises(OverflowError):
                self.calculator.factorial(101)
        
        def test_multiple_exceptions(self):
            """测试多种异常"""
            test_cases = [
                ("string", 2, TypeError),
                (10, 0, ZeroDivisionError),
                (10, "string", TypeError)
            ]
            
            for a, b, expected_exception in test_cases:
                with self.subTest(a=a, b=b):
                    with self.assertRaises(expected_exception):
                        self.calculator.divide(a, b)
    
    class FileProcessor:
        """文件处理器 - 用于测试模拟"""
        
        def __init__(self, file_system):
            self.file_system = file_system
        
        def read_config(self, filename: str) -> Dict[str, Any]:
            """读取配置文件"""
            try:
                content = self.file_system.read_file(filename)
                return json.loads(content)
            except FileNotFoundError:
                raise FileNotFoundError(f"配置文件 {filename} 不存在")
            except json.JSONDecodeError as e:
                raise ValueError(f"配置文件格式错误: {e}")
    
    class TestFileProcessorWithMocks(unittest.TestCase):
        """使用模拟的文件处理器测试"""
        
        def setUp(self):
            """测试设置"""
            self.mock_file_system = Mock()
            self.processor = FileProcessor(self.mock_file_system)
        
        def test_read_config_success(self):
            """测试成功读取配置"""
            # 设置模拟返回值
            self.mock_file_system.read_file.return_value = '{"key": "value"}'
            
            result = self.processor.read_config("config.json")
            
            self.assertEqual(result, {"key": "value"})
            self.mock_file_system.read_file.assert_called_once_with("config.json")
        
        def test_read_config_file_not_found(self):
            """测试文件不存在异常"""
            # 设置模拟抛出异常
            self.mock_file_system.read_file.side_effect = FileNotFoundError()
            
            with self.assertRaises(FileNotFoundError) as context:
                self.processor.read_config("missing.json")
            
            self.assertIn("missing.json", str(context.exception))
        
        def test_read_config_invalid_json(self):
            """测试JSON格式错误"""
            # 设置模拟返回无效JSON
            self.mock_file_system.read_file.return_value = '{invalid json}'
            
            with self.assertRaises(ValueError) as context:
                self.processor.read_config("invalid.json")
            
            self.assertIn("配置文件格式错误", str(context.exception))
    
    def run_exception_tests():
        """运行异常测试"""
        print("\n--- 运行异常测试 ---")
        
        # 创建测试套件
        suite = unittest.TestSuite()
        
        # 添加测试
        suite.addTest(unittest.makeSuite(TestCalculator))
        suite.addTest(unittest.makeSuite(TestFileProcessorWithMocks))
        
        # 运行测试
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        print(f"\n测试结果:")
        print(f"运行测试: {result.testsRun}")
        print(f"失败: {len(result.failures)}")
        print(f"错误: {len(result.errors)}")
        print(f"成功: {result.testsRun - len(result.failures) - len(result.errors)}")
    
    # 执行测试
    run_exception_tests()


def demonstrate_real_world_examples():
    """演示实际应用示例"""
    print_section("5. 实际应用示例")
    
    print("实际项目中的异常处理应用：")
    print("1. Web API异常处理")
    print("2. 数据库操作异常处理")
    print("3. 文件处理异常处理")
    print("4. 网络请求异常处理")
    
    # 示例1：Web API异常处理
    def demonstrate_web_api_exception_handling():
        """演示Web API异常处理"""
        print("\n--- Web API异常处理 ---")
        
        class APIError(Exception):
            """API异常基类"""
            
            def __init__(self, message: str, status_code: int = 500, 
                        error_code: str = None):
                super().__init__(message)
                self.status_code = status_code
                self.error_code = error_code
        
        class ValidationError(APIError):
            """验证异常"""
            
            def __init__(self, message: str, field: str = None):
                super().__init__(message, 400, "VALIDATION_ERROR")
                self.field = field
        
        class NotFoundError(APIError):
            """资源未找到异常"""
            
            def __init__(self, resource: str, resource_id: Any):
                message = f"{resource} {resource_id} 不存在"
                super().__init__(message, 404, "NOT_FOUND")
                self.resource = resource
                self.resource_id = resource_id
        
        class UserController:
            """用户控制器"""
            
            def __init__(self):
                self.users = {
                    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
                    2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
                }
            
            def get_user(self, user_id: int) -> Dict[str, Any]:
                """获取用户"""
                try:
                    if not isinstance(user_id, int) or user_id <= 0:
                        raise ValidationError("用户ID必须是正整数", "user_id")
                    
                    if user_id not in self.users:
                        raise NotFoundError("用户", user_id)
                    
                    return self.users[user_id]
                    
                except (ValidationError, NotFoundError):
                    # 业务异常直接传播
                    raise
                except Exception as e:
                    # 其他异常转换为内部服务器错误
                    raise APIError(f"内部服务器错误: {e}", 500, "INTERNAL_ERROR") from e
            
            def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
                """创建用户"""
                try:
                    # 验证必需字段
                    required_fields = ["name", "email"]
                    for field in required_fields:
                        if field not in user_data or not user_data[field]:
                            raise ValidationError(f"{field}是必需的", field)
                    
                    # 验证邮箱格式
                    email = user_data["email"]
                    if "@" not in email:
                        raise ValidationError("邮箱格式无效", "email")
                    
                    # 检查邮箱是否已存在
                    for user in self.users.values():
                        if user["email"] == email:
                            raise ValidationError("邮箱已存在", "email")
                    
                    # 创建用户
                    new_id = max(self.users.keys()) + 1
                    new_user = {
                        "id": new_id,
                        "name": user_data["name"],
                        "email": user_data["email"]
                    }
                    self.users[new_id] = new_user
                    
                    return new_user
                    
                except ValidationError:
                    raise
                except Exception as e:
                    raise APIError(f"创建用户失败: {e}", 500, "CREATION_ERROR") from e
        
        def handle_api_request(controller_method, *args, **kwargs) -> Dict[str, Any]:
            """API请求处理器"""
            try:
                result = controller_method(*args, **kwargs)
                return {
                    "success": True,
                    "data": result,
                    "error": None
                }
            except APIError as e:
                return {
                    "success": False,
                    "data": None,
                    "error": {
                        "message": str(e),
                        "status_code": e.status_code,
                        "error_code": e.error_code
                    }
                }
            except Exception as e:
                return {
                    "success": False,
                    "data": None,
                    "error": {
                        "message": "内部服务器错误",
                        "status_code": 500,
                        "error_code": "UNKNOWN_ERROR"
                    }
                }
        
        # 测试Web API异常处理
        controller = UserController()
        
        # 测试获取用户
        test_cases = [
            (1, "正常获取"),
            (999, "用户不存在"),
            (-1, "无效ID"),
            ("abc", "类型错误")
        ]
        
        for user_id, description in test_cases:
            response = handle_api_request(controller.get_user, user_id)
            print(f"{description}: {response}")
        
        # 测试创建用户
        create_test_cases = [
            ({"name": "Charlie", "email": "charlie@example.com"}, "正常创建"),
            ({"name": "David"}, "缺少邮箱"),
            ({"name": "Eve", "email": "invalid-email"}, "邮箱格式错误"),
            ({"name": "Frank", "email": "alice@example.com"}, "邮箱已存在")
        ]
        
        for user_data, description in create_test_cases:
            response = handle_api_request(controller.create_user, user_data)
            print(f"{description}: {response}")
    
    # 示例2：数据库操作异常处理
    def demonstrate_database_exception_handling():
        """演示数据库操作异常处理"""
        print("\n--- 数据库操作异常处理 ---")
        
        class DatabaseError(Exception):
            """数据库异常"""
            pass
        
        class ConnectionError(DatabaseError):
            """连接异常"""
            pass
        
        class QueryError(DatabaseError):
            """查询异常"""
            pass
        
        class MockDatabase:
            """模拟数据库"""
            
            def __init__(self):
                self.connected = False
                self.query_count = 0
            
            def connect(self):
                """连接数据库"""
                if self.query_count > 5:
                    raise ConnectionError("数据库连接失败")
                self.connected = True
            
            def execute_query(self, query: str) -> List[Dict[str, Any]]:
                """执行查询"""
                if not self.connected:
                    raise ConnectionError("数据库未连接")
                
                self.query_count += 1
                
                if "invalid" in query.lower():
                    raise QueryError(f"无效查询: {query}")
                
                if self.query_count % 3 == 0:
                    raise ConnectionError("连接超时")
                
                # 模拟查询结果
                return [{"id": 1, "name": "测试数据"}]
            
            def close(self):
                """关闭连接"""
                self.connected = False
        
        class DatabaseManager:
            """数据库管理器"""
            
            def __init__(self, max_retries: int = 3):
                self.db = MockDatabase()
                self.max_retries = max_retries
                self.logger = logging.getLogger(self.__class__.__name__)
            
            @contextmanager
            def get_connection(self):
                """获取数据库连接上下文管理器"""
                try:
                    self.db.connect()
                    yield self.db
                except Exception as e:
                    # 在上下文管理器中不处理重试逻辑
                    raise
                finally:
                    if self.db.connected:
                        self.db.close()
            
            def execute_with_retry(self, query: str) -> List[Dict[str, Any]]:
                """执行查询并重试"""
                retry_count = 0
                
                while retry_count < self.max_retries:
                    try:
                        with self.get_connection() as db:
                            return db.execute_query(query)
                    except ConnectionError as e:
                        retry_count += 1
                        self.logger.warning(f"连接失败 (第{retry_count}次): {e}")
                        
                        if retry_count >= self.max_retries:
                            raise DatabaseError(f"连接重试{self.max_retries}次后失败") from e
                        
                        time.sleep(0.1 * retry_count)  # 指数退避
                    except Exception as e:
                        raise DatabaseError(f"查询执行失败: {e}") from e
                
                raise DatabaseError("未知错误")
        
        # 测试数据库异常处理
        db_manager = DatabaseManager(max_retries=2)
        
        test_queries = [
            "SELECT * FROM users",
            "SELECT * FROM invalid_table",
            "SELECT * FROM products",
            "INVALID QUERY SYNTAX"
        ]
        
        for query in test_queries:
            try:
                result = db_manager.execute_with_retry(query)
                print(f"查询成功: {query} -> {len(result)} 条记录")
            except DatabaseError as e:
                print(f"查询失败: {query} -> {e}")
    
    # 执行演示
    demonstrate_web_api_exception_handling()
    demonstrate_database_exception_handling()


def main():
    """主函数"""
    print("Python异常处理 - 最佳实践")
    print("=" * 60)
    
    try:
        # 演示各种最佳实践
        demonstrate_exception_handling_principles()
        demonstrate_exception_design_patterns()
        demonstrate_performance_considerations()
        demonstrate_testing_exceptions()
        demonstrate_real_world_examples()
        
        print_section("学习总结")
        print("""
        异常处理最佳实践要点：
        
        1. 异常处理原则：
           - 具体性：捕获具体的异常类型
           - 就近处理：在合适的层级处理异常
           - 失败快速：尽早发现和报告错误
           - 资源清理：确保资源得到正确释放
           - 信息保留：保留足够的错误信息
        
        2. 设计模式：
           - 异常转换模式：将底层异常转换为业务异常
           - 异常聚合模式：收集多个验证错误
           - 重试模式：自动重试失败的操作
           - 断路器模式：防止级联失败
           - 装饰器模式：简化异常处理代码
        
        3. 性能考虑：
           - 避免用异常控制程序流程
           - 缓存和重用异常实例
           - 异步异常处理优化
           - 监控异常性能影响
        
        4. 测试策略：
           - 测试异常是否正确抛出
           - 验证异常消息和类型
           - 模拟异常场景
           - 测试异常处理逻辑
        
        5. 实际应用：
           - Web API异常处理架构
           - 数据库操作异常处理
           - 文件和网络异常处理
           - 分布式系统异常处理
        
        核心建议：
        - 异常应该是异常情况，不是正常流程
        - 提供清晰、有用的错误信息
        - 在适当的层级处理异常
        - 确保资源得到正确清理
        - 记录足够的上下文信息
        - 为异常处理编写测试
        
        异常处理是编写健壮Python程序的关键技能！
        """)
        
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"程序执行过程中发生错误: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()